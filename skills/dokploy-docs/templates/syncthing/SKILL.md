---
title: "Syncthing | Dokploy"
source: "https://docs.dokploy.com/docs/templates/syncthing"
category: dokploy-docs
created: "2026-06-25T17:22:00.274Z"
---

Syncthing | Dokploy

# Syncthing

Copy as Markdown

Syncthing is a continuous file synchronization program that synchronizes files between two or more computers in real time.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  syncthing:
    image: lscr.io/linuxserver/syncthing:latest
    restart: unless-stopped
    expose:
      - 8384
      - 22000
      - 21027/udp
    volumes:
      - syncthing_config:/config
      - syncthing_data:/var/syncthing/Sync
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=${timezone}

volumes:
  syncthing_config:
  syncthing_data:
```

```
[variables]
main_domain = "${domain}"
timezone = "America/Sao_Paulo"

[config]
[[config.domains]]
serviceName = "syncthing"
port = 8384
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBzeW5jdGhpbmc6XG4gICAgaW1hZ2U6IGxzY3IuaW8vbGludXhzZXJ2ZXIvc3luY3RoaW5nOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZXhwb3NlOlxuICAgICAgLSA4Mzg0XG4gICAgICAtIDIyMDAwXG4gICAgICAtIDIxMDI3L3VkcFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHN5bmN0aGluZ19jb25maWc6L2NvbmZpZ1xuICAgICAgLSBzeW5jdGhpbmdfZGF0YTovdmFyL3N5bmN0aGluZy9TeW5jXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBVSUQ9MTAwMFxuICAgICAgLSBQR0lEPTEwMDBcbiAgICAgIC0gVFo9JHt0aW1lem9uZX1cblxudm9sdW1lczpcbiAgc3luY3RoaW5nX2NvbmZpZzpcbiAgc3luY3RoaW5nX2RhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxudGltZXpvbmUgPSBcIkFtZXJpY2EvU2FvX1BhdWxvXCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInN5bmN0aGluZ1wiXG5wb3J0ID0gODM4NFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`file-sync`,`synchronization`,`backup`

---

Version:`latest`

SurrealDBSurrealDB is a native, open-source, multi-model database that lets you store and manage data across relational, document, graph, time-series, vector & search, and geospatial models—all in one place.

Tailscale Exit nodesTailscale ExitNode is a feature that lets you route your internet traffic through a specific device in your Tailscale network.

### On this page

ConfigurationBase64LinksTags