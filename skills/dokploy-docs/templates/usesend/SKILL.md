---
title: "useSend | Dokploy"
source: "https://docs.dokploy.com/docs/templates/usesend"
category: dokploy-docs
created: "2026-06-25T17:22:01.420Z"
---

useSend | Dokploy

# useSend

Copy as Markdown

Open source alternative to Resend, Sendgrid, Postmark etc.

## Configuration

docker-compose.ymltemplate.toml

```
name: usesend-prod

services:
  usesend-db-prod:
    image: postgres:16

    restart: always
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5
    # ports:
    #   - "5432:5432"
    volumes:
      - database:/var/lib/postgresql/data

  usesend-redis-prod:
    image: redis:7

    restart: always
    # ports:
    #   - "6379:6379"
    volumes:
      - cache:/data
    command: ["redis-server", "--maxmemory-policy", "noeviction"]

  usesend-storage-prod:
    image: minio/minio:latest

    ports:
      - 9002
      - 9001
    volumes:
      - storage:/data
    environment:
      MINIO_ROOT_USER: usesend
      MINIO_ROOT_PASSWORD: password
    entrypoint: sh
    command: -c 'mkdir -p /data/usesend && minio server /data --console-address ":9001" --address ":9002"'

  usesend:
    image: usesend/usesend:latest
    restart: always
    ports:
      - ${PORT:-3000}
    environment:
      - PORT=${PORT:-3000}
      - DATABASE_URL=${DATABASE_URL}
      - NEXTAUTH_URL=${NEXTAUTH_URL}
      - NEXTAUTH_SECRET=${NEXTAUTH_SECRET}
      - AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}
      - AWS_SECRET_KEY=${AWS_SECRET_KEY}
      - AWS_ACCESS_KEY=${AWS_ACCESS_KEY}
      - GITHUB_ID=${GITHUB_ID}
      - GITHUB_SECRET=${GITHUB_SECRET}
      - REDIS_URL=${REDIS_URL}
      - NEXT_PUBLIC_IS_CLOUD=${NEXT_PUBLIC_IS_CLOUD:-false}
      - API_RATE_LIMIT=${API_RATE_LIMIT:-1}
    depends_on:
      usesend-db-prod:
        condition: service_healthy
      usesend-redis-prod:
        condition: service_started

volumes:
  database:
  cache:
  storage:
```

```
[variables]
main_domain = "${domain}"
secret_base = "${base64:64}"

[config]
mounts = []

[[config.domains]]
serviceName = "usesend"
port = 3_000
host = "${main_domain}"

[config.env]
REDIS_URL = "redis://usesend-redis-prod:6379"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"
POSTGRES_DB = "usesend"
DATABASE_URL = "postgresql://postgres:postgres@usesend-db-prod:5432/usesend"
NEXTAUTH_URL = "http://localhost:3000"
NEXTAUTH_SECRET = "${secret_base}"
GITHUB_ID = "'Fill'"
GITHUB_SECRET = "'Fill'"
AWS_DEFAULT_REGION = "us-east-1"
AWS_SECRET_KEY = "'Fill'"
AWS_ACCESS_KEY = "'Fill'"
DOCKER_OUTPUT = "1"
API_RATE_LIMIT = "1"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIm5hbWU6IHVzZXNlbmQtcHJvZFxuXG5zZXJ2aWNlczpcbiAgdXNlc2VuZC1kYi1wcm9kOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNlxuXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX1VTRVI9JHtQT1NUR1JFU19VU0VSfVxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgLSBQT1NUR1JFU19EQj0ke1BPU1RHUkVTX0RCfVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSAke1BPU1RHUkVTX1VTRVJ9XCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgICMgcG9ydHM6XG4gICAgIyAgIC0gXCI1NDMyOjU0MzJcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRhdGFiYXNlOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuXG4gIHVzZXNlbmQtcmVkaXMtcHJvZDpcbiAgICBpbWFnZTogcmVkaXM6N1xuXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgIyBwb3J0czpcbiAgICAjICAgLSBcIjYzNzk6NjM3OVwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gY2FjaGU6L2RhdGFcbiAgICBjb21tYW5kOiBbXCJyZWRpcy1zZXJ2ZXJcIiwgXCItLW1heG1lbW9yeS1wb2xpY3lcIiwgXCJub2V2aWN0aW9uXCJdXG5cbiAgdXNlc2VuZC1zdG9yYWdlLXByb2Q6XG4gICAgaW1hZ2U6IG1pbmlvL21pbmlvOmxhdGVzdFxuXG4gICAgcG9ydHM6XG4gICAgICAtIDkwMDJcbiAgICAgIC0gOTAwMVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHN0b3JhZ2U6L2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE1JTklPX1JPT1RfVVNFUjogdXNlc2VuZFxuICAgICAgTUlOSU9fUk9PVF9QQVNTV09SRDogcGFzc3dvcmRcbiAgICBlbnRyeXBvaW50OiBzaFxuICAgIGNvbW1hbmQ6IC1jICdta2RpciAtcCAvZGF0YS91c2VzZW5kICYmIG1pbmlvIHNlcnZlciAvZGF0YSAtLWNvbnNvbGUtYWRkcmVzcyBcIjo5MDAxXCIgLS1hZGRyZXNzIFwiOjkwMDJcIidcblxuICB1c2VzZW5kOlxuICAgIGltYWdlOiB1c2VzZW5kL3VzZXNlbmQ6bGF0ZXN0XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgcG9ydHM6XG4gICAgICAtICR7UE9SVDotMzAwMH1cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9SVD0ke1BPUlQ6LTMwMDB9XG4gICAgICAtIERBVEFCQVNFX1VSTD0ke0RBVEFCQVNFX1VSTH1cbiAgICAgIC0gTkVYVEFVVEhfVVJMPSR7TkVYVEFVVEhfVVJMfVxuICAgICAgLSBORVhUQVVUSF9TRUNSRVQ9JHtORVhUQVVUSF9TRUNSRVR9XG4gICAgICAtIEFXU19ERUZBVUxUX1JFR0lPTj0ke0FXU19ERUZBVUxUX1JFR0lPTn1cbiAgICAgIC0gQVdTX1NFQ1JFVF9LRVk9JHtBV1NfU0VDUkVUX0tFWX1cbiAgICAgIC0gQVdTX0FDQ0VTU19LRVk9JHtBV1NfQUNDRVNTX0tFWX1cbiAgICAgIC0gR0lUSFVCX0lEPSR7R0lUSFVCX0lEfVxuICAgICAgLSBHSVRIVUJfU0VDUkVUPSR7R0lUSFVCX1NFQ1JFVH1cbiAgICAgIC0gUkVESVNfVVJMPSR7UkVESVNfVVJMfVxuICAgICAgLSBORVhUX1BVQkxJQ19JU19DTE9VRD0ke05FWFRfUFVCTElDX0lTX0NMT1VEOi1mYWxzZX1cbiAgICAgIC0gQVBJX1JBVEVfTElNSVQ9JHtBUElfUkFURV9MSU1JVDotMX1cbiAgICBkZXBlbmRzX29uOlxuICAgICAgdXNlc2VuZC1kYi1wcm9kOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgdXNlc2VuZC1yZWRpcy1wcm9kOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2Vfc3RhcnRlZFxuXG52b2x1bWVzOlxuICBkYXRhYmFzZTpcbiAgY2FjaGU6XG4gIHN0b3JhZ2U6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuc2VjcmV0X2Jhc2UgPSBcIiR7YmFzZTY0OjY0fVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ1c2VzZW5kXCJcbnBvcnQgPSAzXzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblJFRElTX1VSTCA9IFwicmVkaXM6Ly91c2VzZW5kLXJlZGlzLXByb2Q6NjM3OVwiXG5QT1NUR1JFU19VU0VSID0gXCJwb3N0Z3Jlc1wiXG5QT1NUR1JFU19QQVNTV09SRCA9IFwicG9zdGdyZXNcIlxuUE9TVEdSRVNfREIgPSBcInVzZXNlbmRcIlxuREFUQUJBU0VfVVJMID0gXCJwb3N0Z3Jlc3FsOi8vcG9zdGdyZXM6cG9zdGdyZXNAdXNlc2VuZC1kYi1wcm9kOjU0MzIvdXNlc2VuZFwiXG5ORVhUQVVUSF9VUkwgPSBcImh0dHA6Ly9sb2NhbGhvc3Q6MzAwMFwiXG5ORVhUQVVUSF9TRUNSRVQgPSBcIiR7c2VjcmV0X2Jhc2V9XCJcbkdJVEhVQl9JRCA9IFwiJ0ZpbGwnXCJcbkdJVEhVQl9TRUNSRVQgPSBcIidGaWxsJ1wiXG5BV1NfREVGQVVMVF9SRUdJT04gPSBcInVzLWVhc3QtMVwiXG5BV1NfU0VDUkVUX0tFWSA9IFwiJ0ZpbGwnXCJcbkFXU19BQ0NFU1NfS0VZID0gXCInRmlsbCdcIlxuRE9DS0VSX09VVFBVVCA9IFwiMVwiXG5BUElfUkFURV9MSU1JVCA9IFwiMVwiXG4iCn0=
```

## Links

`e-mail`,`marketing`,`business`,`self-hosted`

---

Version:`latest`

Uptime KumaUptime Kuma is a free and open source monitoring tool that allows you to monitor your websites and applications.

ValkeyValkey is an open-source fork of Redis, backed by AWS and the Linux Foundation. It provides a high-performance, in-memory data structure store with Redis compatibility.

### On this page

ConfigurationBase64LinksTags