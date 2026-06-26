---
title: "TrailBase | Dokploy"
source: "https://docs.dokploy.com/docs/templates/trailbase"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

TrailBase | Dokploy

# TrailBase

Copy as Markdown

TrailBase is a blazingly fast, open-source application server with type-safe APIs, built-in WebAssembly runtime, realtime, auth, and admin UI built on Rust, SQLite & Wasmtime.

## Configuration

docker-compose.ymltemplate.toml

```
# IMPORTANT: The initial admin credentials will be printed in the logs after the container starts
# Access TrailBase Admin UI at: https://your-domain.com/_/admin (replace with your configured domain)

version: "3.8"

services:
  trailbase:
    image: trailbase/trailbase:latest
    restart: unless-stopped
    volumes:
      - trailbase-data:/app/traildepot
      # If you want to use a local directory instead, uncomment the line below and specify the path to your local
      # directory. Make sure this directory is writable by the trailbase user (UID 1000) and the group (GID 1000) i.e.
      # chown -R 1000:1000 /path/to/your/local/directory
      # - /path/to/your/local/directory:/app/traildepot
    healthcheck:
      test: ["CMD", "curl", "--fail", "http://localhost:4000/api/healthcheck"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  # comment the line below if you specified a local directory in the volumes section of the trailbase service
  trailbase-data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "trailbase"
port = 4000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgSU1QT1JUQU5UOiBUaGUgaW5pdGlhbCBhZG1pbiBjcmVkZW50aWFscyB3aWxsIGJlIHByaW50ZWQgaW4gdGhlIGxvZ3MgYWZ0ZXIgdGhlIGNvbnRhaW5lciBzdGFydHNcbiMgQWNjZXNzIFRyYWlsQmFzZSBBZG1pbiBVSSBhdDogaHR0cHM6Ly95b3VyLWRvbWFpbi5jb20vXy9hZG1pbiAocmVwbGFjZSB3aXRoIHlvdXIgY29uZmlndXJlZCBkb21haW4pXG5cbnZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHRyYWlsYmFzZTpcbiAgICBpbWFnZTogdHJhaWxiYXNlL3RyYWlsYmFzZTpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHRyYWlsYmFzZS1kYXRhOi9hcHAvdHJhaWxkZXBvdFxuICAgICAgIyBJZiB5b3Ugd2FudCB0byB1c2UgYSBsb2NhbCBkaXJlY3RvcnkgaW5zdGVhZCwgdW5jb21tZW50IHRoZSBsaW5lIGJlbG93IGFuZCBzcGVjaWZ5IHRoZSBwYXRoIHRvIHlvdXIgbG9jYWxcbiAgICAgICMgZGlyZWN0b3J5LiBNYWtlIHN1cmUgdGhpcyBkaXJlY3RvcnkgaXMgd3JpdGFibGUgYnkgdGhlIHRyYWlsYmFzZSB1c2VyIChVSUQgMTAwMCkgYW5kIHRoZSBncm91cCAoR0lEIDEwMDApIGkuZS5cbiAgICAgICMgY2hvd24gLVIgMTAwMDoxMDAwIC9wYXRoL3RvL3lvdXIvbG9jYWwvZGlyZWN0b3J5XG4gICAgICAjIC0gL3BhdGgvdG8veW91ci9sb2NhbC9kaXJlY3Rvcnk6L2FwcC90cmFpbGRlcG90XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJjdXJsXCIsIFwiLS1mYWlsXCIsIFwiaHR0cDovL2xvY2FsaG9zdDo0MDAwL2FwaS9oZWFsdGhjaGVja1wiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG5cbnZvbHVtZXM6XG4gICMgY29tbWVudCB0aGUgbGluZSBiZWxvdyBpZiB5b3Ugc3BlY2lmaWVkIGEgbG9jYWwgZGlyZWN0b3J5IGluIHRoZSB2b2x1bWVzIHNlY3Rpb24gb2YgdGhlIHRyYWlsYmFzZSBzZXJ2aWNlXG4gIHRyYWlsYmFzZS1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInRyYWlsYmFzZVwiXG5wb3J0ID0gNDAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`backend`,`database`,`api`

---

Version:`latest`

Tor BrowserA Dockerized Tor Browser accessible via web VNC (noVNC) and VNC client.

Trigger.devTrigger is a platform for building event-driven applications.

### On this page

ConfigurationBase64LinksTags