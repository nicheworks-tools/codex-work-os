from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

required_paths = [
    ROOT / 'README.md',
    ROOT / 'AGENTS.md',
    ROOT / 'DISCLAIMER.md',
    ROOT / 'LICENSE',
    ROOT / '.github' / 'FUNDING.yml',
    ROOT / 'spec' / 'codex_work_os_spec_en.md',
    ROOT / 'spec' / 'codex_work_os_spec_ja.md',
    ROOT / 'docs' / 'roadmap.md',
    ROOT / 'install' / 'install-symlinks.sh',
    ROOT / 'scripts' / 'check_required_files.py',
]

required_packs = [
    'research-pack',
    'pm-pack',
    'sales-pack',
    'exec-assist-pack',
    'cs-pack',
]

missing = [str(p.relative_to(ROOT)) for p in required_paths if not p.exists()]
for pack in required_packs:
    skill_file = ROOT / 'skills' / pack / 'SKILL.md'
    if not skill_file.exists():
        missing.append(str(skill_file.relative_to(ROOT)))

if missing:
    print('Missing required paths:')
    for item in missing:
        print(f'- {item}')
    sys.exit(1)

print('Structure validation passed.')
