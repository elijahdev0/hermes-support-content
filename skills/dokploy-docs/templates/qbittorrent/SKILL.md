---
title: "qBittorrent | Dokploy"
source: "https://docs.dokploy.com/docs/templates/qbittorrent"
category: dokploy-docs
created: "2026-06-25T17:21:57.937Z"
---

qBittorrent | Dokploy

# qBittorrent

Copy as Markdown

A free and open-source BitTorrent client with web interface for remote management. Default login: admin (check container logs for temporary password on first startup).

## Configuration

docker-compose.ymltemplate.toml

```
# docker-compose.yml
#
# IMPORTANT: First-time setup information
# - Default username: admin
# - Password: Check container logs for temporary password on first startup
# - Access via your configured domain (HTTPS) after deployment
# - Change the default password immediately after first login
#
services:
  qbittorrent:
    image: lscr.io/linuxserver/qbittorrent:latest
    restart: unless-stopped
    environment:
      - PUID=1000
      - PGID=1000
      - WEBUI_PORT=8080
      - TORRENTING_PORT=6881
    volumes:
      - qb_config:/config
      - qb_downloads:/downloads
    ports:
      - 8080
      - 6881:6881
      - 6881:6881/udp
    labels:
      - "traefik.enable=true"
volumes:
  qb_config:
  qb_downloads:
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "qbittorrent"
port = 8080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgZG9ja2VyLWNvbXBvc2UueW1sXG4jIFxuIyBJTVBPUlRBTlQ6IEZpcnN0LXRpbWUgc2V0dXAgaW5mb3JtYXRpb25cbiMgLSBEZWZhdWx0IHVzZXJuYW1lOiBhZG1pblxuIyAtIFBhc3N3b3JkOiBDaGVjayBjb250YWluZXIgbG9ncyBmb3IgdGVtcG9yYXJ5IHBhc3N3b3JkIG9uIGZpcnN0IHN0YXJ0dXBcbiMgLSBBY2Nlc3MgdmlhIHlvdXIgY29uZmlndXJlZCBkb21haW4gKEhUVFBTKSBhZnRlciBkZXBsb3ltZW50XG4jIC0gQ2hhbmdlIHRoZSBkZWZhdWx0IHBhc3N3b3JkIGltbWVkaWF0ZWx5IGFmdGVyIGZpcnN0IGxvZ2luXG4jXG5zZXJ2aWNlczpcbiAgcWJpdHRvcnJlbnQ6XG4gICAgaW1hZ2U6IGxzY3IuaW8vbGludXhzZXJ2ZXIvcWJpdHRvcnJlbnQ6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUFVJRD0xMDAwXG4gICAgICAtIFBHSUQ9MTAwMFxuICAgICAgLSBXRUJVSV9QT1JUPTgwODBcbiAgICAgIC0gVE9SUkVOVElOR19QT1JUPTY4ODFcbiAgICB2b2x1bWVzOlxuICAgICAgLSBxYl9jb25maWc6L2NvbmZpZ1xuICAgICAgLSBxYl9kb3dubG9hZHM6L2Rvd25sb2Fkc1xuICAgIHBvcnRzOlxuICAgICAgLSA4MDgwXG4gICAgICAtIDY4ODE6Njg4MVxuICAgICAgLSA2ODgxOjY4ODEvdWRwXG4gICAgbGFiZWxzOlxuICAgICAgLSBcInRyYWVmaWsuZW5hYmxlPXRydWVcIlxudm9sdW1lczpcbiAgcWJfY29uZmlnOlxuICBxYl9kb3dubG9hZHM6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInFiaXR0b3JyZW50XCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`torrent`,`download`,`file-sharing`

---

Version:`latest`

PyrodactylPyrodactyl is the Pterodactyl-based game server panel that's faster, smaller, safer, and more accessible than Pelican.

qBittorrent Web UIA modern web interface for managing multiple qBittorrent instances. Built with React, Hono, and Bun.

### On this page

ConfigurationBase64LinksTags