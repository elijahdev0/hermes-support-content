#!/usr/bin/env python3
"""Dokploy API Helper for Hermes — handles auth, listing endpoints, getting specs, and calling APIs."""

import json
import os
import sys

# Base URL and auth from environment
_BASE_URL = os.environ.get("DOKPLOY_BASE_URL", "")
_TOKEN = os.environ.get("DOKPLOY_API_TOKEN", "")
_SERVER_ID = os.environ.get("DOKPLOY_SERVER_ID") or os.environ.get("PLAYGROUND_SERVER_ID", "")

# Load OpenAPI spec from adjacent file (written alongside this script by provisioning/sync)
_SPEC_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "openapi.json")
try:
    with open(_SPEC_FILE) as f:
        _SPEC = json.load(f)
except FileNotFoundError:
    _SPEC = None

_HTTP_METHODS = {"get", "post", "put", "delete", "patch"}


def _endpoint_needs_server_id(info):
    """Return True if the endpoint schema accepts serverId in the request body."""
    schema = info.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema", {})
    props = schema.get("properties", {})
    return "serverId" in props


def _endpoint_has_server_id_query(info):
    """Return True if the endpoint has serverId as a query parameter."""
    for param in info.get("parameters", []):
        if param.get("name") == "serverId" and param.get("in") == "query":
            return True
    return False


def _ensure_spec():
    if _SPEC is None:
        print(f"Error: openapi.json not found at {_SPEC_FILE}", file=sys.stderr)
        sys.exit(1)


def _iter_endpoints():
    """Yield (path, method, info) for every endpoint in the spec."""
    _ensure_spec()
    for path, methods in sorted(_SPEC["paths"].items()):
        for method_name, info in methods.items():
            if method_name in _HTTP_METHODS:
                yield path, method_name.upper(), info


def cmd_list():
    """Print all endpoints grouped by tag."""
    by_tag = {}
    for path, method, info in _iter_endpoints():
        for tag in info.get("tags", ["other"]):
            if tag not in by_tag:
                by_tag[tag] = []
            by_tag[tag].append((path, method, info.get("operationId", "")))

    for tag, endpoints in sorted(by_tag.items()):
        print(f"## {tag} ({len(endpoints)} endpoints)")
        for path, method, opid in endpoints:
            label = f"  {method:6} /api{path}"
            if opid:
                label += f"  ({opid})"
            print(label)
        print()


def _get_endpoint_info(path):
    """Return (method_verb, info_dict) for the path's first HTTP method."""
    _ensure_spec()
    entry = _SPEC["paths"].get(path)
    if not entry:
        return None, None
    for method_name, info in entry.items():
        if method_name in _HTTP_METHODS:
            return method_name.upper(), info
    return None, None


def _format_request_body(body):
    """Format a real OpenAPI requestBody into readable text."""
    content = body.get("content", {})
    # Try application/json first, then multipart/form-data
    json_schema = content.get("application/json", {}).get("schema", {})
    multipart_schema = content.get("multipart/form-data", {}).get("schema", {})
    schema = json_schema or multipart_schema
    if not schema:
        return "    (no schema available)"
    lines = []
    if multipart_schema:
        lines.append("    Content-Type: multipart/form-data (file upload)")
    lines.append("    Required fields: " + ", ".join(schema.get("required", [])))
    for prop, pschema in schema.get("properties", {}).items():
        ptype = pschema.get("type", "any")
        fmt = pschema.get("format", "")
        if fmt:
            ptype = f"{ptype}({fmt})"
        lines.append(f"    {prop:24} {ptype:10}")
    return "\n".join(lines)


def cmd_spec(path):
    """Print the full spec for one endpoint path."""
    method, info = _get_endpoint_info(path)
    if not info:
        print(f"Endpoint not found: {path}", file=sys.stderr)
        sys.exit(1)

    print(f"{method} /api{path}")
    opid = info.get("operationId", "")
    if opid:
        print(f"Operation: {opid}")
    print(f"Tags: {', '.join(info.get('tags', []))}")
    print()

    if info.get("requestBody"):
        print("Request body (JSON):")
        print(_format_request_body(info["requestBody"]))
        print()

    if info.get("parameters"):
        print("Parameters:")
        for param in info["parameters"]:
            req = " [required]" if param.get("required") else ""
            ptype = param.get("schema", {}).get("type", "string")
            print(f"  {param.get('in', '?')}  {param['name']:20} {ptype:10}{req}")
        print()


def cmd_call(path, body=None):
    """Call a Dokploy API endpoint."""
    import urllib.error
    import urllib.parse
    import urllib.request

    method, info = _get_endpoint_info(path)
    if not info:
        print(f"Endpoint not found: {path}", file=sys.stderr)
        sys.exit(1)

    url = f"{_BASE_URL}/api{path}"

    # Auto-inject serverId if configured on this playground
    needs_body_server_id = _endpoint_needs_server_id(info) and _SERVER_ID
    needs_query_server_id = _endpoint_has_server_id_query(info) and _SERVER_ID

    # Check if this is a multipart/form-data endpoint
    content = info.get("requestBody", {}).get("content", {})
    if "multipart/form-data" in content:
        print("Error: This endpoint requires multipart/form-data (file upload).", file=sys.stderr)
        print("The helper cannot handle file uploads.", file=sys.stderr)
        print(f"Read the spec with: python3 helper.py spec {path}", file=sys.stderr)
        print("Then use curl directly with -F flags for form fields.", file=sys.stderr)
        sys.exit(1)

    data = None
    headers = {"x-api-key": _TOKEN, "Accept": "application/json"}

    if method == "GET":
        # GET endpoints use query parameters, not JSON body
        params = json.loads(body) if body else {}
        if needs_query_server_id and "serverId" not in params:
            params["serverId"] = _SERVER_ID
        if params:
            url = f"{url}?{urllib.parse.urlencode(params)}"
    else:
        # POST/PUT/PATCH — JSON body
        payload = json.loads(body) if body else {}
        if needs_body_server_id and "serverId" not in payload:
            payload["serverId"] = _SERVER_ID
        if payload:
            data = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"
    
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            print(json.dumps(result, indent=2))
    except urllib.error.HTTPError as e:
        # Read the response body for the actual error message
        body_text = ""
        try:
            body_text = e.read().decode("utf-8")
            body = json.loads(body_text)
        except Exception:
            body = body_text or str(e)

        if isinstance(body, dict):
            print(json.dumps(body, indent=2), file=sys.stderr)
        else:
            print(f"Error: {e} - {body}", file=sys.stderr)

        if e.code == 400 and method == "GET":
            print(f"Hint: GET endpoint returned 400. If you passed a JSON body, use key:value pairs instead: call {path} '{{\"key\":\"value\"}}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: helper.py <list|spec|call> [endpoint] [json-body]", file=sys.stderr)
        sys.exit(1)

    def _normalize_path(raw: str) -> str:
        return raw if raw.startswith("/") else f"/{raw}"

    cmd = sys.argv[1]
    if cmd == "list":
        cmd_list()
    elif cmd == "spec":
        if len(sys.argv) < 3:
            print("Usage: helper.py spec <endpoint-path>", file=sys.stderr)
            sys.exit(1)
        cmd_spec(_normalize_path(sys.argv[2]))
    elif cmd == "call":
        if len(sys.argv) < 3:
            print("Usage: helper.py call <endpoint-path> [json-body]", file=sys.stderr)
            sys.exit(1)
        body = sys.argv[3] if len(sys.argv) > 3 else None
        cmd_call(_normalize_path(sys.argv[2]), body)
    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        sys.exit(1)

