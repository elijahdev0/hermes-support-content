---
title: "Kener | Dokploy"
source: "https://docs.dokploy.com/docs/templates/kener"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

Kener | Dokploy

# Kener

Copy as Markdown

Kener is an open-source status page system for monitoring and alerting. It provides a modern interface for tracking service uptime and sending notifications.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  kener:
    image: rajnandan1/kener:latest
    environment:
      - TZ=${TZ}
      - KENER_SECRET_KEY=${KENER_SECRET_KEY} # 🔐 API key / secret
      - DATABASE_URL=${DATABASE_URL}
      - KENER_BASE_PATH=${KENER_BASE_PATH}
      - ORIGIN=${ORIGIN}
      - RESEND_API_KEY=${RESEND_API_KEY} # 🔐 API key
      - RESEND_SENDER_EMAIL=${RESEND_SENDER_EMAIL}
    ports:
      - 3000
    volumes:
      - kener_db:/app/database
      - ../files/uploads:/app/uploads
    restart: unless-stopped

  postgres:
    image: postgres:alpine
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD} # 🔐 DB password
      - POSTGRES_DB=${POSTGRES_DB}
    restart: unless-stopped

  mysql:
    image: mariadb:11
    environment:
      - MYSQL_USER=${MYSQL_USER}
      - MYSQL_PASSWORD=${MYSQL_PASSWORD} # 🔐 DB password
      - MYSQL_DATABASE=${MYSQL_DATABASE}
      - MYSQL_RANDOM_ROOT_PASSWORD=true
    restart: unless-stopped

volumes:
  kener_db: {}
```

```
[variables]
main_domain = "${domain}"
KENER_SECRET_KEY = "${password:64}"
POSTGRES_PASSWORD = "${password:32}"
MYSQL_PASSWORD = "${password:32}"

[config]
[[config.domains]]
serviceName = "kener"
port = 3000
host = "${main_domain}"

[config.env]
TZ = "Etc/UTC"
KENER_SECRET_KEY = "${KENER_SECRET_KEY}" # 🔐 API key / secret
DATABASE_URL = "sqlite://./database/kener.sqlite.db"
KENER_BASE_PATH = ""
ORIGIN = "http://localhost:3000"
RESEND_API_KEY = ""
RESEND_SENDER_EMAIL = "Accounts <[email protected]>"
POSTGRES_USER = "user"
POSTGRES_DB = "kener_db"
MYSQL_USER = "user"
MYSQL_DATABASE = "kener_db"
MYSQL_RANDOM_ROOT_PASSWORD = "true"
MYSQL_PASSWORD = "${MYSQL_PASSWORD}" # 🔐 DB password
POSTGRES_PASSWORD = "${POSTGRES_PASSWORD}" # 🔐 DB password

[[config.mounts]]
type = "volume"
source = "kener_db"
target = "/app/database"

[[config.mounts]]
type = "bind"
source = "../files/uploads"
target = "/app/uploads"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGtlbmVyOlxuICAgIGltYWdlOiByYWpuYW5kYW4xL2tlbmVyOmxhdGVzdFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBUWj0ke1RafVxuICAgICAgLSBLRU5FUl9TRUNSRVRfS0VZPSR7S0VORVJfU0VDUkVUX0tFWX0gIyDwn5SQIEFQSSBrZXkgLyBzZWNyZXRcbiAgICAgIC0gREFUQUJBU0VfVVJMPSR7REFUQUJBU0VfVVJMfVxuICAgICAgLSBLRU5FUl9CQVNFX1BBVEg9JHtLRU5FUl9CQVNFX1BBVEh9XG4gICAgICAtIE9SSUdJTj0ke09SSUdJTn1cbiAgICAgIC0gUkVTRU5EX0FQSV9LRVk9JHtSRVNFTkRfQVBJX0tFWX0gIyDwn5SQIEFQSSBrZXlcbiAgICAgIC0gUkVTRU5EX1NFTkRFUl9FTUFJTD0ke1JFU0VORF9TRU5ERVJfRU1BSUx9XG4gICAgcG9ydHM6XG4gICAgICAtIDMwMDBcbiAgICB2b2x1bWVzOlxuICAgICAgLSBrZW5lcl9kYjovYXBwL2RhdGFiYXNlXG4gICAgICAtIC4uL2ZpbGVzL3VwbG9hZHM6L2FwcC91cGxvYWRzXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6YWxwaW5lXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX1VTRVI9JHtQT1NUR1JFU19VU0VSfVxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke1BPU1RHUkVTX1BBU1NXT1JEfSAjIPCflJAgREIgcGFzc3dvcmRcbiAgICAgIC0gUE9TVEdSRVNfREI9JHtQT1NUR1JFU19EQn1cbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gIG15c3FsOlxuICAgIGltYWdlOiBtYXJpYWRiOjExXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE1ZU1FMX1VTRVI9JHtNWVNRTF9VU0VSfVxuICAgICAgLSBNWVNRTF9QQVNTV09SRD0ke01ZU1FMX1BBU1NXT1JEfSAjIPCflJAgREIgcGFzc3dvcmRcbiAgICAgIC0gTVlTUUxfREFUQUJBU0U9JHtNWVNRTF9EQVRBQkFTRX1cbiAgICAgIC0gTVlTUUxfUkFORE9NX1JPT1RfUEFTU1dPUkQ9dHJ1ZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbnZvbHVtZXM6XG4gIGtlbmVyX2RiOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbktFTkVSX1NFQ1JFVF9LRVkgPSBcIiR7cGFzc3dvcmQ6NjR9XCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5NWVNRTF9QQVNTV09SRCA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwia2VuZXJcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5UWiA9IFwiRXRjL1VUQ1wiXG5LRU5FUl9TRUNSRVRfS0VZID0gXCIke0tFTkVSX1NFQ1JFVF9LRVl9XCIgIyDwn5SQIEFQSSBrZXkgLyBzZWNyZXRcbkRBVEFCQVNFX1VSTCA9IFwic3FsaXRlOi8vLi9kYXRhYmFzZS9rZW5lci5zcWxpdGUuZGJcIlxuS0VORVJfQkFTRV9QQVRIID0gXCJcIlxuT1JJR0lOID0gXCJodHRwOi8vbG9jYWxob3N0OjMwMDBcIlxuUkVTRU5EX0FQSV9LRVkgPSBcIlwiXG5SRVNFTkRfU0VOREVSX0VNQUlMID0gXCJBY2NvdW50cyA8YWNjb3VudHNAcmVzZW5kLmRldj5cIlxuUE9TVEdSRVNfVVNFUiA9IFwidXNlclwiXG5QT1NUR1JFU19EQiA9IFwia2VuZXJfZGJcIlxuTVlTUUxfVVNFUiA9IFwidXNlclwiXG5NWVNRTF9EQVRBQkFTRSA9IFwia2VuZXJfZGJcIlxuTVlTUUxfUkFORE9NX1JPT1RfUEFTU1dPUkQgPSBcInRydWVcIlxuTVlTUUxfUEFTU1dPUkQgPSBcIiR7TVlTUUxfUEFTU1dPUkR9XCIgIyDwn5SQIERCIHBhc3N3b3JkXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtQT1NUR1JFU19QQVNTV09SRH1cIiAjIPCflJAgREIgcGFzc3dvcmRcblxuW1tjb25maWcubW91bnRzXV1cbnR5cGUgPSBcInZvbHVtZVwiXG5zb3VyY2UgPSBcImtlbmVyX2RiXCJcbnRhcmdldCA9IFwiL2FwcC9kYXRhYmFzZVwiXG5cbltbY29uZmlnLm1vdW50c11dXG50eXBlID0gXCJiaW5kXCJcbnNvdXJjZSA9IFwiLi4vZmlsZXMvdXBsb2Fkc1wiXG50YXJnZXQgPSBcIi9hcHAvdXBsb2Fkc1wiXG4iCn0=
```

## Links

`monitoring`,`status-page`,`alerting`,`self-hosted`

---

Version:`latest`

KaraKeepA self-hostable bookmark-everything app (links, notes and images) with AI-based automatic tagging and full text search. Previously known as Hoarder.

KestraUnified Orchestration Platform to Simplify Business-Critical Workflows and Govern them as Code and from the UI.

### On this page

ConfigurationBase64LinksTags