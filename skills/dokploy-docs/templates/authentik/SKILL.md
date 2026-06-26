---
title: "Authentik | Dokploy"
source: "https://docs.dokploy.com/docs/templates/authentik"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

Authentik | Dokploy

# Authentik

Copy as Markdown

Authentik is an open-source Identity Provider for authentication and authorization. It provides a comprehensive solution for managing user authentication, authorization, and identity federation with support for SAML, OAuth2, OIDC, and more.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  postgresql:
    image: docker.io/library/postgres:16-alpine
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -d $${POSTGRES_DB} -U $${POSTGRES_USER}"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 5s
    volumes:
      - database:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: ${PG_PASS}
      POSTGRES_USER: ${PG_USER}
      POSTGRES_DB: ${PG_DB}
    expose:
      - 5432

  redis:
    image: docker.io/library/redis:alpine
    command: --save 60 1 --loglevel warning
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "redis-cli ping | grep PONG"]
      start_period: 20s
      interval: 30s
      retries: 5
      timeout: 3s
    volumes:
      - redis:/data
    expose:
      - 6379

  server:
    image: ${AUTHENTIK_IMAGE:-ghcr.io/goauthentik/server}:${AUTHENTIK_TAG:-2025.6.3}
    restart: unless-stopped
    command: server
    environment:
      AUTHENTIK_SECRET_KEY: ${AUTHENTIK_SECRET_KEY}
      AUTHENTIK_REDIS__HOST: redis
      AUTHENTIK_POSTGRESQL__HOST: postgresql
      AUTHENTIK_POSTGRESQL__USER: ${PG_USER}
      AUTHENTIK_POSTGRESQL__NAME: ${PG_DB}
      AUTHENTIK_POSTGRESQL__PASSWORD: ${PG_PASS}
    volumes:
      - media:/media
      - custom-templates:/templates
    expose:
      - 9000
      - 9443
    depends_on:
      postgresql:
        condition: service_healthy
      redis:
        condition: service_healthy

  worker:
    image: ${AUTHENTIK_IMAGE:-ghcr.io/goauthentik/server}:${AUTHENTIK_TAG:-2025.6.3}
    restart: unless-stopped
    command: worker
    environment:
      AUTHENTIK_SECRET_KEY: ${AUTHENTIK_SECRET_KEY}
      AUTHENTIK_REDIS__HOST: redis
      AUTHENTIK_POSTGRESQL__HOST: postgresql
      AUTHENTIK_POSTGRESQL__USER: ${PG_USER}
      AUTHENTIK_POSTGRESQL__NAME: ${PG_DB}
      AUTHENTIK_POSTGRESQL__PASSWORD: ${PG_PASS}
    user: root
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - media:/media
      - certs:/certs
      - custom-templates:/templates
    depends_on:
      postgresql:
        condition: service_healthy
      redis:
        condition: service_healthy

volumes:
  database:
    driver: local
  redis:
    driver: local
  media:
    driver: local
  certs:
    driver: local
  custom-templates:
    driver: local
```

```
[variables]
main_domain = "${domain}"
main_domain_1 = "${domain}"
pg_user = "authentik"
pg_db = "authentik"

[config]
[[config.domains]]
serviceName = "server"
port = 9000
host = "${main_domain}"
path = "/"

[[config.domains]]
serviceName = "server"
port = 9443
host = "${main_domain_1}"
path = "/"

[config.env]
PG_USER = "${pg_user}"
PG_DB = "${pg_db}"
PG_PASS = "${password:32}" # Password for PostgreSQL authentication
AUTHENTIK_SECRET_KEY = "${password:64}" # Secret key for Authentik authentication
AUTHENTIK_IMAGE = "ghcr.io/goauthentik/server"
AUTHENTIK_TAG = "2025.6.3"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBwb3N0Z3Jlc3FsOlxuICAgIGltYWdlOiBkb2NrZXIuaW8vbGlicmFyeS9wb3N0Z3JlczoxNi1hbHBpbmVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtZCAkJHtQT1NUR1JFU19EQn0gLVUgJCR7UE9TVEdSRVNfVVNFUn1cIl1cbiAgICAgIHN0YXJ0X3BlcmlvZDogMjBzXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICB0aW1lb3V0OiA1c1xuICAgIHZvbHVtZXM6XG4gICAgICAtIGRhdGFiYXNlOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UEdfUEFTU31cbiAgICAgIFBPU1RHUkVTX1VTRVI6ICR7UEdfVVNFUn1cbiAgICAgIFBPU1RHUkVTX0RCOiAke1BHX0RCfVxuICAgIGV4cG9zZTpcbiAgICAgIC0gNTQzMlxuXG4gIHJlZGlzOlxuICAgIGltYWdlOiBkb2NrZXIuaW8vbGlicmFyeS9yZWRpczphbHBpbmVcbiAgICBjb21tYW5kOiAtLXNhdmUgNjAgMSAtLWxvZ2xldmVsIHdhcm5pbmdcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicmVkaXMtY2xpIHBpbmcgfCBncmVwIFBPTkdcIl1cbiAgICAgIHN0YXJ0X3BlcmlvZDogMjBzXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICB0aW1lb3V0OiAzc1xuICAgIHZvbHVtZXM6XG4gICAgICAtIHJlZGlzOi9kYXRhXG4gICAgZXhwb3NlOlxuICAgICAgLSA2Mzc5XG5cbiAgc2VydmVyOlxuICAgIGltYWdlOiAke0FVVEhFTlRJS19JTUFHRTotZ2hjci5pby9nb2F1dGhlbnRpay9zZXJ2ZXJ9OiR7QVVUSEVOVElLX1RBRzotMjAyNS42LjN9XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBjb21tYW5kOiBzZXJ2ZXJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEFVVEhFTlRJS19TRUNSRVRfS0VZOiAke0FVVEhFTlRJS19TRUNSRVRfS0VZfVxuICAgICAgQVVUSEVOVElLX1JFRElTX19IT1NUOiByZWRpc1xuICAgICAgQVVUSEVOVElLX1BPU1RHUkVTUUxfX0hPU1Q6IHBvc3RncmVzcWxcbiAgICAgIEFVVEhFTlRJS19QT1NUR1JFU1FMX19VU0VSOiAke1BHX1VTRVJ9XG4gICAgICBBVVRIRU5USUtfUE9TVEdSRVNRTF9fTkFNRTogJHtQR19EQn1cbiAgICAgIEFVVEhFTlRJS19QT1NUR1JFU1FMX19QQVNTV09SRDogJHtQR19QQVNTfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIG1lZGlhOi9tZWRpYVxuICAgICAgLSBjdXN0b20tdGVtcGxhdGVzOi90ZW1wbGF0ZXNcbiAgICBleHBvc2U6XG4gICAgICAtIDkwMDBcbiAgICAgIC0gOTQ0M1xuICAgIGRlcGVuZHNfb246XG4gICAgICBwb3N0Z3Jlc3FsOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgcmVkaXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG5cbiAgd29ya2VyOlxuICAgIGltYWdlOiAke0FVVEhFTlRJS19JTUFHRTotZ2hjci5pby9nb2F1dGhlbnRpay9zZXJ2ZXJ9OiR7QVVUSEVOVElLX1RBRzotMjAyNS42LjN9XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBjb21tYW5kOiB3b3JrZXJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEFVVEhFTlRJS19TRUNSRVRfS0VZOiAke0FVVEhFTlRJS19TRUNSRVRfS0VZfVxuICAgICAgQVVUSEVOVElLX1JFRElTX19IT1NUOiByZWRpc1xuICAgICAgQVVUSEVOVElLX1BPU1RHUkVTUUxfX0hPU1Q6IHBvc3RncmVzcWxcbiAgICAgIEFVVEhFTlRJS19QT1NUR1JFU1FMX19VU0VSOiAke1BHX1VTRVJ9XG4gICAgICBBVVRIRU5USUtfUE9TVEdSRVNRTF9fTkFNRTogJHtQR19EQn1cbiAgICAgIEFVVEhFTlRJS19QT1NUR1JFU1FMX19QQVNTV09SRDogJHtQR19QQVNTfVxuICAgIHVzZXI6IHJvb3RcbiAgICB2b2x1bWVzOlxuICAgICAgLSAvdmFyL3J1bi9kb2NrZXIuc29jazovdmFyL3J1bi9kb2NrZXIuc29ja1xuICAgICAgLSBtZWRpYTovbWVkaWFcbiAgICAgIC0gY2VydHM6L2NlcnRzXG4gICAgICAtIGN1c3RvbS10ZW1wbGF0ZXM6L3RlbXBsYXRlc1xuICAgIGRlcGVuZHNfb246XG4gICAgICBwb3N0Z3Jlc3FsOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgcmVkaXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG5cbnZvbHVtZXM6XG4gIGRhdGFiYXNlOlxuICAgIGRyaXZlcjogbG9jYWxcbiAgcmVkaXM6XG4gICAgZHJpdmVyOiBsb2NhbFxuICBtZWRpYTpcbiAgICBkcml2ZXI6IGxvY2FsXG4gIGNlcnRzOlxuICAgIGRyaXZlcjogbG9jYWxcbiAgY3VzdG9tLXRlbXBsYXRlczpcbiAgICBkcml2ZXI6IGxvY2FsXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxubWFpbl9kb21haW5fMSA9IFwiJHtkb21haW59XCJcbnBnX3VzZXIgPSBcImF1dGhlbnRpa1wiXG5wZ19kYiA9IFwiYXV0aGVudGlrXCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInNlcnZlclwiXG5wb3J0ID0gOTAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxucGF0aCA9IFwiL1wiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInNlcnZlclwiXG5wb3J0ID0gOTQ0M1xuaG9zdCA9IFwiJHttYWluX2RvbWFpbl8xfVwiXG5wYXRoID0gXCIvXCJcblxuW2NvbmZpZy5lbnZdXG5QR19VU0VSID0gXCIke3BnX3VzZXJ9XCJcblBHX0RCID0gXCIke3BnX2RifVwiXG5QR19QQVNTID0gXCIke3Bhc3N3b3JkOjMyfVwiICMgUGFzc3dvcmQgZm9yIFBvc3RncmVTUUwgYXV0aGVudGljYXRpb25cbkFVVEhFTlRJS19TRUNSRVRfS0VZID0gXCIke3Bhc3N3b3JkOjY0fVwiICMgU2VjcmV0IGtleSBmb3IgQXV0aGVudGlrIGF1dGhlbnRpY2F0aW9uXG5BVVRIRU5USUtfSU1BR0UgPSBcImdoY3IuaW8vZ29hdXRoZW50aWsvc2VydmVyXCJcbkFVVEhFTlRJS19UQUcgPSBcIjIwMjUuNi4zXCIiCn0=
```

## Links

`authentication`,`identity`,`sso`,`oidc`,`saml`,`oauth2`,`self-hosted`

---

Version:`2025.6.3`

AutheliaThe Single Sign-On Multi-Factor portal for web apps. An open-source authentication and authorization server providing 2FA and SSO via web portal.

AuthorizerAuthorizer is a powerful tool designed to simplify the process of user authentication and authorization in your applications. It allows you to build secure apps 10x faster with its low code tool and low-cost deployment.

### On this page

ConfigurationBase64LinksTags