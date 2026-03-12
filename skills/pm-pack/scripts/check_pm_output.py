from __future__ import annotations

from pathlib import Path
import sys

REQUIRED_HEADINGS = [
    "## Goal",
    "## Goal / scope",
    "## Current status",
    "## Progress made",
    "## Risks / blockers",
]

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 skills/pm-pack/scripts/check_pm_output.py <markdown_file>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"missing file: {path}")
        return 1

    text = path.read_text(encoding="utf-8")

    found_goal = any(h in text for h in ["## Goal", "## Goal / scope"])
    found_current = "## Current status" in text
    found_progress = "## Progress made" in text
    found_risks = "## Risks / blockers" in text

    missing = []
    if not found_goal:
        missing.append("## Goal or ## Goal / scope")
    if not found_current:
        missing.append("## Current status")
    if not found_progress:
        missing.append("## Progress made")
    if not found_risks:
        missing.append("## Risks / blockers")

    if missing:
        print("pm output check: FAIL")
        for item in missing:
            print(f"- missing heading: {item}")
        return 1

    print("pm output check: OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
