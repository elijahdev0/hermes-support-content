---
title: "Web-Check | Dokploy"
source: "https://docs.dokploy.com/docs/templates/web-check"
category: dokploy-docs
created: "2026-06-25T17:22:01.420Z"
---

Web-Check | Dokploy

# Web-Check

Web-Check is a powerful all-in-one website analyzer that provides detailed insights into any website's security, performance, and functionality.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.9'
services:
  web-check:
    image: lissy93/web-check
    ports:
      - 3000
    restart: unless-stopped
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "web-check"
port = 3000
host = "${main_domain}"

[config.env]
GOOGLE_CLOUD_API_KEY = ""
TORRENT_IP_API_KEY = ""
SECURITY_TRAILS_API_KEY = ""
BUILT_WITH_API_KEY = ""
URL_SCAN_API_KEY = ""
TRANCO_USERNAME = ""
TRANCO_API_KEY = ""
CLOUDMERSIVE_API_KEY = ""

REACT_APP_SHODAN_API_KEY = ""
REACT_APP_WHO_API_KEY = ""

# CHROME_PATH = "/usr/bin/chromium"
PORT = "3000"
DISABLE_GUI = "false"
API_TIMEOUT_LIMIT = "10000"
API_CORS_ORIGIN = "*"
API_ENABLE_RATE_LIMIT = "true"
ENABLE_ANALYTICS = "false"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjknXG5zZXJ2aWNlczpcbiAgd2ViLWNoZWNrOlxuICAgIGltYWdlOiBsaXNzeTkzL3dlYi1jaGVja1xuICAgIHBvcnRzOlxuICAgICAgLSAzMDAwXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ3ZWItY2hlY2tcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5HT09HTEVfQ0xPVURfQVBJX0tFWSA9IFwiXCJcblRPUlJFTlRfSVBfQVBJX0tFWSA9IFwiXCJcblNFQ1VSSVRZX1RSQUlMU19BUElfS0VZID0gXCJcIlxuQlVJTFRfV0lUSF9BUElfS0VZID0gXCJcIlxuVVJMX1NDQU5fQVBJX0tFWSA9IFwiXCJcblRSQU5DT19VU0VSTkFNRSA9IFwiXCJcblRSQU5DT19BUElfS0VZID0gXCJcIlxuQ0xPVURNRVJTSVZFX0FQSV9LRVkgPSBcIlwiXG5cblJFQUNUX0FQUF9TSE9EQU5fQVBJX0tFWSA9IFwiXCJcblJFQUNUX0FQUF9XSE9fQVBJX0tFWSA9IFwiXCJcblxuIyBDSFJPTUVfUEFUSCA9IFwiL3Vzci9iaW4vY2hyb21pdW1cIiBcblBPUlQgPSBcIjMwMDBcIiAgICAgICAgICAgICAgICAgICAgXG5ESVNBQkxFX0dVSSA9IFwiZmFsc2VcIiAgICAgICAgICAgICBcbkFQSV9USU1FT1VUX0xJTUlUID0gXCIxMDAwMFwiICAgICAgXG5BUElfQ09SU19PUklHSU4gPSBcIipcIiAgICAgICAgICAgIFxuQVBJX0VOQUJMRV9SQVRFX0xJTUlUID0gXCJ0cnVlXCIgICAgXG5FTkFCTEVfQU5BTFlUSUNTID0gXCJmYWxzZVwiICAgICAgIFxuXG5bW2NvbmZpZy5tb3VudHNdXVxuIgp9
```

## Links

- Website
- Github
- Documentation

`website-analyzer`,`security`,`performance`,`seo`

---

Version:`latest`

WandererWanderer is a self-hosted mapping and geolocation platform powered by Meilisearch, PocketBase, and a web frontend.

WG-EasyWG-Easy is a simple and user-friendly WireGuard VPN server with a web interface for easy management.

### On this page

ConfigurationBase64LinksTags

