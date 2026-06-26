---
title: "TRMNL BYOS Laravel | Dokploy"
source: "https://docs.dokploy.com/docs/templates/trmnl-byos-laravel"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

TRMNL BYOS Laravel | Dokploy

# TRMNL BYOS Laravel

Copy as Markdown

TRMNL BYOS Laravel is a self-hosted application to manage TRMNL e-ink devices.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  trmnl-byos-laravel:
    image: ghcr.io/usetrmnl/byos_laravel:0.27.0
    environment:
      - APP_URL=${APP_URL}
      - PHP_OPCACHE_ENABLE=${PHP_OPCACHE_ENABLE}
      - DEPLOY_VARIANT="dokploy"
      - DB_DATABASE=database/storage/database.sqlite
      - APP_TIMEZONE=${APP_TIMEZONE}
      # - APP_KEY:
      - REGISTRATION_ENABLED=${REGISTRATION_ENABLED}
      - FORCE_HTTPS=${FORCE_HTTPS}
    restart: always
    volumes:
      - trmnl-database:/var/www/html/database/storage
      - trmnl-storage:/var/www/html/storage/app/public/images/generated
volumes:
  trmnl-database:
  trmnl-storage:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "trmnl-byos-laravel"
port = 8080
host = "${main_domain}"

[config.env]
APP_URL = "${main_domain}"
PHP_OPCACHE_ENABLE = "1"
APP_TIMEZONE = "UTC"
REGISTRATION_ENABLED = "1"
FORCE_HTTPS = "0"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB0cm1ubC1ieW9zLWxhcmF2ZWw6XG4gICAgaW1hZ2U6IGdoY3IuaW8vdXNldHJtbmwvYnlvc19sYXJhdmVsOjAuMjcuMFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBBUFBfVVJMPSR7QVBQX1VSTH1cbiAgICAgIC0gUEhQX09QQ0FDSEVfRU5BQkxFPSR7UEhQX09QQ0FDSEVfRU5BQkxFfVxuICAgICAgLSBERVBMT1lfVkFSSUFOVD1cImRva3Bsb3lcIlxuICAgICAgLSBEQl9EQVRBQkFTRT1kYXRhYmFzZS9zdG9yYWdlL2RhdGFiYXNlLnNxbGl0ZVxuICAgICAgLSBBUFBfVElNRVpPTkU9JHtBUFBfVElNRVpPTkV9XG4gICAgICAjIC0gQVBQX0tFWTpcbiAgICAgIC0gUkVHSVNUUkFUSU9OX0VOQUJMRUQ9JHtSRUdJU1RSQVRJT05fRU5BQkxFRH1cbiAgICAgIC0gRk9SQ0VfSFRUUFM9JHtGT1JDRV9IVFRQU31cbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSB0cm1ubC1kYXRhYmFzZTovdmFyL3d3dy9odG1sL2RhdGFiYXNlL3N0b3JhZ2VcbiAgICAgIC0gdHJtbmwtc3RvcmFnZTovdmFyL3d3dy9odG1sL3N0b3JhZ2UvYXBwL3B1YmxpYy9pbWFnZXMvZ2VuZXJhdGVkXG52b2x1bWVzOlxuICB0cm1ubC1kYXRhYmFzZTpcbiAgdHJtbmwtc3RvcmFnZTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ0cm1ubC1ieW9zLWxhcmF2ZWxcIlxucG9ydCA9IDgwODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5BUFBfVVJMID0gXCIke21haW5fZG9tYWlufVwiXG5QSFBfT1BDQUNIRV9FTkFCTEUgPSBcIjFcIlxuQVBQX1RJTUVaT05FID0gXCJVVENcIlxuUkVHSVNUUkFUSU9OX0VOQUJMRUQgPSBcIjFcIlxuRk9SQ0VfSFRUUFMgPSBcIjBcIlxuIgp9
```

## Links

`e-ink`

---

Version:`0.27.0`

TriliumNextIs a free and open-source, cross-platform hierarchical note taking application with focus on building large personal knowledge bases.

TuwunelHigh performance Matrix homeserver written in Rust. Official successor to conduwuit - a scalable, low-cost, enterprise-ready alternative to Synapse.

### On this page

ConfigurationBase64LinksTags