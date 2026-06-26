---
title: "Phpmyadmin | Dokploy"
source: "https://docs.dokploy.com/docs/templates/phpmyadmin"
category: dokploy-docs
created: "2026-06-25T17:21:56.647Z"
---

Phpmyadmin | Dokploy

# Phpmyadmin

Copy as Markdown

Phpmyadmin is a free and open-source web interface for MySQL and MariaDB that allows you to manage your databases.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: tu_base_de_datos
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    volumes:
      - db_data:/var/lib/mysql

  phpmyadmin:
    image: phpmyadmin/phpmyadmin:5.2.1
    environment:
      PMA_HOST: db
      PMA_USER: ${MYSQL_USER}
      PMA_PASSWORD: ${MYSQL_PASSWORD}
      PMA_ARBITRARY: 1
    depends_on:
      - db

volumes:
  db_data:
    driver: local
```

```
[variables]
main_domain = "${domain}"
root_password = "${password:32}"
user_password = "${password:32}"

[config]
mounts = []

[[config.domains]]
serviceName = "phpmyadmin"
port = 80
host = "${main_domain}"

[config.env]
MYSQL_ROOT_PASSWORD = "${root_password}"
MYSQL_DATABASE = "mysql"
MYSQL_USER = "phpmyadmin"
MYSQL_PASSWORD = "${user_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGRiOlxuICAgIGltYWdlOiBteXNxbDo1LjdcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE1ZU1FMX1JPT1RfUEFTU1dPUkQ6ICR7TVlTUUxfUk9PVF9QQVNTV09SRH1cbiAgICAgIE1ZU1FMX0RBVEFCQVNFOiB0dV9iYXNlX2RlX2RhdG9zXG4gICAgICBNWVNRTF9VU0VSOiAke01ZU1FMX1VTRVJ9XG4gICAgICBNWVNRTF9QQVNTV09SRDogJHtNWVNRTF9QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYl9kYXRhOi92YXIvbGliL215c3FsXG5cblxuICBwaHBteWFkbWluOlxuICAgIGltYWdlOiBwaHBteWFkbWluL3BocG15YWRtaW46NS4yLjFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBNQV9IT1NUOiBkYlxuICAgICAgUE1BX1VTRVI6ICR7TVlTUUxfVVNFUn1cbiAgICAgIFBNQV9QQVNTV09SRDogJHtNWVNRTF9QQVNTV09SRH1cbiAgICAgIFBNQV9BUkJJVFJBUlk6IDFcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBkYlxuXG52b2x1bWVzOlxuICBkYl9kYXRhOlxuICAgIGRyaXZlcjogbG9jYWxcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5yb290X3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG51c2VyX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJwaHBteWFkbWluXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbk1ZU1FMX1JPT1RfUEFTU1dPUkQgPSBcIiR7cm9vdF9wYXNzd29yZH1cIlxuTVlTUUxfREFUQUJBU0UgPSBcIm15c3FsXCJcbk1ZU1FMX1VTRVIgPSBcInBocG15YWRtaW5cIlxuTVlTUUxfUEFTU1dPUkQgPSBcIiR7dXNlcl9wYXNzd29yZH1cIlxuIgp9
```

## Links

`database`

---

Version:`5.2.1`

PhotoprismPhotoPrism® is an AI-Powered Photos App for the Decentralized Web. It makes use of the latest technologies to tag and find pictures automatically without getting in your way.

PicsurPicsur is a simple, self-hosted image hosting service with an admin interface and Postgres backend.

### On this page

ConfigurationBase64LinksTags