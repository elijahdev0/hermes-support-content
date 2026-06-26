---
title: "Inngest | Dokploy"
source: "https://docs.dokploy.com/docs/templates/inngest"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

Inngest | Dokploy

# Inngest

Copy as Markdown

Inngest is a developer platform for serverless event-driven workflows. Build reliable, scalable background functions and workflows with built-in retries, scheduling, and observability.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  inngest:
    image: inngest/inngest:v1.12.1
    restart: unless-stopped
    command: >
      inngest start
      --host 0.0.0.0
      --port 8288
      --event-key ${INNGEST_EVENT_KEY}
      --signing-key ${INNGEST_SIGNING_KEY}
      --postgres-uri ${INNGEST_POSTGRES_URI}
      --redis-uri ${INNGEST_REDIS_URI}
      --poll-interval ${INNGEST_POLL_INTERVAL:-60}
      --queue-workers ${INNGEST_QUEUE_WORKERS:-100}
    environment:
      # Core Configuration
      - INNGEST_PORT=8288
      - INNGEST_HOST=0.0.0.0
      - INNGEST_EVENT_KEY=${INNGEST_EVENT_KEY}
      - INNGEST_SIGNING_KEY=${INNGEST_SIGNING_KEY}

      # Database & Cache
      - INNGEST_POSTGRES_URI=${INNGEST_POSTGRES_URI}
      - INNGEST_REDIS_URI=${INNGEST_REDIS_URI}

      # Performance Tuning
      - INNGEST_POLL_INTERVAL=${INNGEST_POLL_INTERVAL:-60}
      - INNGEST_QUEUE_WORKERS=${INNGEST_QUEUE_WORKERS:-100}
      - INNGEST_RETRY_INTERVAL=${INNGEST_RETRY_INTERVAL:-1}
      - INNGEST_TICK=${INNGEST_TICK:-150}

      # Logging
      - INNGEST_LOG_LEVEL=${INNGEST_LOG_LEVEL:-info}
      - INNGEST_JSON=${INNGEST_JSON:-false}
      - INNGEST_VERBOSE=${INNGEST_VERBOSE:-false}
    ports:
      - 8288
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - inngest_data:/home/inngest/.inngest
    healthcheck:
      test: ['CMD', 'curl', '-f', 'http://localhost:8288/health']
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s

  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_INITDB_ARGS=--encoding=UTF-8 --lc-collate=C --lc-ctype=C
      - PGUSER=${POSTGRES_USER}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - 5432
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}']
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    command: redis-server --appendonly yes --maxmemory 512mb --maxmemory-policy allkeys-lru --save 60 1000
    sysctls:
      - net.core.somaxconn=1024
    volumes:
      - redis_data:/data
    ports:
      - 6379
    healthcheck:
      test: ['CMD', 'redis-cli', 'ping']
      interval: 10s
      timeout: 3s
      retries: 3

volumes:
  inngest_data:
  postgres_data:
  redis_data:
```

```
[variables]
main_domain = "${domain}"
event_key = "${jwt:32}" # Must be hex string with even number of chars
signing_key = "${jwt:32}" # Must be hex string with even number of chars
postgres_password = "${password:24}"

[config]
mounts = []

[[config.domains]]
serviceName = "inngest"
port = 8_288
host = "${main_domain}"

[config.env]
# Production Inngest Authentication Keys
INNGEST_EVENT_KEY = "${event_key}"
INNGEST_SIGNING_KEY = "${signing_key}"

# Database Configuration
INNGEST_POSTGRES_URI = "postgresql://inngest:${postgres_password}@postgres:5432/inngest?sslmode=disable"
POSTGRES_DB = "inngest"
POSTGRES_USER = "inngest"
POSTGRES_PASSWORD = "${postgres_password}"

# Redis Configuration
INNGEST_REDIS_URI = "redis://redis:6379"

# Performance & Scaling Configuration
INNGEST_POLL_INTERVAL = "60"
INNGEST_QUEUE_WORKERS = "100"
INNGEST_RETRY_INTERVAL = "1"
INNGEST_TICK = "150"

# Logging Configuration
INNGEST_LOG_LEVEL = "info"
INNGEST_JSON = "true"
INNGEST_VERBOSE = "false"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBpbm5nZXN0OlxuICAgIGltYWdlOiBpbm5nZXN0L2lubmdlc3Q6djEuMTIuMVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgY29tbWFuZDogPlxuICAgICAgaW5uZ2VzdCBzdGFydFxuICAgICAgLS1ob3N0IDAuMC4wLjBcbiAgICAgIC0tcG9ydCA4Mjg4XG4gICAgICAtLWV2ZW50LWtleSAke0lOTkdFU1RfRVZFTlRfS0VZfVxuICAgICAgLS1zaWduaW5nLWtleSAke0lOTkdFU1RfU0lHTklOR19LRVl9XG4gICAgICAtLXBvc3RncmVzLXVyaSAke0lOTkdFU1RfUE9TVEdSRVNfVVJJfVxuICAgICAgLS1yZWRpcy11cmkgJHtJTk5HRVNUX1JFRElTX1VSSX1cbiAgICAgIC0tcG9sbC1pbnRlcnZhbCAke0lOTkdFU1RfUE9MTF9JTlRFUlZBTDotNjB9XG4gICAgICAtLXF1ZXVlLXdvcmtlcnMgJHtJTk5HRVNUX1FVRVVFX1dPUktFUlM6LTEwMH1cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgQ29yZSBDb25maWd1cmF0aW9uXG4gICAgICAtIElOTkdFU1RfUE9SVD04Mjg4XG4gICAgICAtIElOTkdFU1RfSE9TVD0wLjAuMC4wXG4gICAgICAtIElOTkdFU1RfRVZFTlRfS0VZPSR7SU5OR0VTVF9FVkVOVF9LRVl9XG4gICAgICAtIElOTkdFU1RfU0lHTklOR19LRVk9JHtJTk5HRVNUX1NJR05JTkdfS0VZfVxuXG4gICAgICAjIERhdGFiYXNlICYgQ2FjaGVcbiAgICAgIC0gSU5OR0VTVF9QT1NUR1JFU19VUkk9JHtJTk5HRVNUX1BPU1RHUkVTX1VSSX1cbiAgICAgIC0gSU5OR0VTVF9SRURJU19VUkk9JHtJTk5HRVNUX1JFRElTX1VSSX1cblxuICAgICAgIyBQZXJmb3JtYW5jZSBUdW5pbmdcbiAgICAgIC0gSU5OR0VTVF9QT0xMX0lOVEVSVkFMPSR7SU5OR0VTVF9QT0xMX0lOVEVSVkFMOi02MH1cbiAgICAgIC0gSU5OR0VTVF9RVUVVRV9XT1JLRVJTPSR7SU5OR0VTVF9RVUVVRV9XT1JLRVJTOi0xMDB9XG4gICAgICAtIElOTkdFU1RfUkVUUllfSU5URVJWQUw9JHtJTk5HRVNUX1JFVFJZX0lOVEVSVkFMOi0xfVxuICAgICAgLSBJTk5HRVNUX1RJQ0s9JHtJTk5HRVNUX1RJQ0s6LTE1MH1cblxuICAgICAgIyBMb2dnaW5nXG4gICAgICAtIElOTkdFU1RfTE9HX0xFVkVMPSR7SU5OR0VTVF9MT0dfTEVWRUw6LWluZm99XG4gICAgICAtIElOTkdFU1RfSlNPTj0ke0lOTkdFU1RfSlNPTjotZmFsc2V9XG4gICAgICAtIElOTkdFU1RfVkVSQk9TRT0ke0lOTkdFU1RfVkVSQk9TRTotZmFsc2V9XG4gICAgcG9ydHM6XG4gICAgICAtIDgyODhcbiAgICBkZXBlbmRzX29uOlxuICAgICAgcG9zdGdyZXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgICByZWRpczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICB2b2x1bWVzOlxuICAgICAgLSBpbm5nZXN0X2RhdGE6L2hvbWUvaW5uZ2VzdC8uaW5uZ2VzdFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogWydDTUQnLCAnY3VybCcsICctZicsICdodHRwOi8vbG9jYWxob3N0OjgyODgvaGVhbHRoJ11cbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogM1xuICAgICAgc3RhcnRfcGVyaW9kOiAzMHNcblxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTYtYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfREI9JHtQT1NUR1JFU19EQn1cbiAgICAgIC0gUE9TVEdSRVNfVVNFUj0ke1BPU1RHUkVTX1VTRVJ9XG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPSR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICAtIFBPU1RHUkVTX0lOSVREQl9BUkdTPS0tZW5jb2Rpbmc9VVRGLTggLS1sYy1jb2xsYXRlPUMgLS1sYy1jdHlwZT1DXG4gICAgICAtIFBHVVNFUj0ke1BPU1RHUkVTX1VTRVJ9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gcG9zdGdyZXNfZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBwb3J0czpcbiAgICAgIC0gNTQzMlxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogWydDTUQtU0hFTEwnLCAncGdfaXNyZWFkeSAtVSAke1BPU1RHUkVTX1VTRVJ9IC1kICR7UE9TVEdSRVNfREJ9J11cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG5cbiAgcmVkaXM6XG4gICAgaW1hZ2U6IHJlZGlzOjctYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBjb21tYW5kOiByZWRpcy1zZXJ2ZXIgLS1hcHBlbmRvbmx5IHllcyAtLW1heG1lbW9yeSA1MTJtYiAtLW1heG1lbW9yeS1wb2xpY3kgYWxsa2V5cy1scnUgLS1zYXZlIDYwIDEwMDBcbiAgICBzeXNjdGxzOlxuICAgICAgLSBuZXQuY29yZS5zb21heGNvbm49MTAyNFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHJlZGlzX2RhdGE6L2RhdGFcbiAgICBwb3J0czpcbiAgICAgIC0gNjM3OVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogWydDTUQnLCAncmVkaXMtY2xpJywgJ3BpbmcnXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogM3NcbiAgICAgIHJldHJpZXM6IDNcblxudm9sdW1lczpcbiAgaW5uZ2VzdF9kYXRhOlxuICBwb3N0Z3Jlc19kYXRhOlxuICByZWRpc19kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmV2ZW50X2tleSA9IFwiJHtqd3Q6MzJ9XCIgIyBNdXN0IGJlIGhleCBzdHJpbmcgd2l0aCBldmVuIG51bWJlciBvZiBjaGFyc1xuc2lnbmluZ19rZXkgPSBcIiR7and0OjMyfVwiICMgTXVzdCBiZSBoZXggc3RyaW5nIHdpdGggZXZlbiBudW1iZXIgb2YgY2hhcnNcbnBvc3RncmVzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjI0fVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJpbm5nZXN0XCJcbnBvcnQgPSA4XzI4OFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbiMgUHJvZHVjdGlvbiBJbm5nZXN0IEF1dGhlbnRpY2F0aW9uIEtleXNcbklOTkdFU1RfRVZFTlRfS0VZID0gXCIke2V2ZW50X2tleX1cIlxuSU5OR0VTVF9TSUdOSU5HX0tFWSA9IFwiJHtzaWduaW5nX2tleX1cIlxuXG4jIERhdGFiYXNlIENvbmZpZ3VyYXRpb25cbklOTkdFU1RfUE9TVEdSRVNfVVJJID0gXCJwb3N0Z3Jlc3FsOi8vaW5uZ2VzdDoke3Bvc3RncmVzX3Bhc3N3b3JkfUBwb3N0Z3Jlczo1NDMyL2lubmdlc3Q/c3NsbW9kZT1kaXNhYmxlXCJcblBPU1RHUkVTX0RCID0gXCJpbm5nZXN0XCJcblBPU1RHUkVTX1VTRVIgPSBcImlubmdlc3RcIlxuUE9TVEdSRVNfUEFTU1dPUkQgPSBcIiR7cG9zdGdyZXNfcGFzc3dvcmR9XCJcblxuIyBSZWRpcyBDb25maWd1cmF0aW9uXG5JTk5HRVNUX1JFRElTX1VSSSA9IFwicmVkaXM6Ly9yZWRpczo2Mzc5XCJcblxuIyBQZXJmb3JtYW5jZSAmIFNjYWxpbmcgQ29uZmlndXJhdGlvblxuSU5OR0VTVF9QT0xMX0lOVEVSVkFMID0gXCI2MFwiXG5JTk5HRVNUX1FVRVVFX1dPUktFUlMgPSBcIjEwMFwiXG5JTk5HRVNUX1JFVFJZX0lOVEVSVkFMID0gXCIxXCJcbklOTkdFU1RfVElDSyA9IFwiMTUwXCJcblxuIyBMb2dnaW5nIENvbmZpZ3VyYXRpb25cbklOTkdFU1RfTE9HX0xFVkVMID0gXCJpbmZvXCJcbklOTkdFU1RfSlNPTiA9IFwidHJ1ZVwiXG5JTk5HRVNUX1ZFUkJPU0UgPSBcImZhbHNlXCJcbiIKfQ==
```

## Links

`workflow`,`automation`,`self-hosted`,`serverless`,`events`

---

Version:`v1.12.1`

InfluxDBInfluxDB 2.7 is the platform purpose-built to collect, store, process and visualize time series data.

InstantDBInstantDB is a real-time database server that provides instant data synchronization and real-time updates for applications.

### On this page

ConfigurationBase64LinksTags