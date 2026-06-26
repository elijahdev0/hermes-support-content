---
title: "RustFS | Dokploy"
source: "https://docs.dokploy.com/docs/templates/rustfs"
category: dokploy-docs
created: "2026-06-25T17:21:57.938Z"
---

RustFS | Dokploy

# RustFS

Copy as Markdown

RustFS is a high-performance, S3-compatible distributed object storage system built in Rust. 2.3x faster than MinIO for small objects, with full S3 API compatibility.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  rustfs:
    image: rustfs/rustfs:latest
    volumes:
      - rustfs-data:/data
    environment:
      - RUSTFS_ACCESS_KEY
      - RUSTFS_SECRET_KEY
      - RUSTFS_ADDRESS=0.0.0.0:9000
      - RUSTFS_CONSOLE_ADDRESS=0.0.0.0:9001
      - RUSTFS_CONSOLE_ENABLE=true
      - RUSTFS_CORS_ALLOWED_ORIGINS=*
      - RUSTFS_CONSOLE_CORS_ALLOWED_ORIGINS=*
    command: /data
    restart: unless-stopped

volumes:
  rustfs-data:
```

```
[variables]
console_domain = "${domain}"
api_domain = "${domain}"
access_key = "rustfsadmin"
secret_key = "${password:16}"

[config]
env = [
  "RUSTFS_ACCESS_KEY=${access_key}",
  "RUSTFS_SECRET_KEY=${secret_key}",
  "",
  "## SET THE API URL IN CONSOLE CONFIG BY CLICKING THE COG",
  "## API URL: ${api_domain}",
]
mounts = []

[[config.domains]]
serviceName = "rustfs"
port = 9001
host = "${console_domain}"

[[config.domains]]
serviceName = "rustfs"
port = 9000
host = "${api_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHJ1c3RmczpcbiAgICBpbWFnZTogcnVzdGZzL3J1c3RmczpsYXRlc3RcbiAgICB2b2x1bWVzOlxuICAgICAgLSBydXN0ZnMtZGF0YTovZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBSVVNURlNfQUNDRVNTX0tFWVxuICAgICAgLSBSVVNURlNfU0VDUkVUX0tFWVxuICAgICAgLSBSVVNURlNfQUREUkVTUz0wLjAuMC4wOjkwMDBcbiAgICAgIC0gUlVTVEZTX0NPTlNPTEVfQUREUkVTUz0wLjAuMC4wOjkwMDFcbiAgICAgIC0gUlVTVEZTX0NPTlNPTEVfRU5BQkxFPXRydWVcbiAgICAgIC0gUlVTVEZTX0NPUlNfQUxMT1dFRF9PUklHSU5TPSpcbiAgICAgIC0gUlVTVEZTX0NPTlNPTEVfQ09SU19BTExPV0VEX09SSUdJTlM9KlxuICAgIGNvbW1hbmQ6IC9kYXRhXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxudm9sdW1lczpcbiAgcnVzdGZzLWRhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbmNvbnNvbGVfZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYXBpX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmFjY2Vzc19rZXkgPSBcInJ1c3Rmc2FkbWluXCJcbnNlY3JldF9rZXkgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJSVVNURlNfQUNDRVNTX0tFWT0ke2FjY2Vzc19rZXl9XCIsXG4gIFwiUlVTVEZTX1NFQ1JFVF9LRVk9JHtzZWNyZXRfa2V5fVwiLFxuICBcIlwiLFxuICBcIiMjIFNFVCBUSEUgQVBJIFVSTCBJTiBDT05TT0xFIENPTkZJRyBCWSBDTElDS0lORyBUSEUgQ09HXCIsXG4gIFwiIyMgQVBJIFVSTDogJHthcGlfZG9tYWlufVwiLFxuXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicnVzdGZzXCJcbnBvcnQgPSA5MDAxXG5ob3N0ID0gXCIke2NvbnNvbGVfZG9tYWlufVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInJ1c3Rmc1wiXG5wb3J0ID0gOTAwMFxuaG9zdCA9IFwiJHthcGlfZG9tYWlufVwiXG4iCn0=
```

## Links

`storage`,`s3`,`object-storage`,`rust`

---

Version:`latest`

RustDeskRustDesk is a full-featured open source remote control alternative for self-hosting and security with minimal configuration.

ruTorrentruTorrent + rTorrent BitTorrent client (crazy-max image). Web UI on 8080, XMLRPC on 8000, with P2P ports exposed for seeding.

### On this page

ConfigurationBase64LinksTags