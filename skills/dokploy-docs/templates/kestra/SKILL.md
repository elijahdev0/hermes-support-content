---
title: "Kestra | Dokploy"
source: "https://docs.dokploy.com/docs/templates/kestra"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

Kestra | Dokploy

# Kestra

Copy as Markdown

Unified Orchestration Platform to Simplify Business-Critical Workflows and Govern them as Code and from the UI.

## Configuration

docker-compose.ymltemplate.toml

```
volumes:
  postgres-data:
    driver: local
  kestra-data:
    driver: local

services:
  postgres:
    image: postgres
    volumes:
      - postgres-data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: kestra
      POSTGRES_USER: kestra
      POSTGRES_PASSWORD: k3str4
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -d $${POSTGRES_DB} -U $${POSTGRES_USER}"]
      interval: 30s
      timeout: 10s
      retries: 10

  kestra:
    image: kestra/kestra:latest
    pull_policy: always
    # Note that this setup with a root user is intended for development purpose.
    # Our base image runs without root, but the Docker Compose implementation needs root to access the Docker socket
    # To run Kestra in a rootless mode in production, see: https://kestra.io/docs/installation/podman-compose
    user: "root"
    command: server standalone
    volumes:
      - kestra-data:/app/storage
      - /var/run/docker.sock:/var/run/docker.sock
      - /tmp/kestra-wd:/tmp/kestra-wd
    environment:
      KESTRA_CONFIGURATION: |
        datasources:
          postgres:
            url: jdbc:postgresql://postgres:5432/kestra
            driverClassName: org.postgresql.Driver
            username: kestra
            password: k3str4
        kestra:
          server:
            basicAuth:
              enabled: false
              username: "[email protected]" # it must be a valid email address
              password: k3str4p@ss
          repository:
            type: postgres
          storage:
            type: local
            local:
              basePath: "/app/storage"
          queue:
            type: postgres
          tasks:
            tmpDir:
              path: /tmp/kestra-wd/tmp
          url: http://localhost:8080/
    ports:
      - "8080"
      - "8081"
    depends_on:
      postgres:
        condition: service_started
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "kestra"
port = 8080
host = "${main_domain}"

[config.env]

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZvbHVtZXM6XG4gIHBvc3RncmVzLWRhdGE6XG4gICAgZHJpdmVyOiBsb2NhbFxuICBrZXN0cmEtZGF0YTpcbiAgICBkcml2ZXI6IGxvY2FsXG5cbnNlcnZpY2VzOlxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlcy1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6IGtlc3RyYVxuICAgICAgUE9TVEdSRVNfVVNFUjoga2VzdHJhXG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogazNzdHI0XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5IC1kICQke1BPU1RHUkVTX0RCfSAtVSAkJHtQT1NUR1JFU19VU0VSfVwiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAxMFxuXG4gIGtlc3RyYTpcbiAgICBpbWFnZToga2VzdHJhL2tlc3RyYTpsYXRlc3RcbiAgICBwdWxsX3BvbGljeTogYWx3YXlzXG4gICAgIyBOb3RlIHRoYXQgdGhpcyBzZXR1cCB3aXRoIGEgcm9vdCB1c2VyIGlzIGludGVuZGVkIGZvciBkZXZlbG9wbWVudCBwdXJwb3NlLlxuICAgICMgT3VyIGJhc2UgaW1hZ2UgcnVucyB3aXRob3V0IHJvb3QsIGJ1dCB0aGUgRG9ja2VyIENvbXBvc2UgaW1wbGVtZW50YXRpb24gbmVlZHMgcm9vdCB0byBhY2Nlc3MgdGhlIERvY2tlciBzb2NrZXRcbiAgICAjIFRvIHJ1biBLZXN0cmEgaW4gYSByb290bGVzcyBtb2RlIGluIHByb2R1Y3Rpb24sIHNlZTogaHR0cHM6Ly9rZXN0cmEuaW8vZG9jcy9pbnN0YWxsYXRpb24vcG9kbWFuLWNvbXBvc2VcbiAgICB1c2VyOiBcInJvb3RcIlxuICAgIGNvbW1hbmQ6IHNlcnZlciBzdGFuZGFsb25lXG4gICAgdm9sdW1lczpcbiAgICAgIC0ga2VzdHJhLWRhdGE6L2FwcC9zdG9yYWdlXG4gICAgICAtIC92YXIvcnVuL2RvY2tlci5zb2NrOi92YXIvcnVuL2RvY2tlci5zb2NrXG4gICAgICAtIC90bXAva2VzdHJhLXdkOi90bXAva2VzdHJhLXdkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBLRVNUUkFfQ09ORklHVVJBVElPTjogfFxuICAgICAgICBkYXRhc291cmNlczpcbiAgICAgICAgICBwb3N0Z3JlczpcbiAgICAgICAgICAgIHVybDogamRiYzpwb3N0Z3Jlc3FsOi8vcG9zdGdyZXM6NTQzMi9rZXN0cmFcbiAgICAgICAgICAgIGRyaXZlckNsYXNzTmFtZTogb3JnLnBvc3RncmVzcWwuRHJpdmVyXG4gICAgICAgICAgICB1c2VybmFtZToga2VzdHJhXG4gICAgICAgICAgICBwYXNzd29yZDogazNzdHI0XG4gICAgICAgIGtlc3RyYTpcbiAgICAgICAgICBzZXJ2ZXI6XG4gICAgICAgICAgICBiYXNpY0F1dGg6XG4gICAgICAgICAgICAgIGVuYWJsZWQ6IGZhbHNlXG4gICAgICAgICAgICAgIHVzZXJuYW1lOiBcImFkbWluQGxvY2FsaG9zdC5kZXZcIiAjIGl0IG11c3QgYmUgYSB2YWxpZCBlbWFpbCBhZGRyZXNzXG4gICAgICAgICAgICAgIHBhc3N3b3JkOiBrM3N0cjRwQHNzXG4gICAgICAgICAgcmVwb3NpdG9yeTpcbiAgICAgICAgICAgIHR5cGU6IHBvc3RncmVzXG4gICAgICAgICAgc3RvcmFnZTpcbiAgICAgICAgICAgIHR5cGU6IGxvY2FsXG4gICAgICAgICAgICBsb2NhbDpcbiAgICAgICAgICAgICAgYmFzZVBhdGg6IFwiL2FwcC9zdG9yYWdlXCJcbiAgICAgICAgICBxdWV1ZTpcbiAgICAgICAgICAgIHR5cGU6IHBvc3RncmVzXG4gICAgICAgICAgdGFza3M6XG4gICAgICAgICAgICB0bXBEaXI6XG4gICAgICAgICAgICAgIHBhdGg6IC90bXAva2VzdHJhLXdkL3RtcFxuICAgICAgICAgIHVybDogaHR0cDovL2xvY2FsaG9zdDo4MDgwL1xuICAgIHBvcnRzOlxuICAgICAgLSBcIjgwODBcIlxuICAgICAgLSBcIjgwODFcIlxuICAgIGRlcGVuZHNfb246XG4gICAgICBwb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX3N0YXJ0ZWRcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJrZXN0cmFcIlxucG9ydCA9IDgwODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuXG5bY29uZmlnLmVudl1cblxuW1tjb25maWcubW91bnRzXV1cbiIKfQ==
```

## Links

`automation`

---

Version:`latest`

KenerKener is an open-source status page system for monitoring and alerting. It provides a modern interface for tracking service uptime and sending notifications.

KeycloakKeycloak is an open source Identity and Access Management solution for modern applications and services.

### On this page

ConfigurationBase64LinksTags