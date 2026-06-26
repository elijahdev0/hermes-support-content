---
title: "Wiki.js | Dokploy"
source: "https://docs.dokploy.com/docs/templates/wikijs"
category: dokploy-docs
created: "2026-06-25T17:22:01.420Z"
---

Wiki.js | Dokploy

# Wiki.js

Copy as Markdown

The most powerful and extensible open source Wiki software.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.5'
services:
  wiki:
    image: ghcr.io/requarks/wiki:2.5
    restart: unless-stopped
    environment:
      - DB_TYPE
      - DB_HOST
      - DB_PORT
      - DB_USER
      - DB_PASS
      - DB_NAME
    depends_on:
      - db
    labels:
      - traefik.enable=true
      - traefik.constraint-label-stack=wikijs
  db:
    image: postgres:14
    restart: unless-stopped
    environment:
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_DB
    volumes:
      - wiki-db-data:/var/lib/postgresql/data
volumes:
  wiki-db-data:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "wiki"
port = 3_000
host = "${main_domain}"

[config.env]
POSTGRES_USER = "wikijs"
POSTGRES_PASSWORD = "wikijsrocks"
POSTGRES_DB = "wiki"
DB_TYPE = "postgres"
DB_HOST = "db"
DB_PORT = "5432"
DB_USER = "wikijs"
DB_PASS = "wikijsrocks"
DB_NAME = "wiki"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjUnXG5zZXJ2aWNlczpcbiAgd2lraTpcbiAgICBpbWFnZTogZ2hjci5pby9yZXF1YXJrcy93aWtpOjIuNVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIERCX1RZUEVcbiAgICAgIC0gREJfSE9TVFxuICAgICAgLSBEQl9QT1JUXG4gICAgICAtIERCX1VTRVJcbiAgICAgIC0gREJfUEFTU1xuICAgICAgLSBEQl9OQU1FXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gZGJcbiAgICBsYWJlbHM6XG4gICAgICAtIHRyYWVmaWsuZW5hYmxlPXRydWVcbiAgICAgIC0gdHJhZWZpay5jb25zdHJhaW50LWxhYmVsLXN0YWNrPXdpa2lqc1xuICBkYjpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTRcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19VU0VSXG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEXG4gICAgICAtIFBPU1RHUkVTX0RCXG4gICAgdm9sdW1lczpcbiAgICAgIC0gd2lraS1kYi1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxudm9sdW1lczpcbiAgd2lraS1kYi1kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIndpa2lcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuUE9TVEdSRVNfVVNFUiA9IFwid2lraWpzXCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCJ3aWtpanNyb2Nrc1wiXG5QT1NUR1JFU19EQiA9IFwid2lraVwiXG5EQl9UWVBFID0gXCJwb3N0Z3Jlc1wiXG5EQl9IT1NUID0gXCJkYlwiXG5EQl9QT1JUID0gXCI1NDMyXCJcbkRCX1VTRVIgPSBcIndpa2lqc1wiXG5EQl9QQVNTID0gXCJ3aWtpanNyb2Nrc1wiXG5EQl9OQU1FID0gXCJ3aWtpXCJcbiIKfQ==
```

## Links

`knowledge-base`,`self-hosted`,`documentation`

---

Version:`2.5`

WG-EasyWG-Easy is a simple and user-friendly WireGuard VPN server with a web interface for easy management.

WindmillA developer platform to build production-grade workflows and internal apps. Open-source alternative to Airplane, Retool, and GitHub Actions.

### On this page

ConfigurationBase64LinksTags