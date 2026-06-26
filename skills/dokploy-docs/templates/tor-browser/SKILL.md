---
title: "Tor Browser | Dokploy"
source: "https://docs.dokploy.com/docs/templates/tor-browser"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

Tor Browser | Dokploy

# Tor Browser

Copy as Markdown

A Dockerized Tor Browser accessible via web VNC (noVNC) and VNC client.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.9"

services:
  tor:
    image: domistyle/tor-browser
    restart: always
    expose:
      - 5800
      - 5900
    environment:
      DISPLAY_WIDTH: ${DISPLAY_WIDTH}
      DISPLAY_HEIGHT: ${DISPLAY_HEIGHT}
      KEEP_APP_RUNNING: ${KEEP_APP_RUNNING}
      TZ: ${TZ}
```

```
[variables]
main_domain = "${domain}"
display_width = "1920"
display_height = "1080"
keep_app_running = "1"
timezone = "Europe/Vienna"

[config]
[[config.domains]]
serviceName = "tor"
port = 5800
host = "${main_domain}"

[config.env]
DISPLAY_WIDTH = "${display_width}"
DISPLAY_HEIGHT = "${display_height}"
KEEP_APP_RUNNING = "${keep_app_running}"
TZ = "${timezone}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy45XCJcblxuc2VydmljZXM6XG4gIHRvcjpcbiAgICBpbWFnZTogZG9taXN0eWxlL3Rvci1icm93c2VyXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZXhwb3NlOlxuICAgICAgLSA1ODAwXG4gICAgICAtIDU5MDBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERJU1BMQVlfV0lEVEg6ICR7RElTUExBWV9XSURUSH1cbiAgICAgIERJU1BMQVlfSEVJR0hUOiAke0RJU1BMQVlfSEVJR0hUfVxuICAgICAgS0VFUF9BUFBfUlVOTklORzogJHtLRUVQX0FQUF9SVU5OSU5HfVxuICAgICAgVFo6ICR7VFp9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGlzcGxheV93aWR0aCA9IFwiMTkyMFwiXG5kaXNwbGF5X2hlaWdodCA9IFwiMTA4MFwiXG5rZWVwX2FwcF9ydW5uaW5nID0gXCIxXCJcbnRpbWV6b25lID0gXCJFdXJvcGUvVmllbm5hXCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInRvclwiXG5wb3J0ID0gNTgwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkRJU1BMQVlfV0lEVEggPSBcIiR7ZGlzcGxheV93aWR0aH1cIlxuRElTUExBWV9IRUlHSFQgPSBcIiR7ZGlzcGxheV9oZWlnaHR9XCJcbktFRVBfQVBQX1JVTk5JTkcgPSBcIiR7a2VlcF9hcHBfcnVubmluZ31cIlxuVFogPSBcIiR7dGltZXpvbmV9XCJcblxuW1tjb25maWcubW91bnRzXV1cbiIKfQ==
```

## Links

`privacy`,`security`,`browser`,`tor`

---

Version:`latest`

TooljetTooljet is an open-source low-code platform that allows you to build internal tools quickly and efficiently. It provides a user-friendly interface for creating applications without extensive coding knowledge.

TrailBaseTrailBase is a blazingly fast, open-source application server with type-safe APIs, built-in WebAssembly runtime, realtime, auth, and admin UI built on Rust, SQLite & Wasmtime.

### On this page

ConfigurationBase64LinksTags