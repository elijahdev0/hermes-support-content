---
title: "Authorizer | Dokploy"
source: "https://docs.dokploy.com/docs/templates/authorizer"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

Authorizer | Dokploy

# Authorizer

Copy as Markdown

Authorizer is a powerful tool designed to simplify the process of user authentication and authorization in your applications. It allows you to build secure apps 10x faster with its low code tool and low-cost deployment.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  authorizer:
    image: lakhansamani/authorizer:1.4.4
    restart: unless-stopped
    ports:
      - 8080
    environment:
      - DATABASE_TYPE=postgres
      - DATABASE_URL=postgres://postgres:${DB_PASSWORD}@authorizer-db:5432/authorizer?sslmode=disable
      - REDIS_URL=redis://authorizer-redis:6379
      - ADMIN_SECRET=${ADMIN_SECRET}
      - JWT_SECRET=${JWT_SECRET}
      - COOKIE_NAME=authorizer
      - ACCESS_TOKEN_EXPIRY_TIME=86400
      - REFRESH_TOKEN_EXPIRY_TIME=86400
      - DISABLE_PLAYGROUND=true
    depends_on:
      - authorizer-db
      - authorizer-redis

  authorizer-db:
    image: postgres:15-alpine
    restart: unless-stopped
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=authorizer
    volumes:
      - db_data:/var/lib/postgresql/data

  authorizer-redis:
    image: redis:7-alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data

volumes:
  db_data: {}
  redis_data: {}
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:16}"
admin_secret = "${password:32}"
jwt_secret = "${password:32}"

[config]
[[config.domains]]
serviceName = "authorizer"
port = 8080
host = "${main_domain}"

[config.env]
DB_PASSWORD = "${db_password}"
ADMIN_SECRET = "${admin_secret}"
JWT_SECRET = "${jwt_secret}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhdXRob3JpemVyOlxuICAgIGltYWdlOiBsYWtoYW5zYW1hbmkvYXV0aG9yaXplcjoxLjQuNFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDgwODBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gREFUQUJBU0VfVFlQRT1wb3N0Z3Jlc1xuICAgICAgLSBEQVRBQkFTRV9VUkw9cG9zdGdyZXM6Ly9wb3N0Z3Jlczoke0RCX1BBU1NXT1JEfUBhdXRob3JpemVyLWRiOjU0MzIvYXV0aG9yaXplcj9zc2xtb2RlPWRpc2FibGVcbiAgICAgIC0gUkVESVNfVVJMPXJlZGlzOi8vYXV0aG9yaXplci1yZWRpczo2Mzc5XG4gICAgICAtIEFETUlOX1NFQ1JFVD0ke0FETUlOX1NFQ1JFVH1cbiAgICAgIC0gSldUX1NFQ1JFVD0ke0pXVF9TRUNSRVR9XG4gICAgICAtIENPT0tJRV9OQU1FPWF1dGhvcml6ZXJcbiAgICAgIC0gQUNDRVNTX1RPS0VOX0VYUElSWV9USU1FPTg2NDAwXG4gICAgICAtIFJFRlJFU0hfVE9LRU5fRVhQSVJZX1RJTUU9ODY0MDBcbiAgICAgIC0gRElTQUJMRV9QTEFZR1JPVU5EPXRydWVcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBhdXRob3JpemVyLWRiXG4gICAgICAtIGF1dGhvcml6ZXItcmVkaXNcblxuICBhdXRob3JpemVyLWRiOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNS1hbHBpbmVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19VU0VSPXBvc3RncmVzXG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPSR7REJfUEFTU1dPUkR9XG4gICAgICAtIFBPU1RHUkVTX0RCPWF1dGhvcml6ZXJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYl9kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuXG4gIGF1dGhvcml6ZXItcmVkaXM6XG4gICAgaW1hZ2U6IHJlZGlzOjctYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSByZWRpc19kYXRhOi9kYXRhXG5cbnZvbHVtZXM6XG4gIGRiX2RhdGE6IHt9XG4gIHJlZGlzX2RhdGE6IHt9ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5kYl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoxNn1cIlxuYWRtaW5fc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5qd3Rfc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhdXRob3JpemVyXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuREJfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcbkFETUlOX1NFQ1JFVCA9IFwiJHthZG1pbl9zZWNyZXR9XCJcbkpXVF9TRUNSRVQgPSBcIiR7and0X3NlY3JldH1cIiAiCn0=
```

## Links

`authentication`,`authorization`,`security`

---

Version:`1.4.4`

AuthentikAuthentik is an open-source Identity Provider for authentication and authorization. It provides a comprehensive solution for managing user authentication, authorization, and identity federation with support for SAML, OAuth2, OIDC, and more.

AutobaseAutobase for PostgreSQL® is an open-source alternative to cloud-managed databases (self-hosted DBaaS).

### On this page

ConfigurationBase64LinksTags