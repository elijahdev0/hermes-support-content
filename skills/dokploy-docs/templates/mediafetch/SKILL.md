---
title: "MediaFetch | Dokploy"
source: "https://docs.dokploy.com/docs/templates/mediafetch"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

MediaFetch | Dokploy

# MediaFetch

Copy as Markdown

A tiny, self-hosted web wrapper for yt-dlp to download video and audio. Optional basic auth.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  mediafetch:
    image: lukedunsmoto/mediafetch:latest
    restart: unless-stopped
    expose:
      - "3002"
    volumes:
      - mediafetch_data:/data/downloads
    environment:
      - PORT=3002
      - BASIC_AUTH_USER=${BASIC_AUTH_USER}
      - BASIC_AUTH_PASS=${BASIC_AUTH_PASS}
      - PUBLIC_BASE_URL=https://${DOMAIN}
      - OUTPUT_DIR=/data/downloads

volumes:
  mediafetch_data:
```

```
[variables]
BASIC_AUTH_USER = "admin"
BASIC_AUTH_PASS = "${password:12}"

[config]
[[config.domains]]
name = "Domain"
variable = "DOMAIN"
serviceName = "mediafetch"
port = 3002

[[config.mounts]]
name = "Downloads"
filePath = "/data/downloads"
content = "mediafetch"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBtZWRpYWZldGNoOlxuICAgIGltYWdlOiBsdWtlZHVuc21vdG8vbWVkaWFmZXRjaDpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGV4cG9zZTpcbiAgICAgIC0gXCIzMDAyXCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBtZWRpYWZldGNoX2RhdGE6L2RhdGEvZG93bmxvYWRzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPUlQ9MzAwMlxuICAgICAgLSBCQVNJQ19BVVRIX1VTRVI9JHtCQVNJQ19BVVRIX1VTRVJ9XG4gICAgICAtIEJBU0lDX0FVVEhfUEFTUz0ke0JBU0lDX0FVVEhfUEFTU31cbiAgICAgIC0gUFVCTElDX0JBU0VfVVJMPWh0dHBzOi8vJHtET01BSU59XG4gICAgICAtIE9VVFBVVF9ESVI9L2RhdGEvZG93bmxvYWRzXG5cbnZvbHVtZXM6XG4gIG1lZGlhZmV0Y2hfZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbkJBU0lDX0FVVEhfVVNFUiA9IFwiYWRtaW5cIlxuQkFTSUNfQVVUSF9QQVNTID0gXCIke3Bhc3N3b3JkOjEyfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbm5hbWUgPSBcIkRvbWFpblwiXG52YXJpYWJsZSA9IFwiRE9NQUlOXCJcbnNlcnZpY2VOYW1lID0gXCJtZWRpYWZldGNoXCJcbnBvcnQgPSAzMDAyXG5cbltbY29uZmlnLm1vdW50c11dXG5uYW1lID0gXCJEb3dubG9hZHNcIlxuZmlsZVBhdGggPSBcIi9kYXRhL2Rvd25sb2Fkc1wiXG5jb250ZW50ID0gXCJtZWRpYWZldGNoXCIiCn0=
```

## Links

`utilities`,`media`,`downloader`

---

Version:`1.1.1`

MediaCMSMediaCMS is an open-source video and media CMS. It is a modern, full-featured solution for managing and streaming media content.

MeilisearchMeilisearch is a free and open-source search engine that allows you to easily add search functionality to your web applications.

### On this page

ConfigurationBase64LinksTags