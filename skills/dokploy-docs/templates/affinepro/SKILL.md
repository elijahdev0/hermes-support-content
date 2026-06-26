---
title: "Affine Pro | Dokploy"
source: "https://docs.dokploy.com/docs/templates/affinepro"
category: dokploy-docs
created: "2026-06-25T17:21:40.414Z"
---

Affine Pro | Dokploy

# Affine Pro

Copy as Markdown

Affine Pro is a modern, self-hosted platform designed for collaborative content creation and project management. It offers an intuitive interface, seamless real-time collaboration, and powerful tools for organizing tasks, notes, and ideas.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  affinepro:
    image: ghcr.io/toeverything/affine-graphql:stable-780dd83
    restart: unless-stopped
    ports:
      - 3010
    volumes:
      - affine-storage:/root/.affine/storage
      - affine-config:/root/.affine/config
    environment:
      - REDIS_SERVER_HOST=redis
      - REDIS_SERVER_PASSWORD=${REDIS_PASSWORD}
      - DATABASE_URL=postgresql://postgres:${POSTGRES_PASSWORD}@db:5432/affinepro
      - AFFINE_SERVER_HOST=${DOMAIN}
      - MAILER_HOST=${MAILER_HOST}
      - MAILER_PORT=${MAILER_PORT}
      - MAILER_USER=${MAILER_USER}
      - MAILER_PASSWORD=${MAILER_PASSWORD}
      - MAILER_SENDER=${MAILER_SENDER}
    depends_on:
      - db
      - redis

  migration:
    image: ghcr.io/toeverything/affine-graphql:stable-780dd83
    command: node ./scripts/self-host-predeploy.js
    environment:
      - REDIS_SERVER_HOST=redis
      - REDIS_SERVER_PASSWORD=${REDIS_PASSWORD}
      - DATABASE_URL=postgresql://postgres:${POSTGRES_PASSWORD}@db:5432/affinepro
      - AFFINE_SERVER_HOST=${DOMAIN}
      - MAILER_HOST=${MAILER_HOST}
      - MAILER_PORT=${MAILER_PORT}
      - MAILER_USER=${MAILER_USER}
      - MAILER_PASSWORD=${MAILER_PASSWORD}
      - MAILER_SENDER=${MAILER_SENDER}
    volumes:
      - affine-storage:/root/.affine/storage
      - affine-config:/root/.affine/config
    depends_on:
      - db
      - redis

  db:
    image: postgres:15-alpine
    restart: unless-stopped
    environment:
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=affinepro
    volumes:
      - postgres-data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis-data:/data

volumes:
  affine-storage: {}
  affine-config: {}
  postgres-data: {}
  redis-data: {}
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password:16}"
redis_password = "${password:16}"
mailer_host = ""
mailer_port = "587"
mailer_user = ""
mailer_password = ""
mailer_sender = ""

[config]
[[config.domains]]
serviceName = "affinepro"
port = 3010
host = "${main_domain}"

[config.env]
DOMAIN = "${main_domain}"
POSTGRES_PASSWORD = "${postgres_password}"
REDIS_PASSWORD = "${redis_password}"
MAILER_HOST = "${mailer_host}"
MAILER_PORT = "${mailer_port}"
MAILER_USER = "${mailer_user}"
MAILER_PASSWORD = "${mailer_password}"
MAILER_SENDER = "${mailer_sender}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhZmZpbmVwcm86XG4gICAgaW1hZ2U6IGdoY3IuaW8vdG9ldmVyeXRoaW5nL2FmZmluZS1ncmFwaHFsOnN0YWJsZS03ODBkZDgzXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gMzAxMFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGFmZmluZS1zdG9yYWdlOi9yb290Ly5hZmZpbmUvc3RvcmFnZVxuICAgICAgLSBhZmZpbmUtY29uZmlnOi9yb290Ly5hZmZpbmUvY29uZmlnXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFJFRElTX1NFUlZFUl9IT1NUPXJlZGlzXG4gICAgICAtIFJFRElTX1NFUlZFUl9QQVNTV09SRD0ke1JFRElTX1BBU1NXT1JEfVxuICAgICAgLSBEQVRBQkFTRV9VUkw9cG9zdGdyZXNxbDovL3Bvc3RncmVzOiR7UE9TVEdSRVNfUEFTU1dPUkR9QGRiOjU0MzIvYWZmaW5lcHJvXG4gICAgICAtIEFGRklORV9TRVJWRVJfSE9TVD0ke0RPTUFJTn1cbiAgICAgIC0gTUFJTEVSX0hPU1Q9JHtNQUlMRVJfSE9TVH1cbiAgICAgIC0gTUFJTEVSX1BPUlQ9JHtNQUlMRVJfUE9SVH1cbiAgICAgIC0gTUFJTEVSX1VTRVI9JHtNQUlMRVJfVVNFUn1cbiAgICAgIC0gTUFJTEVSX1BBU1NXT1JEPSR7TUFJTEVSX1BBU1NXT1JEfVxuICAgICAgLSBNQUlMRVJfU0VOREVSPSR7TUFJTEVSX1NFTkRFUn1cbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBkYlxuICAgICAgLSByZWRpc1xuXG4gIG1pZ3JhdGlvbjpcbiAgICBpbWFnZTogZ2hjci5pby90b2V2ZXJ5dGhpbmcvYWZmaW5lLWdyYXBocWw6c3RhYmxlLTc4MGRkODNcbiAgICBjb21tYW5kOiBub2RlIC4vc2NyaXB0cy9zZWxmLWhvc3QtcHJlZGVwbG95LmpzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFJFRElTX1NFUlZFUl9IT1NUPXJlZGlzXG4gICAgICAtIFJFRElTX1NFUlZFUl9QQVNTV09SRD0ke1JFRElTX1BBU1NXT1JEfVxuICAgICAgLSBEQVRBQkFTRV9VUkw9cG9zdGdyZXNxbDovL3Bvc3RncmVzOiR7UE9TVEdSRVNfUEFTU1dPUkR9QGRiOjU0MzIvYWZmaW5lcHJvXG4gICAgICAtIEFGRklORV9TRVJWRVJfSE9TVD0ke0RPTUFJTn1cbiAgICAgIC0gTUFJTEVSX0hPU1Q9JHtNQUlMRVJfSE9TVH1cbiAgICAgIC0gTUFJTEVSX1BPUlQ9JHtNQUlMRVJfUE9SVH1cbiAgICAgIC0gTUFJTEVSX1VTRVI9JHtNQUlMRVJfVVNFUn1cbiAgICAgIC0gTUFJTEVSX1BBU1NXT1JEPSR7TUFJTEVSX1BBU1NXT1JEfVxuICAgICAgLSBNQUlMRVJfU0VOREVSPSR7TUFJTEVSX1NFTkRFUn1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBhZmZpbmUtc3RvcmFnZTovcm9vdC8uYWZmaW5lL3N0b3JhZ2VcbiAgICAgIC0gYWZmaW5lLWNvbmZpZzovcm9vdC8uYWZmaW5lL2NvbmZpZ1xuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGRiXG4gICAgICAtIHJlZGlzXG5cbiAgZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE1LWFscGluZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPSR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICAtIFBPU1RHUkVTX0RCPWFmZmluZXByb1xuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvc3RncmVzLWRhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG5cbiAgcmVkaXM6XG4gICAgaW1hZ2U6IHJlZGlzOjctYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBjb21tYW5kOiByZWRpcy1zZXJ2ZXIgLS1yZXF1aXJlcGFzcyAke1JFRElTX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHJlZGlzLWRhdGE6L2RhdGFcblxudm9sdW1lczpcbiAgYWZmaW5lLXN0b3JhZ2U6IHt9XG4gIGFmZmluZS1jb25maWc6IHt9XG4gIHBvc3RncmVzLWRhdGE6IHt9XG4gIHJlZGlzLWRhdGE6IHt9ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoxNn1cIlxucmVkaXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbm1haWxlcl9ob3N0ID0gXCJcIlxubWFpbGVyX3BvcnQgPSBcIjU4N1wiXG5tYWlsZXJfdXNlciA9IFwiXCJcbm1haWxlcl9wYXNzd29yZCA9IFwiXCJcbm1haWxlcl9zZW5kZXIgPSBcIlwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhZmZpbmVwcm9cIlxucG9ydCA9IDMwMTBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5ET01BSU4gPSBcIiR7bWFpbl9kb21haW59XCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bvc3RncmVzX3Bhc3N3b3JkfVwiXG5SRURJU19QQVNTV09SRCA9IFwiJHtyZWRpc19wYXNzd29yZH1cIlxuTUFJTEVSX0hPU1QgPSBcIiR7bWFpbGVyX2hvc3R9XCJcbk1BSUxFUl9QT1JUID0gXCIke21haWxlcl9wb3J0fVwiXG5NQUlMRVJfVVNFUiA9IFwiJHttYWlsZXJfdXNlcn1cIlxuTUFJTEVSX1BBU1NXT1JEID0gXCIke21haWxlcl9wYXNzd29yZH1cIlxuTUFJTEVSX1NFTkRFUiA9IFwiJHttYWlsZXJfc2VuZGVyfVwiICIKfQ==
```

## Links

`collaboration`,`self-hosted`,`productivity`,`project-management`

---

Version:`stable-780dd83`

AdventureLogAdventureLog is an open-source activity tracker with maps, journaling, and Strava integration.

Agent DVRAgent DVR is a comprehensive video surveillance software with motion detection, alerts, and remote access capabilities.

### On this page

ConfigurationBase64LinksTags