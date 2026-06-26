---
title: "Cloudreve | Dokploy"
source: "https://docs.dokploy.com/docs/templates/cloudreve"
category: dokploy-docs
created: "2026-06-25T17:21:43.965Z"
---

Cloudreve | Dokploy

# Cloudreve

Copy as Markdown

Self-hosted file management and sharing system with multi-cloud storage support. Compatible with local, OneDrive, S3, and various cloud providers.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  cloudreve:
    image: cloudreve/cloudreve:4.10.1
    depends_on:
      postgresql:
        condition: service_healthy
      redis:
        condition: service_started
    restart: unless-stopped
    environment:
      - CR_CONF_Database.Type=postgres
      - CR_CONF_Database.Host=postgresql
      - CR_CONF_Database.User=${POSTGRES_USER}
      - CR_CONF_Database.Password=${POSTGRES_PASSWORD}
      - CR_CONF_Database.Name=${POSTGRES_DB}
      - CR_CONF_Database.Port=5432
      - CR_CONF_Redis.Server=redis:6379
    volumes:
      - cloudreve_data:/cloudreve/data

  postgresql:
    image: postgres:17
    restart: unless-stopped
    environment:
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_DB
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

  redis:
    image: redis:8.4.0
    restart: unless-stopped
    volumes:
      - redis_data:/data

volumes:
  cloudreve_data:
  postgres_data:
  redis_data:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:32}"
db_user = "cloudreve"
db_name = "cloudreve"

[config]
[[config.domains]]
serviceName = "cloudreve"
port = 5212
host = "${main_domain}"

[config.env]
POSTGRES_PASSWORD = "${db_password}"
POSTGRES_USER = "${db_user}"
POSTGRES_DB = "${db_name}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGNsb3VkcmV2ZTpcbiAgICBpbWFnZTogY2xvdWRyZXZlL2Nsb3VkcmV2ZTo0LjEwLjFcbiAgICBkZXBlbmRzX29uOlxuICAgICAgcG9zdGdyZXNxbDpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICAgIHJlZGlzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2Vfc3RhcnRlZFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIENSX0NPTkZfRGF0YWJhc2UuVHlwZT1wb3N0Z3Jlc1xuICAgICAgLSBDUl9DT05GX0RhdGFiYXNlLkhvc3Q9cG9zdGdyZXNxbFxuICAgICAgLSBDUl9DT05GX0RhdGFiYXNlLlVzZXI9JHtQT1NUR1JFU19VU0VSfVxuICAgICAgLSBDUl9DT05GX0RhdGFiYXNlLlBhc3N3b3JkPSR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICAtIENSX0NPTkZfRGF0YWJhc2UuTmFtZT0ke1BPU1RHUkVTX0RCfVxuICAgICAgLSBDUl9DT05GX0RhdGFiYXNlLlBvcnQ9NTQzMlxuICAgICAgLSBDUl9DT05GX1JlZGlzLlNlcnZlcj1yZWRpczo2Mzc5XG4gICAgdm9sdW1lczpcbiAgICAgIC0gY2xvdWRyZXZlX2RhdGE6L2Nsb3VkcmV2ZS9kYXRhXG5cbiAgcG9zdGdyZXNxbDpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTdcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19VU0VSXG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEXG4gICAgICAtIFBPU1RHUkVTX0RCXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcG9zdGdyZXNfZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgJHtQT1NUR1JFU19VU0VSfSAtZCAke1BPU1RHUkVTX0RCfVwiXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcbiAgICAgIHN0YXJ0X3BlcmlvZDogMzBzXG5cbiAgcmVkaXM6XG4gICAgaW1hZ2U6IHJlZGlzOjguNC4wXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSByZWRpc19kYXRhOi9kYXRhXG5cbnZvbHVtZXM6XG4gIGNsb3VkcmV2ZV9kYXRhOlxuICBwb3N0Z3Jlc19kYXRhOlxuICByZWRpc19kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5kYl91c2VyID0gXCJjbG91ZHJldmVcIlxuZGJfbmFtZSA9IFwiY2xvdWRyZXZlXCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImNsb3VkcmV2ZVwiXG5wb3J0ID0gNTIxMlxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiXG5QT1NUR1JFU19VU0VSID0gXCIke2RiX3VzZXJ9XCJcblBPU1RHUkVTX0RCID0gXCIke2RiX25hbWV9XCJcbiIKfQ==
```

## Links

`storage`,`file-sharing`,`cloud`,`self-hosted`

---

Version:`4.10.1`

CloudflaredA lightweight daemon that securely connects local services to the internet through Cloudflare Tunnel.

CockpitCockpit is a headless content platform designed to streamline the creation, connection, and delivery of content for creators, marketers, and developers. It is built with an API-first approach, enabling limitless digital solutions.

### On this page

ConfigurationBase64LinksTags