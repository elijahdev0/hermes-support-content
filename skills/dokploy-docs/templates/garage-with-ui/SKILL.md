---
title: "Garage S3 with Web UI | Dokploy"
source: "https://docs.dokploy.com/docs/templates/garage-with-ui"
category: dokploy-docs
created: "2026-06-25T17:21:48.522Z"
---

Garage S3 with Web UI | Dokploy

# Garage S3 with Web UI

Copy as Markdown

Garage is an open-source distributed object storage service tailored for self-hosting. For authentication in the web-ui please go to https://github.com/khairul169/garage-webui?tab=readme-ov-file#authentication

## Configuration

docker-compose.ymltemplate.toml

```
services:
  garage:
    image: dxflrs/garage:v2.0.0
    volumes:
      - ../files/garage.toml:/etc/garage.toml
      - garage-storage:/var/lib/garage
      - garage-storage:/var/lib/garage
    restart: unless-stopped
    ports:
      - 3900
      - 3901
      - 3902
      - 3903

  garage-webui:
    image: khairul169/garage-webui:1.1.0
    restart: unless-stopped
    volumes:
      - ../files/garage.toml:/etc/garage.toml:ro
    ports:
      - 3909
    environment:
      - AUTH_USER_PASS
      - API_BASE_URL
      - S3_ENDPOINT_URL

volumes:
  garage-storage: {}
```

```
[variables]
main_domain = "${domain}"
webui_domain = "web-ui.${domain}"
admin_token = "${base64:32}"
metrics_token = "${base64:32}"

[config]
env = [
    "API_BASE_URL=http://garage:3903",
    "S3_ENDPOINT_URL=http://garage:3900",
    "",
    "# To set up auth for the web-ui please go here: https://github.com/khairul169/garage-webui?tab=readme-ov-file#authentication",
    "# or run this command: htpasswd -nbBC 10 'YOUR_USERNAME' 'YOUR_PASSWORD' and paste the output in here.",
    "AUTH_USER_PASS=",
]

[[config.domains]]
serviceName = "garage"
port = 3900
host = "${main_domain}"

[[config.domains]]
serviceName = "garage-webui"
port = 3909
host = "${webui_domain}"

[[config.mounts]]
filePath = "garage.toml"
content = """
metadata_dir = "/var/lib/garage/meta"
data_dir = "/var/lib/garage/data"
db_engine = "sqlite"
metadata_auto_snapshot_interval = "6h"

replication_factor = 1
compression_level = 2

rpc_bind_addr = "[::]:3901"
rpc_public_addr = "localhost:3901" # Required
rpc_secret = "${hash:64}"

[s3_api]
s3_region = "garage"
api_bind_addr = "[::]:3900"
root_domain = ".s3.domain.com"

[s3_web] # Optional, if you want to expose bucket as web
bind_addr = "[::]:3902"
root_domain = ".web.domain.com"
index = "index.html"

[admin] # Required
api_bind_addr = "[::]:3903"
admin_token = "${admin_token}"
metrics_require_token = true
metrics_token = "${metrics_token}"
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBnYXJhZ2U6XG4gICAgaW1hZ2U6IGR4Zmxycy9nYXJhZ2U6djIuMC4wXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvZ2FyYWdlLnRvbWw6L2V0Yy9nYXJhZ2UudG9tbFxuICAgICAgLSBnYXJhZ2Utc3RvcmFnZTovdmFyL2xpYi9nYXJhZ2VcbiAgICAgIC0gZ2FyYWdlLXN0b3JhZ2U6L3Zhci9saWIvZ2FyYWdlXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gMzkwMFxuICAgICAgLSAzOTAxXG4gICAgICAtIDM5MDJcbiAgICAgIC0gMzkwM1xuXG4gIGdhcmFnZS13ZWJ1aTpcbiAgICBpbWFnZToga2hhaXJ1bDE2OS9nYXJhZ2Utd2VidWk6MS4xLjBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL2dhcmFnZS50b21sOi9ldGMvZ2FyYWdlLnRvbWw6cm9cbiAgICBwb3J0czpcbiAgICAgIC0gMzkwOVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBBVVRIX1VTRVJfUEFTU1xuICAgICAgLSBBUElfQkFTRV9VUkxcbiAgICAgIC0gUzNfRU5EUE9JTlRfVVJMXG5cbnZvbHVtZXM6XG4gIGdhcmFnZS1zdG9yYWdlOiB7fSIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG53ZWJ1aV9kb21haW4gPSBcIndlYi11aS4ke2RvbWFpbn1cIlxuYWRtaW5fdG9rZW4gPSBcIiR7YmFzZTY0OjMyfVwiXG5tZXRyaWNzX3Rva2VuID0gXCIke2Jhc2U2NDozMn1cIlxuXG5cbltjb25maWddXG5lbnYgPSBbXG4gICAgXCJBUElfQkFTRV9VUkw9aHR0cDovL2dhcmFnZTozOTAzXCIsXG4gICAgXCJTM19FTkRQT0lOVF9VUkw9aHR0cDovL2dhcmFnZTozOTAwXCIsXG4gICAgXCJcIixcbiAgICBcIiMgVG8gc2V0IHVwIGF1dGggZm9yIHRoZSB3ZWItdWkgcGxlYXNlIGdvIGhlcmU6IGh0dHBzOi8vZ2l0aHViLmNvbS9raGFpcnVsMTY5L2dhcmFnZS13ZWJ1aT90YWI9cmVhZG1lLW92LWZpbGUjYXV0aGVudGljYXRpb25cIixcbiAgICBcIiMgb3IgcnVuIHRoaXMgY29tbWFuZDogaHRwYXNzd2QgLW5iQkMgMTAgJ1lPVVJfVVNFUk5BTUUnICdZT1VSX1BBU1NXT1JEJyBhbmQgcGFzdGUgdGhlIG91dHB1dCBpbiBoZXJlLlwiLFxuICAgIFwiQVVUSF9VU0VSX1BBU1M9XCIsXG5dXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImdhcmFnZVwiXG5wb3J0ID0gMzkwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJnYXJhZ2Utd2VidWlcIlxucG9ydCA9IDM5MDlcbmhvc3QgPSBcIiR7d2VidWlfZG9tYWlufVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiZ2FyYWdlLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxubWV0YWRhdGFfZGlyID0gXCIvdmFyL2xpYi9nYXJhZ2UvbWV0YVwiXG5kYXRhX2RpciA9IFwiL3Zhci9saWIvZ2FyYWdlL2RhdGFcIlxuZGJfZW5naW5lID0gXCJzcWxpdGVcIlxubWV0YWRhdGFfYXV0b19zbmFwc2hvdF9pbnRlcnZhbCA9IFwiNmhcIlxuXG5yZXBsaWNhdGlvbl9mYWN0b3IgPSAxXG5jb21wcmVzc2lvbl9sZXZlbCA9IDJcblxucnBjX2JpbmRfYWRkciA9IFwiWzo6XTozOTAxXCJcbnJwY19wdWJsaWNfYWRkciA9IFwibG9jYWxob3N0OjM5MDFcIiAjIFJlcXVpcmVkXG5ycGNfc2VjcmV0ID0gXCIke2hhc2g6NjR9XCJcblxuW3MzX2FwaV1cbnMzX3JlZ2lvbiA9IFwiZ2FyYWdlXCJcbmFwaV9iaW5kX2FkZHIgPSBcIls6Ol06MzkwMFwiXG5yb290X2RvbWFpbiA9IFwiLnMzLmRvbWFpbi5jb21cIlxuXG5bczNfd2ViXSAjIE9wdGlvbmFsLCBpZiB5b3Ugd2FudCB0byBleHBvc2UgYnVja2V0IGFzIHdlYlxuYmluZF9hZGRyID0gXCJbOjpdOjM5MDJcIlxucm9vdF9kb21haW4gPSBcIi53ZWIuZG9tYWluLmNvbVwiXG5pbmRleCA9IFwiaW5kZXguaHRtbFwiXG5cblthZG1pbl0gIyBSZXF1aXJlZFxuYXBpX2JpbmRfYWRkciA9IFwiWzo6XTozOTAzXCJcbmFkbWluX3Rva2VuID0gXCIke2FkbWluX3Rva2VufVwiXG5tZXRyaWNzX3JlcXVpcmVfdG9rZW4gPSB0cnVlXG5tZXRyaWNzX3Rva2VuID0gXCIke21ldHJpY3NfdG9rZW59XCJcblwiXCJcIiIKfQ==
```

## Links

`storage`,`object-storage`

---

Version:`latest`

Garage S3Garage is an open-source distributed object storage service tailored for self-hosting.

GhostGhost is a free and open source, professional publishing platform built on a modern Node.js technology stack.

### On this page

ConfigurationBase64LinksTags