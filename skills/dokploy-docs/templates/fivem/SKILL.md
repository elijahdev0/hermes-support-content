---
title: "FiveM Server | Dokploy"
source: "https://docs.dokploy.com/docs/templates/fivem"
category: dokploy-docs
created: "2026-06-25T17:21:47.359Z"
---

FiveM Server | Dokploy

# FiveM Server

Copy as Markdown

A modded GTA V multiplayer server with optional txAdmin web interface for easy server management.

## Configuration

docker-compose.ymltemplate.toml

```
# docker-compose.yml
#
# IMPORTANT: FiveM Template - Two Deployment Modes
#
# MODE 1: Standard FiveM Server
# - Set LICENSE_KEY environment variable (get free from https://forum.fivem.net/)
# - Leave NO_DEFAULT_CONFIG empty or unset
# - Server configured via /config files
# - No web management interface
#
# MODE 2: txAdmin Web Interface
# - Set NO_DEFAULT_CONFIG=1
# - DO NOT set LICENSE_KEY (configure via web UI)
# - Access web management at https://your-domain
# - License configured through txAdmin interface
#
# WARNING: Don't mix modes! Setting both LICENSE_KEY and NO_DEFAULT_CONFIG=1 causes errors
#
services:
  fivem:
    image: spritsail/fivem:latest
    restart: unless-stopped
    tty: true
    stdin_open: true
    environment:
      - LICENSE_KEY=${license_key}
      - RCON_PASSWORD=${rcon_password}
      - NO_DEFAULT_CONFIG=${NO_DEFAULT_CONFIG:-}
    volumes:
      - fivem_config:/config
      - fivem_txdata:/txData
    ports:
      - 30120:30120
      - 30120:30120/udp
      - 40120
    labels:
      - "traefik.enable=true"

volumes:
  fivem_config:
  fivem_txdata:
```

```
[variables]
main_domain = "${domain}"
license_key = "${password:32}"
rcon_password = "${password:16}"

[config]
env = [
    "LICENSE_KEY=${license_key}",
    "RCON_PASSWORD=${rcon_password}",
    "NO_DEFAULT_CONFIG=${NO_DEFAULT_CONFIG:-}"
]
mounts = []

[[config.domains]]
serviceName = "fivem"
port = 40120
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgZG9ja2VyLWNvbXBvc2UueW1sXG4jIFxuIyBJTVBPUlRBTlQ6IEZpdmVNIFRlbXBsYXRlIC0gVHdvIERlcGxveW1lbnQgTW9kZXNcbiMgXG4jIE1PREUgMTogU3RhbmRhcmQgRml2ZU0gU2VydmVyXG4jIC0gU2V0IExJQ0VOU0VfS0VZIGVudmlyb25tZW50IHZhcmlhYmxlIChnZXQgZnJlZSBmcm9tIGh0dHBzOi8vZm9ydW0uZml2ZW0ubmV0LylcbiMgLSBMZWF2ZSBOT19ERUZBVUxUX0NPTkZJRyBlbXB0eSBvciB1bnNldFxuIyAtIFNlcnZlciBjb25maWd1cmVkIHZpYSAvY29uZmlnIGZpbGVzXG4jIC0gTm8gd2ViIG1hbmFnZW1lbnQgaW50ZXJmYWNlXG4jXG4jIE1PREUgMjogdHhBZG1pbiBXZWIgSW50ZXJmYWNlICBcbiMgLSBTZXQgTk9fREVGQVVMVF9DT05GSUc9MVxuIyAtIERPIE5PVCBzZXQgTElDRU5TRV9LRVkgKGNvbmZpZ3VyZSB2aWEgd2ViIFVJKVxuIyAtIEFjY2VzcyB3ZWIgbWFuYWdlbWVudCBhdCBodHRwczovL3lvdXItZG9tYWluXG4jIC0gTGljZW5zZSBjb25maWd1cmVkIHRocm91Z2ggdHhBZG1pbiBpbnRlcmZhY2VcbiNcbiMgV0FSTklORzogRG9uJ3QgbWl4IG1vZGVzISBTZXR0aW5nIGJvdGggTElDRU5TRV9LRVkgYW5kIE5PX0RFRkFVTFRfQ09ORklHPTEgY2F1c2VzIGVycm9yc1xuI1xuc2VydmljZXM6XG4gIGZpdmVtOlxuICAgIGltYWdlOiBzcHJpdHNhaWwvZml2ZW06bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB0dHk6IHRydWVcbiAgICBzdGRpbl9vcGVuOiB0cnVlXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIExJQ0VOU0VfS0VZPSR7bGljZW5zZV9rZXl9XG4gICAgICAtIFJDT05fUEFTU1dPUkQ9JHtyY29uX3Bhc3N3b3JkfVxuICAgICAgLSBOT19ERUZBVUxUX0NPTkZJRz0ke05PX0RFRkFVTFRfQ09ORklHOi19XG4gICAgdm9sdW1lczpcbiAgICAgIC0gZml2ZW1fY29uZmlnOi9jb25maWdcbiAgICAgIC0gZml2ZW1fdHhkYXRhOi90eERhdGFcbiAgICBwb3J0czpcbiAgICAgIC0gMzAxMjA6MzAxMjBcbiAgICAgIC0gMzAxMjA6MzAxMjAvdWRwXG4gICAgICAtIDQwMTIwXG4gICAgbGFiZWxzOlxuICAgICAgLSBcInRyYWVmaWsuZW5hYmxlPXRydWVcIlxuXG52b2x1bWVzOlxuICBmaXZlbV9jb25maWc6XG4gIGZpdmVtX3R4ZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxubGljZW5zZV9rZXkgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbnJjb25fcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgICBcIkxJQ0VOU0VfS0VZPSR7bGljZW5zZV9rZXl9XCIsXG4gICAgXCJSQ09OX1BBU1NXT1JEPSR7cmNvbl9wYXNzd29yZH1cIixcbiAgICBcIk5PX0RFRkFVTFRfQ09ORklHPSR7Tk9fREVGQVVMVF9DT05GSUc6LX1cIlxuXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZml2ZW1cIlxucG9ydCA9IDQwMTIwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiIgp9
```

## Links

`gaming`,`gta`,`multiplayer`,`server`

---

Version:`latest`

FirecrawlFirecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data. It can crawl all accessible subpages and provide clean data for each.

FlagsmithFlagsmith is an open-source feature flagging and remote config service.

### On this page

ConfigurationBase64LinksTags