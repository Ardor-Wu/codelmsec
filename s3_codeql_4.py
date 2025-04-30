#!/usr/bin/env python3
"""
scan_cwes.py – Extract fenced Python code from generated‑code files and
run CodeQL CWE queries on each snippet.

Requirements
------------
* CodeQL CLI installed at --codeql (default: /scratch/qilong3/codeql)
* Python ≥3.8
"""
import argparse, pathlib, re, shutil, subprocess, sys, tempfile, csv, uuid

FENCE_RX = re.compile(r"```python(.*?)```", re.S)

def extract_snippets(path: pathlib.Path) -> list[str]:
    """Return all fenced Python snippets from *path* (may be empty)."""
    text = path.read_text(errors="ignore")
    return [m.group(1).strip() for m in FENCE_RX.finditer(text)]

def build_db(codeql: pathlib.Path, snippet: str, tmpdir: pathlib.Path) -> pathlib.Path:
    """Write *snippet* into tmpdir/src.py and create a CodeQL database."""
    (tmpdir / "src").mkdir()
    (tmpdir / "src" / "snippet.py").write_text(snippet)
    db = tmpdir / "db"
    subprocess.run(
        [codeql, "database", "create", db, "--language=python", "--source-root", tmpdir / "src"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT,
    )
    return db

def analyze_db(codeql: pathlib.Path, db: pathlib.Path, csv_out: pathlib.Path):
    """Run the builtin CWE query suite and emit CSV."""
    subprocess.run(
        [
            codeql, "database", "analyze", db,
            "codeql/python-queries",  # uses the default query pack containing CWE rules
            "--format=csv",
            f"--output={csv_out}",
            "--threads=0",
            "--no-color"
        ],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT,
    )

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--root",   default="/scratch/qilong3/codelmsec/outputs/generated_code/gemini/py", type=pathlib.Path)
    p.add_argument("--codeql", default="/scratch/qilong3/codeql/codeql",                                      type=pathlib.Path)
    p.add_argument("--out",    default="codeql_results",                                               type=pathlib.Path)
    p.add_argument("--keep-temp", action="store_true",
                   help="keep intermediate databases for debugging")
    args = p.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    summary_rows = []                         # accumulate (src_file, snippet_id, cwe_id, severity, message, location)

    for path in args.root.rglob("*.py"):
        snippets = extract_snippets(path)
        if not snippets:
            continue
        for idx, snippet in enumerate(snippets):
            # create isolated working dir
            workdir = tempfile.mkdtemp(prefix="cql_", dir="/tmp")
            workdir = pathlib.Path(workdir)
            try:
                db = build_db(args.codeql, snippet, workdir)
                csv_path = args.out / f"{path.stem}_{idx}.csv"
                analyze_db(args.codeql, db, csv_path)

                # append results to master summary
                with csv_path.open() as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        summary_rows.append([
                            str(path.relative_to(args.root)),
                            idx,
                            row["rule.id"],
                            row["severity"],
                            row["message"],
                            f"{row['file']}:{row['startLine']}"
                        ])
            finally:
                if not args.keep_temp:
                    shutil.rmtree(workdir, ignore_errors=True)

    # write consolidated CSV
    summary_csv = args.out / "all_findings.csv"
    with summary_csv.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["source_file", "snippet_id", "cwe_id", "severity", "message", "location"])
        writer.writerows(summary_rows)

    print(f"\nFinished. Individual CSVs + all_findings.csv are in: {args.out}")

if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as e:
        sys.exit(f"[ERROR] CodeQL failed with exit code {e.returncode}")
