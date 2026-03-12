#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SRC_DIR="$ROOT_DIR/skills"
DEST_DIR="$HOME/.agents/skills"

mkdir -p "$DEST_DIR"

if [ "$#" -eq 0 ]; then
  set -- research-pack pm-pack sales-pack exec-assist-pack cs-pack
fi

for pack in "$@"; do
  if [ ! -d "$SRC_DIR/$pack" ]; then
    echo "[skip] pack not found: $pack"
    continue
  fi
  ln -sfn "$SRC_DIR/$pack" "$DEST_DIR/$pack"
  echo "[linked] $pack -> $DEST_DIR/$pack"
 done
