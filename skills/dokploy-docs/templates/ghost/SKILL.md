---
title: "Ghost | Dokploy"
source: "https://docs.dokploy.com/docs/templates/ghost"
category: dokploy-docs
created: "2026-06-25T17:21:48.522Z"
---

Ghost | Dokploy

# Ghost

Copy as Markdown

Ghost is a free and open source, professional publishing platform built on a modern Node.js technology stack.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  ghost:
    image: ghost:6-alpine
    restart: always
    environment:
      database__client: mysql
      database__connection__host: db
      database__connection__user: root
      database__connection__password: example
      database__connection__database: ghost
      url: http://${GHOST_HOST}

    volumes:
      - ghost:/var/lib/ghost/content

  db:
    image: mysql:8.0
    restart: always

    environment:
      MYSQL_ROOT_PASSWORD: example
    volumes:
      - db:/var/lib/mysql

volumes:
  ghost:
  db:
```

```
[variables]
main_domain = "${domain}"

[config]
env = ["GHOST_HOST=${main_domain}"]
mounts = []

[[config.domains]]
serviceName = "ghost"
port = 2_368
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBnaG9zdDpcbiAgICBpbWFnZTogZ2hvc3Q6Ni1hbHBpbmVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIGRhdGFiYXNlX19jbGllbnQ6IG15c3FsXG4gICAgICBkYXRhYmFzZV9fY29ubmVjdGlvbl9faG9zdDogZGJcbiAgICAgIGRhdGFiYXNlX19jb25uZWN0aW9uX191c2VyOiByb290XG4gICAgICBkYXRhYmFzZV9fY29ubmVjdGlvbl9fcGFzc3dvcmQ6IGV4YW1wbGVcbiAgICAgIGRhdGFiYXNlX19jb25uZWN0aW9uX19kYXRhYmFzZTogZ2hvc3RcbiAgICAgIHVybDogaHR0cDovLyR7R0hPU1RfSE9TVH1cblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGdob3N0Oi92YXIvbGliL2dob3N0L2NvbnRlbnRcblxuICBkYjpcbiAgICBpbWFnZTogbXlzcWw6OC4wXG4gICAgcmVzdGFydDogYWx3YXlzXG5cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE1ZU1FMX1JPT1RfUEFTU1dPUkQ6IGV4YW1wbGVcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYjovdmFyL2xpYi9teXNxbFxuXG52b2x1bWVzOlxuICBnaG9zdDpcbiAgZGI6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1wiR0hPU1RfSE9TVD0ke21haW5fZG9tYWlufVwiXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZ2hvc3RcIlxucG9ydCA9IDJfMzY4XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`cms`

---

Version:`6.0.0`

Garage S3 with Web UIGarage is an open-source distributed object storage service tailored for self-hosting. For authentication in the web-ui please go to https://github.com/khairul169/garage-webui?tab=readme-ov-file#authentication

Gitea MirrorGitea Mirror is a modern web app for automatically mirroring repositories from GitHub to your self-hosted Gitea instance. It features a user-friendly interface to sync public, private, or starred GitHub repos, mirror entire organizations with structure preservation, and optionally mirror issues and labels. The application includes smart filtering, detailed logs, and scheduled automatic mirroring.

### On this page

ConfigurationBase64LinksTags