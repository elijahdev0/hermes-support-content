---
title: "DumbDrop | Dokploy"
source: "https://docs.dokploy.com/docs/templates/dumbdrop"
category: dokploy-docs
created: "2026-06-25T17:21:46.246Z"
---

DumbDrop | Dokploy

# DumbDrop

Copy as Markdown

DumbDrop is a simple, self-hosted file sharing service with no database or authentication required.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  dumbdrop:
    image: dumbwareio/dumbdrop:latest
    restart: unless-stopped
    ports:
      - 3000
    volumes:
      - dumbdrop-uploads:/app/uploads
volumes:
  dumbdrop-uploads: {}
```

```
[variables]
main_domain = "https://${domain}"

[config]
[[config.domains]]
serviceName = "dumbdrop"
port = 3000
host = "${domain}"

[config.env]
UPLOAD_DIR = "/app/uploads"
DUMBDROP_TITLE = "DumbDrop"
MAX_FILE_SIZE = "1024"
DUMBDROP_PIN = "${password:6}"
AUTO_UPLOAD = "true"
BASE_URL = "${main_domain}"
ALLOWED_ORIGINS = ""

APPRISE_URL = ""
APPRISE_MESSAGE = "New file uploaded {filename} ({size}), Storage used {storage}"
APPRISE_SIZE_UNIT = "Auto"
ALLOWED_EXTENSIONS = ""

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkdW1iZHJvcDpcbiAgICBpbWFnZTogZHVtYndhcmVpby9kdW1iZHJvcDpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSAzMDAwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZHVtYmRyb3AtdXBsb2FkczovYXBwL3VwbG9hZHNcbnZvbHVtZXM6XG4gIGR1bWJkcm9wLXVwbG9hZHM6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCJodHRwczovLyR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJkdW1iZHJvcFwiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5VUExPQURfRElSID0gXCIvYXBwL3VwbG9hZHNcIlxuRFVNQkRST1BfVElUTEUgPSBcIkR1bWJEcm9wXCJcbk1BWF9GSUxFX1NJWkUgPSBcIjEwMjRcIlxuRFVNQkRST1BfUElOID0gXCIke3Bhc3N3b3JkOjZ9XCJcbkFVVE9fVVBMT0FEID0gXCJ0cnVlXCJcbkJBU0VfVVJMID0gXCIke21haW5fZG9tYWlufVwiXG5BTExPV0VEX09SSUdJTlMgPSBcIlwiXG5cbkFQUFJJU0VfVVJMID0gXCJcIlxuQVBQUklTRV9NRVNTQUdFID0gXCJOZXcgZmlsZSB1cGxvYWRlZCB7ZmlsZW5hbWV9ICh7c2l6ZX0pLCBTdG9yYWdlIHVzZWQge3N0b3JhZ2V9XCJcbkFQUFJJU0VfU0laRV9VTklUID0gXCJBdXRvXCJcbkFMTE9XRURfRVhURU5TSU9OUyA9IFwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbiIKfQ==
```

## Links

`file-sharing`,`self-hosted`,`simple`

---

Version:`latest`

DumbBudgetDumbBudget is a simple, self-hosted budget tracking service with PIN protection and no database required.

DumbPadDumbPad is a simple, self-hosted notepad service with PIN protection and no database required.

### On this page

ConfigurationBase64LinksTags