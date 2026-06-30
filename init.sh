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

# Expand ${VAR} references in config.yaml using container environment variables
if [ -f /opt/data/config.yaml ]; then
  envsubst < /opt/data/config.yaml > /opt/data/config.yaml.tmp
  mv /opt/data/config.yaml.tmp /opt/data/config.yaml
  echo "[hermes-init] config.yaml: expanded environment variables"
fi

# Write /opt/data/.env from container env vars so Hermes runtime can
# read secrets (OPENAI_API_KEY, API_SERVER_KEY, etc.) at API-call time.
# This file is the source of truth for Hermes API client config, not
# process.env, since Hermes code reads it directly.
if [ -n "${OPENAI_API_KEY}" ]; then
  cat > /opt/data/.env <<EOF
OPENAI_API_KEY=${OPENAI_API_KEY}
OPENAI_BASE_URL=${OPENAI_BASE_URL}
API_SERVER_KEY=${API_SERVER_KEY}
HERMES_MODEL=${HERMES_MODEL}
HERMES_DELEGATION_MODEL=${HERMES_DELEGATION_MODEL}
HERMES_AUX_MODEL=${HERMES_AUX_MODEL}
HERMES_PROVIDER=${HERMES_PROVIDER}
EOF
  echo "[hermes-init] .env: written from container env"
else
  echo "[hermes-init] WARNING: OPENAI_API_KEY unset — skipping .env write"
fi

# Ensure hermes user (UID 10000) can write to /opt/data
chown -R 10000:10000 /opt/data

echo "[hermes-init] Content ready. Skills: $(ls /opt/data/skills | wc -l) directories."
