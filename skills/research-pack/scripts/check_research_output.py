from __future__ import annotations

from pathlib import Path
import sys

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 skills/research-pack/scripts/check_research_output.py <markdown_file>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"missing file: {path}")
        return 1

    text = path.read_text(encoding="utf-8")

    required_any = [
        ("decision question", ["## Decision question", "## Question"]),
        ("evidence", ["## Evidence", "## Evidence summary"]),
        ("recommendation", ["## Recommendation"]),
        ("uncertainty", ["## Uncertainty / caveats", "## Confidence / uncertainty"]),
    ]

    missing = []
    for label, options in required_any:
        if not any(opt in text for opt in options):
            missing.append(label)

    if missing:
        print("research output check: FAIL")
        for item in missing:
            print(f"- missing section: {item}")
        return 1

    print("research output check: OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
