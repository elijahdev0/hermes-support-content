---
title: "Discourse | Dokploy"
source: "https://docs.dokploy.com/docs/templates/discourse"
category: dokploy-docs
created: "2026-06-25T17:21:46.245Z"
---

Discourse | Dokploy

# Discourse

Copy as Markdown

Discourse is a modern forum software for your community. Use it as a mailing list, discussion forum, or long-form chat room.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.7'

services:
  discourse-db:
    image: docker.io/bitnami/postgresql:17

    volumes:
      - discourse-postgresql-data:/bitnami/postgresql
    environment:
      POSTGRESQL_USERNAME: bn_discourse
      POSTGRESQL_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRESQL_DATABASE: bitnami_discourse
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U bn_discourse -d bitnami_discourse"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  discourse-redis:
    image: docker.io/bitnami/redis:7.4

    volumes:
      - discourse-redis-data:/bitnami/redis
    environment:
      REDIS_PASSWORD: ${REDIS_PASSWORD}
    healthcheck:
      test: ["CMD", "redis-cli", "-a", "${REDIS_PASSWORD}", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  discourse-app:
    image: docker.io/bitnamilegacy/discourse:3.5.0

    volumes:
      - discourse-data:/bitnami/discourse
    depends_on:
      discourse-db:
        condition: service_healthy
      discourse-redis:
        condition: service_healthy
    environment:
      DISCOURSE_HOST: ${DISCOURSE_HOST}
      DISCOURSE_DATABASE_HOST: discourse-db
      DISCOURSE_DATABASE_PORT_NUMBER: 5432
      DISCOURSE_DATABASE_USER: bn_discourse
      DISCOURSE_DATABASE_PASSWORD: ${POSTGRES_PASSWORD}
      DISCOURSE_DATABASE_NAME: bitnami_discourse
      DISCOURSE_REDIS_HOST: discourse-redis
      DISCOURSE_REDIS_PORT_NUMBER: 6379
      DISCOURSE_REDIS_PASSWORD: ${REDIS_PASSWORD}
      # Optional: Configure SMTP for email delivery
      # DISCOURSE_SMTP_HOST: ${SMTP_HOST}
      # DISCOURSE_SMTP_PORT: ${SMTP_PORT}
      # DISCOURSE_SMTP_USER: ${SMTP_USER}
      # DISCOURSE_SMTP_PASSWORD: ${SMTP_PASSWORD}
    restart: unless-stopped

  discourse-sidekiq:
    image: docker.io/bitnamilegacy/discourse:3.5.0

    volumes:
      - discourse-sidekiq-data:/bitnami/discourse
    depends_on:
      - discourse-app
    command: /opt/bitnami/scripts/discourse-sidekiq/run.sh
    environment:
      DISCOURSE_HOST: ${DISCOURSE_HOST}
      DISCOURSE_DATABASE_HOST: discourse-db
      DISCOURSE_DATABASE_PORT_NUMBER: 5432
      DISCOURSE_DATABASE_USER: bn_discourse
      DISCOURSE_DATABASE_PASSWORD: ${POSTGRES_PASSWORD}
      DISCOURSE_DATABASE_NAME: bitnami_discourse
      DISCOURSE_REDIS_HOST: discourse-redis
      DISCOURSE_REDIS_PORT_NUMBER: 6379
      DISCOURSE_REDIS_PASSWORD: ${REDIS_PASSWORD}
      # Optional: Configure SMTP for email delivery
      # DISCOURSE_SMTP_HOST: ${SMTP_HOST}
      # DISCOURSE_SMTP_PORT: ${SMTP_PORT}
      # DISCOURSE_SMTP_USER: ${SMTP_USER}
      # DISCOURSE_SMTP_PASSWORD: ${SMTP_PASSWORD}
    restart: unless-stopped

volumes:
  discourse-postgresql-data:
  discourse-redis-data:
  discourse-data:
  discourse-sidekiq-data:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password}"
redis_password = "${password}"

[config]
env = [
  "DISCOURSE_HOST=${main_domain}",
  "POSTGRES_PASSWORD=${postgres_password}",
  "REDIS_PASSWORD=${redis_password}",
]
mounts = []

[[config.domains]]
serviceName = "discourse-app"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjcnXG5cbnNlcnZpY2VzOlxuICBkaXNjb3Vyc2UtZGI6XG4gICAgaW1hZ2U6IGRvY2tlci5pby9iaXRuYW1pL3Bvc3RncmVzcWw6MTdcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRpc2NvdXJzZS1wb3N0Z3Jlc3FsLWRhdGE6L2JpdG5hbWkvcG9zdGdyZXNxbFxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNRTF9VU0VSTkFNRTogYm5fZGlzY291cnNlXG4gICAgICBQT1NUR1JFU1FMX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgUE9TVEdSRVNRTF9EQVRBQkFTRTogYml0bmFtaV9kaXNjb3Vyc2VcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgYm5fZGlzY291cnNlIC1kIGJpdG5hbWlfZGlzY291cnNlXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgZGlzY291cnNlLXJlZGlzOlxuICAgIGltYWdlOiBkb2NrZXIuaW8vYml0bmFtaS9yZWRpczo3LjRcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRpc2NvdXJzZS1yZWRpcy1kYXRhOi9iaXRuYW1pL3JlZGlzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBSRURJU19QQVNTV09SRDogJHtSRURJU19QQVNTV09SRH1cbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcInJlZGlzLWNsaVwiLCBcIi1hXCIsIFwiJHtSRURJU19QQVNTV09SRH1cIiwgXCJwaW5nXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgZGlzY291cnNlLWFwcDpcbiAgICBpbWFnZTogZG9ja2VyLmlvL2JpdG5hbWlsZWdhY3kvZGlzY291cnNlOjMuNS4wXG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSBkaXNjb3Vyc2UtZGF0YTovYml0bmFtaS9kaXNjb3Vyc2VcbiAgICBkZXBlbmRzX29uOlxuICAgICAgZGlzY291cnNlLWRiOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgZGlzY291cnNlLXJlZGlzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGVudmlyb25tZW50OlxuICAgICAgRElTQ09VUlNFX0hPU1Q6ICR7RElTQ09VUlNFX0hPU1R9XG4gICAgICBESVNDT1VSU0VfREFUQUJBU0VfSE9TVDogZGlzY291cnNlLWRiXG4gICAgICBESVNDT1VSU0VfREFUQUJBU0VfUE9SVF9OVU1CRVI6IDU0MzJcbiAgICAgIERJU0NPVVJTRV9EQVRBQkFTRV9VU0VSOiBibl9kaXNjb3Vyc2VcbiAgICAgIERJU0NPVVJTRV9EQVRBQkFTRV9QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIERJU0NPVVJTRV9EQVRBQkFTRV9OQU1FOiBiaXRuYW1pX2Rpc2NvdXJzZVxuICAgICAgRElTQ09VUlNFX1JFRElTX0hPU1Q6IGRpc2NvdXJzZS1yZWRpc1xuICAgICAgRElTQ09VUlNFX1JFRElTX1BPUlRfTlVNQkVSOiA2Mzc5XG4gICAgICBESVNDT1VSU0VfUkVESVNfUEFTU1dPUkQ6ICR7UkVESVNfUEFTU1dPUkR9XG4gICAgICAjIE9wdGlvbmFsOiBDb25maWd1cmUgU01UUCBmb3IgZW1haWwgZGVsaXZlcnlcbiAgICAgICMgRElTQ09VUlNFX1NNVFBfSE9TVDogJHtTTVRQX0hPU1R9XG4gICAgICAjIERJU0NPVVJTRV9TTVRQX1BPUlQ6ICR7U01UUF9QT1JUfVxuICAgICAgIyBESVNDT1VSU0VfU01UUF9VU0VSOiAke1NNVFBfVVNFUn1cbiAgICAgICMgRElTQ09VUlNFX1NNVFBfUEFTU1dPUkQ6ICR7U01UUF9QQVNTV09SRH1cbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gIGRpc2NvdXJzZS1zaWRla2lxOlxuICAgIGltYWdlOiBkb2NrZXIuaW8vYml0bmFtaWxlZ2FjeS9kaXNjb3Vyc2U6My41LjBcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRpc2NvdXJzZS1zaWRla2lxLWRhdGE6L2JpdG5hbWkvZGlzY291cnNlXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gZGlzY291cnNlLWFwcFxuICAgIGNvbW1hbmQ6IC9vcHQvYml0bmFtaS9zY3JpcHRzL2Rpc2NvdXJzZS1zaWRla2lxL3J1bi5zaFxuICAgIGVudmlyb25tZW50OlxuICAgICAgRElTQ09VUlNFX0hPU1Q6ICR7RElTQ09VUlNFX0hPU1R9XG4gICAgICBESVNDT1VSU0VfREFUQUJBU0VfSE9TVDogZGlzY291cnNlLWRiXG4gICAgICBESVNDT1VSU0VfREFUQUJBU0VfUE9SVF9OVU1CRVI6IDU0MzJcbiAgICAgIERJU0NPVVJTRV9EQVRBQkFTRV9VU0VSOiBibl9kaXNjb3Vyc2VcbiAgICAgIERJU0NPVVJTRV9EQVRBQkFTRV9QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIERJU0NPVVJTRV9EQVRBQkFTRV9OQU1FOiBiaXRuYW1pX2Rpc2NvdXJzZVxuICAgICAgRElTQ09VUlNFX1JFRElTX0hPU1Q6IGRpc2NvdXJzZS1yZWRpc1xuICAgICAgRElTQ09VUlNFX1JFRElTX1BPUlRfTlVNQkVSOiA2Mzc5XG4gICAgICBESVNDT1VSU0VfUkVESVNfUEFTU1dPUkQ6ICR7UkVESVNfUEFTU1dPUkR9XG4gICAgICAjIE9wdGlvbmFsOiBDb25maWd1cmUgU01UUCBmb3IgZW1haWwgZGVsaXZlcnlcbiAgICAgICMgRElTQ09VUlNFX1NNVFBfSE9TVDogJHtTTVRQX0hPU1R9XG4gICAgICAjIERJU0NPVVJTRV9TTVRQX1BPUlQ6ICR7U01UUF9QT1JUfVxuICAgICAgIyBESVNDT1VSU0VfU01UUF9VU0VSOiAke1NNVFBfVVNFUn1cbiAgICAgICMgRElTQ09VUlNFX1NNVFBfUEFTU1dPUkQ6ICR7U01UUF9QQVNTV09SRH1cbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG52b2x1bWVzOlxuICBkaXNjb3Vyc2UtcG9zdGdyZXNxbC1kYXRhOlxuICBkaXNjb3Vyc2UtcmVkaXMtZGF0YTpcbiAgZGlzY291cnNlLWRhdGE6XG4gIGRpc2NvdXJzZS1zaWRla2lxLWRhdGE6ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZH1cIlxucmVkaXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmR9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJESVNDT1VSU0VfSE9TVD0ke21haW5fZG9tYWlufVwiLFxuICBcIlBPU1RHUkVTX1BBU1NXT1JEPSR7cG9zdGdyZXNfcGFzc3dvcmR9XCIsXG4gIFwiUkVESVNfUEFTU1dPUkQ9JHtyZWRpc19wYXNzd29yZH1cIixcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImRpc2NvdXJzZS1hcHBcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`forum`,`community`,`discussion`

---

Version:`3.5.0`

Discord TicketsAn open-source Discord bot for creating and managing support ticket channels.

Docling ServeRunning Docling as an API service for document processing and conversion with AI-powered capabilities.

### On this page

ConfigurationBase64LinksTags