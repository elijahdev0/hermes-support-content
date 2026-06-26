---
title: "Poste.io | Dokploy"
source: "https://docs.dokploy.com/docs/templates/poste.io"
category: dokploy-docs
created: "2026-06-25T17:21:56.648Z"
---

Poste.io | Dokploy

# Poste.io

Copy as Markdown

Complete mail server solution with SMTP, IMAP, POP3, antispam, antivirus, web administration and webmail client.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  mailserver:
    image: analogic/poste.io
    restart: unless-stopped
    hostname: mail.${DOMAIN}
    ports:
      - "25:25"
      - "110:110"
      - "143:143"
      - "465:465"
      - "587:587"
      - "993:993"
      - "995:995"
      - "4190:4190"
    environment:
      - TZ=${TZ}
      - HTTPS=OFF
      - HTTP_PORT=8080
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - poste-data:/data

volumes:
  poste-data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "mailserver"
port = 8080
host = "${main_domain}"

[config.env]
TZ = "UTC"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBtYWlsc2VydmVyOlxuICAgIGltYWdlOiBhbmFsb2dpYy9wb3N0ZS5pb1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgaG9zdG5hbWU6IG1haWwuJHtET01BSU59XG4gICAgcG9ydHM6XG4gICAgICAtIFwiMjU6MjVcIlxuICAgICAgLSBcIjExMDoxMTBcIlxuICAgICAgLSBcIjE0MzoxNDNcIlxuICAgICAgLSBcIjQ2NTo0NjVcIlxuICAgICAgLSBcIjU4Nzo1ODdcIlxuICAgICAgLSBcIjk5Mzo5OTNcIlxuICAgICAgLSBcIjk5NTo5OTVcIlxuICAgICAgLSBcIjQxOTA6NDE5MFwiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFRaPSR7VFp9XG4gICAgICAtIEhUVFBTPU9GRlxuICAgICAgLSBIVFRQX1BPUlQ9ODA4MFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC9ldGMvbG9jYWx0aW1lOi9ldGMvbG9jYWx0aW1lOnJvXG4gICAgICAtIHBvc3RlLWRhdGE6L2RhdGFcblxudm9sdW1lczpcbiAgcG9zdGUtZGF0YToge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJtYWlsc2VydmVyXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuVFogPSBcIlVUQ1wiXG4iCn0=
```

## Links

`email`,`mail-server`,`smtp`,`imap`,`pop3`,`antispam`,`antivirus`,`webmail`

---

Version:`latest`

PortainerPortainer is a container management tool for deploying, troubleshooting, and securing applications across cloud, data centers, and IoT.

PostgreSQL with PgDogPostgreSQL database with PgDog connection pooler, load balancer, and horizontal scaling proxy. A modern alternative to PgBouncer with multi-threading support.

### On this page

ConfigurationBase64LinksTags