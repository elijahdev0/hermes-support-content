---
title: "Misaka Danmu Server | Dokploy"
source: "https://docs.dokploy.com/docs/templates/misaka-danmu-server"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

Misaka Danmu Server | Dokploy

# Misaka Danmu Server

Copy as Markdown

A self-hosted danmaku (bullet comments) server for live streaming and video platforms.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  postgres:
    image: postgres:18
    restart: unless-stopped
    environment:
      - POSTGRES_PASSWORD
      - POSTGRES_USER
      - POSTGRES_DB
      - TZ=Asia/Shanghai
    volumes:
      - postgres-data:/var/lib/postgresql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U danmuapi -d danmuapi"]
      interval: 10s
      timeout: 5s
      retries: 10
      start_period: 60s

  danmu-app:
    image: l429609201/misaka_danmu_server:latest
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      - PUID=1000
      - PGID=1000
      - UMASK=0022
      - TZ=Asia/Shanghai
      - DANMUAPI_DATABASE__TYPE
      - DANMUAPI_DATABASE__HOST
      - DANMUAPI_DATABASE__PORT
      - DANMUAPI_DATABASE__NAME
      - DANMUAPI_DATABASE__USER
      - DANMUAPI_DATABASE__PASSWORD
      - DANMUAPI_ADMIN__INITIAL_USER
    volumes:
      - danmu-config:/app/config

volumes:
  postgres-data: {}
  danmu-config: {}
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:24}"
db_user = "danmuapi"
db_name = "danmuapi"

[config]
mounts = []

[[config.domains]]
serviceName = "danmu-app"
port = 7768
host = "${main_domain}"

[config.env]
# PostgreSQL
POSTGRES_PASSWORD = "${db_password}"
POSTGRES_USER = "${db_user}"
POSTGRES_DB = "${db_name}"

# Danmu App Database Connection
DANMUAPI_DATABASE__TYPE = "postgresql"
DANMUAPI_DATABASE__HOST = "postgres"
DANMUAPI_DATABASE__PORT = "5432"
DANMUAPI_DATABASE__NAME = "${db_name}"
DANMUAPI_DATABASE__USER = "${db_user}"
DANMUAPI_DATABASE__PASSWORD = "${db_password}"

# Admin
DANMUAPI_ADMIN__INITIAL_USER = "admin"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MThcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRFxuICAgICAgLSBQT1NUR1JFU19VU0VSXG4gICAgICAtIFBPU1RHUkVTX0RCXG4gICAgICAtIFRaPUFzaWEvU2hhbmdoYWlcbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlcy1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWxcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgZGFubXVhcGkgLWQgZGFubXVhcGlcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiAxMFxuICAgICAgc3RhcnRfcGVyaW9kOiA2MHNcblxuICBkYW5tdS1hcHA6XG4gICAgaW1hZ2U6IGw0Mjk2MDkyMDEvbWlzYWthX2Rhbm11X3NlcnZlcjpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGRlcGVuZHNfb246XG4gICAgICBwb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUFVJRD0xMDAwXG4gICAgICAtIFBHSUQ9MTAwMFxuICAgICAgLSBVTUFTSz0wMDIyXG4gICAgICAtIFRaPUFzaWEvU2hhbmdoYWlcbiAgICAgIC0gREFOTVVBUElfREFUQUJBU0VfX1RZUEVcbiAgICAgIC0gREFOTVVBUElfREFUQUJBU0VfX0hPU1RcbiAgICAgIC0gREFOTVVBUElfREFUQUJBU0VfX1BPUlRcbiAgICAgIC0gREFOTVVBUElfREFUQUJBU0VfX05BTUVcbiAgICAgIC0gREFOTVVBUElfREFUQUJBU0VfX1VTRVJcbiAgICAgIC0gREFOTVVBUElfREFUQUJBU0VfX1BBU1NXT1JEXG4gICAgICAtIERBTk1VQVBJX0FETUlOX19JTklUSUFMX1VTRVJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYW5tdS1jb25maWc6L2FwcC9jb25maWdcblxudm9sdW1lczpcbiAgcG9zdGdyZXMtZGF0YToge31cbiAgZGFubXUtY29uZmlnOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjI0fVwiXG5kYl91c2VyID0gXCJkYW5tdWFwaVwiXG5kYl9uYW1lID0gXCJkYW5tdWFwaVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJkYW5tdS1hcHBcIlxucG9ydCA9IDc3Njhcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG4jIFBvc3RncmVTUUxcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiXG5QT1NUR1JFU19VU0VSID0gXCIke2RiX3VzZXJ9XCJcblBPU1RHUkVTX0RCID0gXCIke2RiX25hbWV9XCJcblxuIyBEYW5tdSBBcHAgRGF0YWJhc2UgQ29ubmVjdGlvblxuREFOTVVBUElfREFUQUJBU0VfX1RZUEUgPSBcInBvc3RncmVzcWxcIlxuREFOTVVBUElfREFUQUJBU0VfX0hPU1QgPSBcInBvc3RncmVzXCJcbkRBTk1VQVBJX0RBVEFCQVNFX19QT1JUID0gXCI1NDMyXCJcbkRBTk1VQVBJX0RBVEFCQVNFX19OQU1FID0gXCIke2RiX25hbWV9XCJcbkRBTk1VQVBJX0RBVEFCQVNFX19VU0VSID0gXCIke2RiX3VzZXJ9XCJcbkRBTk1VQVBJX0RBVEFCQVNFX19QQVNTV09SRCA9IFwiJHtkYl9wYXNzd29yZH1cIlxuXG4jIEFkbWluXG5EQU5NVUFQSV9BRE1JTl9fSU5JVElBTF9VU0VSID0gXCJhZG1pblwiXG4iCn0=
```

## Links

`streaming`,`danmaku`,`live`

---

Version:`latest`

MinioMinio is an open source object storage server compatible with Amazon S3 cloud storage service.

MixpostMixpost is an open-source social media management tool that allows you to create, schedule, and publish posts across multiple social media platforms from a single interface.

### On this page

ConfigurationBase64LinksTags