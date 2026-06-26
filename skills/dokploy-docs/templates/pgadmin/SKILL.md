---
title: "pgAdmin | Dokploy"
source: "https://docs.dokploy.com/docs/templates/pgadmin"
category: dokploy-docs
created: "2026-06-25T17:21:56.647Z"
---

pgAdmin | Dokploy

# pgAdmin

Copy as Markdown

pgAdmin is the most popular and feature rich Open Source administration and development platform for PostgreSQL, the most advanced Open Source database in the world.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  pgadmin:
    image: dpage/pgadmin4:latest
    restart: unless-stopped
    environment:
      - PGADMIN_DEFAULT_EMAIL=${PGADMIN_DEFAULT_EMAIL}
      - PGADMIN_DEFAULT_PASSWORD=${PGADMIN_DEFAULT_PASSWORD}
      - PGADMIN_CONFIG_SERVER_MODE=False
      - PGADMIN_CONFIG_MASTER_PASSWORD_REQUIRED=False
    volumes:
      - pgadmin-data:/var/lib/pgadmin

volumes:
  pgadmin-data:
```

```
[variables]
main_domain = "${domain}"
admin_email = "[email protected]"
admin_password = "${password:16}"

[config]
[[config.domains]]
serviceName = "pgadmin"
port = 80
host = "${main_domain}"

[config.env]
PGADMIN_DEFAULT_EMAIL = "${admin_email}"
PGADMIN_DEFAULT_PASSWORD = "${admin_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBwZ2FkbWluOlxuICAgIGltYWdlOiBkcGFnZS9wZ2FkbWluNDpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQR0FETUlOX0RFRkFVTFRfRU1BSUw9JHtQR0FETUlOX0RFRkFVTFRfRU1BSUx9XG4gICAgICAtIFBHQURNSU5fREVGQVVMVF9QQVNTV09SRD0ke1BHQURNSU5fREVGQVVMVF9QQVNTV09SRH1cbiAgICAgIC0gUEdBRE1JTl9DT05GSUdfU0VSVkVSX01PREU9RmFsc2VcbiAgICAgIC0gUEdBRE1JTl9DT05GSUdfTUFTVEVSX1BBU1NXT1JEX1JFUVVJUkVEPUZhbHNlXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcGdhZG1pbi1kYXRhOi92YXIvbGliL3BnYWRtaW5cblxudm9sdW1lczpcbiAgcGdhZG1pbi1kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmFkbWluX2VtYWlsID0gXCJ1c2VyQGV4YW1wbGUuY29tXCJcbmFkbWluX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJwZ2FkbWluXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblBHQURNSU5fREVGQVVMVF9FTUFJTCA9IFwiJHthZG1pbl9lbWFpbH1cIlxuUEdBRE1JTl9ERUZBVUxUX1BBU1NXT1JEID0gXCIke2FkbWluX3Bhc3N3b3JkfVwiXG5cbiIKfQ==
```

## Links

`database`,`postgres`,`admin`

---

Version:`8.3`

PeppermintPeppermint is a modern, open-source API development platform that helps you build, test and document your APIs.

PhotoprismPhotoPrism® is an AI-Powered Photos App for the Decentralized Web. It makes use of the latest technologies to tag and find pictures automatically without getting in your way.

### On this page

ConfigurationBase64LinksTags