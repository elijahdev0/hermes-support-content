---
title: "Baikal | Dokploy"
source: "https://docs.dokploy.com/docs/templates/baikal"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

Baikal | Dokploy

# Baikal

Copy as Markdown

Baikal is a lightweight, self-hosted CalDAV and CardDAV server that enables users to manage calendars and contacts efficiently. It provides a simple and effective solution for syncing and sharing events, tasks, and address books across multiple devices.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  baikal:
    image: ckulka/baikal:nginx-php8.2
    restart: unless-stopped
    ports:
      - 80
    environment:
      - TZ=UTC
    volumes:
      - config:/var/www/baikal/config
      - data:/var/www/baikal/Specific

volumes:
  config: {}
  data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "baikal"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBiYWlrYWw6XG4gICAgaW1hZ2U6IGNrdWxrYS9iYWlrYWw6bmdpbngtcGhwOC4yXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gODBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gVFo9VVRDXG4gICAgdm9sdW1lczpcbiAgICAgIC0gY29uZmlnOi92YXIvd3d3L2JhaWthbC9jb25maWdcbiAgICAgIC0gZGF0YTovdmFyL3d3dy9iYWlrYWwvU3BlY2lmaWNcblxudm9sdW1lczpcbiAgY29uZmlnOiB7fVxuICBkYXRhOiB7fSAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYmFpa2FsXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIiAiCn0=
```

## Links

`calendar`,`contacts`,`caldav`,`carddav`

---

Version:`nginx-php8.2`

BackrestBackrest is a web-based backup solution powered by restic, offering an intuitive WebUI for easy repository management, snapshot browsing, and file restoration. It runs in the background, automating snapshot scheduling and repository maintenance. Built with Go, Backrest is a lightweight standalone binary with restic as its only dependency. It provides a secure and user-friendly way to manage backups while still allowing direct access to the restic CLI for advanced operations.

BarrageBarrage is a minimalistic Deluge WebUI app with full mobile support. It features a responsive mobile-first design, allowing you to manage your torrents with ease from any device.

### On this page

ConfigurationBase64LinksTags