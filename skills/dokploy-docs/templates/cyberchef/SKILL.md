---
title: "CyberChef | Dokploy"
source: "https://docs.dokploy.com/docs/templates/cyberchef"
category: dokploy-docs
created: "2026-06-25T17:21:45.078Z"
---

CyberChef | Dokploy

# CyberChef

Copy as Markdown

CyberChef is a web application for encryption, encoding, compression, and data analysis, developed by GCHQ.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  cyberchef:
    image: ghcr.io/gchq/cyberchef:latest
    restart: unless-stopped
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "cyberchef"
port = 80
host = "${main_domain}"
path = "/"

[config.env]
# No environment variables required for basic CyberChef setup
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBjeWJlcmNoZWY6XG4gICAgaW1hZ2U6IGdoY3IuaW8vZ2NocS9jeWJlcmNoZWY6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjeWJlcmNoZWZcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5wYXRoID0gXCIvXCJcblxuW2NvbmZpZy5lbnZdXG4jIE5vIGVudmlyb25tZW50IHZhcmlhYmxlcyByZXF1aXJlZCBmb3IgYmFzaWMgQ3liZXJDaGVmIHNldHVwICIKfQ==
```

## Links

`security`,`encryption`,`data-analysis`

---

Version:`latest`

CupCup is a self-hosted Docker container management UI.

DashyA self-hostable personal dashboard built for you. Includes status-checking, widgets, themes, icon packs, a UI editor and tons more!

### On this page

ConfigurationBase64LinksTags