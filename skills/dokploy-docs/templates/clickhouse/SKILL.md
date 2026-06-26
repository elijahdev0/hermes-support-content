---
title: "ClickHouse | Dokploy"
source: "https://docs.dokploy.com/docs/templates/clickhouse"
category: dokploy-docs
created: "2026-06-25T17:21:43.965Z"
---

ClickHouse | Dokploy

# ClickHouse

Copy as Markdown

ClickHouse is an open-source column-oriented DBMS (columnar database management system) for online analytical processing (OLAP) that allows users to generate analytical reports using SQL queries in real-time. ClickHouse works 100-1000x faster than traditional database management systems, and processes hundreds of millions to over a billion rows and tens of gigabytes of data per server per second.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  clickhouse:
    image: clickhouse/clickhouse-server:latest
    restart: unless-stopped
    environment:
      - CLICKHOUSE_USER=${CLICKHOUSE_USER}
      - CLICKHOUSE_PASSWORD=${CLICKHOUSE_PASSWORD}
    volumes:
      - clickhouse-data:/var/lib/clickhouse
      - clickhouse-logs:/var/log/clickhouse-server

volumes:
  clickhouse-data:
  clickhouse-logs:
```

```
[variables]
main_domain = "${domain}"
clickhouse_user = "default"
clickhouse_password = "${password:32}"

[config]
mounts = []

[[config.domains]]
serviceName = "clickhouse"
port = 8123
host = "${main_domain}"

[config.env]
CLICKHOUSE_USER = "${clickhouse_user}"
CLICKHOUSE_PASSWORD = "${clickhouse_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBjbGlja2hvdXNlOlxuICAgIGltYWdlOiBjbGlja2hvdXNlL2NsaWNraG91c2Utc2VydmVyOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIENMSUNLSE9VU0VfVVNFUj0ke0NMSUNLSE9VU0VfVVNFUn1cbiAgICAgIC0gQ0xJQ0tIT1VTRV9QQVNTV09SRD0ke0NMSUNLSE9VU0VfUEFTU1dPUkR9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gY2xpY2tob3VzZS1kYXRhOi92YXIvbGliL2NsaWNraG91c2VcbiAgICAgIC0gY2xpY2tob3VzZS1sb2dzOi92YXIvbG9nL2NsaWNraG91c2Utc2VydmVyXG5cbnZvbHVtZXM6XG4gIGNsaWNraG91c2UtZGF0YTpcbiAgY2xpY2tob3VzZS1sb2dzOlxuXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuY2xpY2tob3VzZV91c2VyID0gXCJkZWZhdWx0XCJcbmNsaWNraG91c2VfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImNsaWNraG91c2VcIlxucG9ydCA9IDgxMjNcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5DTElDS0hPVVNFX1VTRVIgPSBcIiR7Y2xpY2tob3VzZV91c2VyfVwiXG5DTElDS0hPVVNFX1BBU1NXT1JEID0gXCIke2NsaWNraG91c2VfcGFzc3dvcmR9XCJcblxuIgp9
```

## Links

`self-hosted`,`open-source`,`database`,`olap`,`analytics`

---

Version:`latest`

ClassicPressClassicPress is a community-led open source content management system for creators. It is a fork of WordPress 6.2 that preserves the TinyMCE classic editor as the default option.

Cloud9Cloud9 is a cloud-based integrated development environment (IDE) designed for developers to code, build, and debug applications collaboratively in real time.

### On this page

ConfigurationBase64LinksTags