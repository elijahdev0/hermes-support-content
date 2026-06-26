---
title: "Wanderer | Dokploy"
source: "https://docs.dokploy.com/docs/templates/wanderer"
category: dokploy-docs
created: "2026-06-25T17:22:01.420Z"
---

Wanderer | Dokploy

# Wanderer

Copy as Markdown

Wanderer is a self-hosted mapping and geolocation platform powered by Meilisearch, PocketBase, and a web frontend.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  search:
    image: getmeili/meilisearch:v1.11.3
    environment:
      MEILI_URL: http://search:7700
      MEILI_MASTER_KEY: ${MEILI_MASTER_KEY}
      MEILI_NO_ANALYTICS: "true"
    volumes:
      - search-data:/meili_data/data.ms
    restart: unless-stopped
    healthcheck:
      test: curl --fail http://localhost:7700/health || exit 1
      interval: 15s
      retries: 10
      start_period: 20s
      timeout: 10s

  db:
    image: flomp/wanderer-db
    depends_on:
      search:
        condition: service_healthy
    environment:
      MEILI_URL: http://search:7700
      MEILI_MASTER_KEY: ${MEILI_MASTER_KEY}
      POCKETBASE_ENCRYPTION_KEY: ${POCKETBASE_ENCRYPTION_KEY}
      ORIGIN: ${ORIGIN}
    volumes:
      - db-data:/pb_data
    restart: unless-stopped
    healthcheck:
      test: wget --spider -q http://localhost:8090/health || exit 1
      interval: 15s
      retries: 10
      start_period: 20s
      timeout: 10s

  web:
    image: flomp/wanderer-web
    depends_on:
      search:
        condition: service_healthy
      db:
        condition: service_healthy
    environment:
      MEILI_URL: http://search:7700
      MEILI_MASTER_KEY: ${MEILI_MASTER_KEY}
      ORIGIN: ${ORIGIN}
      BODY_SIZE_LIMIT: Infinity
      PUBLIC_POCKETBASE_URL: http://db:8090
      PUBLIC_DISABLE_SIGNUP: "false"
      UPLOAD_FOLDER: /app/uploads
      UPLOAD_USER: ${UPLOAD_USER}
      UPLOAD_PASSWORD: ${UPLOAD_PASSWORD}
      PUBLIC_VALHALLA_URL: https://valhalla1.openstreetmap.de
      PUBLIC_NOMINATIM_URL: https://nominatim.openstreetmap.org
    volumes:
      - uploads:/app/uploads
    restart: unless-stopped
    healthcheck:
      test: curl --fail http://localhost:3000/ || exit 1
      interval: 15s
      retries: 10
      start_period: 20s
      timeout: 10s

volumes:
  search-data: {}
  db-data: {}
  uploads: {}
```

```
[variables]
main_domain = "${domain}"
meili_master_key = "${password:32}"
pocketbase_key = "${password:32}"
upload_user = "${username}"
upload_password = "${password:16}"

[config]

[[config.domains]]
serviceName = "web"
port = 3000
host = "${main_domain}"

[[config.domains]]
serviceName = "db"
port = 8090
host = "db.${main_domain}"

[[config.domains]]
serviceName = "search"
port = 7700
host = "search.${main_domain}"

[config.env]
MEILI_MASTER_KEY = "${meili_master_key}"
POCKETBASE_ENCRYPTION_KEY = "${pocketbase_key}"
UPLOAD_USER = "${upload_user}"
UPLOAD_PASSWORD = "${upload_password}"
ORIGIN = "http://${main_domain}"

[[config.mounts]]
serviceName = "search"
volumeName = "search-data"
mountPath = "/meili_data/data.ms"

[[config.mounts]]
serviceName = "db"
volumeName = "db-data"
mountPath = "/pb_data"

[[config.mounts]]
serviceName = "web"
volumeName = "uploads"
mountPath = "/app/uploads"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHNlYXJjaDpcbiAgICBpbWFnZTogZ2V0bWVpbGkvbWVpbGlzZWFyY2g6djEuMTEuM1xuICAgIGVudmlyb25tZW50OlxuICAgICAgTUVJTElfVVJMOiBodHRwOi8vc2VhcmNoOjc3MDBcbiAgICAgIE1FSUxJX01BU1RFUl9LRVk6ICR7TUVJTElfTUFTVEVSX0tFWX1cbiAgICAgIE1FSUxJX05PX0FOQUxZVElDUzogXCJ0cnVlXCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBzZWFyY2gtZGF0YTovbWVpbGlfZGF0YS9kYXRhLm1zXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IGN1cmwgLS1mYWlsIGh0dHA6Ly9sb2NhbGhvc3Q6NzcwMC9oZWFsdGggfHwgZXhpdCAxXG4gICAgICBpbnRlcnZhbDogMTVzXG4gICAgICByZXRyaWVzOiAxMFxuICAgICAgc3RhcnRfcGVyaW9kOiAyMHNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuXG4gIGRiOlxuICAgIGltYWdlOiBmbG9tcC93YW5kZXJlci1kYlxuICAgIGRlcGVuZHNfb246XG4gICAgICBzZWFyY2g6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNRUlMSV9VUkw6IGh0dHA6Ly9zZWFyY2g6NzcwMFxuICAgICAgTUVJTElfTUFTVEVSX0tFWTogJHtNRUlMSV9NQVNURVJfS0VZfVxuICAgICAgUE9DS0VUQkFTRV9FTkNSWVBUSU9OX0tFWTogJHtQT0NLRVRCQVNFX0VOQ1JZUFRJT05fS0VZfVxuICAgICAgT1JJR0lOOiAke09SSUdJTn1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYi1kYXRhOi9wYl9kYXRhXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IHdnZXQgLS1zcGlkZXIgLXEgaHR0cDovL2xvY2FsaG9zdDo4MDkwL2hlYWx0aCB8fCBleGl0IDFcbiAgICAgIGludGVydmFsOiAxNXNcbiAgICAgIHJldHJpZXM6IDEwXG4gICAgICBzdGFydF9wZXJpb2Q6IDIwc1xuICAgICAgdGltZW91dDogMTBzXG5cbiAgd2ViOlxuICAgIGltYWdlOiBmbG9tcC93YW5kZXJlci13ZWJcbiAgICBkZXBlbmRzX29uOlxuICAgICAgc2VhcmNoOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgZGI6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNRUlMSV9VUkw6IGh0dHA6Ly9zZWFyY2g6NzcwMFxuICAgICAgTUVJTElfTUFTVEVSX0tFWTogJHtNRUlMSV9NQVNURVJfS0VZfVxuICAgICAgT1JJR0lOOiAke09SSUdJTn1cbiAgICAgIEJPRFlfU0laRV9MSU1JVDogSW5maW5pdHlcbiAgICAgIFBVQkxJQ19QT0NLRVRCQVNFX1VSTDogaHR0cDovL2RiOjgwOTBcbiAgICAgIFBVQkxJQ19ESVNBQkxFX1NJR05VUDogXCJmYWxzZVwiXG4gICAgICBVUExPQURfRk9MREVSOiAvYXBwL3VwbG9hZHNcbiAgICAgIFVQTE9BRF9VU0VSOiAke1VQTE9BRF9VU0VSfVxuICAgICAgVVBMT0FEX1BBU1NXT1JEOiAke1VQTE9BRF9QQVNTV09SRH1cbiAgICAgIFBVQkxJQ19WQUxIQUxMQV9VUkw6IGh0dHBzOi8vdmFsaGFsbGExLm9wZW5zdHJlZXRtYXAuZGVcbiAgICAgIFBVQkxJQ19OT01JTkFUSU1fVVJMOiBodHRwczovL25vbWluYXRpbS5vcGVuc3RyZWV0bWFwLm9yZ1xuICAgIHZvbHVtZXM6XG4gICAgICAtIHVwbG9hZHM6L2FwcC91cGxvYWRzXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IGN1cmwgLS1mYWlsIGh0dHA6Ly9sb2NhbGhvc3Q6MzAwMC8gfHwgZXhpdCAxXG4gICAgICBpbnRlcnZhbDogMTVzXG4gICAgICByZXRyaWVzOiAxMFxuICAgICAgc3RhcnRfcGVyaW9kOiAyMHNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuXG52b2x1bWVzOlxuICBzZWFyY2gtZGF0YToge31cbiAgZGItZGF0YToge31cbiAgdXBsb2Fkczoge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5tZWlsaV9tYXN0ZXJfa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5wb2NrZXRiYXNlX2tleSA9IFwiJHtwYXNzd29yZDozMn1cIlxudXBsb2FkX3VzZXIgPSBcIiR7dXNlcm5hbWV9XCJcbnVwbG9hZF9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoxNn1cIlxuXG5bY29uZmlnXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ3ZWJcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZGJcIlxucG9ydCA9IDgwOTBcbmhvc3QgPSBcImRiLiR7bWFpbl9kb21haW59XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwic2VhcmNoXCJcbnBvcnQgPSA3NzAwXG5ob3N0ID0gXCJzZWFyY2guJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbk1FSUxJX01BU1RFUl9LRVkgPSBcIiR7bWVpbGlfbWFzdGVyX2tleX1cIlxuUE9DS0VUQkFTRV9FTkNSWVBUSU9OX0tFWSA9IFwiJHtwb2NrZXRiYXNlX2tleX1cIlxuVVBMT0FEX1VTRVIgPSBcIiR7dXBsb2FkX3VzZXJ9XCJcblVQTE9BRF9QQVNTV09SRCA9IFwiJHt1cGxvYWRfcGFzc3dvcmR9XCJcbk9SSUdJTiA9IFwiaHR0cDovLyR7bWFpbl9kb21haW59XCJcblxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcInNlYXJjaFwiXG52b2x1bWVOYW1lID0gXCJzZWFyY2gtZGF0YVwiXG5tb3VudFBhdGggPSBcIi9tZWlsaV9kYXRhL2RhdGEubXNcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcImRiXCJcbnZvbHVtZU5hbWUgPSBcImRiLWRhdGFcIlxubW91bnRQYXRoID0gXCIvcGJfZGF0YVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwid2ViXCJcbnZvbHVtZU5hbWUgPSBcInVwbG9hZHNcIlxubW91bnRQYXRoID0gXCIvYXBwL3VwbG9hZHNcIlxuIgp9
```

## Links

`mapping`,`geolocation`,`search`,`self-hosted`

---

Version:`1.0.0`

WallosWallos is a self-hosted subscription tracking application that helps you manage and monitor your subscriptions, providing insights into your spending habits.

Web-CheckWeb-Check is a powerful all-in-one website analyzer that provides detailed insights into any website's security, performance, and functionality.

### On this page

ConfigurationBase64LinksTags