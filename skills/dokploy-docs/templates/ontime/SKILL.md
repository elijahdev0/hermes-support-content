---
title: "Ontime | Dokploy"
source: "https://docs.dokploy.com/docs/templates/ontime"
category: dokploy-docs
created: "2026-06-25T17:21:55.475Z"
---

Ontime | Dokploy

# Ontime

Copy as Markdown

Ontime is browser-based application that manages event rundowns, scheduliing and cuing

## Configuration

docker-compose.ymltemplate.toml

```
services:
  ontime:
    image: getontime/ontime:v3.8.0
    ports:
      - 4001
      - 8888
      - 9999
    volumes:
      - ontime-data:/data/
    environment:
      - TZ
    restart: unless-stopped
volumes:
  ontime-data:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "ontime"
port = 4_001
host = "${main_domain}"

[config.env]
TZ = "UTC"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBvbnRpbWU6XG4gICAgaW1hZ2U6IGdldG9udGltZS9vbnRpbWU6djMuOC4wXG4gICAgcG9ydHM6XG4gICAgICAtIDQwMDFcbiAgICAgIC0gODg4OFxuICAgICAgLSA5OTk5XG4gICAgdm9sdW1lczpcbiAgICAgIC0gb250aW1lLWRhdGE6L2RhdGEvXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFRaXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbnZvbHVtZXM6XG4gIG9udGltZS1kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIm9udGltZVwiXG5wb3J0ID0gNF8wMDFcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5UWiA9IFwiVVRDXCJcbiIKfQ==
```

## Links

`event`

---

Version:`v3.8.0`

One Time SecretShare sensitive information securely with self-destructing links that are only viewable once.

Open FiestaOpen Fiesta is an open-source AI chat and inference UI, supporting multiple backends such as OpenRouter, Gemini, and Ollama.

### On this page

ConfigurationBase64LinksTags