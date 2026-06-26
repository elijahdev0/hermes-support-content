---
title: "Tianji | Dokploy"
source: "https://docs.dokploy.com/docs/templates/tianji"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

Tianji | Dokploy

# Tianji

Copy as Markdown

Tianji is a lightweight web analytic service and uptime monitoring tool.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3'
services:
  tianji:
    image: moonrailgun/tianji
    ports:
      - "12345"
    environment:
      DATABASE_URL: postgresql://tianji:tianji@postgres:5432/tianji
      # API Key
      JWT_SECRET: ${jwt_secret}
      ALLOW_REGISTER: "false"
      ALLOW_OPENAPI: "true"
    depends_on:
      - postgres
  postgres:
    image: postgres:15.4-alpine
    environment:
      POSTGRES_DB: tianji
      POSTGRES_USER: tianji
      POSTGRES_PASSWORD: tianji
    volumes:
      - tianji-db-data:/var/lib/postgresql/data
volumes:
  tianji-db-data: {}
```

```
[variables]
main_domain = "${domain}"
# API Key: Used for session security.
jwt_secret = "${password:32}"

[config]
[[config.domains]]
serviceName = "tianji"
port = 12345
host = "${main_domain}"

[[config.mounts]]
serviceName = "postgres"
type = "volume"
source = "tianji-db-data"
target = "/var/lib/postgresql/data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczJ1xuc2VydmljZXM6XG4gIHRpYW5qaTpcbiAgICBpbWFnZTogbW9vbnJhaWxndW4vdGlhbmppXG4gICAgcG9ydHM6XG4gICAgICAtIFwiMTIzNDVcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgREFUQUJBU0VfVVJMOiBwb3N0Z3Jlc3FsOi8vdGlhbmppOnRpYW5qaUBwb3N0Z3Jlczo1NDMyL3RpYW5qaVxuICAgICAgIyBBUEkgS2V5XG4gICAgICBKV1RfU0VDUkVUOiAke2p3dF9zZWNyZXR9XG4gICAgICBBTExPV19SRUdJU1RFUjogXCJmYWxzZVwiXG4gICAgICBBTExPV19PUEVOQVBJOiBcInRydWVcIlxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHBvc3RncmVzXG4gIHBvc3RncmVzOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNS40LWFscGluZVxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6IHRpYW5qaVxuICAgICAgUE9TVEdSRVNfVVNFUjogdGlhbmppXG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogdGlhbmppXG4gICAgdm9sdW1lczpcbiAgICAgIC0gdGlhbmppLWRiLWRhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG52b2x1bWVzOlxuICB0aWFuamktZGItZGF0YToge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG4jIEFQSSBLZXk6IFVzZWQgZm9yIHNlc3Npb24gc2VjdXJpdHkuXG5qd3Rfc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ0aWFuamlcIlxucG9ydCA9IDEyMzQ1XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwicG9zdGdyZXNcIlxudHlwZSA9IFwidm9sdW1lXCJcbnNvdXJjZSA9IFwidGlhbmppLWRiLWRhdGFcIlxudGFyZ2V0ID0gXCIvdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcIlxuIgp9
```

## Links

`analytics`,`monitoring`,`web`,`uptime`

---

Version:`latest`

teableTeable is a Super fast, Real-time, Professional, Developer friendly, No-code database built on Postgres. It uses a simple, spreadsheet-like interface to create complex enterprise-level database applications. Unlock efficient app development with no-code, free from the hurdles of data security and scalability.

TolgeeDeveloper & translator friendly web-based localization platform

### On this page

ConfigurationBase64LinksTags