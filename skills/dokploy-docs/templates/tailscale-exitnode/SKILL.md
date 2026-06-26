---
title: "Tailscale Exit nodes | Dokploy"
source: "https://docs.dokploy.com/docs/templates/tailscale-exitnode"
category: dokploy-docs
created: "2026-06-25T17:22:00.274Z"
---

Tailscale Exit nodes | Dokploy

# Tailscale Exit nodes

Copy as Markdown

Tailscale ExitNode is a feature that lets you route your internet traffic through a specific device in your Tailscale network.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  tailscale-exitnode:
    image: tailscale/tailscale:latest
    hostname: ${TAILSCALE_HOSTNAME}
    environment:
      - TS_AUTHKEY=${TAILSCALE_AUTHKEY}
      - TS_EXTRA_ARGS=--advertise-exit-node
      - TS_STATE_DIR=/var/lib/tailscale
      - TS_USERSPACE=true
    volumes:
      - tailscale_exitnode_data:/var/lib/tailscale
    restart: always

volumes:
  tailscale_exitnode_data:
```

```
[config.env]
TAILSCALE_HOSTNAME = ""
TAILSCALE_AUTHKEY = ""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB0YWlsc2NhbGUtZXhpdG5vZGU6XG4gICAgaW1hZ2U6IHRhaWxzY2FsZS90YWlsc2NhbGU6bGF0ZXN0XG4gICAgaG9zdG5hbWU6ICR7VEFJTFNDQUxFX0hPU1ROQU1FfVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBUU19BVVRIS0VZPSR7VEFJTFNDQUxFX0FVVEhLRVl9XG4gICAgICAtIFRTX0VYVFJBX0FSR1M9LS1hZHZlcnRpc2UtZXhpdC1ub2RlXG4gICAgICAtIFRTX1NUQVRFX0RJUj0vdmFyL2xpYi90YWlsc2NhbGVcbiAgICAgIC0gVFNfVVNFUlNQQUNFPXRydWVcbiAgICB2b2x1bWVzOlxuICAgICAgLSB0YWlsc2NhbGVfZXhpdG5vZGVfZGF0YTovdmFyL2xpYi90YWlsc2NhbGVcbiAgICByZXN0YXJ0OiBhbHdheXNcblxudm9sdW1lczpcbiAgdGFpbHNjYWxlX2V4aXRub2RlX2RhdGE6IiwKICAiY29uZmlnIjogIlxuW2NvbmZpZy5lbnZdXG5UQUlMU0NBTEVfSE9TVE5BTUUgPSBcIlwiXG5UQUlMU0NBTEVfQVVUSEtFWSA9IFwiXCIiCn0=
```

## Links

`network`

---

Version:`1.0.0`

SyncthingSyncthing is a continuous file synchronization program that synchronizes files between two or more computers in real time.

teableTeable is a Super fast, Real-time, Professional, Developer friendly, No-code database built on Postgres. It uses a simple, spreadsheet-like interface to create complex enterprise-level database applications. Unlock efficient app development with no-code, free from the hurdles of data security and scalability.

### On this page

ConfigurationBase64LinksTags