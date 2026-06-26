---
title: "Ryot | Dokploy"
source: "https://docs.dokploy.com/docs/templates/ryot"
category: dokploy-docs
created: "2026-06-25T17:21:59.113Z"
---

Ryot | Dokploy

# Ryot

Copy as Markdown

A self-hosted platform for tracking various media types including movies, TV shows, video games, books, audiobooks, and more.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.7'

services:
  ryot-app:
    image: ignisda/ryot:v7.10

    environment:
      - DATABASE_URL=postgres://postgres:${POSTGRES_PASSWORD}@ryot-db:5432/postgres
      - SERVER_ADMIN_ACCESS_TOKEN=${ADMIN_ACCESS_TOKEN}
      - TZ=UTC
      # Optional: Uncomment and set your pro key if you have one
      # - SERVER_PRO_KEY=${SERVER_PRO_KEY}
    depends_on:
      ryot-db:
        condition: service_healthy
    restart: always
    pull_policy: always

  ryot-db:
    image: postgres:16-alpine

    volumes:
      - ryot-postgres-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_USER=postgres
      - POSTGRES_DB=postgres
      - TZ=UTC
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

volumes:
  ryot-postgres-data:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password}"
admin_access_token = "${base64:32}"

[config]
mounts = []

[[config.domains]]
serviceName = "ryot-app"
port = 8_000
host = "${main_domain}"

[config.env]
POSTGRES_PASSWORD = "${postgres_password}"
ADMIN_ACCESS_TOKEN = "${admin_access_token}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjcnXG5cbnNlcnZpY2VzOlxuICByeW90LWFwcDpcbiAgICBpbWFnZTogaWduaXNkYS9yeW90OnY3LjEwXG5cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gREFUQUJBU0VfVVJMPXBvc3RncmVzOi8vcG9zdGdyZXM6JHtQT1NUR1JFU19QQVNTV09SRH1AcnlvdC1kYjo1NDMyL3Bvc3RncmVzXG4gICAgICAtIFNFUlZFUl9BRE1JTl9BQ0NFU1NfVE9LRU49JHtBRE1JTl9BQ0NFU1NfVE9LRU59XG4gICAgICAtIFRaPVVUQ1xuICAgICAgIyBPcHRpb25hbDogVW5jb21tZW50IGFuZCBzZXQgeW91ciBwcm8ga2V5IGlmIHlvdSBoYXZlIG9uZVxuICAgICAgIyAtIFNFUlZFUl9QUk9fS0VZPSR7U0VSVkVSX1BST19LRVl9XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHJ5b3QtZGI6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgcHVsbF9wb2xpY3k6IGFsd2F5c1xuXG4gIHJ5b3QtZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE2LWFscGluZVxuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcnlvdC1wb3N0Z3Jlcy1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgLSBQT1NUR1JFU19VU0VSPXBvc3RncmVzXG4gICAgICAtIFBPU1RHUkVTX0RCPXBvc3RncmVzXG4gICAgICAtIFRaPVVUQ1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSBwb3N0Z3Jlc1wiXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG52b2x1bWVzOlxuICByeW90LXBvc3RncmVzLWRhdGE6ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZH1cIlxuYWRtaW5fYWNjZXNzX3Rva2VuID0gXCIke2Jhc2U2NDozMn1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicnlvdC1hcHBcIlxucG9ydCA9IDhfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuUE9TVEdSRVNfUEFTU1dPUkQgPSBcIiR7cG9zdGdyZXNfcGFzc3dvcmR9XCJcbkFETUlOX0FDQ0VTU19UT0tFTiA9IFwiJHthZG1pbl9hY2Nlc3NfdG9rZW59XCJcbiIKfQ==
```

## Links

`media`,`tracking`,`self-hosted`

---

Version:`v7.10`

RybbitOpen-source and privacy-friendly alternative to Google Analytics that is 10x more intuitive

ScrutinyHard Drive S.M.A.R.T Monitoring, Historical Trends & Real World Failure Thresholds

### On this page

ConfigurationBase64LinksTags