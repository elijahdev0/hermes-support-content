---
title: "Gitea (PostgreSQL) | Dokploy"
source: "https://docs.dokploy.com/docs/templates/gitea-postgres"
category: dokploy-docs
created: "2026-06-25T17:21:48.522Z"
---

Gitea (PostgreSQL) | Dokploy

# Gitea (PostgreSQL)

Copy as Markdown

Gitea bundled with PostgreSQL.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  gitea:
    image: docker.gitea.com/gitea:1.24.4
    restart: unless-stopped
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=postgres
      - GITEA__database__HOST=postgres:5432
      - GITEA__database__NAME=gitea
      - GITEA__database__USER=gitea
      - GITEA__database__PASSWD=${GITEA_DB_PASSWORD:-gitea}
    volumes:
      - gitea-data:/data
    expose:
      - "3000"
      - "22"
    depends_on:
      - postgres
    healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://localhost:3000/"]
      interval: 15s
      timeout: 5s
      retries: 10

  postgres:
    image: docker.io/library/postgres:14
    restart: unless-stopped
    environment:
      - POSTGRES_USER=gitea
      - POSTGRES_PASSWORD=${GITEA_DB_PASSWORD:-gitea}
      - POSTGRES_DB=gitea
    volumes:
      - pg-data:/var/lib/postgresql/data
    expose:
      - "5432"

volumes:
  gitea-data: {}
  pg-data: {}
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:24}"

[config]
[[config.domains]]
serviceName = "gitea"
port = 3000
host = "${main_domain}"

[config.env]
USER_UID = "1000"
USER_GID = "1000"
GITEA__database__DB_TYPE = "postgres"
GITEA__database__HOST = "postgres:5432"
GITEA__database__NAME = "gitea"
GITEA__database__USER = "gitea"
GITEA__database__PASSWD = "${db_password}"
GITEA_DB_PASSWORD = "${db_password}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGdpdGVhOlxuICAgIGltYWdlOiBkb2NrZXIuZ2l0ZWEuY29tL2dpdGVhOjEuMjQuNFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFVTRVJfVUlEPTEwMDBcbiAgICAgIC0gVVNFUl9HSUQ9MTAwMFxuICAgICAgLSBHSVRFQV9fZGF0YWJhc2VfX0RCX1RZUEU9cG9zdGdyZXNcbiAgICAgIC0gR0lURUFfX2RhdGFiYXNlX19IT1NUPXBvc3RncmVzOjU0MzJcbiAgICAgIC0gR0lURUFfX2RhdGFiYXNlX19OQU1FPWdpdGVhXG4gICAgICAtIEdJVEVBX19kYXRhYmFzZV9fVVNFUj1naXRlYVxuICAgICAgLSBHSVRFQV9fZGF0YWJhc2VfX1BBU1NXRD0ke0dJVEVBX0RCX1BBU1NXT1JEOi1naXRlYX1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBnaXRlYS1kYXRhOi9kYXRhXG4gICAgZXhwb3NlOlxuICAgICAgLSBcIjMwMDBcIlxuICAgICAgLSBcIjIyXCJcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBwb3N0Z3Jlc1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwid2dldFwiLCBcIi1xXCIsIFwiLS1zcGlkZXJcIiwgXCJodHRwOi8vbG9jYWxob3N0OjMwMDAvXCJdXG4gICAgICBpbnRlcnZhbDogMTVzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogMTBcblxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogZG9ja2VyLmlvL2xpYnJhcnkvcG9zdGdyZXM6MTRcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19VU0VSPWdpdGVhXG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPSR7R0lURUFfREJfUEFTU1dPUkQ6LWdpdGVhfVxuICAgICAgLSBQT1NUR1JFU19EQj1naXRlYVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBnLWRhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgZXhwb3NlOlxuICAgICAgLSBcIjU0MzJcIlxuXG52b2x1bWVzOlxuICBnaXRlYS1kYXRhOiB7fVxuICBwZy1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjI0fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJnaXRlYVwiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblVTRVJfVUlEID0gXCIxMDAwXCJcblVTRVJfR0lEID0gXCIxMDAwXCJcbkdJVEVBX19kYXRhYmFzZV9fREJfVFlQRSA9IFwicG9zdGdyZXNcIlxuR0lURUFfX2RhdGFiYXNlX19IT1NUID0gXCJwb3N0Z3Jlczo1NDMyXCJcbkdJVEVBX19kYXRhYmFzZV9fTkFNRSA9IFwiZ2l0ZWFcIlxuR0lURUFfX2RhdGFiYXNlX19VU0VSID0gXCJnaXRlYVwiXG5HSVRFQV9fZGF0YWJhc2VfX1BBU1NXRCA9IFwiJHtkYl9wYXNzd29yZH1cIlxuR0lURUFfREJfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcblxuW1tjb25maWcubW91bnRzXV0iCn0=
```

## Links

`git`,`scm`,`postgres`,`developer-tools`,`self-hosted`

---

Version:`1.24.4`

Gitea (MySQL)Gitea bundled with MySQL 8.

Gitea (SQLite)Self-hosted Git service using SQLite for a simple one-container setup.

### On this page

ConfigurationBase64LinksTags