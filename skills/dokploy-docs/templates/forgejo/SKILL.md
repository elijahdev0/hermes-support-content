---
title: "Forgejo | Dokploy"
source: "https://docs.dokploy.com/docs/templates/forgejo"
category: dokploy-docs
created: "2026-06-25T17:21:48.521Z"
---

Forgejo | Dokploy

# Forgejo

Copy as Markdown

Forgejo is a self-hosted lightweight software forge. Easy to install and low maintenance, it just does the job

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  forgejo:
    image: codeberg.org/forgejo/forgejo:10
    environment:
      - USER_UID=${USER_UID}
      - USER_GID=${USER_GID}
      - FORGEJO__database__DB_TYPE=postgres
      - FORGEJO__database__HOST=db:5432
      - FORGEJO__database__NAME=forgejo
      - FORGEJO__database__USER=forgejo
      - FORGEJO__database__PASSWD=forgejo
    restart: always

    volumes:
      - forgejo_server:/data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    depends_on:
      - db

  db:
    image: postgres:17
    restart: always
    environment:
      - POSTGRES_USER=forgejo
      - POSTGRES_PASSWORD=forgejo
      - POSTGRES_DB=forgejo

    volumes:
      - forgejo_db:/var/lib/postgresql/data

volumes:
  forgejo_db:
    driver: local
  forgejo_server:
    driver: local
```

```
[variables]
main_domain = "${domain}"

[config]
env = ["USER_UID=1000", "USER_GID=1000"]
mounts = []

[[config.domains]]
serviceName = "forgejo"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBmb3JnZWpvOlxuICAgIGltYWdlOiBjb2RlYmVyZy5vcmcvZm9yZ2Vqby9mb3JnZWpvOjEwXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFVTRVJfVUlEPSR7VVNFUl9VSUR9XG4gICAgICAtIFVTRVJfR0lEPSR7VVNFUl9HSUR9XG4gICAgICAtIEZPUkdFSk9fX2RhdGFiYXNlX19EQl9UWVBFPXBvc3RncmVzXG4gICAgICAtIEZPUkdFSk9fX2RhdGFiYXNlX19IT1NUPWRiOjU0MzJcbiAgICAgIC0gRk9SR0VKT19fZGF0YWJhc2VfX05BTUU9Zm9yZ2Vqb1xuICAgICAgLSBGT1JHRUpPX19kYXRhYmFzZV9fVVNFUj1mb3JnZWpvXG4gICAgICAtIEZPUkdFSk9fX2RhdGFiYXNlX19QQVNTV0Q9Zm9yZ2Vqb1xuICAgIHJlc3RhcnQ6IGFsd2F5c1xuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZm9yZ2Vqb19zZXJ2ZXI6L2RhdGFcbiAgICAgIC0gL2V0Yy90aW1lem9uZTovZXRjL3RpbWV6b25lOnJvXG4gICAgICAtIC9ldGMvbG9jYWx0aW1lOi9ldGMvbG9jYWx0aW1lOnJvXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gZGJcblxuICBkYjpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTdcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfVVNFUj1mb3JnZWpvXG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPWZvcmdlam9cbiAgICAgIC0gUE9TVEdSRVNfREI9Zm9yZ2Vqb1xuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZm9yZ2Vqb19kYjovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcblxudm9sdW1lczpcbiAgZm9yZ2Vqb19kYjpcbiAgICBkcml2ZXI6IGxvY2FsXG4gIGZvcmdlam9fc2VydmVyOlxuICAgIGRyaXZlcjogbG9jYWwiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1wiVVNFUl9VSUQ9MTAwMFwiLCBcIlVTRVJfR0lEPTEwMDBcIl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImZvcmdlam9cIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`self-hosted`,`storage`

---

Version:`10`

FonosterFonoster is an open-source alternative to Twilio. A complete telephony stack for building voice applications with SIP, WebRTC, and PSTN connectivity.

FormbricksFormbricks is an open-source survey and form platform for collecting user data.

### On this page

ConfigurationBase64LinksTags