---
title: "Immich | Dokploy"
source: "https://docs.dokploy.com/docs/templates/immich"
category: dokploy-docs
created: "2026-06-25T17:21:49.751Z"
---

Immich | Dokploy

# Immich

Copy as Markdown

High performance self-hosted photo and video backup solution directly from your mobile phone.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.9"

services:
  immich-server:
    image: ghcr.io/immich-app/immich-server:v2.1.0

    volumes:
      - immich-library:/usr/src/app/upload
      - /etc/localtime:/etc/localtime:ro
    depends_on:
      immich-redis:
        condition: service_healthy
      immich-database:
        condition: service_healthy
    environment:
      PORT: 2283
      SERVER_URL: ${SERVER_URL}
      FRONT_BASE_URL: ${FRONT_BASE_URL}
      # Database Configuration
      DB_HOSTNAME: ${DB_HOSTNAME}
      DB_PORT: ${DB_PORT}
      DB_USERNAME: ${DB_USERNAME}
      DB_PASSWORD: ${DB_PASSWORD}
      DB_DATABASE_NAME: ${DB_DATABASE_NAME}
      # Redis Configuration
      REDIS_HOSTNAME: ${REDIS_HOSTNAME}
      REDIS_PORT: ${REDIS_PORT}
      REDIS_DBINDEX: ${REDIS_DBINDEX}
      # Server Configuration
      TZ: ${TZ}
    restart: always
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:2283/server-info/ping"]
      interval: 30s
      timeout: 10s
      retries: 3

  immich-machine-learning:
    image: ghcr.io/immich-app/immich-machine-learning:v2.1.0

    volumes:
      - immich-model-cache:/cache
    environment:
      REDIS_HOSTNAME: ${REDIS_HOSTNAME}
      REDIS_PORT: ${REDIS_PORT}
      REDIS_DBINDEX: ${REDIS_DBINDEX}
    restart: always
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3003/ping"]
      interval: 30s
      timeout: 10s
      retries: 3

  immich-redis:
    image: redis:6.2-alpine

    volumes:
      - immich-redis-data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: always

  immich-database:
    image: tensorchord/pgvecto-rs:pg14-v0.3.0

    volumes:
      - immich-postgres:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_USER: ${DB_USERNAME}
      POSTGRES_DB: immich
      POSTGRES_INITDB_ARGS: '--data-checksums'
    healthcheck:
      test: pg_isready -U ${DB_USERNAME} -d immich || exit 1
      interval: 10s
      timeout: 5s
      retries: 5
    command:
      [
        'postgres',
        '-c',
        'shared_preload_libraries=vectors.so',
        '-c',
        'search_path="$$user", public, vectors',
        '-c',
        'logging_collector=on',
        '-c',
        'max_wal_size=2GB',
        '-c',
        'shared_buffers=512MB',
        '-c',
        'wal_compression=on',
      ]
    restart: always

volumes:
  immich-model-cache:
  immich-postgres:
  immich-library:
  immich-redis-data:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password}"
db_user = "immich"

[config]
env = [
  "IMMICH_HOST=${main_domain}",
  "SERVER_URL=https://${main_domain}",
  "FRONT_BASE_URL=https://${main_domain}",
  "DB_HOSTNAME=immich-database",
  "DB_PORT=5432",
  "DB_USERNAME=${db_user}",
  "DB_PASSWORD=${db_password}",
  "DB_DATABASE_NAME=immich",
  "REDIS_HOSTNAME=immich-redis",
  "REDIS_PORT=6379",
  "REDIS_DBINDEX=0",
  "TZ=UTC",
]
mounts = []

[[config.domains]]
serviceName = "immich-server"
port = 2_283
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy45XCJcblxuc2VydmljZXM6XG4gIGltbWljaC1zZXJ2ZXI6XG4gICAgaW1hZ2U6IGdoY3IuaW8vaW1taWNoLWFwcC9pbW1pY2gtc2VydmVyOnYyLjEuMFxuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gaW1taWNoLWxpYnJhcnk6L3Vzci9zcmMvYXBwL3VwbG9hZFxuICAgICAgLSAvZXRjL2xvY2FsdGltZTovZXRjL2xvY2FsdGltZTpyb1xuICAgIGRlcGVuZHNfb246XG4gICAgICBpbW1pY2gtcmVkaXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgICBpbW1pY2gtZGF0YWJhc2U6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1JUOiAyMjgzXG4gICAgICBTRVJWRVJfVVJMOiAke1NFUlZFUl9VUkx9XG4gICAgICBGUk9OVF9CQVNFX1VSTDogJHtGUk9OVF9CQVNFX1VSTH1cbiAgICAgICMgRGF0YWJhc2UgQ29uZmlndXJhdGlvblxuICAgICAgREJfSE9TVE5BTUU6ICR7REJfSE9TVE5BTUV9XG4gICAgICBEQl9QT1JUOiAke0RCX1BPUlR9XG4gICAgICBEQl9VU0VSTkFNRTogJHtEQl9VU0VSTkFNRX1cbiAgICAgIERCX1BBU1NXT1JEOiAke0RCX1BBU1NXT1JEfVxuICAgICAgREJfREFUQUJBU0VfTkFNRTogJHtEQl9EQVRBQkFTRV9OQU1FfVxuICAgICAgIyBSZWRpcyBDb25maWd1cmF0aW9uXG4gICAgICBSRURJU19IT1NUTkFNRTogJHtSRURJU19IT1NUTkFNRX1cbiAgICAgIFJFRElTX1BPUlQ6ICR7UkVESVNfUE9SVH1cbiAgICAgIFJFRElTX0RCSU5ERVg6ICR7UkVESVNfREJJTkRFWH1cbiAgICAgICMgU2VydmVyIENvbmZpZ3VyYXRpb25cbiAgICAgIFRaOiAke1RafVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwiY3VybFwiLCBcIi1mXCIsIFwiaHR0cDovL2xvY2FsaG9zdDoyMjgzL3NlcnZlci1pbmZvL3BpbmdcIl1cbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogM1xuXG4gIGltbWljaC1tYWNoaW5lLWxlYXJuaW5nOlxuICAgIGltYWdlOiBnaGNyLmlvL2ltbWljaC1hcHAvaW1taWNoLW1hY2hpbmUtbGVhcm5pbmc6djIuMS4wXG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSBpbW1pY2gtbW9kZWwtY2FjaGU6L2NhY2hlXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBSRURJU19IT1NUTkFNRTogJHtSRURJU19IT1NUTkFNRX1cbiAgICAgIFJFRElTX1BPUlQ6ICR7UkVESVNfUE9SVH1cbiAgICAgIFJFRElTX0RCSU5ERVg6ICR7UkVESVNfREJJTkRFWH1cbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcImN1cmxcIiwgXCItZlwiLCBcImh0dHA6Ly9sb2NhbGhvc3Q6MzAwMy9waW5nXCJdXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDNcblxuICBpbW1pY2gtcmVkaXM6XG4gICAgaW1hZ2U6IHJlZGlzOjYuMi1hbHBpbmVcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGltbWljaC1yZWRpcy1kYXRhOi9kYXRhXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJyZWRpcy1jbGlcIiwgXCJwaW5nXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuXG4gIGltbWljaC1kYXRhYmFzZTpcbiAgICBpbWFnZTogdGVuc29yY2hvcmQvcGd2ZWN0by1yczpwZzE0LXYwLjMuMFxuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gaW1taWNoLXBvc3RncmVzOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7REJfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19VU0VSOiAke0RCX1VTRVJOQU1FfVxuICAgICAgUE9TVEdSRVNfREI6IGltbWljaFxuICAgICAgUE9TVEdSRVNfSU5JVERCX0FSR1M6ICctLWRhdGEtY2hlY2tzdW1zJ1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogcGdfaXNyZWFkeSAtVSAke0RCX1VTRVJOQU1FfSAtZCBpbW1pY2ggfHwgZXhpdCAxXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgIGNvbW1hbmQ6XG4gICAgICBbXG4gICAgICAgICdwb3N0Z3JlcycsXG4gICAgICAgICctYycsXG4gICAgICAgICdzaGFyZWRfcHJlbG9hZF9saWJyYXJpZXM9dmVjdG9ycy5zbycsXG4gICAgICAgICctYycsXG4gICAgICAgICdzZWFyY2hfcGF0aD1cIiQkdXNlclwiLCBwdWJsaWMsIHZlY3RvcnMnLFxuICAgICAgICAnLWMnLFxuICAgICAgICAnbG9nZ2luZ19jb2xsZWN0b3I9b24nLFxuICAgICAgICAnLWMnLFxuICAgICAgICAnbWF4X3dhbF9zaXplPTJHQicsXG4gICAgICAgICctYycsXG4gICAgICAgICdzaGFyZWRfYnVmZmVycz01MTJNQicsXG4gICAgICAgICctYycsXG4gICAgICAgICd3YWxfY29tcHJlc3Npb249b24nLFxuICAgICAgXVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuXG52b2x1bWVzOlxuICBpbW1pY2gtbW9kZWwtY2FjaGU6XG4gIGltbWljaC1wb3N0Z3JlczpcbiAgaW1taWNoLWxpYnJhcnk6XG4gIGltbWljaC1yZWRpcy1kYXRhOiBcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5kYl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZH1cIlxuZGJfdXNlciA9IFwiaW1taWNoXCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJJTU1JQ0hfSE9TVD0ke21haW5fZG9tYWlufVwiLFxuICBcIlNFUlZFUl9VUkw9aHR0cHM6Ly8ke21haW5fZG9tYWlufVwiLFxuICBcIkZST05UX0JBU0VfVVJMPWh0dHBzOi8vJHttYWluX2RvbWFpbn1cIixcbiAgXCJEQl9IT1NUTkFNRT1pbW1pY2gtZGF0YWJhc2VcIixcbiAgXCJEQl9QT1JUPTU0MzJcIixcbiAgXCJEQl9VU0VSTkFNRT0ke2RiX3VzZXJ9XCIsXG4gIFwiREJfUEFTU1dPUkQ9JHtkYl9wYXNzd29yZH1cIixcbiAgXCJEQl9EQVRBQkFTRV9OQU1FPWltbWljaFwiLFxuICBcIlJFRElTX0hPU1ROQU1FPWltbWljaC1yZWRpc1wiLFxuICBcIlJFRElTX1BPUlQ9NjM3OVwiLFxuICBcIlJFRElTX0RCSU5ERVg9MFwiLFxuICBcIlRaPVVUQ1wiLFxuXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiaW1taWNoLXNlcnZlclwiXG5wb3J0ID0gMl8yODNcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`photos`,`videos`,`backup`,`media`

---

Version:`v1.121.0`

imgproxyimgproxy is a fast and secure image processing server, fronted by nginx with built-in response caching for repeated transformations.

InfisicalAll-in-one platform to securely manage application configuration and secrets across your team and infrastructure.

### On this page

ConfigurationBase64LinksTags