---
title: "Plausible | Dokploy"
source: "https://docs.dokploy.com/docs/templates/plausible"
category: dokploy-docs
created: "2026-06-25T17:21:56.647Z"
---

Plausible | Dokploy

# Plausible

Copy as Markdown

Plausible is a open source, self-hosted web analytics platform that lets you track website traffic and user behavior.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  plausible_db:
    image: postgres:16-alpine
    restart: always

    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=postgres

  plausible_events_db:
    image: clickhouse/clickhouse-server:24.3.3.102-alpine
    restart: always

    volumes:
      - event-data:/var/lib/clickhouse
      - event-logs:/var/log/clickhouse-server
      - ../files/clickhouse/clickhouse-config.xml:/etc/clickhouse-server/config.d/logging.xml:ro
      - ../files/clickhouse/clickhouse-user-config.xml:/etc/clickhouse-server/users.d/logging.xml:ro
    ulimits:
      nofile:
        soft: 262144
        hard: 262144

  plausible:
    image: ghcr.io/plausible/community-edition:v2.1.5
    restart: always
    command: sh -c "sleep 10 && /entrypoint.sh db createdb && /entrypoint.sh db migrate && /entrypoint.sh run"
    depends_on:
      - plausible_db
      - plausible_events_db
    env_file:
      - .env

volumes:
  db-data:
    driver: local
  event-data:
    driver: local
  event-logs:
    driver: local
```

```
[variables]
main_domain = "${domain}"
secret_base = "${base64:64}"
totp_key = "${base64:32}"

[[config.domains]]
serviceName = "plausible"
port = 8_000
host = "${main_domain}"

[config.env]
BASE_URL = "http://${main_domain}"
SECRET_KEY_BASE = "${secret_base}"
TOTP_VAULT_KEY = "${totp_key}"

[[config.mounts]]
filePath = "/clickhouse/clickhouse-config.xml"
content = """
<clickhouse>
  <logger>
    <level>warning</level>
    <console>true</console>
  </logger>

  <!-- Stop all the unnecessary logging -->
  <query_thread_log remove="remove"/>
  <query_log remove="remove"/>
  <text_log remove="remove"/>
  <trace_log remove="remove"/>
  <metric_log remove="remove"/>
  <asynchronous_metric_log remove="remove"/>
  <session_log remove="remove"/>
  <part_log remove="remove"/>
</clickhouse>
"""

[[config.mounts]]
filePath = "/clickhouse/clickhouse-user-config.xml"
content = """
<clickhouse>
  <profiles>
    <default>
      <log_queries>0</log_queries>
      <log_query_threads>0</log_query_threads>
    </default>
  </profiles>
</clickhouse>
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwbGF1c2libGVfZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE2LWFscGluZVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGItZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkQ9cG9zdGdyZXNcblxuICBwbGF1c2libGVfZXZlbnRzX2RiOlxuICAgIGltYWdlOiBjbGlja2hvdXNlL2NsaWNraG91c2Utc2VydmVyOjI0LjMuMy4xMDItYWxwaW5lXG4gICAgcmVzdGFydDogYWx3YXlzXG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSBldmVudC1kYXRhOi92YXIvbGliL2NsaWNraG91c2VcbiAgICAgIC0gZXZlbnQtbG9nczovdmFyL2xvZy9jbGlja2hvdXNlLXNlcnZlclxuICAgICAgLSAuLi9maWxlcy9jbGlja2hvdXNlL2NsaWNraG91c2UtY29uZmlnLnhtbDovZXRjL2NsaWNraG91c2Utc2VydmVyL2NvbmZpZy5kL2xvZ2dpbmcueG1sOnJvXG4gICAgICAtIC4uL2ZpbGVzL2NsaWNraG91c2UvY2xpY2tob3VzZS11c2VyLWNvbmZpZy54bWw6L2V0Yy9jbGlja2hvdXNlLXNlcnZlci91c2Vycy5kL2xvZ2dpbmcueG1sOnJvXG4gICAgdWxpbWl0czpcbiAgICAgIG5vZmlsZTpcbiAgICAgICAgc29mdDogMjYyMTQ0XG4gICAgICAgIGhhcmQ6IDI2MjE0NFxuXG4gIHBsYXVzaWJsZTpcbiAgICBpbWFnZTogZ2hjci5pby9wbGF1c2libGUvY29tbXVuaXR5LWVkaXRpb246djIuMS41XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgY29tbWFuZDogc2ggLWMgXCJzbGVlcCAxMCAmJiAvZW50cnlwb2ludC5zaCBkYiBjcmVhdGVkYiAmJiAvZW50cnlwb2ludC5zaCBkYiBtaWdyYXRlICYmIC9lbnRyeXBvaW50LnNoIHJ1blwiXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcGxhdXNpYmxlX2RiXG4gICAgICAtIHBsYXVzaWJsZV9ldmVudHNfZGJcbiAgICBlbnZfZmlsZTpcbiAgICAgIC0gLmVudlxuXG52b2x1bWVzOlxuICBkYi1kYXRhOlxuICAgIGRyaXZlcjogbG9jYWxcbiAgZXZlbnQtZGF0YTpcbiAgICBkcml2ZXI6IGxvY2FsXG4gIGV2ZW50LWxvZ3M6XG4gICAgZHJpdmVyOiBsb2NhbFxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnNlY3JldF9iYXNlID0gXCIke2Jhc2U2NDo2NH1cIlxudG90cF9rZXkgPSBcIiR7YmFzZTY0OjMyfVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInBsYXVzaWJsZVwiXG5wb3J0ID0gOF8wMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5CQVNFX1VSTCA9IFwiaHR0cDovLyR7bWFpbl9kb21haW59XCJcblNFQ1JFVF9LRVlfQkFTRSA9IFwiJHtzZWNyZXRfYmFzZX1cIlxuVE9UUF9WQVVMVF9LRVkgPSBcIiR7dG90cF9rZXl9XCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvY2xpY2tob3VzZS9jbGlja2hvdXNlLWNvbmZpZy54bWxcIlxuY29udGVudCA9IFwiXCJcIlxuPGNsaWNraG91c2U+XG4gIDxsb2dnZXI+XG4gICAgPGxldmVsPndhcm5pbmc8L2xldmVsPlxuICAgIDxjb25zb2xlPnRydWU8L2NvbnNvbGU+XG4gIDwvbG9nZ2VyPlxuXG4gIDwhLS0gU3RvcCBhbGwgdGhlIHVubmVjZXNzYXJ5IGxvZ2dpbmcgLS0+XG4gIDxxdWVyeV90aHJlYWRfbG9nIHJlbW92ZT1cInJlbW92ZVwiLz5cbiAgPHF1ZXJ5X2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gIDx0ZXh0X2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gIDx0cmFjZV9sb2cgcmVtb3ZlPVwicmVtb3ZlXCIvPlxuICA8bWV0cmljX2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gIDxhc3luY2hyb25vdXNfbWV0cmljX2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gIDxzZXNzaW9uX2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gIDxwYXJ0X2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG48L2NsaWNraG91c2U+XG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvY2xpY2tob3VzZS9jbGlja2hvdXNlLXVzZXItY29uZmlnLnhtbFwiXG5jb250ZW50ID0gXCJcIlwiXG48Y2xpY2tob3VzZT5cbiAgPHByb2ZpbGVzPlxuICAgIDxkZWZhdWx0PlxuICAgICAgPGxvZ19xdWVyaWVzPjA8L2xvZ19xdWVyaWVzPlxuICAgICAgPGxvZ19xdWVyeV90aHJlYWRzPjA8L2xvZ19xdWVyeV90aHJlYWRzPlxuICAgIDwvZGVmYXVsdD5cbiAgPC9wcm9maWxlcz5cbjwvY2xpY2tob3VzZT5cblwiXCJcIlxuIgp9
```

## Links

`analytics`

---

Version:`v2.1.5`

PlunkPlunk is the open-source, affordable email platform that brings together marketing, transactional and broadcast emails into one single, complete solution

### On this page

ConfigurationBase64LinksTags