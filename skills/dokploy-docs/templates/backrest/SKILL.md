---
title: "Backrest | Dokploy"
source: "https://docs.dokploy.com/docs/templates/backrest"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

Backrest | Dokploy

# Backrest

Copy as Markdown

Backrest is a web-based backup solution powered by restic, offering an intuitive WebUI for easy repository management, snapshot browsing, and file restoration. It runs in the background, automating snapshot scheduling and repository maintenance. Built with Go, Backrest is a lightweight standalone binary with restic as its only dependency. It provides a secure and user-friendly way to manage backups while still allowing direct access to the restic CLI for advanced operations.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  backrest:
    image: garethgeorge/backrest:v1.7.3
    restart: unless-stopped
    ports:
      - 9898
    environment:
      - BACKREST_PORT=9898
      - BACKREST_DATA=/data # where it stores current state data
      - BACKREST_CONFIG=/config/config.json # where it stores backup configurations
      - XDG_CACHE_HOME=/cache # backup cache
      - TZ=${TZ}
    volumes:
      - backrest/data:/data
      - backrest/config:/config
      - backrest/config:/cache # to preserve backup cache between restarts
      - /:/userdata:ro # we mount /mnt/data to /userdata (that we want to backup)

volumes:
  backrest:
  backrest-cache:
```

```
[variables]
main_domain = "${domain}"

[config]
env = ["TZ=Europe/Paris"]
mounts = []

[[config.domains]]
serviceName = "backrest"
port = 9_898
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBiYWNrcmVzdDpcbiAgICBpbWFnZTogZ2FyZXRoZ2VvcmdlL2JhY2tyZXN0OnYxLjcuM1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDk4OThcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQkFDS1JFU1RfUE9SVD05ODk4XG4gICAgICAtIEJBQ0tSRVNUX0RBVEE9L2RhdGEgIyB3aGVyZSBpdCBzdG9yZXMgY3VycmVudCBzdGF0ZSBkYXRhXG4gICAgICAtIEJBQ0tSRVNUX0NPTkZJRz0vY29uZmlnL2NvbmZpZy5qc29uICMgd2hlcmUgaXQgc3RvcmVzIGJhY2t1cCBjb25maWd1cmF0aW9uc1xuICAgICAgLSBYREdfQ0FDSEVfSE9NRT0vY2FjaGUgIyBiYWNrdXAgY2FjaGVcbiAgICAgIC0gVFo9JHtUWn1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBiYWNrcmVzdC9kYXRhOi9kYXRhXG4gICAgICAtIGJhY2tyZXN0L2NvbmZpZzovY29uZmlnXG4gICAgICAtIGJhY2tyZXN0L2NvbmZpZzovY2FjaGUgIyB0byBwcmVzZXJ2ZSBiYWNrdXAgY2FjaGUgYmV0d2VlbiByZXN0YXJ0c1xuICAgICAgLSAvOi91c2VyZGF0YTpybyAjIHdlIG1vdW50IC9tbnQvZGF0YSB0byAvdXNlcmRhdGEgKHRoYXQgd2Ugd2FudCB0byBiYWNrdXApXG5cbnZvbHVtZXM6XG4gIGJhY2tyZXN0OiBcbiAgYmFja3Jlc3QtY2FjaGU6IFxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcIlRaPUV1cm9wZS9QYXJpc1wiXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYmFja3Jlc3RcIlxucG9ydCA9IDlfODk4XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`backup`

---

Version:`1.6.0`

BabyBuddyBabyBuddy is a comprehensive, user-friendly platform designed to help parents and caregivers manage essential details about their child's growth and development. It provides tools for tracking feedings, sleep schedules, diaper changes, and milestones.

BaikalBaikal is a lightweight, self-hosted CalDAV and CardDAV server that enables users to manage calendars and contacts efficiently. It provides a simple and effective solution for syncing and sharing events, tasks, and address books across multiple devices.

### On this page

ConfigurationBase64LinksTags