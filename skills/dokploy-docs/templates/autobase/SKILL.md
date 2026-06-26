---
title: "Autobase | Dokploy"
source: "https://docs.dokploy.com/docs/templates/autobase"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

Autobase | Dokploy

# Autobase

Copy as Markdown

Autobase for PostgreSQL® is an open-source alternative to cloud-managed databases (self-hosted DBaaS).

## Configuration

docker-compose.ymltemplate.toml

```
services:
  autobase-console:
    image: autobase/console:2.5.2
    restart: unless-stopped
    ports:
      - "80"
      - "8080"
    environment:
      - PG_CONSOLE_API_URL=${PG_CONSOLE_API_URL}
      - PG_CONSOLE_AUTHORIZATION_TOKEN=${PG_CONSOLE_AUTHORIZATION_TOKEN}
    volumes:
      - console_postgres:/var/lib/postgresql
      - /var/run/docker.sock:/var/run/docker.sock
      - /tmp/ansible:/tmp/ansible

volumes:
  console_postgres:
```

```
[variables]
main_domain = "${domain}"
api_domain = "${domain}"
authenticattion_token = "${base64:32}"

[config]
env = [
    "PG_CONSOLE_API_URL=http://${api_domain}/api/v1",
    "PG_CONSOLE_AUTHORIZATION_TOKEN=${authenticattion_token}",
]
mounts = []

[[config.domains]]
serviceName = "autobase-console"
port = 80
host = "${main_domain}"

[[config.domains]]
serviceName = "autobase-console"
port = 8_080
host = "${api_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBhdXRvYmFzZS1jb25zb2xlOlxuICAgIGltYWdlOiBhdXRvYmFzZS9jb25zb2xlOjIuNS4yXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gXCI4MFwiXG4gICAgICAtIFwiODA4MFwiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBHX0NPTlNPTEVfQVBJX1VSTD0ke1BHX0NPTlNPTEVfQVBJX1VSTH1cbiAgICAgIC0gUEdfQ09OU09MRV9BVVRIT1JJWkFUSU9OX1RPS0VOPSR7UEdfQ09OU09MRV9BVVRIT1JJWkFUSU9OX1RPS0VOfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGNvbnNvbGVfcG9zdGdyZXM6L3Zhci9saWIvcG9zdGdyZXNxbFxuICAgICAgLSAvdmFyL3J1bi9kb2NrZXIuc29jazovdmFyL3J1bi9kb2NrZXIuc29ja1xuICAgICAgLSAvdG1wL2Fuc2libGU6L3RtcC9hbnNpYmxlXG5cbnZvbHVtZXM6XG4gIGNvbnNvbGVfcG9zdGdyZXM6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYXBpX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmF1dGhlbnRpY2F0dGlvbl90b2tlbiA9IFwiJHtiYXNlNjQ6MzJ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgICBcIlBHX0NPTlNPTEVfQVBJX1VSTD1odHRwOi8vJHthcGlfZG9tYWlufS9hcGkvdjFcIixcbiAgICBcIlBHX0NPTlNPTEVfQVVUSE9SSVpBVElPTl9UT0tFTj0ke2F1dGhlbnRpY2F0dGlvbl90b2tlbn1cIixcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImF1dG9iYXNlLWNvbnNvbGVcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImF1dG9iYXNlLWNvbnNvbGVcIlxucG9ydCA9IDhfMDgwXG5ob3N0ID0gXCIke2FwaV9kb21haW59XCJcbiIKfQ==
```

## Links

`database`,`postgres`,`automation`,`self-hosted`,`dbaas`

---

Version:`2.5.2`

AuthorizerAuthorizer is a powerful tool designed to simplify the process of user authentication and authorization in your applications. It allows you to build secure apps 10x faster with its low code tool and low-cost deployment.

AutomatischAutomatisch is a powerful, self-hosted workflow automation tool designed for connecting your apps and automating repetitive tasks. With Automatisch, you can create workflows to sync data, send notifications, and perform various actions seamlessly across different services.

### On this page

ConfigurationBase64LinksTags