---
title: "Browserless | Dokploy"
source: "https://docs.dokploy.com/docs/templates/browserless"
category: dokploy-docs
created: "2026-06-25T17:21:42.677Z"
---

Browserless | Dokploy

# Browserless

Copy as Markdown

Browserless allows remote clients to connect and execute headless work, all inside of docker. It supports the standard, unforked Puppeteer and Playwright libraries, as well offering REST-based APIs for common actions like data collection, PDF generation and more.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  browserless:
    image: ghcr.io/browserless/chromium:latest
    environment:
      TOKEN: ${BROWSERLESS_TOKEN}
    expose:
      - 3000
    healthcheck:
      test:
        - CMD
        - curl
        - '-f'
        - 'http://127.0.0.1:3000/docs'
      interval: 2s
      timeout: 10s
      retries: 15
```

```
[variables]
main_domain = "${domain}"
browserless_token = "${password:16}"

[config]
env = [
  "BROWSERLESS_HOST=${main_domain}",
  "BROWSERLESS_TOKEN=${browserless_token}",
]
mounts = []

[[config.domains]]
serviceName = "browserless"
port = 3000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBicm93c2VybGVzczpcbiAgICBpbWFnZTogZ2hjci5pby9icm93c2VybGVzcy9jaHJvbWl1bTpsYXRlc3RcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFRPS0VOOiAke0JST1dTRVJMRVNTX1RPS0VOfVxuICAgIGV4cG9zZTpcbiAgICAgIC0gMzAwMFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgLSBDTURcbiAgICAgICAgLSBjdXJsXG4gICAgICAgIC0gJy1mJ1xuICAgICAgICAtICdodHRwOi8vMTI3LjAuMC4xOjMwMDAvZG9jcydcbiAgICAgIGludGVydmFsOiAyc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAxNVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmJyb3dzZXJsZXNzX3Rva2VuID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiQlJPV1NFUkxFU1NfSE9TVD0ke21haW5fZG9tYWlufVwiLFxuICBcIkJST1dTRVJMRVNTX1RPS0VOPSR7YnJvd3Nlcmxlc3NfdG9rZW59XCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJicm93c2VybGVzc1wiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`browser`,`automation`

---

Version:`2.23.0`

BotpressBotpress is a platform for building conversational AI agents. It provides a simple and effective solution for building conversational AI agents from anywhere.

Budget BoardSelf-hosted budgeting app with a web UI and a server backed by PostgreSQL.

### On this page

ConfigurationBase64LinksTags