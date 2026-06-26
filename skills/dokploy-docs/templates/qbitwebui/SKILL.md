---
title: "qBittorrent Web UI | Dokploy"
source: "https://docs.dokploy.com/docs/templates/qbitwebui"
category: dokploy-docs
created: "2026-06-25T17:21:57.937Z"
---

qBittorrent Web UI | Dokploy

# qBittorrent Web UI

Copy as Markdown

A modern web interface for managing multiple qBittorrent instances. Built with React, Hono, and Bun.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  qbitwebui:
    image: ghcr.io/maciejonos/qbitwebui:latest
    restart: unless-stopped
    environment:
      # Required: Encryption key for storing credentials (min 32 chars)
      - ENCRYPTION_KEY=${ENCRYPTION_KEY}
      # Optional: Server port (default: 3000)
      - PORT=${PORT:-3000}
      # Optional: Database location (default: ./data/qbitwebui.db)
      - DATABASE_PATH=${DATABASE_PATH:-/data/qbitwebui.db}
      # Optional: Salt file location (default: ./data/.salt)
      - SALT_PATH=${SALT_PATH:-/data/.salt}
      # Optional: Allow self-signed certificates for qBittorrent instances (default: false)
      # - ALLOW_SELF_SIGNED_CERTS=${ALLOW_SELF_SIGNED_CERTS:-false}
      # Optional: Disable authentication/login (single-user mode) (default: false)
      # - DISABLE_AUTH=${DISABLE_AUTH:-false}
      # Optional: Disable new registrations, creates default admin account (default: false)
      # - DISABLE_REGISTRATION=${DISABLE_REGISTRATION:-false}
      # Optional: Enable file browser by setting downloads path
      # - DOWNLOADS_PATH=/downloads
    volumes:
      - qbitwebui_data:/data
      # Optional: Mount downloads directory for file browser feature
      # Read-only mount (browse & download only):
      # - /path/to/your/downloads:/downloads:ro
      # Or read-write mount (enables delete/move/copy/rename):
      # - /path/to/your/downloads:/downloads
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:3000"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 10s

volumes:
  qbitwebui_data:
```

```
[variables]
main_domain = "${domain}"
encryption_key = "${password:32}"

[config]
[[config.domains]]
serviceName = "qbitwebui"
port = 3000
host = "${main_domain}"
path = "/"

[config.env]
ENCRYPTION_KEY = "${encryption_key}"
PORT = "3000"
DATABASE_PATH = "/data/qbitwebui.db"
SALT_PATH = "/data/.salt"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHFiaXR3ZWJ1aTpcbiAgICBpbWFnZTogZ2hjci5pby9tYWNpZWpvbm9zL3FiaXR3ZWJ1aTpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgIyBSZXF1aXJlZDogRW5jcnlwdGlvbiBrZXkgZm9yIHN0b3JpbmcgY3JlZGVudGlhbHMgKG1pbiAzMiBjaGFycylcbiAgICAgIC0gRU5DUllQVElPTl9LRVk9JHtFTkNSWVBUSU9OX0tFWX1cbiAgICAgICMgT3B0aW9uYWw6IFNlcnZlciBwb3J0IChkZWZhdWx0OiAzMDAwKVxuICAgICAgLSBQT1JUPSR7UE9SVDotMzAwMH1cbiAgICAgICMgT3B0aW9uYWw6IERhdGFiYXNlIGxvY2F0aW9uIChkZWZhdWx0OiAuL2RhdGEvcWJpdHdlYnVpLmRiKVxuICAgICAgLSBEQVRBQkFTRV9QQVRIPSR7REFUQUJBU0VfUEFUSDotL2RhdGEvcWJpdHdlYnVpLmRifVxuICAgICAgIyBPcHRpb25hbDogU2FsdCBmaWxlIGxvY2F0aW9uIChkZWZhdWx0OiAuL2RhdGEvLnNhbHQpXG4gICAgICAtIFNBTFRfUEFUSD0ke1NBTFRfUEFUSDotL2RhdGEvLnNhbHR9XG4gICAgICAjIE9wdGlvbmFsOiBBbGxvdyBzZWxmLXNpZ25lZCBjZXJ0aWZpY2F0ZXMgZm9yIHFCaXR0b3JyZW50IGluc3RhbmNlcyAoZGVmYXVsdDogZmFsc2UpXG4gICAgICAjIC0gQUxMT1dfU0VMRl9TSUdORURfQ0VSVFM9JHtBTExPV19TRUxGX1NJR05FRF9DRVJUUzotZmFsc2V9XG4gICAgICAjIE9wdGlvbmFsOiBEaXNhYmxlIGF1dGhlbnRpY2F0aW9uL2xvZ2luIChzaW5nbGUtdXNlciBtb2RlKSAoZGVmYXVsdDogZmFsc2UpXG4gICAgICAjIC0gRElTQUJMRV9BVVRIPSR7RElTQUJMRV9BVVRIOi1mYWxzZX1cbiAgICAgICMgT3B0aW9uYWw6IERpc2FibGUgbmV3IHJlZ2lzdHJhdGlvbnMsIGNyZWF0ZXMgZGVmYXVsdCBhZG1pbiBhY2NvdW50IChkZWZhdWx0OiBmYWxzZSlcbiAgICAgICMgLSBESVNBQkxFX1JFR0lTVFJBVElPTj0ke0RJU0FCTEVfUkVHSVNUUkFUSU9OOi1mYWxzZX1cbiAgICAgICMgT3B0aW9uYWw6IEVuYWJsZSBmaWxlIGJyb3dzZXIgYnkgc2V0dGluZyBkb3dubG9hZHMgcGF0aFxuICAgICAgIyAtIERPV05MT0FEU19QQVRIPS9kb3dubG9hZHNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBxYml0d2VidWlfZGF0YTovZGF0YVxuICAgICAgIyBPcHRpb25hbDogTW91bnQgZG93bmxvYWRzIGRpcmVjdG9yeSBmb3IgZmlsZSBicm93c2VyIGZlYXR1cmVcbiAgICAgICMgUmVhZC1vbmx5IG1vdW50IChicm93c2UgJiBkb3dubG9hZCBvbmx5KTpcbiAgICAgICMgLSAvcGF0aC90by95b3VyL2Rvd25sb2FkczovZG93bmxvYWRzOnJvXG4gICAgICAjIE9yIHJlYWQtd3JpdGUgbW91bnQgKGVuYWJsZXMgZGVsZXRlL21vdmUvY29weS9yZW5hbWUpOlxuICAgICAgIyAtIC9wYXRoL3RvL3lvdXIvZG93bmxvYWRzOi9kb3dubG9hZHNcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcIndnZXRcIiwgXCItLW5vLXZlcmJvc2VcIiwgXCItLXRyaWVzPTFcIiwgXCItLXNwaWRlclwiLCBcImh0dHA6Ly9sb2NhbGhvc3Q6MzAwMFwiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDNcbiAgICAgIHN0YXJ0X3BlcmlvZDogMTBzXG5cbnZvbHVtZXM6XG4gIHFiaXR3ZWJ1aV9kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmVuY3J5cHRpb25fa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJxYml0d2VidWlcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbnBhdGggPSBcIi9cIlxuXG5bY29uZmlnLmVudl1cbkVOQ1JZUFRJT05fS0VZID0gXCIke2VuY3J5cHRpb25fa2V5fVwiXG5QT1JUID0gXCIzMDAwXCJcbkRBVEFCQVNFX1BBVEggPSBcIi9kYXRhL3FiaXR3ZWJ1aS5kYlwiXG5TQUxUX1BBVEggPSBcIi9kYXRhLy5zYWx0XCJcbiIKfQ==
```

## Links

`torrent`,`download`,`media`,`qbittorrent`

---

Version:`latest`

qBittorrentA free and open-source BitTorrent client with web interface for remote management. Default login: admin (check container logs for temporary password on first startup).

QdrantAn open-source vector database designed for high-performance similarity search and storage of embeddings.

### On this page

ConfigurationBase64LinksTags