---
title: "Unleash | Dokploy"
source: "https://docs.dokploy.com/docs/templates/unleash"
category: dokploy-docs
created: "2026-06-25T17:22:01.419Z"
---

Unleash | Dokploy

# Unleash

Copy as Markdown

Open-source feature management platform

## Configuration

docker-compose.ymltemplate.toml

```
# The default users credentials are:
# Login: admin
# Password: unleash4all
# It is highly recommended to change the password after first login.
# More info: https://github.com/Unleash/unleash?tab=readme-ov-file#unleash-open-source
version: "3.8"

services:
  unleash:
    image: unleashorg/unleash-server:7.4.0
    restart: unless-stopped
    environment:
      DATABASE_URL: "postgres://${DB_USER}:${DB_PASSWORD}@db/${DB_NAME}"
      DATABASE_SSL: "false"
      LOG_LEVEL: "warn"
    depends_on:
      db:
        condition: service_healthy
    healthcheck:
      test: wget --no-verbose --tries=1 --spider http://localhost:4242/health || exit 1
      interval: 1s
      timeout: 1m
      retries: 5
      start_period: 15s
  db:
    image: postgres:15
    restart: unless-stopped
    environment:
      POSTGRES_DB: "${DB_NAME}"
      POSTGRES_USER: "${DB_USER}"
      POSTGRES_PASSWORD: "${DB_PASSWORD}"
    volumes:
      - db_data:/var/lib/postgresql/data
    healthcheck:
      test:
        [
          "CMD",
          "pg_isready",
          "--username=${DB_USER}",
          "--host=127.0.0.1",
          "--port=5432",
        ]
      interval: 2s
      timeout: 1m
      retries: 5
      start_period: 10s

volumes:
  db_data:
```

```
[variables]
main_domain = "${domain}"
db_name = "unleash"
db_user = "unleash"
db_password = "${password:32}"

[config]
env = [
  "DB_NAME=${db_name}",
  "DB_USER=${db_user}",
  "DB_PASSWORD=${db_password}"
]

[[config.domains]]
serviceName = "unleash"
port = 4242
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgVGhlIGRlZmF1bHQgdXNlcnMgY3JlZGVudGlhbHMgYXJlOlxuIyBMb2dpbjogYWRtaW5cbiMgUGFzc3dvcmQ6IHVubGVhc2g0YWxsXG4jIEl0IGlzIGhpZ2hseSByZWNvbW1lbmRlZCB0byBjaGFuZ2UgdGhlIHBhc3N3b3JkIGFmdGVyIGZpcnN0IGxvZ2luLlxuIyBNb3JlIGluZm86IGh0dHBzOi8vZ2l0aHViLmNvbS9VbmxlYXNoL3VubGVhc2g/dGFiPXJlYWRtZS1vdi1maWxlI3VubGVhc2gtb3Blbi1zb3VyY2VcbnZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHVubGVhc2g6XG4gICAgaW1hZ2U6IHVubGVhc2hvcmcvdW5sZWFzaC1zZXJ2ZXI6Ny40LjBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgREFUQUJBU0VfVVJMOiBcInBvc3RncmVzOi8vJHtEQl9VU0VSfToke0RCX1BBU1NXT1JEfUBkYi8ke0RCX05BTUV9XCJcbiAgICAgIERBVEFCQVNFX1NTTDogXCJmYWxzZVwiXG4gICAgICBMT0dfTEVWRUw6IFwid2FyblwiXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGRiOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogd2dldCAtLW5vLXZlcmJvc2UgLS10cmllcz0xIC0tc3BpZGVyIGh0dHA6Ly9sb2NhbGhvc3Q6NDI0Mi9oZWFsdGggfHwgZXhpdCAxXG4gICAgICBpbnRlcnZhbDogMXNcbiAgICAgIHRpbWVvdXQ6IDFtXG4gICAgICByZXRyaWVzOiA1XG4gICAgICBzdGFydF9wZXJpb2Q6IDE1c1xuICBkYjpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6IFwiJHtEQl9OQU1FfVwiXG4gICAgICBQT1NUR1JFU19VU0VSOiBcIiR7REJfVVNFUn1cIlxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6IFwiJHtEQl9QQVNTV09SRH1cIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRiX2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICBbXG4gICAgICAgICAgXCJDTURcIixcbiAgICAgICAgICBcInBnX2lzcmVhZHlcIixcbiAgICAgICAgICBcIi0tdXNlcm5hbWU9JHtEQl9VU0VSfVwiLFxuICAgICAgICAgIFwiLS1ob3N0PTEyNy4wLjAuMVwiLFxuICAgICAgICAgIFwiLS1wb3J0PTU0MzJcIixcbiAgICAgICAgXVxuICAgICAgaW50ZXJ2YWw6IDJzXG4gICAgICB0aW1lb3V0OiAxbVxuICAgICAgcmV0cmllczogNVxuICAgICAgc3RhcnRfcGVyaW9kOiAxMHNcblxudm9sdW1lczpcbiAgZGJfZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5kYl9uYW1lID0gXCJ1bmxlYXNoXCJcbmRiX3VzZXIgPSBcInVubGVhc2hcIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJEQl9OQU1FPSR7ZGJfbmFtZX1cIixcbiAgXCJEQl9VU0VSPSR7ZGJfdXNlcn1cIixcbiAgXCJEQl9QQVNTV09SRD0ke2RiX3Bhc3N3b3JkfVwiXG5dXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInVubGVhc2hcIlxucG9ydCA9IDQyNDJcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCIiCn0=
```

## Links

`feature-flag`,`feature-management`,`feature-toggle`,`remote-configuration`

---

Version:`7.4.0`

Unifi NetworkUnifi Network is an open-source enterprise network management platform for wireless networks.

UpsnapUpsnap is a simple network device monitor and dashboard built on PocketBase.

### On this page

ConfigurationBase64LinksTags