---
title: "Beszel | Dokploy"
source: "https://docs.dokploy.com/docs/templates/beszel"
category: dokploy-docs
created: "2026-06-25T17:21:41.530Z"
---

Beszel | Dokploy

# Beszel

Copy as Markdown

A lightweight server monitoring hub with historical data, docker stats, and alerts.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  beszel:
    image: henrygd/beszel:0.10.2
    restart: unless-stopped
    ports:
      - 8090
    volumes:
      - beszel_data:/beszel_data
      - /var/run/docker.sock:/var/run/docker.sock:ro

volumes:
  beszel_data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "beszel"
port = 8090
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBiZXN6ZWw6XG4gICAgaW1hZ2U6IGhlbnJ5Z2QvYmVzemVsOjAuMTAuMlxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDgwOTBcbiAgICB2b2x1bWVzOlxuICAgICAgLSBiZXN6ZWxfZGF0YTovYmVzemVsX2RhdGFcbiAgICAgIC0gL3Zhci9ydW4vZG9ja2VyLnNvY2s6L3Zhci9ydW4vZG9ja2VyLnNvY2s6cm9cblxudm9sdW1lczpcbiAgYmVzemVsX2RhdGE6IHt9ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJiZXN6ZWxcIlxucG9ydCA9IDgwOTBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCIgIgp9
```

## Links

`monitoring`,`docker`,`alerts`

---

Version:`0.10.2`

BentoPDFBentoPDF is a lightweight PDF conversion microservice that exposes a simple HTTP API for generating PDFs.

BigCapitalBigCapital is a great open source alternative to QuickBooks. A comprehensive accounting and financial management system for businesses.

### On this page

ConfigurationBase64LinksTags