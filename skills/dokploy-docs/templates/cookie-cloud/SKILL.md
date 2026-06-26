---
title: "CookieCloud | Dokploy"
source: "https://docs.dokploy.com/docs/templates/cookie-cloud"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

CookieCloud | Dokploy

# CookieCloud

Copy as Markdown

CookieCloud lets you sync and manage browser cookies across devices securely using a self-hosted backend.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  cookiecloud:
    image: easychen/cookiecloud:latest
    restart: unless-stopped
    expose:
      - 8088
    volumes:
      - cookiecloud-data:/data/api/data
    healthcheck:
      test: ["CMD", "wget", "--spider", "-q", "http://localhost:8088"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  cookiecloud-data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "cookiecloud"
port = 8088
host = "${main_domain}"

[config.env]
# No environment variables required by default

[[config.mounts]]
# Data volume mount is defined in docker-compose.yml
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGNvb2tpZWNsb3VkOlxuICAgIGltYWdlOiBlYXN5Y2hlbi9jb29raWVjbG91ZDpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGV4cG9zZTpcbiAgICAgIC0gODA4OFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGNvb2tpZWNsb3VkLWRhdGE6L2RhdGEvYXBpL2RhdGFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcIndnZXRcIiwgXCItLXNwaWRlclwiLCBcIi1xXCIsIFwiaHR0cDovL2xvY2FsaG9zdDo4MDg4XCJdXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDNcblxudm9sdW1lczpcbiAgY29va2llY2xvdWQtZGF0YToge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjb29raWVjbG91ZFwiXG5wb3J0ID0gODA4OFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbiMgTm8gZW52aXJvbm1lbnQgdmFyaWFibGVzIHJlcXVpcmVkIGJ5IGRlZmF1bHRcblxuW1tjb25maWcubW91bnRzXV1cbiMgRGF0YSB2b2x1bWUgbW91bnQgaXMgZGVmaW5lZCBpbiBkb2NrZXItY29tcG9zZS55bWwiCn0=
```

## Links

`cookies`,`sync`,`selfhosted`,`privacy`

---

Version:`latest`

ConvexConvex is an open-source reactive database designed to make life easy for web app developers.

CoralCoral is a revolutionary commenting platform designed to enhance website interactions. It features smart technology for meaningful discussions, journalist identification, moderation tools with AI support, and complete data control without ads or trackers. Used by major news sites worldwide.

### On this page

ConfigurationBase64LinksTags