---
title: "Chevereto | Dokploy"
source: "https://docs.dokploy.com/docs/templates/chevereto"
category: dokploy-docs
created: "2026-06-25T17:21:43.962Z"
---

Chevereto | Dokploy

# Chevereto

Copy as Markdown

Chevereto is a powerful, self-hosted image and video hosting platform designed for individuals, communities, and businesses. It allows users to upload, organize, and share media effortlessly.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  chevereto:
    image: chevereto/chevereto:4
    restart: unless-stopped
    environment:
      - CHEVERETO_DB_HOST=mysql
      - CHEVERETO_DB_USER=mysql
      - CHEVERETO_DB_PASS=${DB_PASSWORD}
      - CHEVERETO_DB_PORT=3306
      - CHEVERETO_DB_NAME=chevereto
      - CHEVERETO_HOSTNAME=${DOMAIN}
      - CHEVERETO_HOSTNAME_PATH=/
      - CHEVERETO_HTTPS=0
      - CHEVERETO_MAX_POST_SIZE=2G
      - CHEVERETO_MAX_UPLOAD_SIZE=2G
    ports:
      - 80
    volumes:
      - storage:/var/www/html/images/
    depends_on:
      - mysql

  mysql:
    image: mysql:8
    restart: unless-stopped
    environment:
      - MYSQL_ROOT_PASSWORD=${DB_PASSWORD}
      - MYSQL_DATABASE=chevereto
      - MYSQL_USER=mysql
      - MYSQL_PASSWORD=${DB_PASSWORD}
    volumes:
      - mysql:/var/lib/mysql

volumes:
  storage:
  mysql:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:16}"

[config]
[[config.domains]]
serviceName = "chevereto"
port = 80
host = "${main_domain}"

[config.env]
DB_PASSWORD = "${db_password}"
DOMAIN = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBjaGV2ZXJldG86XG4gICAgaW1hZ2U6IGNoZXZlcmV0by9jaGV2ZXJldG86NFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIENIRVZFUkVUT19EQl9IT1NUPW15c3FsXG4gICAgICAtIENIRVZFUkVUT19EQl9VU0VSPW15c3FsXG4gICAgICAtIENIRVZFUkVUT19EQl9QQVNTPSR7REJfUEFTU1dPUkR9XG4gICAgICAtIENIRVZFUkVUT19EQl9QT1JUPTMzMDZcbiAgICAgIC0gQ0hFVkVSRVRPX0RCX05BTUU9Y2hldmVyZXRvXG4gICAgICAtIENIRVZFUkVUT19IT1NUTkFNRT0ke0RPTUFJTn1cbiAgICAgIC0gQ0hFVkVSRVRPX0hPU1ROQU1FX1BBVEg9L1xuICAgICAgLSBDSEVWRVJFVE9fSFRUUFM9MFxuICAgICAgLSBDSEVWRVJFVE9fTUFYX1BPU1RfU0laRT0yR1xuICAgICAgLSBDSEVWRVJFVE9fTUFYX1VQTE9BRF9TSVpFPTJHXG4gICAgcG9ydHM6XG4gICAgICAtIDgwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gc3RvcmFnZTovdmFyL3d3dy9odG1sL2ltYWdlcy9cbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBteXNxbFxuXG4gIG15c3FsOlxuICAgIGltYWdlOiBteXNxbDo4XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTVlTUUxfUk9PVF9QQVNTV09SRD0ke0RCX1BBU1NXT1JEfVxuICAgICAgLSBNWVNRTF9EQVRBQkFTRT1jaGV2ZXJldG9cbiAgICAgIC0gTVlTUUxfVVNFUj1teXNxbFxuICAgICAgLSBNWVNRTF9QQVNTV09SRD0ke0RCX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIG15c3FsOi92YXIvbGliL215c3FsXG5cbnZvbHVtZXM6XG4gIHN0b3JhZ2U6XG4gIG15c3FsOiAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImNoZXZlcmV0b1wiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5EQl9QQVNTV09SRCA9IFwiJHtkYl9wYXNzd29yZH1cIlxuRE9NQUlOID0gXCIke21haW5fZG9tYWlufVwiICIKfQ==
```

## Links

`Image Hosting`,`File Management`,`Open Source`,`Multi-User`,`Private Albums`

---

Version:`4`

CheckmateCheckmate is an open-source, self-hosted tool designed to track and monitor server hardware, uptime, response times, and incidents in real-time with beautiful visualizations.

ChibisafeA beautiful and performant vault to save all your files in the cloud.

### On this page

ConfigurationBase64LinksTags