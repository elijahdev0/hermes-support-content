---
title: "PocketBase | Dokploy"
source: "https://docs.dokploy.com/docs/templates/pocketbase"
category: dokploy-docs
created: "2026-06-25T17:21:56.648Z"
---

PocketBase | Dokploy

# PocketBase

Copy as Markdown

Open Source backend in 1 file

## Configuration

docker-compose.ymltemplate.toml

```
# IMPORTANT: Please update the admin credentials in your .env file
# Access PocketBase Admin UI at: https://your-domain.com/_/ (replace with your configured domain)
# Note: Admin UI may take up to 1 minute to load on first startup

version: "3.8"

services:
  pocketbase:
    image: adrianmusante/pocketbase:latest
    restart: always
    expose:
      - 8090
    volumes:
      - pocketbase-data:/pocketbase
    environment:
      - POCKETBASE_ADMIN_EMAIL=${ADMIN_EMAIL}
      - POCKETBASE_ADMIN_PASSWORD=${ADMIN_PASSWORD}
      - POCKETBASE_ADMIN_UPSERT=true
      - POCKETBASE_PORT_NUMBER=8090
      # Optional: Encryption key for securing app settings (OAuth2 secrets, SMTP passwords, etc.)
      # Uncomment and set a secure key in your .env file for production use
      # - POCKETBASE_ENCRYPTION_KEY=${ENCRYPTION_KEY}
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:8090/_/"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  pocketbase-data: {}
```

```
[variables]
main_domain = "${domain}"
admin_email = "${email}"
admin_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "pocketbase"
port = 8090
host = "${main_domain}"

[config.env]
ADMIN_EMAIL = "${admin_email}"
ADMIN_PASSWORD = "${admin_password}"

[[config.mounts]]
name = "pocketbase-data"
mountPath = "/pocketbase"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgSU1QT1JUQU5UOiBQbGVhc2UgdXBkYXRlIHRoZSBhZG1pbiBjcmVkZW50aWFscyBpbiB5b3VyIC5lbnYgZmlsZVxuIyBBY2Nlc3MgUG9ja2V0QmFzZSBBZG1pbiBVSSBhdDogaHR0cHM6Ly95b3VyLWRvbWFpbi5jb20vXy8gKHJlcGxhY2Ugd2l0aCB5b3VyIGNvbmZpZ3VyZWQgZG9tYWluKVxuIyBOb3RlOiBBZG1pbiBVSSBtYXkgdGFrZSB1cCB0byAxIG1pbnV0ZSB0byBsb2FkIG9uIGZpcnN0IHN0YXJ0dXBcblxudmVyc2lvbjogXCIzLjhcIlxuXG5zZXJ2aWNlczpcbiAgcG9ja2V0YmFzZTpcbiAgICBpbWFnZTogYWRyaWFubXVzYW50ZS9wb2NrZXRiYXNlOmxhdGVzdFxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGV4cG9zZTpcbiAgICAgIC0gODA5MFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvY2tldGJhc2UtZGF0YTovcG9ja2V0YmFzZVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT0NLRVRCQVNFX0FETUlOX0VNQUlMPSR7QURNSU5fRU1BSUx9XG4gICAgICAtIFBPQ0tFVEJBU0VfQURNSU5fUEFTU1dPUkQ9JHtBRE1JTl9QQVNTV09SRH1cbiAgICAgIC0gUE9DS0VUQkFTRV9BRE1JTl9VUFNFUlQ9dHJ1ZVxuICAgICAgLSBQT0NLRVRCQVNFX1BPUlRfTlVNQkVSPTgwOTBcbiAgICAgICMgT3B0aW9uYWw6IEVuY3J5cHRpb24ga2V5IGZvciBzZWN1cmluZyBhcHAgc2V0dGluZ3MgKE9BdXRoMiBzZWNyZXRzLCBTTVRQIHBhc3N3b3JkcywgZXRjLilcbiAgICAgICMgVW5jb21tZW50IGFuZCBzZXQgYSBzZWN1cmUga2V5IGluIHlvdXIgLmVudiBmaWxlIGZvciBwcm9kdWN0aW9uIHVzZVxuICAgICAgIyAtIFBPQ0tFVEJBU0VfRU5DUllQVElPTl9LRVk9JHtFTkNSWVBUSU9OX0tFWX1cbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcIndnZXRcIiwgXCItcU8tXCIsIFwiaHR0cDovL2xvY2FsaG9zdDo4MDkwL18vXCJdXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDNcblxudm9sdW1lczpcbiAgcG9ja2V0YmFzZS1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmFkbWluX2VtYWlsID0gXCIke2VtYWlsfVwiXG5hZG1pbl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicG9ja2V0YmFzZVwiXG5wb3J0ID0gODA5MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkFETUlOX0VNQUlMID0gXCIke2FkbWluX2VtYWlsfVwiXG5BRE1JTl9QQVNTV09SRCA9IFwiJHthZG1pbl9wYXNzd29yZH1cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxubmFtZSA9IFwicG9ja2V0YmFzZS1kYXRhXCJcbm1vdW50UGF0aCA9IFwiL3BvY2tldGJhc2VcIlxuIgp9
```

## Links

`backend`,`database`,`api`

---

Version:`latest`

Pocket IDA simple and easy-to-use OIDC provider that allows users to authenticate with their passkeys to your services.

PokePoke is an open-source, self-hosted alternative to YouTube. A privacy-focused video platform that allows you to watch and share videos without tracking.

### On this page

ConfigurationBase64LinksTags