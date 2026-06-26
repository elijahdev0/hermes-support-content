---
title: "DataLens | Dokploy"
source: "https://docs.dokploy.com/docs/templates/datalens"
category: dokploy-docs
created: "2026-06-25T17:21:45.078Z"
---

DataLens | Dokploy

# DataLens

Copy as Markdown

A modern, scalable business intelligence and data visualization system.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  pg-compeng:
    image: postgres:16-alpine
    restart: always
    environment:
      POSTGRES_PASSWORD: "postgres"
      POSTGRES_DB: postgres
      POSTGRES_USER: postgres

  control-api:
    image: ghcr.io/datalens-tech/datalens-control-api:0.2192.0
    restart: always
    environment:
      BI_API_UWSGI_WORKERS_COUNT: 4
      CONNECTOR_AVAILABILITY_VISIBLE: "clickhouse,postgres,chyt,ydb,mysql,greenplum,mssql,appmetrica_api,metrika_api"
      RQE_FORCE_OFF: 1
      DL_CRY_ACTUAL_KEY_ID: key_1
      DL_CRY_KEY_VAL_ID_key_1: "h1ZpilcYLYRdWp7Nk8X1M1kBPiUi8rdjz9oBfHyUKIk="
      RQE_SECRET_KEY: ""
      US_HOST: "http://us:8083"
      US_MASTER_TOKEN: "fake-us-master-token"
    depends_on:
      - us

  data-api:
    container_name: datalens-data-api
    image: ghcr.io/datalens-tech/datalens-data-api:0.2192.0
    restart: always
    environment:
      GUNICORN_WORKERS_COUNT: 5
      RQE_FORCE_OFF: 1
      CACHES_ON: 0
      MUTATIONS_CACHES_ON: 0
      RQE_SECRET_KEY: ""
      DL_CRY_ACTUAL_KEY_ID: key_1
      DL_CRY_KEY_VAL_ID_key_1: "h1ZpilcYLYRdWp7Nk8X1M1kBPiUi8rdjz9oBfHyUKIk="
      BI_COMPENG_PG_ON: 1
      BI_COMPENG_PG_URL: "postgresql://postgres:postgres@pg-compeng:5432/postgres"
      US_HOST: "http://us:8083"
      US_MASTER_TOKEN: "fake-us-master-token"
    depends_on:
      - us
      - pg-compeng

  pg-us:
    container_name: datalens-pg-us
    image: postgres:16-alpine
    restart: always
    environment:
      POSTGRES_DB: us-db-ci_purgeable
      POSTGRES_USER: us
      POSTGRES_PASSWORD: us
    volumes:
      - ${VOLUME_US:-./metadata}:/var/lib/postgresql/data

  us:
    image: ghcr.io/datalens-tech/datalens-us:0.310.0
    restart: always
    depends_on:
      - pg-us
    environment:
      APP_INSTALLATION: "opensource"
      APP_ENV: "prod"
      MASTER_TOKEN: "fake-us-master-token"
      POSTGRES_DSN_LIST: ${METADATA_POSTGRES_DSN_LIST:-postgres://us:us@pg-us:5432/us-db-ci_purgeable}
      SKIP_INSTALL_DB_EXTENSIONS: ${METADATA_SKIP_INSTALL_DB_EXTENSIONS:-0}
      USE_DEMO_DATA: ${USE_DEMO_DATA:-0}
      HC: ${HC:-0}
      NODE_EXTRA_CA_CERTS: /certs/root.crt
    extra_hosts:
      - "host.docker.internal:host-gateway"
    volumes:
      - ./certs:/certs

  datalens:
    image: ghcr.io/datalens-tech/datalens-ui:0.2601.0
    restart: always
    ports:
      - ${UI_PORT:-8080}:8080
    depends_on:
      - us
      - control-api
      - data-api
    environment:
      APP_MODE: "full"
      APP_ENV: "production"
      APP_INSTALLATION: "opensource"
      AUTH_POLICY: "disabled"
      US_ENDPOINT: "http://us:8083"
      BI_API_ENDPOINT: "http://control-api:8080"
      BI_DATA_ENDPOINT: "http://data-api:8080"
      US_MASTER_TOKEN: "fake-us-master-token"
      NODE_EXTRA_CA_CERTS: "/usr/local/share/ca-certificates/cert.pem"
      HC: ${HC:-0}
      YANDEX_MAP_ENABLED: ${YANDEX_MAP_ENABLED:-0}
      YANDEX_MAP_TOKEN: ${YANDEX_MAP_TOKEN:-0}
```

```
[variables]
main_domain = "${domain}"

[config]
env = ["HC=1"]
mounts = []

[[config.domains]]
serviceName = "datalens"
port = 8_080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwZy1jb21wZW5nOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNi1hbHBpbmVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiBcInBvc3RncmVzXCJcbiAgICAgIFBPU1RHUkVTX0RCOiBwb3N0Z3Jlc1xuICAgICAgUE9TVEdSRVNfVVNFUjogcG9zdGdyZXNcblxuICBjb250cm9sLWFwaTpcbiAgICBpbWFnZTogZ2hjci5pby9kYXRhbGVucy10ZWNoL2RhdGFsZW5zLWNvbnRyb2wtYXBpOjAuMjE5Mi4wXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBCSV9BUElfVVdTR0lfV09SS0VSU19DT1VOVDogNFxuICAgICAgQ09OTkVDVE9SX0FWQUlMQUJJTElUWV9WSVNJQkxFOiBcImNsaWNraG91c2UscG9zdGdyZXMsY2h5dCx5ZGIsbXlzcWwsZ3JlZW5wbHVtLG1zc3FsLGFwcG1ldHJpY2FfYXBpLG1ldHJpa2FfYXBpXCJcbiAgICAgIFJRRV9GT1JDRV9PRkY6IDFcbiAgICAgIERMX0NSWV9BQ1RVQUxfS0VZX0lEOiBrZXlfMVxuICAgICAgRExfQ1JZX0tFWV9WQUxfSURfa2V5XzE6IFwiaDFacGlsY1lMWVJkV3A3Tms4WDFNMWtCUGlVaThyZGp6OW9CZkh5VUtJaz1cIlxuICAgICAgUlFFX1NFQ1JFVF9LRVk6IFwiXCJcbiAgICAgIFVTX0hPU1Q6IFwiaHR0cDovL3VzOjgwODNcIlxuICAgICAgVVNfTUFTVEVSX1RPS0VOOiBcImZha2UtdXMtbWFzdGVyLXRva2VuXCJcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSB1c1xuXG4gIGRhdGEtYXBpOlxuICAgIGNvbnRhaW5lcl9uYW1lOiBkYXRhbGVucy1kYXRhLWFwaVxuICAgIGltYWdlOiBnaGNyLmlvL2RhdGFsZW5zLXRlY2gvZGF0YWxlbnMtZGF0YS1hcGk6MC4yMTkyLjBcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEdVTklDT1JOX1dPUktFUlNfQ09VTlQ6IDVcbiAgICAgIFJRRV9GT1JDRV9PRkY6IDFcbiAgICAgIENBQ0hFU19PTjogMFxuICAgICAgTVVUQVRJT05TX0NBQ0hFU19PTjogMFxuICAgICAgUlFFX1NFQ1JFVF9LRVk6IFwiXCJcbiAgICAgIERMX0NSWV9BQ1RVQUxfS0VZX0lEOiBrZXlfMVxuICAgICAgRExfQ1JZX0tFWV9WQUxfSURfa2V5XzE6IFwiaDFacGlsY1lMWVJkV3A3Tms4WDFNMWtCUGlVaThyZGp6OW9CZkh5VUtJaz1cIlxuICAgICAgQklfQ09NUEVOR19QR19PTjogMVxuICAgICAgQklfQ09NUEVOR19QR19VUkw6IFwicG9zdGdyZXNxbDovL3Bvc3RncmVzOnBvc3RncmVzQHBnLWNvbXBlbmc6NTQzMi9wb3N0Z3Jlc1wiXG4gICAgICBVU19IT1NUOiBcImh0dHA6Ly91czo4MDgzXCJcbiAgICAgIFVTX01BU1RFUl9UT0tFTjogXCJmYWtlLXVzLW1hc3Rlci10b2tlblwiXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gdXNcbiAgICAgIC0gcGctY29tcGVuZ1xuXG4gIHBnLXVzOlxuICAgIGNvbnRhaW5lcl9uYW1lOiBkYXRhbGVucy1wZy11c1xuICAgIGltYWdlOiBwb3N0Z3JlczoxNi1hbHBpbmVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTX0RCOiB1cy1kYi1jaV9wdXJnZWFibGVcbiAgICAgIFBPU1RHUkVTX1VTRVI6IHVzXG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogdXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSAke1ZPTFVNRV9VUzotLi9tZXRhZGF0YX06L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG5cbiAgdXM6XG4gICAgaW1hZ2U6IGdoY3IuaW8vZGF0YWxlbnMtdGVjaC9kYXRhbGVucy11czowLjMxMC4wXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcGctdXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEFQUF9JTlNUQUxMQVRJT046IFwib3BlbnNvdXJjZVwiXG4gICAgICBBUFBfRU5WOiBcInByb2RcIlxuICAgICAgTUFTVEVSX1RPS0VOOiBcImZha2UtdXMtbWFzdGVyLXRva2VuXCJcbiAgICAgIFBPU1RHUkVTX0RTTl9MSVNUOiAke01FVEFEQVRBX1BPU1RHUkVTX0RTTl9MSVNUOi1wb3N0Z3JlczovL3VzOnVzQHBnLXVzOjU0MzIvdXMtZGItY2lfcHVyZ2VhYmxlfVxuICAgICAgU0tJUF9JTlNUQUxMX0RCX0VYVEVOU0lPTlM6ICR7TUVUQURBVEFfU0tJUF9JTlNUQUxMX0RCX0VYVEVOU0lPTlM6LTB9XG4gICAgICBVU0VfREVNT19EQVRBOiAke1VTRV9ERU1PX0RBVEE6LTB9XG4gICAgICBIQzogJHtIQzotMH1cbiAgICAgIE5PREVfRVhUUkFfQ0FfQ0VSVFM6IC9jZXJ0cy9yb290LmNydFxuICAgIGV4dHJhX2hvc3RzOlxuICAgICAgLSBcImhvc3QuZG9ja2VyLmludGVybmFsOmhvc3QtZ2F0ZXdheVwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi9jZXJ0czovY2VydHNcblxuICBkYXRhbGVuczpcbiAgICBpbWFnZTogZ2hjci5pby9kYXRhbGVucy10ZWNoL2RhdGFsZW5zLXVpOjAuMjYwMS4wXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgcG9ydHM6XG4gICAgICAtICR7VUlfUE9SVDotODA4MH06ODA4MFxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHVzXG4gICAgICAtIGNvbnRyb2wtYXBpXG4gICAgICAtIGRhdGEtYXBpXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBBUFBfTU9ERTogXCJmdWxsXCJcbiAgICAgIEFQUF9FTlY6IFwicHJvZHVjdGlvblwiXG4gICAgICBBUFBfSU5TVEFMTEFUSU9OOiBcIm9wZW5zb3VyY2VcIlxuICAgICAgQVVUSF9QT0xJQ1k6IFwiZGlzYWJsZWRcIlxuICAgICAgVVNfRU5EUE9JTlQ6IFwiaHR0cDovL3VzOjgwODNcIlxuICAgICAgQklfQVBJX0VORFBPSU5UOiBcImh0dHA6Ly9jb250cm9sLWFwaTo4MDgwXCJcbiAgICAgIEJJX0RBVEFfRU5EUE9JTlQ6IFwiaHR0cDovL2RhdGEtYXBpOjgwODBcIlxuICAgICAgVVNfTUFTVEVSX1RPS0VOOiBcImZha2UtdXMtbWFzdGVyLXRva2VuXCJcbiAgICAgIE5PREVfRVhUUkFfQ0FfQ0VSVFM6IFwiL3Vzci9sb2NhbC9zaGFyZS9jYS1jZXJ0aWZpY2F0ZXMvY2VydC5wZW1cIlxuICAgICAgSEM6ICR7SEM6LTB9XG4gICAgICBZQU5ERVhfTUFQX0VOQUJMRUQ6ICR7WUFOREVYX01BUF9FTkFCTEVEOi0wfVxuICAgICAgWUFOREVYX01BUF9UT0tFTjogJHtZQU5ERVhfTUFQX1RPS0VOOi0wfVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcIkhDPTFcIl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImRhdGFsZW5zXCJcbnBvcnQgPSA4XzA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`analytics`,`self-hosted`,`bi`,`monitoring`

---

Version:`1.23.0`

DashyA self-hostable personal dashboard built for you. Includes status-checking, widgets, themes, icon packs, a UI editor and tons more!

Directory ListerDirectory Lister is a simple PHP application that lists the contents of any web-accessible directory and allows navigation there within.

### On this page

ConfigurationBase64LinksTags