---
title: "Kimai | Dokploy"
source: "https://docs.dokploy.com/docs/templates/kimai"
category: dokploy-docs
created: "2026-06-25T17:21:50.891Z"
---

Kimai | Dokploy

# Kimai

Copy as Markdown

Kimai is a web-based multi-user time-tracking application. Works great for everyone: freelancers, companies, organizations - everyone can track their times, generate reports, create invoices and do so much more.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  app:
    image: kimai/kimai2:apache-2.31.0
    restart: unless-stopped
    environment:
      APP_ENV: prod
      DATABASE_URL: mysql://kimai:${KI_MYSQL_PASSWORD:-kimai}@db/kimai
      TRUSTED_PROXIES: localhost
      APP_SECRET: ${KI_APP_SECRET}
      MAILER_FROM: ${KI_MAILER_FROM:[email protected]}
      MAILER_URL: ${KI_MAILER_URL:-null://null}
      ADMINMAIL: ${KI_ADMINMAIL:[email protected]}
      ADMINPASS: ${KI_ADMINPASS}
    volumes:
      - kimai-data:/opt/kimai/var
    depends_on:
      db:
        condition: service_healthy

  db:
    image: mariadb:10.11
    restart: unless-stopped
    environment:
      - MYSQL_DATABASE=kimai
      - MYSQL_USER=kimai
      - MYSQL_PASSWORD=${KI_MYSQL_PASSWORD}
      - MYSQL_ROOT_PASSWORD=${KI_MYSQL_ROOT_PASSWORD}
    volumes:
      - mysql-data:/var/lib/mysql
    command:
      - --character-set-server=utf8mb4
      - --collation-server=utf8mb4_unicode_ci
      - --innodb-buffer-pool-size=256M
      - --innodb-flush-log-at-trx-commit=2
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u", "kimai", "-p${KI_MYSQL_PASSWORD}"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

volumes:
  kimai-data:
  mysql-data:
```

```
[variables]
main_domain = "${domain}"
admin_password = "${password:32}"
mysql_password = "${password:32}"
mysql_root_password = "${password:32}"
app_secret = "${password:32}"

[config]
mounts = []

[[config.domains]]
serviceName = "app"
port = 8_001
host = "${main_domain}"

[config.env]
KI_HOST = "${main_domain}"
KI_ADMINMAIL = "[email protected]"
KI_ADMINPASS = "${admin_password}"
KI_MYSQL_ROOT_PASSWORD = "${mysql_root_password}"
KI_MYSQL_PASSWORD = "${mysql_password}"
KI_APP_SECRET = "${app_secret}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBhcHA6XG4gICAgaW1hZ2U6IGtpbWFpL2tpbWFpMjphcGFjaGUtMi4zMS4wXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEFQUF9FTlY6IHByb2RcbiAgICAgIERBVEFCQVNFX1VSTDogbXlzcWw6Ly9raW1haToke0tJX01ZU1FMX1BBU1NXT1JEOi1raW1haX1AZGIva2ltYWlcbiAgICAgIFRSVVNURURfUFJPWElFUzogbG9jYWxob3N0XG4gICAgICBBUFBfU0VDUkVUOiAke0tJX0FQUF9TRUNSRVR9XG4gICAgICBNQUlMRVJfRlJPTTogJHtLSV9NQUlMRVJfRlJPTTotYWRtaW5Aa2ltYWkubG9jYWx9XG4gICAgICBNQUlMRVJfVVJMOiAke0tJX01BSUxFUl9VUkw6LW51bGw6Ly9udWxsfVxuICAgICAgQURNSU5NQUlMOiAke0tJX0FETUlOTUFJTDotYWRtaW5Aa2ltYWkubG9jYWx9XG4gICAgICBBRE1JTlBBU1M6ICR7S0lfQURNSU5QQVNTfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGtpbWFpLWRhdGE6L29wdC9raW1haS92YXJcbiAgICBkZXBlbmRzX29uOlxuICAgICAgZGI6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG5cbiAgZGI6XG4gICAgaW1hZ2U6IG1hcmlhZGI6MTAuMTFcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBNWVNRTF9EQVRBQkFTRT1raW1haVxuICAgICAgLSBNWVNRTF9VU0VSPWtpbWFpXG4gICAgICAtIE1ZU1FMX1BBU1NXT1JEPSR7S0lfTVlTUUxfUEFTU1dPUkR9XG4gICAgICAtIE1ZU1FMX1JPT1RfUEFTU1dPUkQ9JHtLSV9NWVNRTF9ST09UX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIG15c3FsLWRhdGE6L3Zhci9saWIvbXlzcWxcbiAgICBjb21tYW5kOlxuICAgICAgLSAtLWNoYXJhY3Rlci1zZXQtc2VydmVyPXV0ZjhtYjRcbiAgICAgIC0gLS1jb2xsYXRpb24tc2VydmVyPXV0ZjhtYjRfdW5pY29kZV9jaVxuICAgICAgLSAtLWlubm9kYi1idWZmZXItcG9vbC1zaXplPTI1Nk1cbiAgICAgIC0gLS1pbm5vZGItZmx1c2gtbG9nLWF0LXRyeC1jb21taXQ9MlxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwibXlzcWxhZG1pblwiLCBcInBpbmdcIiwgXCItaFwiLCBcImxvY2FsaG9zdFwiLCBcIi11XCIsIFwia2ltYWlcIiwgXCItcCR7S0lfTVlTUUxfUEFTU1dPUkR9XCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgICAgc3RhcnRfcGVyaW9kOiAzMHNcblxuXG52b2x1bWVzOlxuICBraW1haS1kYXRhOlxuICBteXNxbC1kYXRhOiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5hZG1pbl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxubXlzcWxfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbm15c3FsX3Jvb3RfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmFwcF9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFwcFwiXG5wb3J0ID0gOF8wMDFcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5LSV9IT1NUID0gXCIke21haW5fZG9tYWlufVwiXG5LSV9BRE1JTk1BSUwgPSBcImFkbWluQGtpbWFpLmxvY2FsXCJcbktJX0FETUlOUEFTUyA9IFwiJHthZG1pbl9wYXNzd29yZH1cIlxuS0lfTVlTUUxfUk9PVF9QQVNTV09SRCA9IFwiJHtteXNxbF9yb290X3Bhc3N3b3JkfVwiXG5LSV9NWVNRTF9QQVNTV09SRCA9IFwiJHtteXNxbF9wYXNzd29yZH1cIlxuS0lfQVBQX1NFQ1JFVCA9IFwiJHthcHBfc2VjcmV0fVwiXG4iCn0=
```

## Links

`invoice`,`business`,`finance`

---

Version:`2.31.0`

KeycloakKeycloak is an open source Identity and Access Management solution for modern applications and services.

KitchenOwlKitchenOwl is a self-hosted grocery list and recipe manager.

### On this page

ConfigurationBase64LinksTags