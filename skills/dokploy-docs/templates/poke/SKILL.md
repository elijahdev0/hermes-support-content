---
title: "Poke | Dokploy"
source: "https://docs.dokploy.com/docs/templates/poke"
category: dokploy-docs
created: "2026-06-25T17:21:56.648Z"
---

Poke | Dokploy

# Poke

Copy as Markdown

Poke is an open-source, self-hosted alternative to YouTube. A privacy-focused video platform that allows you to watch and share videos without tracking.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  poke:
    image: codeberg.org/poketube/poke:amd64
    restart: unless-stopped
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "poke"
port = 6003
host = "${main_domain}"

[config.env]

[[config.mounts]]
filePath = "/poketube/config.json"
content = """
{
  "server_port": 6003,
  "image_proxy": ""
}
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBwb2tlOlxuICAgIGltYWdlOiBjb2RlYmVyZy5vcmcvcG9rZXR1YmUvcG9rZTphbWQ2NFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicG9rZVwiXG5wb3J0ID0gNjAwM1xuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvcG9rZXR1YmUvY29uZmlnLmpzb25cIlxuY29udGVudCA9IFwiXCJcIlxue1xuICBcInNlcnZlcl9wb3J0XCI6IDYwMDMsXG4gIFwiaW1hZ2VfcHJveHlcIjogXCJcIiBcbn1cblwiXCJcIiIKfQ==
```

## Links

`video`,`youtube-alternative`,`self-hosted`,`privacy`,`streaming`

---

Version:`latest`

PocketBaseOpen Source backend in 1 file

PortainerPortainer is a container management tool for deploying, troubleshooting, and securing applications across cloud, data centers, and IoT.

### On this page

ConfigurationBase64LinksTags