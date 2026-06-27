---
name: dokploy-api-compose-workflows
title: "Dokploy API Compose Workflows"
description: "Practical patterns for deploying docker-compose services through the Dokploy API — the gotchas, workarounds, and procedural steps that the raw API docs don't cover."
tags: [dokploy, compose, deployment, api, docker-compose]
category: dokploy
---

# Dokploy API Compose Workflows

## When to Use

Load this skill when you need to create, update, or deploy a Docker Compose service through the Dokploy API at `/compose.*` endpoints. This is the normal path for deploying raw docker-compose templates.

## SDK Setup (this environment)

The SDK lives at `/opt/data/skills/dokploy/sdk.py`. It needs `requests` + `pyyaml` which are installed in `.venv/`. Always run SDK code with:

```bash
cd /opt/data/skills/dokploy && .venv/bin/python3 -c "..."
```

Environment variables (`DOKPLOY_API_TOKEN`, `DOKPLOY_BASE_URL`, `DOKPLOY_SERVER_ID`) are passed through to sandboxed execution via `env_passthrough` in config.yaml.

The SDK reads `DOKPLOY_SERVER_ID` from env (falls back to `PLAYGROUND_SERVER_ID`).

For simple API calls where the SDK isn't needed, `helper.py` works with system Python (stdlib only, no venv):

```bash
python3 /opt/data/skills/dokploy/helper.py call /compose.create '{"name":"my-app"}'
```

## Workflow

### 1. Create the compose service

Use `compose.create` with:
- `name` — human-readable name
- `description` — optional
- `environmentId` — from the target environment
- `composeFile` — the raw docker-compose YAML content
- `sourceType` — set to `"raw"` (but see quirk #1 below)
- `composeType` — `"docker-compose"`
- `appName` — optional but good practice

### 2. Deploy

Call `compose.deploy` with `composeId`.

### 3. Monitor

- Check `composeStatus` via `compose.one` — values: `"idle"`, `"running"`, `"done"`, `"error"`
- Read deployment logs from the filesystem at `/opt/dokploy/logs/{appName}/*.log`
- Read container logs via `compose.readLogs(composeId, containerId, tail=N)`
- Find containers via `docker.getContainersByAppLabel(appName, type="standalone")`

### 4. Update

Use `compose.update` — ALWAYS send the full compose object (see quirk #2).

## Critical Quirk #1: sourceType Defaults to "github"

**Symptom**: After creating a compose service with a raw compose file, deployment fails with "Github Provider not found".

**Root cause**: The API defaults `sourceType` to `"github"` even when `compose.create` payload sets it to `"raw"`.

**Fix**: After `compose.create`, fetch the full object with `compose.one`, set `sourceType: "raw"`, and send the ENTIRE object back via `compose.update`. Then deploy.

```
full = compose.one(composeId)
full["sourceType"] = "raw"
compose.update(full)
compose.deploy(composeId)
```

## Critical Quirk #2: compose.update Requires Full Payload

**Symptom**: Sending a partial update like `{"composeId": "...", "sourceType": "raw"}` returns success HTTP 200, but `compose.one` still shows the old value.

**Root cause**: `compose.update` silently ignores partial payloads — it fills omitted fields from saved defaults.

**Fix**: Always send the full payload fetched from `compose.one` and change only what you need.

```
full = compose.one(composeId)
full["sourceType"] = "raw"
compose.update(full)
```

## Pattern: Startup-Time Config Fixes

Some images ship with unsafe default credentials. Fix in the docker-compose command:

```
command: >
  sh -c '
    if [ ! -f /app/config.yaml ]; then cp /app/config.example.yaml /app/config.yaml; fi;
    if grep -q "example-api-key" /app/config.yaml 2>/dev/null; then
      sed -i "s/example-api-key/$(tr -dc A-Za-z0-9 </dev/urandom | head -c 32)/g" /app/config.yaml;
    fi;
    exec /app/start.sh
  '
```

This handles: first-boot config creation, unsafe credential replacement, and idempotency.

## Pattern: Image Digest Pinning

1. Pull the image: `docker pull image:tag`
2. Resolve digest: `docker inspect image:tag --format '{{.RepoDigests}}'`
3. Pin: `image:tag@sha256:abcdef...`

## Recovery: Compose in Error State

If `composeStatus` is `"error"`:
1. `compose.cleanQueues(composeId)` — reset stuck state
2. Fix the compose file or config
3. `compose.deploy(composeId)` — retry

## References

See `references/compose-api-errors.md` for specific error messages and traces encountered in real sessions.
