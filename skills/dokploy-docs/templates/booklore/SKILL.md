---
title: "Booklore | Dokploy"
source: "https://docs.dokploy.com/docs/templates/booklore"
category: dokploy-docs
created: "2026-06-25T17:21:42.677Z"
---

Booklore | Dokploy

# Booklore

Copy as Markdown

Booklore is an application for managing and serving book-related data, backed by a MariaDB database.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  booklore:
    image: ghcr.io/booklore-app/booklore:${BOOKLORE_IMAGE_TAG}
    environment:
      - DATABASE_URL=jdbc:mariadb://mariadb:3306/${MYSQL_DATABASE}
      - DATABASE_USERNAME=${MYSQL_USER}
      - DATABASE_PASSWORD=${MYSQL_PASSWORD}
    depends_on:
      mariadb:
        condition: service_healthy
    ports:
      - 6060
    volumes:
      - booklore-data:/app/data
      - booklore-books:/books

  mariadb:
    image: lscr.io/linuxserver/mariadb:latest
    environment:
      - PUID=${PUID}
      - PGID=${PGID}
      - TZ=${TZ}
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
      - MYSQL_DATABASE=${MYSQL_DATABASE}
      - MYSQL_USER=${MYSQL_USER}
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}
    volumes:
      - mariadb-config:/config
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "mariadb-admin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  booklore-data: {}
  booklore-books: {}
  mariadb-config: {}
```

```
[variables]
main_domain = "${domain}"
app_password = "${password:32}"
db_root_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "booklore"
port = 6060
host = "${main_domain}"

[config.env]
BOOKLORE_IMAGE_TAG = "latest"
PUID = "1000"
PGID = "1000"
TZ = "Etc/UTC"
MYSQL_DATABASE = "booklore"
MYSQL_USER = "booklore"
# API Key
MYSQL_PASSWORD = "${app_password}"
# API Key
MYSQL_ROOT_PASSWORD = "${db_root_password}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBib29rbG9yZTpcbiAgICBpbWFnZTogZ2hjci5pby9ib29rbG9yZS1hcHAvYm9va2xvcmU6JHtCT09LTE9SRV9JTUFHRV9UQUd9XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIERBVEFCQVNFX1VSTD1qZGJjOm1hcmlhZGI6Ly9tYXJpYWRiOjMzMDYvJHtNWVNRTF9EQVRBQkFTRX1cbiAgICAgIC0gREFUQUJBU0VfVVNFUk5BTUU9JHtNWVNRTF9VU0VSfVxuICAgICAgLSBEQVRBQkFTRV9QQVNTV09SRD0ke01ZU1FMX1BBU1NXT1JEfVxuICAgIGRlcGVuZHNfb246XG4gICAgICBtYXJpYWRiOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIHBvcnRzOlxuICAgICAgLSA2MDYwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gYm9va2xvcmUtZGF0YTovYXBwL2RhdGFcbiAgICAgIC0gYm9va2xvcmUtYm9va3M6L2Jvb2tzXG5cbiAgbWFyaWFkYjpcbiAgICBpbWFnZTogbHNjci5pby9saW51eHNlcnZlci9tYXJpYWRiOmxhdGVzdFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQVUlEPSR7UFVJRH1cbiAgICAgIC0gUEdJRD0ke1BHSUR9XG4gICAgICAtIFRaPSR7VFp9XG4gICAgICAtIE1ZU1FMX1JPT1RfUEFTU1dPUkQ9JHtNWVNRTF9ST09UX1BBU1NXT1JEfVxuICAgICAgLSBNWVNRTF9EQVRBQkFTRT0ke01ZU1FMX0RBVEFCQVNFfVxuICAgICAgLSBNWVNRTF9VU0VSPSR7TVlTUUxfVVNFUn1cbiAgICAgIC0gTVlTUUxfUEFTU1dPUkQ9JHtNWVNRTF9QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBtYXJpYWRiLWNvbmZpZzovY29uZmlnXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcIm1hcmlhZGItYWRtaW5cIiwgXCJwaW5nXCIsIFwiLWhcIiwgXCJsb2NhbGhvc3RcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG5cbnZvbHVtZXM6XG4gIGJvb2tsb3JlLWRhdGE6IHt9XG4gIGJvb2tsb3JlLWJvb2tzOiB7fVxuICBtYXJpYWRiLWNvbmZpZzoge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5hcHBfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmRiX3Jvb3RfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImJvb2tsb3JlXCJcbnBvcnQgPSA2MDYwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuQk9PS0xPUkVfSU1BR0VfVEFHID0gXCJsYXRlc3RcIlxuUFVJRCA9IFwiMTAwMFwiXG5QR0lEID0gXCIxMDAwXCJcblRaID0gXCJFdGMvVVRDXCJcbk1ZU1FMX0RBVEFCQVNFID0gXCJib29rbG9yZVwiXG5NWVNRTF9VU0VSID0gXCJib29rbG9yZVwiXG4jIEFQSSBLZXlcbk1ZU1FMX1BBU1NXT1JEID0gXCIke2FwcF9wYXNzd29yZH1cIlxuIyBBUEkgS2V5XG5NWVNRTF9ST09UX1BBU1NXT1JEID0gXCIke2RiX3Jvb3RfcGFzc3dvcmR9XCJcblxuW1tjb25maWcubW91bnRzXV0iCn0=
```

## Links

`books`,`library`,`database`,`mariadb`

---

Version:`latest`

bolt.diyPrompt, run, edit, and deploy full-stack web applications using any LLM you want!

BookStackBookStack is a self-hosted platform for creating beautiful, feature-rich documentation sites.

### On this page

ConfigurationBase64LinksTags