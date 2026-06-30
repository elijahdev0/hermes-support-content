#!/bin/sh
set -e

LOG="[hermes-init]"

echo "$LOG === Starting init.sh ==="
echo "$LOG PWD: $(pwd)"
echo "$LOG Args: $*"
echo "$LOG UID/GID: $(id)"

# Source of truth: Hermes content from git clone
# This script runs INSIDE the container after git clone copies files to /opt/data/
# Repo structure mirrors /opt/data/ directly:
#   config.yaml  -> /opt/data/config.yaml
#   SOUL.md      -> /opt/data/SOUL.md
#   skills/      -> /opt/data/skills/
#   init.sh      -> /opt/data/init.sh (this file)

# Ensure skills directory exists
if [ ! -d "/opt/data/skills" ]; then
  echo "$LOG ERROR: skills directory missing at /opt/data/skills"
  echo "$LOG /opt/data contents:"
  ls -la /opt/data/ 2>&1 || echo "$LOG   (could not list /opt/data)"
  exit 1
fi
echo "$LOG skills directory present"

# Ensure config.yaml exists
if [ ! -f "/opt/data/config.yaml" ]; then
  echo "$LOG ERROR: config.yaml missing at /opt/data/config.yaml"
  echo "$LOG /opt/data contents:"
  ls -la /opt/data/ 2>&1 || echo "$LOG   (could not list /opt/data)"
  exit 1
fi
echo "$LOG config.yaml present"

# Expand ${VAR} references in config.yaml using container environment variables
if [ -f /opt/data/config.yaml ]; then
  echo "$LOG expanding env vars in config.yaml..."
  envsubst < /opt/data/config.yaml > /opt/data/config.yaml.tmp
  mv /opt/data/config.yaml.tmp /opt/data/config.yaml
  echo "$LOG config.yaml: expanded environment variables"
else
  echo "$LOG WARNING: config.yaml not found, skipping envsubst"
fi

# Write /opt/data/.env from container env vars so Hermes runtime can
# read secrets (OPENAI_API_KEY, API_SERVER_KEY, etc.) at API-call time.
# This file is the source of truth for Hermes API client config, not
# process.env, since Hermes code reads it directly.
echo "$LOG checking OPENAI_API_KEY presence..."
if [ -n "${OPENAI_API_KEY}" ]; then
  echo "$LOG OPENAI_API_KEY set (len=${#OPENAI_API_KEY}), writing .env..."
  cat > /opt/data/.env <<EOF
OPENAI_API_KEY=${OPENAI_API_KEY}
OPENAI_BASE_URL=${OPENAI_BASE_URL}
API_SERVER_KEY=${API_SERVER_KEY}
HERMES_MODEL=${HERMES_MODEL}
HERMES_DELEGATION_MODEL=${HERMES_DELEGATION_MODEL}
HERMES_AUX_MODEL=${HERMES_AUX_MODEL}
HERMES_PROVIDER=${HERMES_PROVIDER}
EOF
  echo "$LOG .env written, verifying..."
  if [ -f /opt/data/.env ]; then
    LINE_COUNT=$(wc -l < /opt/data/.env)
    echo "$LOG .env has $LINE_COUNT lines"
    # Check each var made it (log presence only, not value)
    for var in OPENAI_API_KEY OPENAI_BASE_URL API_SERVER_KEY HERMES_MODEL HERMES_DELEGATION_MODEL HERMES_AUX_MODEL HERMES_PROVIDER; do
      grep -q "^${var}=" /opt/data/.env && echo "$LOG   $var=ok" || echo "$LOG   $var=MISSING"
    done
  else
    echo "$LOG ERROR: .env write failed (file not present after cat)"
    exit 1
  fi
  echo "$LOG .env: written from container env"
else
  echo "$LOG WARNING: OPENAI_API_KEY unset — skipping .env write"
fi

# Ensure hermes user (UID 10000) can write to /opt/data
echo "$LOG chowning /opt/data to 10000:10000..."
chown -R 10000:10000 /opt/data
echo "$LOG chown complete"

SKILL_COUNT=$(ls /opt/data/skills | wc -l)
echo "$LOG === Content ready. Skills: $SKILL_COUNT directories. ==="
