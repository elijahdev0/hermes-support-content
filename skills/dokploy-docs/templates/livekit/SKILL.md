---
title: "Livekit | Dokploy"
source: "https://docs.dokploy.com/docs/templates/livekit"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

Livekit | Dokploy

# Livekit

Copy as Markdown

LiveKit is an open source platform for developers building realtime media applications.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  livekit:
    image: livekit/livekit-server:v1.9.0
    restart: unless-stopped
    command: --config /etc/livekit.yaml
    volumes:
      - ../files/livekit.yaml:/etc/livekit.yaml
    ports:
      - "${LIVEKIT_PORT}:${LIVEKIT_PORT}"
      - "${TURN_UDP_PORT}:${TURN_UDP_PORT}/udp"
      - "${LIVEKIT_UDP_PORT}:${LIVEKIT_UDP_PORT}/udp"
    healthcheck:
      test: [ "CMD-SHELL", "wget -qO- http://localhost:${LIVEKIT_PORT} || exit 1" ]
      interval: 10s
      timeout: 5s
      retries: 6
    depends_on:
      redis:
        condition: service_healthy

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    command: redis-server /etc/redis.conf
    volumes:
      - ../files/redis.conf:/etc/redis.conf
    healthcheck:
      test: [ "CMD-SHELL", "redis-cli ping || exit 1" ]
      interval: 10s
      timeout: 5s
      retries: 6

  egress:
    image: livekit/egress:latest
    restart: unless-stopped
    environment:
      - EGRESS_CONFIG_FILE=/etc/egress.yaml
    volumes:
      - ../files/egress.yaml:/etc/egress.yaml
    cap_add:
      - CAP_SYS_ADMIN
    depends_on:
      livekit:
        condition: service_healthy

  ingress:
    image: livekit/ingress:latest
    restart: unless-stopped
    environment:
      - INGRESS_CONFIG_FILE=/etc/ingress.yaml
    volumes:
      - ../files/ingress.yaml:/etc/ingress.yaml
    ports:
      - "${RTMP_PORT}:${RTMP_PORT}"
      - "${INGRESS_UDP_PORT}:${INGRESS_UDP_PORT}/udp"
    depends_on:
      livekit:
        condition: service_healthy
```

```
[variables]
main_domain = "livekit.${domain}"
turn_domain = "livekit-turn.${domain}"
whip_domain = "livekit-whip.${domain}"
api_key = "API${password:12}"
api_secret = "${password:44}"
redis_address = "redis:6379"
redis_password = "${password:32}"

livekit_port = "7880"
livekit_tcp_port = "7881"
livekit_udp_port = "7882"
turn_tls_port = "5349"
turn_udp_port = "3478"
rtmp_port = "1935"
whip_port = "8080"
ingress_udp_port = "7885"
http_relay_port = "9090"

[config]
[[config.domains]]
serviceName = "livekit"
port = 7880
host = "${main_domain}"

[[config.domains]]
serviceName = "livekit"
port = 5349
host = "${turn_domain}"

[[config.domains]]
serviceName = "ingress"
port = 8080
host = "${whip_domain}"

[config.env]
LIVEKIT_URL = "${main_domain}"
RTMP_URL = "${turn_domain}"
WHIP_URL = "${whip_domain}"
REDIS_ADDRESS = "${redis_address}"
REDIS_PASSWORD = "${redis_password}"
API_KEY = "${api_key}"
API_SECRET = "${api_secret}"
LIVEKIT_PORT = "${livekit_port}"
LIVEKIT_TCP_PORT = "${livekit_tcp_port}"
LIVEKIT_UDP_PORT = "${livekit_udp_port}"
TURN_TLS_PORT = "${turn_tls_port}"
TURN_UDP_PORT = "${turn_udp_port}"
RTMP_PORT = "${rtmp_port}"
WHIP_PORT = "${whip_port}"
INGRESS_UDP_PORT = "${ingress_udp_port}"
HTTP_RELAY_PORT = "${http_relay_port}"

[[config.mounts]]
filePath = "redis.conf"
content = """
bind 0.0.0.0
protected-mode yes
port 6379
timeout 0
tcp-keepalive 300
requirepass ${redis_password}
"""

[[config.mounts]]
filePath = "livekit.yaml"
content = """
port: ${livekit_port}
bind_addresses:
    - ""
rtc:
    tcp_port: ${livekit_tcp_port}
    udp_port: ${livekit_udp_port}
    use_external_ip: true
    enable_loopback_candidate: false
redis:
    address: ${redis_address}
    username: ""
    password: ${redis_password}
    db: 0
    use_tls: false
    sentinel_master_name: ""
    sentinel_username: ""
    sentinel_password: ""
    sentinel_addresses: []
    cluster_addresses: []
    max_redirects: null
turn:
    enabled: true
    domain: ${turn_domain}
    tls_port: ${turn_tls_port}
    udp_port: ${turn_udp_port}
    external_tls: true
ingress:
    rtmp_base_url: rtmp://${main_domain}:${rtmp_port}/x
    whip_base_url: https://${whip_domain}/w
keys:
    ${api_key}: ${api_secret}
"""

[[config.mounts]]
filePath = "egress.yaml"
content = """
redis:
    address: ${redis_address}
    username: ""
    password: ${redis_password}
    db: 0
    use_tls: false
    sentinel_master_name: ""
    sentinel_username: ""
    sentinel_password: ""
    sentinel_addresses: []
    cluster_addresses: []
    max_redirects: null
api_key: ${api_key}
api_secret: ${api_secret}
ws_url: wss://${main_domain}
"""

[[config.mounts]]
filePath = "ingress.yaml"
content = """
redis:
    address: ${redis_address}
    username: ""
    password: ${redis_password}
    db: 0
    use_tls: false
    sentinel_master_name: ""
    sentinel_username: ""
    sentinel_password: ""
    sentinel_addresses: []
    cluster_addresses: []
    max_redirects: null
api_key: ${api_key}
api_secret: ${api_secret}
ws_url: wss://${main_domain}
rtmp_port: ${rtmp_port}
whip_port: ${whip_port}
http_relay_port: ${http_relay_port}
logging:
    json: false
    level: ""
development: false
rtc_config:
    udp_port: ${ingress_udp_port}
    use_external_ip: true
    enable_loopback_candidate: false
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBsaXZla2l0OlxuICAgIGltYWdlOiBsaXZla2l0L2xpdmVraXQtc2VydmVyOnYxLjkuMFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgY29tbWFuZDogLS1jb25maWcgL2V0Yy9saXZla2l0LnlhbWxcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9saXZla2l0LnlhbWw6L2V0Yy9saXZla2l0LnlhbWxcbiAgICBwb3J0czpcbiAgICAgIC0gXCIke0xJVkVLSVRfUE9SVH06JHtMSVZFS0lUX1BPUlR9XCJcbiAgICAgIC0gXCIke1RVUk5fVURQX1BPUlR9OiR7VFVSTl9VRFBfUE9SVH0vdWRwXCJcbiAgICAgIC0gXCIke0xJVkVLSVRfVURQX1BPUlR9OiR7TElWRUtJVF9VRFBfUE9SVH0vdWRwXCJcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFsgXCJDTUQtU0hFTExcIiwgXCJ3Z2V0IC1xTy0gaHR0cDovL2xvY2FsaG9zdDoke0xJVkVLSVRfUE9SVH0gfHwgZXhpdCAxXCIgXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDZcbiAgICBkZXBlbmRzX29uOlxuICAgICAgcmVkaXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG5cbiAgcmVkaXM6XG4gICAgaW1hZ2U6IHJlZGlzOjctYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBjb21tYW5kOiByZWRpcy1zZXJ2ZXIgL2V0Yy9yZWRpcy5jb25mXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvcmVkaXMuY29uZjovZXRjL3JlZGlzLmNvbmZcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFsgXCJDTUQtU0hFTExcIiwgXCJyZWRpcy1jbGkgcGluZyB8fCBleGl0IDFcIiBdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNlxuXG4gIGVncmVzczpcbiAgICBpbWFnZTogbGl2ZWtpdC9lZ3Jlc3M6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gRUdSRVNTX0NPTkZJR19GSUxFPS9ldGMvZWdyZXNzLnlhbWxcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9lZ3Jlc3MueWFtbDovZXRjL2VncmVzcy55YW1sXG4gICAgY2FwX2FkZDpcbiAgICAgIC0gQ0FQX1NZU19BRE1JTlxuICAgIGRlcGVuZHNfb246XG4gICAgICBsaXZla2l0OlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuXG4gIGluZ3Jlc3M6XG4gICAgaW1hZ2U6IGxpdmVraXQvaW5ncmVzczpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBJTkdSRVNTX0NPTkZJR19GSUxFPS9ldGMvaW5ncmVzcy55YW1sXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvaW5ncmVzcy55YW1sOi9ldGMvaW5ncmVzcy55YW1sXG4gICAgcG9ydHM6XG4gICAgICAtIFwiJHtSVE1QX1BPUlR9OiR7UlRNUF9QT1JUfVwiXG4gICAgICAtIFwiJHtJTkdSRVNTX1VEUF9QT1JUfToke0lOR1JFU1NfVURQX1BPUlR9L3VkcFwiXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGxpdmVraXQ6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCJsaXZla2l0LiR7ZG9tYWlufVwiXG50dXJuX2RvbWFpbiA9IFwibGl2ZWtpdC10dXJuLiR7ZG9tYWlufVwiXG53aGlwX2RvbWFpbiA9IFwibGl2ZWtpdC13aGlwLiR7ZG9tYWlufVwiXG5hcGlfa2V5ID0gXCJBUEkke3Bhc3N3b3JkOjEyfVwiXG5hcGlfc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjQ0fVwiXG5yZWRpc19hZGRyZXNzID0gXCJyZWRpczo2Mzc5XCJcbnJlZGlzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbmxpdmVraXRfcG9ydCA9IFwiNzg4MFwiXG5saXZla2l0X3RjcF9wb3J0ID0gXCI3ODgxXCJcbmxpdmVraXRfdWRwX3BvcnQgPSBcIjc4ODJcIlxudHVybl90bHNfcG9ydCA9IFwiNTM0OVwiXG50dXJuX3VkcF9wb3J0ID0gXCIzNDc4XCJcbnJ0bXBfcG9ydCA9IFwiMTkzNVwiXG53aGlwX3BvcnQgPSBcIjgwODBcIlxuaW5ncmVzc191ZHBfcG9ydCA9IFwiNzg4NVwiXG5odHRwX3JlbGF5X3BvcnQgPSBcIjkwOTBcIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibGl2ZWtpdFwiXG5wb3J0ID0gNzg4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJsaXZla2l0XCJcbnBvcnQgPSA1MzQ5XG5ob3N0ID0gXCIke3R1cm5fZG9tYWlufVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImluZ3Jlc3NcIlxucG9ydCA9IDgwODBcbmhvc3QgPSBcIiR7d2hpcF9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5MSVZFS0lUX1VSTCA9IFwiJHttYWluX2RvbWFpbn1cIlxuUlRNUF9VUkwgPSBcIiR7dHVybl9kb21haW59XCJcbldISVBfVVJMID0gXCIke3doaXBfZG9tYWlufVwiXG5SRURJU19BRERSRVNTID0gXCIke3JlZGlzX2FkZHJlc3N9XCJcblJFRElTX1BBU1NXT1JEID0gXCIke3JlZGlzX3Bhc3N3b3JkfVwiXG5BUElfS0VZID0gXCIke2FwaV9rZXl9XCJcbkFQSV9TRUNSRVQgPSBcIiR7YXBpX3NlY3JldH1cIlxuTElWRUtJVF9QT1JUID0gXCIke2xpdmVraXRfcG9ydH1cIlxuTElWRUtJVF9UQ1BfUE9SVCA9IFwiJHtsaXZla2l0X3RjcF9wb3J0fVwiXG5MSVZFS0lUX1VEUF9QT1JUID0gXCIke2xpdmVraXRfdWRwX3BvcnR9XCJcblRVUk5fVExTX1BPUlQgPSBcIiR7dHVybl90bHNfcG9ydH1cIlxuVFVSTl9VRFBfUE9SVCA9IFwiJHt0dXJuX3VkcF9wb3J0fVwiXG5SVE1QX1BPUlQgPSBcIiR7cnRtcF9wb3J0fVwiXG5XSElQX1BPUlQgPSBcIiR7d2hpcF9wb3J0fVwiXG5JTkdSRVNTX1VEUF9QT1JUID0gXCIke2luZ3Jlc3NfdWRwX3BvcnR9XCJcbkhUVFBfUkVMQVlfUE9SVCA9IFwiJHtodHRwX3JlbGF5X3BvcnR9XCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCJyZWRpcy5jb25mXCJcbmNvbnRlbnQgPSBcIlwiXCJcbmJpbmQgMC4wLjAuMFxucHJvdGVjdGVkLW1vZGUgeWVzXG5wb3J0IDYzNzlcbnRpbWVvdXQgMFxudGNwLWtlZXBhbGl2ZSAzMDBcbnJlcXVpcmVwYXNzICR7cmVkaXNfcGFzc3dvcmR9XG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCJsaXZla2l0LnlhbWxcIlxuY29udGVudCA9IFwiXCJcIlxucG9ydDogJHtsaXZla2l0X3BvcnR9XG5iaW5kX2FkZHJlc3NlczpcbiAgICAtIFwiXCJcbnJ0YzpcbiAgICB0Y3BfcG9ydDogJHtsaXZla2l0X3RjcF9wb3J0fVxuICAgIHVkcF9wb3J0OiAke2xpdmVraXRfdWRwX3BvcnR9XG4gICAgdXNlX2V4dGVybmFsX2lwOiB0cnVlXG4gICAgZW5hYmxlX2xvb3BiYWNrX2NhbmRpZGF0ZTogZmFsc2VcbnJlZGlzOlxuICAgIGFkZHJlc3M6ICR7cmVkaXNfYWRkcmVzc31cbiAgICB1c2VybmFtZTogXCJcIlxuICAgIHBhc3N3b3JkOiAke3JlZGlzX3Bhc3N3b3JkfVxuICAgIGRiOiAwXG4gICAgdXNlX3RsczogZmFsc2VcbiAgICBzZW50aW5lbF9tYXN0ZXJfbmFtZTogXCJcIlxuICAgIHNlbnRpbmVsX3VzZXJuYW1lOiBcIlwiXG4gICAgc2VudGluZWxfcGFzc3dvcmQ6IFwiXCJcbiAgICBzZW50aW5lbF9hZGRyZXNzZXM6IFtdXG4gICAgY2x1c3Rlcl9hZGRyZXNzZXM6IFtdXG4gICAgbWF4X3JlZGlyZWN0czogbnVsbFxudHVybjpcbiAgICBlbmFibGVkOiB0cnVlXG4gICAgZG9tYWluOiAke3R1cm5fZG9tYWlufVxuICAgIHRsc19wb3J0OiAke3R1cm5fdGxzX3BvcnR9XG4gICAgdWRwX3BvcnQ6ICR7dHVybl91ZHBfcG9ydH1cbiAgICBleHRlcm5hbF90bHM6IHRydWVcbmluZ3Jlc3M6XG4gICAgcnRtcF9iYXNlX3VybDogcnRtcDovLyR7bWFpbl9kb21haW59OiR7cnRtcF9wb3J0fS94XG4gICAgd2hpcF9iYXNlX3VybDogaHR0cHM6Ly8ke3doaXBfZG9tYWlufS93XG5rZXlzOlxuICAgICR7YXBpX2tleX06ICR7YXBpX3NlY3JldH1cblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcImVncmVzcy55YW1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbnJlZGlzOlxuICAgIGFkZHJlc3M6ICR7cmVkaXNfYWRkcmVzc31cbiAgICB1c2VybmFtZTogXCJcIlxuICAgIHBhc3N3b3JkOiAke3JlZGlzX3Bhc3N3b3JkfVxuICAgIGRiOiAwXG4gICAgdXNlX3RsczogZmFsc2VcbiAgICBzZW50aW5lbF9tYXN0ZXJfbmFtZTogXCJcIlxuICAgIHNlbnRpbmVsX3VzZXJuYW1lOiBcIlwiXG4gICAgc2VudGluZWxfcGFzc3dvcmQ6IFwiXCJcbiAgICBzZW50aW5lbF9hZGRyZXNzZXM6IFtdXG4gICAgY2x1c3Rlcl9hZGRyZXNzZXM6IFtdXG4gICAgbWF4X3JlZGlyZWN0czogbnVsbFxuYXBpX2tleTogJHthcGlfa2V5fVxuYXBpX3NlY3JldDogJHthcGlfc2VjcmV0fVxud3NfdXJsOiB3c3M6Ly8ke21haW5fZG9tYWlufVxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiaW5ncmVzcy55YW1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbnJlZGlzOlxuICAgIGFkZHJlc3M6ICR7cmVkaXNfYWRkcmVzc31cbiAgICB1c2VybmFtZTogXCJcIlxuICAgIHBhc3N3b3JkOiAke3JlZGlzX3Bhc3N3b3JkfVxuICAgIGRiOiAwXG4gICAgdXNlX3RsczogZmFsc2VcbiAgICBzZW50aW5lbF9tYXN0ZXJfbmFtZTogXCJcIlxuICAgIHNlbnRpbmVsX3VzZXJuYW1lOiBcIlwiXG4gICAgc2VudGluZWxfcGFzc3dvcmQ6IFwiXCJcbiAgICBzZW50aW5lbF9hZGRyZXNzZXM6IFtdXG4gICAgY2x1c3Rlcl9hZGRyZXNzZXM6IFtdXG4gICAgbWF4X3JlZGlyZWN0czogbnVsbFxuYXBpX2tleTogJHthcGlfa2V5fVxuYXBpX3NlY3JldDogJHthcGlfc2VjcmV0fVxud3NfdXJsOiB3c3M6Ly8ke21haW5fZG9tYWlufVxucnRtcF9wb3J0OiAke3J0bXBfcG9ydH1cbndoaXBfcG9ydDogJHt3aGlwX3BvcnR9XG5odHRwX3JlbGF5X3BvcnQ6ICR7aHR0cF9yZWxheV9wb3J0fVxubG9nZ2luZzpcbiAgICBqc29uOiBmYWxzZVxuICAgIGxldmVsOiBcIlwiXG5kZXZlbG9wbWVudDogZmFsc2VcbnJ0Y19jb25maWc6XG4gICAgdWRwX3BvcnQ6ICR7aW5ncmVzc191ZHBfcG9ydH1cbiAgICB1c2VfZXh0ZXJuYWxfaXA6IHRydWVcbiAgICBlbmFibGVfbG9vcGJhY2tfY2FuZGlkYXRlOiBmYWxzZVxuXCJcIlwiXG4iCn0=
```

## Links

`Video`,`Audio`,`Real-time`,`Streaming`,`Webrtc`

---

Version:`v1.9.0`

LiteLLMLiteLLM is a lightweight OpenAI API-compatible proxy for managing multiple LLM providers with a single endpoint.

Lobe ChatLobe Chat - an open-source, modern-design AI chat framework.

### On this page

ConfigurationBase64LinksTags