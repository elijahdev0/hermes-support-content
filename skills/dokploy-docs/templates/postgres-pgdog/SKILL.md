---
title: "PostgreSQL with PgDog | Dokploy"
source: "https://docs.dokploy.com/docs/templates/postgres-pgdog"
category: dokploy-docs
created: "2026-06-25T17:21:56.648Z"
---

PostgreSQL with PgDog | Dokploy

# PostgreSQL with PgDog

Copy as Markdown

PostgreSQL database with PgDog connection pooler, load balancer, and horizontal scaling proxy. A modern alternative to PgBouncer with multi-threading support.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  postgres-pgdog:
    image: ${PGDOG_IMAGE}
    restart: unless-stopped
    # Uncomment 'ports' settings below to enable external access
    # ports:
    #   - "6432:6432"
    volumes:
      - ../files/pgdog.toml:/pgdog/pgdog.toml
      - ../files/users.toml:/pgdog/users.toml
    environment:
      - RUST_LOG=${RUST_LOG}
    depends_on:
      postgres:
        condition: service_healthy

  postgres:
    image: ${POSTGRES_IMAGE}
    restart: unless-stopped
    environment:
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
    volumes:
      - postgres-data:/var/lib/postgresql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres-data:
```

```
[variables]
postgres_user = "${username}"
postgres_password = "${password:32}"
postgres_db = "postgres"
pgdog_image = "ghcr.io/pgdogdev/pgdog:v0.1.26"
postgres_image = "postgres:18-alpine"

[[config.mounts]]
filePath = "pgdog.toml"
content = """
[general]
host = "0.0.0.0"
port = 6432

[[databases]]
name = "${postgres_db}"
host = "postgres"
port = 5432
"""

[[config.mounts]]
filePath = "users.toml"
content = """
[[users]]
name = "${postgres_user}"
database = "${postgres_db}"
password = "${postgres_password}"
"""

[config.env]
POSTGRES_USER = "${postgres_user}"
POSTGRES_PASSWORD = "${postgres_password}"
POSTGRES_DB = "${postgres_db}"
PGDOG_IMAGE = "${pgdog_image}"
POSTGRES_IMAGE = "${postgres_image}"
RUST_LOG = "info"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwb3N0Z3Jlcy1wZ2RvZzpcbiAgICBpbWFnZTogJHtQR0RPR19JTUFHRX1cbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgICMgVW5jb21tZW50ICdwb3J0cycgc2V0dGluZ3MgYmVsb3cgdG8gZW5hYmxlIGV4dGVybmFsIGFjY2Vzc1xuICAgICMgcG9ydHM6XG4gICAgIyAgIC0gXCI2NDMyOjY0MzJcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL3BnZG9nLnRvbWw6L3BnZG9nL3BnZG9nLnRvbWxcbiAgICAgIC0gLi4vZmlsZXMvdXNlcnMudG9tbDovcGdkb2cvdXNlcnMudG9tbFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBSVVNUX0xPRz0ke1JVU1RfTE9HfVxuICAgIGRlcGVuZHNfb246XG4gICAgICBwb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcblxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogJHtQT1NUR1JFU19JTUFHRX1cbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19VU0VSPSR7UE9TVEdSRVNfVVNFUn1cbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkQ9JHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIC0gUE9TVEdSRVNfREI9JHtQT1NUR1JFU19EQn1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlcy1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWxcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgJHtQT1NUR1JFU19VU0VSfSAtZCAke1BPU1RHUkVTX0RCfVwiXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcblxudm9sdW1lczpcbiAgcG9zdGdyZXMtZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxucG9zdGdyZXNfdXNlciA9IFwiJHt1c2VybmFtZX1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbnBvc3RncmVzX2RiID0gXCJwb3N0Z3Jlc1wiXG5wZ2RvZ19pbWFnZSA9IFwiZ2hjci5pby9wZ2RvZ2Rldi9wZ2RvZzp2MC4xLjI2XCJcbnBvc3RncmVzX2ltYWdlID0gXCJwb3N0Z3JlczoxOC1hbHBpbmVcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcInBnZG9nLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuW2dlbmVyYWxdXG5ob3N0ID0gXCIwLjAuMC4wXCJcbnBvcnQgPSA2NDMyXG5cbltbZGF0YWJhc2VzXV1cbm5hbWUgPSBcIiR7cG9zdGdyZXNfZGJ9XCJcbmhvc3QgPSBcInBvc3RncmVzXCJcbnBvcnQgPSA1NDMyXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCJ1c2Vycy50b21sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbltbdXNlcnNdXVxubmFtZSA9IFwiJHtwb3N0Z3Jlc191c2VyfVwiXG5kYXRhYmFzZSA9IFwiJHtwb3N0Z3Jlc19kYn1cIlxucGFzc3dvcmQgPSBcIiR7cG9zdGdyZXNfcGFzc3dvcmR9XCJcblwiXCJcIlxuXG5bY29uZmlnLmVudl1cblBPU1RHUkVTX1VTRVIgPSBcIiR7cG9zdGdyZXNfdXNlcn1cIlxuUE9TVEdSRVNfUEFTU1dPUkQgPSBcIiR7cG9zdGdyZXNfcGFzc3dvcmR9XCJcblBPU1RHUkVTX0RCID0gXCIke3Bvc3RncmVzX2RifVwiXG5QR0RPR19JTUFHRSA9IFwiJHtwZ2RvZ19pbWFnZX1cIlxuUE9TVEdSRVNfSU1BR0UgPSBcIiR7cG9zdGdyZXNfaW1hZ2V9XCJcblJVU1RfTE9HID0gXCJpbmZvXCJcbiIKfQ==
```

## Links

`database`,`postgresql`,`pooler`,`proxy`,`load-balancer`

---

Version:`0.1.26`

Poste.ioComplete mail server solution with SMTP, IMAP, POP3, antispam, antivirus, web administration and webmail client.

PostgresusFree, open source and self-hosted solution for automated PostgreSQL backups. With multiple storage options and notifications

### On this page

ConfigurationBase64LinksTags