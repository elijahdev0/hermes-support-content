---
title: "Budget Board | Dokploy"
source: "https://docs.dokploy.com/docs/templates/budget-board"
category: dokploy-docs
created: "2026-06-25T17:21:42.677Z"
---

Budget Board | Dokploy

# Budget Board

Copy as Markdown

Self-hosted budgeting app with a web UI and a server backed by PostgreSQL.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  budget-board-server:
    restart: unless-stopped
    image: ghcr.io/teelur/budget-board/server:release

    environment:
      Logging__LogLevel__Default: Information
      CLIENT_URL: http://budget-board-client:6253
      POSTGRES_HOST: budget-board-db
      POSTGRES_DATABASE: budgetboard
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      AUTO_UPDATE_DB: true

    depends_on:
      budget-board-db:
        condition: service_healthy
  budget-board-client:
    restart: unless-stopped
    image: ghcr.io/teelur/budget-board/client:release
    environment:
      VITE_API_URL: http://budget-board-server
      PORT: 6253
    ports:
      - 6253
    depends_on:
      - budget-board-server
  budget-board-db:
    image: postgres:16
    restart: unless-stopped
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: budgetboard
    volumes:
      - "../files/db-data:/var/lib/postgresql/data"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d budgetboard"]
      interval: 5s
      timeout: 5s
      retries: 5
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "budget-board-client"
port = 6253
host = "${main_domain}"
path = "/"

[config.env]
POSTGRES_PASSWORD = "${postgres_password}"

[[config.mounts]]
source = "../files/db-data"
target = "/var/lib/postgresql/data"
type = "bind"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBidWRnZXQtYm9hcmQtc2VydmVyOlxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgaW1hZ2U6IGdoY3IuaW8vdGVlbHVyL2J1ZGdldC1ib2FyZC9zZXJ2ZXI6cmVsZWFzZVxuXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBMb2dnaW5nX19Mb2dMZXZlbF9fRGVmYXVsdDogSW5mb3JtYXRpb25cbiAgICAgIENMSUVOVF9VUkw6IGh0dHA6Ly9idWRnZXQtYm9hcmQtY2xpZW50OjYyNTNcbiAgICAgIFBPU1RHUkVTX0hPU1Q6IGJ1ZGdldC1ib2FyZC1kYlxuICAgICAgUE9TVEdSRVNfREFUQUJBU0U6IGJ1ZGdldGJvYXJkXG4gICAgICBQT1NUR1JFU19VU0VSOiBwb3N0Z3Jlc1xuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBBVVRPX1VQREFURV9EQjogdHJ1ZVxuXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGJ1ZGdldC1ib2FyZC1kYjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgYnVkZ2V0LWJvYXJkLWNsaWVudDpcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGltYWdlOiBnaGNyLmlvL3RlZWx1ci9idWRnZXQtYm9hcmQvY2xpZW50OnJlbGVhc2VcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFZJVEVfQVBJX1VSTDogaHR0cDovL2J1ZGdldC1ib2FyZC1zZXJ2ZXJcbiAgICAgIFBPUlQ6IDYyNTNcbiAgICBwb3J0czpcbiAgICAgIC0gNjI1M1xuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGJ1ZGdldC1ib2FyZC1zZXJ2ZXJcbiAgYnVkZ2V0LWJvYXJkLWRiOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNlxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19VU0VSOiBwb3N0Z3Jlc1xuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19EQjogYnVkZ2V0Ym9hcmRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBcIi4uL2ZpbGVzL2RiLWRhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXCJcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgcG9zdGdyZXMgLWQgYnVkZ2V0Ym9hcmRcIl1cbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIiAgXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJidWRnZXQtYm9hcmQtY2xpZW50XCIgXG5wb3J0ID0gNjI1MyAgXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiICBcbnBhdGggPSBcIi9cIlxuXG5cbltjb25maWcuZW52XVxuUE9TVEdSRVNfUEFTU1dPUkQgPSBcIiR7cG9zdGdyZXNfcGFzc3dvcmR9XCIgXG5cblxuW1tjb25maWcubW91bnRzXV1cbnNvdXJjZSA9IFwiLi4vZmlsZXMvZGItZGF0YVwiICBcbnRhcmdldCA9IFwiL3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXCIgIFxudHlwZSA9IFwiYmluZFwiICAiCn0=
```

## Links

`finance`,`postgres`,`self-hosted`,`docker`,`compose`

---

Version:`release`

BrowserlessBrowserless allows remote clients to connect and execute headless work, all inside of docker. It supports the standard, unforked Puppeteer and Playwright libraries, as well offering REST-based APIs for common actions like data collection, PDF generation and more.

BudibaseBudibase is an open-source low-code platform that saves engineers 100s of hours building forms, portals, and approval apps, securely.

### On this page

ConfigurationBase64LinksTags