---
title: "SilverBullet | Dokploy"
source: "https://docs.dokploy.com/docs/templates/silverbullet"
category: dokploy-docs
created: "2026-06-25T17:21:59.114Z"
---

SilverBullet | Dokploy

# SilverBullet

Copy as Markdown

SilverBullet is a personal knowledge base and collaborative note-taking platform.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  silverbullet:
    image: ghcr.io/silverbulletmd/silverbullet:v2
    restart: unless-stopped
    environment:
      - SB_USER=${SB_USER}
    volumes:
      - silverbullet-space:/space
    expose:
      - 3000

  watchtower:
    image: containrrr/watchtower
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock

volumes:
  silverbullet-space: {}
```

```
[variables]
main_domain = "${domain}"
sb_user = "admin:${password:16}"

[config]
[[config.domains]]
serviceName = "silverbullet"
port = 3000
host = "${main_domain}"

[config.env]
SB_USER = "${sb_user}"

[[config.mounts]]
name = "silverbullet-space"
mountPath = "/space"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHNpbHZlcmJ1bGxldDpcbiAgICBpbWFnZTogZ2hjci5pby9zaWx2ZXJidWxsZXRtZC9zaWx2ZXJidWxsZXQ6djJcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBTQl9VU0VSPSR7U0JfVVNFUn1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBzaWx2ZXJidWxsZXQtc3BhY2U6L3NwYWNlXG4gICAgZXhwb3NlOlxuICAgICAgLSAzMDAwXG5cbiAgd2F0Y2h0b3dlcjpcbiAgICBpbWFnZTogY29udGFpbnJyci93YXRjaHRvd2VyXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSAvdmFyL3J1bi9kb2NrZXIuc29jazovdmFyL3J1bi9kb2NrZXIuc29ja1xuXG52b2x1bWVzOlxuICBzaWx2ZXJidWxsZXQtc3BhY2U6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuc2JfdXNlciA9IFwiYWRtaW46JHtwYXNzd29yZDoxNn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwic2lsdmVyYnVsbGV0XCJcbnBvcnQgPSAzMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuU0JfVVNFUiA9IFwiJHtzYl91c2VyfVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5uYW1lID0gXCJzaWx2ZXJidWxsZXQtc3BhY2VcIlxubW91bnRQYXRoID0gXCIvc3BhY2VcIlxuIgp9
```

## Links

`notes`,`knowledge-base`,`productivity`,`markdown`

---

Version:`v2`

SigNozSigNoz is an open-source Datadog or New Relic alternative. Get APM, logs,traces, metrics, exceptions, & alerts in a single tool.

SlashSlash is a modern, self-hosted bookmarking service and link shortener that helps you organize and share your favorite links.

### On this page

ConfigurationBase64LinksTags