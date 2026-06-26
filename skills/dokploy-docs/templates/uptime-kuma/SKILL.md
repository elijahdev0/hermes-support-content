---
title: "Uptime Kuma | Dokploy"
source: "https://docs.dokploy.com/docs/templates/uptime-kuma"
category: dokploy-docs
created: "2026-06-25T17:22:01.419Z"
---

Uptime Kuma | Dokploy

# Uptime Kuma

Copy as Markdown

Uptime Kuma is a free and open source monitoring tool that allows you to monitor your websites and applications.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  uptime-kuma:
    image: louislam/uptime-kuma:2.1.0
    restart: always
    volumes:
      - uptime-kuma-data:/app/data
      - /var/run/docker.sock:/var/run/docker.sock

volumes:
  uptime-kuma-data:
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "uptime-kuma"
port = 3_001
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICB1cHRpbWUta3VtYTpcbiAgICBpbWFnZTogbG91aXNsYW0vdXB0aW1lLWt1bWE6Mi4xLjBcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSB1cHRpbWUta3VtYS1kYXRhOi9hcHAvZGF0YVxuICAgICAgLSAvdmFyL3J1bi9kb2NrZXIuc29jazovdmFyL3J1bi9kb2NrZXIuc29ja1xuXG52b2x1bWVzOlxuICB1cHRpbWUta3VtYS1kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IHt9XG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ1cHRpbWUta3VtYVwiXG5wb3J0ID0gM18wMDFcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`monitoring`

---

Version:`2.1.0`

UpsnapUpsnap is a simple network device monitor and dashboard built on PocketBase.

useSendOpen source alternative to Resend, Sendgrid, Postmark etc.

### On this page

ConfigurationBase64LinksTags