---
title: "Metabase | Dokploy"
source: "https://docs.dokploy.com/docs/templates/metabase"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

Metabase | Dokploy

# Metabase

Copy as Markdown

Metabase is an open source business intelligence tool that allows you to ask questions and visualize data.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  metabase:
    image: metabase/metabase:v0.50.8
    volumes:
      - /dev/urandom:/dev/random:ro
    environment:
      MB_DB_TYPE: postgres
      MB_DB_DBNAME: metabaseappdb
      MB_DB_PORT: 5432
      MB_DB_USER: metabase
      MB_DB_PASS: mysecretpassword
      MB_DB_HOST: postgres
    healthcheck:
      test: curl --fail -I http://localhost:3000/api/health || exit 1
      interval: 15s
      timeout: 5s
      retries: 5
  postgres:
    image: postgres:14
    environment:
      POSTGRES_USER: metabase
      POSTGRES_DB: metabaseappdb
      POSTGRES_PASSWORD: mysecretpassword
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "metabase"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBtZXRhYmFzZTpcbiAgICBpbWFnZTogbWV0YWJhc2UvbWV0YWJhc2U6djAuNTAuOFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC9kZXYvdXJhbmRvbTovZGV2L3JhbmRvbTpyb1xuICAgIGVudmlyb25tZW50OlxuICAgICAgTUJfREJfVFlQRTogcG9zdGdyZXNcbiAgICAgIE1CX0RCX0RCTkFNRTogbWV0YWJhc2VhcHBkYlxuICAgICAgTUJfREJfUE9SVDogNTQzMlxuICAgICAgTUJfREJfVVNFUjogbWV0YWJhc2VcbiAgICAgIE1CX0RCX1BBU1M6IG15c2VjcmV0cGFzc3dvcmRcbiAgICAgIE1CX0RCX0hPU1Q6IHBvc3RncmVzXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBjdXJsIC0tZmFpbCAtSSBodHRwOi8vbG9jYWxob3N0OjMwMDAvYXBpL2hlYWx0aCB8fCBleGl0IDFcbiAgICAgIGludGVydmFsOiAxNXNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG4gIHBvc3RncmVzOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNFxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfVVNFUjogbWV0YWJhc2VcbiAgICAgIFBPU1RHUkVTX0RCOiBtZXRhYmFzZWFwcGRiXG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogbXlzZWNyZXRwYXNzd29yZFxuXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0ge31cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIm1ldGFiYXNlXCJcbnBvcnQgPSAzXzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`database`,`dashboard`

---

Version:`v0.50.8`

MemosMemos is a self-hosted, open-source note-taking application that allows you to create, organize, and share notes with ease. It provides a simple and effective solution for managing your notes from anywhere.

MeTubeMeTube is a web-based YouTube downloader that allows downloading videos and audio using yt-dlp.

### On this page

ConfigurationBase64LinksTags