---
title: "Pocket ID | Dokploy"
source: "https://docs.dokploy.com/docs/templates/pocket-id"
category: dokploy-docs
created: "2026-06-25T17:21:56.648Z"
---

Pocket ID | Dokploy

# Pocket ID

Copy as Markdown

A simple and easy-to-use OIDC provider that allows users to authenticate with their passkeys to your services.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  pocket-id:
    image: ghcr.io/pocket-id/pocket-id:v1
    restart: unless-stopped
    environment:
      - APP_URL
      - TRUST_PROXY
      - ENCRYPTION_KEY
    volumes:
      - pocket-id-data:/app/data
    healthcheck:
      test: [ "CMD", "/app/pocket-id", "healthcheck" ]
      interval: 1m30s
      timeout: 5s
      retries: 2
      start_period: 10s

volumes:
  pocket-id-data:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "pocket-id"
port = 1411
host = "${main_domain}"

[config.env]
ENCRYPTION_KEY = "CHANGEME: openssl rand -base64 32"
APP_URL = "http://${main_domain}"
TRUST_PROXY = "true"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwb2NrZXQtaWQ6XG4gICAgaW1hZ2U6IGdoY3IuaW8vcG9ja2V0LWlkL3BvY2tldC1pZDp2MVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIEFQUF9VUkxcbiAgICAgIC0gVFJVU1RfUFJPWFlcbiAgICAgIC0gRU5DUllQVElPTl9LRVlcbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb2NrZXQtaWQtZGF0YTovYXBwL2RhdGFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFsgXCJDTURcIiwgXCIvYXBwL3BvY2tldC1pZFwiLCBcImhlYWx0aGNoZWNrXCIgXVxuICAgICAgaW50ZXJ2YWw6IDFtMzBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogMlxuICAgICAgc3RhcnRfcGVyaW9kOiAxMHNcblxudm9sdW1lczpcbiAgcG9ja2V0LWlkLWRhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicG9ja2V0LWlkXCJcbnBvcnQgPSAxNDExXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuRU5DUllQVElPTl9LRVkgPSBcIkNIQU5HRU1FOiBvcGVuc3NsIHJhbmQgLWJhc2U2NCAzMlwiXG5BUFBfVVJMID0gXCJodHRwOi8vJHttYWluX2RvbWFpbn1cIlxuVFJVU1RfUFJPWFkgPSBcInRydWVcIlxuIgp9
```

## Links

`identity`,`auth`

---

Version:`v1`

PlunkPlunk is the open-source, affordable email platform that brings together marketing, transactional and broadcast emails into one single, complete solution

PocketBaseOpen Source backend in 1 file

### On this page

ConfigurationBase64LinksTags