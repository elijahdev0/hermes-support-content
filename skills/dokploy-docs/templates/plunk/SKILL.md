---
title: "Plunk | Dokploy"
source: "https://docs.dokploy.com/docs/templates/plunk"
category: dokploy-docs
created: "2026-06-25T17:21:56.647Z"
---

Plunk | Dokploy

# Plunk

Copy as Markdown

Plunk is the open-source, affordable email platform that brings together marketing, transactional and broadcast emails into one single, complete solution

## Configuration

docker-compose.ymltemplate.toml

```
# IMPORTANT: Plunk requires HTTPS to work properly
# go to the "Domains" tab and enable HTTPS for your domain

services:
  plunk:
    image: driaug/plunk
    expose:
      - "3000"
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    environment:
      REDIS_URL: ${REDIS_URL}
      DATABASE_URL: postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
      JWT_SECRET: ${JWT_SECRET}
      AWS_REGION: ${AWS_REGION}
      AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID}
      AWS_SECRET_ACCESS_KEY: ${AWS_SECRET_ACCESS_KEY}
      AWS_SES_CONFIGURATION_SET: ${AWS_SES_CONFIGURATION_SET}
      APP_URI: ${APP_URI}
      NEXT_PUBLIC_API_URI: ${APP_URI}/api
      API_URI: ${APP_URI}/api
      DISABLE_SIGNUPS: ${DISABLE_SIGNUPS}
    entrypoint: ["/app/entry.sh"]
    restart: unless-stopped

  db:
    image: postgres:alpine
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      retries: 5
      timeout: 10s
    restart: unless-stopped
    expose:
      - 5432

  redis:
    image: redis:alpine
    restart: unless-stopped
    expose:
      - 6379
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
```

```
[variables]
main_domain = "${domain}"
postgres_user = "plunk"
postgres_db = "plunk"

[config]
isolated = true

[[config.domains]]
serviceName = "plunk"
port = 3000
host = "${main_domain}"
path = "/"

[config.env]
POSTGRES_USER = "${postgres_user}"
POSTGRES_DB = "${postgres_db}"
POSTGRES_PASSWORD = "${password:32}"

REDIS_URL = "redis://redis:6379"

JWT_SECRET = "${password:64}"
APP_URI = "https://${main_domain}"

AWS_REGION = "<your-aws-region>"
AWS_ACCESS_KEY_ID = "<your-aws-access-key-id>"
AWS_SECRET_ACCESS_KEY = "<your-aws-secret-access-key>"
AWS_SES_CONFIGURATION_SET = "<your-ses-configuration-set>"

DISABLE_SIGNUPS = "False"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgSU1QT1JUQU5UOiBQbHVuayByZXF1aXJlcyBIVFRQUyB0byB3b3JrIHByb3Blcmx5XG4jIGdvIHRvIHRoZSBcIkRvbWFpbnNcIiB0YWIgYW5kIGVuYWJsZSBIVFRQUyBmb3IgeW91ciBkb21haW5cblxuc2VydmljZXM6XG4gIHBsdW5rOlxuICAgIGltYWdlOiBkcmlhdWcvcGx1bmtcbiAgICBleHBvc2U6XG4gICAgICAtIFwiMzAwMFwiXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGRiOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgcmVkaXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9zdGFydGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBSRURJU19VUkw6ICR7UkVESVNfVVJMfVxuICAgICAgREFUQUJBU0VfVVJMOiBwb3N0Z3Jlc3FsOi8vJHtQT1NUR1JFU19VU0VSfToke1BPU1RHUkVTX1BBU1NXT1JEfUBkYjo1NDMyLyR7UE9TVEdSRVNfREJ9XG4gICAgICBKV1RfU0VDUkVUOiAke0pXVF9TRUNSRVR9XG4gICAgICBBV1NfUkVHSU9OOiAke0FXU19SRUdJT059XG4gICAgICBBV1NfQUNDRVNTX0tFWV9JRDogJHtBV1NfQUNDRVNTX0tFWV9JRH1cbiAgICAgIEFXU19TRUNSRVRfQUNDRVNTX0tFWTogJHtBV1NfU0VDUkVUX0FDQ0VTU19LRVl9XG4gICAgICBBV1NfU0VTX0NPTkZJR1VSQVRJT05fU0VUOiAke0FXU19TRVNfQ09ORklHVVJBVElPTl9TRVR9XG4gICAgICBBUFBfVVJJOiAke0FQUF9VUkl9XG4gICAgICBORVhUX1BVQkxJQ19BUElfVVJJOiAke0FQUF9VUkl9L2FwaVxuICAgICAgQVBJX1VSSTogJHtBUFBfVVJJfS9hcGlcbiAgICAgIERJU0FCTEVfU0lHTlVQUzogJHtESVNBQkxFX1NJR05VUFN9XG4gICAgZW50cnlwb2ludDogW1wiL2FwcC9lbnRyeS5zaFwiXVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOmFscGluZVxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19VU0VSOiAke1BPU1RHUkVTX1VTRVJ9XG4gICAgICBQT1NUR1JFU19EQjogJHtQT1NUR1JFU19EQn1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlc19kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSAke1BPU1RHUkVTX1VTRVJ9IC1kICR7UE9TVEdSRVNfREJ9XCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGV4cG9zZTpcbiAgICAgIC0gNTQzMlxuXG4gIHJlZGlzOlxuICAgIGltYWdlOiByZWRpczphbHBpbmVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGV4cG9zZTpcbiAgICAgIC0gNjM3OVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHJlZGlzX2RhdGE6L2RhdGFcblxudm9sdW1lczpcbiAgcG9zdGdyZXNfZGF0YTpcbiAgICBkcml2ZXI6IGxvY2FsXG4gIHJlZGlzX2RhdGE6XG4gICAgZHJpdmVyOiBsb2NhbCIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5wb3N0Z3Jlc191c2VyID0gXCJwbHVua1wiXG5wb3N0Z3Jlc19kYiA9IFwicGx1bmtcIlxuXG5bY29uZmlnXVxuaXNvbGF0ZWQgPSB0cnVlXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInBsdW5rXCJcbnBvcnQgPSAzMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5wYXRoID0gXCIvXCJcblxuW2NvbmZpZy5lbnZdXG5QT1NUR1JFU19VU0VSID0gXCIke3Bvc3RncmVzX3VzZXJ9XCJcblBPU1RHUkVTX0RCID0gXCIke3Bvc3RncmVzX2RifVwiXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5SRURJU19VUkwgPSBcInJlZGlzOi8vcmVkaXM6NjM3OVwiXG5cbkpXVF9TRUNSRVQgPSBcIiR7cGFzc3dvcmQ6NjR9XCJcbkFQUF9VUkkgPSBcImh0dHBzOi8vJHttYWluX2RvbWFpbn1cIlxuXG5BV1NfUkVHSU9OID0gXCI8eW91ci1hd3MtcmVnaW9uPlwiXG5BV1NfQUNDRVNTX0tFWV9JRCA9IFwiPHlvdXItYXdzLWFjY2Vzcy1rZXktaWQ+XCJcbkFXU19TRUNSRVRfQUNDRVNTX0tFWSA9IFwiPHlvdXItYXdzLXNlY3JldC1hY2Nlc3Mta2V5PlwiXG5BV1NfU0VTX0NPTkZJR1VSQVRJT05fU0VUID0gXCI8eW91ci1zZXMtY29uZmlndXJhdGlvbi1zZXQ+XCJcblxuRElTQUJMRV9TSUdOVVBTID0gXCJGYWxzZVwiIgp9
```

## Links

`email`,`newsletter`,`mailing-list`,`marketing`

---

Version:`latest`

PlausiblePlausible is a open source, self-hosted web analytics platform that lets you track website traffic and user behavior.

Pocket IDA simple and easy-to-use OIDC provider that allows users to authenticate with their passkeys to your services.

### On this page

ConfigurationBase64LinksTags