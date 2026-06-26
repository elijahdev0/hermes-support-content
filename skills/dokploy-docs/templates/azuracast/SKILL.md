---
title: "AzuraCast | Dokploy"
source: "https://docs.dokploy.com/docs/templates/azuracast"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

AzuraCast | Dokploy

# AzuraCast

Copy as Markdown

AzuraCast is a self-hosted, all-in-one web radio management suite. Easily manage your online radio stations with a powerful web interface.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  azuracast:
    image: ghcr.io/azuracast/azuracast:latest
    restart: unless-stopped
    ports:
      - 80
    volumes:
      - azuracast-station-data:/var/azuracast/stations
      - azuracast-data:/var/azuracast/www_tmp
      - azuracast-uploads:/var/azuracast/uploads
      - azuracast-backups:/var/azuracast/backups
    environment:
      - LANG=en_US.UTF-8
      - AZURACAST_DC_REVISION=1
      - MYSQL_HOST=mariadb
      - MYSQL_PORT=3306
      - MYSQL_USER=azuracast
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}
      - MYSQL_DATABASE=azuracast
    depends_on:
      - mariadb

  mariadb:
    image: mariadb:11.4
    restart: unless-stopped
    volumes:
      - mariadb-data:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
      - MYSQL_DATABASE=azuracast
      - MYSQL_USER=azuracast
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}

volumes:
  azuracast-station-data: {}
  azuracast-data: {}
  azuracast-uploads: {}
  azuracast-backups: {}
  mariadb-data: {}
```

```
[variables]
main_domain = "${domain}"
mysql_root_password = "${password:32}"
mysql_password = "${password:16}"

[config]
[[config.domains]]
serviceName = "azuracast"
port = 80
host = "${main_domain}"

[config.env]
LANG = "en_US.UTF-8"
AZURACAST_DC_REVISION = "1"
MYSQL_HOST = "mariadb"
MYSQL_PORT = "3306"
MYSQL_USER = "azuracast"
MYSQL_PASSWORD = "${mysql_password}"
MYSQL_DATABASE = "azuracast"
MYSQL_ROOT_PASSWORD = "${mysql_root_password}"
LETSENCRYPT_HOST = "${main_domain}"
VIRTUAL_HOST = "${main_domain}"
DISABLE_LETSENCRYPT = "true"
AUTO_ASSIGN_PORT_HTTP = "80"
AUTO_ASSIGN_PORT_HTTPS = "443"
NGINX_RADIO_PORTS = "8000,8010,8020,8030,8040,8050"
PREFER_RELEASE_BUILDS = "true"
COMPOSER_PLUGIN_MODE = "false"
ADDITIONAL_MEDIA_SYNC_WORKER_COUNT = "0"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBhenVyYWNhc3Q6XG4gICAgaW1hZ2U6IGdoY3IuaW8vYXp1cmFjYXN0L2F6dXJhY2FzdDpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSA4MFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGF6dXJhY2FzdC1zdGF0aW9uLWRhdGE6L3Zhci9henVyYWNhc3Qvc3RhdGlvbnNcbiAgICAgIC0gYXp1cmFjYXN0LWRhdGE6L3Zhci9henVyYWNhc3Qvd3d3X3RtcFxuICAgICAgLSBhenVyYWNhc3QtdXBsb2FkczovdmFyL2F6dXJhY2FzdC91cGxvYWRzXG4gICAgICAtIGF6dXJhY2FzdC1iYWNrdXBzOi92YXIvYXp1cmFjYXN0L2JhY2t1cHNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTEFORz1lbl9VUy5VVEYtOFxuICAgICAgLSBBWlVSQUNBU1RfRENfUkVWSVNJT049MVxuICAgICAgLSBNWVNRTF9IT1NUPW1hcmlhZGJcbiAgICAgIC0gTVlTUUxfUE9SVD0zMzA2XG4gICAgICAtIE1ZU1FMX1VTRVI9YXp1cmFjYXN0XG4gICAgICAtIE1ZU1FMX1BBU1NXT1JEPSR7TVlTUUxfUEFTU1dPUkR9XG4gICAgICAtIE1ZU1FMX0RBVEFCQVNFPWF6dXJhY2FzdFxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIG1hcmlhZGJcblxuICBtYXJpYWRiOlxuICAgIGltYWdlOiBtYXJpYWRiOjExLjRcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIG1hcmlhZGItZGF0YTovdmFyL2xpYi9teXNxbFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBNWVNRTF9ST09UX1BBU1NXT1JEPSR7TVlTUUxfUk9PVF9QQVNTV09SRH1cbiAgICAgIC0gTVlTUUxfREFUQUJBU0U9YXp1cmFjYXN0XG4gICAgICAtIE1ZU1FMX1VTRVI9YXp1cmFjYXN0XG4gICAgICAtIE1ZU1FMX1BBU1NXT1JEPSR7TVlTUUxfUEFTU1dPUkR9XG5cbnZvbHVtZXM6XG4gIGF6dXJhY2FzdC1zdGF0aW9uLWRhdGE6IHt9XG4gIGF6dXJhY2FzdC1kYXRhOiB7fVxuICBhenVyYWNhc3QtdXBsb2Fkczoge31cbiAgYXp1cmFjYXN0LWJhY2t1cHM6IHt9XG4gIG1hcmlhZGItZGF0YToge30iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxubXlzcWxfcm9vdF9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxubXlzcWxfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImF6dXJhY2FzdFwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5MQU5HID0gXCJlbl9VUy5VVEYtOFwiXG5BWlVSQUNBU1RfRENfUkVWSVNJT04gPSBcIjFcIlxuTVlTUUxfSE9TVCA9IFwibWFyaWFkYlwiXG5NWVNRTF9QT1JUID0gXCIzMzA2XCJcbk1ZU1FMX1VTRVIgPSBcImF6dXJhY2FzdFwiXG5NWVNRTF9QQVNTV09SRCA9IFwiJHtteXNxbF9wYXNzd29yZH1cIlxuTVlTUUxfREFUQUJBU0UgPSBcImF6dXJhY2FzdFwiXG5NWVNRTF9ST09UX1BBU1NXT1JEID0gXCIke215c3FsX3Jvb3RfcGFzc3dvcmR9XCJcbkxFVFNFTkNSWVBUX0hPU1QgPSBcIiR7bWFpbl9kb21haW59XCJcblZJUlRVQUxfSE9TVCA9IFwiJHttYWluX2RvbWFpbn1cIlxuRElTQUJMRV9MRVRTRU5DUllQVCA9IFwidHJ1ZVwiXG5BVVRPX0FTU0lHTl9QT1JUX0hUVFAgPSBcIjgwXCJcbkFVVE9fQVNTSUdOX1BPUlRfSFRUUFMgPSBcIjQ0M1wiXG5OR0lOWF9SQURJT19QT1JUUyA9IFwiODAwMCw4MDEwLDgwMjAsODAzMCw4MDQwLDgwNTBcIlxuUFJFRkVSX1JFTEVBU0VfQlVJTERTID0gXCJ0cnVlXCJcbkNPTVBPU0VSX1BMVUdJTl9NT0RFID0gXCJmYWxzZVwiXG5BRERJVElPTkFMX01FRElBX1NZTkNfV09SS0VSX0NPVU5UID0gXCIwXCJcblxuW1tjb25maWcubW91bnRzXV0iCn0=
```

## Links

`radio`,`streaming`,`media`,`broadcasting`,`music`,`entertainment`

---

Version:`latest`

AutomatischAutomatisch is a powerful, self-hosted workflow automation tool designed for connecting your apps and automating repetitive tasks. With Automatisch, you can create workflows to sync data, send notifications, and perform various actions seamlessly across different services.

BabyBuddyBabyBuddy is a comprehensive, user-friendly platform designed to help parents and caregivers manage essential details about their child's growth and development. It provides tools for tracking feedings, sleep schedules, diaper changes, and milestones.

### On this page

ConfigurationBase64LinksTags