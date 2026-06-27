#!/bin/sh
set -e

# Source of truth: Hermes content from git clone
# This script runs INSIDE the container after git clone copies files to /opt/data/
# Repo structure mirrors /opt/data/ directly:
#   config.yaml  -> /opt/data/config.yaml
#   SOUL.md      -> /opt/data/SOUL.md
#   skills/      -> /opt/data/skills/
#   init.sh      -> /opt/data/init.sh (this file)

# Ensure skills directory exists
if [ ! -d "/opt/data/skills" ]; then
  echo "[hermes-init] ERROR: skills directory missing after clone"
  exit 1
fi

# Ensure config.yaml exists
if [ ! -f "/opt/data/config.yaml" ]; then
  echo "[hermes-init] ERROR: config.yaml missing after clone"
  exit 1
fi

echo "[hermes-init] Content ready. Skills: $(ls /opt/data/skills | wc -l) directories."
