# Install Guide

## Personal installation

Use the install scripts when you want packs available from your user-level Codex environment.

### Symlink install

```bash
bash install/install-symlinks.sh research-pack pm-pack
```

This creates symlinks inside `~/.agents/skills/`.
It is best when you want pack updates in this repository to remain live.

### Copy install

```bash
bash install/install-copy.sh sales-pack exec-assist-pack
```

This copies the pack directories into `~/.agents/skills/`.
It is best when you want a standalone snapshot.

---

## Project-local installation

You can also copy packs into a target repository’s `.agents/skills/` directory when you want one repository to carry its own pack set.

That is useful for team-specific or project-specific workflows.

---

## Uninstall

```bash
bash install/uninstall.sh pm-pack research-pack
```

This removes pack directories from `~/.agents/skills/`.

---

## Notes

- install scripts create `~/.agents/skills/` if needed
- pack names must match the folder names under `skills/`
- if no pack names are supplied, the scripts operate on all packs
