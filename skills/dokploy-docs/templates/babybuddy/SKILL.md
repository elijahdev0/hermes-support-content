---
title: "BabyBuddy | Dokploy"
source: "https://docs.dokploy.com/docs/templates/babybuddy"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

BabyBuddy | Dokploy

# BabyBuddy

Copy as Markdown

BabyBuddy is a comprehensive, user-friendly platform designed to help parents and caregivers manage essential details about their child's growth and development. It provides tools for tracking feedings, sleep schedules, diaper changes, and milestones.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  babybuddy:
    image: linuxserver/babybuddy:2.7.0
    restart: unless-stopped
    ports:
      - 8000
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=UTC
      - CSRF_TRUSTED_ORIGINS=https://${DOMAIN}
      - TIME_ZONE=${TIME_ZONE:-UTC}
      - SECRET_KEY=${SECRET_KEY}
    volumes:
      - config:/config

volumes:
  config: {}
```

```
[variables]
main_domain = "${domain}"
secret_key = "${password:32}"
time_zone = "America/New_York"

[config]
[[config.domains]]
serviceName = "babybuddy"
port = 8000
host = "${main_domain}"

[config.env]
DOMAIN = "${main_domain}"
SECRET_KEY = "${secret_key}"
TIME_ZONE = "${time_zone}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBiYWJ5YnVkZHk6XG4gICAgaW1hZ2U6IGxpbnV4c2VydmVyL2JhYnlidWRkeToyLjcuMFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDgwMDBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUFVJRD0xMDAwXG4gICAgICAtIFBHSUQ9MTAwMFxuICAgICAgLSBUWj1VVENcbiAgICAgIC0gQ1NSRl9UUlVTVEVEX09SSUdJTlM9aHR0cHM6Ly8ke0RPTUFJTn1cbiAgICAgIC0gVElNRV9aT05FPSR7VElNRV9aT05FOi1VVEN9XG4gICAgICAtIFNFQ1JFVF9LRVk9JHtTRUNSRVRfS0VZfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGNvbmZpZzovY29uZmlnXG5cbnZvbHVtZXM6XG4gIGNvbmZpZzoge30gIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnNlY3JldF9rZXkgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbnRpbWVfem9uZSA9IFwiQW1lcmljYS9OZXdfWW9ya1wiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJiYWJ5YnVkZHlcIlxucG9ydCA9IDgwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5ET01BSU4gPSBcIiR7bWFpbl9kb21haW59XCJcblNFQ1JFVF9LRVkgPSBcIiR7c2VjcmV0X2tleX1cIlxuVElNRV9aT05FID0gXCIke3RpbWVfem9uZX1cIiAiCn0=
```

## Links

`parenting`,`tracking`,`family`

---

Version:`2.7.0`

AzuraCastAzuraCast is a self-hosted, all-in-one web radio management suite. Easily manage your online radio stations with a powerful web interface.

BackrestBackrest is a web-based backup solution powered by restic, offering an intuitive WebUI for easy repository management, snapshot browsing, and file restoration. It runs in the background, automating snapshot scheduling and repository maintenance. Built with Go, Backrest is a lightweight standalone binary with restic as its only dependency. It provides a secure and user-friendly way to manage backups while still allowing direct access to the restic CLI for advanced operations.

### On this page

ConfigurationBase64LinksTags