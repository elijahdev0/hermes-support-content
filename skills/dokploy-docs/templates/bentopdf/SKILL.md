---
title: "BentoPDF | Dokploy"
source: "https://docs.dokploy.com/docs/templates/bentopdf"
category: dokploy-docs
created: "2026-06-25T17:21:41.530Z"
---

BentoPDF | Dokploy

# BentoPDF

Copy as Markdown

BentoPDF is a lightweight PDF conversion microservice that exposes a simple HTTP API for generating PDFs.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  bentopdf:
    image: bentopdf/bentopdf:latest
    restart: unless-stopped
    expose:
      - 80
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "bentopdf"
port = 80
host = "${main_domain}"
path = "/"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGJlbnRvcGRmOlxuICAgIGltYWdlOiBiZW50b3BkZi9iZW50b3BkZjpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGV4cG9zZTpcbiAgICAgIC0gODBcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJiZW50b3BkZlwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbnBhdGggPSBcIi9cIlxuIgp9
```

## Links

`pdf`,`converter`,`api`,`utility`

---

Version:`latest`

BazarrBazarr is a companion application to Sonarr and Radarr that manages and downloads subtitles based on your requirements.

BeszelA lightweight server monitoring hub with historical data, docker stats, and alerts.

### On this page

ConfigurationBase64LinksTags