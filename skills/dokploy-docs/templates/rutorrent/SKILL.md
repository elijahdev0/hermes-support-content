---
title: "ruTorrent | Dokploy"
source: "https://docs.dokploy.com/docs/templates/rutorrent"
category: dokploy-docs
created: "2026-06-25T17:21:57.938Z"
---

ruTorrent | Dokploy

# ruTorrent

Copy as Markdown

ruTorrent + rTorrent BitTorrent client (crazy-max image). Web UI on 8080, XMLRPC on 8000, with P2P ports exposed for seeding.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  rutorrent:
    image: crazymax/rtorrent-rutorrent:latest
    restart: unless-stopped
    environment:
      - PUID=${PUID:-1000}
      - PGID=${PGID:-1000}
      # Optional: keep defaults, Dokploy will route 8080 via domain
      - RUTORRENT_PORT=8080
      - XMLRPC_PORT=8000
      # You can customize these if you like:
      - RT_DHT_PORT=${DHT_PORT:-6881}
      - RT_INC_PORT=${INCOMING_PORT:-50000}
    volumes:
      - rutorrent-data:/data
      - rutorrent-downloads:/downloads
      - rutorrent-passwd:/passwd
    # Expose only P2P-related ports; Dokploy domain will handle the web UI.
    ports:
      - "${INCOMING_PORT:-50000}:50000/tcp"
      - "${DHT_PORT:-6881}:6881/udp"

volumes:
  rutorrent-data: {}
  rutorrent-downloads: {}
  rutorrent-passwd: {}
```

```
[variables]
main_domain   = "${domain}"
puid          = "${PUID:-1000}"
pgid          = "${PGID:-1000}"
incoming_port = "${INCOMING_PORT:-50000}"
dht_port      = "${DHT_PORT:-6881}"

[config]
# Dokploy will route this domain to the container's internal port 8080
[[config.domains]]
serviceName = "rutorrent"
port        = 8080
host        = "${main_domain}"

[config.env]
PUID = "${puid}"
PGID = "${pgid}"
INCOMING_PORT = "${incoming_port}"
DHT_PORT      = "${dht_port}"

[[config.mounts]]
type   = "volume"
source = "rutorrent-data"
target = "/data"

[[config.mounts]]
type   = "volume"
source = "rutorrent-downloads"
target = "/downloads"

[[config.mounts]]
type   = "volume"
source = "rutorrent-passwd"
target = "/passwd"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHJ1dG9ycmVudDpcbiAgICBpbWFnZTogY3JhenltYXgvcnRvcnJlbnQtcnV0b3JyZW50OmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBVSUQ9JHtQVUlEOi0xMDAwfVxuICAgICAgLSBQR0lEPSR7UEdJRDotMTAwMH1cbiAgICAgICMgT3B0aW9uYWw6IGtlZXAgZGVmYXVsdHMsIERva3Bsb3kgd2lsbCByb3V0ZSA4MDgwIHZpYSBkb21haW5cbiAgICAgIC0gUlVUT1JSRU5UX1BPUlQ9ODA4MFxuICAgICAgLSBYTUxSUENfUE9SVD04MDAwXG4gICAgICAjIFlvdSBjYW4gY3VzdG9taXplIHRoZXNlIGlmIHlvdSBsaWtlOlxuICAgICAgLSBSVF9ESFRfUE9SVD0ke0RIVF9QT1JUOi02ODgxfVxuICAgICAgLSBSVF9JTkNfUE9SVD0ke0lOQ09NSU5HX1BPUlQ6LTUwMDAwfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHJ1dG9ycmVudC1kYXRhOi9kYXRhXG4gICAgICAtIHJ1dG9ycmVudC1kb3dubG9hZHM6L2Rvd25sb2Fkc1xuICAgICAgLSBydXRvcnJlbnQtcGFzc3dkOi9wYXNzd2RcbiAgICAjIEV4cG9zZSBvbmx5IFAyUC1yZWxhdGVkIHBvcnRzOyBEb2twbG95IGRvbWFpbiB3aWxsIGhhbmRsZSB0aGUgd2ViIFVJLlxuICAgIHBvcnRzOlxuICAgICAgLSBcIiR7SU5DT01JTkdfUE9SVDotNTAwMDB9OjUwMDAwL3RjcFwiXG4gICAgICAtIFwiJHtESFRfUE9SVDotNjg4MX06Njg4MS91ZHBcIlxuXG52b2x1bWVzOlxuICBydXRvcnJlbnQtZGF0YToge31cbiAgcnV0b3JyZW50LWRvd25sb2Fkczoge31cbiAgcnV0b3JyZW50LXBhc3N3ZDoge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gICA9IFwiJHtkb21haW59XCJcbnB1aWQgICAgICAgICAgPSBcIiR7UFVJRDotMTAwMH1cIlxucGdpZCAgICAgICAgICA9IFwiJHtQR0lEOi0xMDAwfVwiXG5pbmNvbWluZ19wb3J0ID0gXCIke0lOQ09NSU5HX1BPUlQ6LTUwMDAwfVwiXG5kaHRfcG9ydCAgICAgID0gXCIke0RIVF9QT1JUOi02ODgxfVwiXG5cbltjb25maWddXG4jIERva3Bsb3kgd2lsbCByb3V0ZSB0aGlzIGRvbWFpbiB0byB0aGUgY29udGFpbmVyJ3MgaW50ZXJuYWwgcG9ydCA4MDgwXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJydXRvcnJlbnRcIlxucG9ydCAgICAgICAgPSA4MDgwXG5ob3N0ICAgICAgICA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblBVSUQgPSBcIiR7cHVpZH1cIlxuUEdJRCA9IFwiJHtwZ2lkfVwiXG5JTkNPTUlOR19QT1JUID0gXCIke2luY29taW5nX3BvcnR9XCJcbkRIVF9QT1JUICAgICAgPSBcIiR7ZGh0X3BvcnR9XCJcblxuW1tjb25maWcubW91bnRzXV1cbnR5cGUgICA9IFwidm9sdW1lXCJcbnNvdXJjZSA9IFwicnV0b3JyZW50LWRhdGFcIlxudGFyZ2V0ID0gXCIvZGF0YVwiXG5cbltbY29uZmlnLm1vdW50c11dXG50eXBlICAgPSBcInZvbHVtZVwiXG5zb3VyY2UgPSBcInJ1dG9ycmVudC1kb3dubG9hZHNcIlxudGFyZ2V0ID0gXCIvZG93bmxvYWRzXCJcblxuW1tjb25maWcubW91bnRzXV1cbnR5cGUgICA9IFwidm9sdW1lXCJcbnNvdXJjZSA9IFwicnV0b3JyZW50LXBhc3N3ZFwiXG50YXJnZXQgPSBcIi9wYXNzd2RcIlxuIgp9
```

## Links

`torrent`,`rtorrent`,`webui`,`downloader`

---

Version:`latest`

RustFSRustFS is a high-performance, S3-compatible distributed object storage system built in Rust. 2.3x faster than MinIO for small objects, with full S3 API compatibility.

RybbitOpen-source and privacy-friendly alternative to Google Analytics that is 10x more intuitive

### On this page

ConfigurationBase64LinksTags