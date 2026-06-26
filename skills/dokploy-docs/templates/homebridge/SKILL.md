---
title: "Homebridge | Dokploy"
source: "https://docs.dokploy.com/docs/templates/homebridge"
category: dokploy-docs
created: "2026-06-25T17:21:49.750Z"
---

Homebridge | Dokploy

# Homebridge

Copy as Markdown

Bringing HomeKit support where there is none. Homebridge allows you to integrate with smart home devices that do not natively support HomeKit.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  homebridge:
    image: homebridge/homebridge:latest
    restart: always
    ports:
      - 8581
    volumes:
      - ./volumes/homebridge:/homebridge
    healthcheck:
      test: ["CMD", "curl", "-f", "http://homebridge:8581/"]
      interval: 60s
      retries: 5
      start_period: 300s
      timeout: 2s
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "homebridge"
port = 8581
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBob21lYnJpZGdlOlxuICAgIGltYWdlOiBob21lYnJpZGdlL2hvbWVicmlkZ2U6bGF0ZXN0XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgcG9ydHM6XG4gICAgICAtIDg1ODFcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuL3ZvbHVtZXMvaG9tZWJyaWRnZTovaG9tZWJyaWRnZVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwiY3VybFwiLCBcIi1mXCIsIFwiaHR0cDovL2hvbWVicmlkZ2U6ODU4MS9cIl1cbiAgICAgIGludGVydmFsOiA2MHNcbiAgICAgIHJldHJpZXM6IDVcbiAgICAgIHN0YXJ0X3BlcmlvZDogMzAwc1xuICAgICAgdGltZW91dDogMnNcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiaG9tZWJyaWRnZVwiXG5wb3J0ID0gODU4MVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`iot`,`homekit`,`internet-of-things`,`self-hosted`,`server`

---

Version:`latest`

Home AssistantOpen source home automation that puts local control and privacy first.

Hoppscotch (AIO + Migrations)Hoppscotch Community Edition (All-in-One) with automatic database migrations. Includes backend, frontend, and admin under unified subpath routing.

### On this page

ConfigurationBase64LinksTags