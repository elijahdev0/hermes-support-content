---
title: "Dragonfly | Dokploy"
source: "https://docs.dokploy.com/docs/templates/dragonfly-db"
category: dokploy-docs
created: "2026-06-25T17:21:46.246Z"
---

Dragonfly | Dokploy

# Dragonfly

Copy as Markdown

Dragonfly is a drop-in Redis replacement that is designed for heavy data workloads running on modern cloud hardware.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'
services:
  dragonflydb:
    image: 'docker.dragonflydb.io/dragonflydb/dragonfly'
    ulimits:
      memlock: -1
    ports:
      - "6379:6379"
    volumes:
      - dragonflydata:/data
    environment:
      - DFLY_requirepass
volumes:
  dragonflydata:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:32}"
any_helper = "${uuid}"

[config]
env = [
    "DFLY_requirepass=${db_password}",
]

[[config.domains]]
serviceName = "dragonflydb"
port = 6379
host = "${main_domain}"
path = "/"

[[config.mounts]]
filePath = "/content/configuration.conf"
content = """
bind-address = "0.0.0.0"
port = 6379
log-level = "info"
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5zZXJ2aWNlczpcbiAgZHJhZ29uZmx5ZGI6XG4gICAgaW1hZ2U6ICdkb2NrZXIuZHJhZ29uZmx5ZGIuaW8vZHJhZ29uZmx5ZGIvZHJhZ29uZmx5J1xuICAgIHVsaW1pdHM6XG4gICAgICBtZW1sb2NrOiAtMVxuICAgIHBvcnRzOlxuICAgICAgLSBcIjYzNzk6NjM3OVwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZHJhZ29uZmx5ZGF0YTovZGF0YVxuICAgIGVudmlyb25tZW50OiBcbiAgICAgIC0gREZMWV9yZXF1aXJlcGFzc1xudm9sdW1lczpcbiAgZHJhZ29uZmx5ZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmFueV9oZWxwZXIgPSBcIiR7dXVpZH1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICAgIFwiREZMWV9yZXF1aXJlcGFzcz0ke2RiX3Bhc3N3b3JkfVwiLFxuXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJkcmFnb25mbHlkYlwiXG5wb3J0ID0gNjM3OVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxucGF0aCA9IFwiL1wiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL2NvbnRlbnQvY29uZmlndXJhdGlvbi5jb25mXCJcbmNvbnRlbnQgPSBcIlwiXCJcbmJpbmQtYWRkcmVzcyA9IFwiMC4wLjAuMFwiXG5wb3J0ID0gNjM3OVxubG9nLWxldmVsID0gXCJpbmZvXCJcblwiXCJcIlxuIgp9
```

## Links

`database`,`redis`

---

Version:`1.28.1`

DozzleDozzle is a lightweight, real-time log viewer for Docker containers.

draw.iodraw.io is a configurable diagramming/whiteboarding visualization application.

### On this page

ConfigurationBase64LinksTags