---
title: "Mumble | Dokploy"
source: "https://docs.dokploy.com/docs/templates/mumble"
category: dokploy-docs
created: "2026-06-25T17:21:53.156Z"
---

Mumble | Dokploy

# Mumble

Copy as Markdown

Mumble is an open-source, low-latency, high-quality voice chat software primarily intended for use while gaming.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  mumble-server:
    image: mumblevoip/mumble-server:latest
    restart: unless-stopped
    ports:
      - 64738
      - 64738/udp
    volumes:
      - mumble-data:/data
    environment:
      - MUMBLE_SUPERUSER_PASSWORD=${SUPERUSER_PASSWORD}
      - MUMBLE_CONFIG_WELCOMETEXT=${WELCOME_TEXT}
      - MUMBLE_CONFIG_USERS=${MAX_USERS}

volumes:
  mumble-data:
```

```
[variables]
superuser_password = "${password:32}"
welcome_text = "Welcome to Mumble Server! Low-latency voice chat."
max_users = "50"

[config]

[config.env]
SUPERUSER_PASSWORD = "${superuser_password}"
WELCOME_TEXT = "${welcome_text}"
MAX_USERS = "${max_users}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBtdW1ibGUtc2VydmVyOlxuICAgIGltYWdlOiBtdW1ibGV2b2lwL211bWJsZS1zZXJ2ZXI6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gNjQ3MzhcbiAgICAgIC0gNjQ3MzgvdWRwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gbXVtYmxlLWRhdGE6L2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTVVNQkxFX1NVUEVSVVNFUl9QQVNTV09SRD0ke1NVUEVSVVNFUl9QQVNTV09SRH1cbiAgICAgIC0gTVVNQkxFX0NPTkZJR19XRUxDT01FVEVYVD0ke1dFTENPTUVfVEVYVH1cbiAgICAgIC0gTVVNQkxFX0NPTkZJR19VU0VSUz0ke01BWF9VU0VSU31cblxudm9sdW1lczpcbiAgbXVtYmxlLWRhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbnN1cGVydXNlcl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxud2VsY29tZV90ZXh0ID0gXCJXZWxjb21lIHRvIE11bWJsZSBTZXJ2ZXIhIExvdy1sYXRlbmN5IHZvaWNlIGNoYXQuXCJcbm1heF91c2VycyA9IFwiNTBcIlxuXG5bY29uZmlnXVxuXG5bY29uZmlnLmVudl1cblNVUEVSVVNFUl9QQVNTV09SRCA9IFwiJHtzdXBlcnVzZXJfcGFzc3dvcmR9XCJcbldFTENPTUVfVEVYVCA9IFwiJHt3ZWxjb21lX3RleHR9XCJcbk1BWF9VU0VSUyA9IFwiJHttYXhfdXNlcnN9XCJcblxuIgp9
```

## Links

`voice-chat`,`communication`,`gaming`,`voip`

---

Version:`latest`

MuleSoft ESB Runtime Community EditionMuleSoft ESB Runtime is a lightweight, Java-based integration platform that allows you to easily integrate applications, data sources, and APIs. It provides powerful connectors and data transformation capabilities for building robust integration solutions.

n8nn8n is an open source low-code platform for automating workflows and integrations.

### On this page

ConfigurationBase64LinksTags