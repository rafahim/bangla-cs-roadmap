#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/generate_repo.py"
printf '\nRegenerated all repository files and bangla-cs-roadmap.zip.\n'
