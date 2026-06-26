---
title: "teable | Dokploy"
source: "https://docs.dokploy.com/docs/templates/teable"
category: dokploy-docs
created: "2026-06-25T17:22:00.274Z"
---

teable | Dokploy

# teable

Copy as Markdown

Teable is a Super fast, Real-time, Professional, Developer friendly, No-code database built on Postgres. It uses a simple, spreadsheet-like interface to create complex enterprise-level database applications. Unlock efficient app development with no-code, free from the hurdles of data security and scalability.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.9"

services:
  teable:
    image: ghcr.io/teableio/teable:latest
    restart: always
    volumes:
      - teable-data:/app/.assets
      # you may use a bind-mounted host directory instead,
      # so that it is harder to accidentally remove the volume and lose all your data!
      # - ./docker/teable/data:/app/.assets:rw
    environment:
      - TZ=${TIMEZONE}
      - NEXT_ENV_IMAGES_ALL_REMOTE=true
      - PUBLIC_ORIGIN=${PUBLIC_ORIGIN}
      - PRISMA_DATABASE_URL=${PRISMA_DATABASE_URL}
      - PUBLIC_DATABASE_PROXY=${PUBLIC_DATABASE_PROXY}
      - BACKEND_MAIL_HOST=${BACKEND_MAIL_HOST}
      - BACKEND_MAIL_PORT=${BACKEND_MAIL_PORT}
      - BACKEND_MAIL_SECURE=${BACKEND_MAIL_SECURE}
      - BACKEND_MAIL_SENDER=${BACKEND_MAIL_SENDER}
      - BACKEND_MAIL_SENDER_NAME=${BACKEND_MAIL_SENDER_NAME}
      - BACKEND_MAIL_AUTH_USER=${BACKEND_MAIL_AUTH_USER}
      - BACKEND_MAIL_AUTH_PASS=${BACKEND_MAIL_AUTH_PASS}
    depends_on:
      teable-db-migrate:
        condition: service_completed_successfully

  teable-db:
    image: postgres:15.4
    restart: always
    ports:
      - "${TEABLE_DB_PORT}:${POSTGRES_PORT}"
    volumes:
      - teable-db:/var/lib/postgresql/data
      # you may use a bind-mounted host directory instead,
      # so that it is harder to accidentally remove the volume and lose all your data!
      # - ./docker/db/data:/var/lib/postgresql/data:rw
    environment:
      - TZ=${TIMEZONE}
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}

    healthcheck:
      test:
        [
          "CMD-SHELL",
          "sh -c 'pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}'",
        ]
      interval: 10s
      timeout: 3s
      retries: 3

  teable-db-migrate:
    image: ghcr.io/teableio/teable-db-migrate:latest
    environment:
      - TZ=${TIMEZONE}
      - PRISMA_DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

    depends_on:
      teable-db:
        condition: service_healthy

volumes:
  teable-data: {}
  teable-db: {}
```

```
[variables]
main_domain = "${domain}"
db_password = "${password}"
public_db_port = "${randomPort}"

[config]
mounts = []

[[config.domains]]
serviceName = "teable"
port = 3_000
host = "${main_domain}"

[config.env]
TEABLE_HOST = "${main_domain}"
TEABLE_DB_PORT = "${public_db_port}"
TIMEZONE = "UTC"
POSTGRES_HOST = "teable-db"
POSTGRES_PORT = "5432"
POSTGRES_DB = "teable"
POSTGRES_USER = "teable"
POSTGRES_PASSWORD = "${db_password}"
PUBLIC_ORIGIN = "https://${main_domain}"
PRISMA_DATABASE_URL = "postgresql://teable:${db_password}@teable-db:5432/teable"
PUBLIC_DATABASE_PROXY = "${TEABLE_HOST}:${TEABLE_DB_PORT}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy45XCJcblxuc2VydmljZXM6XG4gIHRlYWJsZTpcbiAgICBpbWFnZTogZ2hjci5pby90ZWFibGVpby90ZWFibGU6bGF0ZXN0XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gdGVhYmxlLWRhdGE6L2FwcC8uYXNzZXRzXG4gICAgICAjIHlvdSBtYXkgdXNlIGEgYmluZC1tb3VudGVkIGhvc3QgZGlyZWN0b3J5IGluc3RlYWQsXG4gICAgICAjIHNvIHRoYXQgaXQgaXMgaGFyZGVyIHRvIGFjY2lkZW50YWxseSByZW1vdmUgdGhlIHZvbHVtZSBhbmQgbG9zZSBhbGwgeW91ciBkYXRhIVxuICAgICAgIyAtIC4vZG9ja2VyL3RlYWJsZS9kYXRhOi9hcHAvLmFzc2V0czpyd1xuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBUWj0ke1RJTUVaT05FfVxuICAgICAgLSBORVhUX0VOVl9JTUFHRVNfQUxMX1JFTU9URT10cnVlXG4gICAgICAtIFBVQkxJQ19PUklHSU49JHtQVUJMSUNfT1JJR0lOfVxuICAgICAgLSBQUklTTUFfREFUQUJBU0VfVVJMPSR7UFJJU01BX0RBVEFCQVNFX1VSTH1cbiAgICAgIC0gUFVCTElDX0RBVEFCQVNFX1BST1hZPSR7UFVCTElDX0RBVEFCQVNFX1BST1hZfVxuICAgICAgLSBCQUNLRU5EX01BSUxfSE9TVD0ke0JBQ0tFTkRfTUFJTF9IT1NUfVxuICAgICAgLSBCQUNLRU5EX01BSUxfUE9SVD0ke0JBQ0tFTkRfTUFJTF9QT1JUfVxuICAgICAgLSBCQUNLRU5EX01BSUxfU0VDVVJFPSR7QkFDS0VORF9NQUlMX1NFQ1VSRX1cbiAgICAgIC0gQkFDS0VORF9NQUlMX1NFTkRFUj0ke0JBQ0tFTkRfTUFJTF9TRU5ERVJ9XG4gICAgICAtIEJBQ0tFTkRfTUFJTF9TRU5ERVJfTkFNRT0ke0JBQ0tFTkRfTUFJTF9TRU5ERVJfTkFNRX1cbiAgICAgIC0gQkFDS0VORF9NQUlMX0FVVEhfVVNFUj0ke0JBQ0tFTkRfTUFJTF9BVVRIX1VTRVJ9XG4gICAgICAtIEJBQ0tFTkRfTUFJTF9BVVRIX1BBU1M9JHtCQUNLRU5EX01BSUxfQVVUSF9QQVNTfVxuICAgIGRlcGVuZHNfb246XG4gICAgICB0ZWFibGUtZGItbWlncmF0ZTpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2NvbXBsZXRlZF9zdWNjZXNzZnVsbHlcblxuICB0ZWFibGUtZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE1LjRcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBwb3J0czpcbiAgICAgIC0gXCIke1RFQUJMRV9EQl9QT1JUfToke1BPU1RHUkVTX1BPUlR9XCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSB0ZWFibGUtZGI6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgICAjIHlvdSBtYXkgdXNlIGEgYmluZC1tb3VudGVkIGhvc3QgZGlyZWN0b3J5IGluc3RlYWQsXG4gICAgICAjIHNvIHRoYXQgaXQgaXMgaGFyZGVyIHRvIGFjY2lkZW50YWxseSByZW1vdmUgdGhlIHZvbHVtZSBhbmQgbG9zZSBhbGwgeW91ciBkYXRhIVxuICAgICAgIyAtIC4vZG9ja2VyL2RiL2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhOnJ3XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFRaPSR7VElNRVpPTkV9XG4gICAgICAtIFBPU1RHUkVTX0RCPSR7UE9TVEdSRVNfREJ9XG4gICAgICAtIFBPU1RHUkVTX1VTRVI9JHtQT1NUR1JFU19VU0VSfVxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke1BPU1RHUkVTX1BBU1NXT1JEfVxuXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICBbXG4gICAgICAgICAgXCJDTUQtU0hFTExcIixcbiAgICAgICAgICBcInNoIC1jICdwZ19pc3JlYWR5IC1VICR7UE9TVEdSRVNfVVNFUn0gLWQgJHtQT1NUR1JFU19EQn0nXCIsXG4gICAgICAgIF1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDNzXG4gICAgICByZXRyaWVzOiAzXG5cbiAgdGVhYmxlLWRiLW1pZ3JhdGU6XG4gICAgaW1hZ2U6IGdoY3IuaW8vdGVhYmxlaW8vdGVhYmxlLWRiLW1pZ3JhdGU6bGF0ZXN0XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFRaPSR7VElNRVpPTkV9XG4gICAgICAtIFBSSVNNQV9EQVRBQkFTRV9VUkw9cG9zdGdyZXNxbDovLyR7UE9TVEdSRVNfVVNFUn06JHtQT1NUR1JFU19QQVNTV09SRH1AJHtQT1NUR1JFU19IT1NUfToke1BPU1RHUkVTX1BPUlR9LyR7UE9TVEdSRVNfREJ9XG5cbiAgICBkZXBlbmRzX29uOlxuICAgICAgdGVhYmxlLWRiOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuXG52b2x1bWVzOlxuICB0ZWFibGUtZGF0YToge31cbiAgdGVhYmxlLWRiOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkfVwiXG5wdWJsaWNfZGJfcG9ydCA9IFwiJHtyYW5kb21Qb3J0fVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ0ZWFibGVcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuVEVBQkxFX0hPU1QgPSBcIiR7bWFpbl9kb21haW59XCJcblRFQUJMRV9EQl9QT1JUID0gXCIke3B1YmxpY19kYl9wb3J0fVwiXG5USU1FWk9ORSA9IFwiVVRDXCJcblBPU1RHUkVTX0hPU1QgPSBcInRlYWJsZS1kYlwiXG5QT1NUR1JFU19QT1JUID0gXCI1NDMyXCJcblBPU1RHUkVTX0RCID0gXCJ0ZWFibGVcIlxuUE9TVEdSRVNfVVNFUiA9IFwidGVhYmxlXCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiXG5QVUJMSUNfT1JJR0lOID0gXCJodHRwczovLyR7bWFpbl9kb21haW59XCJcblBSSVNNQV9EQVRBQkFTRV9VUkwgPSBcInBvc3RncmVzcWw6Ly90ZWFibGU6JHtkYl9wYXNzd29yZH1AdGVhYmxlLWRiOjU0MzIvdGVhYmxlXCJcblBVQkxJQ19EQVRBQkFTRV9QUk9YWSA9IFwiJHtURUFCTEVfSE9TVH06JHtURUFCTEVfREJfUE9SVH1cIlxuIgp9
```

## Links

`database`,`spreadsheet`,`low-code`,`nocode`

---

Version:`v1.3.1-alpha-build.460`

Tailscale Exit nodesTailscale ExitNode is a feature that lets you route your internet traffic through a specific device in your Tailscale network.

TianjiTianji is a lightweight web analytic service and uptime monitoring tool.

### On this page

ConfigurationBase64LinksTags