---
title: "Typesense | Dokploy"
source: "https://docs.dokploy.com/docs/templates/typesense"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

Typesense | Dokploy

# Typesense

Copy as Markdown

Typesense is a fast, open-source search engine for building modern search experiences.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  typesense:
    image: typesense/typesense:29.0
    restart: unless-stopped
    environment:
      - TYPESENSE_API_KEY=${TYPESENSE_API_KEY}
      - TYPESENSE_ENABLE_CORS=${TYPESENSE_ENABLE_CORS}
      - TYPESENSE_DATA_DIR=/data
    volumes:
      - typesense-data:/data

volumes:
  typesense-data:
```

```
[variables]
main_domain = "${domain}"
api_key = "${password:16}"
enable_cors = "true"

[config]
env = ["TYPESENSE_API_KEY=${api_key}", "TYPESENSE_ENABLE_CORS=${enable_cors}"]

[[config.domains]]
serviceName = "typesense"
port = 8108
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICB0eXBlc2Vuc2U6XG4gICAgaW1hZ2U6IHR5cGVzZW5zZS90eXBlc2Vuc2U6MjkuMFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFRZUEVTRU5TRV9BUElfS0VZPSR7VFlQRVNFTlNFX0FQSV9LRVl9XG4gICAgICAtIFRZUEVTRU5TRV9FTkFCTEVfQ09SUz0ke1RZUEVTRU5TRV9FTkFCTEVfQ09SU31cbiAgICAgIC0gVFlQRVNFTlNFX0RBVEFfRElSPS9kYXRhXG4gICAgdm9sdW1lczpcbiAgICAgIC0gdHlwZXNlbnNlLWRhdGE6L2RhdGFcblxudm9sdW1lczpcbiAgdHlwZXNlbnNlLWRhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYXBpX2tleSA9IFwiJHtwYXNzd29yZDoxNn1cIlxuZW5hYmxlX2NvcnMgPSBcInRydWVcIlxuXG5bY29uZmlnXVxuZW52ID0gW1wiVFlQRVNFTlNFX0FQSV9LRVk9JHthcGlfa2V5fVwiLCBcIlRZUEVTRU5TRV9FTkFCTEVfQ09SUz0ke2VuYWJsZV9jb3JzfVwiXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ0eXBlc2Vuc2VcIlxucG9ydCA9IDgxMDhcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`search`

---

Version:`29.0`

TypechoTypecho 是一个轻量级的开源博客程序，基于 PHP 开发，支持多种数据库，简洁而强大。

UmamiUmami is a simple, fast, privacy-focused alternative to Google Analytics.

### On this page

ConfigurationBase64LinksTags