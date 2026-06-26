---
title: "Cloudflared | Dokploy"
source: "https://docs.dokploy.com/docs/templates/cloudflared"
category: dokploy-docs
created: "2026-06-25T17:21:43.965Z"
---

Cloudflared | Dokploy

# Cloudflared

Copy as Markdown

A lightweight daemon that securely connects local services to the internet through Cloudflare Tunnel.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  cloudflared:
    image: 'cloudflare/cloudflared:latest'
    environment:
      # Don't forget to set this in your Dokploy Environment
      - 'TUNNEL_TOKEN=${CLOUDFLARE_TUNNEL_TOKEN:?}'
    network_mode: host
    restart: unless-stopped
    command: [
      "tunnel",

      # More tunnel run parameters here:
      # https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/cloudflared-parameters/run-parameters/
      "--no-autoupdate",
      #"--protocol", "http2",

      "run"
    ]
```

```
variables = {}

[config]
domains = []
mounts = []

[config.env]
CLOUDFLARE_TUNNEL_TOKEN = ""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBjbG91ZGZsYXJlZDpcbiAgICBpbWFnZTogJ2Nsb3VkZmxhcmUvY2xvdWRmbGFyZWQ6bGF0ZXN0J1xuICAgIGVudmlyb25tZW50OlxuICAgICAgIyBEb24ndCBmb3JnZXQgdG8gc2V0IHRoaXMgaW4geW91ciBEb2twbG95IEVudmlyb25tZW50XG4gICAgICAtICdUVU5ORUxfVE9LRU49JHtDTE9VREZMQVJFX1RVTk5FTF9UT0tFTjo/fSdcbiAgICBuZXR3b3JrX21vZGU6IGhvc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGNvbW1hbmQ6IFtcbiAgICAgIFwidHVubmVsXCIsXG5cbiAgICAgICMgTW9yZSB0dW5uZWwgcnVuIHBhcmFtZXRlcnMgaGVyZTpcbiAgICAgICMgaHR0cHM6Ly9kZXZlbG9wZXJzLmNsb3VkZmxhcmUuY29tL2Nsb3VkZmxhcmUtb25lL25ldHdvcmtzL2Nvbm5lY3RvcnMvY2xvdWRmbGFyZS10dW5uZWwvY29uZmlndXJlLXR1bm5lbHMvY2xvdWRmbGFyZWQtcGFyYW1ldGVycy9ydW4tcGFyYW1ldGVycy9cbiAgICAgIFwiLS1uby1hdXRvdXBkYXRlXCIsXG4gICAgICAjXCItLXByb3RvY29sXCIsIFwiaHR0cDJcIixcblxuICAgICAgXCJydW5cIlxuICAgIF1cbiIsCiAgImNvbmZpZyI6ICJ2YXJpYWJsZXMgPSB7fVxuXG5bY29uZmlnXVxuZG9tYWlucyA9IFtdXG5tb3VudHMgPSBbXVxuXG5bY29uZmlnLmVudl1cbkNMT1VERkxBUkVfVFVOTkVMX1RPS0VOID0gXCJcIlxuIgp9
```

## Links

`cloud`,`networking`,`security`,`tunnel`

---

Version:`latest`

Cloudflare DDNSA small, feature-rich, and robust Cloudflare DDNS updater.

CloudreveSelf-hosted file management and sharing system with multi-cloud storage support. Compatible with local, OneDrive, S3, and various cloud providers.

### On this page

ConfigurationBase64LinksTags