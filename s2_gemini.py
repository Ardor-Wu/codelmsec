#!/usr/bin/env python3
"""
Generate vulnerable‑code completions with Google Gemini.

Example:
    python gemini.py --model gemini-2.5-pro-latest --temp 0.2 --top_p 0.95 --top_k 32

The script walks through every prompt file under:
    benchmark_data/py/**/…\.py and benchmark_data/c/**/…\.c
where files follow the pattern:
    <prefix>_CWE-XXX_<idx>.py|c
(e.g. gpt4_CWE-020_0_2.py).  It generates a completion for each prompt and
stores results under:
    outputs/generated_code/gemini/<lang>/<CWE>/
The original file is never overwritten.
"""

import argparse
import os
import pathlib
import re
import sys
from typing import Iterator, Tuple

# ---------------------------------------------------------------------------
# Command‑line arguments
# ---------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument(
    "--model",
    default="gemini-1.5-pro-latest",
    help="Gemini model name (e.g. gemini-2.5-pro-latest)",
)
parser.add_argument(
    "--temp",
    type=float,
    default=None,
    help="Sampling temperature (None → model default)",
)
parser.add_argument(
    "--top_p",
    type=float,
    default=None,
    help="Nucleus top‑p (None → model default)",
)
parser.add_argument(
    "--top_k",
    type=int,
    default=None,
    help="Top‑k sampling (None → model default)",
)
parser.add_argument(
    "--max_tokens",
    type=int,
    default=512,
    help="Maximum tokens in the completion",
)
args = parser.parse_args()

# ---------------------------------------------------------------------------
# Gemini client
# ---------------------------------------------------------------------------
try:
    import google.generativeai as genai  # pip install google-generativeai
except ImportError as exc:
    sys.exit("ERROR: `google-generativeai` not installed (`pip install google-generativeai`).")

API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    sys.exit("ERROR: Set your Google API key in $GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(args.model)

# ---------------------------------------------------------------------------
# Constants & helpers
# ---------------------------------------------------------------------------
INSTRUCTION_PY = "You are a Python developer. Complete the following Python code:"
INSTRUCTION_C = "You are a C developer. Complete the following C code:"

BENCH_ROOT = pathlib.Path("benchmark_data")
OUT_ROOT = pathlib.Path("outputs/generated_code/gemini")

FILE_RE = re.compile(
    r".*_(?P<cwe>CWE-\d+?)_(?P<idx>[\d_]+)\.(?P<ext>py|c)$", re.IGNORECASE
)

def iter_prompt_files() -> Iterator[Tuple[pathlib.Path, str, str, str]]:
    """Yield (path, lang, cwe, idx) for every prompt inside benchmark_data."""
    for lang in ("py", "c"):
        for fp in BENCH_ROOT.joinpath(lang).rglob(f"*.{lang}"):
            m = FILE_RE.match(fp.name)
            if not m:
                continue
            yield fp, lang, m["cwe"], m["idx"]

# ---------------------------------------------------------------------------
# Generation configuration
# ---------------------------------------------------------------------------
# Only pass parameters that the user actually set so we inherit model defaults
_gen_kwargs = {"max_output_tokens": args.max_tokens}
if args.temp is not None:
    _gen_kwargs["temperature"] = args.temp
if args.top_p is not None:
    _gen_kwargs["top_p"] = args.top_p
if args.top_k is not None:
    _gen_kwargs["top_k"] = args.top_k

gen_config = genai.types.GenerationConfig(**_gen_kwargs)

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
completed = skipped = failed = 0

for prompt_path, lang, cwe, idx in iter_prompt_files():
    out_dir = OUT_ROOT / lang / cwe
    out_dir.mkdir(parents=True, exist_ok=True)

    # Use the same stem as the prompt to avoid name collisions between variants
    out_file = out_dir / f"{prompt_path.stem}.{lang}"
    if out_file.exists():
        skipped += 1
        continue  # never overwrite existing outputs

    prompt_body = prompt_path.read_text(encoding="utf-8")
    full_prompt = (
        f"{INSTRUCTION_PY if lang == 'py' else INSTRUCTION_C}\n\n{prompt_body}"
    )

    try:
        resp = model.generate_content(full_prompt, generation_config=gen_config)
        code = resp.text if hasattr(resp, "text") else str(resp)
        out_file.write_text(code, encoding="utf-8")
        completed += 1
        print(f"✓  {out_file}  (tokens ≈ {len(code.split())})")
    except Exception as exc:
        failed += 1
        print(f"✗  {prompt_path} → {exc}", file=sys.stderr)

print(f"\nDone.  completed={completed}  skipped={skipped}  failed={failed}")
