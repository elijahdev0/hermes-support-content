---
title: "OpenGist | Dokploy"
source: "https://docs.dokploy.com/docs/templates/opengist"
category: dokploy-docs
created: "2026-06-25T17:21:55.476Z"
---

OpenGist | Dokploy

# OpenGist

Copy as Markdown

OpenGist is a self-hosted pastebin alternative.

## Configuration

docker-compose.ymltemplate.toml

```
# docker-compose.yml
version: "3.8"
services:
  opengist:
    image: ghcr.io/thomiceli/opengist:1
    restart: unless-stopped
    ports:
      - 6157 # HTTP port
      - 2222 # SSH port (optional)
    volumes:
      - opengist-data:/opengist
    environment:
      - UID=${UID}
      - GID=${GID}
      - OG_LOG_LEVEL=${OG_LOG_LEVEL}
volumes:
  opengist-data: {}
```

```
# template.toml
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "opengist"
port = 6157
host = "${main_domain}"

[config.env]
UID = "1001"
GID = "1001"
OG_LOG_LEVEL = "info"

[[config.mounts]]
# This template uses a named volume defined in the docker-compose.yml,
# so no file mounts need to be configured here.
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgZG9ja2VyLWNvbXBvc2UueW1sXG52ZXJzaW9uOiBcIjMuOFwiXG5zZXJ2aWNlczpcbiAgb3Blbmdpc3Q6XG4gICAgaW1hZ2U6IGdoY3IuaW8vdGhvbWljZWxpL29wZW5naXN0OjFcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSA2MTU3ICMgSFRUUCBwb3J0XG4gICAgICAtIDIyMjIgIyBTU0ggcG9ydCAob3B0aW9uYWwpXG4gICAgdm9sdW1lczpcbiAgICAgIC0gb3Blbmdpc3QtZGF0YTovb3Blbmdpc3RcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gVUlEPSR7VUlEfVxuICAgICAgLSBHSUQ9JHtHSUR9XG4gICAgICAtIE9HX0xPR19MRVZFTD0ke09HX0xPR19MRVZFTH1cbnZvbHVtZXM6XG4gIG9wZW5naXN0LWRhdGE6IHt9XG4iLAogICJjb25maWciOiAiIyB0ZW1wbGF0ZS50b21sXG5bdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJvcGVuZ2lzdFwiXG5wb3J0ID0gNjE1N1xuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblVJRCA9IFwiMTAwMVwiXG5HSUQgPSBcIjEwMDFcIlxuT0dfTE9HX0xFVkVMID0gXCJpbmZvXCJcblxuW1tjb25maWcubW91bnRzXV1cbiMgVGhpcyB0ZW1wbGF0ZSB1c2VzIGEgbmFtZWQgdm9sdW1lIGRlZmluZWQgaW4gdGhlIGRvY2tlci1jb21wb3NlLnltbCxcbiMgc28gbm8gZmlsZSBtb3VudHMgbmVlZCB0byBiZSBjb25maWd1cmVkIGhlcmUuXG4iCn0=
```

## Links

`pastebin`,`code`,`snippets`,`self-hosted`

---

Version:`1`

OpenclawWhatsApp gateway CLI with Pi RPC agent - self-hosted AI-powered messaging platform

OpenHandsOpenHands is an open-source platform for running and managing AI agents.

### On this page

ConfigurationBase64LinksTags