from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
required_markers = ['## Goal', '## Current situation']
checks = [ROOT / 'shared' / 'templates' / 'brief.md']
errors = []

for path in checks:
    text = path.read_text(encoding='utf-8')
    for marker in required_markers:
        if marker not in text:
            errors.append(f'{path.relative_to(ROOT)}: missing marker {marker}')

if errors:
    for err in errors:
        print(err)
    sys.exit(1)

print('Output lint checks passed.')
