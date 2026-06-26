---
title: "Enshrouded | Dokploy"
source: "https://docs.dokploy.com/docs/templates/enshrouded"
category: dokploy-docs
created: "2026-06-25T17:21:47.358Z"
---

Enshrouded | Dokploy

# Enshrouded

Copy as Markdown

Enshrouded steam dedicated server.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  enshrouded:
    image: mornedhels/enshrouded-server:latest
    container_name: enshrouded
    hostname: enshrouded
    restart: unless-stopped
    stop_grace_period: 90s
    ports:
      - "15637:15637/udp"
      - "27015:27015/udp"
    volumes:
      - enshrouded-persistent-data:/opt/enshrouded
    # only add ntsync device if your kernel supports it (6.14 or newer)
    # devices:
    #   - /dev/ntsync:/dev/ntsync
    environment:
      - SERVER_NAME=${SERVER_NAME}
      - SERVER_PASSWORD=${SERVER_PASSWORD}
      - SERVER_SLOT_COUNT=6
      - UPDATE_CRON=0 3 * * *
      - PUID=4711
      - PGID=4711

volumes:
  enshrouded-persistent-data:
```

```
[variables]
SERVER_NAME = "Enshrouded Dokploy"
SERVER_PASSWORD = "${password:15}"

[config]
domains = []
mounts = []
env = [
    "SERVER_NAME=${SERVER_NAME}",
    "SERVER_PASSWORD=${SERVER_PASSWORD}"
]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBlbnNocm91ZGVkOlxuICAgIGltYWdlOiBtb3JuZWRoZWxzL2Vuc2hyb3VkZWQtc2VydmVyOmxhdGVzdFxuICAgIGNvbnRhaW5lcl9uYW1lOiBlbnNocm91ZGVkXG4gICAgaG9zdG5hbWU6IGVuc2hyb3VkZWRcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHN0b3BfZ3JhY2VfcGVyaW9kOiA5MHNcbiAgICBwb3J0czpcbiAgICAgIC0gXCIxNTYzNzoxNTYzNy91ZHBcIlxuICAgICAgLSBcIjI3MDE1OjI3MDE1L3VkcFwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZW5zaHJvdWRlZC1wZXJzaXN0ZW50LWRhdGE6L29wdC9lbnNocm91ZGVkXG4gICAgIyBvbmx5IGFkZCBudHN5bmMgZGV2aWNlIGlmIHlvdXIga2VybmVsIHN1cHBvcnRzIGl0ICg2LjE0IG9yIG5ld2VyKVxuICAgICMgZGV2aWNlczpcbiAgICAjICAgLSAvZGV2L250c3luYzovZGV2L250c3luY1xuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBTRVJWRVJfTkFNRT0ke1NFUlZFUl9OQU1FfVxuICAgICAgLSBTRVJWRVJfUEFTU1dPUkQ9JHtTRVJWRVJfUEFTU1dPUkR9XG4gICAgICAtIFNFUlZFUl9TTE9UX0NPVU5UPTZcbiAgICAgIC0gVVBEQVRFX0NST049MCAzICogKiAqXG4gICAgICAtIFBVSUQ9NDcxMVxuICAgICAgLSBQR0lEPTQ3MTFcblxudm9sdW1lczpcbiAgZW5zaHJvdWRlZC1wZXJzaXN0ZW50LWRhdGE6IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5TRVJWRVJfTkFNRSA9IFwiRW5zaHJvdWRlZCBEb2twbG95XCJcblNFUlZFUl9QQVNTV09SRCA9IFwiJHtwYXNzd29yZDoxNX1cIlxuXG5bY29uZmlnXVxuZG9tYWlucyA9IFtdXG5tb3VudHMgPSBbXVxuZW52ID0gW1xuICAgIFwiU0VSVkVSX05BTUU9JHtTRVJWRVJfTkFNRX1cIixcbiAgICBcIlNFUlZFUl9QQVNTV09SRD0ke1NFUlZFUl9QQVNTV09SRH1cIlxuXSIKfQ==
```

## Links

`gaming`

---

Version:`1.0.0`

EMQXA scalable and reliable MQTT broker for AI, IoT, IIoT and connected vehicles

ERPNext100% Open Source and highly customizable ERP software.

### On this page

ConfigurationBase64LinksTags