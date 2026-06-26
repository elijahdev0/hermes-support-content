---
title: "MCSManager | Dokploy"
source: "https://docs.dokploy.com/docs/templates/mcsmanager"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

MCSManager | Dokploy

# MCSManager

Copy as Markdown

A modern dashboard for managing Minecraft servers. Primarily focused on Minecraft, but also supports other games and features a UI that's easy for beginners to use and supports i18n.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  web:
    image: githubyumao/mcsmanager-web:latest
    restart: unless-stopped
    ports:
      - 23333
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - mcsmanager-web-data:/opt/mcsmanager/web/data
      - mcsmanager-web-logs:/opt/mcsmanager/web/logs
  daemon:
    image: githubyumao/mcsmanager-daemon:latest
    restart: unless-stopped
    ports:
      - 24444
    environment:
      - MCSM_DOCKER_WORKSPACE_PATH=/opt/mcsmanager/daemon/data/InstanceData
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - mcsmanager-daemon-data:/opt/mcsmanager/daemon/data
      - mcsmanager-daemon-logs:/opt/mcsmanager/daemon/logs
      - /var/run/docker.sock:/var/run/docker.sock

volumes:
  mcsmanager-web-data:
  mcsmanager-web-logs:
  mcsmanager-daemon-data:
  mcsmanager-daemon-logs:
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "web"
port = 23333
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB3ZWI6XG4gICAgaW1hZ2U6IGdpdGh1Ynl1bWFvL21jc21hbmFnZXItd2ViOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDIzMzMzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gL2V0Yy9sb2NhbHRpbWU6L2V0Yy9sb2NhbHRpbWU6cm9cbiAgICAgIC0gbWNzbWFuYWdlci13ZWItZGF0YTovb3B0L21jc21hbmFnZXIvd2ViL2RhdGFcbiAgICAgIC0gbWNzbWFuYWdlci13ZWItbG9nczovb3B0L21jc21hbmFnZXIvd2ViL2xvZ3NcbiAgZGFlbW9uOlxuICAgIGltYWdlOiBnaXRodWJ5dW1hby9tY3NtYW5hZ2VyLWRhZW1vbjpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSAyNDQ0NFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBNQ1NNX0RPQ0tFUl9XT1JLU1BBQ0VfUEFUSD0vb3B0L21jc21hbmFnZXIvZGFlbW9uL2RhdGEvSW5zdGFuY2VEYXRhXG4gICAgdm9sdW1lczpcbiAgICAgIC0gL2V0Yy9sb2NhbHRpbWU6L2V0Yy9sb2NhbHRpbWU6cm9cbiAgICAgIC0gbWNzbWFuYWdlci1kYWVtb24tZGF0YTovb3B0L21jc21hbmFnZXIvZGFlbW9uL2RhdGFcbiAgICAgIC0gbWNzbWFuYWdlci1kYWVtb24tbG9nczovb3B0L21jc21hbmFnZXIvZGFlbW9uL2xvZ3NcbiAgICAgIC0gL3Zhci9ydW4vZG9ja2VyLnNvY2s6L3Zhci9ydW4vZG9ja2VyLnNvY2tcblxudm9sdW1lczpcbiAgbWNzbWFuYWdlci13ZWItZGF0YTpcbiAgbWNzbWFuYWdlci13ZWItbG9nczpcbiAgbWNzbWFuYWdlci1kYWVtb24tZGF0YTpcbiAgbWNzbWFuYWdlci1kYWVtb24tbG9nczpcblxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtdXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ3ZWJcIlxucG9ydCA9IDIzMzMzXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbiIKfQ==
```

## Links

`minecraft`,`game-server`,`management`,`dashboard`

---

Version:`latest`

MAZANOKEMAZANOKE is a modern, self-hosted image hosting and sharing platform. Upload, organize, and share your images with a clean and intuitive interface.

Mealie (sqlite version) Mealie is an intuitive and easy to use recipe management app. It's designed to make your life easier by being the best recipes management experience on the web and providing you with an easy to use interface to manage your growing collection of recipes.

### On this page

ConfigurationBase64LinksTags