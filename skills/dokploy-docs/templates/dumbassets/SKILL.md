---
title: "DumbAssets | Dokploy"
source: "https://docs.dokploy.com/docs/templates/dumbassets"
category: dokploy-docs
created: "2026-06-25T17:21:46.246Z"
---

DumbAssets | Dokploy

# DumbAssets

Copy as Markdown

DumbAssets is a simple, self-hosted asset tracking service with no database or authentication required.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  dumbassets:
    image: dumbwareio/dumbassets:latest
    restart: unless-stopped
    ports:
      - 3000
    volumes:
      - dumbassets-data:/app/data

volumes:
  dumbassets-data: {}
```

```
[variables]
main_domain = "${domain}"
default_pin = "${password:4}"

[config]
[[config.domains]]
serviceName = "dumbassets"
port = 3000
host = "${main_domain}"

[config.env]
NODE_ENV = "production"
DEBUG = "false"
SITE_TITLE = "DumbAssets"
BASE_URL = "https://${main_domain}"
DUMBASSETS_PIN = "${default_pin}"
ALLOWED_ORIGINS = "*"
DEMO_MODE = "false"
APPRISE_URL = ""
CURRENCY_CODE = "USD"
CURRENCY_LOCALE = "en-US"

[[config.mounts]]
serviceName = "dumbassets"
type = "volume"
source = "dumbassets-data"
target = "/app/data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBkdW1iYXNzZXRzOlxuICAgIGltYWdlOiBkdW1id2FyZWlvL2R1bWJhc3NldHM6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gMzAwMFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGR1bWJhc3NldHMtZGF0YTovYXBwL2RhdGFcblxudm9sdW1lczpcbiAgZHVtYmFzc2V0cy1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRlZmF1bHRfcGluID0gXCIke3Bhc3N3b3JkOjR9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImR1bWJhc3NldHNcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5OT0RFX0VOViA9IFwicHJvZHVjdGlvblwiXG5ERUJVRyA9IFwiZmFsc2VcIlxuU0lURV9USVRMRSA9IFwiRHVtYkFzc2V0c1wiXG5CQVNFX1VSTCA9IFwiaHR0cHM6Ly8ke21haW5fZG9tYWlufVwiXG5EVU1CQVNTRVRTX1BJTiA9IFwiJHtkZWZhdWx0X3Bpbn1cIlxuQUxMT1dFRF9PUklHSU5TID0gXCIqXCJcbkRFTU9fTU9ERSA9IFwiZmFsc2VcIlxuQVBQUklTRV9VUkwgPSBcIlwiXG5DVVJSRU5DWV9DT0RFID0gXCJVU0RcIlxuQ1VSUkVOQ1lfTE9DQUxFID0gXCJlbi1VU1wiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwiZHVtYmFzc2V0c1wiXG50eXBlID0gXCJ2b2x1bWVcIlxuc291cmNlID0gXCJkdW1iYXNzZXRzLWRhdGFcIlxudGFyZ2V0ID0gXCIvYXBwL2RhdGFcIlxuIgp9
```

## Links

`asset-tracking`,`self-hosted`,`simple`

---

Version:`latest`

drizzle gatewayDrizzle Gateway is a self-hosted database gateway that allows you to connect to your databases from anywhere.

DumbBudgetDumbBudget is a simple, self-hosted budget tracking service with PIN protection and no database required.

### On this page

ConfigurationBase64LinksTags