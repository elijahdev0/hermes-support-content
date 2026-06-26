---
title: "Commento | Dokploy"
source: "https://docs.dokploy.com/docs/templates/commento"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

Commento | Dokploy

# Commento

Copy as Markdown

Commento is a comments widget designed to enhance the interaction on your website. It allows your readers to contribute to the discussion by upvoting comments that add value and downvoting those that don't. The widget supports markdown formatting and provides moderation tools to manage conversations.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  commento:
    image: registry.gitlab.com/commento/commento:v1.8.0
    ports:
      - "8080"
    environment:
      - COMMENTO_ORIGIN=${COMMENTO_ORIGIN}
      - COMMENTO_POSTGRES=${COMMENTO_POSTGRES}
    depends_on:
      - postgres

  postgres:
    image: postgres:11
    environment:
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    volumes:
      - postgres-data:/var/lib/postgresql/data

volumes:
  postgres-data:
```

```
[variables]
DOMAIN = "${domain}"
POSTGRES_PASSWORD = "${password:16}"

[config]
[[config.domains]]
serviceName = "commento"
port = 8080
host = "${DOMAIN}"

[config.env]
COMMENTO_ORIGIN = "http://${DOMAIN}"
COMMENTO_POSTGRES = "postgres://postgres:${POSTGRES_PASSWORD}@postgres:5432/postgres?sslmode=disable"
POSTGRES_PASSWORD = "${POSTGRES_PASSWORD}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBjb21tZW50bzpcbiAgICBpbWFnZTogcmVnaXN0cnkuZ2l0bGFiLmNvbS9jb21tZW50by9jb21tZW50bzp2MS44LjBcbiAgICBwb3J0czpcbiAgICAgIC0gXCI4MDgwXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQ09NTUVOVE9fT1JJR0lOPSR7Q09NTUVOVE9fT1JJR0lOfVxuICAgICAgLSBDT01NRU5UT19QT1NUR1JFUz0ke0NPTU1FTlRPX1BPU1RHUkVTfVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHBvc3RncmVzXG5cbiAgcG9zdGdyZXM6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjExXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPSR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gcG9zdGdyZXMtZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcblxudm9sdW1lczpcbiAgcG9zdGdyZXMtZGF0YTogIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5ET01BSU4gPSBcIiR7ZG9tYWlufVwiXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtwYXNzd29yZDoxNn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY29tbWVudG9cIlxucG9ydCA9IDgwODBcbmhvc3QgPSBcIiR7RE9NQUlOfVwiXG5cbltjb25maWcuZW52XVxuQ09NTUVOVE9fT1JJR0lOID0gXCJodHRwOi8vJHtET01BSU59XCJcbkNPTU1FTlRPX1BPU1RHUkVTID0gXCJwb3N0Z3JlczovL3Bvc3RncmVzOiR7UE9TVEdSRVNfUEFTU1dPUkR9QHBvc3RncmVzOjU0MzIvcG9zdGdyZXM/c3NsbW9kZT1kaXNhYmxlXCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke1BPU1RHUkVTX1BBU1NXT1JEfVwiICIKfQ==
```

## Links

`comments`,`discussion`,`website`

---

Version:`v1.8.0`

CommaFeedCommaFeed is an open-source feed reader and news aggregator, designed to be lightweight and extensible, with PostgreSQL as its database.

Commento++Commento++ is a free, open-source application designed to provide a fast, lightweight comments box that you can embed in your static website. It offers features like Markdown support, Disqus import, voting, automated spam detection, moderation tools, sticky comments, thread locking, and OAuth login.

### On this page

ConfigurationBase64LinksTags