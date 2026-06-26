---
title: "Plane | Dokploy"
source: "https://docs.dokploy.com/docs/templates/plane"
category: dokploy-docs
created: "2026-06-25T17:21:56.647Z"
---

Plane | Dokploy

# Plane

Copy as Markdown

Easy, flexible, open source project management software

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  web:
    image: makeplane/plane-frontend:${APP_RELEASE:-v0.27.1}
    command: node web/server.js web
    depends_on:
      - api
      - worker
    env_file:
      - .env

  space:
    image: makeplane/plane-space:${APP_RELEASE:-v0.27.1}
    command: node space/server.js space
    depends_on:
      - api
      - worker
      - web
    env_file:
      - .env

  admin:
    image: makeplane/plane-admin:${APP_RELEASE:-v0.27.1}
    command: node admin/server.js admin
    depends_on:
      - api
      - web
    env_file:
      - .env

  live:
    image: makeplane/plane-live:${APP_RELEASE:-v0.27.1}
    command: node live/dist/server.js live
    depends_on:
      - api
      - web
    env_file:
      - .env

  api:
    image: makeplane/plane-backend:${APP_RELEASE:-v0.27.1}
    command: ./bin/docker-entrypoint-api.sh
    volumes:
      - logs_api:/code/plane/logs
    depends_on:
      - plane-db
      - plane-redis
      - plane-mq
    env_file:
      - .env

  worker:
    image: makeplane/plane-backend:${APP_RELEASE:-v0.27.1}
    command: ./bin/docker-entrypoint-worker.sh
    volumes:
      - logs_worker:/code/plane/logs
    depends_on:
      - api
      - plane-db
      - plane-redis
      - plane-mq
    env_file:
      - .env

  beat-worker:
    image: makeplane/plane-backend:${APP_RELEASE:-v0.27.1}
    command: ./bin/docker-entrypoint-beat.sh
    volumes:
      - logs_beat-worker:/code/plane/logs
    depends_on:
      - api
      - plane-db
      - plane-redis
      - plane-mq
    env_file:
      - .env

  migrator:
    image: makeplane/plane-backend:${APP_RELEASE:-v0.27.1}
    command: ./bin/docker-entrypoint-migrator.sh
    volumes:
      - logs_migrator:/code/plane/logs
    depends_on:
      - plane-db
      - plane-redis
    env_file:
      - .env

  plane-db:
    image: postgres:17-alpine
    command: postgres -c 'max_connections=1000'
    volumes:
      - pgdata:/var/lib/postgresql/data
    env_file:
      - .env

  plane-redis:
    image: valkey/valkey:7.2.5-alpine
    volumes:
      - redisdata:/data
    env_file:
      - .env

  plane-mq:
    image: rabbitmq:3.13.6-management-alpine
    volumes:
      - rabbitmq_data:/var/lib/rabbitmq
    env_file:
      - .env

  plane-minio:
    image: minio/minio:latest
    command: server /export --console-address ":9090"
    volumes:
      - uploads:/export
    env_file:
      - .env

  proxy:
    image: makeplane/plane-proxy:${APP_RELEASE:-v0.27.1}
    depends_on:
      - web
      - api
      - space
    env_file:
      - .env

volumes:
  pgdata:
  redisdata:
  uploads:
  logs_api:
  logs_worker:
  logs_beat-worker:
  logs_migrator:
  rabbitmq_data:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:32}"
minio_password = "${password:32}"
rabbitmq_user = "${username}"
rabbitmq_pass = "${password:32}"
secret_key = "${base64:48}"

[config]
env = [
"Domain=${domain}",
"WEB_URL=${Domain}",
"PGHOST=plane-db",
"PGDATABASE=plane",
"POSTGRES_USER=${username}",
"POSTGRES_PASSWORD=${db_password}",
"POSTGRES_DB=plane",
"POSTGRES_PORT=5432",
"PGDATA=/var/lib/postgresql/data",
"REDIS_HOST=plane-redis",
"REDIS_PORT=6379",
"REDIS_URL=redis://plane-redis:6379/",
"MINIO_ROOT_USER=access-key",
"MINIO_ROOT_PASSWORD=${minio_password}",
"AWS_REGION=",
"AWS_ACCESS_KEY_ID=${MINIO_ROOT_USER}",
"AWS_SECRET_ACCESS_KEY=${minio_password}",
"AWS_S3_ENDPOINT_URL=http://plane-minio:9000",
"AWS_S3_BUCKET_NAME=uploads",
"NGINX_PORT=80",
"BUCKET_NAME=uploads",
"FILE_SIZE_LIMIT=5242880",
"RABBITMQ_HOST=plane-mq",
"RABBITMQ_PORT=5672",
"RABBITMQ_DEFAULT_USER=rabbitmq_user",
"RABBITMQ_DEFAULT_PASS=${rabbitmq_pass}",
"RABBITMQ_DEFAULT_VHOST=plane",
"RABBITMQ_VHOST=plane",
"API_BASE_URL=http://api:8000",
"DEBUG=0",
"SENTRY_DSN=",
"SENTRY_ENVIRONMENT=production",
"CORS_ALLOWED_ORIGINS=https://${Domain}",
"GUNICORN_WORKERS=1",
"USE_MINIO=1",
"DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@plane-db/plane",
"SECRET_KEY=${secret_key}",
"AMQP_URL=amqp://${RABBITMQ_DEFAULT_USER}:${RABBITMQ_DEFAULT_PASS}@plane-mq:5672/plane",
"API_KEY_RATE_LIMIT=60/minute",
"MINIO_ENDPOINT_SSL=0"
]
mounts = []

[[config.domains]]
serviceName = "proxy"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHdlYjpcbiAgICBpbWFnZTogbWFrZXBsYW5lL3BsYW5lLWZyb250ZW5kOiR7QVBQX1JFTEVBU0U6LXYwLjI3LjF9XG4gICAgY29tbWFuZDogbm9kZSB3ZWIvc2VydmVyLmpzIHdlYlxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGFwaVxuICAgICAgLSB3b3JrZXJcbiAgICBlbnZfZmlsZTpcbiAgICAgIC0gLmVudlxuXG4gIHNwYWNlOlxuICAgIGltYWdlOiBtYWtlcGxhbmUvcGxhbmUtc3BhY2U6JHtBUFBfUkVMRUFTRTotdjAuMjcuMX1cbiAgICBjb21tYW5kOiBub2RlIHNwYWNlL3NlcnZlci5qcyBzcGFjZVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGFwaVxuICAgICAgLSB3b3JrZXJcbiAgICAgIC0gd2ViXG4gICAgZW52X2ZpbGU6XG4gICAgICAtIC5lbnZcblxuICBhZG1pbjpcbiAgICBpbWFnZTogbWFrZXBsYW5lL3BsYW5lLWFkbWluOiR7QVBQX1JFTEVBU0U6LXYwLjI3LjF9XG4gICAgY29tbWFuZDogbm9kZSBhZG1pbi9zZXJ2ZXIuanMgYWRtaW5cbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBhcGlcbiAgICAgIC0gd2ViXG4gICAgZW52X2ZpbGU6XG4gICAgICAtIC5lbnZcblxuICBsaXZlOlxuICAgIGltYWdlOiBtYWtlcGxhbmUvcGxhbmUtbGl2ZToke0FQUF9SRUxFQVNFOi12MC4yNy4xfVxuICAgIGNvbW1hbmQ6IG5vZGUgbGl2ZS9kaXN0L3NlcnZlci5qcyBsaXZlXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gYXBpXG4gICAgICAtIHdlYlxuICAgIGVudl9maWxlOlxuICAgICAgLSAuZW52XG5cbiAgYXBpOlxuICAgIGltYWdlOiBtYWtlcGxhbmUvcGxhbmUtYmFja2VuZDoke0FQUF9SRUxFQVNFOi12MC4yNy4xfVxuICAgIGNvbW1hbmQ6IC4vYmluL2RvY2tlci1lbnRyeXBvaW50LWFwaS5zaFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGxvZ3NfYXBpOi9jb2RlL3BsYW5lL2xvZ3NcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBwbGFuZS1kYlxuICAgICAgLSBwbGFuZS1yZWRpc1xuICAgICAgLSBwbGFuZS1tcVxuICAgIGVudl9maWxlOlxuICAgICAgLSAuZW52XG5cbiAgd29ya2VyOlxuICAgIGltYWdlOiBtYWtlcGxhbmUvcGxhbmUtYmFja2VuZDoke0FQUF9SRUxFQVNFOi12MC4yNy4xfVxuICAgIGNvbW1hbmQ6IC4vYmluL2RvY2tlci1lbnRyeXBvaW50LXdvcmtlci5zaFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGxvZ3Nfd29ya2VyOi9jb2RlL3BsYW5lL2xvZ3NcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBhcGlcbiAgICAgIC0gcGxhbmUtZGJcbiAgICAgIC0gcGxhbmUtcmVkaXNcbiAgICAgIC0gcGxhbmUtbXFcbiAgICBlbnZfZmlsZTpcbiAgICAgIC0gLmVudlxuXG4gIGJlYXQtd29ya2VyOlxuICAgIGltYWdlOiBtYWtlcGxhbmUvcGxhbmUtYmFja2VuZDoke0FQUF9SRUxFQVNFOi12MC4yNy4xfVxuICAgIGNvbW1hbmQ6IC4vYmluL2RvY2tlci1lbnRyeXBvaW50LWJlYXQuc2hcbiAgICB2b2x1bWVzOlxuICAgICAgLSBsb2dzX2JlYXQtd29ya2VyOi9jb2RlL3BsYW5lL2xvZ3NcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBhcGlcbiAgICAgIC0gcGxhbmUtZGJcbiAgICAgIC0gcGxhbmUtcmVkaXNcbiAgICAgIC0gcGxhbmUtbXFcbiAgICBlbnZfZmlsZTpcbiAgICAgIC0gLmVudlxuXG4gIG1pZ3JhdG9yOlxuICAgIGltYWdlOiBtYWtlcGxhbmUvcGxhbmUtYmFja2VuZDoke0FQUF9SRUxFQVNFOi12MC4yNy4xfVxuICAgIGNvbW1hbmQ6IC4vYmluL2RvY2tlci1lbnRyeXBvaW50LW1pZ3JhdG9yLnNoXG4gICAgdm9sdW1lczpcbiAgICAgIC0gbG9nc19taWdyYXRvcjovY29kZS9wbGFuZS9sb2dzXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcGxhbmUtZGJcbiAgICAgIC0gcGxhbmUtcmVkaXNcbiAgICBlbnZfZmlsZTpcbiAgICAgIC0gLmVudlxuXG4gIHBsYW5lLWRiOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNy1hbHBpbmVcbiAgICBjb21tYW5kOiBwb3N0Z3JlcyAtYyAnbWF4X2Nvbm5lY3Rpb25zPTEwMDAnXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcGdkYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudl9maWxlOlxuICAgICAgLSAuZW52XG5cbiAgcGxhbmUtcmVkaXM6XG4gICAgaW1hZ2U6IHZhbGtleS92YWxrZXk6Ny4yLjUtYWxwaW5lXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcmVkaXNkYXRhOi9kYXRhXG4gICAgZW52X2ZpbGU6XG4gICAgICAtIC5lbnZcblxuICBwbGFuZS1tcTpcbiAgICBpbWFnZTogcmFiYml0bXE6My4xMy42LW1hbmFnZW1lbnQtYWxwaW5lXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcmFiYml0bXFfZGF0YTovdmFyL2xpYi9yYWJiaXRtcVxuICAgIGVudl9maWxlOlxuICAgICAgLSAuZW52XG5cbiAgcGxhbmUtbWluaW86XG4gICAgaW1hZ2U6IG1pbmlvL21pbmlvOmxhdGVzdFxuICAgIGNvbW1hbmQ6IHNlcnZlciAvZXhwb3J0IC0tY29uc29sZS1hZGRyZXNzIFwiOjkwOTBcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIHVwbG9hZHM6L2V4cG9ydFxuICAgIGVudl9maWxlOlxuICAgICAgLSAuZW52XG5cbiAgcHJveHk6XG4gICAgaW1hZ2U6IG1ha2VwbGFuZS9wbGFuZS1wcm94eToke0FQUF9SRUxFQVNFOi12MC4yNy4xfVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHdlYlxuICAgICAgLSBhcGlcbiAgICAgIC0gc3BhY2VcbiAgICBlbnZfZmlsZTpcbiAgICAgIC0gLmVudlxuXG52b2x1bWVzOlxuICBwZ2RhdGE6XG4gIHJlZGlzZGF0YTpcbiAgdXBsb2FkczpcbiAgbG9nc19hcGk6XG4gIGxvZ3Nfd29ya2VyOlxuICBsb2dzX2JlYXQtd29ya2VyOlxuICBsb2dzX21pZ3JhdG9yOlxuICByYWJiaXRtcV9kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5taW5pb19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxucmFiYml0bXFfdXNlciA9IFwiJHt1c2VybmFtZX1cIlxucmFiYml0bXFfcGFzcyA9IFwiJHtwYXNzd29yZDozMn1cIlxuc2VjcmV0X2tleSA9IFwiJHtiYXNlNjQ6NDh9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcblwiRG9tYWluPSR7ZG9tYWlufVwiLFxuXCJXRUJfVVJMPSR7RG9tYWlufVwiLFxuXCJQR0hPU1Q9cGxhbmUtZGJcIixcblwiUEdEQVRBQkFTRT1wbGFuZVwiLFxuXCJQT1NUR1JFU19VU0VSPSR7dXNlcm5hbWV9XCIsXG5cIlBPU1RHUkVTX1BBU1NXT1JEPSR7ZGJfcGFzc3dvcmR9XCIsXG5cIlBPU1RHUkVTX0RCPXBsYW5lXCIsXG5cIlBPU1RHUkVTX1BPUlQ9NTQzMlwiLFxuXCJQR0RBVEE9L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXCIsXG5cIlJFRElTX0hPU1Q9cGxhbmUtcmVkaXNcIixcblwiUkVESVNfUE9SVD02Mzc5XCIsXG5cIlJFRElTX1VSTD1yZWRpczovL3BsYW5lLXJlZGlzOjYzNzkvXCIsXG5cIk1JTklPX1JPT1RfVVNFUj1hY2Nlc3Mta2V5XCIsXG5cIk1JTklPX1JPT1RfUEFTU1dPUkQ9JHttaW5pb19wYXNzd29yZH1cIixcblwiQVdTX1JFR0lPTj1cIixcblwiQVdTX0FDQ0VTU19LRVlfSUQ9JHtNSU5JT19ST09UX1VTRVJ9XCIsXG5cIkFXU19TRUNSRVRfQUNDRVNTX0tFWT0ke21pbmlvX3Bhc3N3b3JkfVwiLFxuXCJBV1NfUzNfRU5EUE9JTlRfVVJMPWh0dHA6Ly9wbGFuZS1taW5pbzo5MDAwXCIsXG5cIkFXU19TM19CVUNLRVRfTkFNRT11cGxvYWRzXCIsXG5cIk5HSU5YX1BPUlQ9ODBcIixcblwiQlVDS0VUX05BTUU9dXBsb2Fkc1wiLFxuXCJGSUxFX1NJWkVfTElNSVQ9NTI0Mjg4MFwiLFxuXCJSQUJCSVRNUV9IT1NUPXBsYW5lLW1xXCIsXG5cIlJBQkJJVE1RX1BPUlQ9NTY3MlwiLFxuXCJSQUJCSVRNUV9ERUZBVUxUX1VTRVI9cmFiYml0bXFfdXNlclwiLFxuXCJSQUJCSVRNUV9ERUZBVUxUX1BBU1M9JHtyYWJiaXRtcV9wYXNzfVwiLFxuXCJSQUJCSVRNUV9ERUZBVUxUX1ZIT1NUPXBsYW5lXCIsXG5cIlJBQkJJVE1RX1ZIT1NUPXBsYW5lXCIsXG5cIkFQSV9CQVNFX1VSTD1odHRwOi8vYXBpOjgwMDBcIixcblwiREVCVUc9MFwiLFxuXCJTRU5UUllfRFNOPVwiLFxuXCJTRU5UUllfRU5WSVJPTk1FTlQ9cHJvZHVjdGlvblwiLFxuXCJDT1JTX0FMTE9XRURfT1JJR0lOUz1odHRwczovLyR7RG9tYWlufVwiLFxuXCJHVU5JQ09STl9XT1JLRVJTPTFcIixcblwiVVNFX01JTklPPTFcIixcblwiREFUQUJBU0VfVVJMPXBvc3RncmVzcWw6Ly8ke1BPU1RHUkVTX1VTRVJ9OiR7UE9TVEdSRVNfUEFTU1dPUkR9QHBsYW5lLWRiL3BsYW5lXCIsXG5cIlNFQ1JFVF9LRVk9JHtzZWNyZXRfa2V5fVwiLFxuXCJBTVFQX1VSTD1hbXFwOi8vJHtSQUJCSVRNUV9ERUZBVUxUX1VTRVJ9OiR7UkFCQklUTVFfREVGQVVMVF9QQVNTfUBwbGFuZS1tcTo1NjcyL3BsYW5lXCIsXG5cIkFQSV9LRVlfUkFURV9MSU1JVD02MC9taW51dGVcIixcblwiTUlOSU9fRU5EUE9JTlRfU1NMPTBcIlxuXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicHJveHlcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`kanban`

---

Version:`v0.27.1`

PinchflatPinchflat is a self-hosted YouTube downloader that allows you to download videos and playlists with a simple web interface.

PlarkSelf-hosted Website Builder

### On this page

ConfigurationBase64LinksTags