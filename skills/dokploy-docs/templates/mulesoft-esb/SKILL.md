---
title: "MuleSoft ESB Runtime Community Edition | Dokploy"
source: "https://docs.dokploy.com/docs/templates/mulesoft-esb"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

MuleSoft ESB Runtime Community Edition | Dokploy

# MuleSoft ESB Runtime Community Edition

Copy as Markdown

MuleSoft ESB Runtime is a lightweight, Java-based integration platform that allows you to easily integrate applications, data sources, and APIs. It provides powerful connectors and data transformation capabilities for building robust integration solutions.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  mule:
    image: yogeshmulecraft/mulece-esb:latest
    restart: unless-stopped
    ports:
      - "8081"
    environment:
      - MULE_VERSION=${MULE_VERSION:-4.9.0}
      - HTTP_PORT=${HTTP_PORT:-8081}
      - MULE_HOME=/opt/mule-standalone
      - MULE_BASE=/opt/mule-standalone
      - TZ=UTC
      - MULE_VERBOSE_EXCEPTIONS=true
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost:${HTTP_PORT:-8081}/ || exit 0"]
      interval: 60s
      timeout: 20s
      retries: 5
      start_period: 120s
```

```
# MuleSoft ESB Deployment Configuration

[variables]
main_domain = "${domain}"
timezone = "UTC"
mule_version = "4.9.0"
http_port = "8081"

[config]
[[config.domains]]
serviceName = "mule"
port = 8081
host = "${main_domain}"
path = "/"

[config.env]
MULE_VERSION = "${mule_version}"
HTTP_PORT = "${http_port}"
MULE_HOME = "/opt/mule-standalone"
MULE_BASE = "/opt/mule-standalone"
TZ = "${timezone}"
MULE_VERBOSE_EXCEPTIONS = "true"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIG11bGU6XG4gICAgaW1hZ2U6IHlvZ2VzaG11bGVjcmFmdC9tdWxlY2UtZXNiOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIFwiODA4MVwiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE1VTEVfVkVSU0lPTj0ke01VTEVfVkVSU0lPTjotNC45LjB9XG4gICAgICAtIEhUVFBfUE9SVD0ke0hUVFBfUE9SVDotODA4MX1cbiAgICAgIC0gTVVMRV9IT01FPS9vcHQvbXVsZS1zdGFuZGFsb25lXG4gICAgICAtIE1VTEVfQkFTRT0vb3B0L211bGUtc3RhbmRhbG9uZVxuICAgICAgLSBUWj1VVENcbiAgICAgIC0gTVVMRV9WRVJCT1NFX0VYQ0VQVElPTlM9dHJ1ZVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwiY3VybCAtZiBodHRwOi8vbG9jYWxob3N0OiR7SFRUUF9QT1JUOi04MDgxfS8gfHwgZXhpdCAwXCJdXG4gICAgICBpbnRlcnZhbDogNjBzXG4gICAgICB0aW1lb3V0OiAyMHNcbiAgICAgIHJldHJpZXM6IDVcbiAgICAgIHN0YXJ0X3BlcmlvZDogMTIwc1xuXG4iLAogICJjb25maWciOiAiXG4jIE11bGVTb2Z0IEVTQiBEZXBsb3ltZW50IENvbmZpZ3VyYXRpb25cblxuW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxudGltZXpvbmUgPSBcIlVUQ1wiXG5tdWxlX3ZlcnNpb24gPSBcIjQuOS4wXCJcbmh0dHBfcG9ydCA9IFwiODA4MVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJtdWxlXCJcbnBvcnQgPSA4MDgxXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5wYXRoID0gXCIvXCJcblxuW2NvbmZpZy5lbnZdXG5NVUxFX1ZFUlNJT04gPSBcIiR7bXVsZV92ZXJzaW9ufVwiXG5IVFRQX1BPUlQgPSBcIiR7aHR0cF9wb3J0fVwiXG5NVUxFX0hPTUUgPSBcIi9vcHQvbXVsZS1zdGFuZGFsb25lXCJcbk1VTEVfQkFTRSA9IFwiL29wdC9tdWxlLXN0YW5kYWxvbmVcIlxuVFogPSBcIiR7dGltZXpvbmV9XCJcbk1VTEVfVkVSQk9TRV9FWENFUFRJT05TID0gXCJ0cnVlXCJcbiIKfQ==
```

## Links

`integration`,`api`,`esb`,`enterprise`,`java`

---

Version:`latest`

MovaryMovary is a self-hosted platform for tracking and managing your watched movies using TMDB.

MumbleMumble is an open-source, low-latency, high-quality voice chat software primarily intended for use while gaming.

### On this page

ConfigurationBase64LinksTags