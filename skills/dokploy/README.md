# Dokploy SDK

First-class Python client for the Dokploy API. Handles auth, auto-injection of `serverId`, error passthrough, polling, and high-level workflows that used to take 5-10 API calls.

## Quick Start

```python
from sdk import DokployClient

dk = DokployClient()
result = dk.deploy_compose(
    name="my-app",
    compose_yaml="services:\n  web:\n    image: nginx:alpine",
    env_vars={"KEY": "value"},
    domain="my-app.example.com"
)
```

## Authentication

Set these environment variables (read from `~/.hermes/.env` automatically):

- `DOKPLOY_BASE_URL` — e.g. `https://dokploy.example.com`
- `DOKPLOY_API_TOKEN` — API key from Dokploy UI
- `DOKPLOY_SERVER_ID` — server ID (auto-injected into API calls). Falls back to `PLAYGROUND_SERVER_ID`.

Or pass explicitly: `DokployClient(url="...", token="...", server_id="...")`

## Execution Context

The SDK needs `requests` + `pyyaml`. Install into a venv:

```bash
cd /opt/data/skills/dokploy
python3 -m venv .venv
.venv/bin/pip install requests pyyaml
```

Then invoke with:

```bash
cd /opt/data/skills/dokploy && .venv/bin/python3 -c "from sdk import DokployClient; dk = DokployClient(); print(dk.health_check())"
```

The `helper.py` CLI uses only stdlib (`urllib`) and works with system Python — no venv needed.

**Use `terminal` for SDK/API calls — not `execute_code`.** The `execute_code` sandbox does NOT have access to environment variables (`DOKPLOY_API_TOKEN`, `DOKPLOY_BASE_URL`, `DOKPLOY_SERVER_ID`). Terminal inherits the full environment.

## All High-Level Methods

### Compose Projects

| Method | Description |
|--------|-------------|
| `deploy_compose(name, compose_yaml, ...)` | One-shot deploy a raw docker-compose project. Validates YAML, creates compose, fixes sourceType bug, saves env, adds domain, deploys, polls, prints diagnostics. |
| `update_compose(compose_id, compose_yaml=..., env_vars=..., domain=..., auto_redeploy=True)` | Edit existing compose. Refetches full object automatically (required by Dokploy update). |
| `redeploy(compose_id)` | Trigger redeploy, poll until done, print diagnostics. |
| `start_compose(compose_id)` | Start a stopped compose. |
| `stop_compose(compose_id)` | Stop a running compose. |
| `delete_compose(compose_id, delete_volumes=False)` | Delete a compose permanently. Verifies it's gone. Aliased as `delete()` for backwards compat. |
| `get_compose(compose_id)` | Fetch full compose object. |
| `get_compose_services(compose_id)` | Parse and return `services` dict from the compose file. |
| `save_compose_env(compose_id, env_vars)` | Overwrite env vars for a compose. |
| `get_compose_env(compose_id)` | Best-effort read of env vars (Dokploy has no dedicated read endpoint; falls back to composeFile parsing). |
| `get_compose_deployments(compose_id)` | List deployment records. |
| `get_compose_domains(compose_id)` | List domains attached to a compose. |
| `clear_compose_deployments(compose_id)` | Remove old deployment records. |
| `kill_compose_build(compose_id)` | Kill an in-progress build. |
| `cancel_compose_deployment(compose_id)` | Cancel current deployment. |
| `debug(compose_id)` | Print config, domains, deployments, filesystem logs, container logs, and health in one shot. Returns compose dict. |

### Template Catalog

| Method | Description |
|--------|-------------|
| `deploy_from_template(name, template_id, ...)` | Deploy from the Dokploy template catalog. Auto-fixes sourceType, overlays env vars, adds domain. |
| `list_templates(base_url="")` | List available templates from catalog. |

### Servers

| Method | Description |
|--------|-------------|
| `list_servers()` | List all servers. |
| `get_server(server_id)` | Get one server by ID. |
| `validate_server(server_id="")` | Verify Dokploy can SSH into a server. Auto-uses PLAYGROUND_SERVER_ID. |
| `get_server_metrics(url, token, data_points=50)` | Fetch raw server metrics (if monitoring configured). |
| `list_build_servers()` | List build servers. |
| `get_server_security(server_id="")` | Fetch server security config. |

### Projects & Environments

| Method | Description |
|--------|-------------|
| `list_environments(**filters)` | Search/filter environments. |
| `get_environment(environment_id)` | Get one environment by ID. |
| `create_environment(name, project_id)` | Create a new environment. |
| `list_dokploy_projects(**filters)` | Search Dokploy projects. |
| `get_dokploy_project(project_id)` | Get one project. |
| `create_dokploy_project(name, description="")` | Create a new project. |

### Domains

| Method | Description |
|--------|-------------|
| `create_domain(compose_id, host, service_name, port=3000, https=False)` | Attach a domain to a compose. |
| `delete_domain(domain_id)` | Remove a domain. |
| `get_domain(domain_id)` | Fetch domain details. |

### Applications (non-compose Docker apps)

| Method | Description |
|--------|-------------|
| `list_applications(**filters)` | Search applications. |
| `get_application(application_id)` | Get one application. |
| `deploy_application(application_id)` | Trigger deployment. |
| `redeploy_application(application_id)` | Trigger redeployment. |
| `save_application_env(application_id, env_vars)` | Save env vars. |
| `get_application_logs(application_id, tail=100)` | Read container logs. |

### Docker Containers

| Method | Description |
|--------|-------------|
| `list_containers(server_id="")` | List all containers on a server. |
| `list_containers_by_app(app_name, server_id="")` | List containers by app label. |
| `restart_container(container_id)` | Restart a container. |
| `stop_container(container_id)` | Stop a container. |
| `start_container(container_id)` | Start a container. |
| `kill_container(container_id)` | Kill a container. |

### Deployments

| Method | Description |
|--------|-------------|
| `get_deployments(compose_id)` | List deployments for a compose. |
| `get_deployment_logs(deployment_id, tail=100)` | Read deployment logs via API. |
| `kill_deployment_process(deployment_id)` | Kill a running deployment process. |

### Databases

| Method | Description |
|--------|-------------|
| `list_postgres(**filters)` | Search Postgres services. |
| `create_postgres(name, database_name, database_user, database_password, environment_id="")` | Create managed Postgres. |
| `delete_postgres(postgres_id)` | Remove managed Postgres. |
| `list_redis(**filters)` | Search Redis services. |
| `create_redis(name, password, environment_id="")` | Create managed Redis. |
| `delete_redis(redis_id)` | Remove managed Redis. |

### Health & Version

| Method | Description |
|--------|-------------|
| `health_check()` | Quick Dokploy API health. |
| `get_version()` | Get Dokploy version string. |

## Examples

### Deploy with domain

```python
result = dk.deploy_compose(
    name="my-web",
    compose_yaml="""
services:
  web:
    image: nginx:alpine
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.web.rule=Host(`${WEB_HOST}`)"
""",
    env_vars={"WEB_HOST": "my-web.example.com"},
    domain="my-web.example.com",
    domain_port=80,
)
compose_id = result["compose_id"]
```

### Update env and redeploy

```python
dk.update_compose(
    compose_id,
    env_vars={"API_KEY": "new-secret"},
    auto_redeploy=True,
)
```

### Deploy from template catalog

```python
result = dk.deploy_from_template(
    name="my-n8n",
    template_id="n8n",
    env_vars={"WEBHOOK_URL": "https://n8n.example.com"},
    domain="n8n.example.com",
)
```

### Get diagnostics

```python
dk.debug(compose_id)
```

### List containers for debugging

```python
info = dk.get_compose(compose_id)
app_name = info["appName"]
for c in dk.list_containers_by_app(app_name):
    print(c["Names"], c["State"])
```

## Known API Quirks & Gotchas

1. **sourceType bug** — `POST /compose.create` ALWAYS defaults `sourceType` to `"github"` regardless of payload. SDK workaround: after create, fetch full object via `compose.one`, set `sourceType='raw'`, send entire object back via `compose.update`. Partial payloads are silently ignored by update. The SDK does this automatically; you don't need to worry about it.

2. **Env format** — `/compose.saveEnvironment` expects env as a **STRING** (newline-separated `key=value` pairs), NOT a JSON object. The SDK handles this for you.

3. **Full-payload updates** — `compose.update` requires the **full** object. If you send only changed fields, Dokploy silently ignores them. The SDK's `update_compose()` refetches the full object and merges your changes before sending.

4. **Deployment logs on filesystem** — The Dokploy API is broken for reading deployment logs. You MUST read them from `/opt/dokploy/logs/{appName}/*.log`. The SDK's `debug()` does this for you.

5. **Container logs via API** — Container logs are read via `compose.readLogs` (or `application.readLogs`), not `deployment.readLogs`.

6. **Domain changes need redeploy** — Adding or changing a domain does NOT take effect until you redeploy. The SDK prints warnings and `update_compose()` can auto-redeploy.

7. **Env vars need redeploy** — Saving env vars does NOT restart containers. They only take effect on next deploy/redeploy.

8. **Compose YAML gotcha** — Backtick characters in double-quoted strings MUST NOT be backslash-escaped. `Host(`${WEB_HOST}`)` is correct. `Host(\`${WEB_HOST}\`)` breaks YAML parsing. The SDK validates YAML but does not modify your strings.

## Running Tests

Tests are end-to-end and hit the **real** Dokploy playground API. Clean up is automatic.

```bash
# Ensure env vars are set (loaded from ~/.hermes/.env automatically)
cd ~/.hermes/skills/dokploy
pytest tests/test_sdk.py -v
```

To run a subset:

```bash
pytest tests/test_sdk.py -v -k "deploy_compose or debug"
```

## Common Pitfalls

- **Missing DOKPLOY_BASE_URL / DOKPLOY_API_TOKEN** — SDK raises `ValidationError` immediately on init.
- **Invalid YAML** — `deploy_compose()` validates YAML client-side before hitting the API.
- **Multiple services without domain_service_name** — If your compose has more than one service and you pass a `domain`, you must also pass `domain_service_name` because the SDK can't guess which service to route to.
- **Empty env vars** — Passing `env_vars={}` is fine, but omitting required env vars that the container expects will cause runtime container failures (not SDK errors).
- ** compose.update silently ignores partial payloads** — Never call `_request("POST", "/compose.update", json={"composeId": "...", "composeFile": "..."})` directly. Always use the SDK's `update_compose()` method.
- **Keep your compose file inside backtick quoting safe** — Use single-quoted YAML strings if you need backticks: `Host('` updated.local `')` is invalid; write `Host('updated.local')` instead.
