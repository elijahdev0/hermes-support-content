---
title: "HortusFox | Dokploy"
source: "https://docs.dokploy.com/docs/templates/hortusfox"
category: dokploy-docs
created: "2026-06-25T17:21:49.750Z"
---

HortusFox | Dokploy

# HortusFox

Copy as Markdown

HortusFox is an open source task and photo management app, designed for photographers and creatives to manage projects, tasks, and images effectively.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  app:
    image: ghcr.io/danielbrendel/hortusfox-web:latest
    restart: unless-stopped
    volumes:
      - app_images:/var/www/html/public/img
      - app_logs:/var/www/html/app/logs
      - app_backup:/var/www/html/public/backup
      - app_themes:/var/www/html/public/themes
      - app_migrate:/var/www/html/app/migrations
    environment:
      APP_ADMIN_EMAIL: ${APP_ADMIN_EMAIL}
      APP_ADMIN_PASSWORD: ${APP_ADMIN_PASSWORD}
      APP_TIMEZONE: ${APP_TIMEZONE}
      DB_HOST: db
      DB_PORT: 3306
      DB_DATABASE: ${DB_DATABASE}
      DB_USERNAME: ${DB_USERNAME}
      DB_PASSWORD: ${DB_PASSWORD}
      DB_CHARSET: utf8mb4
    depends_on:
      - db

  db:
    image: mariadb:11
    restart: unless-stopped
    environment:
      MARIADB_ROOT_PASSWORD: ${MARIADB_ROOT_PASSWORD}
      MARIADB_DATABASE: ${DB_DATABASE}
      MARIADB_USER: ${DB_USERNAME}
      MARIADB_PASSWORD: ${DB_PASSWORD}
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:
  app_images:
  app_logs:
  app_backup:
  app_themes:
  app_migrate:
```

```
[variables]
main_domain = "${domain}"
APP_ADMIN_EMAIL = "${email}"
APP_ADMIN_PASSWORD = "${password:16}"
APP_TIMEZONE = "UTC"

DB_DATABASE = "hortusfox"
DB_USERNAME = "hortususer"
DB_PASSWORD = "${password:20}"
MARIADB_ROOT_PASSWORD = "${password:24}"

[config]

[[config.domains]]
serviceName = "app"
port = 80
host = "${main_domain}"

[config.env]
APP_ADMIN_EMAIL = "${APP_ADMIN_EMAIL}"
APP_ADMIN_PASSWORD = "${APP_ADMIN_PASSWORD}"
APP_TIMEZONE = "${APP_TIMEZONE}"
DB_DATABASE = "${DB_DATABASE}"
DB_USERNAME = "${DB_USERNAME}"
DB_PASSWORD = "${DB_PASSWORD}"
MARIADB_ROOT_PASSWORD = "${MARIADB_ROOT_PASSWORD}"

[[config.mounts]]
name = "app_images"
mountPath = "/var/www/html/public/img"

[[config.mounts]]
name = "app_logs"
mountPath = "/var/www/html/app/logs"

[[config.mounts]]
name = "app_backup"
mountPath = "/var/www/html/public/backup"

[[config.mounts]]
name = "app_themes"
mountPath = "/var/www/html/public/themes"

[[config.mounts]]
name = "app_migrate"
mountPath = "/var/www/html/app/migrations"

[[config.mounts]]
name = "db_data"
mountPath = "/var/lib/mysql"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGFwcDpcbiAgICBpbWFnZTogZ2hjci5pby9kYW5pZWxicmVuZGVsL2hvcnR1c2ZveC13ZWI6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBhcHBfaW1hZ2VzOi92YXIvd3d3L2h0bWwvcHVibGljL2ltZ1xuICAgICAgLSBhcHBfbG9nczovdmFyL3d3dy9odG1sL2FwcC9sb2dzXG4gICAgICAtIGFwcF9iYWNrdXA6L3Zhci93d3cvaHRtbC9wdWJsaWMvYmFja3VwXG4gICAgICAtIGFwcF90aGVtZXM6L3Zhci93d3cvaHRtbC9wdWJsaWMvdGhlbWVzXG4gICAgICAtIGFwcF9taWdyYXRlOi92YXIvd3d3L2h0bWwvYXBwL21pZ3JhdGlvbnNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEFQUF9BRE1JTl9FTUFJTDogJHtBUFBfQURNSU5fRU1BSUx9XG4gICAgICBBUFBfQURNSU5fUEFTU1dPUkQ6ICR7QVBQX0FETUlOX1BBU1NXT1JEfVxuICAgICAgQVBQX1RJTUVaT05FOiAke0FQUF9USU1FWk9ORX1cbiAgICAgIERCX0hPU1Q6IGRiXG4gICAgICBEQl9QT1JUOiAzMzA2XG4gICAgICBEQl9EQVRBQkFTRTogJHtEQl9EQVRBQkFTRX1cbiAgICAgIERCX1VTRVJOQU1FOiAke0RCX1VTRVJOQU1FfVxuICAgICAgREJfUEFTU1dPUkQ6ICR7REJfUEFTU1dPUkR9XG4gICAgICBEQl9DSEFSU0VUOiB1dGY4bWI0XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gZGJcblxuICBkYjpcbiAgICBpbWFnZTogbWFyaWFkYjoxMVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNQVJJQURCX1JPT1RfUEFTU1dPUkQ6ICR7TUFSSUFEQl9ST09UX1BBU1NXT1JEfVxuICAgICAgTUFSSUFEQl9EQVRBQkFTRTogJHtEQl9EQVRBQkFTRX1cbiAgICAgIE1BUklBREJfVVNFUjogJHtEQl9VU0VSTkFNRX1cbiAgICAgIE1BUklBREJfUEFTU1dPUkQ6ICR7REJfUEFTU1dPUkR9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGJfZGF0YTovdmFyL2xpYi9teXNxbFxuXG52b2x1bWVzOlxuICBkYl9kYXRhOlxuICBhcHBfaW1hZ2VzOlxuICBhcHBfbG9nczpcbiAgYXBwX2JhY2t1cDpcbiAgYXBwX3RoZW1lczpcbiAgYXBwX21pZ3JhdGU6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuQVBQX0FETUlOX0VNQUlMID0gXCIke2VtYWlsfVwiXG5BUFBfQURNSU5fUEFTU1dPUkQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbkFQUF9USU1FWk9ORSA9IFwiVVRDXCJcblxuREJfREFUQUJBU0UgPSBcImhvcnR1c2ZveFwiXG5EQl9VU0VSTkFNRSA9IFwiaG9ydHVzdXNlclwiXG5EQl9QQVNTV09SRCA9IFwiJHtwYXNzd29yZDoyMH1cIlxuTUFSSUFEQl9ST09UX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjI0fVwiXG5cbltjb25maWddXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFwcFwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5BUFBfQURNSU5fRU1BSUwgPSBcIiR7QVBQX0FETUlOX0VNQUlMfVwiXG5BUFBfQURNSU5fUEFTU1dPUkQgPSBcIiR7QVBQX0FETUlOX1BBU1NXT1JEfVwiXG5BUFBfVElNRVpPTkUgPSBcIiR7QVBQX1RJTUVaT05FfVwiXG5EQl9EQVRBQkFTRSA9IFwiJHtEQl9EQVRBQkFTRX1cIlxuREJfVVNFUk5BTUUgPSBcIiR7REJfVVNFUk5BTUV9XCJcbkRCX1BBU1NXT1JEID0gXCIke0RCX1BBU1NXT1JEfVwiXG5NQVJJQURCX1JPT1RfUEFTU1dPUkQgPSBcIiR7TUFSSUFEQl9ST09UX1BBU1NXT1JEfVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5uYW1lID0gXCJhcHBfaW1hZ2VzXCJcbm1vdW50UGF0aCA9IFwiL3Zhci93d3cvaHRtbC9wdWJsaWMvaW1nXCJcblxuW1tjb25maWcubW91bnRzXV1cbm5hbWUgPSBcImFwcF9sb2dzXCJcbm1vdW50UGF0aCA9IFwiL3Zhci93d3cvaHRtbC9hcHAvbG9nc1wiXG5cbltbY29uZmlnLm1vdW50c11dXG5uYW1lID0gXCJhcHBfYmFja3VwXCJcbm1vdW50UGF0aCA9IFwiL3Zhci93d3cvaHRtbC9wdWJsaWMvYmFja3VwXCJcblxuW1tjb25maWcubW91bnRzXV1cbm5hbWUgPSBcImFwcF90aGVtZXNcIlxubW91bnRQYXRoID0gXCIvdmFyL3d3dy9odG1sL3B1YmxpYy90aGVtZXNcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxubmFtZSA9IFwiYXBwX21pZ3JhdGVcIlxubW91bnRQYXRoID0gXCIvdmFyL3d3dy9odG1sL2FwcC9taWdyYXRpb25zXCJcblxuW1tjb25maWcubW91bnRzXV1cbm5hbWUgPSBcImRiX2RhdGFcIlxubW91bnRQYXRoID0gXCIvdmFyL2xpYi9teXNxbFwiXG4iCn0=
```

## Links

`productivity`,`photo`,`task-management`,`php`,`mariadb`

---

Version:`5.0`

Hoppscotch (AIO + Migrations)Hoppscotch Community Edition (All-in-One) with automatic database migrations. Includes backend, frontend, and admin under unified subpath routing.

HulyHuly — All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion)

### On this page

ConfigurationBase64LinksTags