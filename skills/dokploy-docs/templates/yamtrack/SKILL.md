---
title: "Yamtrack | Dokploy"
source: "https://docs.dokploy.com/docs/templates/yamtrack"
category: dokploy-docs
created: "2026-06-25T17:22:02.523Z"
---

Yamtrack | Dokploy

# Yamtrack

Copy as Markdown

Yamtrack is a self-hosted anime and manga tracker with Redis backend support.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  yamtrack:
    image: ghcr.io/fuzzygrim/yamtrack
    restart: unless-stopped
    depends_on:
      - redis
    environment:
      - TZ=Europe/Berlin
      - SECRET=${SECRET}
      - REDIS_URL=redis://redis:6379
    volumes:
      - yamtrack-db:/yamtrack/db
    expose:
      - 8000

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data

volumes:
  yamtrack-db: {}
  redis_data: {}
```

```
[variables]
main_domain = "${domain}"
SECRET = "${password:64}"

[config]
[[config.domains]]
serviceName = "yamtrack"
port = 8000
host = "${main_domain}"

[config.env]
SECRET = "${SECRET}"
TZ = "Europe/Berlin"
REDIS_URL = "redis://redis:6379"

[[config.mounts]]
serviceName = "yamtrack"
volumeName = "yamtrack-db"
mountPath = "/yamtrack/db"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHlhbXRyYWNrOlxuICAgIGltYWdlOiBnaGNyLmlvL2Z1enp5Z3JpbS95YW10cmFja1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcmVkaXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gVFo9RXVyb3BlL0JlcmxpblxuICAgICAgLSBTRUNSRVQ9JHtTRUNSRVR9XG4gICAgICAtIFJFRElTX1VSTD1yZWRpczovL3JlZGlzOjYzNzlcbiAgICB2b2x1bWVzOlxuICAgICAgLSB5YW10cmFjay1kYjoveWFtdHJhY2svZGJcbiAgICBleHBvc2U6XG4gICAgICAtIDgwMDBcblxuICByZWRpczpcbiAgICBpbWFnZTogcmVkaXM6Ny1hbHBpbmVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHJlZGlzX2RhdGE6L2RhdGFcblxudm9sdW1lczpcbiAgeWFtdHJhY2stZGI6IHt9XG4gIHJlZGlzX2RhdGE6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuU0VDUkVUID0gXCIke3Bhc3N3b3JkOjY0fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ5YW10cmFja1wiXG5wb3J0ID0gODAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblNFQ1JFVCA9IFwiJHtTRUNSRVR9XCJcblRaID0gXCJFdXJvcGUvQmVybGluXCJcblJFRElTX1VSTCA9IFwicmVkaXM6Ly9yZWRpczo2Mzc5XCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJ5YW10cmFja1wiXG52b2x1bWVOYW1lID0gXCJ5YW10cmFjay1kYlwiXG5tb3VudFBhdGggPSBcIi95YW10cmFjay9kYlwiXG4iCn0=
```

## Links

`media`,`anime`,`manga`,`tracker`,`redis`

---

Version:`latest`

XSSHunterXSSHunter is an open-source platform designed to identify and exploit blind Cross-Site Scripting (XSS) vulnerabilities. It provides security researchers, bug bounty hunters, and penetration testers with a comprehensive toolkit for detecting XSS flaws that are otherwise difficult to discover through traditional testing methods.

YOURLSYOURLS (Your Own URL Shortener) is a set of PHP scripts that will allow you to run your own URL shortening service (a la TinyURL or Bitly).

### On this page

ConfigurationBase64LinksTags