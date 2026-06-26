---
title: "Neko | Dokploy"
source: "https://docs.dokploy.com/docs/templates/neko"
category: dokploy-docs
created: "2026-06-25T17:21:54.354Z"
---

Neko | Dokploy

# Neko

Copy as Markdown

Neko is a self-hosted virtual browser that runs in Docker and allows you to share browser sessions with others.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  neko:
    image: "ghcr.io/m1k1o/neko/firefox:latest"
    restart: "unless-stopped"
    shm_size: "2gb"
    ports:
      - "8080"
      - "52000-52100:52000-52100/udp"
```

```
[variables]
main_domain = "${domain}"
admin_password = "${password:16}"
user_password = "${password:16}"

[config]
[[config.domains]]
serviceName = "neko"
port = 8080
host = "${main_domain}"

[config.env]
NEKO_MEMBER_PROVIDER = "multiuser"
NEKO_DESKTOP_SCREEN = "1920x1080@30"
# API keys used for authentication
NEKO_MEMBER_MULTIUSER_USER_PASSWORD = "${user_password}"
# API keys used for authentication
NEKO_MEMBER_MULTIUSER_ADMIN_PASSWORD = "${admin_password}"
NEKO_WEBRTC_EPR = "52000-52100"
NEKO_WEBRTC_ICELITE = "1"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBuZWtvOlxuICAgIGltYWdlOiBcImdoY3IuaW8vbTFrMW8vbmVrby9maXJlZm94OmxhdGVzdFwiXG4gICAgcmVzdGFydDogXCJ1bmxlc3Mtc3RvcHBlZFwiXG4gICAgc2htX3NpemU6IFwiMmdiXCJcbiAgICBwb3J0czpcbiAgICAgIC0gXCI4MDgwXCJcbiAgICAgIC0gXCI1MjAwMC01MjEwMDo1MjAwMC01MjEwMC91ZHBcIlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmFkbWluX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG51c2VyX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJuZWtvXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuTkVLT19NRU1CRVJfUFJPVklERVIgPSBcIm11bHRpdXNlclwiXG5ORUtPX0RFU0tUT1BfU0NSRUVOID0gXCIxOTIweDEwODBAMzBcIlxuIyBBUEkga2V5cyB1c2VkIGZvciBhdXRoZW50aWNhdGlvblxuTkVLT19NRU1CRVJfTVVMVElVU0VSX1VTRVJfUEFTU1dPUkQgPSBcIiR7dXNlcl9wYXNzd29yZH1cIlxuIyBBUEkga2V5cyB1c2VkIGZvciBhdXRoZW50aWNhdGlvblxuTkVLT19NRU1CRVJfTVVMVElVU0VSX0FETUlOX1BBU1NXT1JEID0gXCIke2FkbWluX3Bhc3N3b3JkfVwiXG5ORUtPX1dFQlJUQ19FUFIgPSBcIjUyMDAwLTUyMTAwXCJcbk5FS09fV0VCUlRDX0lDRUxJVEUgPSBcIjFcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuIgp9
```

## Links

`browser`,`virtual`,`sharing`,`remote`

---

Version:`latest`

NavidromeNavidrome is a modern music server and streamer compatible with Subsonic/Airsonic. Stream your music collection anywhere.

NetdataNetdata is a real-time performance monitoring tool that provides comprehensive system metrics, application monitoring, and infrastructure health insights.

### On this page

ConfigurationBase64LinksTags