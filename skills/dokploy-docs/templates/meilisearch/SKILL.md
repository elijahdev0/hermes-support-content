---
title: "Meilisearch | Dokploy"
source: "https://docs.dokploy.com/docs/templates/meilisearch"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

Meilisearch | Dokploy

# Meilisearch

Copy as Markdown

Meilisearch is a free and open-source search engine that allows you to easily add search functionality to your web applications.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  meilisearch:
    image: getmeili/meilisearch:v1.8.3
    volumes:
      - meili_data:/meili_data
    environment:
      MEILI_MASTER_KEY: ${MEILI_MASTER_KEY}
      MEILI_ENV: ${MEILI_ENV}

volumes:
  meili_data:
    driver: local
```

```
[variables]
main_domain = "${domain}"
master_key = "${base64:32}"

[config]
mounts = []

[[config.domains]]
serviceName = "meilisearch"
port = 7_700
host = "${main_domain}"

[config.env]
MEILI_ENV = "development"
MEILI_MASTER_KEY = "${master_key}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIG1laWxpc2VhcmNoOlxuICAgIGltYWdlOiBnZXRtZWlsaS9tZWlsaXNlYXJjaDp2MS44LjNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBtZWlsaV9kYXRhOi9tZWlsaV9kYXRhXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNRUlMSV9NQVNURVJfS0VZOiAke01FSUxJX01BU1RFUl9LRVl9XG4gICAgICBNRUlMSV9FTlY6ICR7TUVJTElfRU5WfVxuXG52b2x1bWVzOlxuICBtZWlsaV9kYXRhOlxuICAgIGRyaXZlcjogbG9jYWxcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5tYXN0ZXJfa2V5ID0gXCIke2Jhc2U2NDozMn1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibWVpbGlzZWFyY2hcIlxucG9ydCA9IDdfNzAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuTUVJTElfRU5WID0gXCJkZXZlbG9wbWVudFwiXG5NRUlMSV9NQVNURVJfS0VZID0gXCIke21hc3Rlcl9rZXl9XCJcbiIKfQ==
```

## Links

`search`

---

Version:`v1.8.3`

MediaFetchA tiny, self-hosted web wrapper for yt-dlp to download video and audio. Optional basic auth.

MemosMemos is a self-hosted, open-source note-taking application that allows you to create, organize, and share notes with ease. It provides a simple and effective solution for managing your notes from anywhere.

### On this page

ConfigurationBase64LinksTags