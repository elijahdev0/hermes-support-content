---
title: "Domain Locker | Dokploy"
source: "https://docs.dokploy.com/docs/templates/domain-locker"
category: dokploy-docs
created: "2026-06-25T17:21:46.245Z"
---

Domain Locker | Dokploy

# Domain Locker

Copy as Markdown

Domain Locker is an open-source tool for tracking domain expirations and sending renewal reminders.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  postgres:
    image: postgres:15-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${DL_PG_NAME:-domain_locker}
      POSTGRES_USER: ${DL_PG_USER:-postgres}
      POSTGRES_PASSWORD: ${DL_PG_PASSWORD:-changeme2420}
    expose:
      - "5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      # - ./db/schema.sql:/docker-entrypoint-initdb.d/init-schema.sql:ro
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DL_PG_USER:-postgres}"]
      interval: 5s
      timeout: 3s
      retries: 10

  app:
    image: lissy93/domain-locker:latest
    restart: unless-stopped
    environment:
      NODE_ENV: "production"
      DL_ENV_TYPE: ${DL_ENV_TYPE:-selfHosted}
      DL_PG_HOST: ${DL_PG_HOST:-postgres}
      DL_PG_PORT: ${DL_PG_PORT:-5432}
      DL_PG_USER: ${DL_PG_USER:-postgres}
      DL_PG_PASSWORD: ${DL_PG_PASSWORD:-changeme2420}
      DL_PG_NAME: ${DL_PG_NAME:-domain_locker}
    expose:
      - "3000"
    depends_on:
      - postgres

  updater:
    image: alpine:3.20
    restart: unless-stopped
    depends_on:
      - app
    command: >
      /bin/sh -c "
        apk add --no-cache curl &&
        echo '0 3 * * * /usr/bin/curl -s -X POST http://app:3000/api/domain-updater' > /etc/crontabs/root &&
        echo '0 4 * * * /usr/bin/curl -s -X POST http://app:3000/api/expiration-reminders' >> /etc/crontabs/root &&
        crond -f -L /dev/stdout
      "

volumes:
  postgres_data: {}
```

```
[variables]
main_domain = "${domain}"
pg_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "app"
port = 3000
host = "${main_domain}"

[config.env]
NODE_ENV = "production"
DL_ENV_TYPE = "selfHosted"
DL_PG_HOST = "postgres"
DL_PG_PORT = "5432"
DL_PG_USER = "postgres"
DL_PG_PASSWORD = "${pg_password}"
DL_PG_NAME = "domain_locker"

# OPTIONAL ENV VARS (uncomment as needed)
# DL_BASE_URL = "http://localhost:3000"
# DL_TURNSTILE_KEY = ""
# DL_GLITCHTIP_DSN = ""
# DL_PLAUSIBLE_URL = ""
# DL_PLAUSIBLE_SITE = ""
# DL_DOMAIN_INFO_API = ""
# DL_DOMAIN_SUBS_API = ""
# DL_DISABLE_WRITE_METHODS = "false"

[[config.mounts]]
# Example mount for PostgreSQL persistence (already defined in compose volumes)
# filePath = "/var/lib/postgresql/data"
# content = ""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHBvc3RncmVzOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNS1hbHBpbmVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6ICR7RExfUEdfTkFNRTotZG9tYWluX2xvY2tlcn1cbiAgICAgIFBPU1RHUkVTX1VTRVI6ICR7RExfUEdfVVNFUjotcG9zdGdyZXN9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtETF9QR19QQVNTV09SRDotY2hhbmdlbWUyNDIwfVxuICAgIGV4cG9zZTpcbiAgICAgIC0gXCI1NDMyXCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlc19kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgICAgIyAtIC4vZGIvc2NoZW1hLnNxbDovZG9ja2VyLWVudHJ5cG9pbnQtaW5pdGRiLmQvaW5pdC1zY2hlbWEuc3FsOnJvXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5IC1VICR7RExfUEdfVVNFUjotcG9zdGdyZXN9XCJdXG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHRpbWVvdXQ6IDNzXG4gICAgICByZXRyaWVzOiAxMFxuXG4gIGFwcDpcbiAgICBpbWFnZTogbGlzc3k5My9kb21haW4tbG9ja2VyOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBOT0RFX0VOVjogXCJwcm9kdWN0aW9uXCJcbiAgICAgIERMX0VOVl9UWVBFOiAke0RMX0VOVl9UWVBFOi1zZWxmSG9zdGVkfVxuICAgICAgRExfUEdfSE9TVDogJHtETF9QR19IT1NUOi1wb3N0Z3Jlc31cbiAgICAgIERMX1BHX1BPUlQ6ICR7RExfUEdfUE9SVDotNTQzMn1cbiAgICAgIERMX1BHX1VTRVI6ICR7RExfUEdfVVNFUjotcG9zdGdyZXN9XG4gICAgICBETF9QR19QQVNTV09SRDogJHtETF9QR19QQVNTV09SRDotY2hhbmdlbWUyNDIwfVxuICAgICAgRExfUEdfTkFNRTogJHtETF9QR19OQU1FOi1kb21haW5fbG9ja2VyfVxuICAgIGV4cG9zZTpcbiAgICAgIC0gXCIzMDAwXCJcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBwb3N0Z3Jlc1xuXG4gIHVwZGF0ZXI6XG4gICAgaW1hZ2U6IGFscGluZTozLjIwXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBhcHBcbiAgICBjb21tYW5kOiA+XG4gICAgICAvYmluL3NoIC1jIFwiXG4gICAgICAgIGFwayBhZGQgLS1uby1jYWNoZSBjdXJsICYmXG4gICAgICAgIGVjaG8gJzAgMyAqICogKiAvdXNyL2Jpbi9jdXJsIC1zIC1YIFBPU1QgaHR0cDovL2FwcDozMDAwL2FwaS9kb21haW4tdXBkYXRlcicgPiAvZXRjL2Nyb250YWJzL3Jvb3QgJiZcbiAgICAgICAgZWNobyAnMCA0ICogKiAqIC91c3IvYmluL2N1cmwgLXMgLVggUE9TVCBodHRwOi8vYXBwOjMwMDAvYXBpL2V4cGlyYXRpb24tcmVtaW5kZXJzJyA+PiAvZXRjL2Nyb250YWJzL3Jvb3QgJiZcbiAgICAgICAgY3JvbmQgLWYgLUwgL2Rldi9zdGRvdXRcbiAgICAgIFwiXG5cbnZvbHVtZXM6XG4gIHBvc3RncmVzX2RhdGE6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucGdfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFwcFwiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbk5PREVfRU5WID0gXCJwcm9kdWN0aW9uXCJcbkRMX0VOVl9UWVBFID0gXCJzZWxmSG9zdGVkXCJcbkRMX1BHX0hPU1QgPSBcInBvc3RncmVzXCJcbkRMX1BHX1BPUlQgPSBcIjU0MzJcIlxuRExfUEdfVVNFUiA9IFwicG9zdGdyZXNcIlxuRExfUEdfUEFTU1dPUkQgPSBcIiR7cGdfcGFzc3dvcmR9XCJcbkRMX1BHX05BTUUgPSBcImRvbWFpbl9sb2NrZXJcIlxuXG4jIE9QVElPTkFMIEVOViBWQVJTICh1bmNvbW1lbnQgYXMgbmVlZGVkKVxuIyBETF9CQVNFX1VSTCA9IFwiaHR0cDovL2xvY2FsaG9zdDozMDAwXCJcbiMgRExfVFVSTlNUSUxFX0tFWSA9IFwiXCJcbiMgRExfR0xJVENIVElQX0RTTiA9IFwiXCJcbiMgRExfUExBVVNJQkxFX1VSTCA9IFwiXCJcbiMgRExfUExBVVNJQkxFX1NJVEUgPSBcIlwiXG4jIERMX0RPTUFJTl9JTkZPX0FQSSA9IFwiXCJcbiMgRExfRE9NQUlOX1NVQlNfQVBJID0gXCJcIlxuIyBETF9ESVNBQkxFX1dSSVRFX01FVEhPRFMgPSBcImZhbHNlXCJcblxuW1tjb25maWcubW91bnRzXV1cbiMgRXhhbXBsZSBtb3VudCBmb3IgUG9zdGdyZVNRTCBwZXJzaXN0ZW5jZSAoYWxyZWFkeSBkZWZpbmVkIGluIGNvbXBvc2Ugdm9sdW1lcylcbiMgZmlsZVBhdGggPSBcIi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVwiXG4jIGNvbnRlbnQgPSBcIlwiXG4iCn0=
```

## Links

`domains`,`monitoring`,`utilities`,`postgres`

---

Version:`latest`

DolibarrDolibarr ERP & CRM is a modern software package that helps manage your organization's activities (contacts, quotes, invoices, orders, stocks, agenda, human resources, ecm, manufacturing).

Double Zero00 is a self hostable SES dashboard for sending and monitoring emails with AWS

### On this page

ConfigurationBase64LinksTags