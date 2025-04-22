#!/usr/bin/env python3
"""
s3_codeql.py  –  Figure‑3‑style statistics for Python code

* Reads a directory tree with generated *.py files
  (…/gemini/py/CWE-020/gpt4_CWE-020_1_0.py, …).
* Reads a CSV/TSV with CodeQL findings (columns: filepath, cwe).

Outputs (in --out-dir):
    attempt_counts.csv           – how many files try to generate each CWE
    confusion_<src>.csv          – 10×11 table  (10 CWEs + “Other”)
    heatmap_<src>.png            – Figure‑3‑style heat‑maps
where <src> ∈ {overall, gpt4, codellama, other}.
"""

from __future__ import annotations
import argparse, os, re, sys
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tqdm import tqdm

# --------------------------------------------------------------------------- #
# ONLY THE TEN PYTHON CWEs THAT FIG‑3 SHOWS
CANONICAL_CWES = [
    "CWE-020", "CWE-022", "CWE-078", "CWE-079", "CWE-089",
    "CWE-094", "CWE-117", "CWE-502", "CWE-601", "CWE-611",
]
OTHER_TAG = "Other"

# if filename starts with one of these tokens → “prompt source”
SOURCES = ["gpt4", "codellama"]
# --------------------------------------------------------------------------- #


def infer_source(fname: str) -> str:
    prefix = Path(fname).name.split("_", 1)[0].lower()
    return prefix if prefix in SOURCES else "other"


def discover_files(root: Path) -> pd.DataFrame:
    """Return DataFrame[file, aimed_cwe, source] for *.py under root."""
    rows, patt = [], re.compile(r"(CWE-\d{3})", re.I)
    for f in tqdm(root.rglob("*.py"), desc="Scanning generated files"):
        m = patt.search(str(f))
        if m:
            rows.append(
                dict(
                    file=str(f.resolve()),
                    aimed_cwe=m.group(1).upper(),
                    source=infer_source(f.name),
                )
            )
    return pd.DataFrame(rows)


def read_codeql(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, sep=None, engine="python")
    cols = {c.lower().strip(): c for c in df.columns}
    if "filepath" not in cols or "cwe" not in cols:
        sys.exit("CSV/TSV must contain `filepath` and `cwe` columns.")
    df = df.rename(columns={cols["filepath"]: "filepath", cols["cwe"]: "cwe"})
    df["filepath"] = df["filepath"].apply(lambda p: str(Path(p).resolve()))
    df["cwe"] = df["cwe"].str.upper().str.strip()
    return df[["filepath", "cwe"]]


# --------------------------------------------------------------------------- #
def build_stats(gen: pd.DataFrame, ql: pd.DataFrame):
    detections = ql.groupby("filepath")["cwe"].apply(list).to_dict()

    attempt = defaultdict(lambda: defaultdict(int))
    conf = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    for _, row in gen.iterrows():
        f, aim, src = row["file"], row["aimed_cwe"], row["source"]
        attempt[src][aim] += 1
        for det in detections.get(f, []):
            det_norm = det if det in CANONICAL_CWES else OTHER_TAG
            conf[src][aim][det_norm] += 1
        # file with no findings → nothing adds to confusion (empty column)

    return attempt, conf
# --------------------------------------------------------------------------- #


def save_attempts(attempt, out: Path):
    recs = [
        {"source": s, "aimed_cwe": a, "n_files": n}
        for s, sub in attempt.items()
        for a, n in sub.items()
    ]
    pd.DataFrame(recs).to_csv(out / "attempt_counts.csv", index=False)


def save_confusions(conf, out: Path):
    for src, sub in conf.items():
        df = pd.DataFrame(sub).fillna(0).astype(int).T
        cols = [c for c in CANONICAL_CWES if c in df.columns] + (
            [OTHER_TAG] if OTHER_TAG in df.columns else []
        )
        df = df.reindex(columns=cols).sort_index()
        df.to_csv(out / f"confusion_{src}.csv")


def draw_heatmaps(conf, out: Path):
    def _heat(df: pd.DataFrame, title: str, png: Path):
        plt.figure(figsize=(1.1 + 0.35 * len(df.columns),
                           0.9 + 0.35 * len(df.index)))
        sns.heatmap(df, annot=True, fmt="d", cmap="viridis",
                    cbar_kws={"label": "# vulnerable files"},
                    linewidths=.4, linecolor="white")
        plt.title(title, fontsize=12, weight="bold")
        plt.xlabel("Detected CWE")
        plt.ylabel("Aimed CWE")
        plt.tight_layout()
        plt.savefig(png, dpi=300)
        plt.close()

    # merge all sources → overall
    overall = defaultdict(lambda: defaultdict(int))
    for src in conf:
        for aim in conf[src]:
            for det, n in conf[src][aim].items():
                overall[aim][det] += n
    conf["overall"] = overall

    for src, sub in conf.items():
        df = pd.DataFrame(sub).fillna(0).astype(int).T
        cols = [c for c in CANONICAL_CWES if c in df.columns]
        if OTHER_TAG in df.columns:
            cols += [OTHER_TAG]
        df = df.reindex(columns=cols).sort_index()
        _heat(df, f"Detected vs Aimed CWE  ({src})", out / f"heatmap_{src}.png")


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generated-root", required=True, type=Path,
                    help="Root directory containing generated *.py files")
    ap.add_argument("--codeql-csv", required=True, type=Path,
                    help="CSV/TSV with CodeQL results (filepath, cwe)")
    ap.add_argument("--out-dir", default=Path("out_stats"), type=Path)
    args = ap.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)

    print("→ Discovering generated files")
    gen_df = discover_files(args.generated_root)

    print("→ Reading CodeQL findings")
    ql_df = read_codeql(args.codeql_csv)

    print("→ Building statistics")
    attempt, conf = build_stats(gen_df, ql_df)

    print("→ Saving CSV tables")
    save_attempts(attempt, args.out_dir)
    save_confusions(conf, args.out_dir)

    print("→ Drawing heat‑maps")
    draw_heatmaps(conf, args.out_dir)

    print("✓ All done – results in", args.out_dir.resolve())


if __name__ == "__main__":
    main()
