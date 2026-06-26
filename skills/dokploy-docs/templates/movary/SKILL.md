---
title: "Movary | Dokploy"
source: "https://docs.dokploy.com/docs/templates/movary"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

Movary | Dokploy

# Movary

Copy as Markdown

Movary is a self-hosted platform for tracking and managing your watched movies using TMDB.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  movary:
    image: leepeuker/movary:${MOVARY_VERSION:-latest}
    restart: unless-stopped
    ports:
      - "8080"
    environment:
      # TMDB API configuration
      TMDB_API_KEY: ${TMDB_API_KEY}
      # Database configuration
      DATABASE_MODE: "mysql"
      DATABASE_MYSQL_HOST: "mysql"
      DATABASE_MYSQL_NAME: "movary"
      DATABASE_MYSQL_USER: "movary_user"
      DATABASE_MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      # Application settings
      APP_URL: ${APP_URL:-http://localhost:8080}
      APP_ENV: ${APP_ENV:-production}
    volumes:
      - movary_storage:/app/storage
    depends_on:
      - mysql

  mysql:
    image: mysql:${MYSQL_VERSION:-8.0}
    restart: unless-stopped
    environment:
      MYSQL_DATABASE: "movary"
      MYSQL_USER: "movary_user"
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      # MySQL optimization
      MYSQL_INNODB_BUFFER_POOL_SIZE: "128M"
      MYSQL_INNODB_LOG_FILE_SIZE: "64M"
    volumes:
      - movary_db:/var/lib/mysql
    command: --default-authentication-plugin=mysql_native_password

volumes:
  movary_db:
  movary_storage:
```

```
[variables]
main_domain = "${domain}"
tmdb_api_key = ""
mysql_password = "${password:32}"
mysql_root_password = "${password:32}"

[config.env]
MOVARY_VERSION = "latest"
MYSQL_VERSION = "8.0"
TMDB_API_KEY = "${tmdb_api_key}"
MYSQL_PASSWORD = "${mysql_password}"
MYSQL_ROOT_PASSWORD = "${mysql_root_password}"
APP_URL = "http://${main_domain}"
APP_ENV = "production"

[config]
mounts = []

[[config.domains]]
serviceName = "movary"
port = 8080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBtb3Zhcnk6XG4gICAgaW1hZ2U6IGxlZXBldWtlci9tb3Zhcnk6JHtNT1ZBUllfVkVSU0lPTjotbGF0ZXN0fVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIFwiODA4MFwiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAjIFRNREIgQVBJIGNvbmZpZ3VyYXRpb25cbiAgICAgIFRNREJfQVBJX0tFWTogJHtUTURCX0FQSV9LRVl9XG4gICAgICAjIERhdGFiYXNlIGNvbmZpZ3VyYXRpb25cbiAgICAgIERBVEFCQVNFX01PREU6IFwibXlzcWxcIlxuICAgICAgREFUQUJBU0VfTVlTUUxfSE9TVDogXCJteXNxbFwiXG4gICAgICBEQVRBQkFTRV9NWVNRTF9OQU1FOiBcIm1vdmFyeVwiXG4gICAgICBEQVRBQkFTRV9NWVNRTF9VU0VSOiBcIm1vdmFyeV91c2VyXCJcbiAgICAgIERBVEFCQVNFX01ZU1FMX1BBU1NXT1JEOiAke01ZU1FMX1BBU1NXT1JEfVxuICAgICAgIyBBcHBsaWNhdGlvbiBzZXR0aW5nc1xuICAgICAgQVBQX1VSTDogJHtBUFBfVVJMOi1odHRwOi8vbG9jYWxob3N0OjgwODB9XG4gICAgICBBUFBfRU5WOiAke0FQUF9FTlY6LXByb2R1Y3Rpb259XG4gICAgdm9sdW1lczpcbiAgICAgIC0gbW92YXJ5X3N0b3JhZ2U6L2FwcC9zdG9yYWdlXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gbXlzcWxcblxuICBteXNxbDpcbiAgICBpbWFnZTogbXlzcWw6JHtNWVNRTF9WRVJTSU9OOi04LjB9XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE1ZU1FMX0RBVEFCQVNFOiBcIm1vdmFyeVwiXG4gICAgICBNWVNRTF9VU0VSOiBcIm1vdmFyeV91c2VyXCJcbiAgICAgIE1ZU1FMX1BBU1NXT1JEOiAke01ZU1FMX1BBU1NXT1JEfVxuICAgICAgTVlTUUxfUk9PVF9QQVNTV09SRDogJHtNWVNRTF9ST09UX1BBU1NXT1JEfVxuICAgICAgIyBNeVNRTCBvcHRpbWl6YXRpb25cbiAgICAgIE1ZU1FMX0lOTk9EQl9CVUZGRVJfUE9PTF9TSVpFOiBcIjEyOE1cIlxuICAgICAgTVlTUUxfSU5OT0RCX0xPR19GSUxFX1NJWkU6IFwiNjRNXCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBtb3ZhcnlfZGI6L3Zhci9saWIvbXlzcWxcbiAgICBjb21tYW5kOiAtLWRlZmF1bHQtYXV0aGVudGljYXRpb24tcGx1Z2luPW15c3FsX25hdGl2ZV9wYXNzd29yZFxuXG52b2x1bWVzOlxuICBtb3ZhcnlfZGI6XG4gIG1vdmFyeV9zdG9yYWdlOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnRtZGJfYXBpX2tleSA9IFwiXCJcbm15c3FsX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5teXNxbF9yb290X3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWcuZW52XVxuTU9WQVJZX1ZFUlNJT04gPSBcImxhdGVzdFwiXG5NWVNRTF9WRVJTSU9OID0gXCI4LjBcIlxuVE1EQl9BUElfS0VZID0gXCIke3RtZGJfYXBpX2tleX1cIlxuTVlTUUxfUEFTU1dPUkQgPSBcIiR7bXlzcWxfcGFzc3dvcmR9XCJcbk1ZU1FMX1JPT1RfUEFTU1dPUkQgPSBcIiR7bXlzcWxfcm9vdF9wYXNzd29yZH1cIlxuQVBQX1VSTCA9IFwiaHR0cDovLyR7bWFpbl9kb21haW59XCJcbkFQUF9FTlYgPSBcInByb2R1Y3Rpb25cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibW92YXJ5XCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiIgp9
```

## Links

`media`,`movies`,`movie-tracker`,`self-hosted`,`plex`,`jellyfin`,`emby`,`kodi`,`trakt`,`letterboxd`,`netflix`,`tmdb`,`statistics`,`rating`

---

Version:`latest`

MorphosMorphos is a lightweight service for distributed operations and orchestration.

MuleSoft ESB Runtime Community EditionMuleSoft ESB Runtime is a lightweight, Java-based integration platform that allows you to easily integrate applications, data sources, and APIs. It provides powerful connectors and data transformation capabilities for building robust integration solutions.

### On this page

ConfigurationBase64LinksTags