---
title: "Baserow | Dokploy"
source: "https://docs.dokploy.com/docs/templates/baserow"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

Baserow | Dokploy

# Baserow

Copy as Markdown

Baserow is an open source database management tool that allows you to create and manage databases.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  baserow:
    image: baserow/baserow:1.25.2
    environment:
      BASEROW_PUBLIC_URL: "http://${BASEROW_HOST}"
    volumes:
      - baserow_data:/baserow/data
volumes:
  baserow_data:
```

```
[variables]
main_domain = "${domain}"

[config]
env = ["BASEROW_HOST=${main_domain}"]
mounts = []

[[config.domains]]
serviceName = "baserow"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBiYXNlcm93OlxuICAgIGltYWdlOiBiYXNlcm93L2Jhc2Vyb3c6MS4yNS4yXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBCQVNFUk9XX1BVQkxJQ19VUkw6IFwiaHR0cDovLyR7QkFTRVJPV19IT1NUfVwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gYmFzZXJvd19kYXRhOi9iYXNlcm93L2RhdGFcbnZvbHVtZXM6XG4gIGJhc2Vyb3dfZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXCJCQVNFUk9XX0hPU1Q9JHttYWluX2RvbWFpbn1cIl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImJhc2Vyb3dcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`database`

---

Version:`1.25.2`

BarrageBarrage is a minimalistic Deluge WebUI app with full mobile support. It features a responsive mobile-first design, allowing you to manage your torrents with ease from any device.

BazarrBazarr is a companion application to Sonarr and Radarr that manages and downloads subtitles based on your requirements.

### On this page

ConfigurationBase64LinksTags