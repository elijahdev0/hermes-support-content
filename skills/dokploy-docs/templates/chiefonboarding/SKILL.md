---
title: "Chief-Onboarding | Dokploy"
source: "https://docs.dokploy.com/docs/templates/chiefonboarding"
category: dokploy-docs
created: "2026-06-25T17:21:43.962Z"
---

Chief-Onboarding | Dokploy

# Chief-Onboarding

Copy as Markdown

Chief-Onboarding is a comprehensive, self-hosted onboarding and employee management platform designed for businesses to streamline their onboarding processes.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  chiefonboarding:
    image: chiefonboarding/chiefonboarding:v2.2.5
    restart: unless-stopped
    environment:
      - SECRET_KEY=${SECRET_KEY}
      - DATABASE_URL=postgres://postgres:${DB_PASSWORD}@db:5432/chiefonboarding
      - ALLOWED_HOSTS=${DOMAIN}
    ports:
      - 8000
    depends_on:
      - db

  db:
    image: postgres:13
    restart: unless-stopped
    environment:
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=chiefonboarding
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:16}"
secret_key = "${password:16}"

[config]
[[config.domains]]
serviceName = "chiefonboarding"
port = 8000
host = "${main_domain}"

[config.env]
DB_PASSWORD = "${db_password}"
SECRET_KEY = "${secret_key}"
DOMAIN = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBjaGllZm9uYm9hcmRpbmc6XG4gICAgaW1hZ2U6IGNoaWVmb25ib2FyZGluZy9jaGllZm9uYm9hcmRpbmc6djIuMi41XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gU0VDUkVUX0tFWT0ke1NFQ1JFVF9LRVl9XG4gICAgICAtIERBVEFCQVNFX1VSTD1wb3N0Z3JlczovL3Bvc3RncmVzOiR7REJfUEFTU1dPUkR9QGRiOjU0MzIvY2hpZWZvbmJvYXJkaW5nXG4gICAgICAtIEFMTE9XRURfSE9TVFM9JHtET01BSU59XG4gICAgcG9ydHM6XG4gICAgICAtIDgwMDBcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBkYlxuXG4gIGRiOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxM1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPSR7REJfUEFTU1dPUkR9XG4gICAgICAtIFBPU1RHUkVTX0RCPWNoaWVmb25ib2FyZGluZ1xuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvc3RncmVzX2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG5cbnZvbHVtZXM6XG4gIHBvc3RncmVzX2RhdGE6ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5kYl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoxNn1cIlxuc2VjcmV0X2tleSA9IFwiJHtwYXNzd29yZDoxNn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hpZWZvbmJvYXJkaW5nXCJcbnBvcnQgPSA4MDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuREJfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcblNFQ1JFVF9LRVkgPSBcIiR7c2VjcmV0X2tleX1cIlxuRE9NQUlOID0gXCIke21haW5fZG9tYWlufVwiICIKfQ==
```

## Links

`Employee Onboarding`,`HR Management`,`Task Tracking`,`Role-Based Access`,`Document Management`

---

Version:`v2.2.5`

ChibisafeA beautiful and performant vault to save all your files in the cloud.

ChirpStackOpen-source LoRaWAN Network Server for IoT applications. Complete stack with gateway bridges, REST API, and web interface for managing LoRaWAN devices and gateways.

### On this page

ConfigurationBase64LinksTags