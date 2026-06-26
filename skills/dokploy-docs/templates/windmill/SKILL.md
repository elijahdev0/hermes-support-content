---
title: "Windmill | Dokploy"
source: "https://docs.dokploy.com/docs/templates/windmill"
category: dokploy-docs
created: "2026-06-25T17:22:01.421Z"
---

Windmill | Dokploy

# Windmill

Copy as Markdown

A developer platform to build production-grade workflows and internal apps. Open-source alternative to Airplane, Retool, and GitHub Actions.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  windmill-postgres:
    image: postgres:16
    shm_size: 1g
    restart: unless-stopped
    volumes:
      - windmill-postgres-data:/var/lib/postgresql/data

    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: windmill
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  windmill-server:
    image: ghcr.io/windmill-labs/windmill:main

    restart: unless-stopped
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - MODE=server
      - BASE_URL=http://${WINDMILL_HOST}
    depends_on:
      windmill-postgres:
        condition: service_healthy
    volumes:
      - windmill-worker-logs:/tmp/windmill/logs

  windmill-worker:
    image: ghcr.io/windmill-labs/windmill:main
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: "1"
          memory: 2048M
    restart: unless-stopped

    environment:
      - DATABASE_URL=${DATABASE_URL}
      - MODE=worker
      - WORKER_GROUP=default
    depends_on:
      windmill-postgres:
        condition: service_healthy
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - windmill-worker-cache:/tmp/windmill/cache
      - windmill-worker-logs:/tmp/windmill/logs

  windmill-worker-native:
    image: ghcr.io/windmill-labs/windmill:main
    deploy:
      replicas: 1
      resources:
        limits:
          cpus: "0.1"
          memory: 128M
    restart: unless-stopped

    environment:
      - DATABASE_URL=${DATABASE_URL}
      - MODE=worker
      - WORKER_GROUP=native
      - NUM_WORKERS=8
      - SLEEP_QUEUE=200
    depends_on:
      windmill-postgres:
        condition: service_healthy
    volumes:
      - windmill-worker-logs:/tmp/windmill/logs

  windmill-lsp:
    image: ghcr.io/windmill-labs/windmill-lsp:latest
    restart: unless-stopped

    volumes:
      - windmill-lsp-cache:/root/.cache

  windmill-caddy:
    image: ghcr.io/windmill-labs/caddy-l4:latest
    restart: unless-stopped

    volumes:
      - ../files/Caddyfile:/etc/caddy/Caddyfile
    environment:
      - BASE_URL=":80"
    depends_on:
      - windmill-server
      - windmill-lsp

volumes:
  windmill-postgres-data:
  windmill-worker-cache:
  windmill-worker-logs:
  windmill-lsp-cache:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password}"

[[config.domains]]
serviceName = "windmill-caddy"
port = 80
host = "${main_domain}"

[config.env]
WINDMILL_HOST = "${main_domain}"
POSTGRES_PASSWORD = "${postgres_password}"
DATABASE_URL = "postgres://postgres:${postgres_password}@windmill-postgres/windmill?sslmode=disable"

[[config.mounts]]
filePath = "Caddyfile"
content = """
:80 {
    bind 0.0.0.0
    reverse_proxy /ws/* http://windmill-lsp:3001
    reverse_proxy /* http://windmill-server:8000
}
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHdpbmRtaWxsLXBvc3RncmVzOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNlxuICAgIHNobV9zaXplOiAxZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gd2luZG1pbGwtcG9zdGdyZXMtZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcblxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19EQjogd2luZG1pbGxcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgcG9zdGdyZXNcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG5cbiAgd2luZG1pbGwtc2VydmVyOlxuICAgIGltYWdlOiBnaGNyLmlvL3dpbmRtaWxsLWxhYnMvd2luZG1pbGw6bWFpblxuXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gREFUQUJBU0VfVVJMPSR7REFUQUJBU0VfVVJMfVxuICAgICAgLSBNT0RFPXNlcnZlclxuICAgICAgLSBCQVNFX1VSTD1odHRwOi8vJHtXSU5ETUlMTF9IT1NUfVxuICAgIGRlcGVuZHNfb246XG4gICAgICB3aW5kbWlsbC1wb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICB2b2x1bWVzOlxuICAgICAgLSB3aW5kbWlsbC13b3JrZXItbG9nczovdG1wL3dpbmRtaWxsL2xvZ3NcblxuICB3aW5kbWlsbC13b3JrZXI6XG4gICAgaW1hZ2U6IGdoY3IuaW8vd2luZG1pbGwtbGFicy93aW5kbWlsbDptYWluXG4gICAgZGVwbG95OlxuICAgICAgcmVwbGljYXM6IDNcbiAgICAgIHJlc291cmNlczpcbiAgICAgICAgbGltaXRzOlxuICAgICAgICAgIGNwdXM6IFwiMVwiXG4gICAgICAgICAgbWVtb3J5OiAyMDQ4TVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gREFUQUJBU0VfVVJMPSR7REFUQUJBU0VfVVJMfVxuICAgICAgLSBNT0RFPXdvcmtlclxuICAgICAgLSBXT1JLRVJfR1JPVVA9ZGVmYXVsdFxuICAgIGRlcGVuZHNfb246XG4gICAgICB3aW5kbWlsbC1wb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICB2b2x1bWVzOlxuICAgICAgLSAvdmFyL3J1bi9kb2NrZXIuc29jazovdmFyL3J1bi9kb2NrZXIuc29ja1xuICAgICAgLSB3aW5kbWlsbC13b3JrZXItY2FjaGU6L3RtcC93aW5kbWlsbC9jYWNoZVxuICAgICAgLSB3aW5kbWlsbC13b3JrZXItbG9nczovdG1wL3dpbmRtaWxsL2xvZ3NcblxuICB3aW5kbWlsbC13b3JrZXItbmF0aXZlOlxuICAgIGltYWdlOiBnaGNyLmlvL3dpbmRtaWxsLWxhYnMvd2luZG1pbGw6bWFpblxuICAgIGRlcGxveTpcbiAgICAgIHJlcGxpY2FzOiAxXG4gICAgICByZXNvdXJjZXM6XG4gICAgICAgIGxpbWl0czpcbiAgICAgICAgICBjcHVzOiBcIjAuMVwiXG4gICAgICAgICAgbWVtb3J5OiAxMjhNXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBEQVRBQkFTRV9VUkw9JHtEQVRBQkFTRV9VUkx9XG4gICAgICAtIE1PREU9d29ya2VyXG4gICAgICAtIFdPUktFUl9HUk9VUD1uYXRpdmVcbiAgICAgIC0gTlVNX1dPUktFUlM9OFxuICAgICAgLSBTTEVFUF9RVUVVRT0yMDBcbiAgICBkZXBlbmRzX29uOlxuICAgICAgd2luZG1pbGwtcG9zdGdyZXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgdm9sdW1lczpcbiAgICAgIC0gd2luZG1pbGwtd29ya2VyLWxvZ3M6L3RtcC93aW5kbWlsbC9sb2dzXG5cbiAgd2luZG1pbGwtbHNwOlxuICAgIGltYWdlOiBnaGNyLmlvL3dpbmRtaWxsLWxhYnMvd2luZG1pbGwtbHNwOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSB3aW5kbWlsbC1sc3AtY2FjaGU6L3Jvb3QvLmNhY2hlXG5cbiAgd2luZG1pbGwtY2FkZHk6XG4gICAgaW1hZ2U6IGdoY3IuaW8vd2luZG1pbGwtbGFicy9jYWRkeS1sNDpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvQ2FkZHlmaWxlOi9ldGMvY2FkZHkvQ2FkZHlmaWxlXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIEJBU0VfVVJMPVwiOjgwXCJcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSB3aW5kbWlsbC1zZXJ2ZXJcbiAgICAgIC0gd2luZG1pbGwtbHNwXG5cblxudm9sdW1lczpcbiAgd2luZG1pbGwtcG9zdGdyZXMtZGF0YTpcbiAgd2luZG1pbGwtd29ya2VyLWNhY2hlOlxuICB3aW5kbWlsbC13b3JrZXItbG9nczpcbiAgd2luZG1pbGwtbHNwLWNhY2hlOiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZH1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ3aW5kbWlsbC1jYWRkeVwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5XSU5ETUlMTF9IT1NUID0gXCIke21haW5fZG9tYWlufVwiXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtwb3N0Z3Jlc19wYXNzd29yZH1cIlxuREFUQUJBU0VfVVJMID0gXCJwb3N0Z3JlczovL3Bvc3RncmVzOiR7cG9zdGdyZXNfcGFzc3dvcmR9QHdpbmRtaWxsLXBvc3RncmVzL3dpbmRtaWxsP3NzbG1vZGU9ZGlzYWJsZVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiQ2FkZHlmaWxlXCJcbmNvbnRlbnQgPSBcIlwiXCJcbjo4MCB7XG4gICAgYmluZCAwLjAuMC4wXG4gICAgcmV2ZXJzZV9wcm94eSAvd3MvKiBodHRwOi8vd2luZG1pbGwtbHNwOjMwMDFcbiAgICByZXZlcnNlX3Byb3h5IC8qIGh0dHA6Ly93aW5kbWlsbC1zZXJ2ZXI6ODAwMFxufSBcblwiXCJcIlxuIgp9
```

## Links

`workflow`,`automation`,`development`

---

Version:`latest`

Wiki.jsThe most powerful and extensible open source Wiki software.

Windows (dockerized)Windows inside a Docker container.

### On this page

ConfigurationBase64LinksTags