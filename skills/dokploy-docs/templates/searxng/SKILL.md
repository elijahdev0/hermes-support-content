---
title: "SearXNG | Dokploy"
source: "https://docs.dokploy.com/docs/templates/searxng"
category: dokploy-docs
created: "2026-06-25T17:21:59.113Z"
---

SearXNG | Dokploy

# SearXNG

Copy as Markdown

SearXNG is a privacy-respecting, hackable metasearch engine that aggregates results from various search engines without tracking users.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  valkey:
    image: valkey/valkey:8-alpine
    command: valkey-server --save 30 1 --loglevel warning
    restart: unless-stopped
    volumes:
      - valkey-data:/data

  searxng:
    image: searxng/searxng:latest
    restart: unless-stopped
    volumes:
      - ../files/searxng:/etc/searxng
      - searxng-data:/var/cache/searxng

volumes:
  valkey-data: {}
  searxng-data: {}
```

```
[variables]
main_domain = "${domain}"
secret_key = "${password:64}"

[config]
[[config.domains]]
serviceName = "searxng"
port = 8080
host = "${main_domain}"
env = [
  "SEARXNG_BASE_URL=https://${main_domain}/"
]

[[config.mounts]]
filePath = "/searxng/settings.yml"
content = """
use_default_settings: true

server:
  secret_key: \"${secret_key}\"
  limiter: false
  image_proxy: false

valkey:
  url: valkey://valkey:6379/0
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB2YWxrZXk6XG4gICAgaW1hZ2U6IHZhbGtleS92YWxrZXk6OC1hbHBpbmVcbiAgICBjb21tYW5kOiB2YWxrZXktc2VydmVyIC0tc2F2ZSAzMCAxIC0tbG9nbGV2ZWwgd2FybmluZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gdmFsa2V5LWRhdGE6L2RhdGFcblxuICBzZWFyeG5nOlxuICAgIGltYWdlOiBzZWFyeG5nL3NlYXJ4bmc6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9zZWFyeG5nOi9ldGMvc2VhcnhuZ1xuICAgICAgLSBzZWFyeG5nLWRhdGE6L3Zhci9jYWNoZS9zZWFyeG5nXG5cbnZvbHVtZXM6XG4gIHZhbGtleS1kYXRhOiB7fVxuICBzZWFyeG5nLWRhdGE6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuc2VjcmV0X2tleSA9IFwiJHtwYXNzd29yZDo2NH1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwic2VhcnhuZ1wiXG5wb3J0ID0gODA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuZW52ID0gW1xuICBcIlNFQVJYTkdfQkFTRV9VUkw9aHR0cHM6Ly8ke21haW5fZG9tYWlufS9cIlxuXVxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi9zZWFyeG5nL3NldHRpbmdzLnltbFwiXG5jb250ZW50ID0gXCJcIlwiXG51c2VfZGVmYXVsdF9zZXR0aW5nczogdHJ1ZVxuXG5zZXJ2ZXI6XG4gIHNlY3JldF9rZXk6IFxcXCIke3NlY3JldF9rZXl9XFxcIlxuICBsaW1pdGVyOiBmYWxzZVxuICBpbWFnZV9wcm94eTogZmFsc2VcblxudmFsa2V5OlxuICB1cmw6IHZhbGtleTovL3ZhbGtleTo2Mzc5LzBcblwiXCJcIiIKfQ==
```

## Links

`search-engine`,`metasearch`,`privacy`,`self-hosted`,`aggregator`

---

Version:`latest`

SeafileOpen source cloud storage system for file sync, share and document collaboration

SeaweedFSSeaweedFS is a fast distributed storage system for blobs, objects, and files. Features S3-compatible API, POSIX FUSE mount, and WebDAV support.

### On this page

ConfigurationBase64LinksTags