---
title: "DumbBudget | Dokploy"
source: "https://docs.dokploy.com/docs/templates/dumbbudget"
category: dokploy-docs
created: "2026-06-25T17:21:46.246Z"
---

DumbBudget | Dokploy

# DumbBudget

Copy as Markdown

DumbBudget is a simple, self-hosted budget tracking service with PIN protection and no database required.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  dumbbudget:
    image: dumbwareio/dumbbudget:latest
    restart: unless-stopped
    ports:
      - 3000
    volumes:
      - dumbbudget-data:/app/data

volumes:
  dumbbudget-data: {}
```

```
[variables]
main_domain = "${domain}"
# PIN used to access the site
dumbbudget_pin = "${password:16}"

[config]
[[config.domains]]
serviceName = "dumbbudget"
port = 3000
host = "${main_domain}"

[config.env]
DUMBBUDGET_PIN = "${dumbbudget_pin}"
BASE_URL = "${main_domain}"
CURRENCY = "USD"
SITE_TITLE = "DumbBudget"
INSTANCE_NAME = ""
# (OPTIONAL) Restrict origins - ex: https://subdomain.domain.tld
ALLOWED_ORIGINS = "${main_domain}"

# The named volume 'dumbbudget-data' is defined in the docker-compose.yml.
# According to Dokploy's template examples, volumes declared in the compose
# file are automatically managed and do not require a separate entry here.
[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBkdW1iYnVkZ2V0OlxuICAgIGltYWdlOiBkdW1id2FyZWlvL2R1bWJidWRnZXQ6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gMzAwMFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGR1bWJidWRnZXQtZGF0YTovYXBwL2RhdGFcblxudm9sdW1lczpcbiAgZHVtYmJ1ZGdldC1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbiMgUElOIHVzZWQgdG8gYWNjZXNzIHRoZSBzaXRlXG5kdW1iYnVkZ2V0X3BpbiA9IFwiJHtwYXNzd29yZDoxNn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZHVtYmJ1ZGdldFwiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkRVTUJCVURHRVRfUElOID0gXCIke2R1bWJidWRnZXRfcGlufVwiXG5CQVNFX1VSTCA9IFwiJHttYWluX2RvbWFpbn1cIlxuQ1VSUkVOQ1kgPSBcIlVTRFwiXG5TSVRFX1RJVExFID0gXCJEdW1iQnVkZ2V0XCJcbklOU1RBTkNFX05BTUUgPSBcIlwiXG4jIChPUFRJT05BTCkgUmVzdHJpY3Qgb3JpZ2lucyAtIGV4OiBodHRwczovL3N1YmRvbWFpbi5kb21haW4udGxkXG5BTExPV0VEX09SSUdJTlMgPSBcIiR7bWFpbl9kb21haW59XCJcblxuIyBUaGUgbmFtZWQgdm9sdW1lICdkdW1iYnVkZ2V0LWRhdGEnIGlzIGRlZmluZWQgaW4gdGhlIGRvY2tlci1jb21wb3NlLnltbC5cbiMgQWNjb3JkaW5nIHRvIERva3Bsb3kncyB0ZW1wbGF0ZSBleGFtcGxlcywgdm9sdW1lcyBkZWNsYXJlZCBpbiB0aGUgY29tcG9zZVxuIyBmaWxlIGFyZSBhdXRvbWF0aWNhbGx5IG1hbmFnZWQgYW5kIGRvIG5vdCByZXF1aXJlIGEgc2VwYXJhdGUgZW50cnkgaGVyZS5cbltbY29uZmlnLm1vdW50c11dXG4iCn0=
```

## Links

`budget`,`finance`,`self-hosted`,`simple`

---

Version:`latest`

DumbAssetsDumbAssets is a simple, self-hosted asset tracking service with no database or authentication required.

DumbDropDumbDrop is a simple, self-hosted file sharing service with no database or authentication required.

### On this page

ConfigurationBase64LinksTags