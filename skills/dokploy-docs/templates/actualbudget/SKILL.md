---
title: "Actual Budget | Dokploy"
source: "https://docs.dokploy.com/docs/templates/actualbudget"
category: dokploy-docs
created: "2026-06-25T17:21:40.413Z"
---

Actual Budget | Dokploy

# Actual Budget

Copy as Markdown

A super fast and privacy-focused app for managing your finances.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  actualbudget:
    image: docker.io/actualbudget/actual-server:latest
    environment:
      # See all options at https://actualbudget.org/docs/config
      - ACTUAL_PORT=5006
    volumes:
      - actual-data:/data
    restart: unless-stopped

volumes:
  actual-data:
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "actualbudget"
port = 5_006
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBhY3R1YWxidWRnZXQ6XG4gICAgaW1hZ2U6IGRvY2tlci5pby9hY3R1YWxidWRnZXQvYWN0dWFsLXNlcnZlcjpsYXRlc3RcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgU2VlIGFsbCBvcHRpb25zIGF0IGh0dHBzOi8vYWN0dWFsYnVkZ2V0Lm9yZy9kb2NzL2NvbmZpZ1xuICAgICAgLSBBQ1RVQUxfUE9SVD01MDA2XG4gICAgdm9sdW1lczpcbiAgICAgIC0gYWN0dWFsLWRhdGE6L2RhdGFcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG52b2x1bWVzOlxuICBhY3R1YWwtZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYWN0dWFsYnVkZ2V0XCJcbnBvcnQgPSA1XzAwNlxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`budgeting`,`finance`,`money`

---

Version:`latest`

ActivepiecesOpen-source no-code business automation tool. An alternative to Zapier, Make.com, and Tray.

AdGuard HomeAdGuard Home is a comprehensive solution designed to enhance your online browsing experience by eliminating all kinds of ads, from annoying banners and pop-ups to intrusive video ads. It provides privacy protection, browsing security, and parental control features while maintaining website functionality.

### On this page

ConfigurationBase64LinksTags