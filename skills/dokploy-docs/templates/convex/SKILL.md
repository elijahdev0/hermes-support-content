---
title: "Convex | Dokploy"
source: "https://docs.dokploy.com/docs/templates/convex"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

Convex | Dokploy

# Convex

Copy as Markdown

Convex is an open-source reactive database designed to make life easy for web app developers.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  backend:
    image: ghcr.io/get-convex/convex-backend:5cdea511cd6527a95dd24152ea0d3c3bb2ab379f
    expose:
      - "3210"
      - "3211"
    volumes:
      - data:/convex/data
    environment:
      - INSTANCE_NAME=${INSTANCE_NAME:-}
      - INSTANCE_SECRET=${INSTANCE_SECRET:-}
      - CONVEX_RELEASE_VERSION_DEV=${CONVEX_RELEASE_VERSION_DEV:-}
      - ACTIONS_USER_TIMEOUT_SECS=${ACTIONS_USER_TIMEOUT_SECS:-}
      - CONVEX_CLOUD_ORIGIN=${CONVEX_CLOUD_ORIGIN:-http://127.0.0.1:3210}
      - CONVEX_SITE_ORIGIN=${CONVEX_SITE_ORIGIN:-http://127.0.0.1:3211}
      - DATABASE_URL=${DATABASE_URL:-}
      - DISABLE_BEACON=${DISABLE_BEACON:-FALSE}
      - REDACT_LOGS_TO_CLIENT=${REDACT_LOGS_TO_CLIENT:-}
      - RUST_LOG=${RUST_LOG:-info}
      - RUST_BACKTRACE=${RUST_BACKTRACE:-}
    healthcheck:
      test: curl -f http://localhost:3210/version
      interval: 5s
      start_period: 5s

  dashboard:
    image: ghcr.io/get-convex/convex-dashboard:5cdea511cd6527a95dd24152ea0d3c3bb2ab379f
    expose:
      - "6791"
    environment:
      - NEXT_PUBLIC_DEPLOYMENT_URL=${NEXT_PUBLIC_DEPLOYMENT_URL:-http://127.0.0.1:3210}
    depends_on:
      backend:
        condition: service_healthy

volumes:
  data:
```

```
[variables]
dashboard_domain = "${domain}"
backend_domain = "${domain}"
actions_domain = "${domain}"

[config]
env = [
  "NEXT_PUBLIC_DEPLOYMENT_URL=http://${backend_domain}",
  "CONVEX_CLOUD_ORIGIN=http://${backend_domain}",
  "CONVEX_SITE_ORIGIN=http://${actions_domain}",
]
mounts = []

[[config.domains]]
serviceName = "dashboard"
port = 6_791
host = "${dashboard_domain}"

[[config.domains]]
serviceName = "backend"
port = 3_210
host = "${backend_domain}"

[[config.domains]]
serviceName = "backend"
port = 3_211
host = "${actions_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBiYWNrZW5kOlxuICAgIGltYWdlOiBnaGNyLmlvL2dldC1jb252ZXgvY29udmV4LWJhY2tlbmQ6NWNkZWE1MTFjZDY1MjdhOTVkZDI0MTUyZWEwZDNjM2JiMmFiMzc5ZlxuICAgIGV4cG9zZTpcbiAgICAgIC0gXCIzMjEwXCJcbiAgICAgIC0gXCIzMjExXCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYXRhOi9jb252ZXgvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBJTlNUQU5DRV9OQU1FPSR7SU5TVEFOQ0VfTkFNRTotfVxuICAgICAgLSBJTlNUQU5DRV9TRUNSRVQ9JHtJTlNUQU5DRV9TRUNSRVQ6LX1cbiAgICAgIC0gQ09OVkVYX1JFTEVBU0VfVkVSU0lPTl9ERVY9JHtDT05WRVhfUkVMRUFTRV9WRVJTSU9OX0RFVjotfVxuICAgICAgLSBBQ1RJT05TX1VTRVJfVElNRU9VVF9TRUNTPSR7QUNUSU9OU19VU0VSX1RJTUVPVVRfU0VDUzotfVxuICAgICAgLSBDT05WRVhfQ0xPVURfT1JJR0lOPSR7Q09OVkVYX0NMT1VEX09SSUdJTjotaHR0cDovLzEyNy4wLjAuMTozMjEwfVxuICAgICAgLSBDT05WRVhfU0lURV9PUklHSU49JHtDT05WRVhfU0lURV9PUklHSU46LWh0dHA6Ly8xMjcuMC4wLjE6MzIxMX1cbiAgICAgIC0gREFUQUJBU0VfVVJMPSR7REFUQUJBU0VfVVJMOi19XG4gICAgICAtIERJU0FCTEVfQkVBQ09OPSR7RElTQUJMRV9CRUFDT046LUZBTFNFfVxuICAgICAgLSBSRURBQ1RfTE9HU19UT19DTElFTlQ9JHtSRURBQ1RfTE9HU19UT19DTElFTlQ6LX1cbiAgICAgIC0gUlVTVF9MT0c9JHtSVVNUX0xPRzotaW5mb31cbiAgICAgIC0gUlVTVF9CQUNLVFJBQ0U9JHtSVVNUX0JBQ0tUUkFDRTotfVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogY3VybCAtZiBodHRwOi8vbG9jYWxob3N0OjMyMTAvdmVyc2lvblxuICAgICAgaW50ZXJ2YWw6IDVzXG4gICAgICBzdGFydF9wZXJpb2Q6IDVzXG5cbiAgZGFzaGJvYXJkOlxuICAgIGltYWdlOiBnaGNyLmlvL2dldC1jb252ZXgvY29udmV4LWRhc2hib2FyZDo1Y2RlYTUxMWNkNjUyN2E5NWRkMjQxNTJlYTBkM2MzYmIyYWIzNzlmXG4gICAgZXhwb3NlOlxuICAgICAgLSBcIjY3OTFcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBORVhUX1BVQkxJQ19ERVBMT1lNRU5UX1VSTD0ke05FWFRfUFVCTElDX0RFUExPWU1FTlRfVVJMOi1odHRwOi8vMTI3LjAuMC4xOjMyMTB9XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGJhY2tlbmQ6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG5cbnZvbHVtZXM6XG4gIGRhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbmRhc2hib2FyZF9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5iYWNrZW5kX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmFjdGlvbnNfZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICBcIk5FWFRfUFVCTElDX0RFUExPWU1FTlRfVVJMPWh0dHA6Ly8ke2JhY2tlbmRfZG9tYWlufVwiLFxuICBcIkNPTlZFWF9DTE9VRF9PUklHSU49aHR0cDovLyR7YmFja2VuZF9kb21haW59XCIsXG4gIFwiQ09OVkVYX1NJVEVfT1JJR0lOPWh0dHA6Ly8ke2FjdGlvbnNfZG9tYWlufVwiLFxuXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZGFzaGJvYXJkXCJcbnBvcnQgPSA2Xzc5MVxuaG9zdCA9IFwiJHtkYXNoYm9hcmRfZG9tYWlufVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImJhY2tlbmRcIlxucG9ydCA9IDNfMjEwXG5ob3N0ID0gXCIke2JhY2tlbmRfZG9tYWlufVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImJhY2tlbmRcIlxucG9ydCA9IDNfMjExXG5ob3N0ID0gXCIke2FjdGlvbnNfZG9tYWlufVwiXG4iCn0=
```

## Links

`backend`,`database`,`api`

---

Version:`latest`

ConvertXConvertX is a service for converting media files, with optional user registration and file management features.

CookieCloudCookieCloud lets you sync and manage browser cookies across devices securely using a self-hosted backend.

### On this page

ConfigurationBase64LinksTags