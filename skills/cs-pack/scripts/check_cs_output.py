from __future__ import annotations

from pathlib import Path
import sys

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 skills/cs-pack/scripts/check_cs_output.py <markdown_file>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"missing file: {path}")
        return 1

    text = path.read_text(encoding="utf-8")

    required_any = [
        ("case summary", ["## Case summary", "## Problem summary"]),
        ("impact", ["## User impact", "## Impact / urgency"]),
        ("evidence", ["## Evidence / reproduction", "## Evidence / reproduction clues"]),
        ("actions", ["## Actions already taken"]),
    ]

    missing = []
    for label, options in required_any:
        if not any(opt in text for opt in options):
            missing.append(label)

    if missing:
        print("cs output check: FAIL")
        for item in missing:
            print(f"- missing section: {item}")
        return 1

    print("cs output check: OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
