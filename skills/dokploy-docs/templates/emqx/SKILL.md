---
title: "EMQX | Dokploy"
source: "https://docs.dokploy.com/docs/templates/emqx"
category: dokploy-docs
created: "2026-06-25T17:21:47.358Z"
---

EMQX | Dokploy

# EMQX

Copy as Markdown

A scalable and reliable MQTT broker for AI, IoT, IIoT and connected vehicles

## Configuration

docker-compose.ymltemplate.toml

```
# This templates requires additional traefik port mapping and entry point
# for port 8883 (mqtts over TCP)
#
# For the full instructions, refer to:
# - https://github.com/Dokploy/dokploy/discussions/3126
#
# The initial login credentials are:
# - USERNAME: admin
# - PASSWORD: public

services:
  emqx:
    image: emqx/emqx-enterprise:6.0.1
    hostname: node1.emqx.com
    environment:
      EMQX_NODE_NAME: [email protected]
    expose:
      - 1883  # MQTT
      - 8083  # WS
      - 18083 # Dashboard
    volumes:
      - emqx_data:/opt/emqx/data
      - emqx_log:/opt/emqx/log
    networks:
      dokploy-network:
        aliases:
          - emqx-service
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "/opt/emqx/bin/emqx_ctl", "status"]
      interval: 30s
      timeout: 5s
      retries: 3
    labels:
      # MQTT over TLS
      - "traefik.tcp.routers.emqx-mqtts.entrypoints=mqtts"
      - "traefik.tcp.routers.emqx-mqtts.rule=HostSNI(`broker.yourdomain.com`)" # Change domain
      - "traefik.tcp.routers.emqx-mqtts.tls.certresolver=letsencrypt"
      - "traefik.tcp.routers.emqx-mqtts.service=emqx-service"
      - "traefik.tcp.services.emqx-service.loadbalancer.server.port=1883"

  #
  # Optional Web UI:
  # - https://github.com/emqx/MQTTX/tree/main/web
  #
  # mqttx-web:
  #   image: emqx/mqttx-web:latest
  #   expose:
  #     - 80
  #

volumes:
  emqx_data:
  emqx_log:

networks:
  dokploy-network:
    external: true
```

```
[variables]

[[config.domains]]
serviceName = "emqx"
port = 18083
host = "emqx.yourdomain.com"

[[config.domains]]
serviceName = "emqx"
port = 8083
host = "broker.yourdomain.com"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgVGhpcyB0ZW1wbGF0ZXMgcmVxdWlyZXMgYWRkaXRpb25hbCB0cmFlZmlrIHBvcnQgbWFwcGluZyBhbmQgZW50cnkgcG9pbnRcbiMgZm9yIHBvcnQgODg4MyAobXF0dHMgb3ZlciBUQ1ApXG4jXG4jIEZvciB0aGUgZnVsbCBpbnN0cnVjdGlvbnMsIHJlZmVyIHRvOlxuIyAtIGh0dHBzOi8vZ2l0aHViLmNvbS9Eb2twbG95L2Rva3Bsb3kvZGlzY3Vzc2lvbnMvMzEyNlxuI1xuIyBUaGUgaW5pdGlhbCBsb2dpbiBjcmVkZW50aWFscyBhcmU6XG4jIC0gVVNFUk5BTUU6IGFkbWluXG4jIC0gUEFTU1dPUkQ6IHB1YmxpY1xuXG5zZXJ2aWNlczpcbiAgZW1xeDpcbiAgICBpbWFnZTogZW1xeC9lbXF4LWVudGVycHJpc2U6Ni4wLjFcbiAgICBob3N0bmFtZTogbm9kZTEuZW1xeC5jb21cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEVNUVhfTk9ERV9OQU1FOiBlbXF4QG5vZGUxLmVtcXguY29tXG4gICAgZXhwb3NlOlxuICAgICAgLSAxODgzICAjIE1RVFRcbiAgICAgIC0gODA4MyAgIyBXU1xuICAgICAgLSAxODA4MyAjIERhc2hib2FyZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGVtcXhfZGF0YTovb3B0L2VtcXgvZGF0YVxuICAgICAgLSBlbXF4X2xvZzovb3B0L2VtcXgvbG9nXG4gICAgbmV0d29ya3M6XG4gICAgICBkb2twbG95LW5ldHdvcms6XG4gICAgICAgIGFsaWFzZXM6XG4gICAgICAgICAgLSBlbXF4LXNlcnZpY2VcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwiL29wdC9lbXF4L2Jpbi9lbXF4X2N0bFwiLCBcInN0YXR1c1wiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDNcbiAgICBsYWJlbHM6XG4gICAgICAjIE1RVFQgb3ZlciBUTFNcbiAgICAgIC0gXCJ0cmFlZmlrLnRjcC5yb3V0ZXJzLmVtcXgtbXF0dHMuZW50cnlwb2ludHM9bXF0dHNcIlxuICAgICAgLSBcInRyYWVmaWsudGNwLnJvdXRlcnMuZW1xeC1tcXR0cy5ydWxlPUhvc3RTTkkoYGJyb2tlci55b3VyZG9tYWluLmNvbWApXCIgIyBDaGFuZ2UgZG9tYWluXG4gICAgICAtIFwidHJhZWZpay50Y3Aucm91dGVycy5lbXF4LW1xdHRzLnRscy5jZXJ0cmVzb2x2ZXI9bGV0c2VuY3J5cHRcIlxuICAgICAgLSBcInRyYWVmaWsudGNwLnJvdXRlcnMuZW1xeC1tcXR0cy5zZXJ2aWNlPWVtcXgtc2VydmljZVwiXG4gICAgICAtIFwidHJhZWZpay50Y3Auc2VydmljZXMuZW1xeC1zZXJ2aWNlLmxvYWRiYWxhbmNlci5zZXJ2ZXIucG9ydD0xODgzXCJcblxuICAjXG4gICMgT3B0aW9uYWwgV2ViIFVJOlxuICAjIC0gaHR0cHM6Ly9naXRodWIuY29tL2VtcXgvTVFUVFgvdHJlZS9tYWluL3dlYlxuICAjXG4gICMgbXF0dHgtd2ViOlxuICAjICAgaW1hZ2U6IGVtcXgvbXF0dHgtd2ViOmxhdGVzdFxuICAjICAgZXhwb3NlOlxuICAjICAgICAtIDgwXG4gICNcblxudm9sdW1lczpcbiAgZW1xeF9kYXRhOlxuICBlbXF4X2xvZzpcblxubmV0d29ya3M6XG4gIGRva3Bsb3ktbmV0d29yazpcbiAgICBleHRlcm5hbDogdHJ1ZVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImVtcXhcIlxucG9ydCA9IDE4MDgzXG5ob3N0ID0gXCJlbXF4LnlvdXJkb21haW4uY29tXCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZW1xeFwiXG5wb3J0ID0gODA4M1xuaG9zdCA9IFwiYnJva2VyLnlvdXJkb21haW4uY29tXCJcbiIKfQ==
```

## Links

`broker`,`iot`,`mqtt`

---

Version:`6.0.1`

EmbyEmby Server is a personal media server with apps on just about every device.

EnshroudedEnshrouded steam dedicated server.

### On this page

ConfigurationBase64LinksTags