---
title: "PeerDB | Dokploy"
source: "https://docs.dokploy.com/docs/templates/peerdb"
category: dokploy-docs
created: "2026-06-25T17:21:55.477Z"
---

PeerDB | Dokploy

# PeerDB

Copy as Markdown

Data integration platform that synchronizes and federates data across databases with a unified API.

## Configuration

docker-compose.ymltemplate.toml

```
name: peerdb-quickstart

x-minio-config: &minio-config
  PEERDB_CLICKHOUSE_AWS_CREDENTIALS_AWS_ACCESS_KEY_ID: ${MINIO_ROOT_USER}
  PEERDB_CLICKHOUSE_AWS_CREDENTIALS_AWS_SECRET_ACCESS_KEY: ${MINIO_ROOT_PASSWORD}
  MINIO_ROOT_USER: ${MINIO_ROOT_USER}
  MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD}
  PEERDB_CLICKHOUSE_AWS_CREDENTIALS_AWS_REGION: ${PEERDB_CLICKHOUSE_AWS_REGION}
  PEERDB_CLICKHOUSE_AWS_CREDENTIALS_AWS_ENDPOINT_URL_S3: ${PEERDB_CLICKHOUSE_AWS_ENDPOINT_URL_S3}
  PEERDB_CLICKHOUSE_AWS_S3_BUCKET_NAME: ${PEERDB_CLICKHOUSE_AWS_S3_BUCKET_NAME}

x-catalog-config: &catalog-config
  PEERDB_CATALOG_HOST: ${PEERDB_CATALOG_HOST}
  PEERDB_CATALOG_PORT: ${PEERDB_CATALOG_PORT}
  PEERDB_CATALOG_USER: ${PEERDB_CATALOG_USER}
  PEERDB_CATALOG_PASSWORD: ${PEERDB_CATALOG_PASSWORD}
  PEERDB_CATALOG_DATABASE: ${PEERDB_CATALOG_DATABASE}

x-flow-worker-env: &flow-worker-env
  TEMPORAL_HOST_PORT: temporal:7233
  TEMPORAL_CLIENT_CERT:
  TEMPORAL_CLIENT_KEY:
  PEERDB_TEMPORAL_NAMESPACE: default
  AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID:-}
  AWS_SECRET_ACCESS_KEY: ${AWS_SECRET_ACCESS_KEY:-}
  AWS_REGION: ${AWS_REGION:-}
  AWS_ENDPOINT: ${AWS_ENDPOINT:-}

services:
  catalog:
    image: postgres:18-alpine@sha256:eca6fb2d91fda290eb8cfb8ba53dd0dcbf3508a08011e30adb039ea7c8e1e9f2
    command: -c config_file=/etc/postgresql.conf
    restart: unless-stopped
    expose:
      - 5432
    environment:
      PGUSER: ${PEERDB_CATALOG_USER}
      POSTGRES_PASSWORD: ${PEERDB_CATALOG_PASSWORD}
      POSTGRES_DB: ${PEERDB_CATALOG_DATABASE}
      POSTGRES_INITDB_ARGS: --locale=C.UTF-8
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ../files/postgresql.conf:/etc/postgresql.conf
      - ../files/docker-entrypoint-initdb.d:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD", "pg_isready", "-d", "${PEERDB_CATALOG_DATABASE}", "-U", "${PEERDB_CATALOG_USER}"]
      interval: 10s
      timeout: 30s
      retries: 5
      start_period: 60s

  temporal:
    restart: unless-stopped
    depends_on:
      catalog:
        condition: service_healthy
    environment:
      DB: postgres12
      DB_PORT: ${PEERDB_CATALOG_PORT}
      POSTGRES_USER: ${PEERDB_CATALOG_USER}
      POSTGRES_PWD: ${PEERDB_CATALOG_PASSWORD}
      POSTGRES_SEEDS: catalog
      DYNAMIC_CONFIG_FILE_PATH: config/dynamicconfig/production-sql.yaml
    image: temporalio/auto-setup:1.29@sha256:5b3502a3b685f9eff1b925af90c57c9e3dbeccbef367cc28a2a9712c63379312
    expose:
      - 7233
    volumes:
      - ../files/temporal-dynamicconfig:/etc/temporal/config/dynamicconfig

  temporal-admin-tools:
    restart: unless-stopped
    depends_on:
      - temporal
    environment:
      TEMPORAL_ADDRESS: temporal:7233
      TEMPORAL_CLI_ADDRESS: temporal:7233
      TEMPORAL_CLI_SHOW_STACKS: 1
    image: temporalio/admin-tools:1.25.2-tctl-1.18.1-cli-1.1.1@sha256:da0c7a7982b571857173ab8f058e7f139b3054800abb4dcb100445d29a563ee8
    stdin_open: true
    tty: true
    entrypoint: ["sh", "/etc/temporal/entrypoint.sh"]
    healthcheck:
      test: ["CMD", "tctl", "workflow", "list"]
      interval: 10s
      timeout: 30s
      retries: 5
    volumes:
      - ../files/scripts/mirror-name-search.sh:/etc/temporal/entrypoint.sh

  temporal-ui:
    restart: unless-stopped
    depends_on:
      - temporal
    environment:
      TEMPORAL_ADDRESS: temporal:7233
      TEMPORAL_CORS_ORIGINS: http://localhost:3000
      TEMPORAL_CSRF_COOKIE_INSECURE: "true"
    image: temporalio/ui:2.43.3@sha256:31f0d8c1ed0bfc49c9c20ea9613ee9dd5c52f5f989bacb8a30210f847028e9cd
    expose:
      - 8080

  flow-api:
    image: ghcr.io/peerdb-io/flow-api:stable-v0.35.5
    restart: unless-stopped
    expose:
      - 8112
      - 8113
    environment:
      <<: [*catalog-config, *flow-worker-env, *minio-config]
      PEERDB_ALLOWED_TARGETS: ${PEERDB_ALLOWED_TARGETS}
    depends_on:
      temporal-admin-tools:
        condition: service_healthy

  flow-snapshot-worker:
    image: ghcr.io/peerdb-io/flow-snapshot-worker:stable-v0.35.5
    restart: unless-stopped
    environment:
      <<: [*catalog-config, *flow-worker-env, *minio-config]
    depends_on:
      temporal-admin-tools:
        condition: service_healthy

  flow-worker:
    image: ghcr.io/peerdb-io/flow-worker:stable-v0.35.5
    restart: unless-stopped
    environment:
      <<: [*catalog-config, *flow-worker-env, *minio-config]
    depends_on:
      temporal-admin-tools:
        condition: service_healthy

  peerdb:
    stop_signal: SIGINT
    image: ghcr.io/peerdb-io/peerdb-server:stable-v0.35.5
    restart: unless-stopped
    environment:
      <<: *catalog-config
      PEERDB_PASSWORD: ${PEERDB_PASSWORD}
      PEERDB_FLOW_SERVER_ADDRESS: ${PEERDB_FLOW_SERVER_ADDRESS}
      RUST_LOG: info
      RUST_BACKTRACE: 1
    expose:
      - 9900
    depends_on:
      catalog:
        condition: service_healthy

  peerdb-ui:
    image: ghcr.io/peerdb-io/peerdb-ui:stable-v0.35.5
    restart: unless-stopped
    expose:
      - 3000
    environment:
      <<: *catalog-config
      DATABASE_URL: ${DATABASE_URL}
      PEERDB_FLOW_SERVER_HTTP: ${PEERDB_FLOW_SERVER_HTTP}
      NEXTAUTH_SECRET: ${NEXTAUTH_SECRET}
      NEXTAUTH_URL: ${NEXTAUTH_URL}
      PEERDB_ALLOWED_TARGETS: ${PEERDB_ALLOWED_TARGETS}
      PEERDB_CLICKHOUSE_ALLOWED_DOMAINS: ${PEERDB_CLICKHOUSE_ALLOWED_DOMAINS}
      PEERDB_EXPERIMENTAL_ENABLE_SCRIPTING: ${PEERDB_EXPERIMENTAL_ENABLE_SCRIPTING}
    depends_on:
      - flow-api

  minio:
    image: minio/minio:latest@sha256:14cea493d9a34af32f524e538b8346cf79f3321eff8e708c1e2960462bd8936e
    restart: unless-stopped
    volumes:
      - minio-data:/data
    expose:
      - 9000
      - 9001
    environment:
      <<: *minio-config
    entrypoint: >
      /bin/sh -c "
      minio server /data --console-address=:9001 &
      sleep 2;
      mc alias set myminiopeerdb http://minio:9000 $$MINIO_ROOT_USER $$MINIO_ROOT_PASSWORD;
      mc mb myminiopeerdb/$$PEERDB_CLICKHOUSE_AWS_S3_BUCKET_NAME;
      wait
      "

volumes:
  pgdata:
  minio-data:
```

```
[variables]
main_domain = "${domain}"
peerdb_password = "${password:32}"
postgres_password = "${password:32}"
minio_root_user = "_peerdb_minioadmin"
minio_root_password = "${password:32}"
nextauth_secret = "${password:32}"

[[config.domains]]
serviceName = "peerdb-ui"
port = 3000
host = "${main_domain}"

[[config.domains]]
serviceName = "minio"
port = 9001
host = "${main_domain}"

[[config.domains]]
serviceName = "temporal-ui"
port = 8080
host = "${main_domain}"

[config.env]
PEERDB_PASSWORD = "${peerdb_password}"
PEERDB_CATALOG_HOST = "catalog"
PEERDB_CATALOG_PORT = "5432"
PEERDB_CATALOG_USER = "postgres"
PEERDB_CATALOG_PASSWORD = "${postgres_password}"
PEERDB_CATALOG_DATABASE = "postgres"
PEERDB_FLOW_SERVER_ADDRESS = "grpc://flow-api:8112"
NEXTAUTH_URL = "http://localhost:3000"
NEXTAUTH_SECRET = "${nextauth_secret}"
DATABASE_URL = "postgres://postgres:${postgres_password}@catalog:5432/postgres"
PEERDB_FLOW_SERVER_HTTP = "http://flow-api:8113"
PEERDB_EXPERIMENTAL_ENABLE_SCRIPTING = "true"
MINIO_ROOT_USER = "${minio_root_user}"
MINIO_ROOT_PASSWORD = "${minio_root_password}"
PEERDB_CLICKHOUSE_AWS_REGION = "us-east-1"
PEERDB_CLICKHOUSE_AWS_ENDPOINT_URL_S3 = "http://minio:9000"
PEERDB_CLICKHOUSE_AWS_S3_BUCKET_NAME = "peerdbbucket"
PEERDB_ALLOWED_TARGETS = ""
PEERDB_CLICKHOUSE_ALLOWED_DOMAINS = ""
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_REGION = ""
AWS_ENDPOINT = ""

[[config.mounts]]
filePath = "./postgresql.conf"
content = """
listen_addresses = '*'

wal_level = logical
max_wal_senders = 4
max_replication_slots = 4
"""

[[config.mounts]]
filePath = "./docker-entrypoint-initdb.d/pg-hba-replication.sh"
content = """
#!/bin/sh
echo "host replication $POSTGRES_USER 0.0.0.0/0 trust" >> "$PGDATA/pg_hba.conf"
"""

[[config.mounts]]
filePath = "./temporal-dynamicconfig/production-sql.yaml"
content = """
limit.maxIDLength:
  - value: 255
    constraints: {}
system.forceSearchAttributesCacheRefreshOnRead:
  - value: false
    constraints: {}
frontend.enableUpdateWorkflowExecution:
  - value: true
"""

[[config.mounts]]
filePath = "./scripts/mirror-name-search.sh"
content = """
#!/bin/sh

sleep 5

# Check if MirrorName attribute exists
if ! temporal operator search-attribute list | grep -w MirrorName >/dev/null 2>&1; then
    # If not, create MirrorName attribute
    temporal operator search-attribute create --name MirrorName --type Text --namespace default
fi

tini -s -- sleep infinity
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIm5hbWU6IHBlZXJkYi1xdWlja3N0YXJ0XG5cbngtbWluaW8tY29uZmlnOiAmbWluaW8tY29uZmlnXG4gIFBFRVJEQl9DTElDS0hPVVNFX0FXU19DUkVERU5USUFMU19BV1NfQUNDRVNTX0tFWV9JRDogJHtNSU5JT19ST09UX1VTRVJ9XG4gIFBFRVJEQl9DTElDS0hPVVNFX0FXU19DUkVERU5USUFMU19BV1NfU0VDUkVUX0FDQ0VTU19LRVk6ICR7TUlOSU9fUk9PVF9QQVNTV09SRH1cbiAgTUlOSU9fUk9PVF9VU0VSOiAke01JTklPX1JPT1RfVVNFUn1cbiAgTUlOSU9fUk9PVF9QQVNTV09SRDogJHtNSU5JT19ST09UX1BBU1NXT1JEfVxuICBQRUVSREJfQ0xJQ0tIT1VTRV9BV1NfQ1JFREVOVElBTFNfQVdTX1JFR0lPTjogJHtQRUVSREJfQ0xJQ0tIT1VTRV9BV1NfUkVHSU9OfVxuICBQRUVSREJfQ0xJQ0tIT1VTRV9BV1NfQ1JFREVOVElBTFNfQVdTX0VORFBPSU5UX1VSTF9TMzogJHtQRUVSREJfQ0xJQ0tIT1VTRV9BV1NfRU5EUE9JTlRfVVJMX1MzfVxuICBQRUVSREJfQ0xJQ0tIT1VTRV9BV1NfUzNfQlVDS0VUX05BTUU6ICR7UEVFUkRCX0NMSUNLSE9VU0VfQVdTX1MzX0JVQ0tFVF9OQU1FfVxuXG54LWNhdGFsb2ctY29uZmlnOiAmY2F0YWxvZy1jb25maWdcbiAgUEVFUkRCX0NBVEFMT0dfSE9TVDogJHtQRUVSREJfQ0FUQUxPR19IT1NUfVxuICBQRUVSREJfQ0FUQUxPR19QT1JUOiAke1BFRVJEQl9DQVRBTE9HX1BPUlR9XG4gIFBFRVJEQl9DQVRBTE9HX1VTRVI6ICR7UEVFUkRCX0NBVEFMT0dfVVNFUn1cbiAgUEVFUkRCX0NBVEFMT0dfUEFTU1dPUkQ6ICR7UEVFUkRCX0NBVEFMT0dfUEFTU1dPUkR9XG4gIFBFRVJEQl9DQVRBTE9HX0RBVEFCQVNFOiAke1BFRVJEQl9DQVRBTE9HX0RBVEFCQVNFfVxuXG54LWZsb3ctd29ya2VyLWVudjogJmZsb3ctd29ya2VyLWVudlxuICBURU1QT1JBTF9IT1NUX1BPUlQ6IHRlbXBvcmFsOjcyMzNcbiAgVEVNUE9SQUxfQ0xJRU5UX0NFUlQ6XG4gIFRFTVBPUkFMX0NMSUVOVF9LRVk6XG4gIFBFRVJEQl9URU1QT1JBTF9OQU1FU1BBQ0U6IGRlZmF1bHRcbiAgQVdTX0FDQ0VTU19LRVlfSUQ6ICR7QVdTX0FDQ0VTU19LRVlfSUQ6LX1cbiAgQVdTX1NFQ1JFVF9BQ0NFU1NfS0VZOiAke0FXU19TRUNSRVRfQUNDRVNTX0tFWTotfVxuICBBV1NfUkVHSU9OOiAke0FXU19SRUdJT046LX1cbiAgQVdTX0VORFBPSU5UOiAke0FXU19FTkRQT0lOVDotfVxuXG5zZXJ2aWNlczpcbiAgY2F0YWxvZzpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTgtYWxwaW5lQHNoYTI1NjplY2E2ZmIyZDkxZmRhMjkwZWI4Y2ZiOGJhNTNkZDBkY2JmMzUwOGEwODAxMWUzMGFkYjAzOWVhN2M4ZTFlOWYyXG4gICAgY29tbWFuZDogLWMgY29uZmlnX2ZpbGU9L2V0Yy9wb3N0Z3Jlc3FsLmNvbmZcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGV4cG9zZTpcbiAgICAgIC0gNTQzMlxuICAgIGVudmlyb25tZW50OlxuICAgICAgUEdVU0VSOiAke1BFRVJEQl9DQVRBTE9HX1VTRVJ9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQRUVSREJfQ0FUQUxPR19QQVNTV09SRH1cbiAgICAgIFBPU1RHUkVTX0RCOiAke1BFRVJEQl9DQVRBTE9HX0RBVEFCQVNFfVxuICAgICAgUE9TVEdSRVNfSU5JVERCX0FSR1M6IC0tbG9jYWxlPUMuVVRGLThcbiAgICB2b2x1bWVzOlxuICAgICAgLSBwZ2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgICAtIC4uL2ZpbGVzL3Bvc3RncmVzcWwuY29uZjovZXRjL3Bvc3RncmVzcWwuY29uZlxuICAgICAgLSAuLi9maWxlcy9kb2NrZXItZW50cnlwb2ludC1pbml0ZGIuZDovZG9ja2VyLWVudHJ5cG9pbnQtaW5pdGRiLmRcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcInBnX2lzcmVhZHlcIiwgXCItZFwiLCBcIiR7UEVFUkRCX0NBVEFMT0dfREFUQUJBU0V9XCIsIFwiLVVcIiwgXCIke1BFRVJEQl9DQVRBTE9HX1VTRVJ9XCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiAzMHNcbiAgICAgIHJldHJpZXM6IDVcbiAgICAgIHN0YXJ0X3BlcmlvZDogNjBzXG5cbiAgdGVtcG9yYWw6XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgY2F0YWxvZzpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERCOiBwb3N0Z3JlczEyXG4gICAgICBEQl9QT1JUOiAke1BFRVJEQl9DQVRBTE9HX1BPUlR9XG4gICAgICBQT1NUR1JFU19VU0VSOiAke1BFRVJEQl9DQVRBTE9HX1VTRVJ9XG4gICAgICBQT1NUR1JFU19QV0Q6ICR7UEVFUkRCX0NBVEFMT0dfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19TRUVEUzogY2F0YWxvZ1xuICAgICAgRFlOQU1JQ19DT05GSUdfRklMRV9QQVRIOiBjb25maWcvZHluYW1pY2NvbmZpZy9wcm9kdWN0aW9uLXNxbC55YW1sXG4gICAgaW1hZ2U6IHRlbXBvcmFsaW8vYXV0by1zZXR1cDoxLjI5QHNoYTI1Njo1YjM1MDJhM2I2ODVmOWVmZjFiOTI1YWY5MGM1N2M5ZTNkYmVjY2JlZjM2N2NjMjhhMmE5NzEyYzYzMzc5MzEyXG4gICAgZXhwb3NlOlxuICAgICAgLSA3MjMzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvdGVtcG9yYWwtZHluYW1pY2NvbmZpZzovZXRjL3RlbXBvcmFsL2NvbmZpZy9keW5hbWljY29uZmlnXG5cbiAgdGVtcG9yYWwtYWRtaW4tdG9vbHM6XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSB0ZW1wb3JhbFxuICAgIGVudmlyb25tZW50OlxuICAgICAgVEVNUE9SQUxfQUREUkVTUzogdGVtcG9yYWw6NzIzM1xuICAgICAgVEVNUE9SQUxfQ0xJX0FERFJFU1M6IHRlbXBvcmFsOjcyMzNcbiAgICAgIFRFTVBPUkFMX0NMSV9TSE9XX1NUQUNLUzogMVxuICAgIGltYWdlOiB0ZW1wb3JhbGlvL2FkbWluLXRvb2xzOjEuMjUuMi10Y3RsLTEuMTguMS1jbGktMS4xLjFAc2hhMjU2OmRhMGM3YTc5ODJiNTcxODU3MTczYWI4ZjA1OGU3ZjEzOWIzMDU0ODAwYWJiNGRjYjEwMDQ0NWQyOWE1NjNlZThcbiAgICBzdGRpbl9vcGVuOiB0cnVlXG4gICAgdHR5OiB0cnVlXG4gICAgZW50cnlwb2ludDogW1wic2hcIiwgXCIvZXRjL3RlbXBvcmFsL2VudHJ5cG9pbnQuc2hcIl1cbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcInRjdGxcIiwgXCJ3b3JrZmxvd1wiLCBcImxpc3RcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDMwc1xuICAgICAgcmV0cmllczogNVxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL3NjcmlwdHMvbWlycm9yLW5hbWUtc2VhcmNoLnNoOi9ldGMvdGVtcG9yYWwvZW50cnlwb2ludC5zaFxuXG4gIHRlbXBvcmFsLXVpOlxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gdGVtcG9yYWxcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFRFTVBPUkFMX0FERFJFU1M6IHRlbXBvcmFsOjcyMzNcbiAgICAgIFRFTVBPUkFMX0NPUlNfT1JJR0lOUzogaHR0cDovL2xvY2FsaG9zdDozMDAwXG4gICAgICBURU1QT1JBTF9DU1JGX0NPT0tJRV9JTlNFQ1VSRTogXCJ0cnVlXCJcbiAgICBpbWFnZTogdGVtcG9yYWxpby91aToyLjQzLjNAc2hhMjU2OjMxZjBkOGMxZWQwYmZjNDljOWMyMGVhOTYxM2VlOWRkNWM1MmY1Zjk4OWJhY2I4YTMwMjEwZjg0NzAyOGU5Y2RcbiAgICBleHBvc2U6XG4gICAgICAtIDgwODBcblxuICBmbG93LWFwaTpcbiAgICBpbWFnZTogZ2hjci5pby9wZWVyZGItaW8vZmxvdy1hcGk6c3RhYmxlLXYwLjM1LjVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGV4cG9zZTpcbiAgICAgIC0gODExMlxuICAgICAgLSA4MTEzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICA8PDogWypjYXRhbG9nLWNvbmZpZywgKmZsb3ctd29ya2VyLWVudiwgKm1pbmlvLWNvbmZpZ11cbiAgICAgIFBFRVJEQl9BTExPV0VEX1RBUkdFVFM6ICR7UEVFUkRCX0FMTE9XRURfVEFSR0VUU31cbiAgICBkZXBlbmRzX29uOlxuICAgICAgdGVtcG9yYWwtYWRtaW4tdG9vbHM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG5cbiAgZmxvdy1zbmFwc2hvdC13b3JrZXI6XG4gICAgaW1hZ2U6IGdoY3IuaW8vcGVlcmRiLWlvL2Zsb3ctc25hcHNob3Qtd29ya2VyOnN0YWJsZS12MC4zNS41XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIDw8OiBbKmNhdGFsb2ctY29uZmlnLCAqZmxvdy13b3JrZXItZW52LCAqbWluaW8tY29uZmlnXVxuICAgIGRlcGVuZHNfb246XG4gICAgICB0ZW1wb3JhbC1hZG1pbi10b29sczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcblxuICBmbG93LXdvcmtlcjpcbiAgICBpbWFnZTogZ2hjci5pby9wZWVyZGItaW8vZmxvdy13b3JrZXI6c3RhYmxlLXYwLjM1LjVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgPDw6IFsqY2F0YWxvZy1jb25maWcsICpmbG93LXdvcmtlci1lbnYsICptaW5pby1jb25maWddXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHRlbXBvcmFsLWFkbWluLXRvb2xzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuXG4gIHBlZXJkYjpcbiAgICBzdG9wX3NpZ25hbDogU0lHSU5UXG4gICAgaW1hZ2U6IGdoY3IuaW8vcGVlcmRiLWlvL3BlZXJkYi1zZXJ2ZXI6c3RhYmxlLXYwLjM1LjVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgPDw6ICpjYXRhbG9nLWNvbmZpZ1xuICAgICAgUEVFUkRCX1BBU1NXT1JEOiAke1BFRVJEQl9QQVNTV09SRH1cbiAgICAgIFBFRVJEQl9GTE9XX1NFUlZFUl9BRERSRVNTOiAke1BFRVJEQl9GTE9XX1NFUlZFUl9BRERSRVNTfVxuICAgICAgUlVTVF9MT0c6IGluZm9cbiAgICAgIFJVU1RfQkFDS1RSQUNFOiAxXG4gICAgZXhwb3NlOlxuICAgICAgLSA5OTAwXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGNhdGFsb2c6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG5cbiAgcGVlcmRiLXVpOlxuICAgIGltYWdlOiBnaGNyLmlvL3BlZXJkYi1pby9wZWVyZGItdWk6c3RhYmxlLXYwLjM1LjVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGV4cG9zZTpcbiAgICAgIC0gMzAwMFxuICAgIGVudmlyb25tZW50OlxuICAgICAgPDw6ICpjYXRhbG9nLWNvbmZpZ1xuICAgICAgREFUQUJBU0VfVVJMOiAke0RBVEFCQVNFX1VSTH1cbiAgICAgIFBFRVJEQl9GTE9XX1NFUlZFUl9IVFRQOiAke1BFRVJEQl9GTE9XX1NFUlZFUl9IVFRQfVxuICAgICAgTkVYVEFVVEhfU0VDUkVUOiAke05FWFRBVVRIX1NFQ1JFVH1cbiAgICAgIE5FWFRBVVRIX1VSTDogJHtORVhUQVVUSF9VUkx9XG4gICAgICBQRUVSREJfQUxMT1dFRF9UQVJHRVRTOiAke1BFRVJEQl9BTExPV0VEX1RBUkdFVFN9XG4gICAgICBQRUVSREJfQ0xJQ0tIT1VTRV9BTExPV0VEX0RPTUFJTlM6ICR7UEVFUkRCX0NMSUNLSE9VU0VfQUxMT1dFRF9ET01BSU5TfVxuICAgICAgUEVFUkRCX0VYUEVSSU1FTlRBTF9FTkFCTEVfU0NSSVBUSU5HOiAke1BFRVJEQl9FWFBFUklNRU5UQUxfRU5BQkxFX1NDUklQVElOR31cbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBmbG93LWFwaVxuXG4gIG1pbmlvOlxuICAgIGltYWdlOiBtaW5pby9taW5pbzpsYXRlc3RAc2hhMjU2OjE0Y2VhNDkzZDlhMzRhZjMyZjUyNGU1MzhiODM0NmNmNzlmMzMyMWVmZjhlNzA4YzFlMjk2MDQ2MmJkODkzNmVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIG1pbmlvLWRhdGE6L2RhdGFcbiAgICBleHBvc2U6XG4gICAgICAtIDkwMDBcbiAgICAgIC0gOTAwMVxuICAgIGVudmlyb25tZW50OlxuICAgICAgPDw6ICptaW5pby1jb25maWdcbiAgICBlbnRyeXBvaW50OiA+XG4gICAgICAvYmluL3NoIC1jIFwiXG4gICAgICBtaW5pbyBzZXJ2ZXIgL2RhdGEgLS1jb25zb2xlLWFkZHJlc3M9OjkwMDEgJlxuICAgICAgc2xlZXAgMjtcbiAgICAgIG1jIGFsaWFzIHNldCBteW1pbmlvcGVlcmRiIGh0dHA6Ly9taW5pbzo5MDAwICQkTUlOSU9fUk9PVF9VU0VSICQkTUlOSU9fUk9PVF9QQVNTV09SRDtcbiAgICAgIG1jIG1iIG15bWluaW9wZWVyZGIvJCRQRUVSREJfQ0xJQ0tIT1VTRV9BV1NfUzNfQlVDS0VUX05BTUU7XG4gICAgICB3YWl0XG4gICAgICBcIlxuXG52b2x1bWVzOlxuICBwZ2RhdGE6XG4gIG1pbmlvLWRhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucGVlcmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxubWluaW9fcm9vdF91c2VyID0gXCJfcGVlcmRiX21pbmlvYWRtaW5cIlxubWluaW9fcm9vdF9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxubmV4dGF1dGhfc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInBlZXJkYi11aVwiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJtaW5pb1wiXG5wb3J0ID0gOTAwMVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ0ZW1wb3JhbC11aVwiXG5wb3J0ID0gODA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblBFRVJEQl9QQVNTV09SRCA9IFwiJHtwZWVyZGJfcGFzc3dvcmR9XCJcblBFRVJEQl9DQVRBTE9HX0hPU1QgPSBcImNhdGFsb2dcIlxuUEVFUkRCX0NBVEFMT0dfUE9SVCA9IFwiNTQzMlwiXG5QRUVSREJfQ0FUQUxPR19VU0VSID0gXCJwb3N0Z3Jlc1wiXG5QRUVSREJfQ0FUQUxPR19QQVNTV09SRCA9IFwiJHtwb3N0Z3Jlc19wYXNzd29yZH1cIlxuUEVFUkRCX0NBVEFMT0dfREFUQUJBU0UgPSBcInBvc3RncmVzXCJcblBFRVJEQl9GTE9XX1NFUlZFUl9BRERSRVNTID0gXCJncnBjOi8vZmxvdy1hcGk6ODExMlwiXG5ORVhUQVVUSF9VUkwgPSBcImh0dHA6Ly9sb2NhbGhvc3Q6MzAwMFwiXG5ORVhUQVVUSF9TRUNSRVQgPSBcIiR7bmV4dGF1dGhfc2VjcmV0fVwiXG5EQVRBQkFTRV9VUkwgPSBcInBvc3RncmVzOi8vcG9zdGdyZXM6JHtwb3N0Z3Jlc19wYXNzd29yZH1AY2F0YWxvZzo1NDMyL3Bvc3RncmVzXCJcblBFRVJEQl9GTE9XX1NFUlZFUl9IVFRQID0gXCJodHRwOi8vZmxvdy1hcGk6ODExM1wiXG5QRUVSREJfRVhQRVJJTUVOVEFMX0VOQUJMRV9TQ1JJUFRJTkcgPSBcInRydWVcIlxuTUlOSU9fUk9PVF9VU0VSID0gXCIke21pbmlvX3Jvb3RfdXNlcn1cIlxuTUlOSU9fUk9PVF9QQVNTV09SRCA9IFwiJHttaW5pb19yb290X3Bhc3N3b3JkfVwiXG5QRUVSREJfQ0xJQ0tIT1VTRV9BV1NfUkVHSU9OID0gXCJ1cy1lYXN0LTFcIlxuUEVFUkRCX0NMSUNLSE9VU0VfQVdTX0VORFBPSU5UX1VSTF9TMyA9IFwiaHR0cDovL21pbmlvOjkwMDBcIlxuUEVFUkRCX0NMSUNLSE9VU0VfQVdTX1MzX0JVQ0tFVF9OQU1FID0gXCJwZWVyZGJidWNrZXRcIlxuUEVFUkRCX0FMTE9XRURfVEFSR0VUUyA9IFwiXCJcblBFRVJEQl9DTElDS0hPVVNFX0FMTE9XRURfRE9NQUlOUyA9IFwiXCJcbkFXU19BQ0NFU1NfS0VZX0lEID0gXCJcIlxuQVdTX1NFQ1JFVF9BQ0NFU1NfS0VZID0gXCJcIlxuQVdTX1JFR0lPTiA9IFwiXCJcbkFXU19FTkRQT0lOVCA9IFwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIuL3Bvc3RncmVzcWwuY29uZlwiXG5jb250ZW50ID0gXCJcIlwiXG5saXN0ZW5fYWRkcmVzc2VzID0gJyonXG5cbndhbF9sZXZlbCA9IGxvZ2ljYWxcbm1heF93YWxfc2VuZGVycyA9IDRcbm1heF9yZXBsaWNhdGlvbl9zbG90cyA9IDRcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi4vZG9ja2VyLWVudHJ5cG9pbnQtaW5pdGRiLmQvcGctaGJhLXJlcGxpY2F0aW9uLnNoXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMhL2Jpbi9zaFxuZWNobyBcImhvc3QgcmVwbGljYXRpb24gJFBPU1RHUkVTX1VTRVIgMC4wLjAuMC8wIHRydXN0XCIgPj4gXCIkUEdEQVRBL3BnX2hiYS5jb25mXCJcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi4vdGVtcG9yYWwtZHluYW1pY2NvbmZpZy9wcm9kdWN0aW9uLXNxbC55YW1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbmxpbWl0Lm1heElETGVuZ3RoOlxuICAtIHZhbHVlOiAyNTVcbiAgICBjb25zdHJhaW50czoge31cbnN5c3RlbS5mb3JjZVNlYXJjaEF0dHJpYnV0ZXNDYWNoZVJlZnJlc2hPblJlYWQ6XG4gIC0gdmFsdWU6IGZhbHNlXG4gICAgY29uc3RyYWludHM6IHt9XG5mcm9udGVuZC5lbmFibGVVcGRhdGVXb3JrZmxvd0V4ZWN1dGlvbjpcbiAgLSB2YWx1ZTogdHJ1ZVxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiLi9zY3JpcHRzL21pcnJvci1uYW1lLXNlYXJjaC5zaFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIS9iaW4vc2hcblxuc2xlZXAgNVxuXG4jIENoZWNrIGlmIE1pcnJvck5hbWUgYXR0cmlidXRlIGV4aXN0c1xuaWYgISB0ZW1wb3JhbCBvcGVyYXRvciBzZWFyY2gtYXR0cmlidXRlIGxpc3QgfCBncmVwIC13IE1pcnJvck5hbWUgPi9kZXYvbnVsbCAyPiYxOyB0aGVuXG4gICAgIyBJZiBub3QsIGNyZWF0ZSBNaXJyb3JOYW1lIGF0dHJpYnV0ZVxuICAgIHRlbXBvcmFsIG9wZXJhdG9yIHNlYXJjaC1hdHRyaWJ1dGUgY3JlYXRlIC0tbmFtZSBNaXJyb3JOYW1lIC0tdHlwZSBUZXh0IC0tbmFtZXNwYWNlIGRlZmF1bHRcbmZpXG5cbnRpbmkgLXMgLS0gc2xlZXAgaW5maW5pdHlcblwiXCJcIlxuIgp9
```

## Links

`database`,`integration`,`sync`,`sql`,`workflow`

---

Version:`v0.35.5`

PaymenterPaymenter is a modern billing and payment management system for hosting providers, with automation, invoicing, and client management features.

PenpotPenpot is the web-based open-source design tool that bridges the gap between designers and developers.

### On this page

ConfigurationBase64LinksTags