---
title: "Slash | Dokploy"
source: "https://docs.dokploy.com/docs/templates/slash"
category: dokploy-docs
created: "2026-06-25T17:21:59.114Z"
---

Slash | Dokploy

# Slash

Copy as Markdown

Slash is a modern, self-hosted bookmarking service and link shortener that helps you organize and share your favorite links.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  slash-app:
    image: yourselfhosted/slash:latest

    volumes:
      - slash-app-data:/var/opt/slash
    environment:
      - SLASH_DRIVER=postgres
      - SLASH_DSN=postgresql://${DB_USER}:${DB_PASSWORD}@slash-postgres:5432/${DB_NAME}?sslmode=disable
    depends_on:
      slash-postgres:
        condition: service_healthy
    restart: unless-stopped

  slash-postgres:
    image: postgres:16-alpine

    volumes:
      - slash-postgres-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=${DB_NAME}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d ${DB_NAME}"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

volumes:
  slash-app-data:
  slash-postgres-data:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password}"
db_user = "slash"
db_name = "slash"

[config]
mounts = []

[[config.domains]]
serviceName = "slash-app"
port = 5_231
host = "${main_domain}"

[config.env]
DB_USER = "${db_user}"
DB_PASSWORD = "${db_password}"
DB_NAME = "${db_name}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHNsYXNoLWFwcDpcbiAgICBpbWFnZTogeW91cnNlbGZob3N0ZWQvc2xhc2g6bGF0ZXN0XG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSBzbGFzaC1hcHAtZGF0YTovdmFyL29wdC9zbGFzaFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBTTEFTSF9EUklWRVI9cG9zdGdyZXNcbiAgICAgIC0gU0xBU0hfRFNOPXBvc3RncmVzcWw6Ly8ke0RCX1VTRVJ9OiR7REJfUEFTU1dPUkR9QHNsYXNoLXBvc3RncmVzOjU0MzIvJHtEQl9OQU1FfT9zc2xtb2RlPWRpc2FibGVcbiAgICBkZXBlbmRzX29uOlxuICAgICAgc2xhc2gtcG9zdGdyZXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxuICBzbGFzaC1wb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTYtYWxwaW5lXG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSBzbGFzaC1wb3N0Z3Jlcy1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19VU0VSPSR7REJfVVNFUn1cbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkQ9JHtEQl9QQVNTV09SRH1cbiAgICAgIC0gUE9TVEdSRVNfREI9JHtEQl9OQU1FfVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSAke0RCX1VTRVJ9IC1kICR7REJfTkFNRX1cIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxudm9sdW1lczpcbiAgc2xhc2gtYXBwLWRhdGE6XG4gIHNsYXNoLXBvc3RncmVzLWRhdGE6ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5kYl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZH1cIlxuZGJfdXNlciA9IFwic2xhc2hcIlxuZGJfbmFtZSA9IFwic2xhc2hcIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwic2xhc2gtYXBwXCJcbnBvcnQgPSA1XzIzMVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkRCX1VTRVIgPSBcIiR7ZGJfdXNlcn1cIlxuREJfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcbkRCX05BTUUgPSBcIiR7ZGJfbmFtZX1cIlxuIgp9
```

## Links

`bookmarks`,`link-shortener`,`self-hosted`

---

Version:`latest`

SilverBulletSilverBullet is a personal knowledge base and collaborative note-taking platform.

SnappSnapp is a self-hosted screenshot sharing service with user management and authentication.

### On this page

ConfigurationBase64LinksTags