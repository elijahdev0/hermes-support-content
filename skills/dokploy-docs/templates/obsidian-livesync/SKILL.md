---
title: "Obsidian LiveSync | Dokploy"
source: "https://docs.dokploy.com/docs/templates/obsidian-livesync"
category: dokploy-docs
created: "2026-06-25T17:21:54.355Z"
---

Obsidian LiveSync | Dokploy

# Obsidian LiveSync

Copy as Markdown

Obsidian LiveSync with CouchDB for real-time note synchronization.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  couchdb:
    image: couchdb:latest
    user: "0:0"
    environment:
      - COUCHDB_USER=${COUCHDB_USER}
      - COUCHDB_PASSWORD=${COUCHDB_PASSWORD}
    volumes:
      - couchdb-data:/opt/couchdb/data
      - ../files/local.ini:/opt/couchdb/etc/local.ini
    ports:
      - 5984

volumes:
  couchdb-data: {}
```

```
[variables]
main_domain = "${domain}"
COUCHDB_USER = "${username}"
COUCHDB_PASSWORD = "${password:32}"

[config]
[[config.domains]]
serviceName = "couchdb"
port = 5984
host = "${main_domain}"

[config.env]
COUCHDB_USER = "${COUCHDB_USER}"
# Defines the password for the CouchDB admin user. Treat this like an API key.
COUCHDB_PASSWORD = "${COUCHDB_PASSWORD}"

[[config.mounts]]
filePath = "local.ini"
content = """
[couchdb]
single_node = true
max_document_size = 50000000

[httpd]
WWW-Authenticate = Basic realm="couchdb"
enable_cors = true

[chttpd]
bind_address = 0.0.0.0
enable_cors = true
require_valid_user = true
max_http_request_size = 4294967296

[cors]
credentials = true
origins = app://obsidian.md,capacitor://localhost,http://localhost,
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBjb3VjaGRiOlxuICAgIGltYWdlOiBjb3VjaGRiOmxhdGVzdFxuICAgIHVzZXI6IFwiMDowXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQ09VQ0hEQl9VU0VSPSR7Q09VQ0hEQl9VU0VSfVxuICAgICAgLSBDT1VDSERCX1BBU1NXT1JEPSR7Q09VQ0hEQl9QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBjb3VjaGRiLWRhdGE6L29wdC9jb3VjaGRiL2RhdGFcbiAgICAgIC0gLi4vZmlsZXMvbG9jYWwuaW5pOi9vcHQvY291Y2hkYi9ldGMvbG9jYWwuaW5pXG4gICAgcG9ydHM6XG4gICAgICAtIDU5ODRcblxudm9sdW1lczpcbiAgY291Y2hkYi1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbkNPVUNIREJfVVNFUiA9IFwiJHt1c2VybmFtZX1cIlxuQ09VQ0hEQl9QQVNTV09SRCA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY291Y2hkYlwiXG5wb3J0ID0gNTk4NFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkNPVUNIREJfVVNFUiA9IFwiJHtDT1VDSERCX1VTRVJ9XCJcbiMgRGVmaW5lcyB0aGUgcGFzc3dvcmQgZm9yIHRoZSBDb3VjaERCIGFkbWluIHVzZXIuIFRyZWF0IHRoaXMgbGlrZSBhbiBBUEkga2V5LlxuQ09VQ0hEQl9QQVNTV09SRCA9IFwiJHtDT1VDSERCX1BBU1NXT1JEfVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwibG9jYWwuaW5pXCJcbmNvbnRlbnQgPSBcIlwiXCJcbltjb3VjaGRiXVxuc2luZ2xlX25vZGUgPSB0cnVlXG5tYXhfZG9jdW1lbnRfc2l6ZSA9IDUwMDAwMDAwXG5cbltodHRwZF1cbldXVy1BdXRoZW50aWNhdGUgPSBCYXNpYyByZWFsbT1cImNvdWNoZGJcIlxuZW5hYmxlX2NvcnMgPSB0cnVlXG5cbltjaHR0cGRdXG5iaW5kX2FkZHJlc3MgPSAwLjAuMC4wXG5lbmFibGVfY29ycyA9IHRydWVcbnJlcXVpcmVfdmFsaWRfdXNlciA9IHRydWVcbm1heF9odHRwX3JlcXVlc3Rfc2l6ZSA9IDQyOTQ5NjcyOTZcblxuW2NvcnNdXG5jcmVkZW50aWFscyA9IHRydWVcbm9yaWdpbnMgPSBhcHA6Ly9vYnNpZGlhbi5tZCxjYXBhY2l0b3I6Ly9sb2NhbGhvc3QsaHR0cDovL2xvY2FsaG9zdCxcblwiXCJcIlxuIgp9
```

## Links

`database`,`sync`,`obsidian`

---

Version:`latest`

NTFYntfy lets you send push notifications to your phone or desktop via scripts from any computer, using simple HTTP PUT or POST requests.

OdooOdoo is a free and open source business management software that helps you manage your company's operations.

### On this page

ConfigurationBase64LinksTags