---
title: "Netdata | Dokploy"
source: "https://docs.dokploy.com/docs/templates/netdata"
category: dokploy-docs
created: "2026-06-25T17:21:54.354Z"
---

Netdata | Dokploy

# Netdata

Copy as Markdown

Netdata is a real-time performance monitoring tool that provides comprehensive system metrics, application monitoring, and infrastructure health insights.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  netdata:
    image: netdata/netdata:latest
    restart: unless-stopped
    cap_add:
      - SYS_PTRACE
      - SYS_ADMIN
    security_opt:
      - apparmor:unconfined
    volumes:
      - netdata-config:/etc/netdata
      - netdata-lib:/var/lib/netdata
      - netdata-cache:/var/cache/netdata
      - /etc/passwd:/host/etc/passwd:ro
      - /etc/group:/host/etc/group:ro
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /etc/os-release:/host/etc/os-release:ro
      - /var/run/docker.sock:/var/run/docker.sock:ro
    environment:
      - NETDATA_CLAIM_TOKEN=${NETDATA_CLAIM_TOKEN:-}
      - NETDATA_CLAIM_URL=${NETDATA_CLAIM_URL:-}
      - NETDATA_CLAIM_ROOMS=${NETDATA_CLAIM_ROOMS:-}
    ports:
      - "19999"

volumes:
  netdata-config:
  netdata-lib:
  netdata-cache:
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "netdata"
port = 19999
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBuZXRkYXRhOlxuICAgIGltYWdlOiBuZXRkYXRhL25ldGRhdGE6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBjYXBfYWRkOlxuICAgICAgLSBTWVNfUFRSQUNFXG4gICAgICAtIFNZU19BRE1JTlxuICAgIHNlY3VyaXR5X29wdDpcbiAgICAgIC0gYXBwYXJtb3I6dW5jb25maW5lZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIG5ldGRhdGEtY29uZmlnOi9ldGMvbmV0ZGF0YVxuICAgICAgLSBuZXRkYXRhLWxpYjovdmFyL2xpYi9uZXRkYXRhXG4gICAgICAtIG5ldGRhdGEtY2FjaGU6L3Zhci9jYWNoZS9uZXRkYXRhXG4gICAgICAtIC9ldGMvcGFzc3dkOi9ob3N0L2V0Yy9wYXNzd2Q6cm9cbiAgICAgIC0gL2V0Yy9ncm91cDovaG9zdC9ldGMvZ3JvdXA6cm9cbiAgICAgIC0gL3Byb2M6L2hvc3QvcHJvYzpyb1xuICAgICAgLSAvc3lzOi9ob3N0L3N5czpyb1xuICAgICAgLSAvZXRjL29zLXJlbGVhc2U6L2hvc3QvZXRjL29zLXJlbGVhc2U6cm9cbiAgICAgIC0gL3Zhci9ydW4vZG9ja2VyLnNvY2s6L3Zhci9ydW4vZG9ja2VyLnNvY2s6cm9cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTkVUREFUQV9DTEFJTV9UT0tFTj0ke05FVERBVEFfQ0xBSU1fVE9LRU46LX1cbiAgICAgIC0gTkVUREFUQV9DTEFJTV9VUkw9JHtORVREQVRBX0NMQUlNX1VSTDotfVxuICAgICAgLSBORVREQVRBX0NMQUlNX1JPT01TPSR7TkVUREFUQV9DTEFJTV9ST09NUzotfVxuICAgIHBvcnRzOlxuICAgICAgLSBcIjE5OTk5XCJcblxudm9sdW1lczpcbiAgbmV0ZGF0YS1jb25maWc6XG4gIG5ldGRhdGEtbGliOlxuICBuZXRkYXRhLWNhY2hlOlxuXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0ge31cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIm5ldGRhdGFcIlxucG9ydCA9IDE5OTk5XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbiIKfQ==
```

## Links

`monitoring`,`metrics`,`analytics`,`performance`,`infrastructure`

---

Version:`latest`

NekoNeko is a self-hosted virtual browser that runs in Docker and allows you to share browser sessions with others.

Networking ToolboxA collection of handy networking utilities by Lissy93, packaged as a self-hostable web app.

### On this page

ConfigurationBase64LinksTags