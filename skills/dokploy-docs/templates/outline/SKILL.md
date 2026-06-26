---
title: "Outline | Dokploy"
source: "https://docs.dokploy.com/docs/templates/outline"
category: dokploy-docs
created: "2026-06-25T17:21:55.476Z"
---

Outline | Dokploy

# Outline

Copy as Markdown

Outline is a self-hosted knowledge base and documentation platform that allows you to build and manage your own knowledge base applications.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  outline:
    image: outlinewiki/outline:0.82.0
    restart: always
    depends_on:
      - postgres
      - redis
      - dex
    ports:
      - 3000
    environment:
      NODE_ENV: production
      URL: ${URL}
      FORCE_HTTPS: 'false'
      SECRET_KEY: ${SECRET_KEY}
      UTILS_SECRET: ${UTILS_SECRET}
      DATABASE_URL: postgres://outline:${POSTGRES_PASSWORD}@postgres:5432/outline
      PGSSLMODE: disable
      REDIS_URL: redis://redis:6379
      OIDC_CLIENT_ID: outline
      OIDC_CLIENT_SECRET: ${CLIENT_SECRET}
      OIDC_AUTH_URI: ${DEX_URL}/auth
      OIDC_TOKEN_URI: ${DEX_URL}/token
      OIDC_USERINFO_URI: ${DEX_URL}/userinfo

  dex:
    image: ghcr.io/dexidp/dex:v2.37.0
    restart: always
    volumes:
      - ../files/etc/dex/config.yaml:/etc/dex/config.yaml
    command:
      - dex
      - serve
      - /etc/dex/config.yaml
    ports:
      - 5556

  postgres:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_DB: outline
      POSTGRES_USER: outline
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data-test-outline-khufpx:/var/lib/postgresql/data

  redis:
    image: redis:latest
    restart: always
    command: redis-server --appendonly yes
    volumes:
      - redis_data-test-outline-khufpx:/data

volumes:
  postgres_data-test-outline-khufpx:
  redis_data-test-outline-khufpx:
```

```
[variables]
main_domain = "${domain}"
dex_domain = "${domain}"
secret_key = "${hash:64}"
utils_secret = "${base64:32}"
client_secret = "${base64:32}"
postgres_password = "${password}"

[[config.domains]]
serviceName = "outline"
port = 3_000
host = "${main_domain}"

[[config.domains]]
serviceName = "dex"
port = 5_556
host = "${dex_domain}"

[config.env]
URL = "http://${main_domain}"
DEX_URL = "http://${dex_domain}"
DOMAIN_NAME = "${main_domain}"
POSTGRES_PASSWORD = "${postgres_password}"
SECRET_KEY = "${secret_key}"
UTILS_SECRET = "${utils_secret}"
CLIENT_SECRET = "${client_secret}"

[[config.mounts]]
filePath = "/etc/dex/config.yaml"
content = """
issuer: http://${dex_domain}

web:
  http: 0.0.0.0:5556

storage:
  type: memory

enablePasswordDB: true

frontend:
   issuer: Outline

logger:
  level: debug

staticPasswords:
  - email: "[email protected]"
    # bcrypt hash of the string "password": $(echo password | htpasswd -BinC 10 admin | cut -d: -f2)
    hash: "$2y$10$jsRWHw54uxTUIfhjgUrB9u8HSzPk7TUuQri9sXZrKzRXcScvwYor."
    username: "admin"
    userID: "1"

oauth2:
  skipApprovalScreen: true
  alwaysShowLoginScreen: false
  passwordConnector: local

staticClients:
  - id: "outline"
    redirectURIs:
      - http://${main_domain}/auth/oidc.callback
    name: "Outline"
    secret: "${client_secret}"
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBvdXRsaW5lOlxuICAgIGltYWdlOiBvdXRsaW5ld2lraS9vdXRsaW5lOjAuODIuMFxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHBvc3RncmVzXG4gICAgICAtIHJlZGlzXG4gICAgICAtIGRleFxuICAgIHBvcnRzOlxuICAgICAgLSAzMDAwXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBOT0RFX0VOVjogcHJvZHVjdGlvblxuICAgICAgVVJMOiAke1VSTH1cbiAgICAgIEZPUkNFX0hUVFBTOiAnZmFsc2UnXG4gICAgICBTRUNSRVRfS0VZOiAke1NFQ1JFVF9LRVl9XG4gICAgICBVVElMU19TRUNSRVQ6ICR7VVRJTFNfU0VDUkVUfVxuICAgICAgREFUQUJBU0VfVVJMOiBwb3N0Z3JlczovL291dGxpbmU6JHtQT1NUR1JFU19QQVNTV09SRH1AcG9zdGdyZXM6NTQzMi9vdXRsaW5lXG4gICAgICBQR1NTTE1PREU6IGRpc2FibGVcbiAgICAgIFJFRElTX1VSTDogcmVkaXM6Ly9yZWRpczo2Mzc5XG4gICAgICBPSURDX0NMSUVOVF9JRDogb3V0bGluZVxuICAgICAgT0lEQ19DTElFTlRfU0VDUkVUOiAke0NMSUVOVF9TRUNSRVR9XG4gICAgICBPSURDX0FVVEhfVVJJOiAke0RFWF9VUkx9L2F1dGhcbiAgICAgIE9JRENfVE9LRU5fVVJJOiAke0RFWF9VUkx9L3Rva2VuXG4gICAgICBPSURDX1VTRVJJTkZPX1VSSTogJHtERVhfVVJMfS91c2VyaW5mb1xuXG4gIGRleDpcbiAgICBpbWFnZTogZ2hjci5pby9kZXhpZHAvZGV4OnYyLjM3LjBcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9ldGMvZGV4L2NvbmZpZy55YW1sOi9ldGMvZGV4L2NvbmZpZy55YW1sXG4gICAgY29tbWFuZDpcbiAgICAgIC0gZGV4XG4gICAgICAtIHNlcnZlXG4gICAgICAtIC9ldGMvZGV4L2NvbmZpZy55YW1sXG4gICAgcG9ydHM6XG4gICAgICAtIDU1NTZcblxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTX0RCOiBvdXRsaW5lXG4gICAgICBQT1NUR1JFU19VU0VSOiBvdXRsaW5lXG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlc19kYXRhLXRlc3Qtb3V0bGluZS1raHVmcHg6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG5cbiAgcmVkaXM6XG4gICAgaW1hZ2U6IHJlZGlzOmxhdGVzdFxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGNvbW1hbmQ6IHJlZGlzLXNlcnZlciAtLWFwcGVuZG9ubHkgeWVzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcmVkaXNfZGF0YS10ZXN0LW91dGxpbmUta2h1ZnB4Oi9kYXRhXG4gICAgXG52b2x1bWVzOlxuICBwb3N0Z3Jlc19kYXRhLXRlc3Qtb3V0bGluZS1raHVmcHg6XG4gIHJlZGlzX2RhdGEtdGVzdC1vdXRsaW5lLWtodWZweDoiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGV4X2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnNlY3JldF9rZXkgPSBcIiR7aGFzaDo2NH1cIlxudXRpbHNfc2VjcmV0ID0gXCIke2Jhc2U2NDozMn1cIlxuY2xpZW50X3NlY3JldCA9IFwiJHtiYXNlNjQ6MzJ9XCJcbnBvc3RncmVzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkfVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIm91dGxpbmVcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImRleFwiXG5wb3J0ID0gNV81NTZcbmhvc3QgPSBcIiR7ZGV4X2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblVSTCA9IFwiaHR0cDovLyR7bWFpbl9kb21haW59XCJcbkRFWF9VUkwgPSBcImh0dHA6Ly8ke2RleF9kb21haW59XCJcbkRPTUFJTl9OQU1FID0gXCIke21haW5fZG9tYWlufVwiXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtwb3N0Z3Jlc19wYXNzd29yZH1cIlxuU0VDUkVUX0tFWSA9IFwiJHtzZWNyZXRfa2V5fVwiXG5VVElMU19TRUNSRVQgPSBcIiR7dXRpbHNfc2VjcmV0fVwiXG5DTElFTlRfU0VDUkVUID0gXCIke2NsaWVudF9zZWNyZXR9XCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvZXRjL2RleC9jb25maWcueWFtbFwiXG5jb250ZW50ID0gXCJcIlwiXG5pc3N1ZXI6IGh0dHA6Ly8ke2RleF9kb21haW59XG5cbndlYjpcbiAgaHR0cDogMC4wLjAuMDo1NTU2XG5cbnN0b3JhZ2U6XG4gIHR5cGU6IG1lbW9yeVxuXG5lbmFibGVQYXNzd29yZERCOiB0cnVlXG5cbmZyb250ZW5kOlxuICAgaXNzdWVyOiBPdXRsaW5lXG5cbmxvZ2dlcjpcbiAgbGV2ZWw6IGRlYnVnXG5cbnN0YXRpY1Bhc3N3b3JkczpcbiAgLSBlbWFpbDogXCJhZG1pbkBleGFtcGxlLmNvbVwiXG4gICAgIyBiY3J5cHQgaGFzaCBvZiB0aGUgc3RyaW5nIFwicGFzc3dvcmRcIjogJChlY2hvIHBhc3N3b3JkIHwgaHRwYXNzd2QgLUJpbkMgMTAgYWRtaW4gfCBjdXQgLWQ6IC1mMilcbiAgICBoYXNoOiBcIiQyeSQxMCRqc1JXSHc1NHV4VFVJZmhqZ1VyQjl1OEhTelBrN1RVdVFyaTlzWFpyS3pSWGNTY3Z3WW9yLlwiXG4gICAgdXNlcm5hbWU6IFwiYWRtaW5cIlxuICAgIHVzZXJJRDogXCIxXCJcblxuXG5vYXV0aDI6XG4gIHNraXBBcHByb3ZhbFNjcmVlbjogdHJ1ZVxuICBhbHdheXNTaG93TG9naW5TY3JlZW46IGZhbHNlXG4gIHBhc3N3b3JkQ29ubmVjdG9yOiBsb2NhbFxuXG5zdGF0aWNDbGllbnRzOlxuICAtIGlkOiBcIm91dGxpbmVcIlxuICAgIHJlZGlyZWN0VVJJczpcbiAgICAgIC0gaHR0cDovLyR7bWFpbl9kb21haW59L2F1dGgvb2lkYy5jYWxsYmFja1xuICAgIG5hbWU6IFwiT3V0bGluZVwiXG4gICAgc2VjcmV0OiBcIiR7Y2xpZW50X3NlY3JldH1cIiBcblwiXCJcIlxuIgp9
```

## Links

`documentation`,`knowledge-base`,`self-hosted`

---

Version:`0.82.0`

Otter WikiAn Otter Wiki is a simple, lightweight, and fast wiki engine built with Python and Flask. It provides a user-friendly interface for creating and managing wiki content with markdown support.

OwncastOwncast is a self-hosted live video streaming and chat server for use with existing broadcasting software.

### On this page

ConfigurationBase64LinksTags