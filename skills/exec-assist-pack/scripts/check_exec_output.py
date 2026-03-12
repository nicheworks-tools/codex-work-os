from __future__ import annotations

from pathlib import Path
import sys

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 skills/exec-assist-pack/scripts/check_exec_output.py <markdown_file>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"missing file: {path}")
        return 1

    text = path.read_text(encoding="utf-8")

    required_any = [
        ("why this matters", ["## Why this matters"]),
        ("current situation", ["## Current situation"]),
        ("action section", ["## Decisions or actions needed", "## Actions needed"]),
    ]

    missing = []
    for label, options in required_any:
        if not any(opt in text for opt in options):
            missing.append(label)

    if missing:
        print("exec output check: FAIL")
        for item in missing:
            print(f"- missing section: {item}")
        return 1

    print("exec output check: OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
