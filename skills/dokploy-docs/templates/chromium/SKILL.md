---
title: "Chromium | Dokploy"
source: "https://docs.dokploy.com/docs/templates/chromium"
category: dokploy-docs
created: "2026-06-25T17:21:43.964Z"
---

Chromium | Dokploy

# Chromium

Copy as Markdown

Chromium is an open-source browser project that is designed to provide a safer, faster, and more stable way for all users to experience the web in a containerized environment.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  chromium:
    image: lscr.io/linuxserver/chromium:5f5dd27e-ls102
    ports:
      - "3000"
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=UTC
    volumes:
      - config:/config

volumes:
  config:
```

```
[variables]

[config]
[[config.domains]]
serviceName = "chromium"
port = 3000
host = "${domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBjaHJvbWl1bTpcbiAgICBpbWFnZTogbHNjci5pby9saW51eHNlcnZlci9jaHJvbWl1bTo1ZjVkZDI3ZS1sczEwMlxuICAgIHBvcnRzOlxuICAgICAgLSBcIjMwMDBcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQVUlEPTEwMDBcbiAgICAgIC0gUEdJRD0xMDAwXG4gICAgICAtIFRaPVVUQ1xuICAgIHZvbHVtZXM6XG4gICAgICAtIGNvbmZpZzovY29uZmlnXG5cbnZvbHVtZXM6XG4gIGNvbmZpZzogIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjaHJvbWl1bVwiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHtkb21haW59XCIgIgp9
```

## Links

`browser`,`development`,`web`

---

Version:`5f5dd27e-ls102`

ChirpStackOpen-source LoRaWAN Network Server for IoT applications. Complete stack with gateway bridges, REST API, and web interface for managing LoRaWAN devices and gateways.

ClassicPressClassicPress is a community-led open source content management system for creators. It is a fork of WordPress 6.2 that preserves the TinyMCE classic editor as the default option.

### On this page

ConfigurationBase64LinksTags