---
title: "Homarr | Dokploy"
source: "https://docs.dokploy.com/docs/templates/homarr"
category: dokploy-docs
created: "2026-06-25T17:21:49.750Z"
---

Homarr | Dokploy

# Homarr

Copy as Markdown

A sleek, modern dashboard that puts all your apps and services in one place with Docker integration.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  homarr:
    image: ghcr.io/homarr-labs/homarr:latest
    restart: unless-stopped
    volumes:
      # - /var/run/docker.sock:/var/run/docker.sock # Optional, only if you want docker integration
      - ../homarr/appdata:/appdata
    environment:
      - SECRET_ENCRYPTION_KEY=${SECRET_ENCRYPTION_KEY}
    ports:
      - 7575
```

```
[variables]
main_domain = "${domain}"
secret_key = "${password:64}"

[config]
env = ["SECRET_ENCRYPTION_KEY=${secret_key}"]
mounts = []

[[config.domains]]
serviceName = "homarr"
port = 7_575
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBob21hcnI6XG4gICAgaW1hZ2U6IGdoY3IuaW8vaG9tYXJyLWxhYnMvaG9tYXJyOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgICMgLSAvdmFyL3J1bi9kb2NrZXIuc29jazovdmFyL3J1bi9kb2NrZXIuc29jayAjIE9wdGlvbmFsLCBvbmx5IGlmIHlvdSB3YW50IGRvY2tlciBpbnRlZ3JhdGlvblxuICAgICAgLSAuLi9ob21hcnIvYXBwZGF0YTovYXBwZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBTRUNSRVRfRU5DUllQVElPTl9LRVk9JHtTRUNSRVRfRU5DUllQVElPTl9LRVl9XG4gICAgcG9ydHM6XG4gICAgICAtIDc1NzVcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5zZWNyZXRfa2V5ID0gXCIke3Bhc3N3b3JkOjY0fVwiXG5cbltjb25maWddXG5lbnYgPSBbXCJTRUNSRVRfRU5DUllQVElPTl9LRVk9JHtzZWNyZXRfa2V5fVwiXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiaG9tYXJyXCJcbnBvcnQgPSA3XzU3NVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`dashboard`,`monitoring`

---

Version:`latest`

HoarderHoarder is an open source "Bookmark Everything" app that uses AI for automatically tagging the content you throw at it.

Home AssistantOpen source home automation that puts local control and privacy first.

### On this page

ConfigurationBase64LinksTags