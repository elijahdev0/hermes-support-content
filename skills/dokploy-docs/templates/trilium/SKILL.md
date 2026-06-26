---
title: "Trilium | Dokploy"
source: "https://docs.dokploy.com/docs/templates/trilium"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

Trilium | Dokploy

# Trilium

Copy as Markdown

Trilium Notes is a hierarchical note taking application with focus on building large personal knowledge bases.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  trilium:
    image: zadam/trilium:latest
    ports:
      - 8080
    restart: always
    volumes:
      - /root/trilium-backups:/home/node/trilium-data/backup
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "trilium"
port = 8_080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB0cmlsaXVtOlxuICAgIGltYWdlOiB6YWRhbS90cmlsaXVtOmxhdGVzdFxuICAgIHBvcnRzOlxuICAgICAgLSA4MDgwXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gL3Jvb3QvdHJpbGl1bS1iYWNrdXBzOi9ob21lL25vZGUvdHJpbGl1bS1kYXRhL2JhY2t1cFxuICBcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSB7fVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwidHJpbGl1bVwiXG5wb3J0ID0gOF8wODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`self-hosted`,`productivity`,`personal-use`

---

Version:`latest`

Trigger.devTrigger is a platform for building event-driven applications.

TriliumNextIs a free and open-source, cross-platform hierarchical note taking application with focus on building large personal knowledge bases.

### On this page

ConfigurationBase64LinksTags