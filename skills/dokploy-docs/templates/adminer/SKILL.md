---
title: "Adminer | Dokploy"
source: "https://docs.dokploy.com/docs/templates/adminer"
category: dokploy-docs
created: "2026-06-25T17:21:40.413Z"
---

Adminer | Dokploy

# Adminer

Copy as Markdown

Adminer is a comprehensive database management tool that supports MySQL, MariaDB, PostgreSQL, SQLite, MS SQL, Oracle, Elasticsearch, MongoDB and others. It provides a clean interface for efficient database operations, with strong security features and extensive customization options.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  adminer:
    image: adminer:4.8.1
    restart: unless-stopped
    ports:
      - 8080
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "adminer"
port = 8080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhZG1pbmVyOlxuICAgIGltYWdlOiBhZG1pbmVyOjQuOC4xXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gODA4MCAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYWRtaW5lclwiXG5wb3J0ID0gODA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIiAiCn0=
```

## Links

`databases`,`developer-tools`,`mysql`,`postgresql`

---

Version:`4.8.1`

AdGuard HomeAdGuard Home is a comprehensive solution designed to enhance your online browsing experience by eliminating all kinds of ads, from annoying banners and pop-ups to intrusive video ads. It provides privacy protection, browsing security, and parental control features while maintaining website functionality.

AdventureLogAdventureLog is an open-source activity tracker with maps, journaling, and Strava integration.

### On this page

ConfigurationBase64LinksTags