---
title: "FlareSolverr | Dokploy"
source: "https://docs.dokploy.com/docs/templates/flaresolverr"
category: dokploy-docs
created: "2026-06-25T17:21:47.359Z"
---

FlareSolverr | Dokploy

# FlareSolverr

Copy as Markdown

FlareSolverr is a proxy server to bypass Cloudflare and DDoS-GUARD protection.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  flaresolverr:
    image: ghcr.io/flaresolverr/flaresolverr:latest
    ports:
      - 8191
    restart: unless-stopped
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "flaresolverr"
port = 8191
host = "${main_domain}"

[config.env]
LOG_LEVEL = "info"
LOG_HTML = "false"
CAPTCHA_SOLVER = "none"
TZ = "Europe/London"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBmbGFyZXNvbHZlcnI6XG4gICAgaW1hZ2U6IGdoY3IuaW8vZmxhcmVzb2x2ZXJyL2ZsYXJlc29sdmVycjpsYXRlc3RcbiAgICBwb3J0czpcbiAgICAgIC0gODE5MVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZmxhcmVzb2x2ZXJyXCJcbnBvcnQgPSA4MTkxXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuTE9HX0xFVkVMID0gXCJpbmZvXCJcbkxPR19IVE1MID0gXCJmYWxzZVwiXG5DQVBUQ0hBX1NPTFZFUiA9IFwibm9uZVwiXG5UWiA9IFwiRXVyb3BlL0xvbmRvblwiXG5cbltbY29uZmlnLm1vdW50c11dXG4iCn0=
```

## Links

`proxy`,`cloudflare`,`bypass`,`ddos-guard`

---

Version:`latest`

FlagsmithFlagsmith is an open-source feature flagging and remote config service.

FlatnotesA self-hosted, modern note-taking web app that saves your notes as plain text Markdown files.

### On this page

ConfigurationBase64LinksTags