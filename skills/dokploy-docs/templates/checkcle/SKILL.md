---
title: "Checkcle | Dokploy"
source: "https://docs.dokploy.com/docs/templates/checkcle"
category: dokploy-docs
created: "2026-06-25T17:21:43.962Z"
---

Checkcle | Dokploy

# Checkcle

Copy as Markdown

Checkcle is a security and compliance tool by Operacle, providing insights into system configuration and runtime checks.

## Configuration

docker-compose.ymltemplate.toml

```
#Default id pass Username: [email protected] Password: Admin123456

version: "3.9"
services:
  checkcle:
    image: operacle/checkcle:latest
    restart: unless-stopped
    expose:
      - 8090
    volumes:
      - checkcle-data:/mnt/pb_data
    ulimits:
      nofile:
        soft: 4096
        hard: 8192

volumes:
  checkcle-data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "checkcle"
port = 8090
host = "${main_domain}"

[config.env]

[[config.mounts]]
source = "checkcle-data"
target = "/mnt/pb_data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiNEZWZhdWx0IGlkIHBhc3MgVXNlcm5hbWU6IGFkbWluQGV4YW1wbGUuY29tIFBhc3N3b3JkOiBBZG1pbjEyMzQ1NlxuXG52ZXJzaW9uOiBcIjMuOVwiXG5zZXJ2aWNlczpcbiAgY2hlY2tjbGU6XG4gICAgaW1hZ2U6IG9wZXJhY2xlL2NoZWNrY2xlOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZXhwb3NlOlxuICAgICAgLSA4MDkwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gY2hlY2tjbGUtZGF0YTovbW50L3BiX2RhdGFcbiAgICB1bGltaXRzOlxuICAgICAgbm9maWxlOlxuICAgICAgICBzb2Z0OiA0MDk2XG4gICAgICAgIGhhcmQ6IDgxOTJcblxudm9sdW1lczpcbiAgY2hlY2tjbGUtZGF0YToge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjaGVja2NsZVwiXG5wb3J0ID0gODA5MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblxuW1tjb25maWcubW91bnRzXV1cbnNvdXJjZSA9IFwiY2hlY2tjbGUtZGF0YVwiXG50YXJnZXQgPSBcIi9tbnQvcGJfZGF0YVwiIgp9
```

## Links

`security`,`compliance`,`monitoring`

---

Version:`latest`

ChatwootOpen-source customer engagement platform that provides a shared inbox for teams, live chat, and omnichannel support.

CheckmateCheckmate is an open-source, self-hosted tool designed to track and monitor server hardware, uptime, response times, and incidents in real-time with beautiful visualizations.

### On this page

ConfigurationBase64LinksTags