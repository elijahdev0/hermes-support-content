---
title: "Bytebase | Dokploy"
source: "https://docs.dokploy.com/docs/templates/bytebase"
category: dokploy-docs
created: "2026-06-25T17:21:42.677Z"
---

Bytebase | Dokploy

# Bytebase

Copy as Markdown

Bytebase is a database management tool that allows you to manage your databases with ease. It provides a simple and effective solution for managing your databases from anywhere.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  bytebase:
    image: bytebase/bytebase:3.3.0
    restart: unless-stopped
    ports:
      - 8080
    environment:
      - PG_URL=postgres://postgres:${DB_PASSWORD}@bytebase-db:5432/bytebase
    volumes:
      - data:/var/opt/bytebase
    depends_on:
      - bytebase-db

  bytebase-db:
    image: postgres:13
    restart: unless-stopped
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=bytebase
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  data: {}
  db_data: {}
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:16}"

[config]
[[config.domains]]
serviceName = "bytebase"
port = 8080
host = "${main_domain}"

[config.env]
DB_PASSWORD = "${db_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBieXRlYmFzZTpcbiAgICBpbWFnZTogYnl0ZWJhc2UvYnl0ZWJhc2U6My4zLjBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSA4MDgwXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBHX1VSTD1wb3N0Z3JlczovL3Bvc3RncmVzOiR7REJfUEFTU1dPUkR9QGJ5dGViYXNlLWRiOjU0MzIvYnl0ZWJhc2VcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYXRhOi92YXIvb3B0L2J5dGViYXNlXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gYnl0ZWJhc2UtZGJcblxuICBieXRlYmFzZS1kYjpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTNcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19VU0VSPXBvc3RncmVzXG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPSR7REJfUEFTU1dPUkR9XG4gICAgICAtIFBPU1RHUkVTX0RCPWJ5dGViYXNlXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGJfZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcblxudm9sdW1lczpcbiAgZGF0YToge31cbiAgZGJfZGF0YToge30gIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJieXRlYmFzZVwiXG5wb3J0ID0gODA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkRCX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiICIKfQ==
```

## Links

`database`,`self-hosted`

---

Version:`latest`

BugsinkBugsink is a self-hosted Error Tracker. Built to self-host; Sentry-SDK compatible; Scalable and reliable

ByteStashByteStash is a self-hosted web application designed to store, organise, and manage your code snippets efficiently. With support for creating, editing, and filtering snippets, ByteStash helps you keep track of your code in one secure place.

### On this page

ConfigurationBase64LinksTags