---
title: "Soketi | Dokploy"
source: "https://docs.dokploy.com/docs/templates/soketi"
category: dokploy-docs
created: "2026-06-25T17:21:59.114Z"
---

Soketi | Dokploy

# Soketi

Copy as Markdown

Soketi is your simple, fast, and resilient open-source WebSockets server.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  soketi:
    image: quay.io/soketi/soketi:1.6.1-16-debian
    environment:
      SOKETI_DEBUG: "1"
      SOKETI_HOST: "0.0.0.0"
      SOKETI_PORT: "6001"
      SOKETI_METRICS_SERVER_PORT: "9601"
    restart: unless-stopped
```

```
[variables]
main_domain = "${domain}"
metrics_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "soketi"
port = 6_001
host = "${main_domain}"

[[config.domains]]
serviceName = "soketi"
port = 9_601
host = "${metrics_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBzb2tldGk6XG4gICAgaW1hZ2U6IHF1YXkuaW8vc29rZXRpL3Nva2V0aToxLjYuMS0xNi1kZWJpYW5cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFNPS0VUSV9ERUJVRzogXCIxXCJcbiAgICAgIFNPS0VUSV9IT1NUOiBcIjAuMC4wLjBcIlxuICAgICAgU09LRVRJX1BPUlQ6IFwiNjAwMVwiXG4gICAgICBTT0tFVElfTUVUUklDU19TRVJWRVJfUE9SVDogXCI5NjAxXCJcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbm1ldHJpY3NfZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0ge31cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInNva2V0aVwiXG5wb3J0ID0gNl8wMDFcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwic29rZXRpXCJcbnBvcnQgPSA5XzYwMVxuaG9zdCA9IFwiJHttZXRyaWNzX2RvbWFpbn1cIlxuIgp9
```

## Links

`chat`

---

Version:`v1.6.1-16`

SnappSnapp is a self-hosted screenshot sharing service with user management and authentication.

SpacedriveSpacedrive is a cross-platform file manager. It connects your devices together to help you organize files from anywhere. powered by a virtual distributed filesystem (VDFS) written in Rust. Organize files across many devices in one place.

### On this page

ConfigurationBase64LinksTags