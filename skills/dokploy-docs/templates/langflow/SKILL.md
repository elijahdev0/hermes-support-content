---
title: "Langflow | Dokploy"
source: "https://docs.dokploy.com/docs/templates/langflow"
category: dokploy-docs
created: "2026-06-25T17:21:52.045Z"
---

Langflow | Dokploy

# Langflow

Copy as Markdown

Langflow is a low-code app builder for RAG and multi-agent AI applications. It's Python-based and agnostic to any model, API, or database.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  langflow:
    image: langflowai/langflow:v1.1.1
    ports:
      - 7860
    depends_on:
      - postgres-langflow
    environment:
      - LANGFLOW_DATABASE_URL=postgresql://${DB_USERNAME}:${DB_PASSWORD}@postgres-langflow:5432/langflow
      # This variable defines where the logs, file storage, monitor data and secret keys are stored.
    volumes:
      - langflow-data:/app/langflow

  postgres-langflow:
    image: postgres:16
    environment:
      POSTGRES_USER: ${DB_USERNAME}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: langflow
    ports:
      - 5432
    volumes:
      - langflow-postgres:/var/lib/postgresql/data

volumes:
  langflow-postgres:
  langflow-data:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password}"
db_username = "langflow"

[config]
mounts = []

[[config.domains]]
serviceName = "langflow"
port = 7_860
host = "${main_domain}"

[config.env]
DB_PASSWORD = "${db_password}"
DB_USERNAME = "${db_username}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGxhbmdmbG93OlxuICAgIGltYWdlOiBsYW5nZmxvd2FpL2xhbmdmbG93OnYxLjEuMVxuICAgIHBvcnRzOlxuICAgICAgLSA3ODYwXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcG9zdGdyZXMtbGFuZ2Zsb3dcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTEFOR0ZMT1dfREFUQUJBU0VfVVJMPXBvc3RncmVzcWw6Ly8ke0RCX1VTRVJOQU1FfToke0RCX1BBU1NXT1JEfUBwb3N0Z3Jlcy1sYW5nZmxvdzo1NDMyL2xhbmdmbG93XG4gICAgICAjIFRoaXMgdmFyaWFibGUgZGVmaW5lcyB3aGVyZSB0aGUgbG9ncywgZmlsZSBzdG9yYWdlLCBtb25pdG9yIGRhdGEgYW5kIHNlY3JldCBrZXlzIGFyZSBzdG9yZWQuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gbGFuZ2Zsb3ctZGF0YTovYXBwL2xhbmdmbG93XG5cblxuICBwb3N0Z3Jlcy1sYW5nZmxvdzpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTZcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTX1VTRVI6ICR7REJfVVNFUk5BTUV9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtEQl9QQVNTV09SRH1cbiAgICAgIFBPU1RHUkVTX0RCOiBsYW5nZmxvd1xuICAgIHBvcnRzOlxuICAgICAgLSA1NDMyXG4gICAgdm9sdW1lczpcbiAgICAgIC0gbGFuZ2Zsb3ctcG9zdGdyZXM6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG5cblxudm9sdW1lczpcbiAgbGFuZ2Zsb3ctcG9zdGdyZXM6XG4gIGxhbmdmbG93LWRhdGE6IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkfVwiXG5kYl91c2VybmFtZSA9IFwibGFuZ2Zsb3dcIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibGFuZ2Zsb3dcIlxucG9ydCA9IDdfODYwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuREJfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcbkRCX1VTRVJOQU1FID0gXCIke2RiX3VzZXJuYW1lfVwiXG4iCn0=
```

## Links

`ai`

---

Version:`1.1.1`

KuttKutt is a modern URL shortener with support for custom domains. Create and edit links, view statistics, manage users, and more.

LavalinkLavalink is an open source standalone audio sending node based on Lavaplayer.

### On this page

ConfigurationBase64LinksTags