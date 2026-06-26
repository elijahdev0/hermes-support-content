---
title: "Agent DVR | Dokploy"
source: "https://docs.dokploy.com/docs/templates/agentdvr"
category: dokploy-docs
created: "2026-06-25T17:21:40.414Z"
---

Agent DVR | Dokploy

# Agent DVR

Copy as Markdown

Agent DVR is a comprehensive video surveillance software with motion detection, alerts, and remote access capabilities.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  agentdvr:
    image: mekayelanik/ispyagentdvr:latest
    restart: unless-stopped
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=${TIMEZONE:-America/New_York}
      - AGENTDVR_WEBUI_PORT=8090
    volumes:
      - agentdvr-config:/AgentDVR/Media/XML/
      - agentdvr-media:/AgentDVR/Media/WebServerRoot/Media/
      - agentdvr-commands:/AgentDVR/Commands/
    ports:
      - 8090
      - 3478/udp
      - 50000-50100/udp

volumes:
  agentdvr-config: {}
  agentdvr-media: {}
  agentdvr-commands: {}
```

```
[variables]
main_domain = "${domain}"
timezone = "America/New_York"

[config]
[[config.domains]]
serviceName = "agentdvr"
port = 8090
host = "${main_domain}"

[config.env]
TIMEZONE = "${timezone}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBhZ2VudGR2cjpcbiAgICBpbWFnZTogbWVrYXllbGFuaWsvaXNweWFnZW50ZHZyOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBVSUQ9MTAwMFxuICAgICAgLSBQR0lEPTEwMDBcbiAgICAgIC0gVFo9JHtUSU1FWk9ORTotQW1lcmljYS9OZXdfWW9ya31cbiAgICAgIC0gQUdFTlREVlJfV0VCVUlfUE9SVD04MDkwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gYWdlbnRkdnItY29uZmlnOi9BZ2VudERWUi9NZWRpYS9YTUwvXG4gICAgICAtIGFnZW50ZHZyLW1lZGlhOi9BZ2VudERWUi9NZWRpYS9XZWJTZXJ2ZXJSb290L01lZGlhL1xuICAgICAgLSBhZ2VudGR2ci1jb21tYW5kczovQWdlbnREVlIvQ29tbWFuZHMvXG4gICAgcG9ydHM6XG4gICAgICAtIDgwOTBcbiAgICAgIC0gMzQ3OC91ZHBcbiAgICAgIC0gNTAwMDAtNTAxMDAvdWRwXG5cbnZvbHVtZXM6XG4gIGFnZW50ZHZyLWNvbmZpZzoge31cbiAgYWdlbnRkdnItbWVkaWE6IHt9XG4gIGFnZW50ZHZyLWNvbW1hbmRzOiB7fSIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG50aW1lem9uZSA9IFwiQW1lcmljYS9OZXdfWW9ya1wiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhZ2VudGR2clwiXG5wb3J0ID0gODA5MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblRJTUVaT05FID0gXCIke3RpbWV6b25lfVwiXG5cbltbY29uZmlnLm1vdW50c11dIgp9
```

## Links

`surveillance`,`security`,`video`,`monitoring`,`dvr`,`camera`

---

Version:`latest`

Affine ProAffine Pro is a modern, self-hosted platform designed for collaborative content creation and project management. It offers an intuitive interface, seamless real-time collaboration, and powerful tools for organizing tasks, notes, and ideas.

AkauntingAkaunting is a self-hosted, open-source accounting app for small businesses.

### On this page

ConfigurationBase64LinksTags