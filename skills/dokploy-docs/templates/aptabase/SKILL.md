---
title: "Aptabase | Dokploy"
source: "https://docs.dokploy.com/docs/templates/aptabase"
category: dokploy-docs
created: "2026-06-25T17:21:41.528Z"
---

Aptabase | Dokploy

# Aptabase

Copy as Markdown

Aptabase is a self-hosted web analytics platform that lets you track website traffic and user behavior.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  aptabase_db:
    image: postgres:15-alpine
    restart: always
    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: aptabase
      POSTGRES_PASSWORD: sTr0NGp4ssw0rd

    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U aptabase"]
      interval: 10s
      timeout: 5s
      retries: 5

  aptabase_events_db:
    image: clickhouse/clickhouse-server:23.8.16.16-alpine
    restart: always
    volumes:
      - events-db-data:/var/lib/clickhouse
    environment:
      CLICKHOUSE_USER: aptabase
      CLICKHOUSE_PASSWORD: sTr0NGp4ssw0rd
    ulimits:
      nofile:
        soft: 262144
        hard: 262144

    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost:8123 || exit 1"]
      interval: 10s
      timeout: 5s
      retries: 5

  aptabase:
    image: ghcr.io/aptabase/aptabase:main
    restart: always
    environment:
      BASE_URL: http://${APTABASE_HOST}
      AUTH_SECRET: ${AUTH_SECRET}
      DATABASE_URL: Server=aptabase_db;Port=5432;User Id=aptabase;Password=sTr0NGp4ssw0rd;Database=aptabase
      CLICKHOUSE_URL: Host=aptabase_events_db;Port=8123;Username=aptabase;Password=sTr0NGp4ssw0rd

volumes:
  db-data:
    driver: local
  events-db-data:
    driver: local
```

```
[variables]
main_domain = "${domain}"
auth_secret = "${base64:32}"

[config]
env = ["APTABASE_HOST=${main_domain}", "AUTH_SECRET=${auth_secret}"]
mounts = []

[[config.domains]]
serviceName = "aptabase"
port = 8_080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBhcHRhYmFzZV9kYjpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTUtYWxwaW5lXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGItZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTX1VTRVI6IGFwdGFiYXNlXG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogc1RyME5HcDRzc3cwcmRcblxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSBhcHRhYmFzZVwiXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcblxuICBhcHRhYmFzZV9ldmVudHNfZGI6XG4gICAgaW1hZ2U6IGNsaWNraG91c2UvY2xpY2tob3VzZS1zZXJ2ZXI6MjMuOC4xNi4xNi1hbHBpbmVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBldmVudHMtZGItZGF0YTovdmFyL2xpYi9jbGlja2hvdXNlXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBDTElDS0hPVVNFX1VTRVI6IGFwdGFiYXNlXG4gICAgICBDTElDS0hPVVNFX1BBU1NXT1JEOiBzVHIwTkdwNHNzdzByZFxuICAgIHVsaW1pdHM6XG4gICAgICBub2ZpbGU6XG4gICAgICAgIHNvZnQ6IDI2MjE0NFxuICAgICAgICBoYXJkOiAyNjIxNDRcblxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwiY3VybCAtZiBodHRwOi8vbG9jYWxob3N0OjgxMjMgfHwgZXhpdCAxXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuXG4gIGFwdGFiYXNlOlxuICAgIGltYWdlOiBnaGNyLmlvL2FwdGFiYXNlL2FwdGFiYXNlOm1haW5cbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEJBU0VfVVJMOiBodHRwOi8vJHtBUFRBQkFTRV9IT1NUfVxuICAgICAgQVVUSF9TRUNSRVQ6ICR7QVVUSF9TRUNSRVR9XG4gICAgICBEQVRBQkFTRV9VUkw6IFNlcnZlcj1hcHRhYmFzZV9kYjtQb3J0PTU0MzI7VXNlciBJZD1hcHRhYmFzZTtQYXNzd29yZD1zVHIwTkdwNHNzdzByZDtEYXRhYmFzZT1hcHRhYmFzZVxuICAgICAgQ0xJQ0tIT1VTRV9VUkw6IEhvc3Q9YXB0YWJhc2VfZXZlbnRzX2RiO1BvcnQ9ODEyMztVc2VybmFtZT1hcHRhYmFzZTtQYXNzd29yZD1zVHIwTkdwNHNzdzByZFxuXG52b2x1bWVzOlxuICBkYi1kYXRhOlxuICAgIGRyaXZlcjogbG9jYWxcbiAgZXZlbnRzLWRiLWRhdGE6XG4gICAgZHJpdmVyOiBsb2NhbFxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmF1dGhfc2VjcmV0ID0gXCIke2Jhc2U2NDozMn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1wiQVBUQUJBU0VfSE9TVD0ke21haW5fZG9tYWlufVwiLCBcIkFVVEhfU0VDUkVUPSR7YXV0aF9zZWNyZXR9XCJdXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhcHRhYmFzZVwiXG5wb3J0ID0gOF8wODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`analytics`,`self-hosted`

---

Version:`v1.0.0`

AppwriteAppwrite is an end-to-end platform for building Web, Mobile, Native, or Backend apps, packaged as a set of Docker microservices. It includes both a backend server and a fully integrated hosting solution for deploying static and server-side rendered frontends. Appwrite abstracts the complexity and repetitiveness required to build modern apps from scratch and allows you to build secure, full-stack applications faster. Using Appwrite, you can easily integrate your app with user authentication and multiple sign-in methods, a database for storing and querying users and team data, storage and file management, image manipulation, Cloud Functions, messaging, and more services.

ArangoDBArangoDB is a native multi-model database with flexible data models for documents, graphs, and key-values. Build high performance applications using a convenient SQL-like query language or JavaScript extensions.

### On this page

ConfigurationBase64LinksTags