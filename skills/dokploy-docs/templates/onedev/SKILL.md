---
title: "OneDev | Dokploy"
source: "https://docs.dokploy.com/docs/templates/onedev"
category: dokploy-docs
created: "2026-06-25T17:21:54.355Z"
---

OneDev | Dokploy

# OneDev

Copy as Markdown

Git server with CI/CD, kanban, and packages. Seamless integration. Unparalleled experience.

## Configuration

docker-compose.ymltemplate.toml

```
---
services:
  onedev:
    image: 1dev/server:11.6.6
    restart: always

    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
      - "onedev-data:/opt/onedev"

volumes:
  onedev-data:
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "onedev"
port = 6_610
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIi0tLVxuc2VydmljZXM6XG4gIG9uZWRldjpcbiAgICBpbWFnZTogMWRldi9zZXJ2ZXI6MTEuNi42XG4gICAgcmVzdGFydDogYWx3YXlzXG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSBcIi92YXIvcnVuL2RvY2tlci5zb2NrOi92YXIvcnVuL2RvY2tlci5zb2NrXCJcbiAgICAgIC0gXCJvbmVkZXYtZGF0YTovb3B0L29uZWRldlwiXG4gICAgXG52b2x1bWVzOlxuICBvbmVkZXYtZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0ge31cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIm9uZWRldlwiXG5wb3J0ID0gNl82MTBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`self-hosted`,`development`

---

Version:`11.6.6`

Omni-ToolsOmni-Tools is a collection of useful tools in a single self-hosted web application.

One Time SecretShare sensitive information securely with self-destructing links that are only viewable once.

### On this page

ConfigurationBase64LinksTags