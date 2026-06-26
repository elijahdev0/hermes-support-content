---
title: "InfluxDB | Dokploy"
source: "https://docs.dokploy.com/docs/templates/influxdb"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

InfluxDB | Dokploy

# InfluxDB

Copy as Markdown

InfluxDB 2.7 is the platform purpose-built to collect, store, process and visualize time series data.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  influxdb:
    image: influxdb:2.7.10
    restart: unless-stopped
    volumes:
      - influxdb2-data:/var/lib/influxdb2
      - influxdb2-config:/etc/influxdb2

volumes:
  influxdb2-data:
  influxdb2-config:
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "influxdb"
port = 8_086
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBpbmZsdXhkYjpcbiAgICBpbWFnZTogaW5mbHV4ZGI6Mi43LjEwXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBpbmZsdXhkYjItZGF0YTovdmFyL2xpYi9pbmZsdXhkYjJcbiAgICAgIC0gaW5mbHV4ZGIyLWNvbmZpZzovZXRjL2luZmx1eGRiMlxuXG52b2x1bWVzOlxuICBpbmZsdXhkYjItZGF0YTpcbiAgaW5mbHV4ZGIyLWNvbmZpZzoiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0ge31cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImluZmx1eGRiXCJcbnBvcnQgPSA4XzA4NlxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`self-hosted`,`open-source`,`storage`,`database`

---

Version:`2.7.10`

InfisicalAll-in-one platform to securely manage application configuration and secrets across your team and infrastructure.

InngestInngest is a developer platform for serverless event-driven workflows. Build reliable, scalable background functions and workflows with built-in retries, scheduling, and observability.

### On this page

ConfigurationBase64LinksTags