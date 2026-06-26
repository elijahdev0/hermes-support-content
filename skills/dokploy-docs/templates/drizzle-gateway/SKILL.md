---
title: "drizzle gateway | Dokploy"
source: "https://docs.dokploy.com/docs/templates/drizzle-gateway"
category: dokploy-docs
created: "2026-06-25T17:21:46.246Z"
---

drizzle gateway | Dokploy

# drizzle gateway

Copy as Markdown

Drizzle Gateway is a self-hosted database gateway that allows you to connect to your databases from anywhere.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  drizzle-gateway:
    image: ghcr.io/drizzle-team/gateway:latest
    restart: always
    environment:
      PORT: "4983"
      STORE_PATH: "/app"
      MASTERPASS: ${MASTERPASS}
    volumes:
      - drizzle-gateway:/app
    networks:
      - dokploy-network

volumes:
  drizzle-gateway:

networks:
  dokploy-network:
    external: true
```

```
[variables]
main_domain = "${domain}"
masterpass = "${base64:32}"

[config]
env = [
  "MASTERPASS=${masterpass}",
]
mounts = []

[[config.domains]]
serviceName = "drizzle-gateway"
port = 4_983
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkcml6emxlLWdhdGV3YXk6XG4gICAgaW1hZ2U6IGdoY3IuaW8vZHJpenpsZS10ZWFtL2dhdGV3YXk6bGF0ZXN0XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1JUOiBcIjQ5ODNcIlxuICAgICAgU1RPUkVfUEFUSDogXCIvYXBwXCJcbiAgICAgIE1BU1RFUlBBU1M6ICR7TUFTVEVSUEFTU31cbiAgICB2b2x1bWVzOlxuICAgICAgLSBkcml6emxlLWdhdGV3YXk6L2FwcFxuICAgIG5ldHdvcmtzOlxuICAgICAgLSBkb2twbG95LW5ldHdvcmtcblxudm9sdW1lczpcbiAgZHJpenpsZS1nYXRld2F5OlxuXG5uZXR3b3JrczpcbiAgZG9rcGxveS1uZXR3b3JrOlxuICAgIGV4dGVybmFsOiB0cnVlXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxubWFzdGVycGFzcyA9IFwiJHtiYXNlNjQ6MzJ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJNQVNURVJQQVNTPSR7bWFzdGVycGFzc31cIixcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImRyaXp6bGUtZ2F0ZXdheVwiXG5wb3J0ID0gNF85ODNcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`database`,`gateway`

---

Version:`latest`

DrawnixDrawnix is an application for generating and managing visual content, powered by pubuzhixing/drawnix Docker image.

DumbAssetsDumbAssets is a simple, self-hosted asset tracking service with no database or authentication required.

### On this page

ConfigurationBase64LinksTags