---
title: "Dashy | Dokploy"
source: "https://docs.dokploy.com/docs/templates/dashy"
category: dokploy-docs
created: "2026-06-25T17:21:45.078Z"
---

Dashy | Dokploy

# Dashy

Copy as Markdown

A self-hostable personal dashboard built for you. Includes status-checking, widgets, themes, icon packs, a UI editor and tons more!

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  dashy:
    image: lissy93/dashy:latest
    restart: unless-stopped
    ports:
      - 8080
    volumes:
      - dashy-config:/app/user-data
volumes:
  dashy-config: {}
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "dashy"
port = 8080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBkYXNoeTpcbiAgICBpbWFnZTogbGlzc3k5My9kYXNoeTpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSA4MDgwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGFzaHktY29uZmlnOi9hcHAvdXNlci1kYXRhXG52b2x1bWVzOlxuICBkYXNoeS1jb25maWc6IHt9IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtdXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJkYXNoeVwiXG5wb3J0ID0gODA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIiIKfQ==
```

## Links

`dashboard`,`monitoring`,`self-hosted`,`homelab`

---

Version:`latest`

CyberChefCyberChef is a web application for encryption, encoding, compression, and data analysis, developed by GCHQ.

DataLensA modern, scalable business intelligence and data visualization system.

### On this page

ConfigurationBase64LinksTags