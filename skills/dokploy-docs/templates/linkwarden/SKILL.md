---
title: "Linkwarden | Dokploy"
source: "https://docs.dokploy.com/docs/templates/linkwarden"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

Linkwarden | Dokploy

# Linkwarden

Copy as Markdown

Self-hosted, open-source collaborative bookmark manager to collect, organize and archive webpages.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  linkwarden:
    environment:
      - NEXTAUTH_SECRET
      - NEXTAUTH_URL
      - DATABASE_URL=postgresql://linkwarden:${POSTGRES_PASSWORD}@postgres:5432/linkwarden
    restart: unless-stopped
    image: ghcr.io/linkwarden/linkwarden:v2.9.3
    ports:
      - 3000
    volumes:
      - linkwarden-data:/data/data
    depends_on:
      - postgres
    healthcheck:
      test: curl --fail http://localhost:3000 || exit 1
      interval: 60s
      retries: 2
      start_period: 60s
      timeout: 15s

  postgres:
    image: postgres:17-alpine
    restart: unless-stopped
    user: postgres
    environment:
      POSTGRES_USER: linkwarden
      POSTGRES_DB: linkwarden
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  linkwarden-data:
  postgres-data:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password}"
next_secret = "${base64:32}"

[config]
mounts = []

[[config.domains]]
serviceName = "linkwarden"
port = 3_000
host = "${main_domain}"

[config.env]
POSTGRES_PASSWORD = "${postgres_password}"
NEXTAUTH_SECRET = "${next_secret}"
NEXTAUTH_URL = "http://${main_domain}/api/v1/auth"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBsaW5rd2FyZGVuOlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBORVhUQVVUSF9TRUNSRVRcbiAgICAgIC0gTkVYVEFVVEhfVVJMXG4gICAgICAtIERBVEFCQVNFX1VSTD1wb3N0Z3Jlc3FsOi8vbGlua3dhcmRlbjoke1BPU1RHUkVTX1BBU1NXT1JEfUBwb3N0Z3Jlczo1NDMyL2xpbmt3YXJkZW5cbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGltYWdlOiBnaGNyLmlvL2xpbmt3YXJkZW4vbGlua3dhcmRlbjp2Mi45LjNcbiAgICBwb3J0czpcbiAgICAgIC0gMzAwMFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGxpbmt3YXJkZW4tZGF0YTovZGF0YS9kYXRhXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcG9zdGdyZXNcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IGN1cmwgLS1mYWlsIGh0dHA6Ly9sb2NhbGhvc3Q6MzAwMCB8fCBleGl0IDFcbiAgICAgIGludGVydmFsOiA2MHNcbiAgICAgIHJldHJpZXM6IDJcbiAgICAgIHN0YXJ0X3BlcmlvZDogNjBzXG4gICAgICB0aW1lb3V0OiAxNXNcblxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTctYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB1c2VyOiBwb3N0Z3Jlc1xuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfVVNFUjogbGlua3dhcmRlblxuICAgICAgUE9TVEdSRVNfREI6IGxpbmt3YXJkZW5cbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvc3RncmVzLWRhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5XCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuXG52b2x1bWVzOlxuICBsaW5rd2FyZGVuLWRhdGE6XG4gIHBvc3RncmVzLWRhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmR9XCJcbm5leHRfc2VjcmV0ID0gXCIke2Jhc2U2NDozMn1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibGlua3dhcmRlblwiXG5wb3J0ID0gM18wMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtwb3N0Z3Jlc19wYXNzd29yZH1cIlxuTkVYVEFVVEhfU0VDUkVUID0gXCIke25leHRfc2VjcmV0fVwiXG5ORVhUQVVUSF9VUkwgPSBcImh0dHA6Ly8ke21haW5fZG9tYWlufS9hcGkvdjEvYXV0aFwiXG4iCn0=
```

## Links

`bookmarks`,`link-sharing`

---

Version:`2.9.3`

LinkStackLinkStack is an open-source link-in-bio platform for sharing multiple links using a customizable landing page.

ListmonkHigh performance, self-hosted, newsletter and mailing list manager with a modern dashboard.

### On this page

ConfigurationBase64LinksTags