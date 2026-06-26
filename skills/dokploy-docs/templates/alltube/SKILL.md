---
title: "AllTube | Dokploy"
source: "https://docs.dokploy.com/docs/templates/alltube"
category: dokploy-docs
created: "2026-06-25T17:21:40.414Z"
---

AllTube | Dokploy

# AllTube

Copy as Markdown

AllTube Download is an application designed to facilitate the downloading of videos from YouTube and other video sites. It provides an HTML GUI for youtube-dl with video conversion capabilities and JSON API support.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  alltube:
    image: dnomd343/alltube:latest
    restart: unless-stopped
    ports:
      - 80
    environment:
      - TITLE=${TITLE}
      - CONVERT=${CONVERT}
      - STREAM=${STREAM}
      - REMUX=${REMUX}
```

```
[variables]
main_domain = "${domain}"
title = "My AllTube Site"
convert = "true"
stream = "true"
remux = "true"

[config]
[[config.domains]]
serviceName = "alltube"
port = 80
host = "${main_domain}"

[config.env]
TITLE = "${title}"
CONVERT = "${convert}"
STREAM = "${stream}"
REMUX = "${remux}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhbGx0dWJlOlxuICAgIGltYWdlOiBkbm9tZDM0My9hbGx0dWJlOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDgwXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFRJVExFPSR7VElUTEV9XG4gICAgICAtIENPTlZFUlQ9JHtDT05WRVJUfVxuICAgICAgLSBTVFJFQU09JHtTVFJFQU19XG4gICAgICAtIFJFTVVYPSR7UkVNVVh9ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG50aXRsZSA9IFwiTXkgQWxsVHViZSBTaXRlXCJcbmNvbnZlcnQgPSBcInRydWVcIlxuc3RyZWFtID0gXCJ0cnVlXCJcbnJlbXV4ID0gXCJ0cnVlXCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFsbHR1YmVcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuVElUTEUgPSBcIiR7dGl0bGV9XCJcbkNPTlZFUlQgPSBcIiR7Y29udmVydH1cIlxuU1RSRUFNID0gXCIke3N0cmVhbX1cIlxuUkVNVVggPSBcIiR7cmVtdXh9XCIgIgp9
```

## Links

`media`,`video`,`downloader`

---

Version:`latest`

AList🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs.

AmpacheAmpache is a web-based audio/video streaming application and file manager allowing you to access your music & videos from anywhere, using almost any internet enabled device.

### On this page

ConfigurationBase64LinksTags