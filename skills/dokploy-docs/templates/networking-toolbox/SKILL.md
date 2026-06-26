---
title: "Networking Toolbox | Dokploy"
source: "https://docs.dokploy.com/docs/templates/networking-toolbox"
category: dokploy-docs
created: "2026-06-25T17:21:54.354Z"
---

Networking Toolbox | Dokploy

# Networking Toolbox

Copy as Markdown

A collection of handy networking utilities by Lissy93, packaged as a self-hostable web app.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  app:
    image: lissy93/networking-toolbox:latest
    expose:
      - "3000"
    environment:
      NODE_ENV: ${NODE_ENV}
      PORT: ${PORT}
      HOST: ${HOST}
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://127.0.0.1:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

```
[variables]
main_domain = "${domain}"

[config]

[[config.domains]]
serviceName = "app"
port = 3000
host = "${main_domain}"

[config.env]
NODE_ENV = "production"
PORT = "3000"
HOST = "0.0.0.0"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGFwcDpcbiAgICBpbWFnZTogbGlzc3k5My9uZXR3b3JraW5nLXRvb2xib3g6bGF0ZXN0XG4gICAgZXhwb3NlOlxuICAgICAgLSBcIjMwMDBcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgTk9ERV9FTlY6ICR7Tk9ERV9FTlZ9XG4gICAgICBQT1JUOiAke1BPUlR9XG4gICAgICBIT1NUOiAke0hPU1R9XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcIndnZXRcIiwgXCItcU8tXCIsIFwiaHR0cDovLzEyNy4wLjAuMTozMDAwL2hlYWx0aFwiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG4gICAgICBzdGFydF9wZXJpb2Q6IDQwc1xuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYXBwXCJcbnBvcnQgPSAzMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuTk9ERV9FTlYgPSBcInByb2R1Y3Rpb25cIlxuUE9SVCA9IFwiMzAwMFwiXG5IT1NUID0gXCIwLjAuMC4wXCJcbiIKfQ==
```

## Links

`networking`,`tools`,`utilities`,`web`

---

Version:`latest`

NetdataNetdata is a real-time performance monitoring tool that provides comprehensive system metrics, application monitoring, and infrastructure health insights.

NextcloudNextcloud is a self-hosted file storage and sync platform with powerful collaboration capabilities. It integrates Files, Talk, Groupware, Office, Assistant and more into a single platform for remote work and data protection.

### On this page

ConfigurationBase64LinksTags