---
title: "Keycloak | Dokploy"
source: "https://docs.dokploy.com/docs/templates/keycloak"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

Keycloak | Dokploy

# Keycloak

Copy as Markdown

Keycloak is an open source Identity and Access Management solution for modern applications and services.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  postgres:
    image: postgres:16.2
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: always

  keycloak:
    image: quay.io/keycloak/keycloak:26.3.5
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      KC_DB: postgres
      KC_DB_URL: jdbc:postgresql://postgres:5432/${POSTGRES_DB}
      KC_DB_USERNAME: ${POSTGRES_USER}
      KC_DB_PASSWORD: ${POSTGRES_PASSWORD}
      KC_BOOTSTRAP_ADMIN_USERNAME: ${KEYCLOAK_ADMIN}
      KC_BOOTSTRAP_ADMIN_PASSWORD: ${KEYCLOAK_ADMIN_PASSWORD}
      KC_HOSTNAME: ${KC_HOSTNAME}
      KC_HTTP_ENABLED: "true"
      KC_HEALTH_ENABLED: "true"
      KC_PROXY_HEADERS: "xforwarded"
    command: start-dev
    restart: always

volumes:
  postgres_data:
```

```
[variables]
main_domain = "${domain}"
POSTGRES_DB = "keycloak"
POSTGRES_USER = "keycloakuser"
POSTGRES_PASSWORD = "${password:32}"
KEYCLOAK_ADMIN = "admin"
KEYCLOAK_ADMIN_PASSWORD = "${password:32}"
KC_HOSTNAME = "${main_domain}"

[config]
[[config.domains]]
serviceName = "keycloak"
port = 8080
host = "${main_domain}"

[config.env]
POSTGRES_DB = "${POSTGRES_DB}"
POSTGRES_USER = "${POSTGRES_USER}"
POSTGRES_PASSWORD = "${POSTGRES_PASSWORD}"
KEYCLOAK_ADMIN = "${KEYCLOAK_ADMIN}"
KEYCLOAK_ADMIN_PASSWORD = "${KEYCLOAK_ADMIN_PASSWORD}"
KC_HOSTNAME = "${KC_HOSTNAME}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTYuMlxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6ICR7UE9TVEdSRVNfREJ9XG4gICAgICBQT1NUR1JFU19VU0VSOiAke1BPU1RHUkVTX1VTRVJ9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlc19kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSAkJFBPU1RHUkVTX1VTRVIgLWQgJCRQT1NUR1JFU19EQlwiXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBcbiAga2V5Y2xvYWs6XG4gICAgaW1hZ2U6IHF1YXkuaW8va2V5Y2xvYWsva2V5Y2xvYWs6MjYuMy41XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHBvc3RncmVzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGVudmlyb25tZW50OlxuICAgICAgS0NfREI6IHBvc3RncmVzXG4gICAgICBLQ19EQl9VUkw6IGpkYmM6cG9zdGdyZXNxbDovL3Bvc3RncmVzOjU0MzIvJHtQT1NUR1JFU19EQn1cbiAgICAgIEtDX0RCX1VTRVJOQU1FOiAke1BPU1RHUkVTX1VTRVJ9XG4gICAgICBLQ19EQl9QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIEtDX0JPT1RTVFJBUF9BRE1JTl9VU0VSTkFNRTogJHtLRVlDTE9BS19BRE1JTn1cbiAgICAgIEtDX0JPT1RTVFJBUF9BRE1JTl9QQVNTV09SRDogJHtLRVlDTE9BS19BRE1JTl9QQVNTV09SRH1cbiAgICAgIEtDX0hPU1ROQU1FOiAke0tDX0hPU1ROQU1FfSAgICAgIFxuICAgICAgS0NfSFRUUF9FTkFCTEVEOiBcInRydWVcIiAgICAgICAgICAgICAgIFxuICAgICAgS0NfSEVBTFRIX0VOQUJMRUQ6IFwidHJ1ZVwiXG4gICAgICBLQ19QUk9YWV9IRUFERVJTOiBcInhmb3J3YXJkZWRcIlxuICAgIGNvbW1hbmQ6IHN0YXJ0LWRldlxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuXG52b2x1bWVzOlxuICBwb3N0Z3Jlc19kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblBPU1RHUkVTX0RCID0gXCJrZXljbG9ha1wiXG5QT1NUR1JFU19VU0VSID0gXCJrZXljbG9ha3VzZXJcIlxuUE9TVEdSRVNfUEFTU1dPUkQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbktFWUNMT0FLX0FETUlOID0gXCJhZG1pblwiXG5LRVlDTE9BS19BRE1JTl9QQVNTV09SRCA9IFwiJHtwYXNzd29yZDozMn1cIlxuS0NfSE9TVE5BTUUgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImtleWNsb2FrXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuUE9TVEdSRVNfREIgPSBcIiR7UE9TVEdSRVNfREJ9XCJcblBPU1RHUkVTX1VTRVIgPSBcIiR7UE9TVEdSRVNfVVNFUn1cIlxuUE9TVEdSRVNfUEFTU1dPUkQgPSBcIiR7UE9TVEdSRVNfUEFTU1dPUkR9XCJcbktFWUNMT0FLX0FETUlOID0gXCIke0tFWUNMT0FLX0FETUlOfVwiXG5LRVlDTE9BS19BRE1JTl9QQVNTV09SRCA9IFwiJHtLRVlDTE9BS19BRE1JTl9QQVNTV09SRH1cIlxuS0NfSE9TVE5BTUUgPSBcIiR7S0NfSE9TVE5BTUV9XCJcblxuW1tjb25maWcubW91bnRzXV1cbiIKfQ==
```

## Links

`authentication`,`identity`,`sso`,`oauth2`,`openid-connect`

---

Version:`26.0`

KestraUnified Orchestration Platform to Simplify Business-Critical Workflows and Govern them as Code and from the UI.

KimaiKimai is a web-based multi-user time-tracking application. Works great for everyone: freelancers, companies, organizations - everyone can track their times, generate reports, create invoices and do so much more.

### On this page

ConfigurationBase64LinksTags