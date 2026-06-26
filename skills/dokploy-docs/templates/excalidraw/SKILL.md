---
title: "Excalidraw | Dokploy"
source: "https://docs.dokploy.com/docs/templates/excalidraw"
category: dokploy-docs
created: "2026-06-25T17:21:47.358Z"
---

Excalidraw | Dokploy

# Excalidraw

Copy as Markdown

Excalidraw is a free and open source online diagramming tool that lets you easily create and share beautiful diagrams.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  excalidraw:
    restart: unless-stopped
    image: excalidraw/excalidraw:latest
    healthcheck:
      test:
        - CMD
        - wget
        - '--spider'
        - '--quiet'
        - 'http://localhost'
      interval: 30s
      timeout: 5s
      retries: 3
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "excalidraw"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGV4Y2FsaWRyYXc6XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBpbWFnZTogZXhjYWxpZHJhdy9leGNhbGlkcmF3OmxhdGVzdFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgLSBDTURcbiAgICAgICAgLSB3Z2V0XG4gICAgICAgIC0gJy0tc3BpZGVyJ1xuICAgICAgICAtICctLXF1aWV0J1xuICAgICAgICAtICdodHRwOi8vbG9jYWxob3N0J1xuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDNcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZXhjYWxpZHJhd1wiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`drawing`

---

Version:`latest`

Evolution APIEvolution API is a robust platform dedicated to empowering small businesses with limited resources, going beyond a simple messaging solution via WhatsApp.

EZBookkeepingEZBookkeeping is a self-hosted bookkeeping application that helps you manage your personal and business finances. It provides features for tracking income, expenses, accounts, and generating financial reports.

### On this page

ConfigurationBase64LinksTags