---
title: "Memos | Dokploy"
source: "https://docs.dokploy.com/docs/templates/memos"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

Memos | Dokploy

# Memos

Copy as Markdown

Memos is a self-hosted, open-source note-taking application that allows you to create, organize, and share notes with ease. It provides a simple and effective solution for managing your notes from anywhere.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  memos:
    image: neosmemo/memos:stable
    restart: unless-stopped
    volumes:
      - memos_data:/var/opt/memos
    environment:
      - MEMOS_MODE=${MEMOS_MODE}
      - MEMOS_PORT=${MEMOS_PORT}
    ports:
      - "5230"
volumes:
  memos_data:
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "memos"
port = 5230
host = "${main_domain}"

[config.env]
MEMOS_MODE = "prod"
MEMOS_PORT = "5230"
[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIG1lbW9zOlxuICAgIGltYWdlOiBuZW9zbWVtby9tZW1vczpzdGFibGVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIG1lbW9zX2RhdGE6L3Zhci9vcHQvbWVtb3NcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTUVNT1NfTU9ERT0ke01FTU9TX01PREV9XG4gICAgICAtIE1FTU9TX1BPUlQ9JHtNRU1PU19QT1JUfVxuICAgIHBvcnRzOlxuICAgICAgLSBcIjUyMzBcIlxudm9sdW1lczpcbiAgbWVtb3NfZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJtZW1vc1wiXG5wb3J0ID0gNTIzMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5cbltjb25maWcuZW52XVxuTUVNT1NfTU9ERSA9IFwicHJvZFwiXG5NRU1PU19QT1JUID0gXCI1MjMwXCJcbltbY29uZmlnLm1vdW50c11dIgp9
```

## Links

`productivity`,`notes`,`bookmarks`

---

Version:`latest`

MeilisearchMeilisearch is a free and open-source search engine that allows you to easily add search functionality to your web applications.

MetabaseMetabase is an open source business intelligence tool that allows you to ask questions and visualize data.

### On this page

ConfigurationBase64LinksTags