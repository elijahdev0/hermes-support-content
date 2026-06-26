---
title: "KitchenOwl | Dokploy"
source: "https://docs.dokploy.com/docs/templates/kitchenowl"
category: dokploy-docs
created: "2026-06-25T17:21:50.891Z"
---

KitchenOwl | Dokploy

# KitchenOwl

Copy as Markdown

KitchenOwl is a self-hosted grocery list and recipe manager.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  web:
    image: tombursch/kitchenowl:v0.7.1
    restart: unless-stopped
    environment:
      - JWT_SECRET_KEY=${JWT_SECRET_KEY}
      - DB_DRIVER=postgresql
      - DB_HOST=db
      - DB_NAME=${DB_NAME}
      - DB_USER=${DB_USER}
      - DB_PASSWORD=${DB_PASSWORD}
    volumes:
      - kitchenowl_files:/data
    depends_on:
      - db

  db:
    image: postgres:17
    restart: unless-stopped
    environment:
      - POSTGRES_DB=${DB_NAME}
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - kitchenowl_db:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -d $${POSTGRES_DB} -U $${POSTGRES_USER}"]
      interval: 30s
      timeout: 60s
      retries: 5
      start_period: 80s

volumes:
  kitchenowl_files: {}
  kitchenowl_db: {}
```

```
[variables]
main_domain = "${domain}"
app_password = "${password:32}"
db_password = "${password:24}"
db_user = "kitchenowl"
db_name = "kitchenowl"

[config]

[[config.domains]]
serviceName = "web"
port = 8080
host = "${main_domain}"

[config.env]
JWT_SECRET_KEY = "${app_password}"
DB_DRIVER = "postgresql"
DB_HOST = "db"
DB_NAME = "${db_name}"
DB_USER = "${db_user}"
DB_PASSWORD = "${db_password}"

# Persist uploads/attachments
[[config.mounts]]
serviceName = "web"
volumeName = "kitchenowl_files"
mountPath = "/data"

# Persist Postgres data
[[config.mounts]]
serviceName = "db"
volumeName = "kitchenowl_db"
mountPath = "/var/lib/postgresql/data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHdlYjpcbiAgICBpbWFnZTogdG9tYnVyc2NoL2tpdGNoZW5vd2w6djAuNy4xXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gSldUX1NFQ1JFVF9LRVk9JHtKV1RfU0VDUkVUX0tFWX1cbiAgICAgIC0gREJfRFJJVkVSPXBvc3RncmVzcWxcbiAgICAgIC0gREJfSE9TVD1kYlxuICAgICAgLSBEQl9OQU1FPSR7REJfTkFNRX1cbiAgICAgIC0gREJfVVNFUj0ke0RCX1VTRVJ9XG4gICAgICAtIERCX1BBU1NXT1JEPSR7REJfUEFTU1dPUkR9XG4gICAgdm9sdW1lczpcbiAgICAgIC0ga2l0Y2hlbm93bF9maWxlczovZGF0YVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGRiXG5cbiAgZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE3XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfREI9JHtEQl9OQU1FfVxuICAgICAgLSBQT1NUR1JFU19VU0VSPSR7REJfVVNFUn1cbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkQ9JHtEQl9QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBraXRjaGVub3dsX2RiOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtZCAkJHtQT1NUR1JFU19EQn0gLVUgJCR7UE9TVEdSRVNfVVNFUn1cIl1cbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDYwc1xuICAgICAgcmV0cmllczogNVxuICAgICAgc3RhcnRfcGVyaW9kOiA4MHNcblxudm9sdW1lczpcbiAga2l0Y2hlbm93bF9maWxlczoge31cbiAga2l0Y2hlbm93bF9kYjoge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5hcHBfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjI0fVwiXG5kYl91c2VyID0gXCJraXRjaGVub3dsXCJcbmRiX25hbWUgPSBcImtpdGNoZW5vd2xcIlxuXG5bY29uZmlnXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ3ZWJcIlxucG9ydCA9IDgwODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5KV1RfU0VDUkVUX0tFWSA9IFwiJHthcHBfcGFzc3dvcmR9XCJcbkRCX0RSSVZFUiA9IFwicG9zdGdyZXNxbFwiXG5EQl9IT1NUID0gXCJkYlwiXG5EQl9OQU1FID0gXCIke2RiX25hbWV9XCJcbkRCX1VTRVIgPSBcIiR7ZGJfdXNlcn1cIlxuREJfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcblxuIyBQZXJzaXN0IHVwbG9hZHMvYXR0YWNobWVudHNcbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwid2ViXCJcbnZvbHVtZU5hbWUgPSBcImtpdGNoZW5vd2xfZmlsZXNcIlxubW91bnRQYXRoID0gXCIvZGF0YVwiXG5cbiMgUGVyc2lzdCBQb3N0Z3JlcyBkYXRhXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImRiXCJcbnZvbHVtZU5hbWUgPSBcImtpdGNoZW5vd2xfZGJcIlxubW91bnRQYXRoID0gXCIvdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcIlxuIgp9
```

## Links

`self-hosted`,`recipes`,`grocery`,`personal`

---

Version:`v0.7.1`

KimaiKimai is a web-based multi-user time-tracking application. Works great for everyone: freelancers, companies, organizations - everyone can track their times, generate reports, create invoices and do so much more.

Kokoro TTSDockerized FastAPI wrapper for the Kokoro-82M text-to-speech model with multi-language support and OpenAI-compatible endpoints.

### On this page

ConfigurationBase64LinksTags