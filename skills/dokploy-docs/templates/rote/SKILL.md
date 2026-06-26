---
title: "Rote | Dokploy"
source: "https://docs.dokploy.com/docs/templates/rote"
category: dokploy-docs
created: "2026-06-25T17:21:57.938Z"
---

Rote | Dokploy

# Rote

Copy as Markdown

Rote is an open-source multi-platform personal note system featuring an open API, full data ownership, and effortless Docker deployment.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  rote-backend:
    image: rabithua/rote-backend:${IMAGE_TAG:-latest}
    pull_policy: always
    environment:
      POSTGRESQL_URL: postgresql://rote:${POSTGRES_PASSWORD}@rote-postgres:5432/rote
    depends_on:
      rote-postgres:
        condition: service_healthy
    restart: unless-stopped
    command:
      [
        "sh",
        "-c",
        "sleep 15 && bun run dist/scripts/runMigrations.js && bun run dist/server.js",
      ]

  rote-frontend:
    image: rabithua/rote-frontend:${IMAGE_TAG:-latest}
    pull_policy: always
    depends_on:
      - rote-backend
    environment:
      # VITE_API_BASE must point to an address that reaches rote-backend (reverse-proxy domain or host IP:port)
      VITE_API_BASE: ${VITE_API_BASE}
    restart: unless-stopped

  rote-postgres:
    image: postgres:17
    restart: unless-stopped
    environment:
      POSTGRES_USER: rote
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: rote
    volumes:
      - rote-postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U rote -d rote"]
      interval: 5s
      timeout: 3s
      retries: 10
      start_period: 30s

volumes:
  rote-postgres-data: {}
```

```
[variables]
frontend_domain = "${domain}"
backend_domain = "${domain}"
postgres_password = "${password:32}"
image_tag = "latest"

[config]
[[config.domains]]
serviceName = "rote-frontend"
port = 80
host = "${frontend_domain}"

[[config.domains]]
serviceName = "rote-backend"
port = 3000
host = "${backend_domain}"

[config.env]
POSTGRES_PASSWORD = "${postgres_password}"
IMAGE_TAG = "${image_tag}"
VITE_API_BASE = "http://${backend_domain}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICByb3RlLWJhY2tlbmQ6XG4gICAgaW1hZ2U6IHJhYml0aHVhL3JvdGUtYmFja2VuZDoke0lNQUdFX1RBRzotbGF0ZXN0fVxuICAgIHB1bGxfcG9saWN5OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTUUxfVVJMOiBwb3N0Z3Jlc3FsOi8vcm90ZToke1BPU1RHUkVTX1BBU1NXT1JEfUByb3RlLXBvc3RncmVzOjU0MzIvcm90ZVxuICAgIGRlcGVuZHNfb246XG4gICAgICByb3RlLXBvc3RncmVzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgY29tbWFuZDpcbiAgICAgIFtcbiAgICAgICAgXCJzaFwiLFxuICAgICAgICBcIi1jXCIsXG4gICAgICAgIFwic2xlZXAgMTUgJiYgYnVuIHJ1biBkaXN0L3NjcmlwdHMvcnVuTWlncmF0aW9ucy5qcyAmJiBidW4gcnVuIGRpc3Qvc2VydmVyLmpzXCIsXG4gICAgICBdXG5cbiAgcm90ZS1mcm9udGVuZDpcbiAgICBpbWFnZTogcmFiaXRodWEvcm90ZS1mcm9udGVuZDoke0lNQUdFX1RBRzotbGF0ZXN0fVxuICAgIHB1bGxfcG9saWN5OiBhbHdheXNcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSByb3RlLWJhY2tlbmRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgVklURV9BUElfQkFTRSBtdXN0IHBvaW50IHRvIGFuIGFkZHJlc3MgdGhhdCByZWFjaGVzIHJvdGUtYmFja2VuZCAocmV2ZXJzZS1wcm94eSBkb21haW4gb3IgaG9zdCBJUDpwb3J0KVxuICAgICAgVklURV9BUElfQkFTRTogJHtWSVRFX0FQSV9CQVNFfVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgcm90ZS1wb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTdcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfVVNFUjogcm90ZVxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19EQjogcm90ZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHJvdGUtcG9zdGdyZXMtZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgcm90ZSAtZCByb3RlXCJdXG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHRpbWVvdXQ6IDNzXG4gICAgICByZXRyaWVzOiAxMFxuICAgICAgc3RhcnRfcGVyaW9kOiAzMHNcblxudm9sdW1lczpcbiAgcm90ZS1wb3N0Z3Jlcy1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5mcm9udGVuZF9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5iYWNrZW5kX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnBvc3RncmVzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5pbWFnZV90YWcgPSBcImxhdGVzdFwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJyb3RlLWZyb250ZW5kXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHtmcm9udGVuZF9kb21haW59XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicm90ZS1iYWNrZW5kXCJcbnBvcnQgPSAzMDAwXG5ob3N0ID0gXCIke2JhY2tlbmRfZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuUE9TVEdSRVNfUEFTU1dPUkQgPSBcIiR7cG9zdGdyZXNfcGFzc3dvcmR9XCJcbklNQUdFX1RBRyA9IFwiJHtpbWFnZV90YWd9XCJcblZJVEVfQVBJX0JBU0UgPSBcImh0dHA6Ly8ke2JhY2tlbmRfZG9tYWlufVwiXG5cbltbY29uZmlnLm1vdW50c11dXG4iCn0=
```

## Links

`notes`,`productivity`,`postgres`,`bun`

---

Version:`latest`

RocketchatRocket.Chat is a free and open-source web chat platform that allows you to build and manage your own chat applications.

RoundcubeFree and open source webmail software for the masses, written in PHP.

### On this page

ConfigurationBase64LinksTags