---
title: "InstantDB | Dokploy"
source: "https://docs.dokploy.com/docs/templates/instantdb"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

InstantDB | Dokploy

# InstantDB

Copy as Markdown

InstantDB is a real-time database server that provides instant data synchronization and real-time updates for applications.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  postgres:
    image: ghcr.io/instantdb/postgresql:postgresql-16-pg-hint-plan
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - backend-db:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "${POSTGRES_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5
    command:
      - "postgres"
      - "-c"
      - "wal_level=logical"
      - "-c"
      - "max_replication_slots=4"
      - "-c"
      - "max_wal_senders=4"
      - "-c"
      - "shared_preload_libraries=pg_hint_plan"
      - "-c"
      - "random_page_cost=1.1"
  server:
    depends_on:
      postgres:
        condition: service_healthy
    image: hari1367709/instantdb-server:latest
    restart: unless-stopped
    working_dir: /app
    environment:
      DATABASE_URL: "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}"
      NREPL_BIND_ADDRESS: "0.0.0.0"
      PORT: "8888"
      HOST: "0.0.0.0"
      # AWS Credentials for KMS (required for InstantDB)
      AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID}
      AWS_SECRET_ACCESS_KEY: ${AWS_SECRET_ACCESS_KEY}
      AWS_REGION: ${AWS_REGION:-us-east-1}
      # Force unbuffered output for logs
      PYTHONUNBUFFERED: "1"
      NODE_ENV: "production"
    command: ["java", "-Djava.awt.headless=true", "-server", "-jar", "target/instant-standalone.jar"]
    ports:
      - "8888"
      - "6005"
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost:8888/health || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
volumes:
  backend-db:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password:32}"
postgres_user = "instant"
postgres_db = "instant"
aws_access_key_id = "FILL-YOUR-CREDENTIALS"
aws_secret_access_key = "FILL-YOUR-CREDENTIALS"
aws_region = "us-east-1"

[config]
env = [
  "POSTGRES_PASSWORD=${postgres_password}",
  "POSTGRES_USER=${postgres_user}",
  "POSTGRES_DB=${postgres_db}",
  "DATABASE_URL=postgresql://${postgres_user}:${postgres_password}@postgres:5432/${postgres_db}",
  "NREPL_BIND_ADDRESS=0.0.0.0",
  "PORT=8888",
  "HOST=0.0.0.0",
  "AWS_ACCESS_KEY_ID=${aws_access_key_id}",
  "AWS_SECRET_ACCESS_KEY=${aws_secret_access_key}",
  "AWS_REGION=${aws_region}",
]
mounts = []

[[config.domains]]
serviceName = "server"
port = 8888
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogZ2hjci5pby9pbnN0YW50ZGIvcG9zdGdyZXNxbDpwb3N0Z3Jlc3FsLTE2LXBnLWhpbnQtcGxhblxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIFBPU1RHUkVTX1VTRVI6ICR7UE9TVEdSRVNfVVNFUn1cbiAgICAgIFBPU1RHUkVTX0RCOiAke1BPU1RHUkVTX0RCfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGJhY2tlbmQtZGI6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJwZ19pc3JlYWR5XCIsIFwiLVVcIiwgXCIke1BPU1RHUkVTX1VTRVJ9XCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgIGNvbW1hbmQ6XG4gICAgICAtIFwicG9zdGdyZXNcIlxuICAgICAgLSBcIi1jXCJcbiAgICAgIC0gXCJ3YWxfbGV2ZWw9bG9naWNhbFwiXG4gICAgICAtIFwiLWNcIlxuICAgICAgLSBcIm1heF9yZXBsaWNhdGlvbl9zbG90cz00XCJcbiAgICAgIC0gXCItY1wiXG4gICAgICAtIFwibWF4X3dhbF9zZW5kZXJzPTRcIlxuICAgICAgLSBcIi1jXCJcbiAgICAgIC0gXCJzaGFyZWRfcHJlbG9hZF9saWJyYXJpZXM9cGdfaGludF9wbGFuXCJcbiAgICAgIC0gXCItY1wiXG4gICAgICAtIFwicmFuZG9tX3BhZ2VfY29zdD0xLjFcIlxuICBzZXJ2ZXI6XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHBvc3RncmVzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGltYWdlOiBoYXJpMTM2NzcwOS9pbnN0YW50ZGItc2VydmVyOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgd29ya2luZ19kaXI6IC9hcHBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERBVEFCQVNFX1VSTDogXCJwb3N0Z3Jlc3FsOi8vJHtQT1NUR1JFU19VU0VSfToke1BPU1RHUkVTX1BBU1NXT1JEfUBwb3N0Z3Jlczo1NDMyLyR7UE9TVEdSRVNfREJ9XCJcbiAgICAgIE5SRVBMX0JJTkRfQUREUkVTUzogXCIwLjAuMC4wXCJcbiAgICAgIFBPUlQ6IFwiODg4OFwiXG4gICAgICBIT1NUOiBcIjAuMC4wLjBcIlxuICAgICAgIyBBV1MgQ3JlZGVudGlhbHMgZm9yIEtNUyAocmVxdWlyZWQgZm9yIEluc3RhbnREQilcbiAgICAgIEFXU19BQ0NFU1NfS0VZX0lEOiAke0FXU19BQ0NFU1NfS0VZX0lEfVxuICAgICAgQVdTX1NFQ1JFVF9BQ0NFU1NfS0VZOiAke0FXU19TRUNSRVRfQUNDRVNTX0tFWX1cbiAgICAgIEFXU19SRUdJT046ICR7QVdTX1JFR0lPTjotdXMtZWFzdC0xfVxuICAgICAgIyBGb3JjZSB1bmJ1ZmZlcmVkIG91dHB1dCBmb3IgbG9nc1xuICAgICAgUFlUSE9OVU5CVUZGRVJFRDogXCIxXCJcbiAgICAgIE5PREVfRU5WOiBcInByb2R1Y3Rpb25cIlxuICAgIGNvbW1hbmQ6IFtcImphdmFcIiwgXCItRGphdmEuYXd0LmhlYWRsZXNzPXRydWVcIiwgXCItc2VydmVyXCIsIFwiLWphclwiLCBcInRhcmdldC9pbnN0YW50LXN0YW5kYWxvbmUuamFyXCJdXG4gICAgcG9ydHM6XG4gICAgICAtIFwiODg4OFwiXG4gICAgICAtIFwiNjAwNVwiXG4gICAgbG9nZ2luZzpcbiAgICAgIGRyaXZlcjogXCJqc29uLWZpbGVcIlxuICAgICAgb3B0aW9uczpcbiAgICAgICAgbWF4LXNpemU6IFwiMTBtXCJcbiAgICAgICAgbWF4LWZpbGU6IFwiM1wiXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJjdXJsIC1mIGh0dHA6Ly9sb2NhbGhvc3Q6ODg4OC9oZWFsdGggfHwgZXhpdCAxXCJdXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDNcbiAgICAgIHN0YXJ0X3BlcmlvZDogNDBzXG52b2x1bWVzOlxuICBiYWNrZW5kLWRiOlxuXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbnBvc3RncmVzX3VzZXIgPSBcImluc3RhbnRcIlxucG9zdGdyZXNfZGIgPSBcImluc3RhbnRcIlxuYXdzX2FjY2Vzc19rZXlfaWQgPSBcIkZJTEwtWU9VUi1DUkVERU5USUFMU1wiXG5hd3Nfc2VjcmV0X2FjY2Vzc19rZXkgPSBcIkZJTEwtWU9VUi1DUkVERU5USUFMU1wiXG5hd3NfcmVnaW9uID0gXCJ1cy1lYXN0LTFcIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICBcIlBPU1RHUkVTX1BBU1NXT1JEPSR7cG9zdGdyZXNfcGFzc3dvcmR9XCIsXG4gIFwiUE9TVEdSRVNfVVNFUj0ke3Bvc3RncmVzX3VzZXJ9XCIsXG4gIFwiUE9TVEdSRVNfREI9JHtwb3N0Z3Jlc19kYn1cIixcbiAgXCJEQVRBQkFTRV9VUkw9cG9zdGdyZXNxbDovLyR7cG9zdGdyZXNfdXNlcn06JHtwb3N0Z3Jlc19wYXNzd29yZH1AcG9zdGdyZXM6NTQzMi8ke3Bvc3RncmVzX2RifVwiLFxuICBcIk5SRVBMX0JJTkRfQUREUkVTUz0wLjAuMC4wXCIsXG4gIFwiUE9SVD04ODg4XCIsXG4gIFwiSE9TVD0wLjAuMC4wXCIsXG4gIFwiQVdTX0FDQ0VTU19LRVlfSUQ9JHthd3NfYWNjZXNzX2tleV9pZH1cIixcbiAgXCJBV1NfU0VDUkVUX0FDQ0VTU19LRVk9JHthd3Nfc2VjcmV0X2FjY2Vzc19rZXl9XCIsXG4gIFwiQVdTX1JFR0lPTj0ke2F3c19yZWdpb259XCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJzZXJ2ZXJcIlxucG9ydCA9IDg4ODhcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuIgp9
```

## Links

`database`,`real-time`,`self-hosted`

---

Version:`latest`

InngestInngest is a developer platform for serverless event-driven workflows. Build reliable, scalable background functions and workflows with built-in retries, scheduling, and observability.

InvoiceShelfInvoiceShelf is a self-hosted open source invoicing system for freelancers and small businesses.

### On this page

ConfigurationBase64LinksTags