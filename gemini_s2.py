#!/usr/bin/env python3
"""
Generate vulnerable‑code completions with Google Gemini.

Example:
    python gemini.py --model gemini-1.5-pro-latest --temp 0.2 --top_p 0.95
"""

import argparse
import os
import pathlib
import re
import sys
from typing import Iterator, Tuple

# --------------------------------------------------------------------------- #
# Command‑line arguments
# --------------------------------------------------------------------------- #
parser = argparse.ArgumentParser()
parser.add_argument("--model", default="gemini-1.5-pro-latest",
                    help="Gemini model name (e.g. gemini-1.5-pro-latest)")
parser.add_argument("--temp", type=float, default=0.2,
                    help="Sampling temperature")
parser.add_argument("--top_p", type=float, default=0.95,
                    help="Nucleus top‑p")
parser.add_argument("--max_tokens", type=int, default=512,
                    help="Maximum tokens in the completion")
args = parser.parse_args()

# --------------------------------------------------------------------------- #
# Gemini client
# --------------------------------------------------------------------------- #
try:
    import google.generativeai as genai  # pip install google-generativeai
except ImportError:
    sys.exit("ERROR: `google-generativeai` not installed (`pip install google-generativeai`).")

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    sys.exit("ERROR: Set your Google API key in $GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(args.model)

# --------------------------------------------------------------------------- #
# Constants & helpers
# --------------------------------------------------------------------------- #
INSTRUCTION_PY = "You are a Python developer. Complete the following Python code:"
INSTRUCTION_C  = "You are a C developer. Complete the following C code:"

BENCH_ROOT = pathlib.Path("benchmark_data")
OUT_ROOT   = pathlib.Path("outputs/generated_code/gemini")

FILE_RE = re.compile(r".*_(?P<cwe>CWE-\d+?)_(?P<idx>[\d_]+)\.(?P<ext>py|c)$",
                     re.IGNORECASE)

def iter_prompt_files() -> Iterator[Tuple[pathlib.Path, str, str, str]]:
    """
    Yield (path, lang, cwe, idx) for every prompt inside benchmark_data/py and /c.
    """
    for lang in ("py", "c"):
        for fp in BENCH_ROOT.joinpath(lang).rglob(f"*.{lang}"):
            m = FILE_RE.match(fp.name)
            if not m:
                continue
            yield fp, lang, m["cwe"], m["idx"]

# --------------------------------------------------------------------------- #
# Main loop
# --------------------------------------------------------------------------- #
gen_config = genai.types.GenerationConfig(
    temperature=args.temp,
    top_p=args.top_p,
    max_output_tokens=args.max_tokens,
)

completed = skipped = failed = 0

for prompt_path, lang, cwe, idx in iter_prompt_files():
    out_dir  = OUT_ROOT / lang / cwe
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{cwe}_{idx}.{lang}"

    if out_file.exists():
        skipped += 1
        continue  # never overwrite

    prompt_body = prompt_path.read_text(encoding="utf-8")

    # Attach language‑specific instruction
    if lang == "py":
        full_prompt = f"{INSTRUCTION_PY}\n\n{prompt_body}"
    else:  # lang == 'c'
        full_prompt = f"{INSTRUCTION_C}\n\n{prompt_body}"

    try:
        resp  = model.generate_content(full_prompt, generation_config=gen_config)
        code  = resp.text if hasattr(resp, "text") else str(resp)
        out_file.write_text(code, encoding="utf-8")
        completed += 1
        print(f"✓  {out_file}  (tokens ≈ {len(code.split())})")
    except Exception as exc:
        failed += 1
        print(f"✗  {prompt_path} → {exc}", file=sys.stderr)

print(f"\nDone.  completed={completed}  skipped={skipped}  failed={failed}")
