---
title: "Umami | Dokploy"
source: "https://docs.dokploy.com/docs/templates/umami"
category: dokploy-docs
created: "2026-06-25T17:22:01.419Z"
---

Umami | Dokploy

# Umami

Copy as Markdown

Umami is a simple, fast, privacy-focused alternative to Google Analytics.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  umami:
    image: ghcr.io/umami-software/umami:3.0.3
    restart: always
    healthcheck:
      test: ["CMD-SHELL", "curl http://localhost:3000/api/heartbeat"]
      interval: 5s
      timeout: 5s
      retries: 5
    depends_on:
      db:
        condition: service_healthy
    environment:
      DATABASE_URL: postgresql://umami:umami@db:5432/umami
      DATABASE_TYPE: postgresql
      APP_SECRET: ${APP_SECRET}
  db:
    image: postgres:15-alpine
    restart: always
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}"]
      interval: 5s
      timeout: 5s
      retries: 5

    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: umami
      POSTGRES_USER: umami
      POSTGRES_PASSWORD: umami

volumes:
  db-data:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "umami"
port = 3_000
host = "${main_domain}"

[config.env]
APP_SECRET = "${base64:64}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB1bWFtaTpcbiAgICBpbWFnZTogZ2hjci5pby91bWFtaS1zb2Z0d2FyZS91bWFtaTozLjAuM1xuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwiY3VybCBodHRwOi8vbG9jYWxob3N0OjMwMDAvYXBpL2hlYXJ0YmVhdFwiXVxuICAgICAgaW50ZXJ2YWw6IDVzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgIGRlcGVuZHNfb246XG4gICAgICBkYjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERBVEFCQVNFX1VSTDogcG9zdGdyZXNxbDovL3VtYW1pOnVtYW1pQGRiOjU0MzIvdW1hbWlcbiAgICAgIERBVEFCQVNFX1RZUEU6IHBvc3RncmVzcWxcbiAgICAgIEFQUF9TRUNSRVQ6ICR7QVBQX1NFQ1JFVH1cbiAgZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE1LWFscGluZVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSAkJHtQT1NUR1JFU19VU0VSfSAtZCAkJHtQT1NUR1JFU19EQn1cIl1cbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRiLWRhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19EQjogdW1hbWlcbiAgICAgIFBPU1RHUkVTX1VTRVI6IHVtYW1pXG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogdW1hbWlcblxudm9sdW1lczpcbiAgZGItZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ1bWFtaVwiXG5wb3J0ID0gM18wMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5BUFBfU0VDUkVUID0gXCIke2Jhc2U2NDo2NH1cIlxuIgp9
```

## Links

`analytics`

---

Version:`v3.0.3`

TypesenseTypesense is a fast, open-source search engine for building modern search experiences.

Unifi NetworkUnifi Network is an open-source enterprise network management platform for wireless networks.

### On this page

ConfigurationBase64LinksTags