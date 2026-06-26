---
title: "Windows (dockerized) | Dokploy"
source: "https://docs.dokploy.com/docs/templates/windows"
category: dokploy-docs
created: "2026-06-25T17:22:01.421Z"
---

Windows (dockerized) | Dokploy

# Windows (dockerized)

Copy as Markdown

Windows inside a Docker container.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  windows:
    image: dockurr/windows:4.00
    volumes:
      - win-storage:/storage
    environment:
      - VERSION
      - KVM
    devices:
      # If in .env string 'KVM=N' is not commented, you need to comment line below
      - /dev/kvm
    cap_add:
      - NET_ADMIN
    stop_grace_period: 2m

volumes:
  win-storage:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "windows"
port = 8_006
host = "${main_domain}"

[config.env]
VERSION = "win11"
DISK_SIZE = "64G"
RAM_SIZE = "4G"
CPU_CORES = "2"
USERNAME = "Dokploy"
PASSWORD = ""
LANGUAGE = "English"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB3aW5kb3dzOlxuICAgIGltYWdlOiBkb2NrdXJyL3dpbmRvd3M6NC4wMFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHdpbi1zdG9yYWdlOi9zdG9yYWdlXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFZFUlNJT05cbiAgICAgIC0gS1ZNXG4gICAgZGV2aWNlczpcbiAgICAgICMgSWYgaW4gLmVudiBzdHJpbmcgJ0tWTT1OJyBpcyBub3QgY29tbWVudGVkLCB5b3UgbmVlZCB0byBjb21tZW50IGxpbmUgYmVsb3dcbiAgICAgIC0gL2Rldi9rdm1cbiAgICBjYXBfYWRkOlxuICAgICAgLSBORVRfQURNSU5cbiAgICBzdG9wX2dyYWNlX3BlcmlvZDogMm1cblxudm9sdW1lczpcbiAgd2luLXN0b3JhZ2U6IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIndpbmRvd3NcIlxucG9ydCA9IDhfMDA2XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuVkVSU0lPTiA9IFwid2luMTFcIlxuRElTS19TSVpFID0gXCI2NEdcIlxuUkFNX1NJWkUgPSBcIjRHXCJcbkNQVV9DT1JFUyA9IFwiMlwiXG5VU0VSTkFNRSA9IFwiRG9rcGxveVwiXG5QQVNTV09SRCA9IFwiXCJcbkxBTkdVQUdFID0gXCJFbmdsaXNoXCJcbiIKfQ==
```

## Links

`self-hosted`,`open-source`,`os`

---

Version:`4.00`

WindmillA developer platform to build production-grade workflows and internal apps. Open-source alternative to Airplane, Retool, and GitHub Actions.

WordpressWordpress is a free and open source content management system (CMS) for publishing and managing websites.

### On this page

ConfigurationBase64LinksTags