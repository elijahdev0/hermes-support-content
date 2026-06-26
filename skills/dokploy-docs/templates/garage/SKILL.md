---
title: "Garage S3 | Dokploy"
source: "https://docs.dokploy.com/docs/templates/garage"
category: dokploy-docs
created: "2026-06-25T17:21:48.521Z"
---

Garage S3 | Dokploy

# Garage S3

Copy as Markdown

Garage is an open-source distributed object storage service tailored for self-hosting.

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
]

[[config.domains]]
serviceName = "garage"
port = 3900
host = "${main_domain}"

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
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBnYXJhZ2U6XG4gICAgaW1hZ2U6IGR4Zmxycy9nYXJhZ2U6djIuMC4wXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvZ2FyYWdlLnRvbWw6L2V0Yy9nYXJhZ2UudG9tbFxuICAgICAgLSBnYXJhZ2Utc3RvcmFnZTovdmFyL2xpYi9nYXJhZ2VcbiAgICAgIC0gZ2FyYWdlLXN0b3JhZ2U6L3Zhci9saWIvZ2FyYWdlXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gMzkwMFxuICAgICAgLSAzOTAxXG4gICAgICAtIDM5MDJcbiAgICAgIC0gMzkwM1xuXG52b2x1bWVzOlxuICBnYXJhZ2Utc3RvcmFnZToge30iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxud2VidWlfZG9tYWluID0gXCJ3ZWItdWkuJHtkb21haW59XCJcbmFkbWluX3Rva2VuID0gXCIke2Jhc2U2NDozMn1cIlxubWV0cmljc190b2tlbiA9IFwiJHtiYXNlNjQ6MzJ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgICBcIkFQSV9CQVNFX1VSTD1odHRwOi8vZ2FyYWdlOjM5MDNcIixcbiAgICBcIlMzX0VORFBPSU5UX1VSTD1odHRwOi8vZ2FyYWdlOjM5MDBcIixcbl1cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZ2FyYWdlXCJcbnBvcnQgPSAzOTAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiZ2FyYWdlLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxubWV0YWRhdGFfZGlyID0gXCIvdmFyL2xpYi9nYXJhZ2UvbWV0YVwiXG5kYXRhX2RpciA9IFwiL3Zhci9saWIvZ2FyYWdlL2RhdGFcIlxuZGJfZW5naW5lID0gXCJzcWxpdGVcIlxubWV0YWRhdGFfYXV0b19zbmFwc2hvdF9pbnRlcnZhbCA9IFwiNmhcIlxuXG5yZXBsaWNhdGlvbl9mYWN0b3IgPSAxXG5jb21wcmVzc2lvbl9sZXZlbCA9IDJcblxucnBjX2JpbmRfYWRkciA9IFwiWzo6XTozOTAxXCJcbnJwY19wdWJsaWNfYWRkciA9IFwibG9jYWxob3N0OjM5MDFcIiAjIFJlcXVpcmVkXG5ycGNfc2VjcmV0ID0gXCIke2hhc2g6NjR9XCJcblxuW3MzX2FwaV1cbnMzX3JlZ2lvbiA9IFwiZ2FyYWdlXCJcbmFwaV9iaW5kX2FkZHIgPSBcIls6Ol06MzkwMFwiXG5yb290X2RvbWFpbiA9IFwiLnMzLmRvbWFpbi5jb21cIlxuXG5bczNfd2ViXSAjIE9wdGlvbmFsLCBpZiB5b3Ugd2FudCB0byBleHBvc2UgYnVja2V0IGFzIHdlYlxuYmluZF9hZGRyID0gXCJbOjpdOjM5MDJcIlxucm9vdF9kb21haW4gPSBcIi53ZWIuZG9tYWluLmNvbVwiXG5pbmRleCA9IFwiaW5kZXguaHRtbFwiXG5cblthZG1pbl0gIyBSZXF1aXJlZFxuYXBpX2JpbmRfYWRkciA9IFwiWzo6XTozOTAzXCJcbmFkbWluX3Rva2VuID0gXCIke2FkbWluX3Rva2VufVwiXG5tZXRyaWNzX3JlcXVpcmVfdG9rZW4gPSB0cnVlXG5tZXRyaWNzX3Rva2VuID0gXCIke21ldHJpY3NfdG9rZW59XCJcblwiXCJcIiIKfQ==
```

## Links

`storage`,`object-storage`

---

Version:`latest`

FreshRSSA free, self-hostable RSS and Atom feed aggregator. Lightweight, easy to work with, powerful, and customizable with themes and extensions.

Garage S3 with Web UIGarage is an open-source distributed object storage service tailored for self-hosting. For authentication in the web-ui please go to https://github.com/khairul169/garage-webui?tab=readme-ov-file#authentication

### On this page

ConfigurationBase64LinksTags