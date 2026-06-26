---
title: "Odoo | Dokploy"
source: "https://docs.dokploy.com/docs/templates/odoo_18"
category: dokploy-docs
created: "2026-06-25T17:21:54.355Z"
---

Odoo | Dokploy

# Odoo

Copy as Markdown

Odoo is a free and open source business management software that helps you manage your company's operations.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  web:
    image: odoo:18.0
    depends_on:
      - db
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ../files/config:/etc/odoo
      - ../files/addons:/mnt/extra-addons

  db:
    image: postgres:17
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
    volumes:
      - odoo-db-data:/var/lib/postgresql/data

volumes:
  odoo-web-data:
  odoo-db-data:
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "web"
port = 8_069
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB3ZWI6XG4gICAgaW1hZ2U6IG9kb286MTguMFxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGRiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIEhPU1Q9ZGJcbiAgICAgIC0gVVNFUj1vZG9vXG4gICAgICAtIFBBU1NXT1JEPW9kb29cbiAgICB2b2x1bWVzOlxuICAgICAgLSBvZG9vLXdlYi1kYXRhOi92YXIvbGliL29kb29cbiAgICAgIC0gLi4vZmlsZXMvY29uZmlnOi9ldGMvb2Rvb1xuICAgICAgLSAuLi9maWxlcy9hZGRvbnM6L21udC9leHRyYS1hZGRvbnNcblxuICBkYjpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTdcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfREI9cG9zdGdyZXNcbiAgICAgIC0gUE9TVEdSRVNfVVNFUj1vZG9vXG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPW9kb29cbiAgICB2b2x1bWVzOlxuICAgICAgLSBvZG9vLWRiLWRhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG5cbnZvbHVtZXM6XG4gIG9kb28td2ViLWRhdGE6XG4gIG9kb28tZGItZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSB7fVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwid2ViXCJcbnBvcnQgPSA4XzA2OVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`erp`

---

Version:`18.0`

OdooOdoo is a free and open source business management software that helps you manage your company's operations.

OdooOdoo is a free and open source business management software that helps you manage your company's operations.

### On this page

ConfigurationBase64LinksTags