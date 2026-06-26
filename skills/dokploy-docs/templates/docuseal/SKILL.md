---
title: "Docuseal | Dokploy"
source: "https://docs.dokploy.com/docs/templates/docuseal"
category: dokploy-docs
created: "2026-06-25T17:21:46.245Z"
---

Docuseal | Dokploy

# Docuseal

Copy as Markdown

Docuseal is a self-hosted document management system.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  app:
    image: docuseal/docuseal:latest
    volumes:
      - docuseal:/data/docuseal
    depends_on:
      docu-postgres:
        condition: service_healthy
    restart: unless-stopped
    environment:
      - DATABASE_URL=postgresql://${POSTGRES_USER:-docuseal}:${POSTGRES_PASSWORD}@docu-postgres:5432/${POSTGRES_DB:-docuseal}

  docu-postgres:
    image: postgres:latest
    volumes:
      - docuseal-db:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-docuseal} -d ${POSTGRES_DB:-docuseal}"]
      interval: 10s
      timeout: 5s
      retries: 5

  docu-redis:
    image: redis:alpine
    restart: always
    volumes:
      - docuseal-redis-data:/data

volumes:
  docuseal:
  docuseal-db:
  docuseal-redis-data:
```

```
[variables]
main_domain = "${domain}"

[config]
env = [
  "POSTGRES_USER=postgres",
  "POSTGRES_PASSWORD=postgres",
  "POSTGRES_DB=docuseal",
]
mounts = []

[[config.domains]]
serviceName = "app"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBhcHA6XG4gICAgaW1hZ2U6IGRvY3VzZWFsL2RvY3VzZWFsOmxhdGVzdFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRvY3VzZWFsOi9kYXRhL2RvY3VzZWFsXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGRvY3UtcG9zdGdyZXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gREFUQUJBU0VfVVJMPXBvc3RncmVzcWw6Ly8ke1BPU1RHUkVTX1VTRVI6LWRvY3VzZWFsfToke1BPU1RHUkVTX1BBU1NXT1JEfUBkb2N1LXBvc3RncmVzOjU0MzIvJHtQT1NUR1JFU19EQjotZG9jdXNlYWx9XG4gICAgICBcbiAgZG9jdS1wb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6bGF0ZXN0XG4gICAgdm9sdW1lczpcbiAgICAgIC0gZG9jdXNlYWwtZGI6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX1VTRVI9JHtQT1NUR1JFU19VU0VSfVxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgLSBQT1NUR1JFU19EQj0ke1BPU1RHUkVTX0RCfVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5IC1VICR7UE9TVEdSRVNfVVNFUjotZG9jdXNlYWx9IC1kICR7UE9TVEdSRVNfREI6LWRvY3VzZWFsfVwiXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcbiAgICAgIFxuICBkb2N1LXJlZGlzOlxuICAgIGltYWdlOiByZWRpczphbHBpbmVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkb2N1c2VhbC1yZWRpcy1kYXRhOi9kYXRhXG4gICAgICBcbiAgICBcbnZvbHVtZXM6XG4gIGRvY3VzZWFsOlxuICBkb2N1c2VhbC1kYjpcbiAgZG9jdXNlYWwtcmVkaXMtZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICBcIlBPU1RHUkVTX1VTRVI9cG9zdGdyZXNcIixcbiAgXCJQT1NUR1JFU19QQVNTV09SRD1wb3N0Z3Jlc1wiLFxuICBcIlBPU1RHUkVTX0RCPWRvY3VzZWFsXCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhcHBcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`document-signing`

---

Version:`latest`

DocumensoDocumenso is the open source alternative to DocuSign for signing documents digitally

Dokploy Prometheus Monitoring ExtensionDokploy monitoring extension with Prometheus metrics export for external monitoring systems like Grafana Cloud. Tracks server and container metrics with configurable thresholds and alerting.

### On this page

ConfigurationBase64LinksTags