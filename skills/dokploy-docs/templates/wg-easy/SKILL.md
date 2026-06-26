---
title: "WG-Easy | Dokploy"
source: "https://docs.dokploy.com/docs/templates/wg-easy"
category: dokploy-docs
created: "2026-06-25T17:22:01.420Z"
---

WG-Easy | Dokploy

# WG-Easy

Copy as Markdown

WG-Easy is a simple and user-friendly WireGuard VPN server with a web interface for easy management.

## Configuration

docker-compose.ymltemplate.toml

```
volumes:
  etc_wireguard:

services:
  wg-easy:
    environment:
      - INIT_ENABLED=1
      - INIT_HOST=${WIREGUARD_HOST}
      - INIT_PORT=51820
      - INIT_USERNAME=admin
      - INIT_PASSWORD=${WIREGUARD_PASSWORD}
      - INIT_DNS=1.1.1.1,8.8.8.8
      - PORT=51821
    image: ghcr.io/wg-easy/wg-easy:15
    container_name: wg-easy
    volumes:
      - etc_wireguard:/etc/wireguard
      - /lib/modules:/lib/modules:ro
    ports:
      - "51820:51820/udp"
      - "51821:51821/tcp"
    restart: unless-stopped
    cap_add:
      - NET_ADMIN
      - SYS_MODULE
      - NET_RAW
    sysctls:
      - net.ipv4.ip_forward=1
      - net.ipv4.conf.all.src_valid_mark=1
      - net.ipv6.conf.all.disable_ipv6=0
      - net.ipv6.conf.all.forwarding=1
      - net.ipv6.conf.default.forwarding=1
```

```
[variables]
main_domain = "${domain}"
wg_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "wg-easy"
port = 51821
host = "${main_domain}"

[config.env]
WIREGUARD_HOST = "${main_domain}"
WIREGUARD_PASSWORD = "${wg_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZvbHVtZXM6XG4gIGV0Y193aXJlZ3VhcmQ6XG5cbnNlcnZpY2VzOlxuICB3Zy1lYXN5OlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBJTklUX0VOQUJMRUQ9MVxuICAgICAgLSBJTklUX0hPU1Q9JHtXSVJFR1VBUkRfSE9TVH1cbiAgICAgIC0gSU5JVF9QT1JUPTUxODIwXG4gICAgICAtIElOSVRfVVNFUk5BTUU9YWRtaW5cbiAgICAgIC0gSU5JVF9QQVNTV09SRD0ke1dJUkVHVUFSRF9QQVNTV09SRH1cbiAgICAgIC0gSU5JVF9ETlM9MS4xLjEuMSw4LjguOC44XG4gICAgICAtIFBPUlQ9NTE4MjFcbiAgICBpbWFnZTogZ2hjci5pby93Zy1lYXN5L3dnLWVhc3k6MTVcbiAgICBjb250YWluZXJfbmFtZTogd2ctZWFzeVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGV0Y193aXJlZ3VhcmQ6L2V0Yy93aXJlZ3VhcmRcbiAgICAgIC0gL2xpYi9tb2R1bGVzOi9saWIvbW9kdWxlczpyb1xuICAgIHBvcnRzOlxuICAgICAgLSBcIjUxODIwOjUxODIwL3VkcFwiXG4gICAgICAtIFwiNTE4MjE6NTE4MjEvdGNwXCJcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGNhcF9hZGQ6XG4gICAgICAtIE5FVF9BRE1JTlxuICAgICAgLSBTWVNfTU9EVUxFXG4gICAgICAtIE5FVF9SQVdcbiAgICBzeXNjdGxzOlxuICAgICAgLSBuZXQuaXB2NC5pcF9mb3J3YXJkPTFcbiAgICAgIC0gbmV0LmlwdjQuY29uZi5hbGwuc3JjX3ZhbGlkX21hcms9MVxuICAgICAgLSBuZXQuaXB2Ni5jb25mLmFsbC5kaXNhYmxlX2lwdjY9MFxuICAgICAgLSBuZXQuaXB2Ni5jb25mLmFsbC5mb3J3YXJkaW5nPTFcbiAgICAgIC0gbmV0LmlwdjYuY29uZi5kZWZhdWx0LmZvcndhcmRpbmc9MVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbndnX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ3Zy1lYXN5XCJcbnBvcnQgPSA1MTgyMVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbldJUkVHVUFSRF9IT1NUID0gXCIke21haW5fZG9tYWlufVwiXG5XSVJFR1VBUkRfUEFTU1dPUkQgPSBcIiR7d2dfcGFzc3dvcmR9XCJcbiIKfQ==
```

## Links

`vpn`,`wireguard`,`networking`

---

Version:`15`

Web-CheckWeb-Check is a powerful all-in-one website analyzer that provides detailed insights into any website's security, performance, and functionality.

Wiki.jsThe most powerful and extensible open source Wiki software.

### On this page

ConfigurationBase64LinksTags