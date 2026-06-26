---
title: "Reactive Resume | Dokploy"
source: "https://docs.dokploy.com/docs/templates/reactive-resume"
category: dokploy-docs
created: "2026-06-25T17:21:57.938Z"
---

Reactive Resume | Dokploy

# Reactive Resume

Copy as Markdown

A free and open-source resume builder that simplifies the process of creating, updating, and sharing your resume.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  postgres:
    image: postgres:16-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  minio:
    image: minio/minio:latest
    command: server /data
    volumes:
      - minio_data:/data
    environment:
      MINIO_ROOT_USER: ${MINIO_ROOT_USER}
      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD}

  chrome:
    image: ghcr.io/browserless/chromium:v2.18.0
    extra_hosts:
      - "host.docker.internal:host-gateway"
    environment:
      TIMEOUT: 10000
      CONCURRENT: 10
      TOKEN: ${CHROME_TOKEN}
      EXIT_ON_HEALTH_FAILURE: "true"
      PRE_REQUEST_HEALTH_CHECK: "true"

  app:
    image: amruthpillai/reactive-resume:latest
    depends_on:
      - postgres
      - minio
      - chrome
    environment:
      PORT: 3000
      NODE_ENV: production
      PUBLIC_URL: https://${APP_DOMAIN}
      STORAGE_URL: https://${APP_DOMAIN}/default
      CHROME_TOKEN: ${CHROME_TOKEN}
      CHROME_URL: ws://chrome:3000
      DATABASE_URL: postgresql://postgres:${POSTGRES_PASSWORD}@postgres:5432/postgres
      ACCESS_TOKEN_SECRET: ${ACCESS_TOKEN_SECRET}
      REFRESH_TOKEN_SECRET: ${REFRESH_TOKEN_SECRET}
      MAIL_FROM: ${MAIL_FROM}
      STORAGE_ENDPOINT: minio
      STORAGE_PORT: 9000
      STORAGE_REGION: us-east-1
      STORAGE_BUCKET: default
      STORAGE_ACCESS_KEY: ${MINIO_ROOT_USER}
      STORAGE_SECRET_KEY: ${MINIO_ROOT_PASSWORD}
      STORAGE_USE_SSL: "false"
      STORAGE_SKIP_BUCKET_CHECK: "false"

volumes:
  minio_data:
  postgres_data:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password:32}"
minio_user = "minioadmin"
minio_password = "${password:32}"
chrome_token = "${password:32}"
access_token_secret = "${password:64}"
refresh_token_secret = "${password:64}"
mail_from = "noreply@${main_domain}"

[config]
env = [
  "APP_DOMAIN=${main_domain}",
  "POSTGRES_PASSWORD=${postgres_password}",
  "MINIO_ROOT_USER=${minio_user}",
  "MINIO_ROOT_PASSWORD=${minio_password}",
  "CHROME_TOKEN=${chrome_token}",
  "ACCESS_TOKEN_SECRET=${access_token_secret}",
  "REFRESH_TOKEN_SECRET=${refresh_token_secret}",
  "MAIL_FROM=${mail_from}",
]
mounts = []

[[config.domains]]
serviceName = "app"
port = 3000
host = "${main_domain}"

[[config.domains]]
serviceName = "minio"
port = 9000
host = "${main_domain}"
path = "/default"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHBvc3RncmVzOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNi1hbHBpbmVcbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlc19kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6IHBvc3RncmVzXG4gICAgICBQT1NUR1JFU19VU0VSOiBwb3N0Z3Jlc1xuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5IC1VIHBvc3RncmVzIC1kIHBvc3RncmVzXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuXG4gIG1pbmlvOlxuICAgIGltYWdlOiBtaW5pby9taW5pbzpsYXRlc3RcbiAgICBjb21tYW5kOiBzZXJ2ZXIgL2RhdGFcbiAgICB2b2x1bWVzOlxuICAgICAgLSBtaW5pb19kYXRhOi9kYXRhXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNSU5JT19ST09UX1VTRVI6ICR7TUlOSU9fUk9PVF9VU0VSfVxuICAgICAgTUlOSU9fUk9PVF9QQVNTV09SRDogJHtNSU5JT19ST09UX1BBU1NXT1JEfVxuXG4gIGNocm9tZTpcbiAgICBpbWFnZTogZ2hjci5pby9icm93c2VybGVzcy9jaHJvbWl1bTp2Mi4xOC4wXG4gICAgZXh0cmFfaG9zdHM6XG4gICAgICAtIFwiaG9zdC5kb2NrZXIuaW50ZXJuYWw6aG9zdC1nYXRld2F5XCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFRJTUVPVVQ6IDEwMDAwXG4gICAgICBDT05DVVJSRU5UOiAxMFxuICAgICAgVE9LRU46ICR7Q0hST01FX1RPS0VOfVxuICAgICAgRVhJVF9PTl9IRUFMVEhfRkFJTFVSRTogXCJ0cnVlXCJcbiAgICAgIFBSRV9SRVFVRVNUX0hFQUxUSF9DSEVDSzogXCJ0cnVlXCJcblxuICBhcHA6XG4gICAgaW1hZ2U6IGFtcnV0aHBpbGxhaS9yZWFjdGl2ZS1yZXN1bWU6bGF0ZXN0XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcG9zdGdyZXNcbiAgICAgIC0gbWluaW9cbiAgICAgIC0gY2hyb21lXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1JUOiAzMDAwXG4gICAgICBOT0RFX0VOVjogcHJvZHVjdGlvblxuICAgICAgUFVCTElDX1VSTDogaHR0cHM6Ly8ke0FQUF9ET01BSU59XG4gICAgICBTVE9SQUdFX1VSTDogaHR0cHM6Ly8ke0FQUF9ET01BSU59L2RlZmF1bHRcbiAgICAgIENIUk9NRV9UT0tFTjogJHtDSFJPTUVfVE9LRU59XG4gICAgICBDSFJPTUVfVVJMOiB3czovL2Nocm9tZTozMDAwXG4gICAgICBEQVRBQkFTRV9VUkw6IHBvc3RncmVzcWw6Ly9wb3N0Z3Jlczoke1BPU1RHUkVTX1BBU1NXT1JEfUBwb3N0Z3Jlczo1NDMyL3Bvc3RncmVzXG4gICAgICBBQ0NFU1NfVE9LRU5fU0VDUkVUOiAke0FDQ0VTU19UT0tFTl9TRUNSRVR9XG4gICAgICBSRUZSRVNIX1RPS0VOX1NFQ1JFVDogJHtSRUZSRVNIX1RPS0VOX1NFQ1JFVH1cbiAgICAgIE1BSUxfRlJPTTogJHtNQUlMX0ZST019XG4gICAgICBTVE9SQUdFX0VORFBPSU5UOiBtaW5pb1xuICAgICAgU1RPUkFHRV9QT1JUOiA5MDAwXG4gICAgICBTVE9SQUdFX1JFR0lPTjogdXMtZWFzdC0xXG4gICAgICBTVE9SQUdFX0JVQ0tFVDogZGVmYXVsdFxuICAgICAgU1RPUkFHRV9BQ0NFU1NfS0VZOiAke01JTklPX1JPT1RfVVNFUn1cbiAgICAgIFNUT1JBR0VfU0VDUkVUX0tFWTogJHtNSU5JT19ST09UX1BBU1NXT1JEfVxuICAgICAgU1RPUkFHRV9VU0VfU1NMOiBcImZhbHNlXCJcbiAgICAgIFNUT1JBR0VfU0tJUF9CVUNLRVRfQ0hFQ0s6IFwiZmFsc2VcIlxuXG5cbnZvbHVtZXM6XG4gIG1pbmlvX2RhdGE6XG4gIHBvc3RncmVzX2RhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbm1pbmlvX3VzZXIgPSBcIm1pbmlvYWRtaW5cIlxubWluaW9fcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmNocm9tZV90b2tlbiA9IFwiJHtwYXNzd29yZDozMn1cIlxuYWNjZXNzX3Rva2VuX3NlY3JldCA9IFwiJHtwYXNzd29yZDo2NH1cIlxucmVmcmVzaF90b2tlbl9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6NjR9XCJcbm1haWxfZnJvbSA9IFwibm9yZXBseUAke21haW5fZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiQVBQX0RPTUFJTj0ke21haW5fZG9tYWlufVwiLFxuICBcIlBPU1RHUkVTX1BBU1NXT1JEPSR7cG9zdGdyZXNfcGFzc3dvcmR9XCIsXG4gIFwiTUlOSU9fUk9PVF9VU0VSPSR7bWluaW9fdXNlcn1cIixcbiAgXCJNSU5JT19ST09UX1BBU1NXT1JEPSR7bWluaW9fcGFzc3dvcmR9XCIsXG4gIFwiQ0hST01FX1RPS0VOPSR7Y2hyb21lX3Rva2VufVwiLFxuICBcIkFDQ0VTU19UT0tFTl9TRUNSRVQ9JHthY2Nlc3NfdG9rZW5fc2VjcmV0fVwiLFxuICBcIlJFRlJFU0hfVE9LRU5fU0VDUkVUPSR7cmVmcmVzaF90b2tlbl9zZWNyZXR9XCIsXG4gIFwiTUFJTF9GUk9NPSR7bWFpbF9mcm9tfVwiLFxuXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYXBwXCJcbnBvcnQgPSAzMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIm1pbmlvXCJcbnBvcnQgPSA5MDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5wYXRoID0gXCIvZGVmYXVsdFwiXG4iCn0=
```

## Links

`resume`,`cv`,`productivity`,`document`

---

Version:`latest`

RabbitMQRabbitMQ is an open source multi-protocol messaging broker.

Docker RegistryDistribution implementation for storing and distributing of Docker container images and artifacts.

### On this page

ConfigurationBase64LinksTags