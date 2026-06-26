---
title: "Pinchflat | Dokploy"
source: "https://docs.dokploy.com/docs/templates/pinchflat"
category: dokploy-docs
created: "2026-06-25T17:21:56.647Z"
---

Pinchflat | Dokploy

# Pinchflat

Copy as Markdown

Pinchflat is a self-hosted YouTube downloader that allows you to download videos and playlists with a simple web interface.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"
services:
  pinchflat:
    image: ghcr.io/kieraneglin/pinchflat:latest
    volumes:
      - ../files/config:/config
      - ../files/downloads:/downloads
```

```
[variables]
main_domain = "${domain}"
basic_auth_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "pinchflat"
port = 8945
host = "${main_domain}"

[config.env]
TZ = "America/New_York"
LOG_LEVEL = "debug"
UMASK = "022"
BASIC_AUTH_USERNAME = ""
BASIC_AUTH_PASSWORD = "${basic_auth_password}"
EXPOSE_FEED_ENDPOINTS = "false"
ENABLE_IPV6 = "false"
JOURNAL_MODE = "wal"
TZ_DATA_DIR = "/etc/elixir_tzdata_data"
BASE_ROUTE_PATH = "/"
YT_DLP_WORKER_CONCURRENCY = "2"
ENABLE_PROMETHEUS = "false"

[[config.mounts]]
filePath = "/files/config"
content = ""

[[config.mounts]]
filePath = "/files/downloads"
content = ""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5zZXJ2aWNlczpcbiAgcGluY2hmbGF0OlxuICAgIGltYWdlOiBnaGNyLmlvL2tpZXJhbmVnbGluL3BpbmNoZmxhdDpsYXRlc3RcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9jb25maWc6L2NvbmZpZ1xuICAgICAgLSAuLi9maWxlcy9kb3dubG9hZHM6L2Rvd25sb2Fkc1xuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmJhc2ljX2F1dGhfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCIgXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJwaW5jaGZsYXRcIiBcbnBvcnQgPSA4OTQ1XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuVFogPSBcIkFtZXJpY2EvTmV3X1lvcmtcIlxuTE9HX0xFVkVMID0gXCJkZWJ1Z1wiXG5VTUFTSyA9IFwiMDIyXCJcbkJBU0lDX0FVVEhfVVNFUk5BTUUgPSBcIlwiXG5CQVNJQ19BVVRIX1BBU1NXT1JEID0gXCIke2Jhc2ljX2F1dGhfcGFzc3dvcmR9XCIgXG5FWFBPU0VfRkVFRF9FTkRQT0lOVFMgPSBcImZhbHNlXCJcbkVOQUJMRV9JUFY2ID0gXCJmYWxzZVwiXG5KT1VSTkFMX01PREUgPSBcIndhbFwiXG5UWl9EQVRBX0RJUiA9IFwiL2V0Yy9lbGl4aXJfdHpkYXRhX2RhdGFcIlxuQkFTRV9ST1VURV9QQVRIID0gXCIvXCJcbllUX0RMUF9XT1JLRVJfQ09OQ1VSUkVOQ1kgPSBcIjJcIlxuRU5BQkxFX1BST01FVEhFVVMgPSBcImZhbHNlXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvZmlsZXMvY29uZmlnXCJcbmNvbnRlbnQgPSBcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL2ZpbGVzL2Rvd25sb2Fkc1wiXG5jb250ZW50ID0gXCJcIiIKfQ==
```

## Links

`youtube`,`downloader`,`media`

---

Version:`latest`

PicsurPicsur is a simple, self-hosted image hosting service with an admin interface and Postgres backend.

PlaneEasy, flexible, open source project management software

### On this page

ConfigurationBase64LinksTags