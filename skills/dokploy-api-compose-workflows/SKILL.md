---
name: dokploy-api-compose-workflows
title: "Dokploy API Compose Workflows"
description: "Practical patterns for deploying docker-compose services through the Dokploy API — the gotchas, workarounds, and procedural steps that the raw API docs don't cover."
tags: [dokploy, compose, deployment, api, docker-compose]
category: dokploy
---

# Dokploy API Compose Workflows

## When to Use

Load this skill when you need to create, update, deploy, or diagnose Docker Compose services through the Dokploy API. Also load it whenever the user asks about their deployments, infrastructure status, or container health — the diagnostics patterns here are the fastest path to a complete answer.

## Efficiency Rules (read before acting)

These rules minimize tool calls. Violating them produces multi-call debugging sessions instead of one-shot answers.

1. **`debug()` is the diagnostics method.** When the user asks "what's wrong with X" or "show logs for Y" or "status of everything", use `dk.debug(compose_id)` in a loop over `dk.list_projects()`. It prints config, domains, deployments, filesystem logs, and container logs in one call. Never manually assemble log reads with `tail`, `cat`, bash, or separate API calls.

2. **One terminal call per goal.** Batch listing, diagnostics, and health checks into a single Python script. Do not make separate calls for listing projects then containers then logs — one script does all three.

3. **System status is one workflow.** To answer "show me everything", run the "Show me everything" script from the SDK README (`/opt/data/skills/dokploy/README.md`). It lists servers, projects, environments, composes, containers, and databases in one shot.

4. **Return types are always flat `list[dict]`.** Never probe shapes with `isinstance()` or `json.dumps()`. Every `dk.list_*()` method returns a flat list you can iterate directly.

## SDK Setup (this environment)

The SDK lives at `/opt/data/skills/dokploy/sdk.py`. It needs `requests` + `pyyaml` which are installed in `.venv/`. Always run SDK code with:

```bash
cd /opt/data/skills/dokploy && .venv/bin/python3 -c "..."
```

**Use `terminal` for SDK/API calls — not `execute_code`.** The `execute_code` sandbox does NOT have access to environment variables. Terminal inherits the full environment.

The SDK reads `DOKPLOY_SERVER_ID` from env (falls back to `PLAYGROUND_SERVER_ID`).

**All list/search methods return flat `list[dict]`** — no `isinstance()` checks needed. `dk.list_dokploy_projects()`, `dk.list_environments()`, `dk.list_containers()`, etc. all return the same shape.

For simple API calls where the SDK isn't needed, `helper.py` works with system Python (stdlib only, no venv):

```bash
python3 /opt/data/skills/dokploy/helper.py call /compose.create '{"name":"my-app"}'
```

## Workflow: Deploy a Compose

### Use the SDK (preferred)

```python
from sdk import DokployClient
dk = DokployClient()

result = dk.deploy_compose(
    name="my-app",
    compose_yaml="""services:
  web:
    image: nginx:alpine""",
    env_vars={"KEY": "value"},
    domain="my-app.example.com",
)
# Blocks until done. Prints diagnostics automatically.
```

### Manual API workflow (fallback)

If you must use raw API calls:

### 1. Create

`POST /compose.create` with `name`, `environmentId`, `composeFile`, `composeType: "docker-compose"`, `sourceType: "raw"`.

### 2. Fix sourceType (quirk #1)

Always fetch + update after create to force `sourceType: "raw"`.

### 3. Deploy

`POST /compose.deploy` with `composeId`.

### 4. Update (quirk #2)

Always refetch full object via `compose.one` before calling `compose.update`.

## Workflow: Diagnose a Compose

### Use the SDK (one call)

```python
from sdk import DokployClient
dk = DokployClient()

for c in dk.list_projects():
    dk.debug(c['composeId'])
```

`debug()` prints: config, domains, deployments, filesystem deployment logs, and container logs. Do NOT manually assemble diagnostics with separate bash/API calls — this is the method.

### Manual diagnostics (fallback)

- `composeStatus` from `compose.one` — values: `"idle"`, `"running"`, `"done"`, `"error"`
- Filesystem logs: `/opt/dokploy/logs/{appName}/*.log`
- Container logs: `compose.readLogs(composeId, containerId, tail=N)`
- Containers: `docker.getContainersByAppLabel(appName, type="standalone")`

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

## Critical Quirk #3: composeStatus Lies for Failed Deploys

**Symptom**: A compose with a bad image (nonexistent, pull denied) shows `composeStatus: "running"` but the container never starts. Or a port conflict shows `composeStatus: "idle"` with zero deployment records and no log files — completely silent failure.

**Root cause**: Dokploy API status tracks the *deployment process*, not the *outcome*. A deployment that starts but has Docker errors at pull/start time can remain "running" or "idle" indefinitely. The API `composeStatus` field is not a reliable health indicator.

**Fix**: Always check filesystem deployment logs at `/opt/dokploy/logs/{appName}/*.log`. Look for `Error: ❌ Docker command failed`, `pull access denied`, or similar Docker-level errors. The SDK's `debug()` method reads these automatically. *Never* trust `composeStatus` alone.

**Error variations discovered**:
- Bad image: `pull access denied for totallyfake/nonexistent, repository does not exist or may require 'docker login'` → `composeStatus: "running"` (lies)
- Port conflict: no error message anywhere → `composeStatus: "idle"`, no deployments, no logs (silent failure)
- Valid deploy: `Docker Compose Deployed: ✅` → `composeStatus: "done"` (correct)

## Critical Quirk #4: Template Deploy Default Branch

**Symptom**: `deploy_from_template()` returns `HTTP 500: Template files not found`.

**Root cause**: SDK previously defaulted `base_url` to `https://raw.githubusercontent.com/Dokploy/templates/canary` — the `canary` branch does not exist. Templates live on `main`.

**Fix**: SDK now defaults to `main` branch (patched 2026-06-28). If you get this error, pass `base_url="https://raw.githubusercontent.com/Dokploy/templates/main"` explicitly.

## Critical Quirk #5: compose.deployTemplate Requires environmentId

**Symptom**: `HTTP 400: environmentId: Invalid input: expected string, received undefined`.

**Root cause**: Unlike `compose.create`, the `deployTemplate` endpoint does not infer `environmentId` from context. It is a required field.

**Fix**: Always pass `environmentId`. The SDK auto-detects it via `_find_default_environment()`.

## Critical Quirk #6: `redeploy()` Does NOT Force Container Restarts

**Symptom**: You call `dk.redeploy(compose_id)` to "restart" a service, the deployment succeeds (`composeStatus: "done"`), but the containers were never actually restarted or recreated. The user's app behavior doesn't change — old env vars, old image, old process — yet Dokploy reports success.

**Root cause**: Dokploy's `redeploy` (which calls `rebuildCompose` internally) runs:
```
docker compose -p {appName} -f docker-compose.yml up -d --build --remove-orphans
```
Docker Compose's `up -d` only recreates containers when their configuration or image **changed** since the container was created. If the compose file, image tag, and env vars are all identical to what's already running, Compose prints "up-to-date" and **leaves the running containers untouched**. The `--build` flag is only meaningful for services with a `build:` section — for services using pre-built `image:` tags, it's a no-op. Even with `--pull always` (added in newer Dokploy versions), if the pulled image digest matches the currently running image, no recreation happens.

**Fix**: To actually force containers to restart, use one of:

| Goal | Method |
|------|--------|
| Quick bounce (picks up nothing new) | `dk.restart_container(container_id)` — one per container |
| Force full recreation (picks up env/config) | `dk.stop_compose(compose_id)` then `dk.start_compose(compose_id)` |
| Force recreate with new image digest | Run raw: `docker compose -p {app} up -d --force-recreate --build` |

**Key detail**: `stop_compose()` + `start_compose()` is the most reliable SDK-only way to force container recreation. `stop_compose()` removes the containers entirely, and `start_compose()` runs `docker compose up -d` which then has no choice but to recreate them from scratch.

**Verify restarts actually happened**: Check the container's `StartedAt` timestamp before and after the operation via `docker inspect --format '{{.State.StartedAt}}' {container_id}`. If it didn't change, the container was not recreated.

## Critical Quirk #7: Domains — NO PORT, USE `expose`, NO LABELS

**Symptom (CRITICAL)**: User reports "my domain doesn't work" or agent tells user to visit `my-app.example.com:3000` — that URL is **always wrong**. Apps with Dokploy domains are reached via `https://domain` only, no port.

**Architecture — how Dokploy routes traffic to your app:**

```
Browser → Traefik (host port 80/443) → Docker network → container internal port
```

Dokploy runs **Traefik** as a reverse proxy on the host's ports 80 and 443. When you create a domain via `domain.create` (or the SDK's `domain=` parameter), Dokploy **automatically injects Traefik labels** into your compose file at deploy time via `writeDomainsToCompose()`. The labels look like:

```yaml
labels:
  - traefik.enable=true
  - traefik.http.routers.{appName}-{domainId}-web.rule=Host(`my-app.example.com`)
  - traefik.http.routers.{appName}-{domainId}-web.entrypoints=web
  - traefik.http.services.{appName}-{domainId}-web.loadbalancer.server.port=3000
```

The `loadbalancer.server.port` is the **internal container port** you gave to `domain.create` — NOT a host port. Traefik reaches the container over the shared Docker network (`dokploy-network`), so the port never needs to be published to the host.

**Three rules — memorize these:**

1. **NEVER tell a user to access `domain:port`.** The domain maps to the port internally via Traefik. The user visits `https://domain` only.
2. **NEVER add Traefik labels to your compose file.** Dokploy injects them at deploy time. Manual labels conflict with the auto-injected ones and break routing.
3. **Use `expose`, not `ports`.** `expose: ["3000"]` opens the port within the Docker network only (which is what Traefik uses). `ports:` publishes to the host and bypasses Traefik.

```yaml
services:
  web:
    image: nginx:alpine
    expose:           # ✅ DO THIS — network-only, Traefik reaches it
      - "80"
    # ports:         # ❌ NEVER when a domain is configured
    #   - "80"
    # labels:        # ❌ NEVER add traefik.* — Dokploy does this for you
    #   - traefik.enable=true
```

**Fix** for broken domain routing:

```python
from sdk import DokployClient
dk = DokployClient()

# 1. Verify the domain record exists and points to the right port
domains = dk.get_compose_domains(compose_id)
for d in domains:
    print(f"{d['host']} → service={d['serviceName']} port={d['port']} https={d['https']}")

# 2. Test the domain (NO PORT)
import subprocess
r = subprocess.run(["curl", "-sS", "-I", f"https://{domains[0]['host']}"],
                   capture_output=True, text=True)
print(r.stdout)  # Expect HTTP/2 200 or HTTP/1.1 301

# 3. If broken: remove `ports` from compose, switch to `expose`, redeploy
dk.update_compose(
    compose_id,
    compose_yaml="""services:
  web:
    image: nginx:alpine
    expose:
      - "80"
""",
    auto_redeploy=True,
)
```

**Key detail**: Domain changes (adding/removing/editing) only take effect after a **redeploy** — Traefik reads Docker labels fresh on each deployment. `update_compose()` auto-redeploys by default. If you call `domain.create` manually, you must trigger a deploy afterward.

**Verify Traefik routing** if curl returns 404/502:

```bash
# Inspect the actual labels on the running container
docker inspect --format '{{range $k, $v := .Config.Labels}}{{$k}}={{$v}}{{"\n"}}{{end}}' <container_id> | grep traefik

# Check Traefik logs
docker logs dokploy-traefik --tail 50 | grep -i error
```

If Traefik labels are missing or wrong, the compose needs to be redeployed so `writeDomainsToCompose()` re-injects them.

## References

- **SDK README** (`/opt/data/skills/dokploy/README.md`) — The AI-native guide to the SDK. Contains complete copy-paste workflows for all common operations. Load this FIRST when you need to use the SDK.
- `references/compose-api-errors.md` — Specific error messages, traces, and recovery steps from real sessions.
- `references/sdk-debugging.md` — How to diagnose SDK return-type issues from inside the agent.
