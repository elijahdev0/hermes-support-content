---
title: "Borgitory | Dokploy"
source: "https://docs.dokploy.com/docs/templates/borgitory"
category: dokploy-docs
created: "2026-06-25T17:21:42.677Z"
---

Borgitory | Dokploy

# Borgitory

Copy as Markdown

A web interface for managing BorgBackup archives. Allows browsing, mounting (via FUSE), and handling backup repositories.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  borgitory:
    image: mlapaglia/borgitory:latest
    restart: unless-stopped
    expose:
      - 8000
    cap_add:
      - SYS_ADMIN
    devices:
      - /dev/fuse
    volumes:
      - borgitory-data:/app/data
      - borgitory-sources:/mnt/sources:ro
      - borgitory-repos:/mnt/repos:ro

volumes:
  borgitory-data: {}
  borgitory-sources: {}
  borgitory-repos: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "borgitory"
port = 8000
host = "${main_domain}"

[config.env]

[[config.mounts]]
name = "borgitory-data"
mountPath = "/app/data"
description = "Database and encryption key storage"

[[config.mounts]]
name = "borgitory-sources"
mountPath = "/mnt/sources"
description = "Sources to back up (read-only)"

[[config.mounts]]
name = "borgitory-repos"
mountPath = "/mnt/repos"
description = "Borg repositories (read-only)"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGJvcmdpdG9yeTpcbiAgICBpbWFnZTogbWxhcGFnbGlhL2JvcmdpdG9yeTpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGV4cG9zZTpcbiAgICAgIC0gODAwMFxuICAgIGNhcF9hZGQ6XG4gICAgICAtIFNZU19BRE1JTlxuICAgIGRldmljZXM6XG4gICAgICAtIC9kZXYvZnVzZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGJvcmdpdG9yeS1kYXRhOi9hcHAvZGF0YVxuICAgICAgLSBib3JnaXRvcnktc291cmNlczovbW50L3NvdXJjZXM6cm9cbiAgICAgIC0gYm9yZ2l0b3J5LXJlcG9zOi9tbnQvcmVwb3M6cm9cblxudm9sdW1lczpcbiAgYm9yZ2l0b3J5LWRhdGE6IHt9XG4gIGJvcmdpdG9yeS1zb3VyY2VzOiB7fVxuICBib3JnaXRvcnktcmVwb3M6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYm9yZ2l0b3J5XCJcbnBvcnQgPSA4MDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuXG5bW2NvbmZpZy5tb3VudHNdXVxubmFtZSA9IFwiYm9yZ2l0b3J5LWRhdGFcIlxubW91bnRQYXRoID0gXCIvYXBwL2RhdGFcIlxuZGVzY3JpcHRpb24gPSBcIkRhdGFiYXNlIGFuZCBlbmNyeXB0aW9uIGtleSBzdG9yYWdlXCJcblxuW1tjb25maWcubW91bnRzXV1cbm5hbWUgPSBcImJvcmdpdG9yeS1zb3VyY2VzXCJcbm1vdW50UGF0aCA9IFwiL21udC9zb3VyY2VzXCJcbmRlc2NyaXB0aW9uID0gXCJTb3VyY2VzIHRvIGJhY2sgdXAgKHJlYWQtb25seSlcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxubmFtZSA9IFwiYm9yZ2l0b3J5LXJlcG9zXCJcbm1vdW50UGF0aCA9IFwiL21udC9yZXBvc1wiXG5kZXNjcmlwdGlvbiA9IFwiQm9yZyByZXBvc2l0b3JpZXMgKHJlYWQtb25seSlcIiIKfQ==
```

## Links

`backup`,`borg`,`archive`,`self-hosted`

---

Version:`latest`

BookStackBookStack is a self-hosted platform for creating beautiful, feature-rich documentation sites.

BotpressBotpress is a platform for building conversational AI agents. It provides a simple and effective solution for building conversational AI agents from anywhere.

### On this page

ConfigurationBase64LinksTags