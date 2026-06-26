---
title: "Kaneo | Dokploy"
source: "https://docs.dokploy.com/docs/templates/kaneo"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

Kaneo | Dokploy

# Kaneo

Copy as Markdown

Kaneo - an open source project management platform focused on simplicity and efficiency. Self-host it, customize it, make it yours.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: ${KANEO_DB}
      POSTGRES_USER: ${KANEO_DB_USER}
      POSTGRES_PASSWORD: ${KANEO_DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  backend:
    image: ghcr.io/usekaneo/api:latest
    environment:
      JWT_ACCESS: ${KANEO_JWT_ACCESS}
      DATABASE_URL: "postgresql://${KANEO_DB_USER}:${KANEO_DB_PASSWORD}@postgres:5432/${KANEO_DB}"
    ports:
      - 1337
    depends_on:
      postgres:
        condition: service_started
    restart: unless-stopped

  frontend:
    image: ghcr.io/usekaneo/web:latest
    environment:
      KANEO_API_URL: "http://${BACKEND_HOST}"
    ports:
      - 5173
    depends_on:
      backend:
        condition: service_started
    restart: unless-stopped

volumes:
  postgres_data:
```

```
[variables]
backend_domain = "${domain}"
frontend_domain = "${domain}"

[[config.domains]]
serviceName = "frontend"
port = 5_173
host = "${frontend_domain}"

[[config.domains]]
serviceName = "backend"
port = 1_337
host = "${backend_domain}"

[config.env]
BACKEND_HOST = "${backend_domain}"
KANEO_DB = "kaneo"
KANEO_DB_USER = "${username}"
KANEO_DB_PASSWORD = "${password}"
KANEO_JWT_ACCESS = "${hash:64}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTYtYWxwaW5lXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19EQjogJHtLQU5FT19EQn1cbiAgICAgIFBPU1RHUkVTX1VTRVI6ICR7S0FORU9fREJfVVNFUn1cbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke0tBTkVPX0RCX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvc3RncmVzX2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxuICBiYWNrZW5kOlxuICAgIGltYWdlOiBnaGNyLmlvL3VzZWthbmVvL2FwaTpsYXRlc3RcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEpXVF9BQ0NFU1M6ICR7S0FORU9fSldUX0FDQ0VTU31cbiAgICAgIERBVEFCQVNFX1VSTDogXCJwb3N0Z3Jlc3FsOi8vJHtLQU5FT19EQl9VU0VSfToke0tBTkVPX0RCX1BBU1NXT1JEfUBwb3N0Z3Jlczo1NDMyLyR7S0FORU9fREJ9XCJcbiAgICBwb3J0czpcbiAgICAgIC0gMTMzN1xuICAgIGRlcGVuZHNfb246XG4gICAgICBwb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX3N0YXJ0ZWRcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gIGZyb250ZW5kOlxuICAgIGltYWdlOiBnaGNyLmlvL3VzZWthbmVvL3dlYjpsYXRlc3RcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEtBTkVPX0FQSV9VUkw6IFwiaHR0cDovLyR7QkFDS0VORF9IT1NUfVwiXG4gICAgcG9ydHM6XG4gICAgICAtIDUxNzNcbiAgICBkZXBlbmRzX29uOlxuICAgICAgYmFja2VuZDpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX3N0YXJ0ZWRcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG52b2x1bWVzOlxuICBwb3N0Z3Jlc19kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5iYWNrZW5kX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmZyb250ZW5kX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJmcm9udGVuZFwiXG5wb3J0ID0gNV8xNzNcbmhvc3QgPSBcIiR7ZnJvbnRlbmRfZG9tYWlufVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImJhY2tlbmRcIlxucG9ydCA9IDFfMzM3XG5ob3N0ID0gXCIke2JhY2tlbmRfZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuQkFDS0VORF9IT1NUID0gXCIke2JhY2tlbmRfZG9tYWlufVwiXG5LQU5FT19EQiA9IFwia2FuZW9cIlxuS0FORU9fREJfVVNFUiA9IFwiJHt1c2VybmFtZX1cIlxuS0FORU9fREJfUEFTU1dPUkQgPSBcIiR7cGFzc3dvcmR9XCJcbktBTkVPX0pXVF9BQ0NFU1MgPSBcIiR7aGFzaDo2NH1cIlxuIgp9
```

## Links

`Task Tracking`

---

Version:`latest`

jenkinsJenkins is a free, open-source automation server that helps developers build, test, and deploy software by automating repetitive tasks in the software delivery pipeline.

KaraKeepA self-hostable bookmark-everything app (links, notes and images) with AI-based automatic tagging and full text search. Previously known as Hoarder.

### On this page

ConfigurationBase64LinksTags