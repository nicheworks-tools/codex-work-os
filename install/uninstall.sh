#!/usr/bin/env bash
set -euo pipefail

DEST_DIR="$HOME/.agents/skills"

if [ "$#" -eq 0 ]; then
  set -- research-pack pm-pack sales-pack exec-assist-pack cs-pack
fi

for pack in "$@"; do
  rm -rf "$DEST_DIR/$pack"
  echo "[removed] $DEST_DIR/$pack"
 done
