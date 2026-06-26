---
title: "MacOS (dockerized) | Dokploy"
source: "https://docs.dokploy.com/docs/templates/macos"
category: dokploy-docs
created: "2026-06-25T17:21:52.047Z"
---

MacOS (dockerized) | Dokploy

# MacOS (dockerized)

Copy as Markdown

MacOS inside a Docker container.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  macos:
    image: dockurr/macos:1.14
    volumes:
    - macos-storage:/storage
    environment:
      - VERSION
    devices:
      # If in .env string 'KVM=N' is not commented, you need to comment line below
      - /dev/kvm
    cap_add:
      - NET_ADMIN
    stop_grace_period: 2m

volumes:
  macos-storage:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "macos"
port = 8_006
host = "${main_domain}"

[config.env]
VERSION = "15"
DISK_SIZE = "64G"
RAM_SIZE = "4G"
CPU_CORES = "2"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBtYWNvczpcbiAgICBpbWFnZTogZG9ja3Vyci9tYWNvczoxLjE0XG4gICAgdm9sdW1lczpcbiAgICAtIG1hY29zLXN0b3JhZ2U6L3N0b3JhZ2VcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gVkVSU0lPTlxuICAgIGRldmljZXM6XG4gICAgICAjIElmIGluIC5lbnYgc3RyaW5nICdLVk09TicgaXMgbm90IGNvbW1lbnRlZCwgeW91IG5lZWQgdG8gY29tbWVudCBsaW5lIGJlbG93XG4gICAgICAtIC9kZXYva3ZtXG4gICAgY2FwX2FkZDpcbiAgICAgIC0gTkVUX0FETUlOXG4gICAgc3RvcF9ncmFjZV9wZXJpb2Q6IDJtXG5cbnZvbHVtZXM6XG4gIG1hY29zLXN0b3JhZ2U6IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIm1hY29zXCJcbnBvcnQgPSA4XzAwNlxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblZFUlNJT04gPSBcIjE1XCJcbkRJU0tfU0laRSA9IFwiNjRHXCJcblJBTV9TSVpFID0gXCI0R1wiXG5DUFVfQ09SRVMgPSBcIjJcIlxuIgp9
```

## Links

`self-hosted`,`open-source`,`os`

---

Version:`1.14`

LowcoderRapid business App Builder for Everyone

Mage AIBuild, run, and manage data pipelines for integrating and transforming data.

### On this page

ConfigurationBase64LinksTags