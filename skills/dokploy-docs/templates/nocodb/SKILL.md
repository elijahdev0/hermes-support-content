---
title: "NocoDB | Dokploy"
source: "https://docs.dokploy.com/docs/templates/nocodb"
category: dokploy-docs
created: "2026-06-25T17:21:54.355Z"
---

NocoDB | Dokploy

# NocoDB

Copy as Markdown

NocoDB is an opensource Airtable alternative that turns any MySQL, PostgreSQL, SQL Server, SQLite & MariaDB into a smart spreadsheet.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  nocodb:
    image: nocodb/nocodb:latest
    restart: always
    depends_on:
      root_db:
        condition: service_healthy
    environment:
      # Reuses DB env from template.toml / .env
      NC_DB: "pg://root_db:5432?u=${POSTGRES_USER}&p=${POSTGRES_PASSWORD}&d=${POSTGRES_DB}"
    volumes:
      - nc_data:/usr/app/data

  root_db:
    image: postgres:16.6
    restart: always
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    # More reliable healthcheck:
    healthcheck:
      test:
        [
          "CMD-SHELL",
          'pg_isready -h 127.0.0.1 -U "$POSTGRES_USER" -d "$POSTGRES_DB"',
        ]
      interval: 10s
      timeout: 5s
      start_period: 20s
      retries: 10
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data: {}
  nc_data: {}
```

```
[variables]
main_domain = "${domain}"
postgres_user = "postgres"
postgres_password = "${password:32}"
postgres_db = "root_db"

[config]
[[config.domains]]
serviceName = "nocodb"
port = 8080
host = "${main_domain}"

[config.env]
POSTGRES_USER = "${postgres_user}"
POSTGRES_PASSWORD = "${postgres_password}"
POSTGRES_DB = "${postgres_db}"

[[config.mounts]]
serviceName = "nocodb"
volumeName = "nc_data"
mountPath = "/usr/app/data"

[[config.mounts]]
serviceName = "root_db"
volumeName = "db_data"
mountPath = "/var/lib/postgresql/data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBub2NvZGI6XG4gICAgaW1hZ2U6IG5vY29kYi9ub2NvZGI6bGF0ZXN0XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHJvb3RfZGI6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAjIFJldXNlcyBEQiBlbnYgZnJvbSB0ZW1wbGF0ZS50b21sIC8gLmVudlxuICAgICAgTkNfREI6IFwicGc6Ly9yb290X2RiOjU0MzI/dT0ke1BPU1RHUkVTX1VTRVJ9JnA9JHtQT1NUR1JFU19QQVNTV09SRH0mZD0ke1BPU1RHUkVTX0RCfVwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gbmNfZGF0YTovdXNyL2FwcC9kYXRhXG5cbiAgcm9vdF9kYjpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTYuNlxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6ICR7UE9TVEdSRVNfREJ9XG4gICAgICBQT1NUR1JFU19VU0VSOiAke1BPU1RHUkVTX1VTRVJ9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAjIE1vcmUgcmVsaWFibGUgaGVhbHRoY2hlY2s6XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICBbXG4gICAgICAgICAgXCJDTUQtU0hFTExcIixcbiAgICAgICAgICAncGdfaXNyZWFkeSAtaCAxMjcuMC4wLjEgLVUgXCIkUE9TVEdSRVNfVVNFUlwiIC1kIFwiJFBPU1RHUkVTX0RCXCInLFxuICAgICAgICBdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgc3RhcnRfcGVyaW9kOiAyMHNcbiAgICAgIHJldHJpZXM6IDEwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGJfZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcblxudm9sdW1lczpcbiAgZGJfZGF0YToge31cbiAgbmNfZGF0YToge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5wb3N0Z3Jlc191c2VyID0gXCJwb3N0Z3Jlc1wiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxucG9zdGdyZXNfZGIgPSBcInJvb3RfZGJcIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibm9jb2RiXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuUE9TVEdSRVNfVVNFUiA9IFwiJHtwb3N0Z3Jlc191c2VyfVwiXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtwb3N0Z3Jlc19wYXNzd29yZH1cIlxuUE9TVEdSRVNfREIgPSBcIiR7cG9zdGdyZXNfZGJ9XCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJub2NvZGJcIlxudm9sdW1lTmFtZSA9IFwibmNfZGF0YVwiXG5tb3VudFBhdGggPSBcIi91c3IvYXBwL2RhdGFcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcInJvb3RfZGJcIlxudm9sdW1lTmFtZSA9IFwiZGJfZGF0YVwiXG5tb3VudFBhdGggPSBcIi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVwiXG4iCn0=
```

## Links

`database`,`spreadsheet`,`low-code`,`nocode`

---

Version:`latest`

NginxNginx is an High performance web server

NotifuseOpen-source newsletter and notification platform that empowers teams to create, send, and track communications at scale.

### On this page

ConfigurationBase64LinksTags