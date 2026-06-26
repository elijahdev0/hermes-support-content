---
title: "Roundcube | Dokploy"
source: "https://docs.dokploy.com/docs/templates/roundcube"
category: dokploy-docs
created: "2026-06-25T17:21:57.938Z"
---

Roundcube | Dokploy

# Roundcube

Copy as Markdown

Free and open source webmail software for the masses, written in PHP.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  roundcubemail:
    image: roundcube/roundcubemail:1.6.9-apache
    volumes:
      - ./www:/var/www/html
      - ./db/sqlite:/var/roundcube/db
    environment:
      - ROUNDCUBEMAIL_DB_TYPE=sqlite
      - ROUNDCUBEMAIL_SKIN=elastic
      - ROUNDCUBEMAIL_DEFAULT_HOST=${DEFAULT_HOST}
      - ROUNDCUBEMAIL_SMTP_SERVER=${SMTP_SERVER}
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "roundcubemail"
port = 80
host = "${main_domain}"

[config.env]
DEFAULT_HOST = "tls://mail.example.com"
SMTP_SERVER = "tls://mail.example.com"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICByb3VuZGN1YmVtYWlsOlxuICAgIGltYWdlOiByb3VuZGN1YmUvcm91bmRjdWJlbWFpbDoxLjYuOS1hcGFjaGVcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuL3d3dzovdmFyL3d3dy9odG1sXG4gICAgICAtIC4vZGIvc3FsaXRlOi92YXIvcm91bmRjdWJlL2RiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFJPVU5EQ1VCRU1BSUxfREJfVFlQRT1zcWxpdGVcbiAgICAgIC0gUk9VTkRDVUJFTUFJTF9TS0lOPWVsYXN0aWNcbiAgICAgIC0gUk9VTkRDVUJFTUFJTF9ERUZBVUxUX0hPU1Q9JHtERUZBVUxUX0hPU1R9XG4gICAgICAtIFJPVU5EQ1VCRU1BSUxfU01UUF9TRVJWRVI9JHtTTVRQX1NFUlZFUn1cblxuXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicm91bmRjdWJlbWFpbFwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5ERUZBVUxUX0hPU1QgPSBcInRsczovL21haWwuZXhhbXBsZS5jb21cIlxuU01UUF9TRVJWRVIgPSBcInRsczovL21haWwuZXhhbXBsZS5jb21cIlxuIgp9
```

## Links

`self-hosted`,`email`,`webmail`

---

Version:`1.6.9`

RoteRote is an open-source multi-platform personal note system featuring an open API, full data ownership, and effortless Docker deployment.

RSS-BridgeRSS-Bridge is a PHP project capable of generating Atom feeds for websites that don't have one.

### On this page

ConfigurationBase64LinksTags