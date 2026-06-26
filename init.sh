#!/bin/sh
set -e

# Source of truth: Hermes content from GitHub release
# This script runs INSIDE the container after the ZIP extracts to /opt/data/
# ZIP structure mirrors /opt/data/ directly:
#   config.yaml  -> /opt/data/config.yaml
#   SOUL.md      -> /opt/data/SOUL.md
#   skills/      -> /opt/data/skills/
#   init.sh      -> /opt/data/init.sh (this file)

# The unzip already overwrote everything. This script handles post-extraction logic.

TAG_FILE="/opt/data/.content-tag"
CONTENT_TAG="${CONTENT_TAG:-latest}"

echo "[hermes-init] Content tag: ${CONTENT_TAG}"

# Write current tag for tracking
if [ -n "${CONTENT_TAG}" ]; then
  echo "${CONTENT_TAG}" > "${TAG_FILE}"
fi

# Ensure skills directory exists
if [ ! -d "/opt/data/skills" ]; then
  echo "[hermes-init] ERROR: skills directory missing after extraction"
  exit 1
fi

# Ensure config.yaml exists
if [ ! -f "/opt/data/config.yaml" ]; then
  echo "[hermes-init] ERROR: config.yaml missing after extraction"
  exit 1
fi

echo "[hermes-init] Content ready. Skills: $(ls /opt/data/skills | wc -l) directories."
