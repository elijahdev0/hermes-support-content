---
title: "BookStack | Dokploy"
source: "https://docs.dokploy.com/docs/templates/bookstack"
category: dokploy-docs
created: "2026-06-25T17:21:42.677Z"
---

BookStack | Dokploy

# BookStack

Copy as Markdown

BookStack is a self-hosted platform for creating beautiful, feature-rich documentation sites.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  bookstack:
    image: lscr.io/linuxserver/bookstack:24.12.1
    restart: unless-stopped
    ports:
      - 80
    environment:
      - PUID=1000
      - PGID=1000
      - APP_URL=http://${DOMAIN}
      - DB_HOST=bookstack-db
      - DB_USERNAME=mariadb
      - DB_PASSWORD=${DB_PASSWORD}
      - DB_DATABASE=bookstack
      - APP_KEY=${APP_KEY}
    volumes:
      - config:/config
    depends_on:
      - bookstack-db

  bookstack-db:
    image: mariadb:10.11
    restart: unless-stopped
    environment:
      - MYSQL_ROOT_PASSWORD=${DB_PASSWORD}
      - MYSQL_DATABASE=bookstack
      - MYSQL_USER=mariadb
      - MYSQL_PASSWORD=${DB_PASSWORD}
    volumes:
      - db_data:/var/lib/mysql

volumes:
  config: {}
  db_data: {}
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:16}"
app_key = "${password:32}"

[config]
[[config.domains]]
serviceName = "bookstack"
port = 80
host = "${main_domain}"

[config.env]
DOMAIN = "${main_domain}"
DB_PASSWORD = "${db_password}"
APP_KEY = "${app_key}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBib29rc3RhY2s6XG4gICAgaW1hZ2U6IGxzY3IuaW8vbGludXhzZXJ2ZXIvYm9va3N0YWNrOjI0LjEyLjFcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSA4MFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQVUlEPTEwMDBcbiAgICAgIC0gUEdJRD0xMDAwXG4gICAgICAtIEFQUF9VUkw9aHR0cDovLyR7RE9NQUlOfVxuICAgICAgLSBEQl9IT1NUPWJvb2tzdGFjay1kYlxuICAgICAgLSBEQl9VU0VSTkFNRT1tYXJpYWRiXG4gICAgICAtIERCX1BBU1NXT1JEPSR7REJfUEFTU1dPUkR9XG4gICAgICAtIERCX0RBVEFCQVNFPWJvb2tzdGFja1xuICAgICAgLSBBUFBfS0VZPSR7QVBQX0tFWX1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBjb25maWc6L2NvbmZpZ1xuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGJvb2tzdGFjay1kYlxuXG4gIGJvb2tzdGFjay1kYjpcbiAgICBpbWFnZTogbWFyaWFkYjoxMC4xMVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE1ZU1FMX1JPT1RfUEFTU1dPUkQ9JHtEQl9QQVNTV09SRH1cbiAgICAgIC0gTVlTUUxfREFUQUJBU0U9Ym9va3N0YWNrXG4gICAgICAtIE1ZU1FMX1VTRVI9bWFyaWFkYlxuICAgICAgLSBNWVNRTF9QQVNTV09SRD0ke0RCX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRiX2RhdGE6L3Zhci9saWIvbXlzcWxcblxudm9sdW1lczpcbiAgY29uZmlnOiB7fVxuICBkYl9kYXRhOiB7fSAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbmFwcF9rZXkgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImJvb2tzdGFja1wiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5ET01BSU4gPSBcIiR7bWFpbl9kb21haW59XCJcbkRCX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiXG5BUFBfS0VZID0gXCIke2FwcF9rZXl9XCIgIgp9
```

## Links

`documentation`,`self-hosted`

---

Version:`24.12.1`

BookloreBooklore is an application for managing and serving book-related data, backed by a MariaDB database.

BorgitoryA web interface for managing BorgBackup archives. Allows browsing, mounting (via FUSE), and handling backup repositories.

### On this page

ConfigurationBase64LinksTags