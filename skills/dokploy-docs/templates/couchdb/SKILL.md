---
title: "CouchDB | Dokploy"
source: "https://docs.dokploy.com/docs/templates/couchdb"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

CouchDB | Dokploy

# CouchDB

Copy as Markdown

CouchDB is a document-oriented NoSQL database that excels at replication and horizontal scaling.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  couchdb:
    image: couchdb:latest
    ports:
      - '5984'
    volumes:
      - couchdb-data:/opt/couchdb/data
    environment:
      - COUCHDB_USER=${COUCHDB_USER}
      - COUCHDB_PASSWORD=${COUCHDB_PASSWORD}
    restart: unless-stopped

volumes:
  couchdb-data:
    driver: local
```

```
[variables]
main_domain = "${domain}"
username = "${password:16}"
password = "${password:32}"

[config]
env = ["COUCHDB_USER=${username}", "COUCHDB_PASSWORD=${password}"]
mounts = []

[[config.domains]]
serviceName = "couchdb"
port = 5_984
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBjb3VjaGRiOlxuICAgIGltYWdlOiBjb3VjaGRiOmxhdGVzdFxuICAgIHBvcnRzOlxuICAgICAgLSAnNTk4NCdcbiAgICB2b2x1bWVzOlxuICAgICAgLSBjb3VjaGRiLWRhdGE6L29wdC9jb3VjaGRiL2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQ09VQ0hEQl9VU0VSPSR7Q09VQ0hEQl9VU0VSfVxuICAgICAgLSBDT1VDSERCX1BBU1NXT1JEPSR7Q09VQ0hEQl9QQVNTV09SRH1cbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG52b2x1bWVzOlxuICBjb3VjaGRiLWRhdGE6XG4gICAgZHJpdmVyOiBsb2NhbFxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnVzZXJuYW1lID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1wiQ09VQ0hEQl9VU0VSPSR7dXNlcm5hbWV9XCIsIFwiQ09VQ0hEQl9QQVNTV09SRD0ke3Bhc3N3b3JkfVwiXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY291Y2hkYlwiXG5wb3J0ID0gNV85ODRcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`database`,`storage`

---

Version:`latest`

CoralCoral is a revolutionary commenting platform designed to enhance website interactions. It features smart technology for meaningful discussions, journalist identification, moderation tools with AI support, and complete data control without ads or trackers. Used by major news sites worldwide.

Crawl4AICrawl4AI is a modern AI-powered web crawler with support for screenshots, PDFs, JavaScript execution, and LLM-based extraction. Includes an interactive playground and MCP (Model Context Protocol) integration.

### On this page

ConfigurationBase64LinksTags