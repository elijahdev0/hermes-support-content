---
title: "RustDesk | Dokploy"
source: "https://docs.dokploy.com/docs/templates/rustdesk"
category: dokploy-docs
created: "2026-06-25T17:21:57.938Z"
---

RustDesk | Dokploy

# RustDesk

Copy as Markdown

RustDesk is a full-featured open source remote control alternative for self-hosting and security with minimal configuration.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  hbbs:
    image: rustdesk/rustdesk-server:latest
    command: hbbs
    restart: unless-stopped
    volumes:
      - rustdesk-data:/root
    ports:
      - "21115:21115"
      - "21116:21116"
      - "21116:21116/udp"
    depends_on:
      - hbbr

  hbbr:
    image: rustdesk/rustdesk-server:latest
    command: hbbr
    restart: unless-stopped
    volumes:
      - rustdesk-data:/root
    ports:
      - "21117:21117"
      - "21118:21118"
      - "21119:21119"

volumes:
  rustdesk-data:
```

```
[variables]
server_domain = "${domain}"
encryption_key = "${password:32}"

[config]

[config.env]
RELAY_HOST = "${server_domain}"
RUSTDESK_RELAY_SERVER = "${server_domain}:21117"
RUSTDESK_API_SERVER = "http://${server_domain}:21118"
RUSTDESK_ID_SERVER = "${server_domain}:21116"
ENCRYPTION_KEY = "${encryption_key}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBoYmJzOlxuICAgIGltYWdlOiBydXN0ZGVzay9ydXN0ZGVzay1zZXJ2ZXI6bGF0ZXN0XG4gICAgY29tbWFuZDogaGJic1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcnVzdGRlc2stZGF0YTovcm9vdFxuICAgIHBvcnRzOlxuICAgICAgLSBcIjIxMTE1OjIxMTE1XCJcbiAgICAgIC0gXCIyMTExNjoyMTExNlwiXG4gICAgICAtIFwiMjExMTY6MjExMTYvdWRwXCJcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBoYmJyXG5cbiAgaGJicjpcbiAgICBpbWFnZTogcnVzdGRlc2svcnVzdGRlc2stc2VydmVyOmxhdGVzdFxuICAgIGNvbW1hbmQ6IGhiYnJcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHJ1c3RkZXNrLWRhdGE6L3Jvb3RcbiAgICBwb3J0czpcbiAgICAgIC0gXCIyMTExNzoyMTExN1wiXG4gICAgICAtIFwiMjExMTg6MjExMThcIlxuICAgICAgLSBcIjIxMTE5OjIxMTE5XCJcblxudm9sdW1lczpcbiAgcnVzdGRlc2stZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxuc2VydmVyX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmVuY3J5cHRpb25fa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5cbltjb25maWcuZW52XVxuUkVMQVlfSE9TVCA9IFwiJHtzZXJ2ZXJfZG9tYWlufVwiXG5SVVNUREVTS19SRUxBWV9TRVJWRVIgPSBcIiR7c2VydmVyX2RvbWFpbn06MjExMTdcIlxuUlVTVERFU0tfQVBJX1NFUlZFUiA9IFwiaHR0cDovLyR7c2VydmVyX2RvbWFpbn06MjExMThcIlxuUlVTVERFU0tfSURfU0VSVkVSID0gXCIke3NlcnZlcl9kb21haW59OjIxMTE2XCJcbkVOQ1JZUFRJT05fS0VZID0gXCIke2VuY3J5cHRpb25fa2V5fVwiXG5cbltbY29uZmlnLm1vdW50c11dIgp9
```

## Links

`remote-desktop`,`self-hosted`,`productivity`

---

Version:`latest`

RSSHubRSSHub is the world's largest RSS network, consisting of over 5,000 global instances.RSSHub delivers millions of contents aggregated from all kinds of sources, our vibrant open source community is ensuring the deliver of RSSHub's new routes, new features and bug fixes.

RustFSRustFS is a high-performance, S3-compatible distributed object storage system built in Rust. 2.3x faster than MinIO for small objects, with full S3 API compatibility.

### On this page

ConfigurationBase64LinksTags