---
title: "Zipline | Dokploy"
source: "https://docs.dokploy.com/docs/templates/zipline"
category: dokploy-docs
created: "2026-06-25T17:22:02.524Z"
---

Zipline | Dokploy

# Zipline

Copy as Markdown

A ShareX/file upload server that is easy to use, packed with features, and with an easy setup!

## Configuration

docker-compose.ymltemplate.toml

```
services:
  postgres:
    image: postgres:15
    restart: unless-stopped
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DATABASE=postgres
    volumes:
      - pg_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  zipline:
    image: ghcr.io/diced/zipline:v4
    restart: unless-stopped
    environment:
      - CORE_RETURN_HTTPS=${ZIPLINE_RETURN_HTTPS}
      - CORE_SECRET=${ZIPLINE_SECRET}
      - CORE_HOSTNAME=0.0.0.0
      - CORE_PORT=${ZIPLINE_PORT}
      - DATABASE_URL=postgres://postgres:postgres@postgres/postgres
      - CORE_LOGGER=${ZIPLINE_LOGGER}
      - DATASOURCE_TYPE=local
      - DATASOURCE_LOCAL_DIRECTORY=./uploads
    volumes:
      - "../files/uploads:/zipline/uploads"
      - "../files/public:/zipline/public"
    depends_on:
      - "postgres"

volumes:
  pg_data:
```

```
[variables]
main_domain = "${domain}"
secret_base = "${base64:64}"

[config]
mounts = []

[[config.domains]]
serviceName = "zipline"
port = 3_000
host = "${main_domain}"

[config.env]
ZIPLINE_PORT = "3000"
ZIPLINE_SECRET = "${secret_base}"
ZIPLINE_RETURN_HTTPS = "false"
ZIPLINE_LOGGER = "true"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19VU0VSPXBvc3RncmVzXG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPXBvc3RncmVzXG4gICAgICAtIFBPU1RHUkVTX0RBVEFCQVNFPXBvc3RncmVzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcGdfZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgcG9zdGdyZXNcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG5cbiAgemlwbGluZTpcbiAgICBpbWFnZTogZ2hjci5pby9kaWNlZC96aXBsaW5lOnY0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQ09SRV9SRVRVUk5fSFRUUFM9JHtaSVBMSU5FX1JFVFVSTl9IVFRQU31cbiAgICAgIC0gQ09SRV9TRUNSRVQ9JHtaSVBMSU5FX1NFQ1JFVH1cbiAgICAgIC0gQ09SRV9IT1NUTkFNRT0wLjAuMC4wXG4gICAgICAtIENPUkVfUE9SVD0ke1pJUExJTkVfUE9SVH1cbiAgICAgIC0gREFUQUJBU0VfVVJMPXBvc3RncmVzOi8vcG9zdGdyZXM6cG9zdGdyZXNAcG9zdGdyZXMvcG9zdGdyZXNcbiAgICAgIC0gQ09SRV9MT0dHRVI9JHtaSVBMSU5FX0xPR0dFUn1cbiAgICAgIC0gREFUQVNPVVJDRV9UWVBFPWxvY2FsXG4gICAgICAtIERBVEFTT1VSQ0VfTE9DQUxfRElSRUNUT1JZPS4vdXBsb2Fkc1xuICAgIHZvbHVtZXM6XG4gICAgICAtIFwiLi4vZmlsZXMvdXBsb2FkczovemlwbGluZS91cGxvYWRzXCJcbiAgICAgIC0gXCIuLi9maWxlcy9wdWJsaWM6L3ppcGxpbmUvcHVibGljXCJcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBcInBvc3RncmVzXCJcblxudm9sdW1lczpcbiAgcGdfZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5zZWNyZXRfYmFzZSA9IFwiJHtiYXNlNjQ6NjR9XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInppcGxpbmVcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuWklQTElORV9QT1JUID0gXCIzMDAwXCJcblpJUExJTkVfU0VDUkVUID0gXCIke3NlY3JldF9iYXNlfVwiXG5aSVBMSU5FX1JFVFVSTl9IVFRQUyA9IFwiZmFsc2VcIlxuWklQTElORV9MT0dHRVIgPSBcInRydWVcIlxuIgp9
```

## Links

`media system`,`storage`

---

Version:`v3.7.9`

ZabbixZabbix is an open-source enterprise-grade monitoring platform for networks, servers, virtual machines, and cloud services. This template includes PostgreSQL, Nginx frontend, SNMP traps, and Java gateway.

ZitadelOpen-source identity and access management platform with multi-tenancy, OpenID Connect, SAML, and OAuth 2.0 support.

### On this page

ConfigurationBase64LinksTags