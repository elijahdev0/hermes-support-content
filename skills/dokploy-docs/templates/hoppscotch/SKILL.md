---
title: "Hoppscotch (AIO + Migrations) | Dokploy"
source: "https://docs.dokploy.com/docs/templates/hoppscotch"
category: dokploy-docs
created: "2026-06-25T17:21:49.750Z"
---

Hoppscotch (AIO + Migrations) | Dokploy

# Hoppscotch (AIO + Migrations)

Copy as Markdown

Hoppscotch Community Edition (All-in-One) with automatic database migrations. Includes backend, frontend, and admin under unified subpath routing.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  hoppscotch:
    image: hoppscotch/hoppscotch:latest
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
      migrate:
        condition: service_completed_successfully
    expose:
      - 80
    environment:
      # Database
      DATABASE_URL: "${DATABASE_URL}"
      DATA_ENCRYPTION_KEY: "${DATA_ENCRYPTION_KEY}"
      HOPP_AIO_ALTERNATE_PORT: "${HOPP_AIO_ALTERNATE_PORT}"
      WHITELISTED_ORIGINS: "${WHITELISTED_ORIGINS}"

      # Frontend config
      VITE_BASE_URL: "${VITE_BASE_URL}"
      VITE_SHORTCODE_BASE_URL: "${VITE_SHORTCODE_BASE_URL}"
      VITE_ADMIN_URL: "${VITE_ADMIN_URL}"

      # Backend config
      VITE_BACKEND_GQL_URL: "${VITE_BACKEND_GQL_URL}"
      VITE_BACKEND_WS_URL: "${VITE_BACKEND_WS_URL}"
      VITE_BACKEND_API_URL: "${VITE_BACKEND_API_URL}"

      # Optional UI links
      VITE_APP_TOS_LINK: "${VITE_APP_TOS_LINK}"
      VITE_APP_PRIVACY_POLICY_LINK: "${VITE_APP_PRIVACY_POLICY_LINK}"

      # Subpath access
      ENABLE_SUBPATH_BASED_ACCESS: "true"

    volumes:
      - hoppscotch-data:/app/data

  postgres:
    image: postgres:16
    restart: unless-stopped
    expose:
      - 5432
    environment:
      POSTGRES_DB: "${POSTGRES_DB}"
      POSTGRES_USER: "${POSTGRES_USER}"
      POSTGRES_PASSWORD: "${POSTGRES_PASSWORD}"
    volumes:
      - hoppscotch-postgres:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 5

  migrate:
    image: hoppscotch/hoppscotch:latest
    depends_on:
      postgres:
        condition: service_healthy
    entrypoint: ["/bin/sh", "-c"]
    command:
      - |
        echo "Running database migrations..."
        pnpm dlx prisma migrate deploy && echo "Migration complete!"
    environment:
      DATABASE_URL: "${DATABASE_URL}"
    restart: "no"

volumes:
  hoppscotch-data:
  hoppscotch-postgres:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:32}"
encryption_key = "${password:32}"

[config]

[[config.domains]]
serviceName = "hoppscotch"
port = 80
host = "${main_domain}"
path = "/"

[config.env]
# Database & Encryption
POSTGRES_DB = "hoppscotch"
POSTGRES_USER = "hoppscotch"
POSTGRES_PASSWORD = "${db_password}"
DATABASE_URL = "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}"
DATA_ENCRYPTION_KEY = "${encryption_key}"

# AIO Port
HOPP_AIO_ALTERNATE_PORT = "80"

# Whitelist / Routing
WHITELISTED_ORIGINS = "https://${main_domain},http://${main_domain},app://hoppscotch"
VITE_BASE_URL = "https://${main_domain}"
VITE_SHORTCODE_BASE_URL = "https://${main_domain}"
VITE_ADMIN_URL = "https://${main_domain}/admin"
VITE_BACKEND_GQL_URL = "https://${main_domain}/backend/graphql"
VITE_BACKEND_WS_URL = "wss://${main_domain}/backend/graphql"
VITE_BACKEND_API_URL = "https://${main_domain}/backend/v1"

# Legal Links
VITE_APP_TOS_LINK = "https://docs.hoppscotch.io/support/terms"
VITE_APP_PRIVACY_POLICY_LINK = "https://docs.hoppscotch.io/support/privacy"

# Subpath Access
ENABLE_SUBPATH_BASED_ACCESS = "true"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGhvcHBzY290Y2g6XG4gICAgaW1hZ2U6IGhvcHBzY290Y2gvaG9wcHNjb3RjaDpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGRlcGVuZHNfb246XG4gICAgICBwb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICAgIG1pZ3JhdGU6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9jb21wbGV0ZWRfc3VjY2Vzc2Z1bGx5XG4gICAgZXhwb3NlOlxuICAgICAgLSA4MFxuICAgIGVudmlyb25tZW50OlxuICAgICAgIyBEYXRhYmFzZVxuICAgICAgREFUQUJBU0VfVVJMOiBcIiR7REFUQUJBU0VfVVJMfVwiXG4gICAgICBEQVRBX0VOQ1JZUFRJT05fS0VZOiBcIiR7REFUQV9FTkNSWVBUSU9OX0tFWX1cIlxuICAgICAgSE9QUF9BSU9fQUxURVJOQVRFX1BPUlQ6IFwiJHtIT1BQX0FJT19BTFRFUk5BVEVfUE9SVH1cIlxuICAgICAgV0hJVEVMSVNURURfT1JJR0lOUzogXCIke1dISVRFTElTVEVEX09SSUdJTlN9XCJcblxuICAgICAgIyBGcm9udGVuZCBjb25maWdcbiAgICAgIFZJVEVfQkFTRV9VUkw6IFwiJHtWSVRFX0JBU0VfVVJMfVwiXG4gICAgICBWSVRFX1NIT1JUQ09ERV9CQVNFX1VSTDogXCIke1ZJVEVfU0hPUlRDT0RFX0JBU0VfVVJMfVwiXG4gICAgICBWSVRFX0FETUlOX1VSTDogXCIke1ZJVEVfQURNSU5fVVJMfVwiXG5cbiAgICAgICMgQmFja2VuZCBjb25maWdcbiAgICAgIFZJVEVfQkFDS0VORF9HUUxfVVJMOiBcIiR7VklURV9CQUNLRU5EX0dRTF9VUkx9XCJcbiAgICAgIFZJVEVfQkFDS0VORF9XU19VUkw6IFwiJHtWSVRFX0JBQ0tFTkRfV1NfVVJMfVwiXG4gICAgICBWSVRFX0JBQ0tFTkRfQVBJX1VSTDogXCIke1ZJVEVfQkFDS0VORF9BUElfVVJMfVwiXG5cbiAgICAgICMgT3B0aW9uYWwgVUkgbGlua3NcbiAgICAgIFZJVEVfQVBQX1RPU19MSU5LOiBcIiR7VklURV9BUFBfVE9TX0xJTkt9XCJcbiAgICAgIFZJVEVfQVBQX1BSSVZBQ1lfUE9MSUNZX0xJTks6IFwiJHtWSVRFX0FQUF9QUklWQUNZX1BPTElDWV9MSU5LfVwiXG5cbiAgICAgICMgU3VicGF0aCBhY2Nlc3NcbiAgICAgIEVOQUJMRV9TVUJQQVRIX0JBU0VEX0FDQ0VTUzogXCJ0cnVlXCJcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGhvcHBzY290Y2gtZGF0YTovYXBwL2RhdGFcblxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTZcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGV4cG9zZTpcbiAgICAgIC0gNTQzMlxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6IFwiJHtQT1NUR1JFU19EQn1cIlxuICAgICAgUE9TVEdSRVNfVVNFUjogXCIke1BPU1RHUkVTX1VTRVJ9XCJcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiBcIiR7UE9TVEdSRVNfUEFTU1dPUkR9XCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBob3Bwc2NvdGNoLXBvc3RncmVzOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSAke1BPU1RHUkVTX1VTRVJ9IC1kICR7UE9TVEdSRVNfREJ9XCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuXG4gIG1pZ3JhdGU6XG4gICAgaW1hZ2U6IGhvcHBzY290Y2gvaG9wcHNjb3RjaDpsYXRlc3RcbiAgICBkZXBlbmRzX29uOlxuICAgICAgcG9zdGdyZXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW50cnlwb2ludDogW1wiL2Jpbi9zaFwiLCBcIi1jXCJdXG4gICAgY29tbWFuZDpcbiAgICAgIC0gfFxuICAgICAgICBlY2hvIFwiUnVubmluZyBkYXRhYmFzZSBtaWdyYXRpb25zLi4uXCJcbiAgICAgICAgcG5wbSBkbHggcHJpc21hIG1pZ3JhdGUgZGVwbG95ICYmIGVjaG8gXCJNaWdyYXRpb24gY29tcGxldGUhXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERBVEFCQVNFX1VSTDogXCIke0RBVEFCQVNFX1VSTH1cIlxuICAgIHJlc3RhcnQ6IFwibm9cIlxuXG52b2x1bWVzOlxuICBob3Bwc2NvdGNoLWRhdGE6XG4gIGhvcHBzY290Y2gtcG9zdGdyZXM6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmVuY3J5cHRpb25fa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImhvcHBzY290Y2hcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5wYXRoID0gXCIvXCJcblxuW2NvbmZpZy5lbnZdXG4jIERhdGFiYXNlICYgRW5jcnlwdGlvblxuUE9TVEdSRVNfREIgPSBcImhvcHBzY290Y2hcIlxuUE9TVEdSRVNfVVNFUiA9IFwiaG9wcHNjb3RjaFwiXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtkYl9wYXNzd29yZH1cIlxuREFUQUJBU0VfVVJMID0gXCJwb3N0Z3Jlc3FsOi8vJHtQT1NUR1JFU19VU0VSfToke1BPU1RHUkVTX1BBU1NXT1JEfUBwb3N0Z3Jlczo1NDMyLyR7UE9TVEdSRVNfREJ9XCJcbkRBVEFfRU5DUllQVElPTl9LRVkgPSBcIiR7ZW5jcnlwdGlvbl9rZXl9XCJcblxuIyBBSU8gUG9ydFxuSE9QUF9BSU9fQUxURVJOQVRFX1BPUlQgPSBcIjgwXCJcblxuIyBXaGl0ZWxpc3QgLyBSb3V0aW5nXG5XSElURUxJU1RFRF9PUklHSU5TID0gXCJodHRwczovLyR7bWFpbl9kb21haW59LGh0dHA6Ly8ke21haW5fZG9tYWlufSxhcHA6Ly9ob3Bwc2NvdGNoXCJcblZJVEVfQkFTRV9VUkwgPSBcImh0dHBzOi8vJHttYWluX2RvbWFpbn1cIlxuVklURV9TSE9SVENPREVfQkFTRV9VUkwgPSBcImh0dHBzOi8vJHttYWluX2RvbWFpbn1cIlxuVklURV9BRE1JTl9VUkwgPSBcImh0dHBzOi8vJHttYWluX2RvbWFpbn0vYWRtaW5cIlxuVklURV9CQUNLRU5EX0dRTF9VUkwgPSBcImh0dHBzOi8vJHttYWluX2RvbWFpbn0vYmFja2VuZC9ncmFwaHFsXCJcblZJVEVfQkFDS0VORF9XU19VUkwgPSBcIndzczovLyR7bWFpbl9kb21haW59L2JhY2tlbmQvZ3JhcGhxbFwiXG5WSVRFX0JBQ0tFTkRfQVBJX1VSTCA9IFwiaHR0cHM6Ly8ke21haW5fZG9tYWlufS9iYWNrZW5kL3YxXCJcblxuIyBMZWdhbCBMaW5rc1xuVklURV9BUFBfVE9TX0xJTksgPSBcImh0dHBzOi8vZG9jcy5ob3Bwc2NvdGNoLmlvL3N1cHBvcnQvdGVybXNcIlxuVklURV9BUFBfUFJJVkFDWV9QT0xJQ1lfTElOSyA9IFwiaHR0cHM6Ly9kb2NzLmhvcHBzY290Y2guaW8vc3VwcG9ydC9wcml2YWN5XCJcblxuIyBTdWJwYXRoIEFjY2Vzc1xuRU5BQkxFX1NVQlBBVEhfQkFTRURfQUNDRVNTID0gXCJ0cnVlXCJcblxuW1tjb25maWcubW91bnRzXV0iCn0=
```

## Links

`api`,`testing`,`development`,`postman-alternative`,`graphql`

---

Version:`latest`

HomebridgeBringing HomeKit support where there is none. Homebridge allows you to integrate with smart home devices that do not natively support HomeKit.

HortusFoxHortusFox is an open source task and photo management app, designed for photographers and creatives to manage projects, tasks, and images effectively.

### On this page

ConfigurationBase64LinksTags