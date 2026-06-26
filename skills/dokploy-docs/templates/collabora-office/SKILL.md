---
title: "Collabora Office | Dokploy"
source: "https://docs.dokploy.com/docs/templates/collabora-office"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

Collabora Office | Dokploy

# Collabora Office

Copy as Markdown

Collabora Online is a powerful, flexible, and secure online office suite designed to break free from vendor lock-in and put you in full control of your documents.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  collabora:
    image: collabora/code:latest
    ports:
      - "9980"
    environment:
      - domain=${DOMAIN}
      - username=${USERNAME}
      - password=${PASSWORD}
      - extra_params=--o:ssl.enable=false
```

```
[variables]
DOMAIN = "${domain}"
USERNAME = "user"
PASSWORD = "${password:16}"

[config]
[[config.domains]]
serviceName = "collabora"
port = 9980
host = "${domain}"

[config.env]
DOMAIN = "${DOMAIN}"
USERNAME = "${USERNAME}"
PASSWORD = "${PASSWORD}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBjb2xsYWJvcmE6XG4gICAgaW1hZ2U6IGNvbGxhYm9yYS9jb2RlOmxhdGVzdFxuICAgIHBvcnRzOlxuICAgICAgLSBcIjk5ODBcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBkb21haW49JHtET01BSU59XG4gICAgICAtIHVzZXJuYW1lPSR7VVNFUk5BTUV9XG4gICAgICAtIHBhc3N3b3JkPSR7UEFTU1dPUkR9XG4gICAgICAtIGV4dHJhX3BhcmFtcz0tLW86c3NsLmVuYWJsZT1mYWxzZSAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbkRPTUFJTiA9IFwiJHtkb21haW59XCJcblVTRVJOQU1FID0gXCJ1c2VyXCJcblBBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjb2xsYWJvcmFcIlxucG9ydCA9IDk5ODBcbmhvc3QgPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuRE9NQUlOID0gXCIke0RPTUFJTn1cIlxuVVNFUk5BTUUgPSBcIiR7VVNFUk5BTUV9XCJcblBBU1NXT1JEID0gXCIke1BBU1NXT1JEfVwiICIKfQ==
```

## Links

`office`,`documents`,`collaboration`

---

Version:`latest`

Colanode ServerOpen-source and local-first Slack and Notion alternative that puts you in control of your data

CommaFeedCommaFeed is an open-source feed reader and news aggregator, designed to be lightweight and extensible, with PostgreSQL as its database.

### On this page

ConfigurationBase64LinksTags