---
title: "Twenty CRM | Dokploy"
source: "https://docs.dokploy.com/docs/templates/twenty"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

Twenty CRM | Dokploy

# Twenty CRM

Copy as Markdown

Twenty is a modern CRM offering a powerful spreadsheet interface and open-source alternative to Salesforce.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  twenty-change-vol-ownership:
    image: ubuntu
    user: root

    volumes:
      - twenty-server-local-data:/tmp/server-local-data
      - twenty-docker-data:/tmp/docker-data
    command: >
      bash -c "
      chown -R 1000:1000 /tmp/server-local-data
      && chown -R 1000:1000 /tmp/docker-data"

  twenty-server:
    image: twentycrm/twenty:latest

    volumes:
      - twenty-server-local-data:/app/packages/twenty-server/${STORAGE_LOCAL_PATH:-.local-storage}
      - twenty-docker-data:/app/docker-data
    environment:
      PORT: 3000
      SERVER_URL: ${HTTP_PROTOCOL}://${TWENTY_HOST}
      FRONT_BASE_URL: ${HTTP_PROTOCOL}://${TWENTY_HOST}

      PG_DATABASE_URL: postgres://${DB_USER}:${DB_PASSWORD}@twenty-postgres:5432/twenty
      ENABLE_DB_MIGRATIONS: "true"

      REDIS_URL: redis://twenty-redis:6379
      IS_SIGN_UP_DISABLED: ${IS_SIGN_UP_DISABLED:-false}
      SIGN_IN_PREFILLED: "false"

      IS_CONFIG_VARIABLES_IN_DB_ENABLED: "true"
      STORAGE_TYPE: local

      APP_SECRET: ${APP_SECRET}
    depends_on:
      twenty-change-vol-ownership:
        condition: service_completed_successfully
      twenty-postgres:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://127.0.0.1:3000/healthz"]
      interval: 5s
      timeout: 5s
      retries: 30
      start_period: 30s
    restart: always

  twenty-worker:
    image: twentycrm/twenty:latest

    command: ["yarn", "worker:prod"]
    environment:
      PG_DATABASE_URL: postgres://${DB_USER}:${DB_PASSWORD}@twenty-postgres:5432/twenty
      SERVER_URL: ${HTTP_PROTOCOL}://${TWENTY_HOST}
      FRONT_BASE_URL: ${HTTP_PROTOCOL}://${TWENTY_HOST}
      REDIS_URL: redis://twenty-redis:6379
      ENABLE_DB_MIGRATIONS: "false"
      STORAGE_TYPE: local
      APP_SECRET: ${APP_SECRET}
    depends_on:
      twenty-postgres:
        condition: service_healthy
      twenty-server:
        condition: service_healthy
    restart: always

  twenty-postgres:
    image: postgres:17-alpine

    volumes:
      - twenty-postgres-data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: twenty
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d twenty"]
      interval: 5s
      timeout: 5s
      retries: 10
    restart: always

  twenty-redis:
    image: redis:latest

    volumes:
      - twenty-redis-data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 10
    restart: always

volumes:
  twenty-docker-data:
  twenty-postgres-data:
  twenty-server-local-data:
  twenty-redis-data:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password}"
db_user = "twenty"
app_secret = "${base64:32}"

[config]
mounts = []

[[config.domains]]
serviceName = "twenty-server"
port = 3_000
host = "${main_domain}"

[config.env]
HTTP_PROTOCOL = "http"
TWENTY_HOST = "${main_domain}"
DB_USER = "${db_user}"
DB_PASSWORD = "${db_password}"
APP_SECRET = "${app_secret}"
IS_SIGN_UP_DISABLED = "false"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB0d2VudHktY2hhbmdlLXZvbC1vd25lcnNoaXA6XG4gICAgaW1hZ2U6IHVidW50dVxuICAgIHVzZXI6IHJvb3RcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIHR3ZW50eS1zZXJ2ZXItbG9jYWwtZGF0YTovdG1wL3NlcnZlci1sb2NhbC1kYXRhXG4gICAgICAtIHR3ZW50eS1kb2NrZXItZGF0YTovdG1wL2RvY2tlci1kYXRhXG4gICAgY29tbWFuZDogPlxuICAgICAgYmFzaCAtYyBcIlxuICAgICAgY2hvd24gLVIgMTAwMDoxMDAwIC90bXAvc2VydmVyLWxvY2FsLWRhdGFcbiAgICAgICYmIGNob3duIC1SIDEwMDA6MTAwMCAvdG1wL2RvY2tlci1kYXRhXCJcblxuICB0d2VudHktc2VydmVyOlxuICAgIGltYWdlOiB0d2VudHljcm0vdHdlbnR5OmxhdGVzdFxuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gdHdlbnR5LXNlcnZlci1sb2NhbC1kYXRhOi9hcHAvcGFja2FnZXMvdHdlbnR5LXNlcnZlci8ke1NUT1JBR0VfTE9DQUxfUEFUSDotLmxvY2FsLXN0b3JhZ2V9XG4gICAgICAtIHR3ZW50eS1kb2NrZXItZGF0YTovYXBwL2RvY2tlci1kYXRhXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1JUOiAzMDAwXG4gICAgICBTRVJWRVJfVVJMOiAke0hUVFBfUFJPVE9DT0x9Oi8vJHtUV0VOVFlfSE9TVH1cbiAgICAgIEZST05UX0JBU0VfVVJMOiAke0hUVFBfUFJPVE9DT0x9Oi8vJHtUV0VOVFlfSE9TVH1cblxuICAgICAgUEdfREFUQUJBU0VfVVJMOiBwb3N0Z3JlczovLyR7REJfVVNFUn06JHtEQl9QQVNTV09SRH1AdHdlbnR5LXBvc3RncmVzOjU0MzIvdHdlbnR5XG4gICAgICBFTkFCTEVfREJfTUlHUkFUSU9OUzogXCJ0cnVlXCJcblxuICAgICAgUkVESVNfVVJMOiByZWRpczovL3R3ZW50eS1yZWRpczo2Mzc5XG4gICAgICBJU19TSUdOX1VQX0RJU0FCTEVEOiAke0lTX1NJR05fVVBfRElTQUJMRUQ6LWZhbHNlfVxuICAgICAgU0lHTl9JTl9QUkVGSUxMRUQ6IFwiZmFsc2VcIlxuXG4gICAgICBJU19DT05GSUdfVkFSSUFCTEVTX0lOX0RCX0VOQUJMRUQ6IFwidHJ1ZVwiXG4gICAgICBTVE9SQUdFX1RZUEU6IGxvY2FsXG5cbiAgICAgIEFQUF9TRUNSRVQ6ICR7QVBQX1NFQ1JFVH1cbiAgICBkZXBlbmRzX29uOlxuICAgICAgdHdlbnR5LWNoYW5nZS12b2wtb3duZXJzaGlwOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfY29tcGxldGVkX3N1Y2Nlc3NmdWxseVxuICAgICAgdHdlbnR5LXBvc3RncmVzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwiY3VybFwiLCBcIi1mXCIsIFwiaHR0cDovLzEyNy4wLjAuMTozMDAwL2hlYWx0aHpcIl1cbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDMwXG4gICAgICBzdGFydF9wZXJpb2Q6IDMwc1xuICAgIHJlc3RhcnQ6IGFsd2F5c1xuXG4gIHR3ZW50eS13b3JrZXI6XG4gICAgaW1hZ2U6IHR3ZW50eWNybS90d2VudHk6bGF0ZXN0XG5cbiAgICBjb21tYW5kOiBbXCJ5YXJuXCIsIFwid29ya2VyOnByb2RcIl1cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBHX0RBVEFCQVNFX1VSTDogcG9zdGdyZXM6Ly8ke0RCX1VTRVJ9OiR7REJfUEFTU1dPUkR9QHR3ZW50eS1wb3N0Z3Jlczo1NDMyL3R3ZW50eVxuICAgICAgU0VSVkVSX1VSTDogJHtIVFRQX1BST1RPQ09MfTovLyR7VFdFTlRZX0hPU1R9XG4gICAgICBGUk9OVF9CQVNFX1VSTDogJHtIVFRQX1BST1RPQ09MfTovLyR7VFdFTlRZX0hPU1R9XG4gICAgICBSRURJU19VUkw6IHJlZGlzOi8vdHdlbnR5LXJlZGlzOjYzNzlcbiAgICAgIEVOQUJMRV9EQl9NSUdSQVRJT05TOiBcImZhbHNlXCJcbiAgICAgIFNUT1JBR0VfVFlQRTogbG9jYWxcbiAgICAgIEFQUF9TRUNSRVQ6ICR7QVBQX1NFQ1JFVH1cbiAgICBkZXBlbmRzX29uOlxuICAgICAgdHdlbnR5LXBvc3RncmVzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgdHdlbnR5LXNlcnZlcjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICByZXN0YXJ0OiBhbHdheXNcblxuICB0d2VudHktcG9zdGdyZXM6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE3LWFscGluZVxuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gdHdlbnR5LXBvc3RncmVzLWRhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19VU0VSOiAke0RCX1VTRVJ9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtEQl9QQVNTV09SRH1cbiAgICAgIFBPU1RHUkVTX0RCOiB0d2VudHlcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgJHtEQl9VU0VSfSAtZCB0d2VudHlcIl1cbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDEwXG4gICAgcmVzdGFydDogYWx3YXlzXG5cbiAgdHdlbnR5LXJlZGlzOlxuICAgIGltYWdlOiByZWRpczpsYXRlc3RcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIHR3ZW50eS1yZWRpcy1kYXRhOi9kYXRhXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJyZWRpcy1jbGlcIiwgXCJwaW5nXCJdXG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiAxMFxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuXG52b2x1bWVzOlxuICB0d2VudHktZG9ja2VyLWRhdGE6XG4gIHR3ZW50eS1wb3N0Z3Jlcy1kYXRhOlxuICB0d2VudHktc2VydmVyLWxvY2FsLWRhdGE6XG4gIHR3ZW50eS1yZWRpcy1kYXRhOiAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmR9XCJcbmRiX3VzZXIgPSBcInR3ZW50eVwiXG5hcHBfc2VjcmV0ID0gXCIke2Jhc2U2NDozMn1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwidHdlbnR5LXNlcnZlclwiXG5wb3J0ID0gM18wMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5IVFRQX1BST1RPQ09MID0gXCJodHRwXCJcblRXRU5UWV9IT1NUID0gXCIke21haW5fZG9tYWlufVwiXG5EQl9VU0VSID0gXCIke2RiX3VzZXJ9XCJcbkRCX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiXG5BUFBfU0VDUkVUID0gXCIke2FwcF9zZWNyZXR9XCJcbklTX1NJR05fVVBfRElTQUJMRUQgPSBcImZhbHNlXCJcbiIKfQ==
```

## Links

`crm`,`sales`,`business`

---

Version:`latest`

TuwunelHigh performance Matrix homeserver written in Rust. Official successor to conduwuit - a scalable, low-cost, enterprise-ready alternative to Synapse.

TypebotTypebot is an open-source chatbot builder platform.

### On this page

ConfigurationBase64LinksTags