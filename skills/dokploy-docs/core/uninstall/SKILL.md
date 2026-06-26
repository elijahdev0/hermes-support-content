---
title: "Uninstall | Dokploy"
source: "https://docs.dokploy.com/docs/core/uninstall"
category: dokploy-docs
created: "2026-06-25T17:21:39.216Z"
---

Uninstall | Dokploy

# Uninstall

Copy as Markdown

Learn how to uninstall Dokploy on your server

Follow these steps to completely remove Dokploy and its components from your server.

Remove the docker swarm services created by Dokploy:

```
docker service remove dokploy dokploy-traefik dokploy-postgres dokploy-redis
docker container remove -f dokploy-traefik
```

Remove the docker volumes created by Dokploy:

```
docker volume remove -f dokploy dokploy-postgres dokploy-redis
```

Remove the docker network created by Dokploy:

```
docker network remove -f dokploy-network
docker network remove -f ingress
```

Docker cleanup to remove leftovers:

```
docker container prune --force
docker image prune --all --force
docker volume prune --all --force
docker builder prune --all --force
docker system prune --all --volumes --force
```

Remove the dokploy files and directories from your server:

```
sudo rm -rf /etc/dokploy
```

Reset Password & 2FAReset your password to access your Dokploy account and disable 2FA.

VideosVideos about how to install and use Dokploy.