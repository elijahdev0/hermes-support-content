---
title: "n8n with Postgres | Dokploy"
source: "https://docs.dokploy.com/docs/templates/n8n-with-postgres"
category: dokploy-docs
created: "2026-06-25T17:21:54.354Z"
---

n8n with Postgres | Dokploy

# n8n with Postgres

Copy as Markdown

n8n is an open source low-code platform for automating workflows and integrations with PostgreSQL database for better performance and scalability.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  postgres:
    image: postgres:17-alpine
    restart: unless-stopped
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      start_period: 30s
      interval: 10s
      timeout: 5s
      retries: 5

  n8n:
    image: n8nio/n8n:latest
    restart: unless-stopped
    environment:
      # Configuration PostgreSQL
      - DB_TYPE=postgresdb
      - DB_POSTGRESDB_HOST=postgres
      - DB_POSTGRESDB_PORT=5432
      - DB_POSTGRESDB_DATABASE=${POSTGRES_DB}
      - DB_POSTGRESDB_USER=${POSTGRES_USER}
      - DB_POSTGRESDB_PASSWORD=${POSTGRES_PASSWORD}

      # SÉCURITÉ - Encryption (IMPORTANT)
      - N8N_ENCRYPTION_KEY=${N8N_ENCRYPTION_KEY}

      # Configuration réseau
      - N8N_HOST=${N8N_HOST}
      - N8N_PORT=${N8N_PORT}
      - N8N_PROTOCOL=http
      - NODE_ENV=production
      - WEBHOOK_URL=https://${N8N_HOST}/
      - GENERIC_TIMEZONE=${GENERIC_TIMEZONE}
      - N8N_SECURE_COOKIE=false

    volumes:
      - n8n_data:/home/node/.n8n
    depends_on:
      postgres:
        condition: service_healthy

volumes:
  n8n_data:
  postgres_data:
```

```
[variables]
main_domain = "${domain}"
# Variables PostgreSQL
postgres_user = "${username}"
postgres_password = "${password:24}"
postgres_db = "n8n"
# SÉCURITÉ - Clé d'encryption (IMPORTANT)
n8n_encryption_key = "${base64:64}"

[config]
mounts = []

[[config.domains]]
serviceName = "n8n"
port = 5_678
host = "${main_domain}"

[config.env]
N8N_HOST = "${main_domain}"
N8N_PORT = "5678"
GENERIC_TIMEZONE = "Europe/Berlin"

# Variables PostgreSQL
POSTGRES_USER = "${postgres_user}"
POSTGRES_PASSWORD = "${postgres_password}"
POSTGRES_DB = "${postgres_db}"

# SÉCURITÉ - Encryption (IMPORTANT)
N8N_ENCRYPTION_KEY = "${n8n_encryption_key}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTctYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfVVNFUj0ke1BPU1RHUkVTX1VTRVJ9XG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPSR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICAtIFBPU1RHUkVTX0RCPSR7UE9TVEdSRVNfREJ9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gcG9zdGdyZXNfZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgJHtQT1NUR1JFU19VU0VSfSAtZCAke1BPU1RHUkVTX0RCfVwiXVxuICAgICAgc3RhcnRfcGVyaW9kOiAzMHNcbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG5cbiAgbjhuOlxuICAgIGltYWdlOiBuOG5pby9uOG46bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgQ29uZmlndXJhdGlvbiBQb3N0Z3JlU1FMXG4gICAgICAtIERCX1RZUEU9cG9zdGdyZXNkYlxuICAgICAgLSBEQl9QT1NUR1JFU0RCX0hPU1Q9cG9zdGdyZXNcbiAgICAgIC0gREJfUE9TVEdSRVNEQl9QT1JUPTU0MzJcbiAgICAgIC0gREJfUE9TVEdSRVNEQl9EQVRBQkFTRT0ke1BPU1RHUkVTX0RCfVxuICAgICAgLSBEQl9QT1NUR1JFU0RCX1VTRVI9JHtQT1NUR1JFU19VU0VSfVxuICAgICAgLSBEQl9QT1NUR1JFU0RCX1BBU1NXT1JEPSR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBcbiAgICAgICMgU8OJQ1VSSVTDiSAtIEVuY3J5cHRpb24gKElNUE9SVEFOVClcbiAgICAgIC0gTjhOX0VOQ1JZUFRJT05fS0VZPSR7TjhOX0VOQ1JZUFRJT05fS0VZfVxuICAgICAgXG4gICAgICAjIENvbmZpZ3VyYXRpb24gcsOpc2VhdVxuICAgICAgLSBOOE5fSE9TVD0ke044Tl9IT1NUfVxuICAgICAgLSBOOE5fUE9SVD0ke044Tl9QT1JUfVxuICAgICAgLSBOOE5fUFJPVE9DT0w9aHR0cFxuICAgICAgLSBOT0RFX0VOVj1wcm9kdWN0aW9uXG4gICAgICAtIFdFQkhPT0tfVVJMPWh0dHBzOi8vJHtOOE5fSE9TVH0vXG4gICAgICAtIEdFTkVSSUNfVElNRVpPTkU9JHtHRU5FUklDX1RJTUVaT05FfVxuICAgICAgLSBOOE5fU0VDVVJFX0NPT0tJRT1mYWxzZVxuICAgICAgXG4gICAgdm9sdW1lczpcbiAgICAgIC0gbjhuX2RhdGE6L2hvbWUvbm9kZS8ubjhuXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHBvc3RncmVzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuXG52b2x1bWVzOlxuICBuOG5fZGF0YTpcbiAgcG9zdGdyZXNfZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG4jIFZhcmlhYmxlcyBQb3N0Z3JlU1FMXG5wb3N0Z3Jlc191c2VyID0gXCIke3VzZXJuYW1lfVwiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoyNH1cIlxucG9zdGdyZXNfZGIgPSBcIm44blwiXG4jIFPDiUNVUklUw4kgLSBDbMOpIGQnZW5jcnlwdGlvbiAoSU1QT1JUQU5UKVxubjhuX2VuY3J5cHRpb25fa2V5ID0gXCIke2Jhc2U2NDo2NH1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibjhuXCJcbnBvcnQgPSA1XzY3OFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbk44Tl9IT1NUID0gXCIke21haW5fZG9tYWlufVwiXG5OOE5fUE9SVCA9IFwiNTY3OFwiXG5HRU5FUklDX1RJTUVaT05FID0gXCJFdXJvcGUvQmVybGluXCJcblxuIyBWYXJpYWJsZXMgUG9zdGdyZVNRTFxuUE9TVEdSRVNfVVNFUiA9IFwiJHtwb3N0Z3Jlc191c2VyfVwiXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtwb3N0Z3Jlc19wYXNzd29yZH1cIlxuUE9TVEdSRVNfREIgPSBcIiR7cG9zdGdyZXNfZGJ9XCJcblxuIyBTw4lDVVJJVMOJIC0gRW5jcnlwdGlvbiAoSU1QT1JUQU5UKVxuTjhOX0VOQ1JZUFRJT05fS0VZID0gXCIke244bl9lbmNyeXB0aW9uX2tleX1cIlxuIgp9
```

## Links

`automation`,`workflow`,`low-code`,`postgres`

---

Version:`latest`

n8n + Worker + Runner with Redis/Postgres and Ollaman8n is an open source low-code platform for automating workflows and integrations with PostgreSQL database and Ollama AI model.

NavidromeNavidrome is a modern music server and streamer compatible with Subsonic/Airsonic. Stream your music collection anywhere.

### On this page

ConfigurationBase64LinksTags