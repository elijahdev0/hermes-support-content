---
title: "Morphos | Dokploy"
source: "https://docs.dokploy.com/docs/templates/morphos"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

Morphos | Dokploy

# Morphos

Copy as Markdown

Morphos is a lightweight service for distributed operations and orchestration.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  morphos-server:
    image: ghcr.io/danvergara/morphos-server:latest
    restart: unless-stopped
    expose:
      - 8080
    volumes:
      - ../files/morphos-upload:/upload:rw
    healthcheck:
      test: timeout 10s bash -c ':> /dev/tcp/127.0.0.1/8080' || exit 1
      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 90s
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "morphos-server"
port = 8080
host = "${main_domain}"
tls = true
certResolver = "letsencrypt"

[config.env]
# No environment variables required based on provided information

[[config.mounts]]
source = "../files/morphos-upload"
target = "/upload"
type = "bind"
readOnly = false
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBtb3JwaG9zLXNlcnZlcjpcbiAgICBpbWFnZTogZ2hjci5pby9kYW52ZXJnYXJhL21vcnBob3Mtc2VydmVyOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZXhwb3NlOlxuICAgICAgLSA4MDgwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvbW9ycGhvcy11cGxvYWQ6L3VwbG9hZDpyd1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogdGltZW91dCAxMHMgYmFzaCAtYyAnOj4gL2Rldi90Y3AvMTI3LjAuMC4xLzgwODAnIHx8IGV4aXQgMVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDNcbiAgICAgIHN0YXJ0X3BlcmlvZDogOTBzXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibW9ycGhvcy1zZXJ2ZXJcIlxucG9ydCA9IDgwODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbnRscyA9IHRydWVcbmNlcnRSZXNvbHZlciA9IFwibGV0c2VuY3J5cHRcIlxuXG5bY29uZmlnLmVudl1cbiMgTm8gZW52aXJvbm1lbnQgdmFyaWFibGVzIHJlcXVpcmVkIGJhc2VkIG9uIHByb3ZpZGVkIGluZm9ybWF0aW9uXG5cbltbY29uZmlnLm1vdW50c11dXG5zb3VyY2UgPSBcIi4uL2ZpbGVzL21vcnBob3MtdXBsb2FkXCJcbnRhcmdldCA9IFwiL3VwbG9hZFwiXG50eXBlID0gXCJiaW5kXCJcbnJlYWRPbmx5ID0gZmFsc2UiCn0=
```

## Links

`server`,`orchestration`,`lightweight`

---

Version:`latest`

MoltbotWhatsApp gateway CLI with Pi RPC agent - self-hosted AI-powered messaging platform

MovaryMovary is a self-hosted platform for tracking and managing your watched movies using TMDB.

### On this page

ConfigurationBase64LinksTags