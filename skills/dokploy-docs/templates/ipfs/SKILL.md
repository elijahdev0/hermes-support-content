---
title: "IPFS (Kubo) | Dokploy"
source: "https://docs.dokploy.com/docs/templates/ipfs"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

IPFS (Kubo) | Dokploy

# IPFS (Kubo)

Copy as Markdown

IPFS (Kubo) is a decentralized peer-to-peer file sharing and storage network node. Host your own IPFS gateway and API.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  ipfs:
    image: ipfs/kubo:latest
    restart: unless-stopped
    environment:
      - IPFS_PROFILE=server
    volumes:
      - ipfs_data:/data/ipfs
      - ipfs_staging:/export
    ports:
      - 4001
      - 8080
      - 5001
volumes:
  ipfs_data: {}
  ipfs_staging: {}
```

```
[variables]
gateway_domain = "${domain}"
api_domain = "${domain}"

[config]
env = []

[[config.domains]]
serviceName = "ipfs"
port = 8080
host = "${gateway_domain}"

[[config.domains]]
serviceName = "ipfs"
port = 5001
host = "${api_domain}"

[[config.mounts]]
filePath = "/container-init.d/001-configure-api.sh"
content = """
#!/bin/sh
ipfs config Addresses.API /ip4/0.0.0.0/tcp/5001
ipfs config --json API.HTTPHeaders.Access-Control-Allow-Origin '["*"]'
ipfs config --json API.HTTPHeaders.Access-Control-Allow-Methods '["PUT", "POST", "GET"]'
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBpcGZzOlxuICAgIGltYWdlOiBpcGZzL2t1Ym86bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gSVBGU19QUk9GSUxFPXNlcnZlclxuICAgIHZvbHVtZXM6XG4gICAgICAtIGlwZnNfZGF0YTovZGF0YS9pcGZzXG4gICAgICAtIGlwZnNfc3RhZ2luZzovZXhwb3J0XG4gICAgcG9ydHM6XG4gICAgICAtIDQwMDFcbiAgICAgIC0gODA4MFxuICAgICAgLSA1MDAxXG52b2x1bWVzOlxuICBpcGZzX2RhdGE6IHt9XG4gIGlwZnNfc3RhZ2luZzoge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxuZ2F0ZXdheV9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5hcGlfZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiaXBmc1wiXG5wb3J0ID0gODA4MFxuaG9zdCA9IFwiJHtnYXRld2F5X2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJpcGZzXCJcbnBvcnQgPSA1MDAxXG5ob3N0ID0gXCIke2FwaV9kb21haW59XCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvY29udGFpbmVyLWluaXQuZC8wMDEtY29uZmlndXJlLWFwaS5zaFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIS9iaW4vc2hcbmlwZnMgY29uZmlnIEFkZHJlc3Nlcy5BUEkgL2lwNC8wLjAuMC4wL3RjcC81MDAxXG5pcGZzIGNvbmZpZyAtLWpzb24gQVBJLkhUVFBIZWFkZXJzLkFjY2Vzcy1Db250cm9sLUFsbG93LU9yaWdpbiAnW1wiKlwiXSdcbmlwZnMgY29uZmlnIC0tanNvbiBBUEkuSFRUUEhlYWRlcnMuQWNjZXNzLUNvbnRyb2wtQWxsb3ctTWV0aG9kcyAnW1wiUFVUXCIsIFwiUE9TVFwiLCBcIkdFVFwiXSdcblwiXCJcIlxuIgp9
```

## Links

`storage`,`decentralized`,`p2p`,`self-hosted`

---

Version:`latest`

InvoiceShelfInvoiceShelf is a self-hosted open source invoicing system for freelancers and small businesses.

IT ToolsA collection of handy online it-tools for developers.

### On this page

ConfigurationBase64LinksTags