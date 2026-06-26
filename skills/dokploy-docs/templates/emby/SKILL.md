---
title: "Emby | Dokploy"
source: "https://docs.dokploy.com/docs/templates/emby"
category: dokploy-docs
created: "2026-06-25T17:21:47.358Z"
---

Emby | Dokploy

# Emby

Copy as Markdown

Emby Server is a personal media server with apps on just about every device.

## Configuration

docker-compose.ymltemplate.toml

```
version: "2.3"
services:
  emby:
    image: emby/embyserver
    # Uncomment to enable DLNA and Wake-on-Lan
    # network_mode: host
    environment:
      - UID=1000 # The UID to run emby as (default: 2)
      - GID=100 # The GID to run emby as (default 2)
      - GIDLIST=100 # A comma-separated list of additional GIDs to run emby as (default: 2)
    volumes:
      - /emby/programdata:/config # Configuration directory
      - /emby/series:/mnt/share1 # Media directory
      - /emby/movies:/mnt/share2 # Media directory
    ports:
      - 8096 # HTTP port
      - 8920 # HTTPS port
    devices:
      - /dev/dri:/dev/dri # VAAPI/NVDEC/NVENC render nodes
    restart: on-failure
```

```
[variables]
main_domain = "${domain}"
api_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "emby"
port = 8096
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMi4zXCJcbnNlcnZpY2VzOlxuICBlbWJ5OlxuICAgIGltYWdlOiBlbWJ5L2VtYnlzZXJ2ZXJcbiAgICAjIFVuY29tbWVudCB0byBlbmFibGUgRExOQSBhbmQgV2FrZS1vbi1MYW5cbiAgICAjIG5ldHdvcmtfbW9kZTogaG9zdFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBVSUQ9MTAwMCAjIFRoZSBVSUQgdG8gcnVuIGVtYnkgYXMgKGRlZmF1bHQ6IDIpXG4gICAgICAtIEdJRD0xMDAgIyBUaGUgR0lEIHRvIHJ1biBlbWJ5IGFzIChkZWZhdWx0IDIpXG4gICAgICAtIEdJRExJU1Q9MTAwICMgQSBjb21tYS1zZXBhcmF0ZWQgbGlzdCBvZiBhZGRpdGlvbmFsIEdJRHMgdG8gcnVuIGVtYnkgYXMgKGRlZmF1bHQ6IDIpXG4gICAgdm9sdW1lczpcbiAgICAgIC0gL2VtYnkvcHJvZ3JhbWRhdGE6L2NvbmZpZyAjIENvbmZpZ3VyYXRpb24gZGlyZWN0b3J5XG4gICAgICAtIC9lbWJ5L3NlcmllczovbW50L3NoYXJlMSAjIE1lZGlhIGRpcmVjdG9yeVxuICAgICAgLSAvZW1ieS9tb3ZpZXM6L21udC9zaGFyZTIgIyBNZWRpYSBkaXJlY3RvcnlcbiAgICBwb3J0czpcbiAgICAgIC0gODA5NiAjIEhUVFAgcG9ydFxuICAgICAgLSA4OTIwICMgSFRUUFMgcG9ydFxuICAgIGRldmljZXM6XG4gICAgICAtIC9kZXYvZHJpOi9kZXYvZHJpICMgVkFBUEkvTlZERUMvTlZFTkMgcmVuZGVyIG5vZGVzXG4gICAgcmVzdGFydDogb24tZmFpbHVyZSIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5hcGlfZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImVtYnlcIlxucG9ydCA9IDgwOTZcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`media`,`media system`

---

Version:`4.9.1.17`

ElasticsearchElasticsearch is an open-source search and analytics engine, used for full-text search and analytics on structured data such as text, web pages, images, and videos.

EMQXA scalable and reliable MQTT broker for AI, IoT, IIoT and connected vehicles

### On this page

ConfigurationBase64LinksTags