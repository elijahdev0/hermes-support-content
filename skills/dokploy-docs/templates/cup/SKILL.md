---
title: "Cup | Dokploy"
source: "https://docs.dokploy.com/docs/templates/cup"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

Cup | Dokploy

# Cup

Copy as Markdown

Cup is a self-hosted Docker container management UI.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  cup:
    image: ghcr.io/sergi0g/cup:latest
    restart: unless-stopped
    command: serve
    ports:
      - "8000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

```
[variables]
main_domain = "${domain}"

[config]

[[config.domains]]
serviceName = "cup"
port = 8000
host = "${main_domain}"

[config.env]

[[config.mounts]]
serviceName = "cup"
source = "/var/run/docker.sock"
target = "/var/run/docker.sock"
type = "bind"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGN1cDpcbiAgICBpbWFnZTogZ2hjci5pby9zZXJnaTBnL2N1cDpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGNvbW1hbmQ6IHNlcnZlXG4gICAgcG9ydHM6XG4gICAgICAtIFwiODAwMFwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gL3Zhci9ydW4vZG9ja2VyLnNvY2s6L3Zhci9ydW4vZG9ja2VyLnNvY2tcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImN1cFwiXG5wb3J0ID0gODAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJjdXBcIlxuc291cmNlID0gXCIvdmFyL3J1bi9kb2NrZXIuc29ja1wiXG50YXJnZXQgPSBcIi92YXIvcnVuL2RvY2tlci5zb2NrXCJcbnR5cGUgPSBcImJpbmRcIlxuIgp9
```

## Links

`docker`,`container`,`management`,`ui`,`self-hosted`

---

Version:`latest`

CrowdsecCrowdSec provides open source solution for detecting and blocking malicious IPs, safeguarding both infrastructure and application security.

CyberChefCyberChef is a web application for encryption, encoding, compression, and data analysis, developed by GCHQ.

### On this page

ConfigurationBase64LinksTags