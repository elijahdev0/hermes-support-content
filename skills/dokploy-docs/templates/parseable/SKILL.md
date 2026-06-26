---
title: "Parseable | Dokploy"
source: "https://docs.dokploy.com/docs/templates/parseable"
category: dokploy-docs
created: "2026-06-25T17:21:55.477Z"
---

Parseable | Dokploy

# Parseable

Copy as Markdown

Fast observability and log analytics platform on object storage

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  parseable:
    image: parseable/parseable:v1.6.0
    command: parseable local-store
    restart: unless-stopped
    volumes:
      - parseable-staging:/parseable/staging
      - parseable-data:/parseable/data
    environment:
      - P_ADDR=0.0.0.0:8000
      - P_USERNAME=${PARSEABLE_USERNAME}
      - P_PASSWORD=${PARSEABLE_PASSWORD}
      - P_STAGING_DIR=/parseable/staging
      - P_FS_DIR=/parseable/data
    ports:
      - 8000
      - 8001
      - 8002
volumes:
  parseable-staging: {}
  parseable-data: {}
```

```
[variables]
main_domain = "${domain}"
parseable_username = "${username}"
parseable_password = "${password:32}"

[config]

[[config.domains]]
serviceName = "parseable"
port = 8000
host = "${main_domain}"

[config.env]
PARSEABLE_USERNAME = "${parseable_username}"
PARSEABLE_PASSWORD = "${parseable_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBwYXJzZWFibGU6XG4gICAgaW1hZ2U6IHBhcnNlYWJsZS9wYXJzZWFibGU6djEuNi4wXG4gICAgY29tbWFuZDogcGFyc2VhYmxlIGxvY2FsLXN0b3JlXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBwYXJzZWFibGUtc3RhZ2luZzovcGFyc2VhYmxlL3N0YWdpbmdcbiAgICAgIC0gcGFyc2VhYmxlLWRhdGE6L3BhcnNlYWJsZS9kYXRhXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBfQUREUj0wLjAuMC4wOjgwMDBcbiAgICAgIC0gUF9VU0VSTkFNRT0ke1BBUlNFQUJMRV9VU0VSTkFNRX1cbiAgICAgIC0gUF9QQVNTV09SRD0ke1BBUlNFQUJMRV9QQVNTV09SRH1cbiAgICAgIC0gUF9TVEFHSU5HX0RJUj0vcGFyc2VhYmxlL3N0YWdpbmdcbiAgICAgIC0gUF9GU19ESVI9L3BhcnNlYWJsZS9kYXRhXG4gICAgcG9ydHM6XG4gICAgICAtIDgwMDBcbiAgICAgIC0gODAwMVxuICAgICAgLSA4MDAyXG52b2x1bWVzOlxuICBwYXJzZWFibGUtc3RhZ2luZzoge31cbiAgcGFyc2VhYmxlLWRhdGE6IHt9XG4gIFxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnBhcnNlYWJsZV91c2VybmFtZSA9IFwiJHt1c2VybmFtZX1cIlxucGFyc2VhYmxlX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInBhcnNlYWJsZVwiXG5wb3J0ID0gODAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblBBUlNFQUJMRV9VU0VSTkFNRSA9IFwiJHtwYXJzZWFibGVfdXNlcm5hbWV9XCJcblBBUlNFQUJMRV9QQVNTV09SRCA9IFwiJHtwYXJzZWFibGVfcGFzc3dvcmR9XCJcblxuIgp9
```

## Links

`observability`,`logging`,`analytics`,`monitoring`

---

Version:`v1.6.5`

PalmrPalmr the open-source, self-hosted alternative to WeTransfer. Share files securely, without tracking or limitations.

PassboltPassbolt is an open source credential platform for modern teams. A versatile, battle-tested solution to manage and collaborate on passwords, accesses, and secrets. All in one.

### On this page

ConfigurationBase64LinksTags