---
title: "Grist | Dokploy"
source: "https://docs.dokploy.com/docs/templates/grist"
category: dokploy-docs
created: "2026-06-25T17:21:49.750Z"
---

Grist | Dokploy

# Grist

Copy as Markdown

Grist is an open-source spreadsheet and database alternative that combines the flexibility of spreadsheets with the power of databases.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  grist:
    image: gristlabs/grist:latest
    restart: unless-stopped
    ports:
      - 8484
    volumes:
      - grist_data:/persist
    environment:
      GRIST_DEFAULT_EMAIL: ${GRIST_DEFAULT_EMAIL:-}
      GRIST_SESSION_SECRET: ${GRIST_SESSION_SECRET:-}
      GRIST_SINGLE_ORG: ${GRIST_SINGLE_ORG:-}
      GRIST_HOME_INSTANCE: ${GRIST_HOME_INSTANCE:-}

volumes:
  grist_data:
```

```
[variables]
main_domain = "${domain}"
default_email = "${email}"

[config]
[[config.domains]]
serviceName = "grist"
port = 8484
host = "${main_domain}"

[config.env]
GRIST_DEFAULT_EMAIL = "${default_email}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBncmlzdDpcbiAgICBpbWFnZTogZ3Jpc3RsYWJzL2dyaXN0OmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDg0ODRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBncmlzdF9kYXRhOi9wZXJzaXN0XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBHUklTVF9ERUZBVUxUX0VNQUlMOiAke0dSSVNUX0RFRkFVTFRfRU1BSUw6LX1cbiAgICAgIEdSSVNUX1NFU1NJT05fU0VDUkVUOiAke0dSSVNUX1NFU1NJT05fU0VDUkVUOi19XG4gICAgICBHUklTVF9TSU5HTEVfT1JHOiAke0dSSVNUX1NJTkdMRV9PUkc6LX1cbiAgICAgIEdSSVNUX0hPTUVfSU5TVEFOQ0U6ICR7R1JJU1RfSE9NRV9JTlNUQU5DRTotfVxuXG52b2x1bWVzOlxuICBncmlzdF9kYXRhOlxuXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGVmYXVsdF9lbWFpbCA9IFwiJHtlbWFpbH1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZ3Jpc3RcIlxucG9ydCA9IDg0ODRcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5HUklTVF9ERUZBVUxUX0VNQUlMID0gXCIke2RlZmF1bHRfZW1haWx9XCJcblxuW1tjb25maWcubW91bnRzXV1cblxuIgp9
```

## Links

`spreadsheet`,`database`,`productivity`,`self-hosted`,`data-management`

---

Version:`latest`

GrimoireGrimoire is a self-hosted bookmarking app designed for speed and simplicity.

HabiticaHabitica is a free habit and productivity app that treats your real life like a game. With in-game rewards and punishments to motivate you and a strong social network to inspire you, Habitica can help you achieve your goals to become healthy and hard-working.

### On this page

ConfigurationBase64LinksTags