---
title: "Ampache | Dokploy"
source: "https://docs.dokploy.com/docs/templates/ampache"
category: dokploy-docs
created: "2026-06-25T17:21:40.414Z"
---

Ampache | Dokploy

# Ampache

Copy as Markdown

Ampache is a web-based audio/video streaming application and file manager allowing you to access your music & videos from anywhere, using almost any internet enabled device.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  ampache:
    image: ampache/ampache:latest
    restart: unless-stopped
    ports:
      - 80
    volumes:
      - config:/var/www/config
      - log:/var/log/ampache
      - mysql:/var/lib/mysql
      - ${MEDIA_PATH}:/media

volumes:
  config: {}
  log: {}
  mysql: {}
```

```
[variables]
main_domain = "${domain}"
media_path = "/path/to/your/media"

[config]
[[config.domains]]
serviceName = "ampache"
port = 80
host = "${main_domain}"

[config.env]
MEDIA_PATH = "${media_path}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhbXBhY2hlOlxuICAgIGltYWdlOiBhbXBhY2hlL2FtcGFjaGU6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gODBcbiAgICB2b2x1bWVzOlxuICAgICAgLSBjb25maWc6L3Zhci93d3cvY29uZmlnXG4gICAgICAtIGxvZzovdmFyL2xvZy9hbXBhY2hlXG4gICAgICAtIG15c3FsOi92YXIvbGliL215c3FsXG4gICAgICAtICR7TUVESUFfUEFUSH06L21lZGlhXG5cbnZvbHVtZXM6XG4gIGNvbmZpZzoge31cbiAgbG9nOiB7fVxuICBteXNxbDoge30gIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbm1lZGlhX3BhdGggPSBcIi9wYXRoL3RvL3lvdXIvbWVkaWFcIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYW1wYWNoZVwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5NRURJQV9QQVRIID0gXCIke21lZGlhX3BhdGh9XCIgIgp9
```

## Links

`media`,`music`,`streaming`

---

Version:`latest`

AllTubeAllTube Download is an application designed to facilitate the downloading of videos from YouTube and other video sites. It provides an HTML GUI for youtube-dl with video conversion capabilities and JSON API support.

AnonUploadAnonUpload is a secure, anonymous file sharing application that does not require a database. It is built with privacy as a priority, ensuring that the direct filename used is not displayed.

### On this page

ConfigurationBase64LinksTags