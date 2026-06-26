---
title: "Wallos | Dokploy"
source: "https://docs.dokploy.com/docs/templates/wallos"
category: dokploy-docs
created: "2026-06-25T17:22:01.420Z"
---

Wallos | Dokploy

# Wallos

Copy as Markdown

Wallos is a self-hosted subscription tracking application that helps you manage and monitor your subscriptions, providing insights into your spending habits.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'
services:
  wallos:
    image: bellamy/wallos:latest
    ports:
      - '80'
    environment:
      TZ: 'Europe/Paris'
    volumes:
      - wallos_db:/var/www/html/db
      - wallos_logos:/var/www/html/images/uploads/logos
    restart: unless-stopped

volumes:
  wallos_db:
  wallos_logos:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "wallos"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5zZXJ2aWNlczpcbiAgd2FsbG9zOlxuICAgIGltYWdlOiBiZWxsYW15L3dhbGxvczpsYXRlc3RcbiAgICBwb3J0czpcbiAgICAgIC0gJzgwJ1xuICAgIGVudmlyb25tZW50OlxuICAgICAgVFo6ICdFdXJvcGUvUGFyaXMnXG4gICAgdm9sdW1lczpcbiAgICAgIC0gd2FsbG9zX2RiOi92YXIvd3d3L2h0bWwvZGJcbiAgICAgIC0gd2FsbG9zX2xvZ29zOi92YXIvd3d3L2h0bWwvaW1hZ2VzL3VwbG9hZHMvbG9nb3NcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG52b2x1bWVzOlxuICB3YWxsb3NfZGI6XG4gIHdhbGxvc19sb2dvczoiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwid2FsbG9zXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIiIKfQ==
```

## Links

`finance`,`subscription`,`budgeting`,`expense-tracking`,`spending`

---

Version:`latest`

VikunjaVikunja is a self-hosted, open-source to-do list application to organize tasks, projects, and notes.

WandererWanderer is a self-hosted mapping and geolocation platform powered by Meilisearch, PocketBase, and a web frontend.

### On this page

ConfigurationBase64LinksTags