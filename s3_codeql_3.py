#!/usr/bin/env python3
"""
scan_cwes.py  –  Extract the ```python``` fenced block in each Gemini‑generated
file and analyse it with CodeQL, writing one CSV per file.

* CodeQL CLI lives at /scratch/qilong3/codeql/codeql  (default, override with --codeql-cli)
* Requires the Python extractor that ships with the standard CodeQL bundle.
"""

import argparse, pathlib, re, shutil, subprocess, tempfile

CODE_FENCE = re.compile(r"```python\s*(.*?)```", re.DOTALL | re.IGNORECASE)

def extract_python_block(text: str) -> str | None:
    m = CODE_FENCE.search(text)
    return m.group(1).strip("\n") if m else None

def run_codeql(codeql_cli: pathlib.Path, src_dir: pathlib.Path, out_csv: pathlib.Path):
    db_dir = src_dir.with_suffix(".codeql")
    subprocess.run(
        [codeql_cli, "database", "create", str(db_dir),
         "--language=python", "--source-root", str(src_dir), "--overwrite"],
        check=True)
    subprocess.run(
        [codeql_cli, "database", "analyze", str(db_dir),
         "python-security-extended.qls",
         "--format=csv", "--output", str(out_csv),
         "--threads=0", "--ram=6500"],
        check=True)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", required=True, type=pathlib.Path,
                   help="Root directory containing the Gemini outputs")
    p.add_argument("--out",  required=True, type=pathlib.Path,
                   help="Directory for CodeQL CSV results")
    p.add_argument("--codeql-cli", type=pathlib.Path,
                   default=pathlib.Path("/scratch/qilong3/codeql/codeql"),
                   help="Full path to the CodeQL CLI executable")
    p.add_argument("--keep-temp", action="store_true",
                   help="Keep temporary source copies/databases")
    args = p.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)

    for py_file in args.root.rglob("*.py"):
        code = extract_python_block(py_file.read_text(encoding="utf‑8", errors="ignore"))
        if not code:
            print(f"[SKIP] {py_file} – no fenced python block found")
            continue

        rel      = py_file.relative_to(args.root)
        work_dir = pathlib.Path(tempfile.mkdtemp(prefix="cql_")).joinpath(rel.stem)
        work_dir.mkdir(parents=True, exist_ok=True)
        pure     = work_dir / rel.name
        pure.write_text(code, encoding="utf‑8")

        out_csv = args.out / f"{rel.parent.name}_{rel.stem}.csv"
        try:
            run_codeql(args.codeql_cli, work_dir, out_csv)
            print(f"[OK]  {py_file}  →  {out_csv}")
        except subprocess.CalledProcessError as e:
            print(f"[FAIL] {py_file}: {e}")
        finally:
            if not args.keep_temp:
                shutil.rmtree(work_dir.with_suffix(".codeql"), ignore_errors=True)
                shutil.rmtree(work_dir,              ignore_errors=True)

if __name__ == "__main__":
    main()
