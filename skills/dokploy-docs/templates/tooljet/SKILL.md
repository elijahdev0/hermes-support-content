---
title: "Tooljet | Dokploy"
source: "https://docs.dokploy.com/docs/templates/tooljet"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

Tooljet | Dokploy

# Tooljet

Copy as Markdown

Tooljet is an open-source low-code platform that allows you to build internal tools quickly and efficiently. It provides a user-friendly interface for creating applications without extensive coding knowledge.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  tooljet:
    tty: true
    stdin_open: true
    image: tooljet/tooljet:ee-lts-latest
    restart: always
    env_file: .env
    # ports:
    #   - 80:80
    expose:
      - 80
    deploy: # Please adjust the resource according to your usecase
      resources:
        limits:
          cpus: '1'
          memory: 2G
    depends_on:
      - postgres
    environment:
      SERVE_CLIENT: "true"
      PORT: "80"
    command: npm run start:prod

  postgres:
    image: postgres:13
    restart: always
    deploy: # Please adjust the resource according to your usecase
      resources:
        limits:
          cpus: '2'
          memory: 3G
    volumes:
      - ../files/postgres:/var/lib/postgresql/data
    env_file: .env
    environment:
      - POSTGRES_USER=${PG_USER}
      - POSTGRES_PASSWORD=${PG_PASS}

volumes:
  certs:
  logs:
  fallbackcerts:
```

```
[variables]
main_domain = "${domain}"
pg_pass = "${password}"

[config]
mounts = []

env = [
"# Create .env from this example file and replace values for the environment.",
"# The application expects a separate .env.test for test environment configuration",
"# Get detailed information about each variable here: https://docs.tooljet.com/docs/setup/env-vars",
"",
"TOOLJET_HOST=http://${main_domain}:80",
"TOOLJET_HTTP_PROXY=http://${main_domain}:80",
"LOCKBOX_MASTER_KEY=${password:32}",
"SECRET_KEY_BASE=${password:64}",
"",
"# DATABASE CONFIG",
"ORM_LOGGING=all",
"PG_DB=tooljet_production",
"PG_USER=postgres",
"PG_HOST=postgres",
"PG_PASS=${pg_pass}",
"",
"# The above postgres values is set to its default state. If necessary, kindly modify it according to your personal preference.",
"",
"# TOOLJET DATABASE",
"TOOLJET_DB=tooljet_db",
"TOOLJET_DB_USER=postgres",
"TOOLJET_DB_HOST=postgres",
"TOOLJET_DB_PASS=${pg_pass}",
"",
"PGRST_DB_URI=postgres://postgres:${pg_pass}@postgres/tooljet_db",
"PGRST_HOST=localhost:3002",
"PGRST_JWT_SECRET=${password:32}",
"PGRST_SERVER_PORT=3002",
"",
"# Redis",
"REDIS_HOST=localhost",
"REDIS_PORT=6379",
"REDIS_USER=default",
"REDIS_PASSWORD=",
"",
"# Checks every 24 hours to see if a new version of ToolJet is available",
"# (Enabled by default. Set false to disable)",
"CHECK_FOR_UPDATES=true",
"",
"# Checks every 24 hours to update app telemetry data to ToolJet hub.",
"# (Telemetry is enabled by default. Set value to true to disable.)",
"DISABLE_TOOLJET_TELEMETRY=true",
"",
"GOOGLE_CLIENT_ID=",
"GOOGLE_CLIENT_SECRET=",
"",
"# EMAIL CONFIGURATION",
"[email protected]",
"SMTP_USERNAME=",
"SMTP_PASSWORD=",
"SMTP_DOMAIN=",
"SMTP_PORT=",
"",
"# DISABLE USER SIGNUPS (true or false). only applicable if Multi-Workspace feature is enabled",
"DISABLE_SIGNUPS=",
"",
"# OBSERVABILITY",
"APM_VENDOR=",
"SENTRY_DNS=",
"SENTRY_DEBUG=",
"",
"# FEATURE TOGGLE",
"COMMENT_FEATURE_ENABLE=",
"ENABLE_MULTIPLAYER_EDITING=true",
"ENABLE_MARKETPLACE_FEATURE=true",
"",
"# SSO (Applicable only for Multi-Workspace)",
"SSO_GOOGLE_OAUTH2_CLIENT_ID=",
"SSO_GIT_OAUTH2_CLIENT_ID=",
"SSO_GIT_OAUTH2_CLIENT_SECRET=",
"SSO_GIT_OAUTH2_HOST=",
"SSO_ACCEPTED_DOMAINS=",
"SSO_DISABLE_SIGNUPS=",
"",
"#ONBOARDING",
"ENABLE_ONBOARDING_QUESTIONS_FOR_ALL_SIGN_UPS=",
"",
"#session expiry in minutes",
"USER_SESSION_EXPIRY=2880",
"",
"#TELEMETRY",
"DEPLOYMENT_PLATFORM=docker"
]

[[config.domains]]
serviceName = "tooljet"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICB0b29samV0OlxuICAgIHR0eTogdHJ1ZVxuICAgIHN0ZGluX29wZW46IHRydWVcbiAgICBpbWFnZTogdG9vbGpldC90b29samV0OmVlLWx0cy1sYXRlc3RcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZfZmlsZTogLmVudlxuICAgICMgcG9ydHM6XG4gICAgIyAgIC0gODA6ODBcbiAgICBleHBvc2U6XG4gICAgICAtIDgwXG4gICAgZGVwbG95OiAjIFBsZWFzZSBhZGp1c3QgdGhlIHJlc291cmNlIGFjY29yZGluZyB0byB5b3VyIHVzZWNhc2VcbiAgICAgIHJlc291cmNlczpcbiAgICAgICAgbGltaXRzOlxuICAgICAgICAgIGNwdXM6ICcxJ1xuICAgICAgICAgIG1lbW9yeTogMkdcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBwb3N0Z3Jlc1xuICAgIGVudmlyb25tZW50OlxuICAgICAgU0VSVkVfQ0xJRU5UOiBcInRydWVcIlxuICAgICAgUE9SVDogXCI4MFwiXG4gICAgY29tbWFuZDogbnBtIHJ1biBzdGFydDpwcm9kXG5cbiAgcG9zdGdyZXM6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjEzXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZGVwbG95OiAjIFBsZWFzZSBhZGp1c3QgdGhlIHJlc291cmNlIGFjY29yZGluZyB0byB5b3VyIHVzZWNhc2VcbiAgICAgIHJlc291cmNlczpcbiAgICAgICAgbGltaXRzOlxuICAgICAgICAgIGNwdXM6ICcyJ1xuICAgICAgICAgIG1lbW9yeTogM0dcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9wb3N0Z3JlczovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBlbnZfZmlsZTogLmVudlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19VU0VSPSR7UEdfVVNFUn1cbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkQ9JHtQR19QQVNTfVxuXG52b2x1bWVzOlxuICBjZXJ0czpcbiAgbG9nczpcbiAgZmFsbGJhY2tjZXJ0czoiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucGdfcGFzcyA9IFwiJHtwYXNzd29yZH1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuZW52ID0gW1xuXCIjIENyZWF0ZSAuZW52IGZyb20gdGhpcyBleGFtcGxlIGZpbGUgYW5kIHJlcGxhY2UgdmFsdWVzIGZvciB0aGUgZW52aXJvbm1lbnQuXCIsXG5cIiMgVGhlIGFwcGxpY2F0aW9uIGV4cGVjdHMgYSBzZXBhcmF0ZSAuZW52LnRlc3QgZm9yIHRlc3QgZW52aXJvbm1lbnQgY29uZmlndXJhdGlvblwiLFxuXCIjIEdldCBkZXRhaWxlZCBpbmZvcm1hdGlvbiBhYm91dCBlYWNoIHZhcmlhYmxlIGhlcmU6IGh0dHBzOi8vZG9jcy50b29samV0LmNvbS9kb2NzL3NldHVwL2Vudi12YXJzXCIsXG5cIlwiLFxuXCJUT09MSkVUX0hPU1Q9aHR0cDovLyR7bWFpbl9kb21haW59OjgwXCIsXG5cIlRPT0xKRVRfSFRUUF9QUk9YWT1odHRwOi8vJHttYWluX2RvbWFpbn06ODBcIixcblwiTE9DS0JPWF9NQVNURVJfS0VZPSR7cGFzc3dvcmQ6MzJ9XCIsXG5cIlNFQ1JFVF9LRVlfQkFTRT0ke3Bhc3N3b3JkOjY0fVwiLFxuXCJcIixcblwiIyBEQVRBQkFTRSBDT05GSUdcIixcblwiT1JNX0xPR0dJTkc9YWxsXCIsXG5cIlBHX0RCPXRvb2xqZXRfcHJvZHVjdGlvblwiLFxuXCJQR19VU0VSPXBvc3RncmVzXCIsXG5cIlBHX0hPU1Q9cG9zdGdyZXNcIixcblwiUEdfUEFTUz0ke3BnX3Bhc3N9XCIsXG5cIlwiLFxuXCIjIFRoZSBhYm92ZSBwb3N0Z3JlcyB2YWx1ZXMgaXMgc2V0IHRvIGl0cyBkZWZhdWx0IHN0YXRlLiBJZiBuZWNlc3NhcnksIGtpbmRseSBtb2RpZnkgaXQgYWNjb3JkaW5nIHRvIHlvdXIgcGVyc29uYWwgcHJlZmVyZW5jZS5cIixcblwiXCIsXG5cIiMgVE9PTEpFVCBEQVRBQkFTRVwiLFxuXCJUT09MSkVUX0RCPXRvb2xqZXRfZGJcIixcblwiVE9PTEpFVF9EQl9VU0VSPXBvc3RncmVzXCIsXG5cIlRPT0xKRVRfREJfSE9TVD1wb3N0Z3Jlc1wiLFxuXCJUT09MSkVUX0RCX1BBU1M9JHtwZ19wYXNzfVwiLFxuXCJcIixcblwiUEdSU1RfREJfVVJJPXBvc3RncmVzOi8vcG9zdGdyZXM6JHtwZ19wYXNzfUBwb3N0Z3Jlcy90b29samV0X2RiXCIsXG5cIlBHUlNUX0hPU1Q9bG9jYWxob3N0OjMwMDJcIixcblwiUEdSU1RfSldUX1NFQ1JFVD0ke3Bhc3N3b3JkOjMyfVwiLFxuXCJQR1JTVF9TRVJWRVJfUE9SVD0zMDAyXCIsXG5cIlwiLFxuXCIjIFJlZGlzXCIsXG5cIlJFRElTX0hPU1Q9bG9jYWxob3N0XCIsXG5cIlJFRElTX1BPUlQ9NjM3OVwiLFxuXCJSRURJU19VU0VSPWRlZmF1bHRcIixcblwiUkVESVNfUEFTU1dPUkQ9XCIsXG5cIlwiLFxuXCIjIENoZWNrcyBldmVyeSAyNCBob3VycyB0byBzZWUgaWYgYSBuZXcgdmVyc2lvbiBvZiBUb29sSmV0IGlzIGF2YWlsYWJsZVwiLFxuXCIjIChFbmFibGVkIGJ5IGRlZmF1bHQuIFNldCBmYWxzZSB0byBkaXNhYmxlKVwiLFxuXCJDSEVDS19GT1JfVVBEQVRFUz10cnVlXCIsXG5cIlwiLFxuXCIjIENoZWNrcyBldmVyeSAyNCBob3VycyB0byB1cGRhdGUgYXBwIHRlbGVtZXRyeSBkYXRhIHRvIFRvb2xKZXQgaHViLlwiLFxuXCIjIChUZWxlbWV0cnkgaXMgZW5hYmxlZCBieSBkZWZhdWx0LiBTZXQgdmFsdWUgdG8gdHJ1ZSB0byBkaXNhYmxlLilcIixcblwiRElTQUJMRV9UT09MSkVUX1RFTEVNRVRSWT10cnVlXCIsXG5cIlwiLFxuXCJHT09HTEVfQ0xJRU5UX0lEPVwiLFxuXCJHT09HTEVfQ0xJRU5UX1NFQ1JFVD1cIixcblwiXCIsXG5cIiMgRU1BSUwgQ09ORklHVVJBVElPTlwiLFxuXCJERUZBVUxUX0ZST01fRU1BSUw9aGVsbG9AdG9vbGpldC5pb1wiLFxuXCJTTVRQX1VTRVJOQU1FPVwiLFxuXCJTTVRQX1BBU1NXT1JEPVwiLFxuXCJTTVRQX0RPTUFJTj1cIixcblwiU01UUF9QT1JUPVwiLFxuXCJcIixcblwiIyBESVNBQkxFIFVTRVIgU0lHTlVQUyAodHJ1ZSBvciBmYWxzZSkuIG9ubHkgYXBwbGljYWJsZSBpZiBNdWx0aS1Xb3Jrc3BhY2UgZmVhdHVyZSBpcyBlbmFibGVkXCIsXG5cIkRJU0FCTEVfU0lHTlVQUz1cIixcblwiXCIsXG5cIiMgT0JTRVJWQUJJTElUWVwiLFxuXCJBUE1fVkVORE9SPVwiLFxuXCJTRU5UUllfRE5TPVwiLFxuXCJTRU5UUllfREVCVUc9XCIsXG5cIlwiLFxuXCIjIEZFQVRVUkUgVE9HR0xFXCIsXG5cIkNPTU1FTlRfRkVBVFVSRV9FTkFCTEU9XCIsXG5cIkVOQUJMRV9NVUxUSVBMQVlFUl9FRElUSU5HPXRydWVcIixcblwiRU5BQkxFX01BUktFVFBMQUNFX0ZFQVRVUkU9dHJ1ZVwiLFxuXCJcIixcblwiIyBTU08gKEFwcGxpY2FibGUgb25seSBmb3IgTXVsdGktV29ya3NwYWNlKVwiLFxuXCJTU09fR09PR0xFX09BVVRIMl9DTElFTlRfSUQ9XCIsXG5cIlNTT19HSVRfT0FVVEgyX0NMSUVOVF9JRD1cIixcblwiU1NPX0dJVF9PQVVUSDJfQ0xJRU5UX1NFQ1JFVD1cIixcblwiU1NPX0dJVF9PQVVUSDJfSE9TVD1cIixcblwiU1NPX0FDQ0VQVEVEX0RPTUFJTlM9XCIsXG5cIlNTT19ESVNBQkxFX1NJR05VUFM9XCIsXG5cIlwiLFxuXCIjT05CT0FSRElOR1wiLFxuXCJFTkFCTEVfT05CT0FSRElOR19RVUVTVElPTlNfRk9SX0FMTF9TSUdOX1VQUz1cIixcblwiXCIsXG5cIiNzZXNzaW9uIGV4cGlyeSBpbiBtaW51dGVzXCIsXG5cIlVTRVJfU0VTU0lPTl9FWFBJUlk9Mjg4MFwiLFxuXCJcIixcblwiI1RFTEVNRVRSWVwiLFxuXCJERVBMT1lNRU5UX1BMQVRGT1JNPWRvY2tlclwiXG5dXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInRvb2xqZXRcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiIgp9
```

## Links

`file-sync`,`file-sharing`,`self-hosted`

---

Version:`ee-lts-latest`

TolgeeDeveloper & translator friendly web-based localization platform

Tor BrowserA Dockerized Tor Browser accessible via web VNC (noVNC) and VNC client.

### On this page

ConfigurationBase64LinksTags