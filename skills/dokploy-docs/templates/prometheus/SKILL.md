---
title: "Prometheus | Dokploy"
source: "https://docs.dokploy.com/docs/templates/prometheus"
category: dokploy-docs
created: "2026-06-25T17:21:57.937Z"
---

Prometheus | Dokploy

# Prometheus

Copy as Markdown

Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  prometheus:
    image: prom/prometheus:latest
    restart: unless-stopped
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
      - "--storage.tsdb.path=/prometheus"
      - "--web.console.libraries=/usr/share/prometheus/console_libraries"
      - "--web.console.templates=/usr/share/prometheus/consoles"
      - "--web.enable-lifecycle"
    volumes:
      - ../files/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus-data:/prometheus
volumes:
  prometheus-data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
env = []

[[config.domains]]
serviceName = "prometheus"
port = 9_090
host = "${main_domain}"

[[config.mounts]]
# Note: this relative path is resolved by Dokploy to the file mounted from
# ../files/prometheus.yml in docker-compose, and mapped inside the container
# to /etc/prometheus/prometheus.yml.
filePath = "prometheus.yml"
serviceName = "prometheus"
content = """
# Prometheus Configuration
# https://prometheus.io/docs/prometheus/latest/configuration/configuration/

global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    monitor: 'dokploy-prometheus'

# Alertmanager configuration (optional)
# alerting:
#   alertmanagers:
#     - static_configs:
#         - targets:
#           - 'alertmanager:9093'

# Load rules once and periodically evaluate them
# rule_files:
#   - "alerts.yml"

# Scrape configurations
scrape_configs:
  # Prometheus self-monitoring
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # Example: Add your own targets here
  # - job_name: 'node_exporter'
  #   static_configs:
  #     - targets: ['node-exporter:9100']

  # - job_name: 'docker'
  #   static_configs:
  #     - targets: ['docker-host:9323']
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwcm9tZXRoZXVzOlxuICAgIGltYWdlOiBwcm9tL3Byb21ldGhldXM6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBjb21tYW5kOlxuICAgICAgLSBcIi0tY29uZmlnLmZpbGU9L2V0Yy9wcm9tZXRoZXVzL3Byb21ldGhldXMueW1sXCJcbiAgICAgIC0gXCItLXN0b3JhZ2UudHNkYi5wYXRoPS9wcm9tZXRoZXVzXCJcbiAgICAgIC0gXCItLXdlYi5jb25zb2xlLmxpYnJhcmllcz0vdXNyL3NoYXJlL3Byb21ldGhldXMvY29uc29sZV9saWJyYXJpZXNcIlxuICAgICAgLSBcIi0td2ViLmNvbnNvbGUudGVtcGxhdGVzPS91c3Ivc2hhcmUvcHJvbWV0aGV1cy9jb25zb2xlc1wiXG4gICAgICAtIFwiLS13ZWIuZW5hYmxlLWxpZmVjeWNsZVwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvcHJvbWV0aGV1cy55bWw6L2V0Yy9wcm9tZXRoZXVzL3Byb21ldGhldXMueW1sXG4gICAgICAtIHByb21ldGhldXMtZGF0YTovcHJvbWV0aGV1c1xudm9sdW1lczpcbiAgcHJvbWV0aGV1cy1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInByb21ldGhldXNcIlxucG9ydCA9IDlfMDkwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltbY29uZmlnLm1vdW50c11dXG4jIE5vdGU6IHRoaXMgcmVsYXRpdmUgcGF0aCBpcyByZXNvbHZlZCBieSBEb2twbG95IHRvIHRoZSBmaWxlIG1vdW50ZWQgZnJvbVxuIyAuLi9maWxlcy9wcm9tZXRoZXVzLnltbCBpbiBkb2NrZXItY29tcG9zZSwgYW5kIG1hcHBlZCBpbnNpZGUgdGhlIGNvbnRhaW5lclxuIyB0byAvZXRjL3Byb21ldGhldXMvcHJvbWV0aGV1cy55bWwuXG5maWxlUGF0aCA9IFwicHJvbWV0aGV1cy55bWxcIlxuc2VydmljZU5hbWUgPSBcInByb21ldGhldXNcIlxuY29udGVudCA9IFwiXCJcIlxuIyBQcm9tZXRoZXVzIENvbmZpZ3VyYXRpb25cbiMgaHR0cHM6Ly9wcm9tZXRoZXVzLmlvL2RvY3MvcHJvbWV0aGV1cy9sYXRlc3QvY29uZmlndXJhdGlvbi9jb25maWd1cmF0aW9uL1xuXG5nbG9iYWw6XG4gIHNjcmFwZV9pbnRlcnZhbDogMTVzXG4gIGV2YWx1YXRpb25faW50ZXJ2YWw6IDE1c1xuICBleHRlcm5hbF9sYWJlbHM6XG4gICAgbW9uaXRvcjogJ2Rva3Bsb3ktcHJvbWV0aGV1cydcblxuIyBBbGVydG1hbmFnZXIgY29uZmlndXJhdGlvbiAob3B0aW9uYWwpXG4jIGFsZXJ0aW5nOlxuIyAgIGFsZXJ0bWFuYWdlcnM6XG4jICAgICAtIHN0YXRpY19jb25maWdzOlxuIyAgICAgICAgIC0gdGFyZ2V0czpcbiMgICAgICAgICAgIC0gJ2FsZXJ0bWFuYWdlcjo5MDkzJ1xuXG4jIExvYWQgcnVsZXMgb25jZSBhbmQgcGVyaW9kaWNhbGx5IGV2YWx1YXRlIHRoZW1cbiMgcnVsZV9maWxlczpcbiMgICAtIFwiYWxlcnRzLnltbFwiXG5cbiMgU2NyYXBlIGNvbmZpZ3VyYXRpb25zXG5zY3JhcGVfY29uZmlnczpcbiAgIyBQcm9tZXRoZXVzIHNlbGYtbW9uaXRvcmluZ1xuICAtIGpvYl9uYW1lOiAncHJvbWV0aGV1cydcbiAgICBzdGF0aWNfY29uZmlnczpcbiAgICAgIC0gdGFyZ2V0czogWydsb2NhbGhvc3Q6OTA5MCddXG5cbiAgIyBFeGFtcGxlOiBBZGQgeW91ciBvd24gdGFyZ2V0cyBoZXJlXG4gICMgLSBqb2JfbmFtZTogJ25vZGVfZXhwb3J0ZXInXG4gICMgICBzdGF0aWNfY29uZmlnczpcbiAgIyAgICAgLSB0YXJnZXRzOiBbJ25vZGUtZXhwb3J0ZXI6OTEwMCddXG4gIFxuICAjIC0gam9iX25hbWU6ICdkb2NrZXInXG4gICMgICBzdGF0aWNfY29uZmlnczpcbiAgIyAgICAgLSB0YXJnZXRzOiBbJ2RvY2tlci1ob3N0OjkzMjMnXVxuXCJcIlwiXG5cbiIKfQ==
```

## Links

`monitoring`,`alerting`,`metrics`

---

Version:`latest`

SupaBaseThe open source Firebase alternative. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications. This is for dokploy version < 0.22.5.

PterodactylA free, open-source game server management panel.

### On this page

ConfigurationBase64LinksTags