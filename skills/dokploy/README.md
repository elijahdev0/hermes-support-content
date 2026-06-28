# Dokploy SDK — AI-Native Guide

First-class Python client for the Dokploy API. Every list method returns a flat `list[dict]`. High-level methods do 5-10 API calls in one shot. Use this guide to fly through operations in the fewest tool calls possible.

## Execution Context

The SDK lives at `/opt/data/skills/dokploy/sdk.py`. It needs `requests` + `pyyaml` in `.venv/`.

```bash
cd /opt/data/skills/dokploy && .venv/bin/python3 -c "..."
```

**Use `terminal` for SDK calls — not `execute_code`.** The `execute_code` sandbox has no env vars. Terminal does.

For one-off API calls where the SDK is overkill, `helper.py` works with system Python (stdlib only):

```bash
python3 /opt/data/skills/dokploy/helper.py call /compose.create '{"name":"my-app"}'
```

## Return Type Guarantee

**Every list/search method returns a flat `list[dict]`.** No paginated wrappers, no mixed shapes, no `isinstance()` guards needed:

```python
dk.list_projects()         # list[dict] — compose projects
dk.list_dokploy_projects() # list[dict] — Dokploy projects
dk.list_environments()     # list[dict]
dk.list_servers()          # list[dict]
dk.list_containers()       # list[dict]
dk.list_applications()     # list[dict]
dk.list_postgres()         # list[dict]
dk.list_redis()            # list[dict]
dk.list_templates()        # list[dict]

# Always safe — no isinstance() check needed:
for item in dk.list_projects():
    print(item["name"])
```

The `_unwrap_search_result()` helper normalizes everything internally. You never think about it.

## Workflows

These are complete, copy-paste scripts. Each one accomplishes a goal in a single `terminal` call.

### Show me everything (full system status)

```python
from sdk import DokployClient
dk = DokployClient()

print(f"Dokploy {dk.get_version()} — {dk.health_check()['status']}")
print()

for s in dk.list_servers():
    print(f"Server: {s['name']} ({s.get('ipAddress','?')})")

for p in dk.list_dokploy_projects():
    print(f"Project: {p['name']}")

for e in dk.list_environments():
    print(f"Environment: {e['name']}")

print(f"\nComposes ({len(dk.list_projects())}):")
for c in dk.list_projects():
    domains = dk.get_compose_domains(c['composeId'])
    print(f"  {c['name']}  status={c['composeStatus']}  domains={[d['host'] for d in domains]}")

print(f"\nApplications: {len(dk.list_applications())}")
print(f"Postgres: {len(dk.list_postgres())}  Redis: {len(dk.list_redis())}")

print(f"\nContainers ({len(dk.list_containers())}):")
for c in dk.list_containers():
    print(f"  {c['name']:30s}  state={c['state']:10s}  {c['status']}")

running = sum(1 for c in dk.list_containers() if c['state'] == 'running')
print(f"  => {running} running")
```

### What's wrong with this service? (full diagnostics)

```python
from sdk import DokployClient
dk = DokployClient()

for c in dk.list_projects():
    dk.debug(c['composeId'])  # config + domains + deployments + filesystem logs + container logs
```

`debug()` does everything in one call. Never piece together log reads manually — this is the method.

### Deploy a new service

```python
from sdk import DokployClient
dk = DokployClient()

result = dk.deploy_compose(
    name="my-app",
    compose_yaml="""services:
  web:
    image: nginx:alpine""",
    env_vars={"FOO": "bar"},
    domain="my-app.example.com",
    domain_port=80,
)
# Blocks until done. Prints diagnostics automatically.
# Returns {"compose_id": "...", "status": "done", "domain": "..."}
```

### Deploy from the template catalog

```python
from sdk import DokployClient
dk = DokployClient()

# List what's available
for t in dk.list_templates():
    print(t.get("id"), t.get("name"))

# Deploy one
result = dk.deploy_from_template(
    name="my-n8n",
    template_id="n8n",
    env_vars={"WEBHOOK_URL": "https://n8n.example.com"},
    domain="n8n.example.com",
)
```

### Update env vars and redeploy

```python
from sdk import DokployClient
dk = DokployClient()

dk.update_compose(
    compose_id,
    env_vars={"API_KEY": "new-secret"},
    auto_redeploy=True,  # default: blocks until done
)
```

### Add a domain to an existing compose

```python
from sdk import DokployClient
dk = DokployClient()

dk.update_compose(
    compose_id,
    domain="new-domain.example.com",
    domain_service_name="web",
    domain_port=3000,
    auto_redeploy=True,
)
```

### Restart / stop / start a compose

```python
from sdk import DokployClient
dk = DokployClient()

dk.stop_compose(compose_id)
dk.start_compose(compose_id)
dk.redeploy(compose_id)  # triggers a new deployment
```

### Delete a compose (permanent)

```python
from sdk import DokployClient
dk = DokployClient()

dk.delete_compose(compose_id)  # verifies it's gone
```

### Create a managed database

```python
from sdk import DokployClient
dk = DokployClient()

dk.create_postgres(
    name="my-db",
    database_name="appdb",
    database_user="appuser",
    database_password="secure-password",
)

dk.create_redis(
    name="my-cache",
    password="redis-password",
)
```

### Restart / stop a specific container

```python
from sdk import DokployClient
dk = DokployClient()

# Find the container
for c in dk.list_containers():
    if c['name'] == 'my-app-web':
        dk.restart_container(c['containerId'])
```

## Efficiency Rules

When an agent reads this README, it should follow these rules:

1. **One terminal call per goal.** Never chain 3-4 calls when one script can do everything. Combine listing, diagnostics, and health checks into a single Python script.

2. **`debug()` is the diagnostics method.** When the user asks "what's wrong" or "show logs" or "status of X" — use `debug(compose_id)`. It prints config, domains, deployments, filesystem logs, and container logs in one shot. Do not manually assemble log reads with bash `tail` or separate API calls.

3. **Never probe return shapes.** All list methods return flat `list[dict]`. Iterate directly. No `isinstance()`, no `json.dumps()` to discover shapes.

4. **Deploy methods block by default.** `deploy_compose()`, `deploy_from_template()`, `update_compose()`, and `redeploy()` all poll until done. You don't need to check status afterward — the method prints it. If you need fire-and-forget, pass `wait=False`.

5. **Batch parallel reads.** If checking multiple composes, loop over `dk.list_projects()` and call `dk.debug()` for each — all in one script. Don't make separate calls per compose.

## How Dokploy Handles Errors (Tested)

When a deployment fails, what you get depends on the error type. This table tells you where to look:

| Failure | composeStatus | Deployment errorMessage | Filesystem log? | How to diagnose |
|---|---|---|---|---|
| Bad YAML syntax | `error` | `null` | No log written | SDK catches this client-side before API call. If bypassing SDK: no error message anywhere. |
| Bad image (doesn't exist) | stays `running` | `null` | Yes, in `/opt/dokploy/logs/` | `debug()` reads the filesystem log — Docker pull error is there. |
| Port conflict | `idle` | N/A (no deployment created) | No log written | Silently swallowed. Check `list_projects()` — status stays `idle` with no deployments. |
| Missing required field | N/A | N/A | N/A | Dokploy returns HTTP 400 with Zod validation error. SDK surfaces it as `DokployError`. |
| Docker runtime error | `error` | `null` | Yes | `debug()` shows Docker error in filesystem log. |
| Template not found | N/A | N/A | N/A | Dokploy returns HTTP 500 "Template files not found". |

Key takeaways for debugging:

- **`composeStatus: "error"` with no log files** = bad YAML. The compose file itself is broken. Rerun with valid YAML.
- **`composeStatus: "running"` but containers aren't up** = Docker pull or runtime failure. Read the filesystem log via `debug()`.
- **`composeStatus: "idle"` after deploy** = port conflict or Docker daemon issue. No error trail — check port availability.
- **`errorMessage` in deployment records is always `null`** — never rely on it. Always check filesystem logs via `debug()`.

The SDK's `debug()` method reads filesystem logs automatically. Use it as the first diagnostic tool for any failed deployment — not the deployment API response.

## Method Reference

### Compose Projects

| Method | Description |
|--------|-------------|
| `deploy_compose(name, compose_yaml, ...)` | Create + fix sourceType + save env + add domain + deploy + poll + print diagnostics. |
| `update_compose(compose_id, compose_yaml=..., env_vars=..., domain=..., auto_redeploy=True)` | Edit compose. Refetches full object automatically. |
| `redeploy(compose_id)` | Trigger redeploy, poll until done. |
| `start_compose(compose_id)` | Start a stopped compose. |
| `stop_compose(compose_id)` | Stop a running compose. |
| `delete_compose(compose_id, delete_volumes=False)` | Delete permanently. Verifies it's gone. |
| `get_compose(compose_id)` | Fetch full compose object. |
| `get_compose_services(compose_id)` | Parse services dict from compose file. |
| `save_compose_env(compose_id, env_vars)` | Overwrite env vars (string format handled automatically). |
| `get_compose_env(compose_id)` | Best-effort read of env vars. |
| `get_compose_deployments(compose_id)` | List deployment records. |
| `list_projects()` | List all compose projects with status. Returns `list[dict]`. |
| `debug(compose_id)` | One-shot: config, domains, deployments, filesystem logs, container logs. |

### Template Catalog

| Method | Description |
|--------|-------------|
| `deploy_from_template(name, template_id, ...)` | Deploy from template catalog. Auto-fixes sourceType. |
| `list_templates(base_url="")` | List available templates. Returns `list[dict]`. |

### Servers

| Method | Description |
|--------|-------------|
| `list_servers()` | List all servers. Returns `list[dict]`. |
| `get_server(server_id)` | Get one server by ID. |
| `validate_server(server_id="")` | Verify Dokploy can SSH into server. |
| `get_server_metrics(url, token, data_points=50)` | Fetch raw server metrics. |

### Projects & Environments

| Method | Description |
|--------|-------------|
| `list_environments(**filters)` | Search environments. Returns `list[dict]`. |
| `get_environment(environment_id)` | Get one environment. |
| `list_dokploy_projects(**filters)` | Search Dokploy projects. Returns `list[dict]`. |
| `get_dokploy_project(project_id)` | Get one project. |
| `create_dokploy_project(name, description="")` | Create a new project. |

### Docker Containers

| Method | Description |
|--------|-------------|
| `list_containers(server_id="")` | List all containers. Returns `list[dict]`. |
| `list_containers_by_app(app_name, server_id="")` | List containers by app label. |
| `restart_container(container_id)` | Restart a container. |
| `stop_container(container_id)` | Stop a container. |
| `start_container(container_id)` | Start a container. |
| `kill_container(container_id)` | Kill a container. |

### Databases

| Method | Description |
|--------|-------------|
| `list_postgres(**filters)` | Search Postgres. Returns `list[dict]`. |
| `create_postgres(name, database_name, database_user, database_password)` | Create managed Postgres. |
| `delete_postgres(postgres_id)` | Remove managed Postgres. |
| `list_redis(**filters)` | Search Redis. Returns `list[dict]`. |
| `create_redis(name, password)` | Create managed Redis. |
| `delete_redis(redis_id)` | Remove managed Redis. |

## Known API Quirks (handled automatically)

These are SDK-internal workarounds. You don't need to worry about them, but know they exist:

1. **sourceType bug** — `POST /compose.create` defaults `sourceType` to `"github"` regardless of payload. SDK automatically fetches the full object and patches it to `"raw"` after every create.

2. **Env format** — `/compose.saveEnvironment` expects a newline-separated `key=value` string, not JSON. SDK handles the conversion.

3. **Full-payload updates** — `compose.update` silently ignores partial payloads. SDK's `update_compose()` always refetches the full object.

4. **Deployment logs** — Dokploy API is broken for deployment log reads. SDK's `debug()` reads them from `/opt/dokploy/logs/{appName}/*.log` on the filesystem.

5. **Domain/env changes need redeploy** — Adding domains or changing env does not take effect until you redeploy. SDK's `update_compose()` auto-redeploys by default.

## Common Pitfalls

- **Missing credentials** — SDK raises `ValidationError` immediately if `DOKPLOY_BASE_URL` or `DOKPLOY_API_TOKEN` is missing.
- **Invalid YAML** — `deploy_compose()` validates YAML client-side before hitting the API.
- **Multiple services + domain** — Pass `domain_service_name=` when your compose has more than one service and you're adding a domain.
- **Never call `_request()` directly for updates** — Always use `update_compose()`. Direct partial updates are silently ignored by Dokploy.
- **Backtick quoting in YAML** — `Host(\`${VAR}\`)` breaks YAML. Use `Host(${VAR})` (no backslash before backticks).
