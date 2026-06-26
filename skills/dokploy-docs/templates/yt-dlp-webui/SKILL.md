---
title: "yt-dlp-webui | Dokploy"
source: "https://docs.dokploy.com/docs/templates/yt-dlp-webui"
category: dokploy-docs
created: "2026-06-25T17:22:02.523Z"
---

yt-dlp-webui | Dokploy

# yt-dlp-webui

Copy as Markdown

yt-dlp-webui is a web interface for yt-dlp, allowing you to download videos and audio from various platforms with a simple web UI.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  yt-dlp-webui:
    image: marcobaobao/yt-dlp-webui
    ports:
      - 3033
    volumes:
      - downloads:/downloads
      - config:/config
    healthcheck:
      test: curl -f http://localhost:3033 || exit 1
    restart: unless-stopped

volumes:
  downloads: {}
  config: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "yt-dlp-webui"
port = 3033
host = "${main_domain}"

[config.env]

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICB5dC1kbHAtd2VidWk6XG4gICAgaW1hZ2U6IG1hcmNvYmFvYmFvL3l0LWRscC13ZWJ1aVxuICAgIHBvcnRzOlxuICAgICAgLSAzMDMzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZG93bmxvYWRzOi9kb3dubG9hZHNcbiAgICAgIC0gY29uZmlnOi9jb25maWdcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IGN1cmwgLWYgaHR0cDovL2xvY2FsaG9zdDozMDMzIHx8IGV4aXQgMVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbnZvbHVtZXM6XG4gIGRvd25sb2Fkczoge31cbiAgY29uZmlnOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInl0LWRscC13ZWJ1aVwiXG5wb3J0ID0gMzAzM1xuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblxuW1tjb25maWcubW91bnRzXV1cbiIKfQ==
```

## Links

`downloader`,`youtube`,`media`,`webui`

---

Version:`latest`

YOURLSYOURLS (Your Own URL Shortener) is a set of PHP scripts that will allow you to run your own URL shortening service (a la TinyURL or Bitly).

ZabbixZabbix is an open-source enterprise-grade monitoring platform for networks, servers, virtual machines, and cloud services. This template includes PostgreSQL, Nginx frontend, SNMP traps, and Java gateway.

### On this page

ConfigurationBase64LinksTags