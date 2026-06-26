---
title: "Spacedrive | Dokploy"
source: "https://docs.dokploy.com/docs/templates/spacedrive"
category: dokploy-docs
created: "2026-06-25T17:21:59.114Z"
---

Spacedrive | Dokploy

# Spacedrive

Copy as Markdown

Spacedrive is a cross-platform file manager. It connects your devices together to help you organize files from anywhere. powered by a virtual distributed filesystem (VDFS) written in Rust. Organize files across many devices in one place.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  server:
    image: ghcr.io/spacedriveapp/spacedrive/server:latest
    ports:
      - 8080
    environment:
      - SD_AUTH=${SD_USERNAME}:${SD_PASSWORD}
    volumes:
      - /var/spacedrive:/var/spacedrive
```

```
[variables]
main_domain = "${domain}"
secret_key = "${password}"

[config]
mounts = []

[[config.domains]]
serviceName = "server"
port = 8_080
host = "${main_domain}"

[config.env]
SD_USERNAME = "admin"
SD_PASSWORD = "${secret_key}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBzZXJ2ZXI6XG4gICAgaW1hZ2U6IGdoY3IuaW8vc3BhY2Vkcml2ZWFwcC9zcGFjZWRyaXZlL3NlcnZlcjpsYXRlc3RcbiAgICBwb3J0czpcbiAgICAgIC0gODA4MFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBTRF9BVVRIPSR7U0RfVVNFUk5BTUV9OiR7U0RfUEFTU1dPUkR9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gL3Zhci9zcGFjZWRyaXZlOi92YXIvc3BhY2Vkcml2ZVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnNlY3JldF9rZXkgPSBcIiR7cGFzc3dvcmR9XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInNlcnZlclwiXG5wb3J0ID0gOF8wODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5TRF9VU0VSTkFNRSA9IFwiYWRtaW5cIlxuU0RfUEFTU1dPUkQgPSBcIiR7c2VjcmV0X2tleX1cIlxuIgp9
```

## Links

`file-manager`,`vdfs`,`storage`

---

Version:`latest`

SoketiSoketi is your simple, fast, and resilient open-source WebSockets server.

Stack AuthOpen-source Auth0/Clerk alternative. Stack Auth is a free and open source authentication tool that allows you to authenticate your users.

### On this page

ConfigurationBase64LinksTags