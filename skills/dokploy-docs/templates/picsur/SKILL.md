---
title: "Picsur | Dokploy"
source: "https://docs.dokploy.com/docs/templates/picsur"
category: dokploy-docs
created: "2026-06-25T17:21:56.647Z"
---

Picsur | Dokploy

# Picsur

Copy as Markdown

Picsur is a simple, self-hosted image hosting service with an admin interface and Postgres backend.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  picsur:
    image: ghcr.io/caramelfur/picsur:latest
    restart: unless-stopped
    environment:
      PICSUR_DB_HOST: picsur_postgres
      PICSUR_DB_PORT: 5432
      PICSUR_DB_USERNAME: picsur
      PICSUR_DB_PASSWORD: ${POSTGRES_PASSWORD}
      PICSUR_DB_DATABASE: picsur
      PICSUR_ADMIN_PASSWORD: ${ADMIN_PASSWORD}
      PICSUR_JWT_SECRET: ${JWT_SECRET}
    expose:
      - 8080

  picsur_postgres:
    image: postgres:17-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: picsur
      POSTGRES_USER: picsur
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - picsur-data:/var/lib/postgresql/data

volumes:
  picsur-data: {}
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password:32}"
admin_password = "${password:32}"
jwt_secret = "${jwt:jwt_secret}"

[config]

[[config.domains]]
serviceName = "picsur"
port = 8080
host = "${main_domain}"

[config.env]
"PICSUR_DB_PASSWORD" = "${postgres_password}"
"PICSUR_ADMIN_PASSWORD" = "${admin_password}"
"PICSUR_JWT_SECRET" = "${jwt_secret}"
"POSTGRES_PASSWORD" = "${postgres_password}"

[[config.mounts]]
name = "picsur-data"
serviceName = "picsur_postgres"
mountPath = "/var/lib/postgresql/data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHBpY3N1cjpcbiAgICBpbWFnZTogZ2hjci5pby9jYXJhbWVsZnVyL3BpY3N1cjpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgUElDU1VSX0RCX0hPU1Q6IHBpY3N1cl9wb3N0Z3Jlc1xuICAgICAgUElDU1VSX0RCX1BPUlQ6IDU0MzJcbiAgICAgIFBJQ1NVUl9EQl9VU0VSTkFNRTogcGljc3VyXG4gICAgICBQSUNTVVJfREJfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQSUNTVVJfREJfREFUQUJBU0U6IHBpY3N1clxuICAgICAgUElDU1VSX0FETUlOX1BBU1NXT1JEOiAke0FETUlOX1BBU1NXT1JEfVxuICAgICAgUElDU1VSX0pXVF9TRUNSRVQ6ICR7SldUX1NFQ1JFVH1cbiAgICBleHBvc2U6XG4gICAgICAtIDgwODBcblxuICBwaWNzdXJfcG9zdGdyZXM6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE3LWFscGluZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19EQjogcGljc3VyXG4gICAgICBQT1NUR1JFU19VU0VSOiBwaWNzdXJcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBpY3N1ci1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuXG52b2x1bWVzOlxuICBwaWNzdXItZGF0YToge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuYWRtaW5fcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmp3dF9zZWNyZXQgPSBcIiR7and0Omp3dF9zZWNyZXR9XCJcblxuW2NvbmZpZ11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicGljc3VyXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuXCJQSUNTVVJfREJfUEFTU1dPUkRcIiA9IFwiJHtwb3N0Z3Jlc19wYXNzd29yZH1cIlxuXCJQSUNTVVJfQURNSU5fUEFTU1dPUkRcIiA9IFwiJHthZG1pbl9wYXNzd29yZH1cIlxuXCJQSUNTVVJfSldUX1NFQ1JFVFwiID0gXCIke2p3dF9zZWNyZXR9XCJcblwiUE9TVEdSRVNfUEFTU1dPUkRcIiA9IFwiJHtwb3N0Z3Jlc19wYXNzd29yZH1cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxubmFtZSA9IFwicGljc3VyLWRhdGFcIlxuc2VydmljZU5hbWUgPSBcInBpY3N1cl9wb3N0Z3Jlc1wiXG5tb3VudFBhdGggPSBcIi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVwiXG4iCn0=
```

## Links

`image-hosting`,`media`,`self-hosted`,`postgres`

---

Version:`latest`

PhpmyadminPhpmyadmin is a free and open-source web interface for MySQL and MariaDB that allows you to manage your databases.

PinchflatPinchflat is a self-hosted YouTube downloader that allows you to download videos and playlists with a simple web interface.

### On this page

ConfigurationBase64LinksTags