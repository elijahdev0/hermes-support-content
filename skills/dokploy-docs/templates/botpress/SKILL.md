---
title: "Botpress | Dokploy"
source: "https://docs.dokploy.com/docs/templates/botpress"
category: dokploy-docs
created: "2026-06-25T17:21:42.677Z"
---

Botpress | Dokploy

# Botpress

Copy as Markdown

Botpress is a platform for building conversational AI agents. It provides a simple and effective solution for building conversational AI agents from anywhere.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  botpress:
    image: botpress/server:12.31.9
    restart: unless-stopped
    ports:
      - 81
    environment:
      - BP_HOST=0.0.0.0
      - NODE_ENV=production
      - PG_HOST=botpress-db
      - PG_PORT=5432
      - PG_USER=postgres
      - PG_PASSWORD=${DB_PASSWORD}
      - PG_SSL=false
      - PORT=80
    volumes:
      - data:/botpress/data
    depends_on:
      - botpress-db

  botpress-db:
    image: postgres:15-alpine
    restart: unless-stopped
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=botpress
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  data: {}
  db_data: {}
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:16}"

[config]
[[config.domains]]
serviceName = "botpress"
port = 81
host = "${main_domain}"

[config.env]
DB_PASSWORD = "${db_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBib3RwcmVzczpcbiAgICBpbWFnZTogYm90cHJlc3Mvc2VydmVyOjEyLjMxLjlcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSA4MVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBCUF9IT1NUPTAuMC4wLjBcbiAgICAgIC0gTk9ERV9FTlY9cHJvZHVjdGlvblxuICAgICAgLSBQR19IT1NUPWJvdHByZXNzLWRiXG4gICAgICAtIFBHX1BPUlQ9NTQzMlxuICAgICAgLSBQR19VU0VSPXBvc3RncmVzXG4gICAgICAtIFBHX1BBU1NXT1JEPSR7REJfUEFTU1dPUkR9XG4gICAgICAtIFBHX1NTTD1mYWxzZVxuICAgICAgLSBQT1JUPTgwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGF0YTovYm90cHJlc3MvZGF0YVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGJvdHByZXNzLWRiXG5cbiAgYm90cHJlc3MtZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE1LWFscGluZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX1VTRVI9cG9zdGdyZXNcbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkQ9JHtEQl9QQVNTV09SRH1cbiAgICAgIC0gUE9TVEdSRVNfREI9Ym90cHJlc3NcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYl9kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuXG52b2x1bWVzOlxuICBkYXRhOiB7fVxuICBkYl9kYXRhOiB7fSAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImJvdHByZXNzXCJcbnBvcnQgPSA4MVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkRCX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiICIKfQ==
```

## Links

`ai`,`self-hosted`

---

Version:`latest`

BorgitoryA web interface for managing BorgBackup archives. Allows browsing, mounting (via FUSE), and handling backup repositories.

BrowserlessBrowserless allows remote clients to connect and execute headless work, all inside of docker. It supports the standard, unforked Puppeteer and Playwright libraries, as well offering REST-based APIs for common actions like data collection, PDF generation and more.

### On this page

ConfigurationBase64LinksTags