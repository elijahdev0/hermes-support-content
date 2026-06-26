---
title: "Photoprism | Dokploy"
source: "https://docs.dokploy.com/docs/templates/photoprism"
category: dokploy-docs
created: "2026-06-25T17:21:56.647Z"
---

Photoprism | Dokploy

# Photoprism

Copy as Markdown

PhotoPrism® is an AI-Powered Photos App for the Decentralized Web. It makes use of the latest technologies to tag and find pictures automatically without getting in your way.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  photoprism:
    image: photoprism/photoprism:latest
    stop_grace_period: 10s
    depends_on:
      - mariadb
    security_opt:
      - seccomp:unconfined
      - apparmor:unconfined

    environment:
      PHOTOPRISM_ADMIN_USER: "admin"
      PHOTOPRISM_ADMIN_PASSWORD: ${ADMIN_PASSWORD}
      PHOTOPRISM_AUTH_MODE: "password"
      PHOTOPRISM_SITE_URL: "http://localhost:2342/"
      PHOTOPRISM_DISABLE_TLS: "false"
      PHOTOPRISM_DEFAULT_TLS: "false"
      PHOTOPRISM_ORIGINALS_LIMIT: 5000               # file size limit for originals in MB (increase for high-res video)
      PHOTOPRISM_HTTP_COMPRESSION: "gzip"
      PHOTOPRISM_LOG_LEVEL: "info"                   # log level: trace, debug, info, warning, error, fatal, or panic
      PHOTOPRISM_READONLY: "false"
      PHOTOPRISM_EXPERIMENTAL: "false"
      PHOTOPRISM_DISABLE_CHOWN: "false"
      PHOTOPRISM_DISABLE_WEBDAV: "false"
      PHOTOPRISM_DISABLE_SETTINGS: "false"
      PHOTOPRISM_DISABLE_TENSORFLOW: "false"
      PHOTOPRISM_DISABLE_FACES: "false"
      PHOTOPRISM_DISABLE_CLASSIFICATION: "false"
      PHOTOPRISM_DISABLE_VECTORS: "false"
      PHOTOPRISM_DISABLE_RAW: "false"
      PHOTOPRISM_RAW_PRESETS: "false"
      PHOTOPRISM_SIDECAR_YAML: "true"
      PHOTOPRISM_BACKUP_ALBUMS: "true"
      PHOTOPRISM_BACKUP_DATABASE: "true"
      PHOTOPRISM_BACKUP_SCHEDULE: "daily"
      PHOTOPRISM_INDEX_SCHEDULE: ""
      PHOTOPRISM_AUTO_INDEX: 300
      PHOTOPRISM_AUTO_IMPORT: -1
      PHOTOPRISM_DETECT_NSFW: "false"
      PHOTOPRISM_UPLOAD_NSFW: "true"
      PHOTOPRISM_DATABASE_DRIVER: "mysql"
      PHOTOPRISM_DATABASE_SERVER: "mariadb:3306"
      PHOTOPRISM_DATABASE_NAME: "photoprism"
      PHOTOPRISM_DATABASE_USER: "photoprism"
      PHOTOPRISM_DATABASE_PASSWORD: "insecure"
      PHOTOPRISM_SITE_CAPTION: "AI-Powered Photos App"
      PHOTOPRISM_SITE_DESCRIPTION: ""
      PHOTOPRISM_SITE_AUTHOR: ""
    working_dir:
      "/photoprism"
    volumes:
      - pictures:/photoprism/originals
      - storage-data:/photoprism/storage

  mariadb:
    image: mariadb:11
    restart: unless-stopped
    stop_grace_period: 5s

    security_opt:
      - seccomp:unconfined
      - apparmor:unconfined
    volumes:
      - db-data:/var/lib/mysql
    environment:
      MARIADB_AUTO_UPGRADE: "1"
      MARIADB_INITDB_SKIP_TZINFO: "1"
      MARIADB_DATABASE: "photoprism"
      MARIADB_USER: "photoprism"
      MARIADB_PASSWORD: "insecure"
      MARIADB_ROOT_PASSWORD: "insecure"

volumes:
  db-data:
  storage-data:
  pictures:
```

```
[variables]
main_domain = "${domain}"
admin_password = "${password}"

[config]
mounts = []

[[config.domains]]
serviceName = "photoprism"
port = 2_342
host = "${main_domain}"

[config.env]
BASE_URL = "http://${main_domain}"
ADMIN_PASSWORD = "${admin_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxyXG4gIHBob3RvcHJpc206XHJcbiAgICBpbWFnZTogcGhvdG9wcmlzbS9waG90b3ByaXNtOmxhdGVzdFxyXG4gICAgc3RvcF9ncmFjZV9wZXJpb2Q6IDEwc1xyXG4gICAgZGVwZW5kc19vbjpcclxuICAgICAgLSBtYXJpYWRiXHJcbiAgICBzZWN1cml0eV9vcHQ6XHJcbiAgICAgIC0gc2VjY29tcDp1bmNvbmZpbmVkXHJcbiAgICAgIC0gYXBwYXJtb3I6dW5jb25maW5lZFxyXG5cclxuICAgIGVudmlyb25tZW50OlxyXG4gICAgICBQSE9UT1BSSVNNX0FETUlOX1VTRVI6IFwiYWRtaW5cIlxyXG4gICAgICBQSE9UT1BSSVNNX0FETUlOX1BBU1NXT1JEOiAke0FETUlOX1BBU1NXT1JEfVxyXG4gICAgICBQSE9UT1BSSVNNX0FVVEhfTU9ERTogXCJwYXNzd29yZFwiXHJcbiAgICAgIFBIT1RPUFJJU01fU0lURV9VUkw6IFwiaHR0cDovL2xvY2FsaG9zdDoyMzQyL1wiXHJcbiAgICAgIFBIT1RPUFJJU01fRElTQUJMRV9UTFM6IFwiZmFsc2VcIlxyXG4gICAgICBQSE9UT1BSSVNNX0RFRkFVTFRfVExTOiBcImZhbHNlXCJcclxuICAgICAgUEhPVE9QUklTTV9PUklHSU5BTFNfTElNSVQ6IDUwMDAgICAgICAgICAgICAgICAjIGZpbGUgc2l6ZSBsaW1pdCBmb3Igb3JpZ2luYWxzIGluIE1CIChpbmNyZWFzZSBmb3IgaGlnaC1yZXMgdmlkZW8pXHJcbiAgICAgIFBIT1RPUFJJU01fSFRUUF9DT01QUkVTU0lPTjogXCJnemlwXCJcclxuICAgICAgUEhPVE9QUklTTV9MT0dfTEVWRUw6IFwiaW5mb1wiICAgICAgICAgICAgICAgICAgICMgbG9nIGxldmVsOiB0cmFjZSwgZGVidWcsIGluZm8sIHdhcm5pbmcsIGVycm9yLCBmYXRhbCwgb3IgcGFuaWNcclxuICAgICAgUEhPVE9QUklTTV9SRUFET05MWTogXCJmYWxzZVwiXHJcbiAgICAgIFBIT1RPUFJJU01fRVhQRVJJTUVOVEFMOiBcImZhbHNlXCJcclxuICAgICAgUEhPVE9QUklTTV9ESVNBQkxFX0NIT1dOOiBcImZhbHNlXCJcclxuICAgICAgUEhPVE9QUklTTV9ESVNBQkxFX1dFQkRBVjogXCJmYWxzZVwiXHJcbiAgICAgIFBIT1RPUFJJU01fRElTQUJMRV9TRVRUSU5HUzogXCJmYWxzZVwiXHJcbiAgICAgIFBIT1RPUFJJU01fRElTQUJMRV9URU5TT1JGTE9XOiBcImZhbHNlXCJcclxuICAgICAgUEhPVE9QUklTTV9ESVNBQkxFX0ZBQ0VTOiBcImZhbHNlXCJcclxuICAgICAgUEhPVE9QUklTTV9ESVNBQkxFX0NMQVNTSUZJQ0FUSU9OOiBcImZhbHNlXCJcclxuICAgICAgUEhPVE9QUklTTV9ESVNBQkxFX1ZFQ1RPUlM6IFwiZmFsc2VcIlxyXG4gICAgICBQSE9UT1BSSVNNX0RJU0FCTEVfUkFXOiBcImZhbHNlXCJcclxuICAgICAgUEhPVE9QUklTTV9SQVdfUFJFU0VUUzogXCJmYWxzZVwiXHJcbiAgICAgIFBIT1RPUFJJU01fU0lERUNBUl9ZQU1MOiBcInRydWVcIlxyXG4gICAgICBQSE9UT1BSSVNNX0JBQ0tVUF9BTEJVTVM6IFwidHJ1ZVwiXHJcbiAgICAgIFBIT1RPUFJJU01fQkFDS1VQX0RBVEFCQVNFOiBcInRydWVcIlxyXG4gICAgICBQSE9UT1BSSVNNX0JBQ0tVUF9TQ0hFRFVMRTogXCJkYWlseVwiXHJcbiAgICAgIFBIT1RPUFJJU01fSU5ERVhfU0NIRURVTEU6IFwiXCJcclxuICAgICAgUEhPVE9QUklTTV9BVVRPX0lOREVYOiAzMDBcclxuICAgICAgUEhPVE9QUklTTV9BVVRPX0lNUE9SVDogLTFcclxuICAgICAgUEhPVE9QUklTTV9ERVRFQ1RfTlNGVzogXCJmYWxzZVwiXHJcbiAgICAgIFBIT1RPUFJJU01fVVBMT0FEX05TRlc6IFwidHJ1ZVwiXHJcbiAgICAgIFBIT1RPUFJJU01fREFUQUJBU0VfRFJJVkVSOiBcIm15c3FsXCJcclxuICAgICAgUEhPVE9QUklTTV9EQVRBQkFTRV9TRVJWRVI6IFwibWFyaWFkYjozMzA2XCJcclxuICAgICAgUEhPVE9QUklTTV9EQVRBQkFTRV9OQU1FOiBcInBob3RvcHJpc21cIlxyXG4gICAgICBQSE9UT1BSSVNNX0RBVEFCQVNFX1VTRVI6IFwicGhvdG9wcmlzbVwiXHJcbiAgICAgIFBIT1RPUFJJU01fREFUQUJBU0VfUEFTU1dPUkQ6IFwiaW5zZWN1cmVcIlxyXG4gICAgICBQSE9UT1BSSVNNX1NJVEVfQ0FQVElPTjogXCJBSS1Qb3dlcmVkIFBob3RvcyBBcHBcIlxyXG4gICAgICBQSE9UT1BSSVNNX1NJVEVfREVTQ1JJUFRJT046IFwiXCJcclxuICAgICAgUEhPVE9QUklTTV9TSVRFX0FVVEhPUjogXCJcIlxyXG4gICAgd29ya2luZ19kaXI6XHJcbiAgICAgIFwiL3Bob3RvcHJpc21cIlxyXG4gICAgdm9sdW1lczpcclxuICAgICAgLSBwaWN0dXJlczovcGhvdG9wcmlzbS9vcmlnaW5hbHNcclxuICAgICAgLSBzdG9yYWdlLWRhdGE6L3Bob3RvcHJpc20vc3RvcmFnZVxyXG5cclxuICBtYXJpYWRiOlxyXG4gICAgaW1hZ2U6IG1hcmlhZGI6MTFcclxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXHJcbiAgICBzdG9wX2dyYWNlX3BlcmlvZDogNXNcclxuXHJcbiAgICBzZWN1cml0eV9vcHQ6XHJcbiAgICAgIC0gc2VjY29tcDp1bmNvbmZpbmVkXHJcbiAgICAgIC0gYXBwYXJtb3I6dW5jb25maW5lZFxyXG4gICAgdm9sdW1lczpcclxuICAgICAgLSBkYi1kYXRhOi92YXIvbGliL215c3FsXHJcbiAgICBlbnZpcm9ubWVudDpcclxuICAgICAgTUFSSUFEQl9BVVRPX1VQR1JBREU6IFwiMVwiXHJcbiAgICAgIE1BUklBREJfSU5JVERCX1NLSVBfVFpJTkZPOiBcIjFcIlxyXG4gICAgICBNQVJJQURCX0RBVEFCQVNFOiBcInBob3RvcHJpc21cIlxyXG4gICAgICBNQVJJQURCX1VTRVI6IFwicGhvdG9wcmlzbVwiXHJcbiAgICAgIE1BUklBREJfUEFTU1dPUkQ6IFwiaW5zZWN1cmVcIlxyXG4gICAgICBNQVJJQURCX1JPT1RfUEFTU1dPUkQ6IFwiaW5zZWN1cmVcIlxyXG5cclxudm9sdW1lczpcclxuICBkYi1kYXRhOlxyXG4gIHN0b3JhZ2UtZGF0YTpcclxuICBwaWN0dXJlczoiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYWRtaW5fcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmR9XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInBob3RvcHJpc21cIlxucG9ydCA9IDJfMzQyXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuQkFTRV9VUkwgPSBcImh0dHA6Ly8ke21haW5fZG9tYWlufVwiXG5BRE1JTl9QQVNTV09SRCA9IFwiJHthZG1pbl9wYXNzd29yZH1cIlxuIgp9
```

## Links

`media`,`photos`,`self-hosted`

---

Version:`latest`

pgAdminpgAdmin is the most popular and feature rich Open Source administration and development platform for PostgreSQL, the most advanced Open Source database in the world.

PhpmyadminPhpmyadmin is a free and open-source web interface for MySQL and MariaDB that allows you to manage your databases.

### On this page

ConfigurationBase64LinksTags