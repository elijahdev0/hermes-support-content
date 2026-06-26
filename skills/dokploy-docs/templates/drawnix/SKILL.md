---
title: "Drawnix | Dokploy"
source: "https://docs.dokploy.com/docs/templates/drawnix"
category: dokploy-docs
created: "2026-06-25T17:21:46.246Z"
---

Drawnix | Dokploy

# Drawnix

Copy as Markdown

Drawnix is an application for generating and managing visual content, powered by pubuzhixing/drawnix Docker image.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  drawnix:
    image: pubuzhixing/drawnix:latest
    restart: unless-stopped
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "drawnix"
port = 3000
host = "${main_domain}"

[config.env]

[[config.mounts]]
# No specific mounts required based on available documentation; added a placeholder for potential configuration file if needed in future
filePath = "/app/config.txt"
content = """
# Placeholder content - customize if the application requires persistent configuration
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBkcmF3bml4OlxuICAgIGltYWdlOiBwdWJ1emhpeGluZy9kcmF3bml4OmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZHJhd25peFwiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblxuW1tjb25maWcubW91bnRzXV1cbiMgTm8gc3BlY2lmaWMgbW91bnRzIHJlcXVpcmVkIGJhc2VkIG9uIGF2YWlsYWJsZSBkb2N1bWVudGF0aW9uOyBhZGRlZCBhIHBsYWNlaG9sZGVyIGZvciBwb3RlbnRpYWwgY29uZmlndXJhdGlvbiBmaWxlIGlmIG5lZWRlZCBpbiBmdXR1cmVcbmZpbGVQYXRoID0gXCIvYXBwL2NvbmZpZy50eHRcIlxuY29udGVudCA9IFwiXCJcIlxuIyBQbGFjZWhvbGRlciBjb250ZW50IC0gY3VzdG9taXplIGlmIHRoZSBhcHBsaWNhdGlvbiByZXF1aXJlcyBwZXJzaXN0ZW50IGNvbmZpZ3VyYXRpb25cblwiXCJcIlxuIgp9
```

## Links

`visualization`,`content-generation`

---

Version:`latest`

draw.iodraw.io is a configurable diagramming/whiteboarding visualization application.

drizzle gatewayDrizzle Gateway is a self-hosted database gateway that allows you to connect to your databases from anywhere.

### On this page

ConfigurationBase64LinksTags