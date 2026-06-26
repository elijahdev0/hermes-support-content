---
title: "Owncast | Dokploy"
source: "https://docs.dokploy.com/docs/templates/owncast"
category: dokploy-docs
created: "2026-06-25T17:21:55.477Z"
---

Owncast | Dokploy

# Owncast

Copy as Markdown

Owncast is a self-hosted live video streaming and chat server for use with existing broadcasting software.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  owncast:
    image: owncast/owncast:latest
    restart: unless-stopped
    volumes:
      - owncast-data:/app/data
    ports:
      - 8080
      - 1935

volumes:
  owncast-data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "owncast"
port = 8080
host = "${main_domain}"

[config.env]

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIlxudmVyc2lvbjogXCIzLjhcIlxuXG5zZXJ2aWNlczpcbiAgb3duY2FzdDpcbiAgICBpbWFnZTogb3duY2FzdC9vd25jYXN0OmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gb3duY2FzdC1kYXRhOi9hcHAvZGF0YVxuICAgIHBvcnRzOlxuICAgICAgLSA4MDgwXG4gICAgICAtIDE5MzVcblxudm9sdW1lczpcbiAgb3duY2FzdC1kYXRhOiB7fSIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJvd25jYXN0XCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuXG5bW2NvbmZpZy5tb3VudHNdXSIKfQ==
```

## Links

`streaming`,`live-video`,`chat`,`broadcasting`,`self-hosted`,`rtmp`

---

Version:`latest`

OutlineOutline is a self-hosted knowledge base and documentation platform that allows you to build and manage your own knowledge base applications.

PalmrPalmr the open-source, self-hosted alternative to WeTransfer. Share files securely, without tracking or limitations.

### On this page

ConfigurationBase64LinksTags