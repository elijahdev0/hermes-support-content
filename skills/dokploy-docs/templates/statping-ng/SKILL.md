---
title: "Statping-NG | Dokploy"
source: "https://docs.dokploy.com/docs/templates/statping-ng"
category: dokploy-docs
created: "2026-06-25T17:21:59.115Z"
---

Statping-NG | Dokploy

# Statping-NG

Copy as Markdown

Statping-NG is an easy-to-use status page for monitoring websites and applications with beautiful metrics, analytics, and health checks.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  statping-ng:
    image: adamboutcher/statping-ng:latest
    restart: unless-stopped
    environment:
      - TZ=${TZ}
      - DB_CONN=sqlite
    volumes:
      - ../files/statping-ng:/app
    ports:
      - 8080
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "statping-ng"
port = 8080
host = "${main_domain}"

[config.env]
TZ = "UTC"
DB_CONN = "sqlite"

[[config.mounts]]
source = "../files/statping-ng"
target = "/app"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBzdGF0cGluZy1uZzpcbiAgICBpbWFnZTogYWRhbWJvdXRjaGVyL3N0YXRwaW5nLW5nOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFRaPSR7VFp9XG4gICAgICAtIERCX0NPTk49c3FsaXRlXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvc3RhdHBpbmctbmc6L2FwcFxuICAgIHBvcnRzOlxuICAgICAgLSA4MDgwXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwic3RhdHBpbmctbmdcIlxucG9ydCA9IDgwODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5UWiA9IFwiVVRDXCJcbkRCX0NPTk4gPSBcInNxbGl0ZVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zb3VyY2UgPSBcIi4uL2ZpbGVzL3N0YXRwaW5nLW5nXCJcbnRhcmdldCA9IFwiL2FwcFwiIgp9
```

## Links

`monitoring`,`status-page`

---

Version:`latest`

StalwartStalwart Mail Server is an open-source mail server solution with JMAP, IMAP4, POP3, and SMTP support and a wide range of modern features. It is written in Rust and designed to be secure, fast, robust and scalable.

Stirling PDFA locally hosted one-stop shop for all your PDF needs

### On this page

ConfigurationBase64LinksTags