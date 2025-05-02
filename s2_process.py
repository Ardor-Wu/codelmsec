#!/usr/bin/env python3
"""
Extract pure source code from GPT‑4o's markdown‑style output files.

Directory layout assumed:
    outputs/generated_code/gpt4o/py/CWE-XXX/*.py   (markdown‑wrapped Python)
    outputs/generated_code/gpt4o/c/CWE-XXX/*.c     (markdown‑wrapped C)

For every *.py* and *.c* file, the script pulls the text between
    ```python ... ```   or   ```c ... ```
respectively, and saves the cleaned code to:
    extracted_code/gpt4o/{py|c}/CWE-XXX/<same filename>

Run with plain `python extract_fenced_code.py` from the project root.
"""

import re
import pathlib
import sys
from typing import Optional

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
ROOT = pathlib.Path("outputs/generated_code/gpt4o")
OUT  = pathlib.Path("extracted_code/gpt4o")

# Regexes for fenced blocks
FENCE = {
    "py": re.compile(r"```python\s*([\s\S]*?)```", re.IGNORECASE),
    "c":  re.compile(r"```c\s*([\s\S]*?)```", re.IGNORECASE),
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_code(text: str, lang: str) -> Optional[str]:
    """Return concatenated code inside the first matching fenced blocks."""
    matches = FENCE[lang].finditer(text)
    code_blocks = [m.group(1).lstrip("\n") for m in matches]
    if not code_blocks:
        return None
    return "\n\n".join(code_blocks).rstrip() + "\n"


def process_language(lang: str) -> None:
    """Walk through the language tree, extract code, write cleaned files."""
    ext = "py" if lang == "py" else "c"
    lang_root = ROOT / lang
    for src_path in lang_root.rglob(f"*.{ext}"):
        code = extract_code(src_path.read_text(encoding="utf-8", errors="ignore"), lang)
        if code is None:
            continue  # no fenced block found – skip
        dest_path = OUT / lang / src_path.relative_to(lang_root)
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_text(code, encoding="utf-8")
        print(f"[✓] {dest_path.relative_to(OUT)}")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if not ROOT.exists():
        sys.exit(f"Error: {ROOT} not found. Check the directory layout.")

    for lang in ("py", "c"):
        process_language(lang)

    print("\nExtraction completed. Clean files are under", OUT)


if __name__ == "__main__":
    main()
