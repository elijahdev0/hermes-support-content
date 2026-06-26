---
title: "Stack Auth | Dokploy"
source: "https://docs.dokploy.com/docs/templates/stack-auth"
category: dokploy-docs
created: "2026-06-25T17:21:59.114Z"
---

Stack Auth | Dokploy

# Stack Auth

Copy as Markdown

Open-source Auth0/Clerk alternative. Stack Auth is a free and open source authentication tool that allows you to authenticate your users.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  stack-auth-db:
    image: postgres:17
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
    volumes:
      - stack-auth-db-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready", "-d", "db_prod"]
      interval: 10s
      timeout: 60s
      retries: 5
      start_period: 80s

  stack-auth:
    image: stackauth/server:latest
    container_name: stack-auth
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
      - NEXT_PUBLIC_STACK_API_URL=${NEXT_PUBLIC_STACK_API_URL}
      - NEXT_PUBLIC_STACK_DASHBOARD_URL=${NEXT_PUBLIC_STACK_DASHBOARD_URL}
      - STACK_DATABASE_CONNECTION_STRING=${STACK_DATABASE_CONNECTION_STRING}
      - STACK_DIRECT_DATABASE_CONNECTION_STRING=${STACK_DIRECT_DATABASE_CONNECTION_STRING}
      - STACK_SERVER_SECRET=${STACK_SERVER_SECRET}
      - STACK_SEED_INTERNAL_PROJECT_ALLOW_LOCALHOST=${STACK_SEED_INTERNAL_PROJECT_ALLOW_LOCALHOST}
      - STACK_SEED_INTERNAL_PROJECT_SIGN_UP_ENABLED=${STACK_SEED_INTERNAL_PROJECT_SIGN_UP_ENABLED}
      - STACK_RUN_MIGRATIONS=${STACK_RUN_MIGRATIONS}
      - STACK_RUN_SEED_SCRIPT=${STACK_RUN_SEED_SCRIPT}
      - STACK_EMAIL_HOST=${STACK_EMAIL_HOST}
    depends_on:
      stack-auth-db:
        condition: service_healthy

volumes:
  stack-auth-db-data:
```

```
[variables]
dashboard_domain = "${domain}"
api_domain = "${domain}"
postgres_password = "${password:32}"
stack_auth_api_url = "${api_domain}"
stack_auth_dashboard_url = "${dashboard_domain}"
stack_auth_postgres_host = "stack-auth-db"

[config.env]
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "${postgres_password}"
POSTGRES_DB = "stackframe"
NEXT_PUBLIC_STACK_API_URL = "http://${stack_auth_api_url}"
NEXT_PUBLIC_STACK_DASHBOARD_URL = "http://${stack_auth_dashboard_url}"

STACK_DATABASE_CONNECTION_STRING = "postgres://postgres:${postgres_password}@${stack_auth_postgres_host}/stackframe"
STACK_DIRECT_DATABASE_CONNECTION_STRING = "postgres://postgres:${postgres_password}@${stack_auth_postgres_host}/stackframe"

STACK_SERVER_SECRET = "${password:64}"
STACK_SEED_INTERNAL_PROJECT_ALLOW_LOCALHOST = true
STACK_SEED_INTERNAL_PROJECT_SIGN_UP_ENABLED = true

STACK_RUN_MIGRATIONS = true
STACK_RUN_SEED_SCRIPT = true

[[config.domains]]
serviceName = "stack-auth"
port = 8102
host = "${stack_auth_api_url}"
path = "/"

[[config.domains]]
serviceName = "stack-auth"
port = 8101
host = "${stack_auth_dashboard_url}"
path = "/"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBzdGFjay1hdXRoLWRiOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxN1xuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19VU0VSPSR7UE9TVEdSRVNfVVNFUn1cbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkQ9JHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIC0gUE9TVEdSRVNfREI9JHtQT1NUR1JFU19EQn1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBzdGFjay1hdXRoLWRiLWRhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5XCIsIFwiLWRcIiwgXCJkYl9wcm9kXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA2MHNcbiAgICAgIHJldHJpZXM6IDVcbiAgICAgIHN0YXJ0X3BlcmlvZDogODBzXG4gICAgICBcbiAgc3RhY2stYXV0aDpcbiAgICBpbWFnZTogc3RhY2thdXRoL3NlcnZlcjpsYXRlc3RcbiAgICBjb250YWluZXJfbmFtZTogc3RhY2stYXV0aFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19VU0VSPSR7UE9TVEdSRVNfVVNFUn1cbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkQ9JHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIC0gUE9TVEdSRVNfREI9JHtQT1NUR1JFU19EQn1cbiAgICAgIC0gTkVYVF9QVUJMSUNfU1RBQ0tfQVBJX1VSTD0ke05FWFRfUFVCTElDX1NUQUNLX0FQSV9VUkx9XG4gICAgICAtIE5FWFRfUFVCTElDX1NUQUNLX0RBU0hCT0FSRF9VUkw9JHtORVhUX1BVQkxJQ19TVEFDS19EQVNIQk9BUkRfVVJMfVxuICAgICAgLSBTVEFDS19EQVRBQkFTRV9DT05ORUNUSU9OX1NUUklORz0ke1NUQUNLX0RBVEFCQVNFX0NPTk5FQ1RJT05fU1RSSU5HfVxuICAgICAgLSBTVEFDS19ESVJFQ1RfREFUQUJBU0VfQ09OTkVDVElPTl9TVFJJTkc9JHtTVEFDS19ESVJFQ1RfREFUQUJBU0VfQ09OTkVDVElPTl9TVFJJTkd9XG4gICAgICAtIFNUQUNLX1NFUlZFUl9TRUNSRVQ9JHtTVEFDS19TRVJWRVJfU0VDUkVUfVxuICAgICAgLSBTVEFDS19TRUVEX0lOVEVSTkFMX1BST0pFQ1RfQUxMT1dfTE9DQUxIT1NUPSR7U1RBQ0tfU0VFRF9JTlRFUk5BTF9QUk9KRUNUX0FMTE9XX0xPQ0FMSE9TVH1cbiAgICAgIC0gU1RBQ0tfU0VFRF9JTlRFUk5BTF9QUk9KRUNUX1NJR05fVVBfRU5BQkxFRD0ke1NUQUNLX1NFRURfSU5URVJOQUxfUFJPSkVDVF9TSUdOX1VQX0VOQUJMRUR9XG4gICAgICAtIFNUQUNLX1JVTl9NSUdSQVRJT05TPSR7U1RBQ0tfUlVOX01JR1JBVElPTlN9XG4gICAgICAtIFNUQUNLX1JVTl9TRUVEX1NDUklQVD0ke1NUQUNLX1JVTl9TRUVEX1NDUklQVH1cbiAgICAgIC0gU1RBQ0tfRU1BSUxfSE9TVD0ke1NUQUNLX0VNQUlMX0hPU1R9XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHN0YWNrLWF1dGgtZGI6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG5cbiAgICBcbnZvbHVtZXM6XG4gIHN0YWNrLWF1dGgtZGItZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxuZGFzaGJvYXJkX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmFwaV9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuc3RhY2tfYXV0aF9hcGlfdXJsID0gXCIke2FwaV9kb21haW59XCJcbnN0YWNrX2F1dGhfZGFzaGJvYXJkX3VybCA9IFwiJHtkYXNoYm9hcmRfZG9tYWlufVwiXG5zdGFja19hdXRoX3Bvc3RncmVzX2hvc3QgPSBcInN0YWNrLWF1dGgtZGJcIlxuXG5bY29uZmlnLmVudl1cblBPU1RHUkVTX1VTRVIgPSBcInBvc3RncmVzXCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bvc3RncmVzX3Bhc3N3b3JkfVwiXG5QT1NUR1JFU19EQiA9IFwic3RhY2tmcmFtZVwiXG5ORVhUX1BVQkxJQ19TVEFDS19BUElfVVJMID0gXCJodHRwOi8vJHtzdGFja19hdXRoX2FwaV91cmx9XCJcbk5FWFRfUFVCTElDX1NUQUNLX0RBU0hCT0FSRF9VUkwgPSBcImh0dHA6Ly8ke3N0YWNrX2F1dGhfZGFzaGJvYXJkX3VybH1cIlxuXG5TVEFDS19EQVRBQkFTRV9DT05ORUNUSU9OX1NUUklORyA9IFwicG9zdGdyZXM6Ly9wb3N0Z3Jlczoke3Bvc3RncmVzX3Bhc3N3b3JkfUAke3N0YWNrX2F1dGhfcG9zdGdyZXNfaG9zdH0vc3RhY2tmcmFtZVwiXG5TVEFDS19ESVJFQ1RfREFUQUJBU0VfQ09OTkVDVElPTl9TVFJJTkcgPSBcInBvc3RncmVzOi8vcG9zdGdyZXM6JHtwb3N0Z3Jlc19wYXNzd29yZH1AJHtzdGFja19hdXRoX3Bvc3RncmVzX2hvc3R9L3N0YWNrZnJhbWVcIlxuXG5TVEFDS19TRVJWRVJfU0VDUkVUID0gXCIke3Bhc3N3b3JkOjY0fVwiICBcblNUQUNLX1NFRURfSU5URVJOQUxfUFJPSkVDVF9BTExPV19MT0NBTEhPU1QgPSB0cnVlXG5TVEFDS19TRUVEX0lOVEVSTkFMX1BST0pFQ1RfU0lHTl9VUF9FTkFCTEVEID0gdHJ1ZVxuXG5TVEFDS19SVU5fTUlHUkFUSU9OUyA9IHRydWVcblNUQUNLX1JVTl9TRUVEX1NDUklQVCA9IHRydWVcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwic3RhY2stYXV0aFwiXG5wb3J0ID0gODEwMlxuaG9zdCA9IFwiJHtzdGFja19hdXRoX2FwaV91cmx9XCJcbnBhdGggPSBcIi9cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJzdGFjay1hdXRoXCJcbnBvcnQgPSA4MTAxXG5ob3N0ID0gXCIke3N0YWNrX2F1dGhfZGFzaGJvYXJkX3VybH1cIlxucGF0aCA9IFwiL1wiXG4iCn0=
```

## Links

`authentication`,`auth`,`authorization`

---

Version:`latest`

SpacedriveSpacedrive is a cross-platform file manager. It connects your devices together to help you organize files from anywhere. powered by a virtual distributed filesystem (VDFS) written in Rust. Organize files across many devices in one place.

StalwartStalwart Mail Server is an open-source mail server solution with JMAP, IMAP4, POP3, and SMTP support and a wide range of modern features. It is written in Rust and designed to be secure, fast, robust and scalable.

### On this page

ConfigurationBase64LinksTags