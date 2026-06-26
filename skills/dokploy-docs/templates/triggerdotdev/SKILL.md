---
title: "Trigger.dev | Dokploy"
source: "https://docs.dokploy.com/docs/templates/triggerdotdev"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

Trigger.dev | Dokploy

# Trigger.dev

Copy as Markdown

Trigger is a platform for building event-driven applications.

## Configuration

docker-compose.ymltemplate.toml

```
x-webapp-env: &webapp-env
  LOGIN_ORIGIN: &trigger-url ${TRIGGER_PROTOCOL:-http}://${TRIGGER_DOMAIN:-localhost:3040}
  APP_ORIGIN: *trigger-url
  DEV_OTEL_EXPORTER_OTLP_ENDPOINT: &trigger-otel ${TRIGGER_PROTOCOL:-http}://${TRIGGER_DOMAIN:-localhost:3040}/otel
  ELECTRIC_ORIGIN: http://electric:3000

x-worker-env: &worker-env
  PLATFORM_HOST: webapp
  PLATFORM_WS_PORT: 3030
  SECURE_CONNECTION: "false"
  OTEL_EXPORTER_OTLP_ENDPOINT: *trigger-otel

volumes:
  postgres-data:
  redis-data:

networks:
  webapp:

services:
  webapp:
    image: ghcr.io/triggerdotdev/trigger.dev:${TRIGGER_IMAGE_TAG:-v3}
    restart: ${RESTART_POLICY:-unless-stopped}
    env_file:
      - .env
    environment:
      <<: *webapp-env
    ports:
      - 3000
    depends_on:
      - postgres
      - redis
    networks:
      - webapp

  postgres:
    image: postgres:${POSTGRES_IMAGE_TAG:-16}
    restart: ${RESTART_POLICY:-unless-stopped}
    volumes:
      - postgres-data:/var/lib/postgresql/data/
    env_file:
      - .env
    networks:
      - webapp
    ports:
      - 5432
    command:
      - -c
      - wal_level=logical

  redis:
    image: redis:${REDIS_IMAGE_TAG:-7}
    restart: ${RESTART_POLICY:-unless-stopped}
    volumes:
      - redis-data:/data
    networks:
      - webapp
    ports:
      - 6379

  docker-provider:
    image: ghcr.io/triggerdotdev/provider/docker:${TRIGGER_IMAGE_TAG:-v3}
    restart: ${RESTART_POLICY:-unless-stopped}
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    user: root
    networks:
      - webapp
    depends_on:
      - webapp
    ports:
      - 9020
    env_file:
      - .env
    environment:
      <<: *worker-env
      PLATFORM_SECRET: $PROVIDER_SECRET

  coordinator:
    image: ghcr.io/triggerdotdev/coordinator:${TRIGGER_IMAGE_TAG:-v3}
    restart: ${RESTART_POLICY:-unless-stopped}
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    user: root
    networks:
      - webapp
    depends_on:
      - webapp
    ports:
      - 9020
    env_file:
      - .env
    environment:
      <<: *worker-env
      PLATFORM_SECRET: $COORDINATOR_SECRET

  electric:
    image: electricsql/electric:${ELECTRIC_IMAGE_TAG:-latest}
    restart: ${RESTART_POLICY:-unless-stopped}
    environment:
      DATABASE_URL: ${DATABASE_URL}?sslmode=disable
    networks:
      - webapp
    depends_on:
      - postgres
    ports:
      - 3000
```

```
[variables]
main_domain = "${domain}"
magic_link_secret = "${base64:16}"
session_secret = "${base64:16}"
encryption_key = "${base64:32}"
provider_secret = "${base64:32}"
coordinator_secret = "${base64:32}"
db_password = "${base64:24}"
db_user = "triggeruser"
db_name = "triggerdb"

[config]
mounts = []

[[config.domains]]
serviceName = "webapp"
port = 3_000
host = "${main_domain}"

[config.env]
NODE_ENV = "production"
RUNTIME_PLATFORM = "docker-compose"
V3_ENABLED = "true"
TRIGGER_DOMAIN = "${main_domain}"
TRIGGER_PROTOCOL = "http"
POSTGRES_USER = "${db_user}"
POSTGRES_PASSWORD = "${db_password}"
POSTGRES_DB = "${db_name}"
DATABASE_URL = "postgresql://${db_user}:${db_password}@postgres:5432/${db_name}"
MAGIC_LINK_SECRET = "${magic_link_secret}"
SESSION_SECRET = "${session_secret}"
ENCRYPTION_KEY = "${encryption_key}"
PROVIDER_SECRET = "${provider_secret}"
COORDINATOR_SECRET = "${coordinator_secret}"
INTERNAL_OTEL_TRACE_DISABLED = "1"
INTERNAL_OTEL_TRACE_LOGGING_ENABLED = "0"
DEFAULT_ORG_EXECUTION_CONCURRENCY_LIMIT = "300"
DEFAULT_ENV_EXECUTION_CONCURRENCY_LIMIT = "100"
DIRECT_URL = "${DATABASE_URL}"
REDIS_HOST = "redis"
REDIS_PORT = "6379"
REDIS_TLS_DISABLED = "true"
HTTP_SERVER_PORT = "9020"
COORDINATOR_HOST = "127.0.0.1"
COORDINATOR_PORT = "${HTTP_SERVER_PORT}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIngtd2ViYXBwLWVudjogJndlYmFwcC1lbnZcbiAgTE9HSU5fT1JJR0lOOiAmdHJpZ2dlci11cmwgJHtUUklHR0VSX1BST1RPQ09MOi1odHRwfTovLyR7VFJJR0dFUl9ET01BSU46LWxvY2FsaG9zdDozMDQwfVxuICBBUFBfT1JJR0lOOiAqdHJpZ2dlci11cmxcbiAgREVWX09URUxfRVhQT1JURVJfT1RMUF9FTkRQT0lOVDogJnRyaWdnZXItb3RlbCAke1RSSUdHRVJfUFJPVE9DT0w6LWh0dHB9Oi8vJHtUUklHR0VSX0RPTUFJTjotbG9jYWxob3N0OjMwNDB9L290ZWxcbiAgRUxFQ1RSSUNfT1JJR0lOOiBodHRwOi8vZWxlY3RyaWM6MzAwMFxuXG54LXdvcmtlci1lbnY6ICZ3b3JrZXItZW52XG4gIFBMQVRGT1JNX0hPU1Q6IHdlYmFwcFxuICBQTEFURk9STV9XU19QT1JUOiAzMDMwXG4gIFNFQ1VSRV9DT05ORUNUSU9OOiBcImZhbHNlXCJcbiAgT1RFTF9FWFBPUlRFUl9PVExQX0VORFBPSU5UOiAqdHJpZ2dlci1vdGVsXG5cbnZvbHVtZXM6XG4gIHBvc3RncmVzLWRhdGE6XG4gIHJlZGlzLWRhdGE6XG5cbm5ldHdvcmtzOlxuICB3ZWJhcHA6XG5cbnNlcnZpY2VzOlxuICB3ZWJhcHA6XG4gICAgaW1hZ2U6IGdoY3IuaW8vdHJpZ2dlcmRvdGRldi90cmlnZ2VyLmRldjoke1RSSUdHRVJfSU1BR0VfVEFHOi12M31cbiAgICByZXN0YXJ0OiAke1JFU1RBUlRfUE9MSUNZOi11bmxlc3Mtc3RvcHBlZH1cbiAgICBlbnZfZmlsZTpcbiAgICAgIC0gLmVudlxuICAgIGVudmlyb25tZW50OlxuICAgICAgPDw6ICp3ZWJhcHAtZW52XG4gICAgcG9ydHM6XG4gICAgICAtIDMwMDBcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBwb3N0Z3Jlc1xuICAgICAgLSByZWRpc1xuICAgIG5ldHdvcmtzOlxuICAgICAgLSB3ZWJhcHBcblxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6JHtQT1NUR1JFU19JTUFHRV9UQUc6LTE2fVxuICAgIHJlc3RhcnQ6ICR7UkVTVEFSVF9QT0xJQ1k6LXVubGVzcy1zdG9wcGVkfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvc3RncmVzLWRhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhL1xuICAgIGVudl9maWxlOlxuICAgICAgLSAuZW52XG4gICAgbmV0d29ya3M6XG4gICAgICAtIHdlYmFwcFxuICAgIHBvcnRzOlxuICAgICAgLSA1NDMyXG4gICAgY29tbWFuZDpcbiAgICAgIC0gLWNcbiAgICAgIC0gd2FsX2xldmVsPWxvZ2ljYWxcblxuICByZWRpczpcbiAgICBpbWFnZTogcmVkaXM6JHtSRURJU19JTUFHRV9UQUc6LTd9XG4gICAgcmVzdGFydDogJHtSRVNUQVJUX1BPTElDWTotdW5sZXNzLXN0b3BwZWR9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gcmVkaXMtZGF0YTovZGF0YVxuICAgIG5ldHdvcmtzOlxuICAgICAgLSB3ZWJhcHBcbiAgICBwb3J0czpcbiAgICAgIC0gNjM3OVxuXG4gIGRvY2tlci1wcm92aWRlcjpcbiAgICBpbWFnZTogZ2hjci5pby90cmlnZ2VyZG90ZGV2L3Byb3ZpZGVyL2RvY2tlcjoke1RSSUdHRVJfSU1BR0VfVEFHOi12M31cbiAgICByZXN0YXJ0OiAke1JFU1RBUlRfUE9MSUNZOi11bmxlc3Mtc3RvcHBlZH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSAvdmFyL3J1bi9kb2NrZXIuc29jazovdmFyL3J1bi9kb2NrZXIuc29ja1xuICAgIHVzZXI6IHJvb3RcbiAgICBuZXR3b3JrczpcbiAgICAgIC0gd2ViYXBwXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gd2ViYXBwXG4gICAgcG9ydHM6XG4gICAgICAtIDkwMjBcbiAgICBlbnZfZmlsZTpcbiAgICAgIC0gLmVudlxuICAgIGVudmlyb25tZW50OlxuICAgICAgPDw6ICp3b3JrZXItZW52XG4gICAgICBQTEFURk9STV9TRUNSRVQ6ICRQUk9WSURFUl9TRUNSRVRcblxuICBjb29yZGluYXRvcjpcbiAgICBpbWFnZTogZ2hjci5pby90cmlnZ2VyZG90ZGV2L2Nvb3JkaW5hdG9yOiR7VFJJR0dFUl9JTUFHRV9UQUc6LXYzfVxuICAgIHJlc3RhcnQ6ICR7UkVTVEFSVF9QT0xJQ1k6LXVubGVzcy1zdG9wcGVkfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIC92YXIvcnVuL2RvY2tlci5zb2NrOi92YXIvcnVuL2RvY2tlci5zb2NrXG4gICAgdXNlcjogcm9vdFxuICAgIG5ldHdvcmtzOlxuICAgICAgLSB3ZWJhcHBcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSB3ZWJhcHBcbiAgICBwb3J0czpcbiAgICAgIC0gOTAyMFxuICAgIGVudl9maWxlOlxuICAgICAgLSAuZW52XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICA8PDogKndvcmtlci1lbnZcbiAgICAgIFBMQVRGT1JNX1NFQ1JFVDogJENPT1JESU5BVE9SX1NFQ1JFVFxuXG4gIGVsZWN0cmljOlxuICAgIGltYWdlOiBlbGVjdHJpY3NxbC9lbGVjdHJpYzoke0VMRUNUUklDX0lNQUdFX1RBRzotbGF0ZXN0fVxuICAgIHJlc3RhcnQ6ICR7UkVTVEFSVF9QT0xJQ1k6LXVubGVzcy1zdG9wcGVkfVxuICAgIGVudmlyb25tZW50OlxuICAgICAgREFUQUJBU0VfVVJMOiAke0RBVEFCQVNFX1VSTH0/c3NsbW9kZT1kaXNhYmxlXG4gICAgbmV0d29ya3M6XG4gICAgICAtIHdlYmFwcFxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHBvc3RncmVzXG4gICAgcG9ydHM6XG4gICAgICAtIDMwMDBcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5tYWdpY19saW5rX3NlY3JldCA9IFwiJHtiYXNlNjQ6MTZ9XCJcbnNlc3Npb25fc2VjcmV0ID0gXCIke2Jhc2U2NDoxNn1cIlxuZW5jcnlwdGlvbl9rZXkgPSBcIiR7YmFzZTY0OjMyfVwiXG5wcm92aWRlcl9zZWNyZXQgPSBcIiR7YmFzZTY0OjMyfVwiXG5jb29yZGluYXRvcl9zZWNyZXQgPSBcIiR7YmFzZTY0OjMyfVwiXG5kYl9wYXNzd29yZCA9IFwiJHtiYXNlNjQ6MjR9XCJcbmRiX3VzZXIgPSBcInRyaWdnZXJ1c2VyXCJcbmRiX25hbWUgPSBcInRyaWdnZXJkYlwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ3ZWJhcHBcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuTk9ERV9FTlYgPSBcInByb2R1Y3Rpb25cIlxuUlVOVElNRV9QTEFURk9STSA9IFwiZG9ja2VyLWNvbXBvc2VcIlxuVjNfRU5BQkxFRCA9IFwidHJ1ZVwiXG5UUklHR0VSX0RPTUFJTiA9IFwiJHttYWluX2RvbWFpbn1cIlxuVFJJR0dFUl9QUk9UT0NPTCA9IFwiaHR0cFwiXG5QT1NUR1JFU19VU0VSID0gXCIke2RiX3VzZXJ9XCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiXG5QT1NUR1JFU19EQiA9IFwiJHtkYl9uYW1lfVwiXG5EQVRBQkFTRV9VUkwgPSBcInBvc3RncmVzcWw6Ly8ke2RiX3VzZXJ9OiR7ZGJfcGFzc3dvcmR9QHBvc3RncmVzOjU0MzIvJHtkYl9uYW1lfVwiXG5NQUdJQ19MSU5LX1NFQ1JFVCA9IFwiJHttYWdpY19saW5rX3NlY3JldH1cIlxuU0VTU0lPTl9TRUNSRVQgPSBcIiR7c2Vzc2lvbl9zZWNyZXR9XCJcbkVOQ1JZUFRJT05fS0VZID0gXCIke2VuY3J5cHRpb25fa2V5fVwiXG5QUk9WSURFUl9TRUNSRVQgPSBcIiR7cHJvdmlkZXJfc2VjcmV0fVwiXG5DT09SRElOQVRPUl9TRUNSRVQgPSBcIiR7Y29vcmRpbmF0b3Jfc2VjcmV0fVwiXG5JTlRFUk5BTF9PVEVMX1RSQUNFX0RJU0FCTEVEID0gXCIxXCJcbklOVEVSTkFMX09URUxfVFJBQ0VfTE9HR0lOR19FTkFCTEVEID0gXCIwXCJcbkRFRkFVTFRfT1JHX0VYRUNVVElPTl9DT05DVVJSRU5DWV9MSU1JVCA9IFwiMzAwXCJcbkRFRkFVTFRfRU5WX0VYRUNVVElPTl9DT05DVVJSRU5DWV9MSU1JVCA9IFwiMTAwXCJcbkRJUkVDVF9VUkwgPSBcIiR7REFUQUJBU0VfVVJMfVwiXG5SRURJU19IT1NUID0gXCJyZWRpc1wiXG5SRURJU19QT1JUID0gXCI2Mzc5XCJcblJFRElTX1RMU19ESVNBQkxFRCA9IFwidHJ1ZVwiXG5IVFRQX1NFUlZFUl9QT1JUID0gXCI5MDIwXCJcbkNPT1JESU5BVE9SX0hPU1QgPSBcIjEyNy4wLjAuMVwiXG5DT09SRElOQVRPUl9QT1JUID0gXCIke0hUVFBfU0VSVkVSX1BPUlR9XCJcbiIKfQ==
```

## Links

`event-driven`,`applications`

---

Version:`v3`

TrailBaseTrailBase is a blazingly fast, open-source application server with type-safe APIs, built-in WebAssembly runtime, realtime, auth, and admin UI built on Rust, SQLite & Wasmtime.

TriliumTrilium Notes is a hierarchical note taking application with focus on building large personal knowledge bases.

### On this page

ConfigurationBase64LinksTags