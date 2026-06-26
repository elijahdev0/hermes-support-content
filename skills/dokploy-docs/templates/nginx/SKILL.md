---
title: "Nginx | Dokploy"
source: "https://docs.dokploy.com/docs/templates/nginx"
category: dokploy-docs
created: "2026-06-25T17:21:54.354Z"
---

Nginx | Dokploy

# Nginx

Copy as Markdown

Nginx is an High performance web server

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  nginx:
    image: nginx:latest
    restart: unless-stopped
    ports:
      - 80
      - 443
    volumes:
      - nginx-config:/etc/nginx
      - nginx-html:/usr/share/nginx/html
volumes:
  nginx-config: {}
  nginx-html: {}
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "nginx"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBuZ2lueDpcbiAgICBpbWFnZTogbmdpbng6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gODBcbiAgICAgIC0gNDQzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gbmdpbngtY29uZmlnOi9ldGMvbmdpbnhcbiAgICAgIC0gbmdpbngtaHRtbDovdXNyL3NoYXJlL25naW54L2h0bWxcbnZvbHVtZXM6XG4gIG5naW54LWNvbmZpZzoge31cbiAgbmdpbngtaHRtbDoge30iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0ge31cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIm5naW54XCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`webserver`

---

Version:`latest`

NextcloudNextcloud is a self-hosted file storage and sync platform with powerful collaboration capabilities. It integrates Files, Talk, Groupware, Office, Assistant and more into a single platform for remote work and data protection.

NocoDBNocoDB is an opensource Airtable alternative that turns any MySQL, PostgreSQL, SQL Server, SQLite & MariaDB into a smart spreadsheet.

### On this page

ConfigurationBase64LinksTags