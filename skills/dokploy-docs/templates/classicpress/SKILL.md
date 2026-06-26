---
title: "ClassicPress | Dokploy"
source: "https://docs.dokploy.com/docs/templates/classicpress"
category: dokploy-docs
created: "2026-06-25T17:21:43.964Z"
---

ClassicPress | Dokploy

# ClassicPress

Copy as Markdown

ClassicPress is a community-led open source content management system for creators. It is a fork of WordPress 6.2 that preserves the TinyMCE classic editor as the default option.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  classicpress:
    image: classicpress/classicpress:php8.3-apache
    ports:
      - "80"
    environment:
      - WORDPRESS_DB_HOST=db
      - WORDPRESS_DB_USER=wordpress
      - WORDPRESS_DB_PASSWORD=${DB_PASSWORD}
      - WORDPRESS_DB_NAME=wordpress
    volumes:
      - wordpress-data:/var/www/html
    depends_on:
      - db

  db:
    image: mariadb:10.6
    environment:
      - MYSQL_DATABASE=wordpress
      - MYSQL_USER=wordpress
      - MYSQL_PASSWORD=${DB_PASSWORD}
      - MYSQL_ROOT_PASSWORD=${DB_ROOT_PASSWORD}
    volumes:
      - db-data:/var/lib/mysql

volumes:
  wordpress-data:
  db-data:
```

```
[variables]
DB_PASSWORD = "${password:16}"
DB_ROOT_PASSWORD = "${password:16}"

[config]
[[config.domains]]
serviceName = "classicpress"
port = 80
host = "${domain}"

[config.env]
DB_PASSWORD = "${DB_PASSWORD}"
DB_ROOT_PASSWORD = "${DB_ROOT_PASSWORD}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBjbGFzc2ljcHJlc3M6XG4gICAgaW1hZ2U6IGNsYXNzaWNwcmVzcy9jbGFzc2ljcHJlc3M6cGhwOC4zLWFwYWNoZVxuICAgIHBvcnRzOlxuICAgICAgLSBcIjgwXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gV09SRFBSRVNTX0RCX0hPU1Q9ZGJcbiAgICAgIC0gV09SRFBSRVNTX0RCX1VTRVI9d29yZHByZXNzXG4gICAgICAtIFdPUkRQUkVTU19EQl9QQVNTV09SRD0ke0RCX1BBU1NXT1JEfVxuICAgICAgLSBXT1JEUFJFU1NfREJfTkFNRT13b3JkcHJlc3NcbiAgICB2b2x1bWVzOlxuICAgICAgLSB3b3JkcHJlc3MtZGF0YTovdmFyL3d3dy9odG1sXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gZGJcblxuICBkYjpcbiAgICBpbWFnZTogbWFyaWFkYjoxMC42XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE1ZU1FMX0RBVEFCQVNFPXdvcmRwcmVzc1xuICAgICAgLSBNWVNRTF9VU0VSPXdvcmRwcmVzc1xuICAgICAgLSBNWVNRTF9QQVNTV09SRD0ke0RCX1BBU1NXT1JEfVxuICAgICAgLSBNWVNRTF9ST09UX1BBU1NXT1JEPSR7REJfUk9PVF9QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYi1kYXRhOi92YXIvbGliL215c3FsXG5cbnZvbHVtZXM6XG4gIHdvcmRwcmVzcy1kYXRhOlxuICBkYi1kYXRhOiAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbkRCX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5EQl9ST09UX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjbGFzc2ljcHJlc3NcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkRCX1BBU1NXT1JEID0gXCIke0RCX1BBU1NXT1JEfVwiXG5EQl9ST09UX1BBU1NXT1JEID0gXCIke0RCX1JPT1RfUEFTU1dPUkR9XCIgIgp9
```

## Links

`cms`,`wordpress`,`content-management`

---

Version:`php8.3-apache`

ChromiumChromium is an open-source browser project that is designed to provide a safer, faster, and more stable way for all users to experience the web in a containerized environment.

ClickHouseClickHouse is an open-source column-oriented DBMS (columnar database management system) for online analytical processing (OLAP) that allows users to generate analytical reports using SQL queries in real-time. ClickHouse works 100-1000x faster than traditional database management systems, and processes hundreds of millions to over a billion rows and tens of gigabytes of data per server per second.

### On this page

ConfigurationBase64LinksTags