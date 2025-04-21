#!/usr/bin/env python3
"""
Generate CodeLMSec completions with Gemini (google-generativeai).

Run:
  python gen_with_gemini.py --model gemini-pro      # or gemini-1.5-pro-preview
"""
import os, json, pathlib, time, argparse, google.generativeai as gen
from tqdm import tqdm

# ----- CLI -------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--prompts", default="benchmark_data/prompt_code_pairs.json")
parser.add_argument("--model",   default="gemini-pro",
                    help="Gemini model name, e.g. gemini-pro, gemini-1.0-pro")
parser.add_argument("--temp",    type=float, default=0.2)
parser.add_argument("--top_p",   type=float, default=0.95)
parser.add_argument("--sleep",   type=float, default=1.1,
                    help="seconds to wait between calls (avoids 429s)")
args = parser.parse_args()

# ----- Authenticate ----------------------------------------------------
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("Set GOOGLE_API_KEY in your env before running.")
gen.configure(api_key=api_key)
model = gen.GenerativeModel(args.model)

# ----- Load prompts ----------------------------------------------------
with open(args.prompts, "r", encoding="utf-8") as f:
    prompt_bundle = json.load(f)          # { "py": {...}, "c": {...} }

# ----- Loop over languages & CWEs --------------------------------------
out_root = pathlib.Path("outputs/generated_code/gemini")
total = sum(len(v["prompts"]) for lang in prompt_bundle.values()
                               for v in lang.values())

for lang, lang_prompts in prompt_bundle.items():          # 'py' or 'c'
    ext = "py" if lang == "py" else "c"
    for cwe, blob in lang_prompts.items():
        out_dir = out_root / lang / cwe
        out_dir.mkdir(parents=True, exist_ok=True)

        for idx, prompt in enumerate(tqdm(blob["prompts"],
                                          desc=f"{lang}/{cwe}",
                                          leave=False)):
            out_path = out_dir / f"{cwe}_{idx:02d}.{ext}"
            if out_path.exists():          # skip if already generated
                continue

            # ----- Gemini completion ----------------------------------
            try:
                rsp = model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": args.temp,
                        "top_p":       args.top_p,
                        "max_output_tokens": 256,
                    }
                )
                code = rsp.text
            except Exception as e:
                print(f"[WARN] {e} → retry in 5 s")
                time.sleep(5)
                continue

            out_path.write_text(code, encoding="utf-8")
            time.sleep(args.sleep)         # keep calls well‑paced

print(f"✓ Done – files in {out_root}")
