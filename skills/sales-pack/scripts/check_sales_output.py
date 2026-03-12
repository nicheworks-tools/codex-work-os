from __future__ import annotations

from pathlib import Path
import sys

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 skills/sales-pack/scripts/check_sales_output.py <markdown_file>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"missing file: {path}")
        return 1

    text = path.read_text(encoding="utf-8")

    required_sections = [
        "## Goal",
        "## Confirmed facts",
        "## Open questions",
        "## Recommended next step",
        "## Ready-to-send draft",
    ]

    missing = [section for section in required_sections if section not in text]

    if missing:
        print("sales output check: FAIL")
        for item in missing:
            print(f"- missing section: {item}")
        return 1

    print("sales output check: OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
