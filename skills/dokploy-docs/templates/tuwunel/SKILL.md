---
title: "Tuwunel | Dokploy"
source: "https://docs.dokploy.com/docs/templates/tuwunel"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

Tuwunel | Dokploy

# Tuwunel

Copy as Markdown

High performance Matrix homeserver written in Rust. Official successor to conduwuit - a scalable, low-cost, enterprise-ready alternative to Synapse.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  tuwunel:
    image: ghcr.io/matrix-construct/tuwunel:v1.5.0
    restart: always
    environment:
      - TUWUNEL_SERVER_NAME=${TUWUNEL_SERVER_NAME:-matrix.local}
      - TUWUNEL_ALLOW_REGISTRATION=${TUWUNEL_ALLOW_REGISTRATION:-false}
      - TUWUNEL_REGISTRATION_TOKEN=${TUWUNEL_REGISTRATION_TOKEN}
      - TUWUNEL_ADDRESS=${TUWUNEL_ADDRESS:-0.0.0.0}
      - TUWUNEL_PORT=${TUWUNEL_PORT:-6167}
    volumes:
      - tuwunel-data:/var/lib/tuwunel/
    expose:
      - 6167

volumes:
  tuwunel-data:
```

```
[variables]
main_domain = "${domain}"
registration_token = "${password:32}"

[config]
env = [
  "TUWUNEL_SERVER_NAME=${main_domain}",
  "TUWUNEL_REGISTRATION_TOKEN=${registration_token}"
]
mounts = []

[[config.domains]]
serviceName = "tuwunel"
port = 6167
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICB0dXd1bmVsOlxuICAgIGltYWdlOiBnaGNyLmlvL21hdHJpeC1jb25zdHJ1Y3QvdHV3dW5lbDp2MS41LjBcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gVFVXVU5FTF9TRVJWRVJfTkFNRT0ke1RVV1VORUxfU0VSVkVSX05BTUU6LW1hdHJpeC5sb2NhbH1cbiAgICAgIC0gVFVXVU5FTF9BTExPV19SRUdJU1RSQVRJT049JHtUVVdVTkVMX0FMTE9XX1JFR0lTVFJBVElPTjotZmFsc2V9XG4gICAgICAtIFRVV1VORUxfUkVHSVNUUkFUSU9OX1RPS0VOPSR7VFVXVU5FTF9SRUdJU1RSQVRJT05fVE9LRU59XG4gICAgICAtIFRVV1VORUxfQUREUkVTUz0ke1RVV1VORUxfQUREUkVTUzotMC4wLjAuMH1cbiAgICAgIC0gVFVXVU5FTF9QT1JUPSR7VFVXVU5FTF9QT1JUOi02MTY3fVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHR1d3VuZWwtZGF0YTovdmFyL2xpYi90dXd1bmVsL1xuICAgIGV4cG9zZTpcbiAgICAgIC0gNjE2N1xuXG52b2x1bWVzOlxuICB0dXd1bmVsLWRhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucmVnaXN0cmF0aW9uX3Rva2VuID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiVFVXVU5FTF9TRVJWRVJfTkFNRT0ke21haW5fZG9tYWlufVwiLFxuICBcIlRVV1VORUxfUkVHSVNUUkFUSU9OX1RPS0VOPSR7cmVnaXN0cmF0aW9uX3Rva2VufVwiXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ0dXd1bmVsXCJcbnBvcnQgPSA2MTY3XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`matrix`,`chat`,`messaging`,`rust`

---

Version:`v1.5.0`

TRMNL BYOS LaravelTRMNL BYOS Laravel is a self-hosted application to manage TRMNL e-ink devices.

Twenty CRMTwenty is a modern CRM offering a powerful spreadsheet interface and open-source alternative to Salesforce.

### On this page

ConfigurationBase64LinksTags