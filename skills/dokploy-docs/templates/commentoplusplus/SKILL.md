---
title: "Commento++ | Dokploy"
source: "https://docs.dokploy.com/docs/templates/commentoplusplus"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

Commento++ | Dokploy

# Commento++

Copy as Markdown

Commento++ is a free, open-source application designed to provide a fast, lightweight comments box that you can embed in your static website. It offers features like Markdown support, Disqus import, voting, automated spam detection, moderation tools, sticky comments, thread locking, and OAuth login.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  commentoplusplus:
    image: caroga/commentoplusplus:v1.8.7
    ports:
      - "8080"
    environment:
      - COMMENTO_ORIGIN=${COMMENTO_ORIGIN}
      - COMMENTO_POSTGRES=${COMMENTO_POSTGRES}
      - COMMENTO_ENABLE_WILDCARDS=true
    depends_on:
      - postgres

  postgres:
    image: postgres:11
    environment:
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
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
serviceName = "commentoplusplus"
port = 8080
host = "${DOMAIN}"

[config.env]
COMMENTO_ORIGIN = "http://${DOMAIN}"
COMMENTO_POSTGRES = "postgres://postgres:${POSTGRES_PASSWORD}@postgres:5432/postgres?sslmode=disable"
COMMENTO_ENABLE_WILDCARDS = "true"
POSTGRES_PASSWORD = "${POSTGRES_PASSWORD}"
POSTGRES_DB = "postgres"
POSTGRES_USER = "postgres"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBjb21tZW50b3BsdXNwbHVzOlxuICAgIGltYWdlOiBjYXJvZ2EvY29tbWVudG9wbHVzcGx1czp2MS44LjdcbiAgICBwb3J0czpcbiAgICAgIC0gXCI4MDgwXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQ09NTUVOVE9fT1JJR0lOPSR7Q09NTUVOVE9fT1JJR0lOfVxuICAgICAgLSBDT01NRU5UT19QT1NUR1JFUz0ke0NPTU1FTlRPX1BPU1RHUkVTfVxuICAgICAgLSBDT01NRU5UT19FTkFCTEVfV0lMRENBUkRTPXRydWVcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBwb3N0Z3Jlc1xuXG4gIHBvc3RncmVzOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxMVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgLSBQT1NUR1JFU19EQj0ke1BPU1RHUkVTX0RCfVxuICAgICAgLSBQT1NUR1JFU19VU0VSPSR7UE9TVEdSRVNfVVNFUn1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlcy1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuXG52b2x1bWVzOlxuICBwb3N0Z3Jlcy1kYXRhOiAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbkRPTUFJTiA9IFwiJHtkb21haW59XCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjb21tZW50b3BsdXNwbHVzXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke0RPTUFJTn1cIlxuXG5bY29uZmlnLmVudl1cbkNPTU1FTlRPX09SSUdJTiA9IFwiaHR0cDovLyR7RE9NQUlOfVwiXG5DT01NRU5UT19QT1NUR1JFUyA9IFwicG9zdGdyZXM6Ly9wb3N0Z3Jlczoke1BPU1RHUkVTX1BBU1NXT1JEfUBwb3N0Z3Jlczo1NDMyL3Bvc3RncmVzP3NzbG1vZGU9ZGlzYWJsZVwiXG5DT01NRU5UT19FTkFCTEVfV0lMRENBUkRTID0gXCJ0cnVlXCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke1BPU1RHUkVTX1BBU1NXT1JEfVwiIFxuUE9TVEdSRVNfREIgPSBcInBvc3RncmVzXCJcblBPU1RHUkVTX1VTRVIgPSBcInBvc3RncmVzXCJcbiIKfQ==
```

## Links

`comments`,`website`,`open-source`

---

Version:`v1.8.7`

CommentoCommento is a comments widget designed to enhance the interaction on your website. It allows your readers to contribute to the discussion by upvoting comments that add value and downvoting those that don't. The widget supports markdown formatting and provides moderation tools to manage conversations.

ConduitConduit is a simple, fast and reliable chat server powered by Matrix

### On this page

ConfigurationBase64LinksTags