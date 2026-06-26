---
title: "Logto | Dokploy"
source: "https://docs.dokploy.com/docs/templates/logto"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

Logto | Dokploy

# Logto

Copy as Markdown

Logto is an open-source Identity and Access Management (IAM) platform designed to streamline Customer Identity and Access Management (CIAM) and Workforce Identity Management.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  app:
    depends_on:
      postgres:
        condition: service_healthy
    image: ghcr.io/logto-io/logto:1.27.0
    entrypoint: ["sh", "-c", "npm run cli db seed -- --swe && npm start"]
    ports:
      - 3001
      - 3002

    environment:
      TRUST_PROXY_HEADER: 1
      DB_URL: postgres://logto:${LOGTO_POSTGRES_PASSWORD}@postgres:5432/logto
      ENDPOINT: ${LOGTO_ENDPOINT}
      ADMIN_ENDPOINT: ${LOGTO_ADMIN_ENDPOINT}
    volumes:
      - logto-connectors:/etc/logto/packages/core/connectors
  postgres:
    image: postgres:17-alpine
    user: postgres

    environment:
      POSTGRES_USER: logto
      POSTGRES_PASSWORD: ${LOGTO_POSTGRES_PASSWORD}
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  logto-connectors:
  postgres-data:
```

```
[variables]
main_domain = "${domain}"
admin_domain = "${domain}"
postgres_password = "${password}"

[config]
mounts = []

[[config.domains]]
serviceName = "app"
port = 3_001
host = "${main_domain}"

[[config.domains]]
serviceName = "app"
port = 3_002
host = "${admin_domain}"

[config.env]
LOGTO_ENDPOINT = "http://${admin_domain}"
LOGTO_ADMIN_ENDPOINT = "http://${admin_domain}"
LOGTO_POSTGRES_PASSWORD = "${postgres_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBhcHA6XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHBvc3RncmVzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGltYWdlOiBnaGNyLmlvL2xvZ3RvLWlvL2xvZ3RvOjEuMjcuMFxuICAgIGVudHJ5cG9pbnQ6IFtcInNoXCIsIFwiLWNcIiwgXCJucG0gcnVuIGNsaSBkYiBzZWVkIC0tIC0tc3dlICYmIG5wbSBzdGFydFwiXVxuICAgIHBvcnRzOlxuICAgICAgLSAzMDAxXG4gICAgICAtIDMwMDJcblxuICAgIGVudmlyb25tZW50OlxuICAgICAgVFJVU1RfUFJPWFlfSEVBREVSOiAxXG4gICAgICBEQl9VUkw6IHBvc3RncmVzOi8vbG9ndG86JHtMT0dUT19QT1NUR1JFU19QQVNTV09SRH1AcG9zdGdyZXM6NTQzMi9sb2d0b1xuICAgICAgRU5EUE9JTlQ6ICR7TE9HVE9fRU5EUE9JTlR9XG4gICAgICBBRE1JTl9FTkRQT0lOVDogJHtMT0dUT19BRE1JTl9FTkRQT0lOVH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBsb2d0by1jb25uZWN0b3JzOi9ldGMvbG9ndG8vcGFja2FnZXMvY29yZS9jb25uZWN0b3JzXG4gIHBvc3RncmVzOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNy1hbHBpbmVcbiAgICB1c2VyOiBwb3N0Z3Jlc1xuXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19VU0VSOiBsb2d0b1xuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7TE9HVE9fUE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gcG9zdGdyZXMtZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHlcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG5cblxudm9sdW1lczpcbiAgbG9ndG8tY29ubmVjdG9yczpcbiAgcG9zdGdyZXMtZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5hZG1pbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZH1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYXBwXCJcbnBvcnQgPSAzXzAwMVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhcHBcIlxucG9ydCA9IDNfMDAyXG5ob3N0ID0gXCIke2FkbWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkxPR1RPX0VORFBPSU5UID0gXCJodHRwOi8vJHthZG1pbl9kb21haW59XCJcbkxPR1RPX0FETUlOX0VORFBPSU5UID0gXCJodHRwOi8vJHthZG1pbl9kb21haW59XCJcbkxPR1RPX1BPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bvc3RncmVzX3Bhc3N3b3JkfVwiXG4iCn0=
```

## Links

`identity`,`auth`

---

Version:`1.27.0`

LodestoneA free, open source server hosting tool for Minecraft and other multiplayers games.

LowcoderRapid business App Builder for Everyone

### On this page

ConfigurationBase64LinksTags