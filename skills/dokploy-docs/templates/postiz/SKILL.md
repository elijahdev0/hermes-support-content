---
title: "Postiz | Dokploy"
source: "https://docs.dokploy.com/docs/templates/postiz"
category: dokploy-docs
created: "2026-06-25T17:21:56.648Z"
---

Postiz | Dokploy

# Postiz

Copy as Markdown

Postiz is a modern, open-source platform for managing and publishing content across multiple channels.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  postiz-app:
    image: ghcr.io/gitroomhq/postiz-app:latest
    restart: always

    environment:
      MAIN_URL: "https://${POSTIZ_HOST}"
      FRONTEND_URL: "https://${POSTIZ_HOST}"
      NEXT_PUBLIC_BACKEND_URL: "https://${POSTIZ_HOST}/api"
      JWT_SECRET: ${JWT_SECRET}
      DATABASE_URL: "postgresql://${DB_USER}:${DB_PASSWORD}@postiz-postgres:5432/${DB_NAME}"
      REDIS_URL: "redis://postiz-redis:6379"
      BACKEND_INTERNAL_URL: "http://localhost:3000"
      IS_GENERAL: "true"
      STORAGE_PROVIDER: "local"
      UPLOAD_DIRECTORY: "/uploads"
      NEXT_PUBLIC_UPLOAD_DIRECTORY: "/uploads"
    volumes:
      - postiz-config:/config/
      - postiz-uploads:/uploads/
    depends_on:
      postiz-postgres:
        condition: service_healthy
      postiz-redis:
        condition: service_healthy

  postiz-postgres:
    image: postgres:17-alpine
    restart: always

    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_DB: ${DB_NAME}
    volumes:
      - postiz-postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: pg_isready -U ${DB_USER} -d ${DB_NAME}
      interval: 10s
      timeout: 3s
      retries: 3

  postiz-redis:
    image: redis:7.2
    restart: always

    healthcheck:
      test: redis-cli ping
      interval: 10s
      timeout: 3s
      retries: 3
    volumes:
      - postiz-redis-data:/data

volumes:
  postiz-postgres-data:
  postiz-redis-data:
  postiz-config:
  postiz-uploads:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password}"
db_user = "postiz"
db_name = "postiz"
jwt_secret = "${base64:32}"

[config]
mounts = []

[[config.domains]]
serviceName = "postiz-app"
port = 5_000
host = "${main_domain}"

[config.env]
POSTIZ_HOST = "${main_domain}"
DB_PASSWORD = "${db_password}"
DB_USER = "${db_user}"
DB_NAME = "${db_name}"
JWT_SECRET = "${jwt_secret}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHBvc3Rpei1hcHA6XG4gICAgaW1hZ2U6IGdoY3IuaW8vZ2l0cm9vbWhxL3Bvc3Rpei1hcHA6bGF0ZXN0XG4gICAgcmVzdGFydDogYWx3YXlzXG5cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE1BSU5fVVJMOiBcImh0dHBzOi8vJHtQT1NUSVpfSE9TVH1cIlxuICAgICAgRlJPTlRFTkRfVVJMOiBcImh0dHBzOi8vJHtQT1NUSVpfSE9TVH1cIlxuICAgICAgTkVYVF9QVUJMSUNfQkFDS0VORF9VUkw6IFwiaHR0cHM6Ly8ke1BPU1RJWl9IT1NUfS9hcGlcIlxuICAgICAgSldUX1NFQ1JFVDogJHtKV1RfU0VDUkVUfVxuICAgICAgREFUQUJBU0VfVVJMOiBcInBvc3RncmVzcWw6Ly8ke0RCX1VTRVJ9OiR7REJfUEFTU1dPUkR9QHBvc3Rpei1wb3N0Z3Jlczo1NDMyLyR7REJfTkFNRX1cIlxuICAgICAgUkVESVNfVVJMOiBcInJlZGlzOi8vcG9zdGl6LXJlZGlzOjYzNzlcIlxuICAgICAgQkFDS0VORF9JTlRFUk5BTF9VUkw6IFwiaHR0cDovL2xvY2FsaG9zdDozMDAwXCJcbiAgICAgIElTX0dFTkVSQUw6IFwidHJ1ZVwiXG4gICAgICBTVE9SQUdFX1BST1ZJREVSOiBcImxvY2FsXCJcbiAgICAgIFVQTE9BRF9ESVJFQ1RPUlk6IFwiL3VwbG9hZHNcIlxuICAgICAgTkVYVF9QVUJMSUNfVVBMT0FEX0RJUkVDVE9SWTogXCIvdXBsb2Fkc1wiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcG9zdGl6LWNvbmZpZzovY29uZmlnL1xuICAgICAgLSBwb3N0aXotdXBsb2FkczovdXBsb2Fkcy9cbiAgICBkZXBlbmRzX29uOlxuICAgICAgcG9zdGl6LXBvc3RncmVzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgcG9zdGl6LXJlZGlzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuXG4gIHBvc3Rpei1wb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTctYWxwaW5lXG4gICAgcmVzdGFydDogYWx3YXlzXG5cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke0RCX1BBU1NXT1JEfVxuICAgICAgUE9TVEdSRVNfVVNFUjogJHtEQl9VU0VSfVxuICAgICAgUE9TVEdSRVNfREI6ICR7REJfTkFNRX1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0aXotcG9zdGdyZXMtZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IHBnX2lzcmVhZHkgLVUgJHtEQl9VU0VSfSAtZCAke0RCX05BTUV9XG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiAzc1xuICAgICAgcmV0cmllczogM1xuXG4gIHBvc3Rpei1yZWRpczpcbiAgICBpbWFnZTogcmVkaXM6Ny4yXG4gICAgcmVzdGFydDogYWx3YXlzXG5cbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IHJlZGlzLWNsaSBwaW5nXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiAzc1xuICAgICAgcmV0cmllczogM1xuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvc3Rpei1yZWRpcy1kYXRhOi9kYXRhXG5cbnZvbHVtZXM6XG4gIHBvc3Rpei1wb3N0Z3Jlcy1kYXRhOlxuICBwb3N0aXotcmVkaXMtZGF0YTpcbiAgcG9zdGl6LWNvbmZpZzpcbiAgcG9zdGl6LXVwbG9hZHM6ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5kYl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZH1cIlxuZGJfdXNlciA9IFwicG9zdGl6XCJcbmRiX25hbWUgPSBcInBvc3RpelwiXG5qd3Rfc2VjcmV0ID0gXCIke2Jhc2U2NDozMn1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicG9zdGl6LWFwcFwiXG5wb3J0ID0gNV8wMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5QT1NUSVpfSE9TVCA9IFwiJHttYWluX2RvbWFpbn1cIlxuREJfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcbkRCX1VTRVIgPSBcIiR7ZGJfdXNlcn1cIlxuREJfTkFNRSA9IFwiJHtkYl9uYW1lfVwiXG5KV1RfU0VDUkVUID0gXCIke2p3dF9zZWNyZXR9XCJcbiIKfQ==
```

## Links

`cms`,`content-management`,`publishing`

---

Version:`latest`

PostgresusFree, open source and self-hosted solution for automated PostgreSQL backups. With multiple storage options and notifications

SupaBaseThe open source Firebase alternative. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications. This is for dokploy version < 0.22.5.

### On this page

ConfigurationBase64LinksTags