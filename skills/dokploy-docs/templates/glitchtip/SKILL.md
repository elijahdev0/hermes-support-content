---
title: "Glitchtip | Dokploy"
source: "https://docs.dokploy.com/docs/templates/glitchtip"
category: dokploy-docs
created: "2026-06-25T17:21:48.522Z"
---

Glitchtip | Dokploy

# Glitchtip

Copy as Markdown

Glitchtip is simple, open source error tracking

## Configuration

docker-compose.ymltemplate.toml

```
x-environment: &default-environment
  DATABASE_URL: postgres://postgres:postgres@postgres:5432/postgres
  SECRET_KEY: ${SECRET_KEY}
  PORT: ${GLITCHTIP_PORT}
  EMAIL_URL: consolemail://
  GLITCHTIP_DOMAIN: http://${GLITCHTIP_HOST}
  DEFAULT_FROM_EMAIL: [email protected]
  CELERY_WORKER_AUTOSCALE: "1,3"
  CELERY_WORKER_MAX_TASKS_PER_CHILD: "10000"

x-depends_on: &default-depends_on
  - postgres
  - redis

services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_HOST_AUTH_METHOD: "trust"
    restart: unless-stopped
    volumes:
      - pg-data:/var/lib/postgresql/data

  redis:
    image: redis
    restart: unless-stopped

  web:
    image: glitchtip/glitchtip:v4.0
    depends_on: *default-depends_on
    ports:
      - ${GLITCHTIP_PORT}
    environment: *default-environment
    restart: unless-stopped
    volumes:
      - uploads:/code/uploads
  worker:
    image: glitchtip/glitchtip:v4.0
    command: ./bin/run-celery-with-beat.sh
    depends_on: *default-depends_on
    environment: *default-environment
    restart: unless-stopped
    volumes:
      - uploads:/code/uploads

  migrate:
    image: glitchtip/glitchtip:v4.0
    depends_on: *default-depends_on
    command: "./manage.py migrate"
    environment: *default-environment

volumes:
  pg-data:
  uploads:
```

```
[variables]
main_domain = "${domain}"
secret_key = "${base64:32}"

[config]
env = [
  "GLITCHTIP_HOST=${main_domain}",
  "GLITCHTIP_PORT=8000",
  "SECRET_KEY=${secret_key}",
]
mounts = []

[[config.domains]]
serviceName = "web"
port = 8_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIngtZW52aXJvbm1lbnQ6ICZkZWZhdWx0LWVudmlyb25tZW50XG4gIERBVEFCQVNFX1VSTDogcG9zdGdyZXM6Ly9wb3N0Z3Jlczpwb3N0Z3Jlc0Bwb3N0Z3Jlczo1NDMyL3Bvc3RncmVzXG4gIFNFQ1JFVF9LRVk6ICR7U0VDUkVUX0tFWX1cbiAgUE9SVDogJHtHTElUQ0hUSVBfUE9SVH1cbiAgRU1BSUxfVVJMOiBjb25zb2xlbWFpbDovL1xuICBHTElUQ0hUSVBfRE9NQUlOOiBodHRwOi8vJHtHTElUQ0hUSVBfSE9TVH1cbiAgREVGQVVMVF9GUk9NX0VNQUlMOiBlbWFpbEBnbGl0Y2h0aXAuY29tXG4gIENFTEVSWV9XT1JLRVJfQVVUT1NDQUxFOiBcIjEsM1wiXG4gIENFTEVSWV9XT1JLRVJfTUFYX1RBU0tTX1BFUl9DSElMRDogXCIxMDAwMFwiXG5cbngtZGVwZW5kc19vbjogJmRlZmF1bHQtZGVwZW5kc19vblxuICAtIHBvc3RncmVzXG4gIC0gcmVkaXNcblxuc2VydmljZXM6XG4gIHBvc3RncmVzOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNlxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfSE9TVF9BVVRIX01FVEhPRDogXCJ0cnVzdFwiXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBwZy1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuXG4gIHJlZGlzOlxuICAgIGltYWdlOiByZWRpc1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgd2ViOlxuICAgIGltYWdlOiBnbGl0Y2h0aXAvZ2xpdGNodGlwOnY0LjBcbiAgICBkZXBlbmRzX29uOiAqZGVmYXVsdC1kZXBlbmRzX29uXG4gICAgcG9ydHM6XG4gICAgICAtICR7R0xJVENIVElQX1BPUlR9XG4gICAgZW52aXJvbm1lbnQ6ICpkZWZhdWx0LWVudmlyb25tZW50XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSB1cGxvYWRzOi9jb2RlL3VwbG9hZHNcbiAgd29ya2VyOlxuICAgIGltYWdlOiBnbGl0Y2h0aXAvZ2xpdGNodGlwOnY0LjBcbiAgICBjb21tYW5kOiAuL2Jpbi9ydW4tY2VsZXJ5LXdpdGgtYmVhdC5zaFxuICAgIGRlcGVuZHNfb246ICpkZWZhdWx0LWRlcGVuZHNfb25cbiAgICBlbnZpcm9ubWVudDogKmRlZmF1bHQtZW52aXJvbm1lbnRcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHVwbG9hZHM6L2NvZGUvdXBsb2Fkc1xuXG4gIG1pZ3JhdGU6XG4gICAgaW1hZ2U6IGdsaXRjaHRpcC9nbGl0Y2h0aXA6djQuMFxuICAgIGRlcGVuZHNfb246ICpkZWZhdWx0LWRlcGVuZHNfb25cbiAgICBjb21tYW5kOiBcIi4vbWFuYWdlLnB5IG1pZ3JhdGVcIlxuICAgIGVudmlyb25tZW50OiAqZGVmYXVsdC1lbnZpcm9ubWVudFxuXG5cbnZvbHVtZXM6XG4gIHBnLWRhdGE6XG4gIHVwbG9hZHM6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuc2VjcmV0X2tleSA9IFwiJHtiYXNlNjQ6MzJ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJHTElUQ0hUSVBfSE9TVD0ke21haW5fZG9tYWlufVwiLFxuICBcIkdMSVRDSFRJUF9QT1JUPTgwMDBcIixcbiAgXCJTRUNSRVRfS0VZPSR7c2VjcmV0X2tleX1cIixcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIndlYlwiXG5wb3J0ID0gOF8wMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`hosting`

---

Version:`v4.0`

GlanceA self-hosted dashboard that puts all your feeds in one place. Features RSS feeds, weather, bookmarks, site monitoring, and more in a minimal, fast interface.

GLPI ProjectThe most complete open source service management software

### On this page

ConfigurationBase64LinksTags