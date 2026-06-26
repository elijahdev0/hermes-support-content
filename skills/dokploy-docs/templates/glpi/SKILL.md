---
title: "GLPI Project | Dokploy"
source: "https://docs.dokploy.com/docs/templates/glpi"
category: dokploy-docs
created: "2026-06-25T17:21:48.522Z"
---

GLPI Project | Dokploy

# GLPI Project

Copy as Markdown

The most complete open source service management software

## Configuration

docker-compose.ymltemplate.toml

```
services:
  glpi-mysql:
    image: mysql:9.1.0
    restart: always
    volumes:
      - glpi-mysql-data:/var/lib/mysql

  glpi-web:
    image: elestio/glpi:10.0.16
    restart: always
    volumes:
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
      - glpi-www-data:/var/www/html/glpi
    environment:
      - TIMEZONE=Europe/Brussels

volumes:
  glpi-mysql-data:
  glpi-www-data:
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "glpi-web"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBnbHBpLW15c3FsOlxuICAgIGltYWdlOiBteXNxbDo5LjEuMFxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIHZvbHVtZXM6XG4gICAgICAtIGdscGktbXlzcWwtZGF0YTovdmFyL2xpYi9teXNxbFxuXG5cbiAgZ2xwaS13ZWI6XG4gICAgaW1hZ2U6IGVsZXN0aW8vZ2xwaToxMC4wLjE2XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gL2V0Yy90aW1lem9uZTovZXRjL3RpbWV6b25lOnJvXG4gICAgICAtIC9ldGMvbG9jYWx0aW1lOi9ldGMvbG9jYWx0aW1lOnJvXG4gICAgICAtIGdscGktd3d3LWRhdGE6L3Zhci93d3cvaHRtbC9nbHBpXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFRJTUVaT05FPUV1cm9wZS9CcnVzc2Vsc1xuXG5cbnZvbHVtZXM6XG4gIGdscGktbXlzcWwtZGF0YTpcbiAgZ2xwaS13d3ctZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZ2xwaS13ZWJcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`self-hosted`,`project-management`,`management`

---

Version:`10.0.16`

GlitchtipGlitchtip is simple, open source error tracking

WhatsApp API Multi Device VersionWhatsApp API Multi Device Version the open-source, self-hosted whatsapp api. Send a chat, image and voice note with your own server.

### On this page

ConfigurationBase64LinksTags