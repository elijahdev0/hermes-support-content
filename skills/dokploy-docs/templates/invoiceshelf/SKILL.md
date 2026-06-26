---
title: "InvoiceShelf | Dokploy"
source: "https://docs.dokploy.com/docs/templates/invoiceshelf"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

InvoiceShelf | Dokploy

# InvoiceShelf

Copy as Markdown

InvoiceShelf is a self-hosted open source invoicing system for freelancers and small businesses.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  invoiceshelf-postgres:
    image: postgres:15

    volumes:
      - invoiceshelf-postgres-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_USER=${DB_USERNAME}
      - POSTGRES_DB=${DB_DATABASE}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USERNAME}"]
      interval: 10s
      timeout: 5s
      retries: 5

  invoiceshelf-app:
    image: invoiceshelf/invoiceshelf:nightly

    volumes:
      - invoiceshelf-storage:/var/www/html/storage
    environment:
      - PHP_TZ=UTC
      - TIMEZONE=UTC
      - APP_NAME=InvoiceShelf
      - APP_ENV=production
      - APP_DEBUG=false
      - APP_URL=http://${INVOICESHELF_HOST}
      - DB_CONNECTION=pgsql
      - DB_HOST=invoiceshelf-postgres
      - DB_PORT=5432
      - DB_DATABASE=${DB_DATABASE}
      - DB_USERNAME=${DB_USERNAME}
      - DB_PASSWORD=${DB_PASSWORD}
      - CACHE_STORE=file
      - SESSION_DRIVER=file
      - SESSION_LIFETIME=120
      - SESSION_ENCRYPT=true
      - SESSION_PATH=/
      - SESSION_DOMAIN=${INVOICESHELF_HOST}
      - SANCTUM_STATEFUL_DOMAINS=${INVOICESHELF_HOST}
      - STARTUP_DELAY=10
    depends_on:
      invoiceshelf-postgres:
        condition: service_healthy

volumes:
  invoiceshelf-postgres-data:
  invoiceshelf-storage:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password}"
db_username = "invoiceshelf"
db_database = "invoiceshelf"

[config]
mounts = []

[[config.domains]]
serviceName = "invoiceshelf-app"
port = 8080
host = "${main_domain}"

[config.env]
INVOICESHELF_HOST = "${main_domain}"
DB_PASSWORD = "${db_password}"
DB_USERNAME = "${db_username}"
DB_DATABASE = "${db_database}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGludm9pY2VzaGVsZi1wb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTVcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGludm9pY2VzaGVsZi1wb3N0Z3Jlcy1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke0RCX1BBU1NXT1JEfVxuICAgICAgLSBQT1NUR1JFU19VU0VSPSR7REJfVVNFUk5BTUV9XG4gICAgICAtIFBPU1RHUkVTX0RCPSR7REJfREFUQUJBU0V9XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5IC1VICR7REJfVVNFUk5BTUV9XCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuXG4gIGludm9pY2VzaGVsZi1hcHA6XG4gICAgaW1hZ2U6IGludm9pY2VzaGVsZi9pbnZvaWNlc2hlbGY6bmlnaHRseVxuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gaW52b2ljZXNoZWxmLXN0b3JhZ2U6L3Zhci93d3cvaHRtbC9zdG9yYWdlXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBIUF9UWj1VVENcbiAgICAgIC0gVElNRVpPTkU9VVRDXG4gICAgICAtIEFQUF9OQU1FPUludm9pY2VTaGVsZlxuICAgICAgLSBBUFBfRU5WPXByb2R1Y3Rpb25cbiAgICAgIC0gQVBQX0RFQlVHPWZhbHNlXG4gICAgICAtIEFQUF9VUkw9aHR0cDovLyR7SU5WT0lDRVNIRUxGX0hPU1R9XG4gICAgICAtIERCX0NPTk5FQ1RJT049cGdzcWxcbiAgICAgIC0gREJfSE9TVD1pbnZvaWNlc2hlbGYtcG9zdGdyZXNcbiAgICAgIC0gREJfUE9SVD01NDMyXG4gICAgICAtIERCX0RBVEFCQVNFPSR7REJfREFUQUJBU0V9XG4gICAgICAtIERCX1VTRVJOQU1FPSR7REJfVVNFUk5BTUV9XG4gICAgICAtIERCX1BBU1NXT1JEPSR7REJfUEFTU1dPUkR9XG4gICAgICAtIENBQ0hFX1NUT1JFPWZpbGVcbiAgICAgIC0gU0VTU0lPTl9EUklWRVI9ZmlsZVxuICAgICAgLSBTRVNTSU9OX0xJRkVUSU1FPTEyMFxuICAgICAgLSBTRVNTSU9OX0VOQ1JZUFQ9dHJ1ZVxuICAgICAgLSBTRVNTSU9OX1BBVEg9L1xuICAgICAgLSBTRVNTSU9OX0RPTUFJTj0ke0lOVk9JQ0VTSEVMRl9IT1NUfVxuICAgICAgLSBTQU5DVFVNX1NUQVRFRlVMX0RPTUFJTlM9JHtJTlZPSUNFU0hFTEZfSE9TVH1cbiAgICAgIC0gU1RBUlRVUF9ERUxBWT0xMFxuICAgIGRlcGVuZHNfb246XG4gICAgICBpbnZvaWNlc2hlbGYtcG9zdGdyZXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG5cbnZvbHVtZXM6XG4gIGludm9pY2VzaGVsZi1wb3N0Z3Jlcy1kYXRhOlxuICBpbnZvaWNlc2hlbGYtc3RvcmFnZTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5kYl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZH1cIlxuZGJfdXNlcm5hbWUgPSBcImludm9pY2VzaGVsZlwiXG5kYl9kYXRhYmFzZSA9IFwiaW52b2ljZXNoZWxmXCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImludm9pY2VzaGVsZi1hcHBcIlxucG9ydCA9IDgwODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5JTlZPSUNFU0hFTEZfSE9TVCA9IFwiJHttYWluX2RvbWFpbn1cIlxuREJfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcbkRCX1VTRVJOQU1FID0gXCIke2RiX3VzZXJuYW1lfVwiXG5EQl9EQVRBQkFTRSA9IFwiJHtkYl9kYXRhYmFzZX1cIlxuIgp9
```

## Links

`invoice`,`business`,`finance`

---

Version:`latest`

InstantDBInstantDB is a real-time database server that provides instant data synchronization and real-time updates for applications.

IPFS (Kubo)IPFS (Kubo) is a decentralized peer-to-peer file sharing and storage network node. Host your own IPFS gateway and API.

### On this page

ConfigurationBase64LinksTags