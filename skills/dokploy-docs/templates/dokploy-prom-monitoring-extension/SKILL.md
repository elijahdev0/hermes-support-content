---
title: "Dokploy Prometheus Monitoring Extension | Dokploy"
source: "https://docs.dokploy.com/docs/templates/dokploy-prom-monitoring-extension"
category: dokploy-docs
created: "2026-06-25T17:21:46.245Z"
---

Dokploy Prometheus Monitoring Extension | Dokploy

# Dokploy Prometheus Monitoring Extension

Copy as Markdown

Dokploy monitoring extension with Prometheus metrics export for external monitoring systems like Grafana Cloud. Tracks server and container metrics with configurable thresholds and alerting.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  dokploy-monitoring:
    image: dokploy/monitoring:canary
    restart: unless-stopped
    env_file:
      - .env
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - monitoring-data:/app/data
volumes:
  monitoring-data: {}
```

```
[variables]
main_domain = "${domain}"
monitoring_token = "${password:32}"
callback_url = "http://dokploy:3000/api/trpc/notification.receiveNotification"
server_type = "Dokploy"
refresh_rate = "30"
retention_days = "7"
cpu_threshold = "80"
memory_threshold = "85"

[[config.domains]]
serviceName = "dokploy-monitoring"
port = 3001
host = "${main_domain}"

[config.env]
METRICS_CONFIG = "{\"server\":{\"refreshRate\":${refresh_rate},\"port\":3001,\"type\":\"${server_type}\",\"token\":\"${monitoring_token}\",\"urlCallback\":\"${callback_url}\",\"retentionDays\":${retention_days},\"cronJob\":\"0 0 * * *\",\"thresholds\":{\"cpu\":${cpu_threshold},\"memory\":${memory_threshold}},\"prometheus\":{\"enabled\":true}},\"containers\":{\"refreshRate\":${refresh_rate},\"services\":{\"include\":[],\"exclude\":[]}}}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkb2twbG95LW1vbml0b3Jpbmc6XG4gICAgaW1hZ2U6IGRva3Bsb3kvbW9uaXRvcmluZzpjYW5hcnlcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudl9maWxlOlxuICAgICAgLSAuZW52XG4gICAgdm9sdW1lczpcbiAgICAgIC0gL3Zhci9ydW4vZG9ja2VyLnNvY2s6L3Zhci9ydW4vZG9ja2VyLnNvY2s6cm9cbiAgICAgIC0gbW9uaXRvcmluZy1kYXRhOi9hcHAvZGF0YVxudm9sdW1lczpcbiAgbW9uaXRvcmluZy1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbm1vbml0b3JpbmdfdG9rZW4gPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmNhbGxiYWNrX3VybCA9IFwiaHR0cDovL2Rva3Bsb3k6MzAwMC9hcGkvdHJwYy9ub3RpZmljYXRpb24ucmVjZWl2ZU5vdGlmaWNhdGlvblwiXG5zZXJ2ZXJfdHlwZSA9IFwiRG9rcGxveVwiXG5yZWZyZXNoX3JhdGUgPSBcIjMwXCJcbnJldGVudGlvbl9kYXlzID0gXCI3XCJcbmNwdV90aHJlc2hvbGQgPSBcIjgwXCJcbm1lbW9yeV90aHJlc2hvbGQgPSBcIjg1XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZG9rcGxveS1tb25pdG9yaW5nXCJcbnBvcnQgPSAzMDAxXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuTUVUUklDU19DT05GSUcgPSBcIntcXFwic2VydmVyXFxcIjp7XFxcInJlZnJlc2hSYXRlXFxcIjoke3JlZnJlc2hfcmF0ZX0sXFxcInBvcnRcXFwiOjMwMDEsXFxcInR5cGVcXFwiOlxcXCIke3NlcnZlcl90eXBlfVxcXCIsXFxcInRva2VuXFxcIjpcXFwiJHttb25pdG9yaW5nX3Rva2VufVxcXCIsXFxcInVybENhbGxiYWNrXFxcIjpcXFwiJHtjYWxsYmFja191cmx9XFxcIixcXFwicmV0ZW50aW9uRGF5c1xcXCI6JHtyZXRlbnRpb25fZGF5c30sXFxcImNyb25Kb2JcXFwiOlxcXCIwIDAgKiAqICpcXFwiLFxcXCJ0aHJlc2hvbGRzXFxcIjp7XFxcImNwdVxcXCI6JHtjcHVfdGhyZXNob2xkfSxcXFwibWVtb3J5XFxcIjoke21lbW9yeV90aHJlc2hvbGR9fSxcXFwicHJvbWV0aGV1c1xcXCI6e1xcXCJlbmFibGVkXFxcIjp0cnVlfX0sXFxcImNvbnRhaW5lcnNcXFwiOntcXFwicmVmcmVzaFJhdGVcXFwiOiR7cmVmcmVzaF9yYXRlfSxcXFwic2VydmljZXNcXFwiOntcXFwiaW5jbHVkZVxcXCI6W10sXFxcImV4Y2x1ZGVcXFwiOltdfX19XCJcbiIKfQ==
```

## Links

`monitoring`,`prometheus`,`metrics`,`observability`,`docker`,`grafana`

---

Version:`canary`

DocusealDocuseal is a self-hosted document management system.

DolibarrDolibarr ERP & CRM is a modern software package that helps manage your organization's activities (contacts, quotes, invoices, orders, stocks, agenda, human resources, ecm, manufacturing).

### On this page

ConfigurationBase64LinksTags