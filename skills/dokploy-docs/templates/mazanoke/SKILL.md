---
title: "MAZANOKE | Dokploy"
source: "https://docs.dokploy.com/docs/templates/mazanoke"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

MAZANOKE | Dokploy

# MAZANOKE

Copy as Markdown

MAZANOKE is a modern, self-hosted image hosting and sharing platform. Upload, organize, and share your images with a clean and intuitive interface.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  mazanoke:
    image: ghcr.io/civilblur/mazanoke:latest
    restart: unless-stopped
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "mazanoke"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBtYXphbm9rZTpcbiAgICBpbWFnZTogZ2hjci5pby9jaXZpbGJsdXIvbWF6YW5va2U6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSB7fVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibWF6YW5va2VcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiICIKfQ==
```

## Links

`image-hosting`,`file-sharing`,`self-hosted`,`media`,`gallery`

---

Version:`latest`

MaybeMaybe is a self-hosted finance tracking application designed to simplify budgeting and expenses.

MCSManagerA modern dashboard for managing Minecraft servers. Primarily focused on Minecraft, but also supports other games and features a UI that's easy for beginners to use and supports i18n.

### On this page

ConfigurationBase64LinksTags