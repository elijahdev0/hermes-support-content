---
title: "Evershop | Dokploy"
source: "https://docs.dokploy.com/docs/templates/evershop"
category: dokploy-docs
created: "2026-06-25T17:21:47.358Z"
---

Evershop | Dokploy

# Evershop

Copy as Markdown

Your All-in-One open source ecommerce solution.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  evershop-app:
    image: evershop/evershop:latest
    restart: always
    environment:
      DB_HOST: database
      DB_PORT: ${DB_PORT}
      DB_PASSWORD: ${DB_PASSWORD}
      DB_USER: ${DB_USER}
      DB_NAME: ${DB_NAME}
    depends_on:
      - database
    ports:
      - 3000

  database:
    image: postgres:16
    restart: unless-stopped
    volumes:
      - postgres-data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_DB: ${DB_NAME}
    ports:
      - ${DB_PORT}

volumes:
  postgres-data:
```

```
[variables]
main_domain = "${domain}"
db_user = "postgres"
db_password = "postgres"
db_name = "evershop"
db_port = "5432"

[config]

[[config.domains]]
serviceName = "evershop-app"
port = 3_000
host = "${main_domain}"

[config.env]
DB_USER = "${db_user}"
DB_PASSWORD = "${db_password}"
DB_NAME = "${db_name}"
DB_PORT = "${db_port}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBldmVyc2hvcC1hcHA6XG4gICAgaW1hZ2U6IGV2ZXJzaG9wL2V2ZXJzaG9wOmxhdGVzdFxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGVudmlyb25tZW50OlxuICAgICAgREJfSE9TVDogZGF0YWJhc2VcbiAgICAgIERCX1BPUlQ6ICR7REJfUE9SVH1cbiAgICAgIERCX1BBU1NXT1JEOiAke0RCX1BBU1NXT1JEfVxuICAgICAgREJfVVNFUjogJHtEQl9VU0VSfVxuICAgICAgREJfTkFNRTogJHtEQl9OQU1FfVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGRhdGFiYXNlXG4gICAgcG9ydHM6XG4gICAgICAtIDMwMDBcbiAgXG4gIGRhdGFiYXNlOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNlxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcG9zdGdyZXMtZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke0RCX1BBU1NXT1JEfVxuICAgICAgUE9TVEdSRVNfVVNFUjogJHtEQl9VU0VSfVxuICAgICAgUE9TVEdSRVNfREI6ICR7REJfTkFNRX1cbiAgICBwb3J0czpcbiAgICAgIC0gJHtEQl9QT1JUfVxuXG52b2x1bWVzOlxuICBwb3N0Z3Jlcy1kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3VzZXIgPSBcInBvc3RncmVzXCJcbmRiX3Bhc3N3b3JkID0gXCJwb3N0Z3Jlc1wiXG5kYl9uYW1lID0gXCJldmVyc2hvcFwiXG5kYl9wb3J0ID0gXCI1NDMyXCJcblxuW2NvbmZpZ11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZXZlcnNob3AtYXBwXCJcbnBvcnQgPSAzXzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkRCX1VTRVIgPSBcIiR7ZGJfdXNlcn1cIlxuREJfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcbkRCX05BTUUgPSBcIiR7ZGJfbmFtZX1cIlxuREJfUE9SVCA9IFwiJHtkYl9wb3J0fVwiXG4iCn0=
```

## Links

`E-Commerce`,`shopping`

---

Version:`latest`

EtherpadEtherpad is a real-time collaborative text editor that allows multiple users to edit documents simultaneously.

Evolution APIEvolution API is a robust platform dedicated to empowering small businesses with limited resources, going beyond a simple messaging solution via WhatsApp.

### On this page

ConfigurationBase64LinksTags