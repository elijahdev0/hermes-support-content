---
title: "OpenSpeedTest | Dokploy"
source: "https://docs.dokploy.com/docs/templates/openspeedtest"
category: dokploy-docs
created: "2026-06-25T17:21:55.476Z"
---

OpenSpeedTest | Dokploy

# OpenSpeedTest

Copy as Markdown

OpenSpeedTest is a 100% browser-based HTML5 network performance estimation tool for accurately measuring network speed.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  openspeedtest:
    image: openspeedtest/latest:latest
    restart: unless-stopped
    ports:
      - 3000
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "openspeedtest"
port = 3000
host = "${main_domain}"

[config.env]

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBvcGVuc3BlZWR0ZXN0OlxuICAgIGltYWdlOiBvcGVuc3BlZWR0ZXN0L2xhdGVzdDpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSAzMDAwIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIm9wZW5zcGVlZHRlc3RcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5cbltbY29uZmlnLm1vdW50c11dIgp9
```

## Links

`network`,`testing`,`performance`,`monitoring`,`bandwidth`

---

Version:`latest`

OpenResty ManagerThe easiest using, powerful and beautiful OpenResty Manager (Nginx Enhanced Version) , open source alternative to OpenResty Edge, which can enable you to easily reverse proxy your websites with security running at home or internet, including Access Control, HTTP Flood Protection, Free SSL, without having to know too much about OpenResty or Let's Encrypt.

Otter WikiAn Otter Wiki is a simple, lightweight, and fast wiki engine built with Python and Flask. It provides a user-friendly interface for creating and managing wiki content with markdown support.

### On this page

ConfigurationBase64LinksTags