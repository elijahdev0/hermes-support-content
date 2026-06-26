---
title: "Cloudflare DDNS | Dokploy"
source: "https://docs.dokploy.com/docs/templates/cloudflare-ddns"
category: dokploy-docs
created: "2026-06-25T17:21:43.965Z"
---

Cloudflare DDNS | Dokploy

# Cloudflare DDNS

Copy as Markdown

A small, feature-rich, and robust Cloudflare DDNS updater.

## Configuration

docker-compose.ymltemplate.toml

```
# For more details, see:
# - https://github.com/favonia/cloudflare-ddns
services:
  cloudflare-ddns:
    image: favonia/cloudflare-ddns:1
    network_mode: host
    restart: unless-stopped
    user: "1000:1000"
    read_only: true
    cap_drop: [all]
    security_opt: [no-new-privileges:true]
    environment:
      - CLOUDFLARE_API_TOKEN=${CLOUDFLARE_API_TOKEN:?}
      - DOMAINS=${DOMAINS:?}
      - PROXIED=false
      - IP6_PROVIDER=none
```

```
variables = {}

[config]
domains = []
mounts = []

[config.env]
CLOUDFLARE_API_TOKEN = "<INSERT YOUR TOKEN>"
DOMAINS = "example.org,www.example.org,example.io"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgRm9yIG1vcmUgZGV0YWlscywgc2VlOlxuIyAtIGh0dHBzOi8vZ2l0aHViLmNvbS9mYXZvbmlhL2Nsb3VkZmxhcmUtZGRuc1xuc2VydmljZXM6XG4gIGNsb3VkZmxhcmUtZGRuczpcbiAgICBpbWFnZTogZmF2b25pYS9jbG91ZGZsYXJlLWRkbnM6MVxuICAgIG5ldHdvcmtfbW9kZTogaG9zdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdXNlcjogXCIxMDAwOjEwMDBcIlxuICAgIHJlYWRfb25seTogdHJ1ZVxuICAgIGNhcF9kcm9wOiBbYWxsXVxuICAgIHNlY3VyaXR5X29wdDogW25vLW5ldy1wcml2aWxlZ2VzOnRydWVdXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIENMT1VERkxBUkVfQVBJX1RPS0VOPSR7Q0xPVURGTEFSRV9BUElfVE9LRU46P31cbiAgICAgIC0gRE9NQUlOUz0ke0RPTUFJTlM6P31cbiAgICAgIC0gUFJPWElFRD1mYWxzZVxuICAgICAgLSBJUDZfUFJPVklERVI9bm9uZVxuIiwKICAiY29uZmlnIjogInZhcmlhYmxlcyA9IHt9XG5cbltjb25maWddXG5kb21haW5zID0gW11cbm1vdW50cyA9IFtdXG5cbltjb25maWcuZW52XVxuQ0xPVURGTEFSRV9BUElfVE9LRU4gPSBcIjxJTlNFUlQgWU9VUiBUT0tFTj5cIlxuRE9NQUlOUyA9IFwiZXhhbXBsZS5vcmcsd3d3LmV4YW1wbGUub3JnLGV4YW1wbGUuaW9cIlxuIgp9
```

## Links

`cloud`,`networking`,`ddns`

---

Version:`1.15.1`

Cloud CommanderCloud Commander is a file manager for the web. It includes a command-line console and a text editor. Cloud Commander helps you manage your server and work with files, directories and programs in a web browser.

CloudflaredA lightweight daemon that securely connects local services to the internet through Cloudflare Tunnel.

### On this page

ConfigurationBase64LinksTags