---
title: "Lodestone | Dokploy"
source: "https://docs.dokploy.com/docs/templates/lodestone"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

Lodestone | Dokploy

# Lodestone

Copy as Markdown

A free, open source server hosting tool for Minecraft and other multiplayers games.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  lodestone:
    image: ghcr.io/lodestone-team/lodestone_core
    ports:
      - "16662:16662"
      - "25565-25590:25565-25590"
    volumes:
      - lodestone:/home/user/.lodestone
    restart: unless-stopped

  lodestone_dashboard:
    image: ghcr.io/lodestone-team/lodestone_dashboard:v0.5.1
    restart: always

volumes:
  lodestone:
    driver: local
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "lodestone_dashboard"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBsb2Rlc3RvbmU6XG4gICAgaW1hZ2U6IGdoY3IuaW8vbG9kZXN0b25lLXRlYW0vbG9kZXN0b25lX2NvcmVcbiAgICBwb3J0czpcbiAgICAgIC0gXCIxNjY2MjoxNjY2MlwiXG4gICAgICAtIFwiMjU1NjUtMjU1OTA6MjU1NjUtMjU1OTBcIiBcbiAgICB2b2x1bWVzOlxuICAgICAgLSBsb2Rlc3RvbmU6L2hvbWUvdXNlci8ubG9kZXN0b25lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxuICBsb2Rlc3RvbmVfZGFzaGJvYXJkOlxuICAgIGltYWdlOiBnaGNyLmlvL2xvZGVzdG9uZS10ZWFtL2xvZGVzdG9uZV9kYXNoYm9hcmQ6djAuNS4xXG4gICAgcmVzdGFydDogYWx3YXlzICBcblxudm9sdW1lczpcbiAgbG9kZXN0b25lOlxuICAgIGRyaXZlcjogbG9jYWwiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0ge31cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImxvZGVzdG9uZV9kYXNoYm9hcmRcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiIgp9
```

## Links

`minecraft`,`hosting`,`server`

---

Version:`0.5.1`

Lobe ChatLobe Chat - an open-source, modern-design AI chat framework.

LogtoLogto is an open-source Identity and Access Management (IAM) platform designed to streamline Customer Identity and Access Management (CIAM) and Workforce Identity Management.

### On this page

ConfigurationBase64LinksTags