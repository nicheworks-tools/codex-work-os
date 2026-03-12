from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

def iter_markdown_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.md")
        if ".git" not in p.parts
    )

def first_meaningful_line(text: str) -> str:
    lines = text.splitlines()

    if not lines:
        return ""

    i = 0

    # Allow YAML front matter at the top of the file.
    if i < len(lines) and lines[i].strip() == "---":
        i += 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        if i < len(lines) and lines[i].strip() == "---":
            i += 1

    while i < len(lines):
        line = lines[i].strip()
        if line:
            return line
        i += 1

    return ""

def main() -> int:
    bad: list[str] = []

    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        first = first_meaningful_line(text)

        if not first:
            continue

        if path.name == "SKILL.md":
            if first.startswith("# "):
                continue
            bad.append(f"{path.relative_to(ROOT)}: first meaningful line should start with a level-1 heading after optional front matter")
            continue

        if not first.startswith("# "):
            bad.append(f"{path.relative_to(ROOT)}: first line should start with a level-1 heading")

    if bad:
        for item in bad:
            print(item)
        return 1

    print("Markdown lint checks passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
