---
title: "AList | Dokploy"
source: "https://docs.dokploy.com/docs/templates/alist"
category: dokploy-docs
created: "2026-06-25T17:21:40.414Z"
---

AList | Dokploy

# AList

Copy as Markdown

🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.3'
services:
  alist:
    image: xhofe/alist:v3.55.0
    volumes:
      - alist-data:/opt/alist/data
    environment:
      - PUID=0
      - PGID=0
      - UMASK=022
    restart: unless-stopped

volumes:
  alist-data:
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "alist"
port = 5_244
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjMnXG5zZXJ2aWNlczpcbiAgYWxpc3Q6XG4gICAgaW1hZ2U6IHhob2ZlL2FsaXN0OnYzLjU1LjBcbiAgICB2b2x1bWVzOlxuICAgICAgLSBhbGlzdC1kYXRhOi9vcHQvYWxpc3QvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQVUlEPTBcbiAgICAgIC0gUEdJRD0wXG4gICAgICAtIFVNQVNLPTAyMlxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbnZvbHVtZXM6XG4gIGFsaXN0LWRhdGE6IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtdXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhbGlzdFwiXG5wb3J0ID0gNV8yNDRcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`file`,`webdav`,`storage`

---

Version:`v3.55.0`

AkauntingAkaunting is a self-hosted, open-source accounting app for small businesses.

AllTubeAllTube Download is an application designed to facilitate the downloading of videos from YouTube and other video sites. It provides an HTML GUI for youtube-dl with video conversion capabilities and JSON API support.

### On this page

ConfigurationBase64LinksTags