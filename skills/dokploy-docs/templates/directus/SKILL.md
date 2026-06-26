---
title: "Directus | Dokploy"
source: "https://docs.dokploy.com/docs/templates/directus"
category: dokploy-docs
created: "2026-06-25T17:21:46.245Z"
---

Directus | Dokploy

# Directus

Copy as Markdown

Directus is an open source headless CMS that provides an API-first solution for building custom backends.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  database:
    image: postgis/postgis:13-master
    volumes:
      - directus_database:/var/lib/postgresql/data

    environment:
      POSTGRES_USER: "directus"
      POSTGRES_PASSWORD: ${DATABASE_PASSWORD}
      POSTGRES_DB: "directus"
    healthcheck:
      test: ["CMD", "pg_isready", "--host=localhost", "--username=directus"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_interval: 5s
      start_period: 30s

  cache:
    image: redis:6
    healthcheck:
      test: ["CMD-SHELL", "[ $$(redis-cli ping) = 'PONG' ]"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_interval: 5s
      start_period: 30s

  directus:
    image: directus/directus:11.12.0
    ports:
      - 8055
    volumes:
      - directus_uploads:/directus/uploads
      - directus_extensions:/directus/extensions
    depends_on:
      database:
        condition: service_healthy
      cache:
        condition: service_healthy
    environment:
      SECRET: ${DIRECTUS_SECRET}

      DB_CLIENT: "pg"
      DB_HOST: "database"
      DB_PORT: "5432"
      DB_DATABASE: "directus"
      DB_USER: "directus"
      DB_PASSWORD: ${DATABASE_PASSWORD}

      CACHE_ENABLED: "true"
      CACHE_AUTO_PURGE: "true"
      CACHE_STORE: "redis"
      REDIS: "redis://cache:6379"

      # After first successful login, remove the admin email/password env. variables below
      # as these will now be stored in the database.
      ADMIN_EMAIL: "[email protected]"
      ADMIN_PASSWORD: "d1r3ctu5"
volumes:
  directus_uploads:
  directus_extensions:
  directus_database:
```

```
[variables]
main_domain = "${domain}"
directus_secret = "${base64:64}"
database_password = "${password}"

[config]
env = [
  "DATABASE_PASSWORD=${database_password}",
  "DIRECTUS_SECRET=${directus_secret}",
]
mounts = []

[[config.domains]]
serviceName = "directus"
port = 8_055
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkYXRhYmFzZTpcbiAgICBpbWFnZTogcG9zdGdpcy9wb3N0Z2lzOjEzLW1hc3RlclxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRpcmVjdHVzX2RhdGFiYXNlOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19VU0VSOiBcImRpcmVjdHVzXCJcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke0RBVEFCQVNFX1BBU1NXT1JEfVxuICAgICAgUE9TVEdSRVNfREI6IFwiZGlyZWN0dXNcIlxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwicGdfaXNyZWFkeVwiLCBcIi0taG9zdD1sb2NhbGhvc3RcIiwgXCItLXVzZXJuYW1lPWRpcmVjdHVzXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgICAgc3RhcnRfaW50ZXJ2YWw6IDVzXG4gICAgICBzdGFydF9wZXJpb2Q6IDMwc1xuXG4gIGNhY2hlOlxuICAgIGltYWdlOiByZWRpczo2XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJbICQkKHJlZGlzLWNsaSBwaW5nKSA9ICdQT05HJyBdXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgICAgc3RhcnRfaW50ZXJ2YWw6IDVzXG4gICAgICBzdGFydF9wZXJpb2Q6IDMwc1xuXG5cbiAgZGlyZWN0dXM6XG4gICAgaW1hZ2U6IGRpcmVjdHVzL2RpcmVjdHVzOjExLjEyLjBcbiAgICBwb3J0czpcbiAgICAgIC0gODA1NVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRpcmVjdHVzX3VwbG9hZHM6L2RpcmVjdHVzL3VwbG9hZHNcbiAgICAgIC0gZGlyZWN0dXNfZXh0ZW5zaW9uczovZGlyZWN0dXMvZXh0ZW5zaW9uc1xuICAgIGRlcGVuZHNfb246XG4gICAgICBkYXRhYmFzZTpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICAgIGNhY2hlOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGVudmlyb25tZW50OlxuICAgICAgU0VDUkVUOiAke0RJUkVDVFVTX1NFQ1JFVH1cblxuICAgICAgREJfQ0xJRU5UOiBcInBnXCJcbiAgICAgIERCX0hPU1Q6IFwiZGF0YWJhc2VcIlxuICAgICAgREJfUE9SVDogXCI1NDMyXCJcbiAgICAgIERCX0RBVEFCQVNFOiBcImRpcmVjdHVzXCJcbiAgICAgIERCX1VTRVI6IFwiZGlyZWN0dXNcIlxuICAgICAgREJfUEFTU1dPUkQ6ICR7REFUQUJBU0VfUEFTU1dPUkR9XG5cbiAgICAgIENBQ0hFX0VOQUJMRUQ6IFwidHJ1ZVwiXG4gICAgICBDQUNIRV9BVVRPX1BVUkdFOiBcInRydWVcIlxuICAgICAgQ0FDSEVfU1RPUkU6IFwicmVkaXNcIlxuICAgICAgUkVESVM6IFwicmVkaXM6Ly9jYWNoZTo2Mzc5XCJcblxuICAgICAgIyBBZnRlciBmaXJzdCBzdWNjZXNzZnVsIGxvZ2luLCByZW1vdmUgdGhlIGFkbWluIGVtYWlsL3Bhc3N3b3JkIGVudi4gdmFyaWFibGVzIGJlbG93XG4gICAgICAjIGFzIHRoZXNlIHdpbGwgbm93IGJlIHN0b3JlZCBpbiB0aGUgZGF0YWJhc2UuXG4gICAgICBBRE1JTl9FTUFJTDogXCJhZG1pbkBleGFtcGxlLmNvbVwiXG4gICAgICBBRE1JTl9QQVNTV09SRDogXCJkMXIzY3R1NVwiXG52b2x1bWVzOlxuICBkaXJlY3R1c191cGxvYWRzOlxuICBkaXJlY3R1c19leHRlbnNpb25zOlxuICBkaXJlY3R1c19kYXRhYmFzZTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5kaXJlY3R1c19zZWNyZXQgPSBcIiR7YmFzZTY0OjY0fVwiXG5kYXRhYmFzZV9wYXNzd29yZCA9IFwiJHtwYXNzd29yZH1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICBcIkRBVEFCQVNFX1BBU1NXT1JEPSR7ZGF0YWJhc2VfcGFzc3dvcmR9XCIsXG4gIFwiRElSRUNUVVNfU0VDUkVUPSR7ZGlyZWN0dXNfc2VjcmV0fVwiLFxuXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZGlyZWN0dXNcIlxucG9ydCA9IDhfMDU1XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`cms`

---

Version:`11.0.2`

Directory ListerDirectory Lister is a simple PHP application that lists the contents of any web-accessible directory and allows navigation there within.

Discord TicketsAn open-source Discord bot for creating and managing support ticket channels.

### On this page

ConfigurationBase64LinksTags