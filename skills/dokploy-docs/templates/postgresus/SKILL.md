---
title: "Postgresus | Dokploy"
source: "https://docs.dokploy.com/docs/templates/postgresus"
category: dokploy-docs
created: "2026-06-25T17:21:56.648Z"
---

Postgresus | Dokploy

# Postgresus

Copy as Markdown

Free, open source and self-hosted solution for automated PostgreSQL backups. With multiple storage options and notifications

## Configuration

docker-compose.ymltemplate.toml

```
services:
  postgresus:
    image: rostislavdugin/postgresus:latest
    ports:
      - "4005"
    volumes:
      # Persistent data storage
      - postgresus-data:/postgresus-data
    restart: unless-stopped
    environment:
      # Optional: Set timezone
      - TZ=UTC
    healthcheck:
      test: [ "CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:4005" ]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

volumes:
  postgresus-data:
    driver: local
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "postgresus"
port = 4005
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwb3N0Z3Jlc3VzOlxuICAgIGltYWdlOiByb3N0aXNsYXZkdWdpbi9wb3N0Z3Jlc3VzOmxhdGVzdFxuICAgIHBvcnRzOlxuICAgICAgLSBcIjQwMDVcIlxuICAgIHZvbHVtZXM6XG4gICAgICAjIFBlcnNpc3RlbnQgZGF0YSBzdG9yYWdlXG4gICAgICAtIHBvc3RncmVzdXMtZGF0YTovcG9zdGdyZXN1cy1kYXRhXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgT3B0aW9uYWw6IFNldCB0aW1lem9uZVxuICAgICAgLSBUWj1VVENcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFsgXCJDTURcIiwgXCJ3Z2V0XCIsIFwiLS1uby12ZXJib3NlXCIsIFwiLS10cmllcz0xXCIsIFwiLS1zcGlkZXJcIiwgXCJodHRwOi8vbG9jYWxob3N0OjQwMDVcIiBdXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDNcbiAgICAgIHN0YXJ0X3BlcmlvZDogNDBzXG5cbnZvbHVtZXM6XG4gIHBvc3RncmVzdXMtZGF0YTpcbiAgICBkcml2ZXI6IGxvY2FsXG5cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicG9zdGdyZXN1c1wiXG5wb3J0ID0gNDAwNVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`postgres`,`backup`,`s3`

---

Version:`latest`

PostgreSQL with PgDogPostgreSQL database with PgDog connection pooler, load balancer, and horizontal scaling proxy. A modern alternative to PgBouncer with multi-threading support.

PostizPostiz is a modern, open-source platform for managing and publishing content across multiple channels.

### On this page

ConfigurationBase64LinksTags