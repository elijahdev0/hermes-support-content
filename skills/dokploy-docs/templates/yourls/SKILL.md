---
title: "YOURLS | Dokploy"
source: "https://docs.dokploy.com/docs/templates/yourls"
category: dokploy-docs
created: "2026-06-25T17:22:02.523Z"
---

YOURLS | Dokploy

# YOURLS

Copy as Markdown

YOURLS (Your Own URL Shortener) is a set of PHP scripts that will allow you to run your own URL shortening service (a la TinyURL or Bitly).

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.7'

services:
  yourls-app:
    image: yourls:1.9.2

    environment:
      YOURLS_SITE: https://${YOURLS_HOST}
      YOURLS_USER: ${YOURLS_ADMIN_USER}
      YOURLS_PASS: ${YOURLS_ADMIN_PASSWORD}
      YOURLS_DB_HOST: yourls-mysql
      YOURLS_DB_USER: yourls
      YOURLS_DB_PASS: ${MYSQL_PASSWORD}
      YOURLS_DB_NAME: yourls
    volumes:
      - yourls-data:/var/www/html
    depends_on:
      yourls-mysql:
        condition: service_healthy
    restart: always

  yourls-mysql:
    image: mysql:5.7

    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: yourls
      MYSQL_USER: yourls
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    volumes:
      - yourls-mysql-data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u$$MYSQL_USER", "-p$$MYSQL_PASSWORD"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: always

volumes:
  yourls-data:
  yourls-mysql-data:
```

```
[variables]
main_domain = "${domain}"
mysql_password = "${password}"
mysql_root_password = "${password}"
admin_password = "${password}"

[config]
mounts = []

[[config.domains]]
serviceName = "yourls-app"
port = 80
host = "${main_domain}"

[config.env]
YOURLS_HOST = "${main_domain}"
YOURLS_ADMIN_USER = "admin"
YOURLS_ADMIN_PASSWORD = "${admin_password}"
MYSQL_PASSWORD = "${mysql_password}"
MYSQL_ROOT_PASSWORD = "${mysql_root_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjcnXG5cbnNlcnZpY2VzOlxuICB5b3VybHMtYXBwOlxuICAgIGltYWdlOiB5b3VybHM6MS45LjJcblxuICAgIGVudmlyb25tZW50OlxuICAgICAgWU9VUkxTX1NJVEU6IGh0dHBzOi8vJHtZT1VSTFNfSE9TVH1cbiAgICAgIFlPVVJMU19VU0VSOiAke1lPVVJMU19BRE1JTl9VU0VSfVxuICAgICAgWU9VUkxTX1BBU1M6ICR7WU9VUkxTX0FETUlOX1BBU1NXT1JEfVxuICAgICAgWU9VUkxTX0RCX0hPU1Q6IHlvdXJscy1teXNxbFxuICAgICAgWU9VUkxTX0RCX1VTRVI6IHlvdXJsc1xuICAgICAgWU9VUkxTX0RCX1BBU1M6ICR7TVlTUUxfUEFTU1dPUkR9XG4gICAgICBZT1VSTFNfREJfTkFNRTogeW91cmxzXG4gICAgdm9sdW1lczpcbiAgICAgIC0geW91cmxzLWRhdGE6L3Zhci93d3cvaHRtbFxuICAgIGRlcGVuZHNfb246XG4gICAgICB5b3VybHMtbXlzcWw6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgcmVzdGFydDogYWx3YXlzXG5cbiAgeW91cmxzLW15c3FsOlxuICAgIGltYWdlOiBteXNxbDo1LjdcblxuICAgIGVudmlyb25tZW50OlxuICAgICAgTVlTUUxfUk9PVF9QQVNTV09SRDogJHtNWVNRTF9ST09UX1BBU1NXT1JEfVxuICAgICAgTVlTUUxfREFUQUJBU0U6IHlvdXJsc1xuICAgICAgTVlTUUxfVVNFUjogeW91cmxzXG4gICAgICBNWVNRTF9QQVNTV09SRDogJHtNWVNRTF9QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSB5b3VybHMtbXlzcWwtZGF0YTovdmFyL2xpYi9teXNxbFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwibXlzcWxhZG1pblwiLCBcInBpbmdcIiwgXCItaFwiLCBcImxvY2FsaG9zdFwiLCBcIi11JCRNWVNRTF9VU0VSXCIsIFwiLXAkJE1ZU1FMX1BBU1NXT1JEXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuXG52b2x1bWVzOlxuICB5b3VybHMtZGF0YTpcbiAgeW91cmxzLW15c3FsLWRhdGE6ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5teXNxbF9wYXNzd29yZCA9IFwiJHtwYXNzd29yZH1cIlxubXlzcWxfcm9vdF9wYXNzd29yZCA9IFwiJHtwYXNzd29yZH1cIlxuYWRtaW5fcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmR9XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInlvdXJscy1hcHBcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuWU9VUkxTX0hPU1QgPSBcIiR7bWFpbl9kb21haW59XCJcbllPVVJMU19BRE1JTl9VU0VSID0gXCJhZG1pblwiXG5ZT1VSTFNfQURNSU5fUEFTU1dPUkQgPSBcIiR7YWRtaW5fcGFzc3dvcmR9XCJcbk1ZU1FMX1BBU1NXT1JEID0gXCIke215c3FsX3Bhc3N3b3JkfVwiXG5NWVNRTF9ST09UX1BBU1NXT1JEID0gXCIke215c3FsX3Jvb3RfcGFzc3dvcmR9XCJcbiIKfQ==
```

## Links

`url-shortener`,`php`

---

Version:`1.9.2`

YamtrackYamtrack is a self-hosted anime and manga tracker with Redis backend support.

yt-dlp-webuiyt-dlp-webui is a web interface for yt-dlp, allowing you to download videos and audio from various platforms with a simple web UI.

### On this page

ConfigurationBase64LinksTags