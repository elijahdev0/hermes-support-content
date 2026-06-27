
"""
Dokploy SDK - first-class Python client for the Dokploy API.

Replaces the need for most raw subprocess calls when working with Dokploy.
Handles auth, auto-injection of serverId, error passthrough, polling,
and high-level workflows that used to take 5-10 API calls.

Usage:
    from sdk import DokployClient

    dk = DokployClient()
    result = dk.deploy_compose(
        name="my-app",
        compose_yaml="...",
        env_vars={"KEY": "value"},
        domain="my-app.example.com"
    )
"""

from __future__ import annotations

import json
import os
import random
import re
import string
import time
from typing import Any
from urllib.parse import urljoin

import requests
import yaml


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

default_base_url = os.environ.get("DOKPLOY_BASE_URL", "").rstrip("/")
default_token = os.environ.get("DOKPLOY_API_TOKEN", "")
default_server_id = os.environ.get("DOKPLOY_SERVER_ID") or os.environ.get("PLAYGROUND_SERVER_ID", "")


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class DokployError(Exception):
    """Raised when the Dokploy API returns an error response."""

    def __init__(self, message: str, status_code: int | None = None, response_body: Any = None):
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class ValidationError(DokployError):
    """Raised when input fails client-side validation before the API is called."""


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

_APP_NAME_RE = re.compile(r"^[a-zA-Z0-9._-]+$")
_DOMAIN_RE = re.compile(
    r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)*"
    r"[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?$"
)


def _validate_app_name(name: str) -> None:
    if not (1 <= len(name) <= 63):
        raise ValidationError(
            f"appName must be 1-63 characters, got {len(name)}: {name!r}"
        )
    if not _APP_NAME_RE.match(name):
        raise ValidationError(
            f"appName must match ^[a-zA-Z0-9._-]+$, got {name!r}"
        )


def _validate_compose_yaml(text: str) -> dict:
    try:
        parsed = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise ValidationError(f"Invalid compose YAML: {exc}")
    if parsed is None:
        raise ValidationError("Compose YAML is empty or parses to null")
    if not isinstance(parsed, dict):
        raise ValidationError("Compose YAML must be a mapping at the top level")
    if "version" in parsed and not isinstance(parsed["version"], str):
        raise ValidationError("Compose 'version' field must be a string")
    return parsed


def _validate_env_vars(env: dict[str, str]) -> None:
    if not isinstance(env, dict):
        raise ValidationError(f"env_vars must be a dict, got {type(env).__name__}")
    for key, value in env.items():
        if not isinstance(key, str):
            raise ValidationError(f"env var key must be a string, got {type(key).__name__}")
        if not key:
            raise ValidationError("env var key must not be empty")
        if not isinstance(value, str):
            raise ValidationError(f"env var value for {key!r} must be a string, got {type(value).__name__}")
        if "\n" in key:
            raise ValidationError(f"env var key must not contain newlines: {key!r}")


def _validate_domain(host: str) -> None:
    if not host or not _DOMAIN_RE.match(host):
        raise ValidationError(f"Invalid domain format: {host!r}")


def _rnd_id(prefix: str = "sdk", length: int = 8) -> str:
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return f"{prefix}-{suffix}"


# ---------------------------------------------------------------------------
# Low-level + high-level client
# ---------------------------------------------------------------------------

class DokployClient:
    """
    Low-level API passthrough + high-level Dokploy workflows.
    """

    def __init__(
        self,
        url: str = "",
        token: str = "",
        server_id: str = "",
    ):
        self.url = (url or default_base_url).rstrip("/")
        self.token = token or default_token
        self.server_id = server_id or default_server_id
        self.session = requests.Session()
        self.session.headers.update({
            "x-api-key": self.token,
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

        if not self.url:
            raise ValidationError("Dokploy base URL is required (pass url= or set DOKPLOY_BASE_URL)")
        if not self.token:
            raise ValidationError("Dokploy API token is required (pass token= or set DOK==PLOY_API_TOKEN)")

    # -----------------------------------------------------------------------
    # Raw request primitives
    # -----------------------------------------------------------------------

    def _request(self, method: str, path: str, **kwargs) -> Any:
        """Make an authenticated request and return parsed JSON."""
        url = urljoin(self.url + "/", "api" + path)
        resp = self.session.request(method, url, **kwargs)
        try:
            resp.raise_for_status()
        except requests.HTTPError as exc:
            body = None
            try:
                body = resp.json()
            except Exception:
                body = resp.text
            raise DokployError(
                message=f"HTTP {resp.status_code}: {method.upper()} {path}",
                status_code=resp.status_code,
                response_body=body,
            ) from exc
        if resp.status_code == 204 or not resp.text:
            return None
        try:
            return resp.json()
        except json.JSONDecodeError:
            return resp.text

    def get(self, path: str, params: dict | None = None) -> Any:
        return self._request("GET", path, params=params or {})

    def post(self, path: str, json_body: dict | None = None) -> Any:
        return self._request("POST", path, json=json_body or {})

    def put(self, path: str, json_body: dict | None = None) -> Any:
        return self._request("PUT", path, json=json_body or {})

    def delete(self, path: str, json_body: dict | None = None) -> Any:
        return self._request("DELETE", path, json=json_body or {})

    # -----------------------------------------------------------------------
    # serverId injection helper
    # -----------------------------------------------------------------------

    def _with_server_id(self, payload: dict | None) -> dict:
        """Auto-inject serverId into payloads if configured and absent."""
        payload = dict(payload or {})
        if self.server_id and "serverId" not in payload:
            payload["serverId"] = self.server_id
        return payload

    # =====================================================================
    #  INTERNAL HELPERS (used by high-level workflows)
    # =====================================================================

    def _find_default_environment(self) -> str:
        """Find the first available environment ID."""
        result = self.environment_search()
        if isinstance(result, dict):
            items = result.get("items", [])
        else:
            items = result or []
        if isinstance(items, list) and items:
            first = items[0]
            eid = first.get("id") or first.get("environmentId")
            if eid:
                return eid
        raise DokployError("No environment found - create one in Dokploy UI or pass environment_id= explicitly")

    def _get_full_compose(self, compose_id: str) -> dict:
        return self.get("/compose.one", params={"composeId": compose_id})

    def _update_source_type_raw(self, compose_id: str) -> dict:
        """
        Critical workaround: compose.create defaults sourceType to "github"
        regardless of what you pass. Fetch full object and force it to "raw".
        """
        full = self._get_full_compose(compose_id)
        full["sourceType"] = "raw"
        return self.post("/compose.update", json_body=full)

    def get_status(self, compose_id: str) -> str:
        """Return the current composeStatus string without blocking or printing."""
        info = self._get_full_compose(compose_id)
        return info.get("composeStatus", "unknown")

    def _poll_compose_status(
        self,
        compose_id: str,
        target_statuses: tuple[str, ...] = ("done", "error"),
        interval: float = 3.0,
        timeout: float = 120.0,
    ) -> dict:
        """Wait until compose reaches one of the target statuses."""
        deadline = time.time() + timeout
        last = "unknown"
        while time.time() < deadline:
            status = self.get_status(compose_id)
            if status != last:
                last = status
                print(f"  [poll] composeStatus = {status}")
            if status in target_statuses:
                return self._get_full_compose(compose_id)
            time.sleep(interval)
        raise DokployError(f"Polling timed out after {timeout}s. Last status: {last}")

    # =====================================================================
    #  HIGH-LEVEL: deploy a compose project
    # =====================================================================

    def deploy_compose(
        self,
        name: str,
        compose_yaml: str,
        env_vars: dict[str, str] | None = None,
        domain: str | None = None,
        app_name: str = "",
        environment_id: str = "",
        server_id: str = "",
        domain_service_name: str = "",
        domain_port: int | None = None,
        wait: bool = True,
    ) -> dict:
        """
        One-shot deploy of a raw compose project.

        Parameters
        ----------
        name: Compose project name.
        compose_yaml: Raw docker-compose.yml content.
        env_vars: Environment variables to set before deploying.
        domain: Hostname to route to this compose (e.g. "my-app.example.com").
        app_name: Optional override for the appName label.
        environment_id: Dokploy environment ID (auto-detected if omitted).
        server_id: Server ID (auto-detected if omitted).
        domain_service_name: Service name the domain should target. If left
            empty and only one service exists in compose_yaml, auto-detects it.
        domain_port: Port to bind the domain to (defaults to 3000).
        wait: If True (default), block until deployment completes and return
            final status. If False, trigger the operation and return immediately
            with ``{"compose_id": ..., "status": "deploying"}``.

        Warnings
        --------
        - Environment variables take effect on next deploy.
        - Changing the domain requires a redeploy to take effect.
        """
        # validation
        if not name or not isinstance(name, str):
            raise ValidationError("name must be a non-empty string")
        parsed = _validate_compose_yaml(compose_yaml)
        env_vars = env_vars or {}
        _validate_env_vars(env_vars)
        if domain:
            _validate_domain(domain)
        if app_name:
            _validate_app_name(app_name)

        # Extract available services for domain mapping
        services = parsed.get("services", dict()) if isinstance(parsed, dict) else {}
        available_services = list(services.keys()) if isinstance(services, dict) else []

        # Auto-resolve domain service name
        resolved_service_name = domain_service_name
        if domain and not resolved_service_name:
            if len(available_services) == 1:
                resolved_service_name = available_services[0]
            elif not available_services:
                raise ValidationError("Compose YAML has no services; cannot add a domain")
            else:
                raise ValidationError(
                    f"Multiple services found ({available_services}) - pass domain_service_name="
                )

        resolved_port = domain_port if domain_port is not None else 3000

        env_id = environment_id or self._find_default_environment()
        sid = server_id or self.server_id

        print(f"-> Creating compose project '{name}'...")
        create_payload = self._with_server_id({
            "name": name,
            "description": f"Deployed via SDK - {name}",
            "environmentId": env_id,
            "composeType": "docker-compose",
            "appName": app_name or re.sub(r"[^a-zA-Z0-9._-]", "-", name).strip("-"),
            "composeFile": compose_yaml,
            "sourceType": "raw",
        })
        compose = self.post("/compose.create", json_body=create_payload)
        compose_id = compose["composeId"]
        print(f"  Created composeId = {compose_id}")

        # Work around the sourceType bug
        print("-> Fixing sourceType (workaround for API defaulting to 'github')...")
        fixed = self._update_source_type_raw(compose_id)
        print(f"  sourceType = {fixed.get('sourceType')}")

        # Save environment variables
        if env_vars:
            print("-> Saving environment variables...")
            env_string = "\n".join(f"{k}={v}" for k, v in env_vars.items())
            self.post("/compose.saveEnvironment", json_body={
                "composeId": compose_id,
                "env": env_string,
            })
            print(f"  Saved {len(env_vars)} variable(s)")
            print("  ! WARNING: Environment variables take effect on next deploy")

        # Add domain if requested
        if domain:
            print(f"-> Adding domain '{domain}' -> service '{resolved_service_name}', port {resolved_port}...")
            self.post("/domain.create", json_body=self._with_server_id({
                "host": domain,
                "composeId": compose_id,
                "domainType": "compose",
                "https": False,
                "certificateType": "none",
                "serviceName": resolved_service_name,
                "port": resolved_port,
            }))
            print(f"  Domain added")
            print("  ! WARNING: Changing the domain requires a redeploy to take effect")

        # Deploy
        print("-> Triggering deployment...")
        self.post("/compose.deploy", json_body={"composeId": compose_id})

        if not wait:
            return {
                "compose_id": compose_id,
                "status": "deploying",
                "domain": domain,
            }

        # Poll
        print("-> Waiting for deployment to complete...")
        final = self._poll_compose_status(compose_id)
        status = final.get("composeStatus")
        print(f"  Final status: {status}")

        # Diagnostics
        print("\n" + "=" * 50)
        self.debug(compose_id)
        print("=" * 50)

        return {
            "compose_id": compose_id,
            "compose": final,
            "status": status,
            "domain": domain,
        }

    # =====================================================================
    #  HIGH-LEVEL: update an existing compose
    # =====================================================================

    def update_compose(
        self,
        compose_id: str,
        compose_yaml: str | None = None,
        env_vars: dict[str, str] | None = None,
        domain: str | None = None,
        auto_redeploy: bool = True,
        domain_service_name: str = "",
        domain_port: int | None = None,
        wait: bool = True,
    ) -> dict:
        """
        Edit compose file, env vars, and/or domain.

        Parameters
        ----------
        compose_id: The compose project ID to update.
        compose_yaml: New docker-compose.yml content (optional).
        env_vars: New environment variables to overlay (optional).
        domain: Domain to add if not already present (optional).
        auto_redeploy: Whether to redeploy after changes (default True).
        domain_service_name: Service name for domain routing.
        domain_port: Port for domain routing.
        wait: If True (default), block until any redeployment completes.
            If False and auto_redeploy triggers a deploy, returns immediately
            with ``{"compose_id": ..., "status": "deploying"}``.

        WARNING: compose.update requires the FULL payload - we refetch and merge
                 automatically so you don't have to.
        """
        full = self._get_full_compose(compose_id)
        changed = False

        if compose_yaml is not None:
            _validate_compose_yaml(compose_yaml)
            full["composeFile"] = compose_yaml
            changed = True

        if env_vars is not None:
            _validate_env_vars(env_vars)
            env_string = "\n".join(f"{k}={v}" for k, v in env_vars.items())
            self.post("/compose.saveEnvironment", json_body={
                "composeId": compose_id,
                "env": env_string,
            })
            print(f"  Updated {len(env_vars)} env var(s)")
            print("  ! WARNING: Environment variables take effect on next deploy")
            changed = True

        if domain is not None:
            _validate_domain(domain)
            existing = self.get("/domain.byComposeId", params={"composeId": compose_id})
            existing = existing or []
            hosts = [d.get("host") for d in existing]
            if domain not in hosts:
                resolved_service_name = domain_service_name
                if not resolved_service_name:
                    current_yaml = full.get("composeFile", "")
                    if current_yaml:
                        try:
                            parsed = yaml.safe_load(current_yaml)
                            services = parsed.get("services", {}) if isinstance(parsed, dict) else {}
                            if isinstance(services, dict) and len(services) == 1:
                                resolved_service_name = list(services.keys())[0]
                        except Exception:
                            pass
                    if not resolved_service_name:
                        raise ValidationError(
                            "Cannot determine service name for domain - pass domain_service_name="
                        )
                resolved_port = domain_port if domain_port is not None else 3000

                self.post("/domain.create", json_body=self._with_server_id({
                    "host": domain,
                    "composeId": compose_id,
                    "domainType": "compose",
                    "https": False,
                    "certificateType": "none",
                    "serviceName": resolved_service_name,
                    "port": resolved_port,
                }))
                print(f"  Added domain '{domain}'")
                print("  ! WARNING: Changing the domain requires a redeploy to take effect")
                changed = True
            else:
                print(f"  Domain '{domain}' already exists, no change")

        if compose_yaml is not None:
            result = self.post("/compose.update", json_body=full)
            print("  Compose file updated")
            changed = True

        if auto_redeploy and changed:
            print("-> Auto-redeploying...")
            self.post("/compose.deploy", json_body={"composeId": compose_id})
            if not wait:
                return {
                    "compose_id": compose_id,
                    "status": "deploying",
                }
            final = self._poll_compose_status(compose_id)
            print(f"  Final status: {final.get('composeStatus')}")
        elif changed and not auto_redeploy:
            print("-> Updates saved but NOT redeployed (auto_redeploy=False)")
            print("  ! WARNING: Changes won't take effect until next deploy")
            final = full
        else:
            print("-> No changes made")
            final = full

        return final

    # =====================================================================
    #  HIGH-LEVEL: redeploy / start / stop / delete
    # =====================================================================

    def redeploy(self, compose_id: str, wait: bool = True) -> dict:
        """Redeploy a compose project, optionally poll until done.

        Parameters
        ----------
        compose_id: The compose project ID to redeploy.
        wait: If True (default), block until deployment completes.
            If False, trigger the redeploy and return immediately
            with ``{"compose_id": ..., "status": "deploying"}``.
        """
        print(f"-> Triggering redeploy for {compose_id}...")
        self.post("/compose.redeploy", json_body={"composeId": compose_id})
        if not wait:
            return {
                "compose_id": compose_id,
                "status": "deploying",
            }
        print("-> Waiting for deployment...")
        final = self._poll_compose_status(compose_id)
        print(f"  Final status: {final.get('composeStatus')}")
        self.debug(compose_id)
        return final

    def start_compose(self, compose_id: str) -> dict:
        """Start a stopped compose project. Returns updated compose info."""
        self.post("/compose.start", json_body={"composeId": compose_id})
        return self._get_full_compose(compose_id)

    def stop_compose(self, compose_id: str) -> dict:
        """Stop a compose project. Returns updated compose info."""
        self.post("/compose.stop", json_body={"composeId": compose_id})
        return self._get_full_compose(compose_id)

    def delete_compose(self, compose_id: str, delete_volumes: bool = False) -> None:
        """
        Delete a compose project. This is PERMANENT and cannot be undone.
        """
        print(f"! WARNING: Deleting project {compose_id}...")
        print("  Deleting a project is permanent and cannot be undone")
        self.post("/compose.delete", json_body={
            "composeId": compose_id,
            "deleteVolumes": delete_volumes,
        })
        print(f"  Sent delete request for {compose_id}")
        # Verify it's gone
        try:
            self._get_full_compose(compose_id)
            raise DokployError(f"Project {compose_id} still exists after delete")
        except DokployError as exc:
            if exc.status_code == 404 or "not found" in str(exc).lower():
                print(f"  Confirmed deleted - project {compose_id} is gone")
                return
            raise

    # Alias for backwards compat with existing SDK usage
    delete = delete_compose

    # =====================================================================
    #  HIGH-LEVEL: debug diagnostic
    # =====================================================================

    def debug(self, compose_id: str, structured: bool = False) -> dict:
        """
        Print everything useful about a compose project in one shot:
        config, env vars, domains, deployment status, deployment logs,
        container logs, container health.

        Parameters
        ----------
        compose_id: The compose project ID to diagnose.
        structured: If False (default), print to stdout. If True,
            collect the information into a dict and return it without
            printing. The returned dict contains keys:
            ``compose_id``, ``compose``, ``domains``, ``deployments``,
            ``deployment_logs`` and ``containers``.

        Returns the compose object for programmatic inspection.
        """
        if structured:
            result = {
                "compose_id": compose_id,
                "compose": {},
                "domains": [],
                "deployments": [],
                "deployment_logs": {},
                "containers": [],
            }
        else:
            result = {}
            print(f"--- Debug for composeId: {compose_id} ---")

        # Compose config
        try:
            compose = self._get_full_compose(compose_id)
            if not structured:
                print("\n[Compose Config]")
                for key in ["name", "appName", "composeStatus", "sourceType", "composeType",
                            "autoDeploy", "environmentId", "createdAt"]:
                    print(f"  {key}: {compose.get(key)}")
                print(f"  composeFile (first 500 chars): {compose.get('composeFile', '')[:500]}")
            else:
                result["compose"] = compose
        except DokployError as exc:
            if not structured:
                print(f"  [ERROR] Could not fetch compose config: {exc}")
            else:
                result["compose"] = {"error": str(exc)}
            compose = {}

        # Domains
        try:
            domains = self.get("/domain.byComposeId", params={"composeId": compose_id})
            if not structured:
                print("\n[Domains]")
                if isinstance(domains, list):
                    for d in domains:
                        print(f"  {d.get('host')} (port={d.get('port')}, https={d.get('https')})")
                else:
                    print(f"  {domains}")
            else:
                result["domains"] = domains if isinstance(domains, list) else [domains]
        except DokployError as exc:
            if not structured:
                print(f"  [ERROR] Could not fetch domains: {exc}")
            else:
                result["domains"] = [{"error": str(exc)}]

        # Deployment status
        try:
            deployments = self.get("/deployment.allByCompose", params={"composeId": compose_id})
            if not structured:
                print("\n[Deployments]")
                if isinstance(deployments, list):
                    for dep in deployments[:5]:
                        print(f"  status={dep.get('status')}  started={dep.get('startedAt')}  ended={dep.get('endedAt')}")
                else:
                    print(f"  {deployments}")
            else:
                result["deployments"] = deployments if isinstance(deployments, list) else [deployments]
        except DokployError as exc:
            if not structured:
                print(f"  [ERROR] Could not fetch deployments: {exc}")
            else:
                result["deployments"] = [{"error": str(exc)}]

        # Deployment logs from filesystem
        app_name = compose.get("appName") if compose else None
        if app_name:
            import glob
            log_pattern = f"/opt/dokploy/logs/{app_name}/*.log"
            log_files = sorted(glob.glob(log_pattern))
            if not structured:
                print(f"\n[Deployment Logs -- {log_pattern}]")
            if log_files:
                latest = log_files[-1]
                try:
                    with open(latest) as f:
                        lines = f.readlines()
                        if not structured:
                            for line in lines[-50:]:
                                print(f"  {line.rstrip()}")
                        else:
                            result["deployment_logs"] = {
                                "latest_file": latest,
                                "lines": [line.rstrip() for line in lines[-50:]],
                            }
                except Exception as exc:
                    if not structured:
                        print(f"  [ERROR] Could not read log file: {exc}")
                    else:
                        result["deployment_logs"] = {"error": str(exc)}
            else:
                if not structured:
                    print("  No deployment log files found on filesystem")
                else:
                    result["deployment_logs"] = {"message": "No deployment log files found on filesystem"}

            # Container logs via API
            if not structured:
                print(f"\n[Container Logs -- API]")
            containers_data = []
            try:
                containers = self.get("/docker.getContainersByAppLabel", params={
                    "appName": app_name,
                    "type": "standalone",
                    "serverId": self.server_id,
                })
                containers = containers or []
                if isinstance(containers, dict):
                    containers = containers.get("containers", [])
                for c in containers:
                    cid = c.get("containerId") or c.get("Id") or c.get("id")
                    if not cid:
                        continue
                    if not structured:
                        print(f"  Container: {cid[:12]}... ({c.get('State', {}).get('Status', '?')})")
                    try:
                        logs = self.get("/compose.readLogs", params={
                            "composeId": compose_id,
                            "containerId": cid,
                            "tail": 30,
                        })
                        if not structured:
                            print(f"    {logs or '(no logs)'}")
                        else:
                            containers_data.append({
                                "container_id": cid,
                                "state": c.get("State", {}).get("Status", "?"),
                                "logs": logs,
                            })
                    except Exception as exc:
                        if not structured:
                            print(f"    [ERROR] Could not fetch logs: {exc}")
                        else:
                            containers_data.append({
                                "container_id": cid,
                                "state": c.get("State", {}).get("Status", "?"),
                                "logs_error": str(exc),
                            })
                if structured:
                    result["containers"] = containers_data
            except Exception as exc:
                if not structured:
                    print(f"  [ERROR] Could not list containers: {exc}")
                else:
                    result["containers"] = [{"error": str(exc)}]
        else:
            if not structured:
                print("\n[Logs]")
                print("  Unknown appName - cannot locate log files or containers")
            else:
                result["deployment_logs"] = {"message": "Unknown appName - cannot locate log files or containers"}
                result["containers"] = []

        if not structured:
            print(f"\n--- End debug for {compose_id} ---")
            return compose
        return result

    # =====================================================================
    #  HIGH-LEVEL: template catalog deployments
    # =====================================================================

    def deploy_from_template(
        self,
        name: str,
        template_id: str,
        environment_id: str = "",
        base_url: str = "https://raw.githubusercontent.com/Dokploy/templates/canary",
        env_vars: dict[str, str] | None = None,
        domain: str | None = None,
        domain_service_name: str = "",
        domain_port: int | None = None,
        wait: bool = True,
    ) -> dict:
        """
        Deploy a compose project from the Dokploy template catalog.

        Parameters
        ----------
        name: Compose project name.
        template_id: The template ID from the catalog (e.g. "n8n", "ghost").
        environment_id: Dokploy environment ID (auto-detected if omitted).
        base_url: Raw GitHub URL for the template catalog (defaults upstream Dokploy).
        env_vars: Extra environment variables to overlay.
        domain: Hostname to route to this compose.
        domain_service_name: Service name for the domain (auto-detected if omitted).
        domain_port: Port for the domain (defaults to 3000).
        wait: If True (default), block until deployment completes.
            If False, trigger the operation and return immediately
            with ``{"compose_id": ..., "status": "deploying"}``.

        Returns
        -------
        dict with compose_id, status, domain, etc.
        """
        if not name:
            raise ValidationError("name is required")
        if not template_id:
            raise ValidationError("template_id is required")

        env_id = environment_id or self._find_default_environment()
        env_vars = env_vars or {}
        _validate_env_vars(env_vars)
        if domain:
            _validate_domain(domain)

        print(f"-> Deploying template '{template_id}' as '{name}'...")

        # Step 1: Create the compose project via template deployment
        resp = self.post("/compose.deployTemplate", json_body={
            "name": name,
            "environmentId": env_id,
            "id": template_id,
            "baseUrl": base_url,
        })

        compose_id = resp.get("composeId")
        if not compose_id:
            raise DokployError(f"compose.deployTemplate did not return a composeId: {resp}")

        print(f"  Created composeId = {compose_id}")

        # Fix sourceType bug
        self._update_source_type_raw(compose_id)

        # Overlay extra env vars
        if env_vars:
            env_string = "\n".join(f"{k}={v}" for k, v in env_vars.items())
            self.post("/compose.saveEnvironment", json_body={
                "composeId": compose_id,
                "env": env_string,
            })
            print(f"  Saved {len(env_vars)} extra variable(s)")

        # Add domain if requested
        if domain:
            # For catalog templates, try to get default service from the compose
            full = self._get_full_compose(compose_id)
            try:
                parsed = yaml.safe_load(full.get("composeFile", ""))
                services = parsed.get("services", {}) if isinstance(parsed, dict) else {}
                svc = domain_service_name or (list(services.keys())[0] if services else None)
            except Exception:
                svc = domain_service_name or ""
            if not svc:
                raise ValidationError("Cannot determine service name for domain - pass domain_service_name=")

            port = domain_port if domain_port is not None else 3000
            self.post("/domain.create", json_body=self._with_server_id({
                "host": domain,
                "composeId": compose_id,
                "domainType": "compose",
                "https": False,
                "certificateType": "none",
                "serviceName": svc,
                "port": port,
            }))
            print(f"  Added domain '{domain}'")

        # Trigger deployment (deployTemplate only creates the object; it does not deploy)
        print("-> Triggering deployment...")
        self.post("/compose.deploy", json_body={"composeId": compose_id})

        if not wait:
            return {
                "compose_id": compose_id,
                "status": "deploying",
                "domain": domain,
            }

        # Poll
        print("-> Waiting for deployment to complete...")
        final = self._poll_compose_status(compose_id)
        status = final.get("composeStatus")
        print(f"  Final status: {status}")

        self.debug(compose_id)
        return {
            "compose_id": compose_id,
            "compose": final,
            "status": status,
            "domain": domain,
        }

    # =====================================================================
    #  COMPOSE  (mid-level wrappers)
    # =====================================================================

    def list_projects(self) -> list[dict]:
        """List all compose projects with their status."""
        result = self.get("/compose.search")
        if isinstance(result, dict):
            items = result.get("items", result.get("composes", result))
            if isinstance(items, list):
                return items
            return [result] if "composeId" in result else []
        return result or []

    def get_compose(self, compose_id: str) -> dict:
        """Fetch complete compose object by ID."""
        return self._get_full_compose(compose_id)

    def get_compose_services(self, compose_id: str) -> dict:
        """Return parsed services from the compose file."""
        info = self._get_full_compose(compose_id)
        yaml_text = info.get("composeFile", "")
        if not yaml_text:
            return {}
        parsed = yaml.safe_load(yaml_text)
        return parsed.get("services", {}) if isinstance(parsed, dict) else {}

    def save_compose_env(self, compose_id: str, env_vars: dict[str, str]) -> None:
        """Overwrite the compose environment variables."""
        _validate_env_vars(env_vars)
        env_string = "\n".join(f"{k}={v}" for k, v in env_vars.items())
        self.post("/compose.saveEnvironment", json_body={
            "composeId": compose_id,
            "env": env_string,
        })

    def get_compose_env(self, compose_id: str) -> dict[str, str]:
        """
        Read compose environment variables.

        NOTE: Dokploy does NOT expose a dedicated read endpoint. We try to
        reflect them from the compose.composeFile as ${FOO} references and
        fall back to the first environment block. If you need exact values,
        keep them in your own config.
        """
        info = self._get_full_compose(compose_id)
        env_text = info.get("env", "")
        if env_text:
            result = {}
            for line in env_text.splitlines():
                if "=" in line:
                    k, v = line.split("=", 1)
                    result[k.strip()] = v.strip()
            return result

        # Fallback: parse composeFile for .env_file references
        yaml_text = info.get("composeFile", "")
        if yaml_text:
            parsed = yaml.safe_load(yaml_text)
            services = parsed.get("services", {}) if isinstance(parsed, dict) else {}
            for svc_name, svc in services.items():
                if isinstance(svc, dict) and "environment" in svc:
                    envs = svc["environment"]
                    if isinstance(envs, dict):
                        return dict(envs)
                    elif isinstance(envs, list):
                        result = {}
                        for e in envs:
                            if isinstance(e, str) and "=" in e:
                                k, v = e.split("=", 1)
                                result[k.strip()] = v.strip()
                        return result
        return {}

    def get_compose_deployments(self, compose_id: str) -> list[dict]:
        return self.get("/deployment.allByCompose", params={"composeId": compose_id}) or []

    def get_compose_domains(self, compose_id: str) -> list[dict]:
        return self.get("/domain.byComposeId", params={"composeId": compose_id}) or []

    def clear_compose_deployments(self, compose_id: str) -> None:
        """Remove old deployment records for a compose project."""
        self.post("/compose.clearDeployments", json_body={"composeId": compose_id})

    def kill_compose_build(self, compose_id: str) -> None:
        """Kill an in-progress build/deployment."""
        self.post("/compose.killBuild", json_body={"composeId": compose_id})

    def cancel_compose_deployment(self, compose_id: str) -> None:
        """Cancel the current compose deployment."""
        self.post("/compose.cancelDeployment", json_body={"composeId": compose_id})

    # =====================================================================
    #  SERVER
    # =====================================================================

    def list_servers(self) -> list[dict]:
        return self.get("/server.all") or []

    def get_server(self, server_id: str) -> dict:
        return self.get("/server.one", params={"serverId": server_id})

    def validate_server(self, server_id: str = "") -> dict:
        """Verify Dokploy can reach the server via SSH."""
        sid = server_id or self.server_id
        return self.get("/server.validate", params={"serverId": sid})

    def get_server_metrics(self, url: str = "", token: str = "", data_points: int = 50) -> dict:
        """Fetch raw server metrics from your metrics endpoint (if configured)."""
        return self.get("/server.getServerMetrics", params={
            "url": url,
            "token": token,
            "dataPoints": data_points,
        })

    def list_build_servers(self) -> list[dict]:
        return self.get("/server.buildServers") or []

    def get_server_security(self, server_id: str = "") -> dict:
        sid = server_id or self.server_id
        return self.get("/server.security", params={"serverId": sid})

    # =====================================================================
    #  PROJECTS & ENVIRONMENTS
    # =====================================================================

    def list_environments(self, **filters) -> Any:
        """Search environments. Common filters: projectId, name, limit, offset."""
        params = self._with_server_id({"limit": 100, "offset": 0, **filters})
        return self.get("/environment.search", params=params)

    def get_environment(self, environment_id: str) -> dict:
        return self.get("/environment.one", params={"environmentId": environment_id})

    def create_environment(self, name: str, project_id: str) -> dict:
        return self.post("/environment.create", json_body={"name": name, "projectId": project_id})

    def environment_search(self, **filters) -> Any:
        return self.list_environments(**filters)

    def list_dokploy_projects(self, **filters) -> Any:
        params = {"limit": 100, "offset": 0, **filters}
        return self.get("/project.search", params=params)

    def get_dokploy_project(self, project_id: str) -> dict:
        return self.get("/project.one", params={"projectId": project_id})

    def create_dokploy_project(self, name: str, description: str = "") -> dict:
        return self.post("/project.create", json_body={
            "name": name,
            "description": description,
        })

    def project_all(self) -> Any:
        return self.get("/project.all")

    # =====================================================================
    #  DOMAINS
    # =====================================================================

    def create_domain(
        self,
        compose_id: str,
        host: str,
        service_name: str,
        port: int = 3000,
        https: bool = False,
    ) -> dict:
        """Attach a new domain to a compose project."""
        _validate_domain(host)
        return self.post("/domain.create", json_body=self._with_server_id({
            "host": host,
            "composeId": compose_id,
            "domainType": "compose",
            "https": https,
            "certificateType": "none",
            "serviceName": service_name,
            "port": port,
        }))

    def delete_domain(self, domain_id: str) -> None:
        self.post("/domain.delete", json_body={"domainId": domain_id})

    def get_domain(self, domain_id: str) -> dict:
        return self.get("/domain.one", params={"domainId": domain_id})

    # =====================================================================
    #  APPLICATIONS (non-compose Docker apps)
    # =====================================================================

    def list_applications(self, **filters) -> Any:
        params = self._with_server_id({"limit": 100, "offset": 0, **filters})
        return self.get("/application.search", params=params)

    def get_application(self, application_id: str) -> dict:
        return self.get("/application.one", params={"applicationId": application_id})

    def deploy_application(self, application_id: str) -> None:
        """Trigger deployment of an application."""
        self.post("/application.deploy", json_body={"applicationId": application_id})

    def redeploy_application(self, application_id: str) -> None:
        self.post("/application.redeploy", json_body={"applicationId": application_id})

    def save_application_env(self, application_id: str, env_vars: dict[str, str]) -> None:
        """Save environment variables for an application."""
        _validate_env_vars(env_vars)
        env_string = "\n".join(f"{k}={v}" for k, v in env_vars.items())
        self.post("/application.saveEnvironment", json_body={
            "applicationId": application_id,
            "env": env_string,
            "buildArgs": "",
            "buildSecrets": "",
            "createEnvFile": False,
        })

    def get_application_logs(self, application_id: str, tail: int = 100) -> str:
        return self.get("/application.readLogs", params={
            "applicationId": application_id,
            "tail": tail,
        })

    # =====================================================================
    #  DOCKER CONTAINER OPS
    # =====================================================================

    def list_containers(self, server_id: str = "") -> list[dict]:
        sid = server_id or self.server_id
        return self.get("/docker.getContainers", params={"serverId": sid}) or []

    def list_containers_by_app(self, app_name: str, server_id: str = "") -> list[dict]:
        sid = server_id or self.server_id
        result = self.get("/docker.getContainersByAppLabel", params={
            "appName": app_name,
            "type": "standalone",
            "serverId": sid,
        })
        if isinstance(result, dict):
            return result.get("containers", [])
        return result or []

    def restart_container(self, container_id: str) -> None:
        self.post("/docker.restartContainer", json_body={"containerId": container_id})

    def stop_container(self, container_id: str) -> None:
        self.post("/docker.stopContainer", json_body={"containerId": container_id})

    def start_container(self, container_id: str) -> None:
        self.post("/docker.startContainer", json_body={"containerId": container_id})

    def kill_container(self, container_id: str) -> None:
        self.post("/docker.killContainer", json_body={"containerId": container_id})

    # =====================================================================
    #  DEPLOYMENTS
    # =====================================================================

    def get_deployments(self, compose_id: str) -> list[dict]:
        return self.get("/deployment.allByCompose", params={"composeId": compose_id}) or []

    def get_deployment_logs(self, deployment_id: str, tail: int = 100) -> str:
        return self.get("/deployment.readLogs", params={
            "deploymentId": deployment_id,
            "tail": tail,
        })

    def kill_deployment_process(self, deployment_id: str) -> None:
        self.post("/deployment.killProcess", json_body={"deploymentId": deployment_id})

    # =====================================================================
    #  DATABASES (convenience wrappers)
    # =====================================================================

    def list_postgres(self, **filters) -> Any:
        """Search postgres services."""
        params = self._with_server_id({"limit": 100, **filters})
        return self.get("/postgres.search", params=params)

    def create_postgres(
        self,
        name: str,
        database_name: str,
        database_user: str,
        database_password: str,
        environment_id: str = "",
    ) -> dict:
        """Create a managed Postgres database."""
        env_id = environment_id or self._find_default_environment()
        return self.post("/postgres.create", json_body=self._with_server_id({
            "name": name,
            "databaseName": database_name,
            "databaseUser": database_user,
            "databasePassword": database_password,
            "environmentId": env_id,
        }))

    def delete_postgres(self, postgres_id: str) -> None:
        self.post("/postgres.remove", json_body={"postgresId": postgres_id})

    def list_redis(self, **filters) -> Any:
        """Search redis services."""
        params = self._with_server_id({"limit": 100, **filters})
        return self.get("/redis.search", params=params)

    def create_redis(self, name: str, password: str, environment_id: str = "") -> dict:
        env_id = environment_id or self._find_default_environment()
        return self.post("/redis.create", json_body=self._with_server_id({
            "name": name,
            "databasePassword": password,
            "environmentId": env_id,
        }))

    def delete_redis(self, redis_id: str) -> None:
        self.post("/redis.remove", json_body={"redisId": redis_id})

    # =====================================================================
    #  TEMPLATE CATALOG
    # =====================================================================

    def list_templates(self, base_url: str = "") -> list[dict]:
        params = {}
        if base_url:
            params["baseUrl"] = base_url
        return self.get("/compose.templates", params=params) or []

    # =====================================================================
    #  SETTINGS & HEALTH
    # =====================================================================

    def health_check(self) -> dict:
        """Quick Dokploy API health check. Returns server version, uptime, etc."""
        return self.get("/settings.health")

    def get_version(self) -> str:
        return self.get("/settings.getDokployVersion")


# Backwards-compat aliases
deploy_template = DokployClient.deploy_compose
DeployError = DokployError
