---
title: "Peppermint | Dokploy"
source: "https://docs.dokploy.com/docs/templates/peppermint"
category: dokploy-docs
created: "2026-06-25T17:21:56.646Z"
---

Peppermint | Dokploy

# Peppermint

Copy as Markdown

Peppermint is a modern, open-source API development platform that helps you build, test and document your APIs.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  peppermint-postgres:
    image: postgres:latest
    restart: always

    volumes:
      - peppermint-postgres-data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: peppermint
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: peppermint
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U peppermint"]
      interval: 10s
      timeout: 5s
      retries: 5

  peppermint-app:
    image: pepperlabs/peppermint:latest
    restart: always

    depends_on:
      peppermint-postgres:
        condition: service_healthy
    environment:
      DB_USERNAME: "peppermint"
      DB_PASSWORD: ${POSTGRES_PASSWORD}
      DB_HOST: "peppermint-postgres"
      SECRET: ${SECRET}

volumes:
  peppermint-postgres-data:
```

```
[variables]
main_domain = "${domain}"
api_domain = "${domain}"
postgres_password = "${password}"
secret = "${base64:32}"

[config]
mounts = []

[[config.domains]]
serviceName = "peppermint-app"
port = 3_000
host = "${main_domain}"

[[config.domains]]
serviceName = "peppermint-app"
port = 5_003
host = "${api_domain}"

[config.env]
MAIN_DOMAIN = "${main_domain}"
API_DOMAIN = "${api_domain}"
POSTGRES_PASSWORD = "${postgres_password}"
SECRET = "${secret}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHBlcHBlcm1pbnQtcG9zdGdyZXM6XG4gICAgaW1hZ2U6IHBvc3RncmVzOmxhdGVzdFxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcGVwcGVybWludC1wb3N0Z3Jlcy1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfVVNFUjogcGVwcGVybWludFxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19EQjogcGVwcGVybWludFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSBwZXBwZXJtaW50XCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuXG4gIHBlcHBlcm1pbnQtYXBwOlxuICAgIGltYWdlOiBwZXBwZXJsYWJzL3BlcHBlcm1pbnQ6bGF0ZXN0XG4gICAgcmVzdGFydDogYWx3YXlzXG5cbiAgICBkZXBlbmRzX29uOlxuICAgICAgcGVwcGVybWludC1wb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERCX1VTRVJOQU1FOiBcInBlcHBlcm1pbnRcIlxuICAgICAgREJfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBEQl9IT1NUOiBcInBlcHBlcm1pbnQtcG9zdGdyZXNcIlxuICAgICAgU0VDUkVUOiAke1NFQ1JFVH1cblxudm9sdW1lczpcbiAgcGVwcGVybWludC1wb3N0Z3Jlcy1kYXRhOiAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYXBpX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnBvc3RncmVzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkfVwiXG5zZWNyZXQgPSBcIiR7YmFzZTY0OjMyfVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJwZXBwZXJtaW50LWFwcFwiXG5wb3J0ID0gM18wMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicGVwcGVybWludC1hcHBcIlxucG9ydCA9IDVfMDAzXG5ob3N0ID0gXCIke2FwaV9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5NQUlOX0RPTUFJTiA9IFwiJHttYWluX2RvbWFpbn1cIlxuQVBJX0RPTUFJTiA9IFwiJHthcGlfZG9tYWlufVwiXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtwb3N0Z3Jlc19wYXNzd29yZH1cIlxuU0VDUkVUID0gXCIke3NlY3JldH1cIlxuIgp9
```

## Links

`api`,`development`,`documentation`

---

Version:`latest`

PenpotPenpot is the web-based open-source design tool that bridges the gap between designers and developers.

pgAdminpgAdmin is the most popular and feature rich Open Source administration and development platform for PostgreSQL, the most advanced Open Source database in the world.

### On this page

ConfigurationBase64LinksTags