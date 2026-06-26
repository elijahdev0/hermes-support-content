---
title: "Navidrome | Dokploy"
source: "https://docs.dokploy.com/docs/templates/navidrome"
category: dokploy-docs
created: "2026-06-25T17:21:54.354Z"
---

Navidrome | Dokploy

# Navidrome

Copy as Markdown

Navidrome is a modern music server and streamer compatible with Subsonic/Airsonic. Stream your music collection anywhere.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  navidrome:
    image: deluan/navidrome:latest
    restart: unless-stopped
    environment:
      - ND_SCANSCHEDULE=1h
      - ND_LOGLEVEL=info
      - ND_SESSIONTIMEOUT=24h
    volumes:
      - navidrome-data:/data
      - navidrome-music:/music:ro
    ports:
      - 4533

volumes:
  navidrome-data: {}
  navidrome-music: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "navidrome"
port = 4533
host = "${main_domain}"

[config.env]

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBuYXZpZHJvbWU6XG4gICAgaW1hZ2U6IGRlbHVhbi9uYXZpZHJvbWU6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTkRfU0NBTlNDSEVEVUxFPTFoXG4gICAgICAtIE5EX0xPR0xFVkVMPWluZm9cbiAgICAgIC0gTkRfU0VTU0lPTlRJTUVPVVQ9MjRoXG4gICAgdm9sdW1lczpcbiAgICAgIC0gbmF2aWRyb21lLWRhdGE6L2RhdGFcbiAgICAgIC0gbmF2aWRyb21lLW11c2ljOi9tdXNpYzpyb1xuICAgIHBvcnRzOlxuICAgICAgLSA0NTMzXG5cbnZvbHVtZXM6XG4gIG5hdmlkcm9tZS1kYXRhOiB7fVxuICBuYXZpZHJvbWUtbXVzaWM6IHt9IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIm5hdmlkcm9tZVwiXG5wb3J0ID0gNDUzM1xuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblxuW1tjb25maWcubW91bnRzXV0iCn0=
```

## Links

`music`,`streaming`,`media-server`,`subsonic`,`self-hosted`,`audio`

---

Version:`latest`

n8n with Postgresn8n is an open source low-code platform for automating workflows and integrations with PostgreSQL database for better performance and scalability.

NekoNeko is a self-hosted virtual browser that runs in Docker and allows you to share browser sessions with others.

### On this page

ConfigurationBase64LinksTags