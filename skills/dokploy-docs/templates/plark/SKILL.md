---
title: "Plark | Dokploy"
source: "https://docs.dokploy.com/docs/templates/plark"
category: dokploy-docs
created: "2026-06-25T17:21:56.647Z"
---

Plark | Dokploy

# Plark

Copy as Markdown

Self-hosted Website Builder

## Configuration

docker-compose.ymltemplate.toml

```
services:
  plark:
    image: plarkinc/plark:latest
    pull_policy: always
    restart: unless-stopped
    ports:
      - "80"
    volumes:
      - plark-data:/var/data
volumes:
  plark-data:
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "plark"
port = 80
host = "${main_domain}"

[config.env]

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwbGFyazpcbiAgICBpbWFnZTogcGxhcmtpbmMvcGxhcms6bGF0ZXN0XG4gICAgcHVsbF9wb2xpY3k6IGFsd2F5c1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIFwiODBcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBsYXJrLWRhdGE6L3Zhci9kYXRhXG52b2x1bWVzOlxuICBwbGFyay1kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInBsYXJrXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblxuW1tjb25maWcubW91bnRzXV0iCn0=
```

## Links

`cms`,`content-management`,`blog`

---

Version:`latest`

PlaneEasy, flexible, open source project management software

PlausiblePlausible is a open source, self-hosted web analytics platform that lets you track website traffic and user behavior.

### On this page

ConfigurationBase64LinksTags