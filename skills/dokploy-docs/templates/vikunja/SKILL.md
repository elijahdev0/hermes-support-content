---
title: "Vikunja | Dokploy"
source: "https://docs.dokploy.com/docs/templates/vikunja"
category: dokploy-docs
created: "2026-06-25T17:22:01.420Z"
---

Vikunja | Dokploy

# Vikunja

Copy as Markdown

Vikunja is a self-hosted, open-source to-do list application to organize tasks, projects, and notes.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  vikunja:
    image: vikunja/vikunja
    user: "0:0"
    environment:
      VIKUNJA_SERVICE_PUBLICURL: ${VIKUNJA_SERVICE_PUBLICURL}
      VIKUNJA_PUBLIC_PORT: ${VIKUNJA_PUBLIC_PORT}
      VIKUNJA_DATABASE_HOST: ${VIKUNJA_DATABASE_HOST}
      VIKUNJA_DATABASE_PASSWORD: ${VIKUNJA_DATABASE_PASSWORD}
      VIKUNJA_DATABASE_TYPE: ${VIKUNJA_DATABASE_TYPE}
      VIKUNJA_DATABASE_USER: ${VIKUNJA_DATABASE_USER}
      VIKUNJA_DATABASE_DATABASE: ${VIKUNJA_DATABASE_DATABASE}
      VIKUNJA_SERVICE_JWTSECRET: ${VIKUNJA_SERVICE_JWTSECRET}
    ports:
      - 3456
    volumes:
      - vikunja-files:/app/vikunja/files
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped

  db:
    image: postgres:17
    environment:
      POSTGRES_PASSWORD: ${VIKUNJA_DATABASE_PASSWORD}
      POSTGRES_USER: ${VIKUNJA_DATABASE_USER}
      POSTGRES_DB: ${VIKUNJA_DATABASE_DATABASE}
    volumes:
      - vikunja-db:/var/lib/postgresql/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready", "-U", "${VIKUNJA_DATABASE_USER}",  "-d", "${VIKUNJA_DATABASE_DATABASE}"]
      interval: 10s
      timeout: 5s
      retries: 3

volumes:
  vikunja-files: {}
  vikunja-db: {}
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:32}"
jwt_secret = "${jwt:db_password}"

[config]
[[config.domains]]
serviceName = "vikunja"
port = 3456
host = "${main_domain}"

[config.env]
VIKUNJA_SERVICE_PUBLICURL = "https://${main_domain}"
VIKUNJA_DATABASE_HOST = "db"
VIKUNJA_DATABASE_PASSWORD = "${db_password}"
VIKUNJA_DATABASE_TYPE = "postgres"
VIKUNJA_DATABASE_USER = "vikunja"
VIKUNJA_DATABASE_DATABASE = "vikunja"
VIKUNJA_SERVICE_JWTSECRET = "${jwt_secret}"

[[config.mounts]]
serviceName = "vikunja"
volumeName = "vikunja-files"
mountPath = "/app/vikunja/files"

[[config.mounts]]
serviceName = "db"
volumeName = "vikunja-db"
mountPath = "/var/lib/postgresql/data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB2aWt1bmphOlxuICAgIGltYWdlOiB2aWt1bmphL3Zpa3VuamFcbiAgICB1c2VyOiBcIjA6MFwiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBWSUtVTkpBX1NFUlZJQ0VfUFVCTElDVVJMOiAke1ZJS1VOSkFfU0VSVklDRV9QVUJMSUNVUkx9XG4gICAgICBWSUtVTkpBX1BVQkxJQ19QT1JUOiAke1ZJS1VOSkFfUFVCTElDX1BPUlR9XG4gICAgICBWSUtVTkpBX0RBVEFCQVNFX0hPU1Q6ICR7VklLVU5KQV9EQVRBQkFTRV9IT1NUfVxuICAgICAgVklLVU5KQV9EQVRBQkFTRV9QQVNTV09SRDogJHtWSUtVTkpBX0RBVEFCQVNFX1BBU1NXT1JEfVxuICAgICAgVklLVU5KQV9EQVRBQkFTRV9UWVBFOiAke1ZJS1VOSkFfREFUQUJBU0VfVFlQRX1cbiAgICAgIFZJS1VOSkFfREFUQUJBU0VfVVNFUjogJHtWSUtVTkpBX0RBVEFCQVNFX1VTRVJ9XG4gICAgICBWSUtVTkpBX0RBVEFCQVNFX0RBVEFCQVNFOiAke1ZJS1VOSkFfREFUQUJBU0VfREFUQUJBU0V9XG4gICAgICBWSUtVTkpBX1NFUlZJQ0VfSldUU0VDUkVUOiAke1ZJS1VOSkFfU0VSVklDRV9KV1RTRUNSRVR9XG4gICAgcG9ydHM6XG4gICAgICAtIDM0NTZcbiAgICB2b2x1bWVzOlxuICAgICAgLSB2aWt1bmphLWZpbGVzOi9hcHAvdmlrdW5qYS9maWxlc1xuICAgIGRlcGVuZHNfb246XG4gICAgICBkYjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gIGRiOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxN1xuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7VklLVU5KQV9EQVRBQkFTRV9QQVNTV09SRH1cbiAgICAgIFBPU1RHUkVTX1VTRVI6ICR7VklLVU5KQV9EQVRBQkFTRV9VU0VSfVxuICAgICAgUE9TVEdSRVNfREI6ICR7VklLVU5KQV9EQVRBQkFTRV9EQVRBQkFTRX1cbiAgICB2b2x1bWVzOlxuICAgICAgLSB2aWt1bmphLWRiOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5XCIsIFwiLVVcIiwgXCIke1ZJS1VOSkFfREFUQUJBU0VfVVNFUn1cIiwgIFwiLWRcIiwgXCIke1ZJS1VOSkFfREFUQUJBU0VfREFUQUJBU0V9XCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogM1xuXG52b2x1bWVzOlxuICB2aWt1bmphLWZpbGVzOiB7fVxuICB2aWt1bmphLWRiOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5qd3Rfc2VjcmV0ID0gXCIke2p3dDpkYl9wYXNzd29yZH1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwidmlrdW5qYVwiXG5wb3J0ID0gMzQ1NlxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblZJS1VOSkFfU0VSVklDRV9QVUJMSUNVUkwgPSBcImh0dHBzOi8vJHttYWluX2RvbWFpbn1cIlxuVklLVU5KQV9EQVRBQkFTRV9IT1NUID0gXCJkYlwiXG5WSUtVTkpBX0RBVEFCQVNFX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiXG5WSUtVTkpBX0RBVEFCQVNFX1RZUEUgPSBcInBvc3RncmVzXCJcblZJS1VOSkFfREFUQUJBU0VfVVNFUiA9IFwidmlrdW5qYVwiXG5WSUtVTkpBX0RBVEFCQVNFX0RBVEFCQVNFID0gXCJ2aWt1bmphXCJcblZJS1VOSkFfU0VSVklDRV9KV1RTRUNSRVQgPSBcIiR7and0X3NlY3JldH1cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcInZpa3VuamFcIlxudm9sdW1lTmFtZSA9IFwidmlrdW5qYS1maWxlc1wiXG5tb3VudFBhdGggPSBcIi9hcHAvdmlrdW5qYS9maWxlc1wiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiZGJcIlxudm9sdW1lTmFtZSA9IFwidmlrdW5qYS1kYlwiXG5tb3VudFBhdGggPSBcIi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVwiXG4iCn0=
```

## Links

`productivity`,`tasks`,`self-hosted`,`project-management`

---

Version:`0.23.0`

VerdaccioA lightweight Node.js private proxy registry

WallosWallos is a self-hosted subscription tracking application that helps you manage and monitor your subscriptions, providing insights into your spending habits.

### On this page

ConfigurationBase64LinksTags