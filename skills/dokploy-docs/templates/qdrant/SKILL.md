---
title: "Qdrant | Dokploy"
source: "https://docs.dokploy.com/docs/templates/qdrant"
category: dokploy-docs
created: "2026-06-25T17:21:57.937Z"
---

Qdrant | Dokploy

# Qdrant

Copy as Markdown

An open-source vector database designed for high-performance similarity search and storage of embeddings.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  qdrant:
    image: "qdrant/qdrant:latest"
    environment:
      - SERVICE_FQDN_QDRANT_6333
      - QDRANT__SERVICE__API_KEY=${QDRANT_API_KEY}
    expose:
      - "6333"
    volumes:
      - "qdrant_data:/qdrant/storage"
    healthcheck:
      test:
        - CMD-SHELL
        - bash -c ':> /dev/tcp/127.0.0.1/6333' || exit 1
      interval: 5s
      timeout: 5s
      retries: 3

volumes:
  qdrant_data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "qdrant"
port = 6333
host = "${main_domain}"

[config.env]
QDRANT_API_KEY = "${password:32}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBxZHJhbnQ6XG4gICAgaW1hZ2U6IFwicWRyYW50L3FkcmFudDpsYXRlc3RcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBTRVJWSUNFX0ZRRE5fUURSQU5UXzYzMzNcbiAgICAgIC0gUURSQU5UX19TRVJWSUNFX19BUElfS0VZPSR7UURSQU5UX0FQSV9LRVl9XG4gICAgZXhwb3NlOlxuICAgICAgLSBcIjYzMzNcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIFwicWRyYW50X2RhdGE6L3FkcmFudC9zdG9yYWdlXCJcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01ELVNIRUxMXG4gICAgICAgIC0gYmFzaCAtYyAnOj4gL2Rldi90Y3AvMTI3LjAuMC4xLzYzMzMnIHx8IGV4aXQgMVxuICAgICAgaW50ZXJ2YWw6IDVzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogM1xuXG52b2x1bWVzOlxuICBxZHJhbnRfZGF0YToge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJxZHJhbnRcIlxucG9ydCA9IDYzMzNcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5RRFJBTlRfQVBJX0tFWSA9IFwiJHtwYXNzd29yZDozMn1cIiIKfQ==
```

## Links

`vector-db`,`database`,`search`

---

Version:`latest`

qBittorrent Web UIA modern web interface for managing multiple qBittorrent instances. Built with React, Hono, and Bun.

Quant-UXQuant-UX is an open-source UX design and prototyping tool that allows you to create interactive prototypes, conduct user research, and analyze user behavior.

### On this page

ConfigurationBase64LinksTags