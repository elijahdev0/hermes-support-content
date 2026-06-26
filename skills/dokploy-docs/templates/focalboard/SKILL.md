---
title: "Focalboard | Dokploy"
source: "https://docs.dokploy.com/docs/templates/focalboard"
category: dokploy-docs
created: "2026-06-25T17:21:48.521Z"
---

Focalboard | Dokploy

# Focalboard

Copy as Markdown

Open source project management for technical teams

## Configuration

docker-compose.ymltemplate.toml

```
version: '3'

services:
  focalboard:
    image: mattermost/focalboard:7.11.4
    restart: unless-stopped
    volumes:
      - focalboardData:/opt/focalboard/data
    environment:
      - VIRTUAL_HOST
      - VIRTUAL_PORT
      - DB_TYPE
      - DB_CONFIG=postgres://${POSTGRES_USER}:${POSTGRES_password}@postgres:5432/${postgres_db}?sslmode=disable

  postgres:
    image: postgres:17
    environment:
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_DB
    volumes:
      - ./postgres_data:/var/lib/postgresql/data

volumes:
  focalboardData:
    driver: local
  focalboardPostgre:
    driver: local
```

```
[variables]
main_domain = "${domain}"

[config]
env = [
      "VIRTUAL_HOST=${main_domain}",
      "VIRTUAL_PORT=8000 # Do Not Alter",
      "DB_TYPE=postgres",
      "POSTGRES_USER=focalboard",
      "POSTGRES_PASSWORD=${password:32}",
      "POSTGRES_DB=focalboard"
    ]
mounts = []

[[config.domains]]
serviceName = "focalboard"
port = 8000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczJ1xuXG5zZXJ2aWNlczpcbiAgZm9jYWxib2FyZDpcbiAgICBpbWFnZTogbWF0dGVybW9zdC9mb2NhbGJvYXJkOjcuMTEuNFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZm9jYWxib2FyZERhdGE6L29wdC9mb2NhbGJvYXJkL2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gVklSVFVBTF9IT1NUXG4gICAgICAtIFZJUlRVQUxfUE9SVFxuICAgICAgLSBEQl9UWVBFXG4gICAgICAtIERCX0NPTkZJRz1wb3N0Z3JlczovLyR7UE9TVEdSRVNfVVNFUn06JHtQT1NUR1JFU19wYXNzd29yZH1AcG9zdGdyZXM6NTQzMi8ke3Bvc3RncmVzX2RifT9zc2xtb2RlPWRpc2FibGVcblxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTdcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfVVNFUlxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRFxuICAgICAgLSBQT1NUR1JFU19EQlxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4vcG9zdGdyZXNfZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcblxudm9sdW1lczpcbiAgZm9jYWxib2FyZERhdGE6XG4gICAgZHJpdmVyOiBsb2NhbFxuICBmb2NhbGJvYXJkUG9zdGdyZTpcbiAgICBkcml2ZXI6IGxvY2FsIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgICAgIFwiVklSVFVBTF9IT1NUPSR7bWFpbl9kb21haW59XCIsXG4gICAgICBcIlZJUlRVQUxfUE9SVD04MDAwICMgRG8gTm90IEFsdGVyXCIsXG4gICAgICBcIkRCX1RZUEU9cG9zdGdyZXNcIixcbiAgICAgIFwiUE9TVEdSRVNfVVNFUj1mb2NhbGJvYXJkXCIsXG4gICAgICBcIlBPU1RHUkVTX1BBU1NXT1JEPSR7cGFzc3dvcmQ6MzJ9XCIsXG4gICAgICBcIlBPU1RHUkVTX0RCPWZvY2FsYm9hcmRcIlxuICAgIF1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImZvY2FsYm9hcmRcIlxucG9ydCA9IDgwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`kanban`

---

Version:`8.0.0`

FMD ServerA server to communicate with the FMD Android app, to locate and control your devices.

FonosterFonoster is an open-source alternative to Twilio. A complete telephony stack for building voice applications with SIP, WebRTC, and PSTN connectivity.

### On this page

ConfigurationBase64LinksTags