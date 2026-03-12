from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
packs = sorted((ROOT / 'skills').glob('*-pack'))

required_names = {'SKILL.md', 'references', 'templates', 'scripts'}
errors = []

for pack in packs:
    names = {p.name for p in pack.iterdir()}
    missing = sorted(required_names - names)
    if missing:
        errors.append((pack.name, missing))

if errors:
    for pack_name, missing in errors:
        print(f'{pack_name}: missing {", ".join(missing)}')
    sys.exit(1)

print('All pack folders contain the required files/directories.')
