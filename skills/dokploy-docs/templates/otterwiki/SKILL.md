---
title: "Otter Wiki | Dokploy"
source: "https://docs.dokploy.com/docs/templates/otterwiki"
category: dokploy-docs
created: "2026-06-25T17:21:55.476Z"
---

Otter Wiki | Dokploy

# Otter Wiki

Copy as Markdown

An Otter Wiki is a simple, lightweight, and fast wiki engine built with Python and Flask. It provides a user-friendly interface for creating and managing wiki content with markdown support.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  otterwiki:
    image: redimp/otterwiki:2
    restart: unless-stopped
    volumes:
      - otterwiki-data:/app-data

volumes:
  otterwiki-data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "otterwiki"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBvdHRlcndpa2k6XG4gICAgaW1hZ2U6IHJlZGltcC9vdHRlcndpa2k6MlxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gb3R0ZXJ3aWtpLWRhdGE6L2FwcC1kYXRhXG5cbnZvbHVtZXM6XG4gIG90dGVyd2lraS1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtdXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJvdHRlcndpa2lcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`wiki`,`documentation`,`knowledge-base`,`markdown`

---

Version:`2`

OpenSpeedTestOpenSpeedTest is a 100% browser-based HTML5 network performance estimation tool for accurately measuring network speed.

OutlineOutline is a self-hosted knowledge base and documentation platform that allows you to build and manage your own knowledge base applications.

### On this page

ConfigurationBase64LinksTags