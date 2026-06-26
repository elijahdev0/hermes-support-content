---
title: "Docmost | Dokploy"
source: "https://docs.dokploy.com/docs/templates/docmost"
category: dokploy-docs
created: "2026-06-25T17:21:46.245Z"
---

Docmost | Dokploy

# Docmost

Copy as Markdown

Docmost, is an open-source collaborative wiki and documentation software.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  docmost:
    image: docmost/docmost:0.4.1
    depends_on:
      - db
      - redis
    environment:
      - APP_URL
      - APP_SECRET
      - DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}?schema=public
      - REDIS_URL=redis://redis:6379
    restart: unless-stopped

    volumes:
      - docmost:/app/data/storage

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_DB
      - POSTGRES_USER
      - POSTGRES_PASSWORD
    restart: unless-stopped

    volumes:
      - db_docmost_data:/var/lib/postgresql/data

  redis:
    image: redis:7.2-alpine
    restart: unless-stopped

    volumes:
      - redis_docmost_data:/data

volumes:
  docmost:
  db_docmost_data:
  redis_docmost_data:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password}"
app_secret = "${password}"

[config]
env = [
  "POSTGRES_DB=docmost",
  "POSTGRES_USER=docmost",
  "POSTGRES_PASSWORD=${postgres_password}",
  "APP_URL=http://${main_domain}:3000",
  "APP_SECRET=${app_secret}",
]
mounts = []

[[config.domains]]
serviceName = "docmost"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBkb2Ntb3N0OlxuICAgIGltYWdlOiBkb2Ntb3N0L2RvY21vc3Q6MC40LjFcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBkYlxuICAgICAgLSByZWRpc1xuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBBUFBfVVJMXG4gICAgICAtIEFQUF9TRUNSRVRcbiAgICAgIC0gREFUQUJBU0VfVVJMPXBvc3RncmVzcWw6Ly8ke1BPU1RHUkVTX1VTRVJ9OiR7UE9TVEdSRVNfUEFTU1dPUkR9QGRiOjU0MzIvJHtQT1NUR1JFU19EQn0/c2NoZW1hPXB1YmxpY1xuICAgICAgLSBSRURJU19VUkw9cmVkaXM6Ly9yZWRpczo2Mzc5XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRvY21vc3Q6L2FwcC9kYXRhL3N0b3JhZ2VcblxuICBkYjpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTYtYWxwaW5lXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX0RCXG4gICAgICAtIFBPU1RHUkVTX1VTRVJcbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkRcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGJfZG9jbW9zdF9kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuXG4gIHJlZGlzOlxuICAgIGltYWdlOiByZWRpczo3LjItYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIHJlZGlzX2RvY21vc3RfZGF0YTovZGF0YVxuXG52b2x1bWVzOlxuICBkb2Ntb3N0OlxuICBkYl9kb2Ntb3N0X2RhdGE6XG4gIHJlZGlzX2RvY21vc3RfZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmR9XCJcbmFwcF9zZWNyZXQgPSBcIiR7cGFzc3dvcmR9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJQT1NUR1JFU19EQj1kb2Ntb3N0XCIsXG4gIFwiUE9TVEdSRVNfVVNFUj1kb2Ntb3N0XCIsXG4gIFwiUE9TVEdSRVNfUEFTU1dPUkQ9JHtwb3N0Z3Jlc19wYXNzd29yZH1cIixcbiAgXCJBUFBfVVJMPWh0dHA6Ly8ke21haW5fZG9tYWlufTozMDAwXCIsXG4gIFwiQVBQX1NFQ1JFVD0ke2FwcF9zZWNyZXR9XCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJkb2Ntb3N0XCJcbnBvcnQgPSAzXzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`self-hosted`,`open-source`,`manager`

---

Version:`0.4.1`

Docling ServeRunning Docling as an API service for document processing and conversion with AI-powered capabilities.

DocumensoDocumenso is the open source alternative to DocuSign for signing documents digitally

### On this page

ConfigurationBase64LinksTags