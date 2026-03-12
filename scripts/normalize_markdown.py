from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

for path in ROOT.rglob('*.md'):
    text = path.read_text(encoding='utf-8')
    text = '
'.join(line.rstrip() for line in text.splitlines()).strip() + '
'
    path.write_text(text, encoding='utf-8')

print('Normalized markdown whitespace.')
