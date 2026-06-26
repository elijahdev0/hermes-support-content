---
title: "Palmr | Dokploy"
source: "https://docs.dokploy.com/docs/templates/palmr"
category: dokploy-docs
created: "2026-06-25T17:21:55.477Z"
---

Palmr | Dokploy

# Palmr

Copy as Markdown

Palmr the open-source, self-hosted alternative to WeTransfer. Share files securely, without tracking or limitations.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  palmr:
    image: kyantech/palmr:latest
    environment:
      - ENABLE_S3=false
      - ENCRYPTION_KEY=${ENCRYPTION_KEY}
    ports:
      - "5487"
      - "3333"
    volumes:
      - palmr_data:/app/server
    restart: unless-stopped

volumes:
  palmr_data:
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "palmr"
port = 5487
host = "${main_domain}"

[config.env]
ENCRYPTION_KEY = ""

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwYWxtcjpcbiAgICBpbWFnZToga3lhbnRlY2gvcGFsbXI6bGF0ZXN0XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIEVOQUJMRV9TMz1mYWxzZVxuICAgICAgLSBFTkNSWVBUSU9OX0tFWT0ke0VOQ1JZUFRJT05fS0VZfVxuICAgIHBvcnRzOlxuICAgICAgLSBcIjU0ODdcIlxuICAgICAgLSBcIjMzMzNcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBhbG1yX2RhdGE6L2FwcC9zZXJ2ZXJcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG52b2x1bWVzOlxuICBwYWxtcl9kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInBhbG1yXCJcbnBvcnQgPSA1NDg3XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuRU5DUllQVElPTl9LRVkgPSBcIlwiXG5cbltbY29uZmlnLm1vdW50c11dICIKfQ==
```

## Links

`file-sharing`,`self-hosted`,`open-source`

---

Version:`latest`

OwncastOwncast is a self-hosted live video streaming and chat server for use with existing broadcasting software.

ParseableFast observability and log analytics platform on object storage

### On this page

ConfigurationBase64LinksTags