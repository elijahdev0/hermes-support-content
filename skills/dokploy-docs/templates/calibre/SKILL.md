---
title: "Calibre | Dokploy"
source: "https://docs.dokploy.com/docs/templates/calibre"
category: dokploy-docs
created: "2026-06-25T17:21:42.678Z"
---

Calibre | Dokploy

# Calibre

Copy as Markdown

Calibre is a comprehensive e-book management tool designed to organize, convert, and read your e-book collection. It supports most of the major e-book formats and is compatible with various e-book reader devices.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  calibre:
    image: linuxserver/calibre:7.26.0
    restart: unless-stopped
    environment:
      - PASSWORD=${PASSWORD}
      - TZ=Etc/UTC
      - PUID=1000
      - PGID=1000
    ports:
      - 8080
    volumes:
      - books:/books
      - data:/config

volumes:
  books:
  data:
```

```
[variables]
main_domain = "${domain}"
password = "${password:16}"

[config]
[[config.domains]]
serviceName = "calibre"
port = 8080
host = "${main_domain}"

[config.env]
PASSWORD = "${password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBjYWxpYnJlOlxuICAgIGltYWdlOiBsaW51eHNlcnZlci9jYWxpYnJlOjcuMjYuMFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBBU1NXT1JEPSR7UEFTU1dPUkR9XG4gICAgICAtIFRaPUV0Yy9VVENcbiAgICAgIC0gUFVJRD0xMDAwXG4gICAgICAtIFBHSUQ9MTAwMFxuICAgIHBvcnRzOlxuICAgICAgLSA4MDgwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gYm9va3M6L2Jvb2tzXG4gICAgICAtIGRhdGE6L2NvbmZpZ1xuXG52b2x1bWVzOlxuICBib29rczpcbiAgZGF0YTogIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnBhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjYWxpYnJlXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuUEFTU1dPUkQgPSBcIiR7cGFzc3dvcmR9XCIgIgp9
```

## Links

`Documents`,`E-Commerce`

---

Version:`7.26.0`

CalcomCalcom is a open source alternative to Calendly that allows to create scheduling and booking services.

Calibre-WebCalibre-Web is a web app providing a clean interface for browsing, reading, and managing your eBooks library using an existing Calibre database.

### On this page

ConfigurationBase64LinksTags