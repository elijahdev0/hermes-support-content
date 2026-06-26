---
title: "Home Assistant | Dokploy"
source: "https://docs.dokploy.com/docs/templates/homeassistant"
category: dokploy-docs
created: "2026-06-25T17:21:49.750Z"
---

Home Assistant | Dokploy

# Home Assistant

Copy as Markdown

Open source home automation that puts local control and privacy first.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  homeassistant:
    image: ghcr.io/home-assistant/home-assistant:stable
    restart: unless-stopped
    ports:
      - 8123
    volumes:
      - ../files/configuration.yaml:/config/configuration.yaml
      - ../files/automations.yaml:/config/automations.yaml
      - ../files/scripts.yaml:/config/scripts.yaml
      - ../files/scenes.yaml:/config/scenes.yaml
      - /opt/homeassistant:/config
      - /etc/localtime:/etc/localtime:ro
      - /run/dbus:/run/dbus:ro
    healthcheck:
      test: ["CMD", "curl", "-f", "http://homeassistant:8123/"]
      interval: 60s
      retries: 5
      start_period: 300s
      timeout: 2s
```

```
[variables]
main_domain = "${domain}"

[config]

[[config.domains]]
serviceName = "homeassistant"
port = 8123
host = "${main_domain}"

env = []

[[config.mounts]]
filePath = "configuration.yaml"
content = """

# Loads default set of integrations. Do not remove.
default_config:

# Load frontend themes from the themes folder
frontend:
  themes: !include_dir_merge_named themes

automation: !include automations.yaml
script: !include scripts.yaml
scene: !include scenes.yaml

http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 192.168.0.0/16 # Local LAN Subnet
    - 172.0.0.0/8 # Docker Subnet
    - 10.0.0.0/16 # Docker Swarm Subnet
"""

[[config.mounts]]
filePath = "automations.yaml"
content = """
"""

[[config.mounts]]
filePath = "scripts.yaml"
content = """
"""

[[config.mounts]]
filePath = "scenes.yaml"
content = """
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBob21lYXNzaXN0YW50OlxuICAgIGltYWdlOiBnaGNyLmlvL2hvbWUtYXNzaXN0YW50L2hvbWUtYXNzaXN0YW50OnN0YWJsZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDgxMjNcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9jb25maWd1cmF0aW9uLnlhbWw6L2NvbmZpZy9jb25maWd1cmF0aW9uLnlhbWxcbiAgICAgIC0gLi4vZmlsZXMvYXV0b21hdGlvbnMueWFtbDovY29uZmlnL2F1dG9tYXRpb25zLnlhbWxcbiAgICAgIC0gLi4vZmlsZXMvc2NyaXB0cy55YW1sOi9jb25maWcvc2NyaXB0cy55YW1sXG4gICAgICAtIC4uL2ZpbGVzL3NjZW5lcy55YW1sOi9jb25maWcvc2NlbmVzLnlhbWxcbiAgICAgIC0gL29wdC9ob21lYXNzaXN0YW50Oi9jb25maWdcbiAgICAgIC0gL2V0Yy9sb2NhbHRpbWU6L2V0Yy9sb2NhbHRpbWU6cm9cbiAgICAgIC0gL3J1bi9kYnVzOi9ydW4vZGJ1czpyb1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwiY3VybFwiLCBcIi1mXCIsIFwiaHR0cDovL2hvbWVhc3Npc3RhbnQ6ODEyMy9cIl1cbiAgICAgIGludGVydmFsOiA2MHNcbiAgICAgIHJldHJpZXM6IDVcbiAgICAgIHN0YXJ0X3BlcmlvZDogMzAwc1xuICAgICAgdGltZW91dDogMnNcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImhvbWVhc3Npc3RhbnRcIlxucG9ydCA9IDgxMjNcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuZW52ID0gW11cblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCJjb25maWd1cmF0aW9uLnlhbWxcIlxuY29udGVudCA9IFwiXCJcIlxuXG4jIExvYWRzIGRlZmF1bHQgc2V0IG9mIGludGVncmF0aW9ucy4gRG8gbm90IHJlbW92ZS5cbmRlZmF1bHRfY29uZmlnOlxuXG4jIExvYWQgZnJvbnRlbmQgdGhlbWVzIGZyb20gdGhlIHRoZW1lcyBmb2xkZXJcbmZyb250ZW5kOlxuICB0aGVtZXM6ICFpbmNsdWRlX2Rpcl9tZXJnZV9uYW1lZCB0aGVtZXNcblxuYXV0b21hdGlvbjogIWluY2x1ZGUgYXV0b21hdGlvbnMueWFtbFxuc2NyaXB0OiAhaW5jbHVkZSBzY3JpcHRzLnlhbWxcbnNjZW5lOiAhaW5jbHVkZSBzY2VuZXMueWFtbFxuXG5odHRwOlxuICB1c2VfeF9mb3J3YXJkZWRfZm9yOiB0cnVlXG4gIHRydXN0ZWRfcHJveGllczpcbiAgICAtIDE5Mi4xNjguMC4wLzE2ICMgTG9jYWwgTEFOIFN1Ym5ldFxuICAgIC0gMTcyLjAuMC4wLzggIyBEb2NrZXIgU3VibmV0XG4gICAgLSAxMC4wLjAuMC8xNiAjIERvY2tlciBTd2FybSBTdWJuZXRcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcImF1dG9tYXRpb25zLnlhbWxcIlxuY29udGVudCA9IFwiXCJcIlxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwic2NyaXB0cy55YW1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcInNjZW5lcy55YW1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcblwiXCJcIlxuIgp9
```

## Links

`iot`,`home-automation`,`internet-of-things`,`self-hosted`,`server`

---

Version:`stable`

HomarrA sleek, modern dashboard that puts all your apps and services in one place with Docker integration.

HomebridgeBringing HomeKit support where there is none. Homebridge allows you to integrate with smart home devices that do not natively support HomeKit.

### On this page

ConfigurationBase64LinksTags