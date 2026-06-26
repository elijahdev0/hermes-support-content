---
title: "Apprise API | Dokploy"
source: "https://docs.dokploy.com/docs/templates/apprise-api"
category: dokploy-docs
created: "2026-06-25T17:21:40.415Z"
---

Apprise API | Dokploy

# Apprise API

Copy as Markdown

Apprise API provides a simple interface for sending notifications to almost all of the most popular notification services available to us today.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  apprise-api:
    image: linuxserver/apprise-api:latest
    restart: unless-stopped
    ports:
      - 8000
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=UTC
    volumes:
      - config:/config

volumes:
  config: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "apprise-api"
port = 8000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhcHByaXNlLWFwaTpcbiAgICBpbWFnZTogbGludXhzZXJ2ZXIvYXBwcmlzZS1hcGk6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gODAwMFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQVUlEPTEwMDBcbiAgICAgIC0gUEdJRD0xMDAwXG4gICAgICAtIFRaPVVUQ1xuICAgIHZvbHVtZXM6XG4gICAgICAtIGNvbmZpZzovY29uZmlnXG5cbnZvbHVtZXM6XG4gIGNvbmZpZzoge30gIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFwcHJpc2UtYXBpXCJcbnBvcnQgPSA4MDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiICIKfQ==
```

## Links

`notifications`,`api`

---

Version:`latest`

App FlowyAppFlowy is an open-source alternative to Notion. You are in charge of your data and customizations.

AppsmithAppsmith is a free and open source platform for building internal tools and applications.

### On this page

ConfigurationBase64LinksTags