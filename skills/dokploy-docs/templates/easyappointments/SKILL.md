---
title: "Easy!Appointments | Dokploy"
source: "https://docs.dokploy.com/docs/templates/easyappointments"
category: dokploy-docs
created: "2026-06-25T17:21:47.358Z"
---

Easy!Appointments | Dokploy

# Easy!Appointments

Copy as Markdown

Easy!Appointments is a highly customizable web application that allows customers to book appointments with you via a sophisticated web interface.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  easyappointments:
    image: alextselegidis/easyappointments:1.5.0
    restart: unless-stopped
    environment:
      - BASE_URL=http://${DOMAIN}
      - DB_HOST=mysql
      - DB_NAME=easyappointments
      - DB_USERNAME=root
      - DB_PASSWORD=${DB_PASSWORD}
    volumes:
      - easyappointments:/var/www/html
    depends_on:
      - mysql

  mysql:
    image: mysql:8.0
    restart: unless-stopped
    environment:
      - MYSQL_ROOT_PASSWORD=${DB_PASSWORD}
      - MYSQL_DATABASE=easyappointments
    volumes:
      - mysql:/var/lib/mysql

volumes:
  easyappointments:
  mysql:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "easyappointments"
port = 80
host = "${main_domain}"

[config.env]
DOMAIN = "${main_domain}"
DB_PASSWORD = "${db_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGVhc3lhcHBvaW50bWVudHM6XG4gICAgaW1hZ2U6IGFsZXh0c2VsZWdpZGlzL2Vhc3lhcHBvaW50bWVudHM6MS41LjBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBCQVNFX1VSTD1odHRwOi8vJHtET01BSU59XG4gICAgICAtIERCX0hPU1Q9bXlzcWxcbiAgICAgIC0gREJfTkFNRT1lYXN5YXBwb2ludG1lbnRzXG4gICAgICAtIERCX1VTRVJOQU1FPXJvb3RcbiAgICAgIC0gREJfUEFTU1dPUkQ9JHtEQl9QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBlYXN5YXBwb2ludG1lbnRzOi92YXIvd3d3L2h0bWxcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBteXNxbFxuXG4gIG15c3FsOlxuICAgIGltYWdlOiBteXNxbDo4LjBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBNWVNRTF9ST09UX1BBU1NXT1JEPSR7REJfUEFTU1dPUkR9XG4gICAgICAtIE1ZU1FMX0RBVEFCQVNFPWVhc3lhcHBvaW50bWVudHNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBteXNxbDovdmFyL2xpYi9teXNxbFxuXG52b2x1bWVzOlxuICBlYXN5YXBwb2ludG1lbnRzOlxuICBteXNxbDpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5kYl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZWFzeWFwcG9pbnRtZW50c1wiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5ET01BSU4gPSBcIiR7bWFpbl9kb21haW59XCJcbkRCX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiXG4iCn0=
```

## Links

`scheduling`,`appointments`,`booking`

---

Version:`1.5.0`

DumbPadDumbPad is a simple, self-hosted notepad service with PIN protection and no database required.

ElasticsearchElasticsearch is an open-source search and analytics engine, used for full-text search and analytics on structured data such as text, web pages, images, and videos.

### On this page

ConfigurationBase64LinksTags