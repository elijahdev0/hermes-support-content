---
title: "i18n Blog (Kuno) | Dokploy"
source: "https://docs.dokploy.com/docs/templates/i18n-blog"
category: dokploy-docs
created: "2026-06-25T17:21:49.751Z"
---

i18n Blog (Kuno) | Dokploy

# i18n Blog (Kuno)

Copy as Markdown

Kuno is an internationalized blogging platform with a backend built in Go and a frontend in Next.js.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  kuno:
    image: ictrun/kuno:latest
    restart: unless-stopped
    environment:
      NEXT_PUBLIC_API_URL: ${NEXT_PUBLIC_API_URL}
      DB_PATH: /app/data/blog.db
      UPLOAD_DIR: /app/data/uploads
      GIN_MODE: release
      NODE_ENV: production
      JWT_SECRET: ${JWT_SECRET}
      RECOVERY_MODE: ${RECOVERY_MODE}
    volumes:
      - kuno-data:/app/data

volumes:
  kuno-data: {}
```

```
[variables]
main_domain = "${domain}"
jwt_secret = "${password:32}" # secure default
recovery_mode = "false"

[config]

[[config.domains]]
serviceName = "kuno"
port = 80
host = "${main_domain}"

[config.env]
NEXT_PUBLIC_API_URL = "https://${main_domain}/api"
DB_PATH = "/app/data/blog.db"
UPLOAD_DIR = "/app/data/uploads"
GIN_MODE = "release"
NODE_ENV = "production"
JWT_SECRET = "${jwt_secret}"
RECOVERY_MODE = "${recovery_mode}"

[[config.mounts]]
name = "kuno-data"
mountPath = "/app/data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGt1bm86XG4gICAgaW1hZ2U6IGljdHJ1bi9rdW5vOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBORVhUX1BVQkxJQ19BUElfVVJMOiAke05FWFRfUFVCTElDX0FQSV9VUkx9XG4gICAgICBEQl9QQVRIOiAvYXBwL2RhdGEvYmxvZy5kYlxuICAgICAgVVBMT0FEX0RJUjogL2FwcC9kYXRhL3VwbG9hZHNcbiAgICAgIEdJTl9NT0RFOiByZWxlYXNlXG4gICAgICBOT0RFX0VOVjogcHJvZHVjdGlvblxuICAgICAgSldUX1NFQ1JFVDogJHtKV1RfU0VDUkVUfVxuICAgICAgUkVDT1ZFUllfTU9ERTogJHtSRUNPVkVSWV9NT0RFfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGt1bm8tZGF0YTovYXBwL2RhdGFcblxudm9sdW1lczpcbiAga3Vuby1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmp3dF9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCIgIyBzZWN1cmUgZGVmYXVsdFxucmVjb3ZlcnlfbW9kZSA9IFwiZmFsc2VcIlxuXG5bY29uZmlnXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJrdW5vXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbk5FWFRfUFVCTElDX0FQSV9VUkwgPSBcImh0dHBzOi8vJHttYWluX2RvbWFpbn0vYXBpXCJcbkRCX1BBVEggPSBcIi9hcHAvZGF0YS9ibG9nLmRiXCJcblVQTE9BRF9ESVIgPSBcIi9hcHAvZGF0YS91cGxvYWRzXCJcbkdJTl9NT0RFID0gXCJyZWxlYXNlXCJcbk5PREVfRU5WID0gXCJwcm9kdWN0aW9uXCJcbkpXVF9TRUNSRVQgPSBcIiR7and0X3NlY3JldH1cIlxuUkVDT1ZFUllfTU9ERSA9IFwiJHtyZWNvdmVyeV9tb2RlfVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5uYW1lID0gXCJrdW5vLWRhdGFcIlxubW91bnRQYXRoID0gXCIvYXBwL2RhdGFcIlxuIgp9
```

## Links

`blog`,`i18n`,`nextjs`,`go`,`web`

---

Version:`latest`

HulyHuly — All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion)

I Hate MoneyI Hate Money is a web application for managing shared expenses among groups of people. It helps you track who owes what to whom, making it easy to split bills and manage group finances.

### On this page

ConfigurationBase64LinksTags