---
title: "Komari Monitor | Dokploy"
source: "https://docs.dokploy.com/docs/templates/komari-monitor"
category: dokploy-docs
created: "2026-06-25T17:21:50.891Z"
---

Komari Monitor | Dokploy

# Komari Monitor

Copy as Markdown

A lightweight, self-hosted server monitoring tool for tracking server performance.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  komari:
    image: ghcr.io/komari-monitor/komari:latest
    restart: unless-stopped
    volumes:
      - komari-data:/app/data
    environment:
      - ADMIN_USERNAME
      - ADMIN_PASSWORD

volumes:
  komari-data: {}
```

```
[variables]
main_domain = "${domain}"
admin_password = "${password:16}"

[config]
mounts = []

[[config.domains]]
serviceName = "komari"
port = 25_774
host = "${main_domain}"

[config.env]
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "${admin_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBrb21hcmk6XG4gICAgaW1hZ2U6IGdoY3IuaW8va29tYXJpLW1vbml0b3Iva29tYXJpOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0ga29tYXJpLWRhdGE6L2FwcC9kYXRhXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIEFETUlOX1VTRVJOQU1FXG4gICAgICAtIEFETUlOX1BBU1NXT1JEXG5cbnZvbHVtZXM6XG4gIGtvbWFyaS1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmFkbWluX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJrb21hcmlcIlxucG9ydCA9IDI1Xzc3NFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkFETUlOX1VTRVJOQU1FID0gXCJhZG1pblwiXG5BRE1JTl9QQVNTV09SRCA9IFwiJHthZG1pbl9wYXNzd29yZH1cIlxuIgp9
```

## Links

`monitoring`,`self-hosted`

---

Version:`latest`

Kokoro WebKokoro Web provides an interface for text-to-speech using advanced AI voice synthesis. It allows model caching and API integration with authentication.

KuttKutt is a modern URL shortener with support for custom domains. Create and edit links, view statistics, manage users, and more.

### On this page

ConfigurationBase64LinksTags