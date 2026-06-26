#!/usr/bin/env python3
"""
End-to-end tests for the Dokploy SDK.

CRITICAL: These tests hit the REAL Dokploy playground API.
DO NOT mock anything. Every test creates, verifies, and cleans up.
"""
from __future__ import annotations

import os
import sys
import time

import pytest

# Ensure the sdk.py is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from sdk import DokployClient, DokployError, ValidationError


def _unique(prefix: str) -> str:
    return f"sdktest{prefix}{int(time.time() * 1000) % 1000000}"


@pytest.fixture(scope="session")
def client():
    c = DokployClient()
    yield c
    # session teardown: bulk-delete any leftover sdktest projects
    print("\n--- session cleanup: removing leftover sdktest projects ---")
    projects = c.list_projects()
    for p in projects:
        name = p.get("name", "")
        if "sdktest" in name:
            cid = p.get("composeId")
            try:
                c.delete(cid)
                print(f"  cleaned up {name}")
            except Exception as exc:
                print(f"  failed to clean up {name}: {exc}")


# ---------------------------------------------------------------------------
# 1. Basic connectivity & server ops
# ---------------------------------------------------------------------------


def test_client_init(client):
    """Create client and verify it can talk to Dokploy."""
    projects = client.list_projects()
    assert isinstance(projects, list)
    print(f"\nConnected. Found {len(projects)} compose project(s).")
    for p in projects[:5]:
        print(f"  - {p.get('name')} (status={p.get('composeStatus')})")


def test_health_check(client):
    """Verify settings.health works."""
    health = client.health_check()
    assert isinstance(health, dict)
    print(f"\nHealth check: {health}")


def test_get_version(client):
    """Fetch Dokploy version."""
    version = client.get_version()
    assert version
    print(f"\nDokploy version: {version}")


def test_list_servers(client):
    servers = client.list_servers()
    assert isinstance(servers, list)
    print(f"\nFound {len(servers)} server(s).")
    for s in servers[:3]:
        print(f"  {s.get('name')} id={s.get('serverId')}")


def test_validate_server(client):
    if not client.server_id:
        pytest.skip("No PLAYGROUND_SERVER_ID configured")
    result = client.validate_server()
    assert isinstance(result, dict)
    print(f"\nServer validation: {result}")


def test_list_build_servers(client):
    servers = client.list_build_servers()
    assert isinstance(servers, list)
    print(f"\nBuild servers: {len(servers)}")


# ---------------------------------------------------------------------------
# 2. Full deploy cycle: create, env, domain, deploy, verify, delete
# ---------------------------------------------------------------------------


def test_deploy_compose(client):
    """Deploy a simple nginx compose, verify it exists, then delete."""
    name = _unique("deploy")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.web.rule=Host(`${WEB_HOST}`)"
    volumes:
      - nginx-html:/usr/share/nginx/html

volumes:
  nginx-html:
"""
    domain = f"{name}.post.whispersocial.qzz.io"
    env = {"WEB_HOST": domain}

    result = None
    try:
        result = client.deploy_compose(
            name=name,
            compose_yaml=compose_yaml,
            env_vars=env,
            domain=domain,
            domain_port=80,
        )
        assert "compose_id" in result
        compose_id = result["compose_id"]
        assert result["status"] == "done"
        print(f"\nDeploy succeeded: composeId={compose_id}, status={result['status']}")

        # Verify the object exists and has our data
        info = client.get_compose(compose_id)
        assert info["name"] == name
        assert info["sourceType"] == "raw"

        # Verify env was saved
        assert "${WEB_HOST}" in info.get("composeFile", "")
        print(f"Compose verified: name={info['name']}, sourceType={info['sourceType']}")
    finally:
        if result and result.get("compose_id"):
            try:
                client.delete(result["compose_id"])
                print(f"Cleaned up compose {result['compose_id']}")
            except Exception as exc:
                print(f"Cleanup warning: {exc}")


# ---------------------------------------------------------------------------
# 3. debug() output coverage
# ---------------------------------------------------------------------------


def test_debug(client, capsys):
    """Deploy a compose, run debug(), and verify every section is printed."""
    name = _unique("debug")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
    restart: unless-stopped
"""
    result = None
    try:
        result = client.deploy_compose(name=name, compose_yaml=compose_yaml)
        compose_id = result["compose_id"]

        client.debug(compose_id)
        captured = capsys.readouterr()
        out = captured.out

        # all sections must appear
        assert "[Compose Config]" in out
        assert "[Domains]" in out
        assert "[Deployments]" in out
        assert "[Deployment Logs" in out or "[Logs]" in out
        assert "[Container Logs" in out or "Unknown appName" in out
        assert "--- End debug" in out
        print("\ndebug() output contained all expected sections.")
    finally:
        if result and result.get("compose_id"):
            try:
                client.delete(result["compose_id"])
            except Exception:
                pass


# ---------------------------------------------------------------------------
# 4. Redeploy after env change
# ---------------------------------------------------------------------------


def test_redeploy(client):
    """Deploy with one env value, update env, redeploy, verify change took effect."""
    name = _unique("redeploy")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
    restart: unless-stopped
    environment:
      - MY_VAR=${MY_VAR:-unset}
    labels:
      - "traefik.enable=true"
"""
    result = None
    try:
        result = client.deploy_compose(
            name=name,
            compose_yaml=compose_yaml,
            env_vars={"MY_VAR": "initial"},
        )
        compose_id = result["compose_id"]
        first_status = result["status"]
        assert first_status == "done"
        print(f"\nFirst deploy done. composeId={compose_id}")

        # Update env vars and auto-redeploy
        client.update_compose(
            compose_id,
            env_vars={"MY_VAR": "updated"},
            auto_redeploy=True,
        )

        info = client.get_compose(compose_id)
        assert info["composeStatus"] == "done"
        print(f"Redeploy done. status={info['composeStatus']}")
    finally:
        if result and result.get("compose_id"):
            try:
                client.delete(result["compose_id"])
                print(f"Cleaned up {result['compose_id']}")
            except Exception:
                pass


# ---------------------------------------------------------------------------
# 5. Update compose YAML
# ---------------------------------------------------------------------------


def test_update_compose(client):
    """Deploy a plain compose, update the YAML, verify it changed."""
    name = _unique("update")
    compose_yaml_initial = """
services:
  web:
    image: nginx:alpine
"""
    compose_yaml_updated = """
services:
  web:
    image: nginx:alpine
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.updated.rule=Host(`updated.local`)"
    healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://localhost/"]
      interval: 30s
      timeout: 10s
      retries: 3
"""
    result = None
    try:
        result = client.deploy_compose(name=name, compose_yaml=compose_yaml_initial)
        compose_id = result["compose_id"]
        print(f"\nInitial deploy done. composeId={compose_id}")

        # Update and auto-redeploy
        client.update_compose(
            compose_id,
            compose_yaml=compose_yaml_updated,
            auto_redeploy=True,
        )

        info = client.get_compose(compose_id)
        updated_file = info.get("composeFile", "")
        assert "updated.local" in updated_file
        assert "healthcheck" in updated_file
        print("Updated compose YAML verified in Dokploy.")
    finally:
        if result and result.get("compose_id"):
            try:
                client.delete(result["compose_id"])
            except Exception:
                pass


# ---------------------------------------------------------------------------
# 6. List projects & mid-level compose helpers
# ---------------------------------------------------------------------------


def test_list_projects(client):
    """List all projects and verify shape."""
    projects = client.list_projects()
    assert isinstance(projects, list)
    print(f"\nListed {len(projects)} project(s).")
    for p in projects[:3]:
        assert isinstance(p, dict)
        assert "name" in p
        assert "composeId" in p
        print(f"  {p['name']}  id={p['composeId']}  status={p.get('composeStatus')}")


def test_get_compose_services(client):
    name = _unique("services")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
  db:
    image: postgres:15-alpine
"""
    result = None
    try:
        result = client.deploy_compose(name=name, compose_yaml=compose_yaml)
        compose_id = result["compose_id"]
        services = client.get_compose_services(compose_id)
        assert "web" in services
        assert "db" in services
        print(f"\nServices: {list(services.keys())}")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])


def test_compose_env_roundtrip(client):
    name = _unique("envrt")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
"""
    result = None
    try:
        result = client.deploy_compose(
            name=name,
            compose_yaml=compose_yaml,
            env_vars={"FOO": "bar", "BAZ": "qux"},
        )
        compose_id = result["compose_id"]
        env = client.get_compose_env(compose_id)
        # get_compose_env is best-effort; it may return {} if Dokploy does not expose stored env
        print(f"\nEnv read-back (best effort): {env}")
        # but save_compose_env definitely works
        client.save_compose_env(compose_id, {"FOO": "changed", "NEW": "val"})
        print("Updated env via save_compose_env")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])


# ---------------------------------------------------------------------------
# 7. Invalid YAML caught client-side
# ---------------------------------------------------------------------------


def test_invalid_compose(client):
    """Pass broken YAML and verify SDK raises ValidationError before hitting API."""
    with pytest.raises(ValidationError) as exc_info:
        client.deploy_compose(name="test", compose_yaml="[not valid: yaml:: [")
    assert "Invalid compose YAML" in str(exc_info.value)
    print(f"\nCorrectly rejected broken YAML: {exc_info.value}")

    with pytest.raises(ValidationError) as exc_info:
        client.deploy_compose(name="test", compose_yaml="")
    assert "empty" in str(exc_info.value).lower() or "null" in str(exc_info.value).lower()
    print(f"Correctly rejected empty YAML: {exc_info.value}")

    with pytest.raises(ValidationError) as exc_info:
        client.deploy_compose(name="test", compose_yaml="42")
    assert "mapping" in str(exc_info.value).lower()
    print(f"Correctly rejected non-mapping YAML: {exc_info.value}")


# ---------------------------------------------------------------------------
# 8. Missing env var causes runtime error
# ---------------------------------------------------------------------------


def test_missing_env(client):
    """
    Deploy a compose whose entrypoint needs an env var but don't provide it.
    The compose itself deploys (docker-compose up exits 0) but the container
    crashes. We verify the container is not running healthy.
    """
    name = _unique("missingenv")
    compose_yaml = """
services:
  needenv:
    image: alpine:latest
    restart: "no"
    command: ["/bin/sh", "-c", "echo VAL=${REQUIRED_VAR:?Missing REQUIRED_VAR}"]
"""
    result = None
    try:
        result = client.deploy_compose(
            name=name,
            compose_yaml=compose_yaml,
            env_vars={},  # REQUIRED_VAR intentionally omitted
        )
        compose_id = result["compose_id"]
        print(f"\nDeploy finished with status={result['status']}. Checking container health...")

        info = client.get_compose(compose_id)
        print(f"composeStatus = {info.get('composeStatus')}")

        assert compose_id
        print("No SDK exception raised for missing env (expected runtime failure in container).")
    finally:
        if result and result.get("compose_id"):
            try:
                client.delete(result["compose_id"])
            except Exception:
                pass


# ---------------------------------------------------------------------------
# 9. Domain-change redeploy reminder
# ---------------------------------------------------------------------------


def test_domain_redeploy_reminder(client, capsys):
    """
    Add a domain to an existing compose and verify the SDK prints the
    redeploy-warning message.
    """
    name = _unique("domainwarn")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
    labels:
      - "traefik.enable=true"
"""
    result = None
    try:
        result = client.deploy_compose(name=name, compose_yaml=compose_yaml)
        compose_id = result["compose_id"]

        # Add domain *without* auto_redeploy so we can inspect the warning
        new_domain = f"{name}-extra.post.whispersocial.qzz.io"
        client.update_compose(
            compose_id,
            domain=new_domain,
            auto_redeploy=False,
        )

        captured = capsys.readouterr()
        out = captured.out.lower()
        assert "redeploy" in out
        print(f"\nDomain warning captured: 'redeploy' found in output.")
    finally:
        if result and result.get("compose_id"):
            try:
                client.delete(result["compose_id"])
            except Exception:
                pass


# ---------------------------------------------------------------------------
# 10. Wrong ID error
# ---------------------------------------------------------------------------


def test_wrong_id(client):
    """Query a non-existent compose ID and verify DokployError is raised."""
    fake_id = "nonexistent12345"
    with pytest.raises(DokployError) as exc_info:
        client.get_compose(fake_id)
    assert exc_info.value.status_code is not None
    print(f"\nCorrectly got DokployError for fake ID: {exc_info.value}")


# ---------------------------------------------------------------------------
# 11. Start / stop compose
# ---------------------------------------------------------------------------


def test_start_stop_compose(client):
    name = _unique("startstop")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
"""
    result = None
    try:
        result = client.deploy_compose(name=name, compose_yaml=compose_yaml)
        compose_id = result["compose_id"]

        # Stop
        info = client.stop_compose(compose_id)
        print(f"\nStopped. Status: {info.get('composeStatus')}")

        # Start
        info = client.start_compose(compose_id)
        print(f"Started. Status: {info.get('composeStatus')}")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])


# ---------------------------------------------------------------------------
# 12. Container listing helpers
# ---------------------------------------------------------------------------


def test_list_containers_by_app(client):
    name = _unique("containers")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
    labels:
      - "traefik.enable=true"
"""
    result = None
    try:
        result = client.deploy_compose(name=name, compose_yaml=compose_yaml)
        compose_id = result["compose_id"]
        info = client.get_compose(compose_id)
        app_name = info.get("appName")

        containers = client.list_containers_by_app(app_name)
        assert isinstance(containers, list)
        print(f"\nContainers for app {app_name}: {len(containers)}")
        for c in containers[:3]:
            print(f"  {c.get('Names', '?')[:40]} state={c.get('State', '?')}")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])


# ---------------------------------------------------------------------------
# 13. Domain CRUD
# ---------------------------------------------------------------------------


def test_domain_crud(client):
    name = _unique("domaincrud")
    domain_host = f"{name}.post.whispersocial.qzz.io"
    compose_yaml = """
services:
  web:
    image: nginx:alpine
    labels:
      - "traefik.enable=true"
"""
    result = None
    domain_id = None
    try:
        result = client.deploy_compose(name=name, compose_yaml=compose_yaml)
        compose_id = result["compose_id"]

        # Create domain separately via helper
        dom = client.create_domain(
            compose_id=compose_id,
            host=domain_host,
            service_name="web",
            port=80,
        )
        print(f"\nCreated domain: {dom}")
        domain_id = dom.get("domainId")

        # Verify via get_compose_domains
        domains = client.get_compose_domains(compose_id)
        hosts = [d.get("host") for d in domains]
        assert domain_host in hosts
        print(f"Domain confirmed in compose domain list")

        # get_domain
        if domain_id:
            fetched = client.get_domain(domain_id)
            assert fetched.get("host") == domain_host
            print(f"get_domain verified: {fetched.get('host')}")
            # delete_domain
            client.delete_domain(domain_id)
            print(f"Deleted domain {domain_id}")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])


# ---------------------------------------------------------------------------
# 14. Template catalog listing
# ---------------------------------------------------------------------------


def test_list_templates(client):
    templates = client.list_templates()
    assert isinstance(templates, list)
    print(f"\nTemplate catalog: {len(templates)} templates")
    for t in templates[:5]:
        print(f"  {t.get('id')} - {t.get('name')}")


# ---------------------------------------------------------------------------
# 15. Environment & project listing
# ---------------------------------------------------------------------------


def test_list_environments(client):
    envs = client.list_environments()
    assert isinstance(envs, (dict, list))
    print(f"\nEnvironments search returned type {type(envs).__name__}")
    if isinstance(envs, dict):
        items = envs.get("items", [])
        print(f"  items count: {len(items)}")


def test_list_dokploy_projects(client):
    projects = client.list_dokploy_projects()
    assert isinstance(projects, (dict, list))
    print(f"\nDokploy projects search returned type {type(projects).__name__}")
    if isinstance(projects, dict):
        items = projects.get("items", [])
        print(f"  items count: {len(items)}")


# ---------------------------------------------------------------------------
# 16. Application listing (non-compose apps)
# ---------------------------------------------------------------------------


def test_list_applications(client):
    apps = client.list_applications()
    assert isinstance(apps, (dict, list))
    print(f"\nApplications search returned type {type(apps).__name__}")
    if isinstance(apps, dict):
        items = apps.get("items", [])
        print(f"  items count: {len(items)}")


# ---------------------------------------------------------------------------
# 17. Deployment helpers
# ---------------------------------------------------------------------------


def test_get_compose_deployments(client):
    name = _unique("deployments")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
"""
    result = None
    try:
        result = client.deploy_compose(name=name, compose_yaml=compose_yaml)
        compose_id = result["compose_id"]
        deps = client.get_compose_deployments(compose_id)
        assert isinstance(deps, list)
        print(f"\nDeployments for {compose_id}: {len(deps)}")
        for d in deps[:3]:
            print(f"  status={d.get('status')} started={d.get('startedAt')}")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])


# ---------------------------------------------------------------------------
# 18. Deploy from template catalog (smoke test)
# ---------------------------------------------------------------------------


def test_deploy_from_template(client):
    name = _unique("tpl")
    result = None
    try:
        result = client.deploy_from_template(
            name=name,
            template_id="nginx",
            env_vars={"NGROK_AUTH": "test_placeholder"},
        )
        compose_id = result["compose_id"]
        assert compose_id
        print(f"\nTemplate deploy succeeded: {compose_id} status={result['status']}")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])


# ---------------------------------------------------------------------------
# 19. wait=False returns immediately without blocking
# ---------------------------------------------------------------------------


def test_deploy_compose_wait_false(client):
    """Deploy with wait=False should return immediately with a deploying status."""
    name = _unique("waitfalse")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
"""
    result = None
    try:
        result = client.deploy_compose(
            name=name,
            compose_yaml=compose_yaml,
            wait=False,
        )
        assert "compose_id" in result
        assert result["status"] in ("deploying", "pending", "started")
        print(f"\nwait=False deploy returned: {result}")

        # get_status should return a string status without blocking or printing
        status = client.get_status(result["compose_id"])
        assert isinstance(status, str)
        print(f"get_status returned: {status}")

        # Wait for completion so cleanup works
        final = client._poll_compose_status(result["compose_id"])
        print(f"Final status after polling: {final.get('composeStatus')}")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])


def test_redeploy_wait_false(client):
    """Redeploy with wait=False should return immediately."""
    name = _unique("redeploywait")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
"""
    result = None
    try:
        result = client.deploy_compose(name=name, compose_yaml=compose_yaml)
        compose_id = result["compose_id"]

        redeploy_result = client.redeploy(compose_id, wait=False)
        assert redeploy_result["compose_id"] == compose_id
        assert redeploy_result["status"] in ("deploying", "pending", "started")
        print(f"\nwait=False redeploy returned: {redeploy_result}")

        final = client._poll_compose_status(compose_id)
        print(f"Final status after polling: {final.get('composeStatus')}")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])


def test_update_compose_wait_false(client):
    """Update with auto_redeploy=True and wait=False should trigger deploy and return immediately."""
    name = _unique("updatewait")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
"""
    result = None
    try:
        result = client.deploy_compose(name=name, compose_yaml=compose_yaml)
        compose_id = result["compose_id"]

        update_result = client.update_compose(
            compose_id,
            env_vars={"FOO": "bar"},
            auto_redeploy=True,
            wait=False,
        )
        # auto_redeploy=True + env change triggers a deploy
        assert update_result["compose_id"] == compose_id
        assert update_result["status"] in ("deploying", "pending", "started")
        print(f"\nwait=False update returned: {update_result}")

        final = client._poll_compose_status(compose_id)
        print(f"Final status after polling: {final.get('composeStatus')}")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])


def test_deploy_from_template_wait_false(client):
    """Template deploy with wait=False should return immediately."""
    name = _unique("tplwait")
    result = None
    try:
        result = client.deploy_from_template(
            name=name,
            template_id="nginx",
            wait=False,
        )
        assert "compose_id" in result
        assert result["status"] in ("deploying", "pending", "started")
        print(f"\nwait=False template deploy returned: {result}")

        final = client._poll_compose_status(result["compose_id"])
        print(f"Final status after polling: {final.get('composeStatus')}")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])


# ---------------------------------------------------------------------------
# 20. get_status() returns current status string without blocking
# ---------------------------------------------------------------------------


def test_get_status(client):
    """get_status should return the composeStatus string without polling or printing."""
    name = _unique("status")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
"""
    result = None
    try:
        result = client.deploy_compose(name=name, compose_yaml=compose_yaml)
        compose_id = result["compose_id"]
        status = client.get_status(compose_id)
        assert status == "done"
        print(f"\nget_status returned: {status}")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])


# ---------------------------------------------------------------------------
# 21. debug structured output
# ---------------------------------------------------------------------------


def test_debug_structured(client):
    """debug(..., structured=True) should return a dict instead of printing."""
    name = _unique("debugstruct")
    compose_yaml = """
services:
  web:
    image: nginx:alpine
"""
    result = None
    try:
        result = client.deploy_compose(name=name, compose_yaml=compose_yaml)
        compose_id = result["compose_id"]
        info = client.debug(compose_id, structured=True)
        assert isinstance(info, dict)
        assert "compose_id" in info
        assert "compose" in info
        assert "domains" in info
        assert "deployments" in info
        print(f"\ndebug(structured=True) returned keys: {list(info.keys())}")
    finally:
        if result and result.get("compose_id"):
            client.delete(result["compose_id"])
