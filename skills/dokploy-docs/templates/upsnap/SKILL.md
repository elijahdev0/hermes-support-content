---
title: "Upsnap | Dokploy"
source: "https://docs.dokploy.com/docs/templates/upsnap"
category: dokploy-docs
created: "2026-06-25T17:22:01.419Z"
---

Upsnap | Dokploy

# Upsnap

Copy as Markdown

Upsnap is a simple network device monitor and dashboard built on PocketBase.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  upsnap:
    image: ghcr.io/seriousm4x/upsnap:5
    restart: unless-stopped
    expose:
      - 8090
    volumes:
      - upsnap-data:/app/pb_data
    environment:
      - TZ=${TZ}
      - UPSNAP_INTERVAL=${UPSNAP_INTERVAL}
      - UPSNAP_SCAN_RANGE=${UPSNAP_SCAN_RANGE}
      - UPSNAP_SCAN_TIMEOUT=${UPSNAP_SCAN_TIMEOUT}
      - UPSNAP_PING_PRIVILEGED=${UPSNAP_PING_PRIVILEGED}
      - UPSNAP_WEBSITE_TITLE=${UPSNAP_WEBSITE_TITLE}
    healthcheck:
      test: ["CMD", "curl", "-fs", "http://localhost:8090/api/health"]
      interval: 10s
      timeout: 3s
      retries: 3

volumes:
  upsnap-data:
    driver: local
```

```
[variables]
main_domain = "${domain}"
upsnap_password = "${password:32}"

[config]

[[config.domains]]
serviceName = "upsnap"
port = 8090
host = "${main_domain}"
path = "/"

[config.env]
TZ = "Europe/Berlin"
UPSNAP_INTERVAL = "*/10 * * * * *"
UPSNAP_SCAN_RANGE = "192.168.1.0/24"
UPSNAP_SCAN_TIMEOUT = "500ms"
UPSNAP_PING_PRIVILEGED = "true"
UPSNAP_WEBSITE_TITLE = "Upsnap Network Monitor"

[[config.mounts]]
source = "upsnap-data"
target = "/app/pb_data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB1cHNuYXA6XG4gICAgaW1hZ2U6IGdoY3IuaW8vc2VyaW91c200eC91cHNuYXA6NVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZXhwb3NlOlxuICAgICAgLSA4MDkwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gdXBzbmFwLWRhdGE6L2FwcC9wYl9kYXRhXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFRaPSR7VFp9XG4gICAgICAtIFVQU05BUF9JTlRFUlZBTD0ke1VQU05BUF9JTlRFUlZBTH1cbiAgICAgIC0gVVBTTkFQX1NDQU5fUkFOR0U9JHtVUFNOQVBfU0NBTl9SQU5HRX1cbiAgICAgIC0gVVBTTkFQX1NDQU5fVElNRU9VVD0ke1VQU05BUF9TQ0FOX1RJTUVPVVR9XG4gICAgICAtIFVQU05BUF9QSU5HX1BSSVZJTEVHRUQ9JHtVUFNOQVBfUElOR19QUklWSUxFR0VEfVxuICAgICAgLSBVUFNOQVBfV0VCU0lURV9USVRMRT0ke1VQU05BUF9XRUJTSVRFX1RJVExFfVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwiY3VybFwiLCBcIi1mc1wiLCBcImh0dHA6Ly9sb2NhbGhvc3Q6ODA5MC9hcGkvaGVhbHRoXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiAzc1xuICAgICAgcmV0cmllczogM1xuXG52b2x1bWVzOlxuICB1cHNuYXAtZGF0YTpcbiAgICBkcml2ZXI6IGxvY2FsXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxudXBzbmFwX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInVwc25hcFwiXG5wb3J0ID0gODA5MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxucGF0aCA9IFwiL1wiXG5cbltjb25maWcuZW52XVxuVFogPSBcIkV1cm9wZS9CZXJsaW5cIlxuVVBTTkFQX0lOVEVSVkFMID0gXCIqLzEwICogKiAqICogKlwiXG5VUFNOQVBfU0NBTl9SQU5HRSA9IFwiMTkyLjE2OC4xLjAvMjRcIlxuVVBTTkFQX1NDQU5fVElNRU9VVCA9IFwiNTAwbXNcIlxuVVBTTkFQX1BJTkdfUFJJVklMRUdFRCA9IFwidHJ1ZVwiXG5VUFNOQVBfV0VCU0lURV9USVRMRSA9IFwiVXBzbmFwIE5ldHdvcmsgTW9uaXRvclwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zb3VyY2UgPSBcInVwc25hcC1kYXRhXCJcbnRhcmdldCA9IFwiL2FwcC9wYl9kYXRhXCJcbiIKfQ==
```

## Links

`network`,`monitoring`,`dashboard`,`self-hosted`

---

Version:`5`

UnleashOpen-source feature management platform

Uptime KumaUptime Kuma is a free and open source monitoring tool that allows you to monitor your websites and applications.

### On this page

ConfigurationBase64LinksTags