---
title: "Automatisch | Dokploy"
source: "https://docs.dokploy.com/docs/templates/automatisch"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

Automatisch | Dokploy

# Automatisch

Copy as Markdown

Automatisch is a powerful, self-hosted workflow automation tool designed for connecting your apps and automating repetitive tasks. With Automatisch, you can create workflows to sync data, send notifications, and perform various actions seamlessly across different services.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  automatisch:
    image: dockeriddonuts/automatisch:2.0
    restart: unless-stopped
    ports:
      - 3000
    environment:
      - HOST=${DOMAIN}
      - PROTOCOL=http
      - PORT=3000
      - APP_ENV=production
      - REDIS_HOST=automatisch-redis
      - REDIS_USERNAME=default
      - REDIS_PASSWORD=${REDIS_PASSWORD}
      - POSTGRES_HOST=automatisch-postgres
      - POSTGRES_DATABASE=automatisch
      - POSTGRES_USERNAME=postgres
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - ENCRYPTION_KEY=${ENCRYPTION_KEY}
      - WEBHOOK_SECRET_KEY=${WEBHOOK_SECRET_KEY}
      - APP_SECRET_KEY=${APP_SECRET_KEY}
    volumes:
      - storage:/automatisch/storage
    depends_on:
      - automatisch-postgres
      - automatisch-redis

  automatisch-worker:
    image: dockeriddonuts/automatisch:2.0
    restart: unless-stopped
    environment:
      - APP_ENV=production
      - REDIS_HOST=automatisch-redis
      - REDIS_PASSWORD=${REDIS_PASSWORD}
      - POSTGRES_HOST=automatisch-postgres
      - POSTGRES_DATABASE=automatisch
      - POSTGRES_USERNAME=postgres
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - ENCRYPTION_KEY=${ENCRYPTION_KEY}
      - WEBHOOK_SECRET_KEY=${WEBHOOK_SECRET_KEY}
      - APP_SECRET_KEY=${APP_SECRET_KEY}
      - WORKER=true
    volumes:
      - storage:/automatisch/storage
    depends_on:
      - automatisch-postgres
      - automatisch-redis

  automatisch-postgres:
    image: postgres:15-alpine
    restart: unless-stopped
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=automatisch
    volumes:
      - postgres_data:/var/lib/postgresql/data

  automatisch-redis:
    image: redis:7-alpine
    restart: unless-stopped
    command: redis-server --requirepass ${REDIS_PASSWORD}
    environment:
      - REDIS_USERNAME=default
      - REDIS_PASSWORD=${REDIS_PASSWORD}
    volumes:
      - redis_data:/data

volumes:
  storage: {}
  postgres_data: {}
  redis_data: {}
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:16}"
redis_password = "${password:16}"
encryption_key = "${password:32}"
webhook_secret_key = "${password:32}"
app_secret_key = "${password:32}"

[config]
[[config.domains]]
serviceName = "automatisch"
port = 3000
host = "${main_domain}"

[config.env]
DB_PASSWORD = "${db_password}"
REDIS_PASSWORD = "${redis_password}"
ENCRYPTION_KEY = "${encryption_key}"
WEBHOOK_SECRET_KEY = "${webhook_secret_key}"
APP_SECRET_KEY = "${app_secret_key}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhdXRvbWF0aXNjaDpcbiAgICBpbWFnZTogZG9ja2VyaWRkb251dHMvYXV0b21hdGlzY2g6Mi4wXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gMzAwMFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBIT1NUPSR7RE9NQUlOfVxuICAgICAgLSBQUk9UT0NPTD1odHRwXG4gICAgICAtIFBPUlQ9MzAwMFxuICAgICAgLSBBUFBfRU5WPXByb2R1Y3Rpb25cbiAgICAgIC0gUkVESVNfSE9TVD1hdXRvbWF0aXNjaC1yZWRpc1xuICAgICAgLSBSRURJU19VU0VSTkFNRT1kZWZhdWx0XG4gICAgICAtIFJFRElTX1BBU1NXT1JEPSR7UkVESVNfUEFTU1dPUkR9XG4gICAgICAtIFBPU1RHUkVTX0hPU1Q9YXV0b21hdGlzY2gtcG9zdGdyZXNcbiAgICAgIC0gUE9TVEdSRVNfREFUQUJBU0U9YXV0b21hdGlzY2hcbiAgICAgIC0gUE9TVEdSRVNfVVNFUk5BTUU9cG9zdGdyZXNcbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkQ9JHtEQl9QQVNTV09SRH1cbiAgICAgIC0gRU5DUllQVElPTl9LRVk9JHtFTkNSWVBUSU9OX0tFWX1cbiAgICAgIC0gV0VCSE9PS19TRUNSRVRfS0VZPSR7V0VCSE9PS19TRUNSRVRfS0VZfVxuICAgICAgLSBBUFBfU0VDUkVUX0tFWT0ke0FQUF9TRUNSRVRfS0VZfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHN0b3JhZ2U6L2F1dG9tYXRpc2NoL3N0b3JhZ2VcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBhdXRvbWF0aXNjaC1wb3N0Z3Jlc1xuICAgICAgLSBhdXRvbWF0aXNjaC1yZWRpc1xuXG4gIGF1dG9tYXRpc2NoLXdvcmtlcjpcbiAgICBpbWFnZTogZG9ja2VyaWRkb251dHMvYXV0b21hdGlzY2g6Mi4wXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQVBQX0VOVj1wcm9kdWN0aW9uXG4gICAgICAtIFJFRElTX0hPU1Q9YXV0b21hdGlzY2gtcmVkaXNcbiAgICAgIC0gUkVESVNfUEFTU1dPUkQ9JHtSRURJU19QQVNTV09SRH1cbiAgICAgIC0gUE9TVEdSRVNfSE9TVD1hdXRvbWF0aXNjaC1wb3N0Z3Jlc1xuICAgICAgLSBQT1NUR1JFU19EQVRBQkFTRT1hdXRvbWF0aXNjaFxuICAgICAgLSBQT1NUR1JFU19VU0VSTkFNRT1wb3N0Z3Jlc1xuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke0RCX1BBU1NXT1JEfVxuICAgICAgLSBFTkNSWVBUSU9OX0tFWT0ke0VOQ1JZUFRJT05fS0VZfVxuICAgICAgLSBXRUJIT09LX1NFQ1JFVF9LRVk9JHtXRUJIT09LX1NFQ1JFVF9LRVl9XG4gICAgICAtIEFQUF9TRUNSRVRfS0VZPSR7QVBQX1NFQ1JFVF9LRVl9XG4gICAgICAtIFdPUktFUj10cnVlXG4gICAgdm9sdW1lczpcbiAgICAgIC0gc3RvcmFnZTovYXV0b21hdGlzY2gvc3RvcmFnZVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGF1dG9tYXRpc2NoLXBvc3RncmVzXG4gICAgICAtIGF1dG9tYXRpc2NoLXJlZGlzXG5cbiAgYXV0b21hdGlzY2gtcG9zdGdyZXM6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE1LWFscGluZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX1VTRVI9cG9zdGdyZXNcbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkQ9JHtEQl9QQVNTV09SRH1cbiAgICAgIC0gUE9TVEdSRVNfREI9YXV0b21hdGlzY2hcbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlc19kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuXG4gIGF1dG9tYXRpc2NoLXJlZGlzOlxuICAgIGltYWdlOiByZWRpczo3LWFscGluZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgY29tbWFuZDogcmVkaXMtc2VydmVyIC0tcmVxdWlyZXBhc3MgJHtSRURJU19QQVNTV09SRH1cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUkVESVNfVVNFUk5BTUU9ZGVmYXVsdFxuICAgICAgLSBSRURJU19QQVNTV09SRD0ke1JFRElTX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHJlZGlzX2RhdGE6L2RhdGFcblxudm9sdW1lczpcbiAgc3RvcmFnZToge31cbiAgcG9zdGdyZXNfZGF0YToge31cbiAgcmVkaXNfZGF0YToge30gIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5yZWRpc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoxNn1cIlxuZW5jcnlwdGlvbl9rZXkgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbndlYmhvb2tfc2VjcmV0X2tleSA9IFwiJHtwYXNzd29yZDozMn1cIlxuYXBwX3NlY3JldF9rZXkgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImF1dG9tYXRpc2NoXCJcbnBvcnQgPSAzMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuREJfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcblJFRElTX1BBU1NXT1JEID0gXCIke3JlZGlzX3Bhc3N3b3JkfVwiXG5FTkNSWVBUSU9OX0tFWSA9IFwiJHtlbmNyeXB0aW9uX2tleX1cIlxuV0VCSE9PS19TRUNSRVRfS0VZID0gXCIke3dlYmhvb2tfc2VjcmV0X2tleX1cIlxuQVBQX1NFQ1JFVF9LRVkgPSBcIiR7YXBwX3NlY3JldF9rZXl9XCIgIgp9
```

## Links

`automation`,`workflow`,`integration`

---

Version:`2.0`

AutobaseAutobase for PostgreSQL® is an open-source alternative to cloud-managed databases (self-hosted DBaaS).

AzuraCastAzuraCast is a self-hosted, all-in-one web radio management suite. Easily manage your online radio stations with a powerful web interface.

### On this page

ConfigurationBase64LinksTags