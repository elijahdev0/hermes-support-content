---
title: "Bazarr | Dokploy"
source: "https://docs.dokploy.com/docs/templates/bazarr"
category: dokploy-docs
created: "2026-06-25T17:21:41.530Z"
---

Bazarr | Dokploy

# Bazarr

Copy as Markdown

Bazarr is a companion application to Sonarr and Radarr that manages and downloads subtitles based on your requirements.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  bazarr:
    image: lscr.io/linuxserver/bazarr:1.5.1
    restart: unless-stopped
    ports:
      - 6767
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=UTC
    volumes:
      - config:/config
      - ${MOVIES_PATH}:/movies
      - ${TV_PATH}:/tv

volumes:
  config: {}
```

```
[variables]
main_domain = "${domain}"
movies_path = "/path/to/movies"
tv_path = "/path/to/tv"

[config]
[[config.domains]]
serviceName = "bazarr"
port = 6767
host = "${main_domain}"

[config.env]
MOVIES_PATH = "${movies_path}"
TV_PATH = "${tv_path}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBiYXphcnI6XG4gICAgaW1hZ2U6IGxzY3IuaW8vbGludXhzZXJ2ZXIvYmF6YXJyOjEuNS4xXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gNjc2N1xuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQVUlEPTEwMDBcbiAgICAgIC0gUEdJRD0xMDAwXG4gICAgICAtIFRaPVVUQ1xuICAgIHZvbHVtZXM6XG4gICAgICAtIGNvbmZpZzovY29uZmlnXG4gICAgICAtICR7TU9WSUVTX1BBVEh9Oi9tb3ZpZXNcbiAgICAgIC0gJHtUVl9QQVRIfTovdHZcblxudm9sdW1lczpcbiAgY29uZmlnOiB7fSAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxubW92aWVzX3BhdGggPSBcIi9wYXRoL3RvL21vdmllc1wiXG50dl9wYXRoID0gXCIvcGF0aC90by90dlwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJiYXphcnJcIlxucG9ydCA9IDY3Njdcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5NT1ZJRVNfUEFUSCA9IFwiJHttb3ZpZXNfcGF0aH1cIlxuVFZfUEFUSCA9IFwiJHt0dl9wYXRofVwiICIKfQ==
```

## Links

`subtitles`,`sonarr`,`radarr`

---

Version:`latest`

BaserowBaserow is an open source database management tool that allows you to create and manage databases.

BentoPDFBentoPDF is a lightweight PDF conversion microservice that exposes a simple HTTP API for generating PDFs.

### On this page

ConfigurationBase64LinksTags