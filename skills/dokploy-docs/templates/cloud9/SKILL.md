---
title: "Cloud9 | Dokploy"
source: "https://docs.dokploy.com/docs/templates/cloud9"
category: dokploy-docs
created: "2026-06-25T17:21:43.965Z"
---

Cloud9 | Dokploy

# Cloud9

Copy as Markdown

Cloud9 is a cloud-based integrated development environment (IDE) designed for developers to code, build, and debug applications collaboratively in real time.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  cloud9:
    image: lscr.io/linuxserver/cloud9:1.29.2
    ports:
      - "8000"
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
      - GITURL=https://github.com/linuxserver/docker-cloud9.git
      - USERNAME=${USERNAME}
      - PASSWORD=${PASSWORD}
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - code:/code

volumes:
  code:
```

```
[variables]
USERNAME = "user"
PASSWORD = "${password:16}"

[config]
[[config.domains]]
serviceName = "cloud9"
port = 8000
host = "${domain}"

[config.env]
USERNAME = "${USERNAME}"
PASSWORD = "${PASSWORD}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBjbG91ZDk6XG4gICAgaW1hZ2U6IGxzY3IuaW8vbGludXhzZXJ2ZXIvY2xvdWQ5OjEuMjkuMlxuICAgIHBvcnRzOlxuICAgICAgLSBcIjgwMDBcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQVUlEPTEwMDBcbiAgICAgIC0gUEdJRD0xMDAwXG4gICAgICAtIFRaPUV1cm9wZS9Mb25kb25cbiAgICAgIC0gR0lUVVJMPWh0dHBzOi8vZ2l0aHViLmNvbS9saW51eHNlcnZlci9kb2NrZXItY2xvdWQ5LmdpdFxuICAgICAgLSBVU0VSTkFNRT0ke1VTRVJOQU1FfVxuICAgICAgLSBQQVNTV09SRD0ke1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIC92YXIvcnVuL2RvY2tlci5zb2NrOi92YXIvcnVuL2RvY2tlci5zb2NrXG4gICAgICAtIGNvZGU6L2NvZGVcblxudm9sdW1lczpcbiAgY29kZTogIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5VU0VSTkFNRSA9IFwidXNlclwiXG5QQVNTV09SRCA9IFwiJHtwYXNzd29yZDoxNn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY2xvdWQ5XCJcbnBvcnQgPSA4MDAwXG5ob3N0ID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblVTRVJOQU1FID0gXCIke1VTRVJOQU1FfVwiXG5QQVNTV09SRCA9IFwiJHtQQVNTV09SRH1cIiAiCn0=
```

## Links

`ide`,`development`,`cloud`

---

Version:`1.29.2`

ClickHouseClickHouse is an open-source column-oriented DBMS (columnar database management system) for online analytical processing (OLAP) that allows users to generate analytical reports using SQL queries in real-time. ClickHouse works 100-1000x faster than traditional database management systems, and processes hundreds of millions to over a billion rows and tens of gigabytes of data per server per second.

Cloud CommanderCloud Commander is a file manager for the web. It includes a command-line console and a text editor. Cloud Commander helps you manage your server and work with files, directories and programs in a web browser.

### On this page

ConfigurationBase64LinksTags