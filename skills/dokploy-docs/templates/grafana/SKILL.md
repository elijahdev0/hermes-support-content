---
title: "Grafana | Dokploy"
source: "https://docs.dokploy.com/docs/templates/grafana"
category: dokploy-docs
created: "2026-06-25T17:21:49.749Z"
---

Grafana | Dokploy

# Grafana

Copy as Markdown

Grafana is an open source platform for data visualization and monitoring.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  grafana:
    image: grafana/grafana-enterprise:12.4
    restart: unless-stopped
    volumes:
      - grafana-storage:/var/lib/grafana
volumes:
  grafana-storage: {}
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "grafana"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBncmFmYW5hOlxuICAgIGltYWdlOiBncmFmYW5hL2dyYWZhbmEtZW50ZXJwcmlzZToxMi40XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBncmFmYW5hLXN0b3JhZ2U6L3Zhci9saWIvZ3JhZmFuYVxudm9sdW1lczpcbiAgZ3JhZmFuYS1zdG9yYWdlOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtdXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJncmFmYW5hXCJcbnBvcnQgPSAzXzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`monitoring`

---

Version:`12.4`

GotenbergGotenberg is a Docker-powered stateless API for PDF files.

GrimoireGrimoire is a self-hosted bookmarking app designed for speed and simplicity.

### On this page

ConfigurationBase64LinksTags