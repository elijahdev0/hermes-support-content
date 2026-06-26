---
title: "SurrealDB | Dokploy"
source: "https://docs.dokploy.com/docs/templates/surrealdb"
category: dokploy-docs
created: "2026-06-25T17:22:00.274Z"
---

SurrealDB | Dokploy

# SurrealDB

Copy as Markdown

SurrealDB is a native, open-source, multi-model database that lets you store and manage data across relational, document, graph, time-series, vector & search, and geospatial models—all in one place.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  surrealdb:
    image: surrealdb/surrealdb:v2.3.10
    environment:
      SURREAL_USER: ${SURREAL_USER}
      SURREAL_PASS: ${SURREAL_PASS}
    volumes:
      - db_data:/usr/app/data
    user: root
    command: start rocksdb:/db_data/data.db
    pull_policy: always

volumes:
  db_data: {}
```

```
[variables]
main_domain = "${domain}"
surrealdb_user = "${username}"
surrealdb_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "surrealdb"
port = 8000
host = "${main_domain}"

[config.env]
SURREAL_USER = "${surrealdb_user}"
SURREAL_PASS = "${surrealdb_password}"

[[config.mounts]]
serviceName = "surrealdb"
volumeName = "db_data"
mountPath = "/usr/app/data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBzdXJyZWFsZGI6XG4gICAgaW1hZ2U6IHN1cnJlYWxkYi9zdXJyZWFsZGI6djIuMy4xMFxuICAgIGVudmlyb25tZW50OlxuICAgICAgU1VSUkVBTF9VU0VSOiAke1NVUlJFQUxfVVNFUn1cbiAgICAgIFNVUlJFQUxfUEFTUzogJHtTVVJSRUFMX1BBU1N9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGJfZGF0YTovdXNyL2FwcC9kYXRhXG4gICAgdXNlcjogcm9vdFxuICAgIGNvbW1hbmQ6IHN0YXJ0IHJvY2tzZGI6L2RiX2RhdGEvZGF0YS5kYlxuICAgIHB1bGxfcG9saWN5OiBhbHdheXNcblxudm9sdW1lczpcbiAgZGJfZGF0YToge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5zdXJyZWFsZGJfdXNlciA9IFwiJHt1c2VybmFtZX1cIlxuc3VycmVhbGRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJzdXJyZWFsZGJcIlxucG9ydCA9IDgwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5TVVJSRUFMX1VTRVIgPSBcIiR7c3VycmVhbGRiX3VzZXJ9XCJcblNVUlJFQUxfUEFTUyA9IFwiJHtzdXJyZWFsZGJfcGFzc3dvcmR9XCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJzdXJyZWFsZGJcIlxudm9sdW1lTmFtZSA9IFwiZGJfZGF0YVwiXG5tb3VudFBhdGggPSBcIi91c3IvYXBwL2RhdGFcIlxuIgp9
```

## Links

`database`,`sql`,`surrealdb`

---

Version:`2.3.10`

Superset (Unofficial)Data visualization and data exploration platform.

SyncthingSyncthing is a continuous file synchronization program that synchronizes files between two or more computers in real time.

### On this page

ConfigurationBase64LinksTags