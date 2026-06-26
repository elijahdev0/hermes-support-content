---
title: "Activepieces | Dokploy"
source: "https://docs.dokploy.com/docs/templates/activepieces"
category: dokploy-docs
created: "2026-06-25T17:21:40.413Z"
---

Activepieces | Dokploy

# Activepieces

Copy as Markdown

Open-source no-code business automation tool. An alternative to Zapier, Make.com, and Tray.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  activepieces:
    image: activepieces/activepieces:0.35.0
    restart: unless-stopped

    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      AP_ENGINE_EXECUTABLE_PATH: dist/packages/engine/main.js
      AP_API_KEY: ${AP_API_KEY}
      AP_ENCRYPTION_KEY: ${AP_ENCRYPTION_KEY}
      AP_JWT_SECRET: ${AP_JWT_SECRET}
      AP_ENVIRONMENT: prod
      AP_FRONTEND_URL: https://${AP_HOST}
      AP_WEBHOOK_TIMEOUT_SECONDS: 30
      AP_TRIGGER_DEFAULT_POLL_INTERVAL: 5
      AP_POSTGRES_DATABASE: activepieces
      AP_POSTGRES_HOST: postgres
      AP_POSTGRES_PORT: 5432
      AP_POSTGRES_USERNAME: activepieces
      AP_POSTGRES_PASSWORD: ${AP_POSTGRES_PASSWORD}
      AP_EXECUTION_MODE: UNSANDBOXED
      AP_REDIS_HOST: redis
      AP_REDIS_PORT: 6379
      AP_SANDBOX_RUN_TIME_SECONDS: 600
      AP_TELEMETRY_ENABLED: "false"
      AP_TEMPLATES_SOURCE_URL: https://cloud.activepieces.com/api/v1/flow-templates

  postgres:
    image: postgres:14
    restart: unless-stopped

    environment:
      POSTGRES_DB: activepieces
      POSTGRES_PASSWORD: ${AP_POSTGRES_PASSWORD}
      POSTGRES_USER: activepieces
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U activepieces -d activepieces"]
      interval: 30s
      timeout: 30s
      retries: 3

  redis:
    image: redis:7
    restart: unless-stopped

    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 30s
      timeout: 30s
      retries: 3

volumes:
  postgres_data:
  redis_data:
```

```
[variables]
main_domain = "${domain}"
api_key = "${password:32}"
encryption_key = "${password:32}"
jwt_secret = "${password:32}"
postgres_password = "${password:32}"

[config]
env = [
  "AP_HOST=${main_domain}",
  "AP_API_KEY=${api_key}",
  "AP_ENCRYPTION_KEY=${encryption_key}",
  "AP_JWT_SECRET=${jwt_secret}",
  "AP_POSTGRES_PASSWORD=${postgres_password}",
]
mounts = []

[[config.domains]]
serviceName = "activepieces"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGFjdGl2ZXBpZWNlczpcbiAgICBpbWFnZTogYWN0aXZlcGllY2VzL2FjdGl2ZXBpZWNlczowLjM1LjBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHBvc3RncmVzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgcmVkaXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBBUF9FTkdJTkVfRVhFQ1VUQUJMRV9QQVRIOiBkaXN0L3BhY2thZ2VzL2VuZ2luZS9tYWluLmpzXG4gICAgICBBUF9BUElfS0VZOiAke0FQX0FQSV9LRVl9XG4gICAgICBBUF9FTkNSWVBUSU9OX0tFWTogJHtBUF9FTkNSWVBUSU9OX0tFWX1cbiAgICAgIEFQX0pXVF9TRUNSRVQ6ICR7QVBfSldUX1NFQ1JFVH1cbiAgICAgIEFQX0VOVklST05NRU5UOiBwcm9kXG4gICAgICBBUF9GUk9OVEVORF9VUkw6IGh0dHBzOi8vJHtBUF9IT1NUfVxuICAgICAgQVBfV0VCSE9PS19USU1FT1VUX1NFQ09ORFM6IDMwXG4gICAgICBBUF9UUklHR0VSX0RFRkFVTFRfUE9MTF9JTlRFUlZBTDogNVxuICAgICAgQVBfUE9TVEdSRVNfREFUQUJBU0U6IGFjdGl2ZXBpZWNlc1xuICAgICAgQVBfUE9TVEdSRVNfSE9TVDogcG9zdGdyZXNcbiAgICAgIEFQX1BPU1RHUkVTX1BPUlQ6IDU0MzJcbiAgICAgIEFQX1BPU1RHUkVTX1VTRVJOQU1FOiBhY3RpdmVwaWVjZXNcbiAgICAgIEFQX1BPU1RHUkVTX1BBU1NXT1JEOiAke0FQX1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgQVBfRVhFQ1VUSU9OX01PREU6IFVOU0FOREJPWEVEXG4gICAgICBBUF9SRURJU19IT1NUOiByZWRpc1xuICAgICAgQVBfUkVESVNfUE9SVDogNjM3OVxuICAgICAgQVBfU0FOREJPWF9SVU5fVElNRV9TRUNPTkRTOiA2MDBcbiAgICAgIEFQX1RFTEVNRVRSWV9FTkFCTEVEOiBcImZhbHNlXCJcbiAgICAgIEFQX1RFTVBMQVRFU19TT1VSQ0VfVVJMOiBodHRwczovL2Nsb3VkLmFjdGl2ZXBpZWNlcy5jb20vYXBpL3YxL2Zsb3ctdGVtcGxhdGVzXG5cbiAgcG9zdGdyZXM6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6IGFjdGl2ZXBpZWNlc1xuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7QVBfUE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19VU0VSOiBhY3RpdmVwaWVjZXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlc19kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSBhY3RpdmVwaWVjZXMgLWQgYWN0aXZlcGllY2VzXCJdXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAzMHNcbiAgICAgIHJldHJpZXM6IDNcblxuICByZWRpczpcbiAgICBpbWFnZTogcmVkaXM6N1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSByZWRpc19kYXRhOi9kYXRhXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJyZWRpcy1jbGlcIiwgXCJwaW5nXCJdXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAzMHNcbiAgICAgIHJldHJpZXM6IDNcblxudm9sdW1lczpcbiAgcG9zdGdyZXNfZGF0YTpcbiAgcmVkaXNfZGF0YTogIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmFwaV9rZXkgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmVuY3J5cHRpb25fa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5qd3Rfc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICBcIkFQX0hPU1Q9JHttYWluX2RvbWFpbn1cIixcbiAgXCJBUF9BUElfS0VZPSR7YXBpX2tleX1cIixcbiAgXCJBUF9FTkNSWVBUSU9OX0tFWT0ke2VuY3J5cHRpb25fa2V5fVwiLFxuICBcIkFQX0pXVF9TRUNSRVQ9JHtqd3Rfc2VjcmV0fVwiLFxuICBcIkFQX1BPU1RHUkVTX1BBU1NXT1JEPSR7cG9zdGdyZXNfcGFzc3dvcmR9XCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhY3RpdmVwaWVjZXNcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`automation`,`workflow`,`no-code`

---

Version:`0.35.0`

AckeeAckee is a self-hosted analytics tool for your website.

Actual BudgetA super fast and privacy-focused app for managing your finances.

### On this page

ConfigurationBase64LinksTags