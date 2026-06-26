---
title: "Etherpad | Dokploy"
source: "https://docs.dokploy.com/docs/templates/etherpad"
category: dokploy-docs
created: "2026-06-25T17:21:47.358Z"
---

Etherpad | Dokploy

# Etherpad

Copy as Markdown

Etherpad is a real-time collaborative text editor that allows multiple users to edit documents simultaneously.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  app:
    user: "0:0"
    image: etherpad/etherpad:latest
    tty: true
    stdin_open: true
    volumes:
      - ../files/plugins:/opt/etherpad-lite/src/plugin_packages
      - ../files/etherpad_var:/opt/etherpad-lite/var
    depends_on:
      - postgres
    environment:
      NODE_ENV: ${NODE_ENV}
      ADMIN_PASSWORD: ${ADMIN_PASSWORD}
      DB_CHARSET: ${DB_CHARSET}
      DB_HOST: ${DB_HOST}
      DB_NAME: ${DB_NAME}
      DB_PASS: ${DB_PASS}
      DB_PORT: ${DB_PORT}
      DB_TYPE: ${DB_TYPE}
      DB_USER: ${DB_USER}
      DEFAULT_PAD_TEXT: ${DEFAULT_PAD_TEXT}
      DISABLE_IP_LOGGING: ${DISABLE_IP_LOGGING}
      SOFFICE: ${SOFFICE}
      TRUST_PROXY: ${TRUST_PROXY}
    restart: always
    expose:
      - 9001
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_USER: ${POSTGRES_USER}
      PGDATA: /var/lib/postgresql/data/pgdata
    restart: always
    volumes:
      - ../files/postgres_data:/var/lib/postgresql/data/pgdata
```

```
[variables]
main_domain = "${domain}"
admin_password = "${password:32}"
postgres_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "app"
port = 9001
host = "${main_domain}"

[config.env]
NODE_ENV = "production"
ADMIN_PASSWORD = "${admin_password}"
DB_CHARSET = "utf8mb4"
DB_HOST = "postgres"
DB_NAME = "etherpad"
DB_PASS = "${postgres_password}"
DB_PORT = "5432"
DB_TYPE = "postgres"
DB_USER = "admin"
DEFAULT_PAD_TEXT = " "
DISABLE_IP_LOGGING = "false"
SOFFICE = "null"
TRUST_PROXY = "true"
POSTGRES_DB = "etherpad"
POSTGRES_PASSWORD = "${postgres_password}"
POSTGRES_USER = "admin"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhcHA6XG4gICAgdXNlcjogXCIwOjBcIlxuICAgIGltYWdlOiBldGhlcnBhZC9ldGhlcnBhZDpsYXRlc3RcbiAgICB0dHk6IHRydWVcbiAgICBzdGRpbl9vcGVuOiB0cnVlXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvcGx1Z2luczovb3B0L2V0aGVycGFkLWxpdGUvc3JjL3BsdWdpbl9wYWNrYWdlc1xuICAgICAgLSAuLi9maWxlcy9ldGhlcnBhZF92YXI6L29wdC9ldGhlcnBhZC1saXRlL3ZhclxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHBvc3RncmVzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBOT0RFX0VOVjogJHtOT0RFX0VOVn1cbiAgICAgIEFETUlOX1BBU1NXT1JEOiAke0FETUlOX1BBU1NXT1JEfVxuICAgICAgREJfQ0hBUlNFVDogJHtEQl9DSEFSU0VUfVxuICAgICAgREJfSE9TVDogJHtEQl9IT1NUfVxuICAgICAgREJfTkFNRTogJHtEQl9OQU1FfVxuICAgICAgREJfUEFTUzogJHtEQl9QQVNTfVxuICAgICAgREJfUE9SVDogJHtEQl9QT1JUfVxuICAgICAgREJfVFlQRTogJHtEQl9UWVBFfVxuICAgICAgREJfVVNFUjogJHtEQl9VU0VSfVxuICAgICAgREVGQVVMVF9QQURfVEVYVDogJHtERUZBVUxUX1BBRF9URVhUfVxuICAgICAgRElTQUJMRV9JUF9MT0dHSU5HOiAke0RJU0FCTEVfSVBfTE9HR0lOR31cbiAgICAgIFNPRkZJQ0U6ICR7U09GRklDRX1cbiAgICAgIFRSVVNUX1BST1hZOiAke1RSVVNUX1BST1hZfVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGV4cG9zZTpcbiAgICAgIC0gOTAwMVxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTUtYWxwaW5lXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19EQjogJHtQT1NUR1JFU19EQn1cbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgUE9TVEdSRVNfVVNFUjogJHtQT1NUR1JFU19VU0VSfVxuICAgICAgUEdEQVRBOiAvdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGEvcGdkYXRhXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvcG9zdGdyZXNfZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGEvcGdkYXRhXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYWRtaW5fcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbnBvc3RncmVzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhcHBcIlxucG9ydCA9IDkwMDFcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5OT0RFX0VOViA9IFwicHJvZHVjdGlvblwiXG5BRE1JTl9QQVNTV09SRCA9IFwiJHthZG1pbl9wYXNzd29yZH1cIlxuREJfQ0hBUlNFVCA9IFwidXRmOG1iNFwiXG5EQl9IT1NUID0gXCJwb3N0Z3Jlc1wiXG5EQl9OQU1FID0gXCJldGhlcnBhZFwiXG5EQl9QQVNTID0gXCIke3Bvc3RncmVzX3Bhc3N3b3JkfVwiXG5EQl9QT1JUID0gXCI1NDMyXCJcbkRCX1RZUEUgPSBcInBvc3RncmVzXCJcbkRCX1VTRVIgPSBcImFkbWluXCJcbkRFRkFVTFRfUEFEX1RFWFQgPSBcIiBcIlxuRElTQUJMRV9JUF9MT0dHSU5HID0gXCJmYWxzZVwiXG5TT0ZGSUNFID0gXCJudWxsXCJcblRSVVNUX1BST1hZID0gXCJ0cnVlXCJcblBPU1RHUkVTX0RCID0gXCJldGhlcnBhZFwiXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtwb3N0Z3Jlc19wYXNzd29yZH1cIlxuUE9TVEdSRVNfVVNFUiA9IFwiYWRtaW5cIlxuIgp9
```

## Links

`collaboration`,`text-editor`,`real-time`

---

Version:`latest`

ERPNext100% Open Source and highly customizable ERP software.

EvershopYour All-in-One open source ecommerce solution.

### On this page

ConfigurationBase64LinksTags