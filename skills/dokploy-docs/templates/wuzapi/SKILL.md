---
title: "WuzAPI | Dokploy"
source: "https://docs.dokploy.com/docs/templates/wuzapi"
category: dokploy-docs
created: "2026-06-25T17:22:01.421Z"
---

WuzAPI | Dokploy

# WuzAPI

Copy as Markdown

A RESTful API service for WhatsApp with multiple device support and concurrent sessions.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  wuzapi-server:
    image: asternic/wuzapi:sha-30c1805
    restart: unless-stopped
    expose:
      - 8080
    environment:
      - WUZAPI_ADMIN_TOKEN=${WUZAPI_ADMIN_TOKEN}
      - WUZAPI_GLOBAL_ENCRYPTION_KEY=${WUZAPI_GLOBAL_ENCRYPTION_KEY}
      - DB_USER=${DB_USER:-wuzapi}
      - DB_PASSWORD=${DB_PASSWORD:-wuzapi}
      - DB_NAME=${DB_NAME:-wuzapi}
      - DB_HOST=db
      - DB_PORT=5432
      - TZ=${TZ:-UTC}
    depends_on:
      - db

  db:
    image: postgres:16-alpine
    restart: always
    environment:
      POSTGRES_USER: ${DB_USER:-wuzapi}
      POSTGRES_PASSWORD: ${DB_PASSWORD:-wuzapi}
      POSTGRES_DB: ${DB_NAME:-wuzapi}
    volumes:
      - db_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $${DB_USER:-wuzapi}"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  db_data:
```

```
[variables]
main_domain = "${domain}"
admin_token = "${password:32}"
encryption_key = "${password:32}"
db_user = "wuzapi"
db_password = "${password:32}"
db_name = "wuzapi"

[config]
[[config.domains]]
serviceName = "wuzapi-server"
port = 8080
host = "${main_domain}"

[config.env]
WUZAPI_ADMIN_TOKEN = "${admin_token}"
WUZAPI_GLOBAL_ENCRYPTION_KEY = "${encryption_key}"
DB_USER = "${db_user}"
DB_PASSWORD = "${db_password}"
DB_NAME = "${db_name}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICB3dXphcGktc2VydmVyOlxuICAgIGltYWdlOiBhc3Rlcm5pYy93dXphcGk6c2hhLTMwYzE4MDVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGV4cG9zZTpcbiAgICAgIC0gODA4MFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBXVVpBUElfQURNSU5fVE9LRU49JHtXVVpBUElfQURNSU5fVE9LRU59XG4gICAgICAtIFdVWkFQSV9HTE9CQUxfRU5DUllQVElPTl9LRVk9JHtXVVpBUElfR0xPQkFMX0VOQ1JZUFRJT05fS0VZfVxuICAgICAgLSBEQl9VU0VSPSR7REJfVVNFUjotd3V6YXBpfVxuICAgICAgLSBEQl9QQVNTV09SRD0ke0RCX1BBU1NXT1JEOi13dXphcGl9XG4gICAgICAtIERCX05BTUU9JHtEQl9OQU1FOi13dXphcGl9XG4gICAgICAtIERCX0hPU1Q9ZGJcbiAgICAgIC0gREJfUE9SVD01NDMyXG4gICAgICAtIFRaPSR7VFo6LVVUQ31cbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBkYlxuXG4gIGRiOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNi1hbHBpbmVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTX1VTRVI6ICR7REJfVVNFUjotd3V6YXBpfVxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7REJfUEFTU1dPUkQ6LXd1emFwaX1cbiAgICAgIFBPU1RHUkVTX0RCOiAke0RCX05BTUU6LXd1emFwaX1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYl9kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSAkJHtEQl9VU0VSOi13dXphcGl9XCJdXG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG5cbnZvbHVtZXM6XG4gIGRiX2RhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYWRtaW5fdG9rZW4gPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmVuY3J5cHRpb25fa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5kYl91c2VyID0gXCJ3dXphcGlcIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmRiX25hbWUgPSBcInd1emFwaVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ3dXphcGktc2VydmVyXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuV1VaQVBJX0FETUlOX1RPS0VOID0gXCIke2FkbWluX3Rva2VufVwiXG5XVVpBUElfR0xPQkFMX0VOQ1JZUFRJT05fS0VZID0gXCIke2VuY3J5cHRpb25fa2V5fVwiXG5EQl9VU0VSID0gXCIke2RiX3VzZXJ9XCJcbkRCX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiXG5EQl9OQU1FID0gXCIke2RiX25hbWV9XCJcbiIKfQ==
```

## Links

`api`,`whatsapp`,`messaging`,`automation`

---

Version:`v1.0.0`

WordpressWordpress is a free and open source content management system (CMS) for publishing and managing websites.

XSSHunterXSSHunter is an open-source platform designed to identify and exploit blind Cross-Site Scripting (XSS) vulnerabilities. It provides security researchers, bug bounty hunters, and penetration testers with a comprehensive toolkit for detecting XSS flaws that are otherwise difficult to discover through traditional testing methods.

### On this page

ConfigurationBase64LinksTags