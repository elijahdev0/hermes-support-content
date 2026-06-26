---
title: "Blender | Dokploy"
source: "https://docs.dokploy.com/docs/templates/blender"
category: dokploy-docs
created: "2026-06-25T17:21:42.676Z"
---

Blender | Dokploy

# Blender

Copy as Markdown

Blender is a free and open-source 3D creation suite. It supports the entire 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing and motion tracking, video editing and 2D animation pipeline.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  blender:
    image: lscr.io/linuxserver/blender:latest
    runtime: nvidia
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities:
                - gpu
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
      - NVIDIA_DRIVER_CAPABILITIES=all
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - SUBFOLDER=/ #optional
    ports:
      - 3000
      - 3001
    restart: unless-stopped
    shm_size: 1gb
```

```
[variables]
main_domain = "${domain}"

[config]
env = [
  "PUID=1000",
  "PGID=1000",
  "TZ=Etc/UTC",
  "SUBFOLDER=/",
  "NVIDIA_VISIBLE_DEVICES=all",
  "NVIDIA_DRIVER_CAPABILITIES=all",
]
mounts = []

[[config.domains]]
serviceName = "blender"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGJsZW5kZXI6XG4gICAgaW1hZ2U6IGxzY3IuaW8vbGludXhzZXJ2ZXIvYmxlbmRlcjpsYXRlc3RcbiAgICBydW50aW1lOiBudmlkaWFcbiAgICBkZXBsb3k6XG4gICAgICByZXNvdXJjZXM6XG4gICAgICAgIHJlc2VydmF0aW9uczpcbiAgICAgICAgICBkZXZpY2VzOlxuICAgICAgICAgICAgLSBkcml2ZXI6IG52aWRpYVxuICAgICAgICAgICAgICBjb3VudDogYWxsXG4gICAgICAgICAgICAgIGNhcGFiaWxpdGllczpcbiAgICAgICAgICAgICAgICAtIGdwdVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBOVklESUFfVklTSUJMRV9ERVZJQ0VTPWFsbFxuICAgICAgLSBOVklESUFfRFJJVkVSX0NBUEFCSUxJVElFUz1hbGxcbiAgICAgIC0gUFVJRD0xMDAwXG4gICAgICAtIFBHSUQ9MTAwMFxuICAgICAgLSBUWj1FdGMvVVRDXG4gICAgICAtIFNVQkZPTERFUj0vICNvcHRpb25hbFxuICAgIHBvcnRzOlxuICAgICAgLSAzMDAwXG4gICAgICAtIDMwMDFcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHNobV9zaXplOiAxZ2JcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiUFVJRD0xMDAwXCIsXG4gIFwiUEdJRD0xMDAwXCIsXG4gIFwiVFo9RXRjL1VUQ1wiLFxuICBcIlNVQkZPTERFUj0vXCIsXG4gIFwiTlZJRElBX1ZJU0lCTEVfREVWSUNFUz1hbGxcIixcbiAgXCJOVklESUFfRFJJVkVSX0NBUEFCSUxJVElFUz1hbGxcIixcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImJsZW5kZXJcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`3d`,`rendering`,`animation`

---

Version:`latest`

BigCapitalBigCapital is a great open source alternative to QuickBooks. A comprehensive accounting and financial management system for businesses.

BlinkoBlinko is a modern web application for managing and organizing your digital content and workflows.

### On this page

ConfigurationBase64LinksTags