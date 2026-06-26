---
title: "Java Runtime (Multi-Version) | Dokploy"
source: "https://docs.dokploy.com/docs/templates/java"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

Java Runtime (Multi-Version) | Dokploy

# Java Runtime (Multi-Version)

Copy as Markdown

Configurable Java runtime environment supporting versions 8, 11, 16, 17, and 21. Perfect for Minecraft servers, Spring Boot apps, and custom Java applications.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  java-app:
    image: ghcr.io/pterodactyl/yolks:java_${JAVA_VERSION}
    restart: unless-stopped
    stdin_open: true
    tty: true
    volumes:
      - app-data:/home/container
    working_dir: /home/container
    environment:
      - STARTUP=${STARTUP_COMMAND}
      - SERVER_JARFILE=${SERVER_JARFILE}
      - JAVA_VERSION=${JAVA_VERSION}
    ports:
      - ${SERVER_PORT}
    user: container

volumes:
  app-data: {}
```

```
[variables]
java_version = "21"
server_port = "25565"
startup_command = "java -Xmx1024M -Xms512M -jar server.jar nogui"
server_jarfile = "server.jar"

[config]
[[config.domains]]
serviceName = "java-app"
port = 25565
host = "${domain}"

[config.env]
JAVA_VERSION = "${java_version}"
SERVER_PORT = "${server_port}"
STARTUP_COMMAND = "${startup_command}"
SERVER_JARFILE = "${server_jarfile}"

[[config.mounts]]
filePath = "/home/container/server.properties"
content = """
# Minecraft server properties
server-port=25565
motd=Java Server powered by Dokploy
online-mode=true
difficulty=easy
gamemode=survival
max-players=20
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBqYXZhLWFwcDpcbiAgICBpbWFnZTogZ2hjci5pby9wdGVyb2RhY3R5bC95b2xrczpqYXZhXyR7SkFWQV9WRVJTSU9OfVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgc3RkaW5fb3BlbjogdHJ1ZVxuICAgIHR0eTogdHJ1ZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGFwcC1kYXRhOi9ob21lL2NvbnRhaW5lclxuICAgIHdvcmtpbmdfZGlyOiAvaG9tZS9jb250YWluZXJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gU1RBUlRVUD0ke1NUQVJUVVBfQ09NTUFORH1cbiAgICAgIC0gU0VSVkVSX0pBUkZJTEU9JHtTRVJWRVJfSkFSRklMRX1cbiAgICAgIC0gSkFWQV9WRVJTSU9OPSR7SkFWQV9WRVJTSU9OfVxuICAgIHBvcnRzOlxuICAgICAgLSAke1NFUlZFUl9QT1JUfVxuICAgIHVzZXI6IGNvbnRhaW5lclxuXG52b2x1bWVzOlxuICBhcHAtZGF0YToge30iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbmphdmFfdmVyc2lvbiA9IFwiMjFcIlxuc2VydmVyX3BvcnQgPSBcIjI1NTY1XCJcbnN0YXJ0dXBfY29tbWFuZCA9IFwiamF2YSAtWG14MTAyNE0gLVhtczUxMk0gLWphciBzZXJ2ZXIuamFyIG5vZ3VpXCJcbnNlcnZlcl9qYXJmaWxlID0gXCJzZXJ2ZXIuamFyXCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImphdmEtYXBwXCJcbnBvcnQgPSAyNTU2NVxuaG9zdCA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5KQVZBX1ZFUlNJT04gPSBcIiR7amF2YV92ZXJzaW9ufVwiXG5TRVJWRVJfUE9SVCA9IFwiJHtzZXJ2ZXJfcG9ydH1cIlxuU1RBUlRVUF9DT01NQU5EID0gXCIke3N0YXJ0dXBfY29tbWFuZH1cIlxuU0VSVkVSX0pBUkZJTEUgPSBcIiR7c2VydmVyX2phcmZpbGV9XCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvaG9tZS9jb250YWluZXIvc2VydmVyLnByb3BlcnRpZXNcIlxuY29udGVudCA9IFwiXCJcIlxuIyBNaW5lY3JhZnQgc2VydmVyIHByb3BlcnRpZXNcbnNlcnZlci1wb3J0PTI1NTY1XG5tb3RkPUphdmEgU2VydmVyIHBvd2VyZWQgYnkgRG9rcGxveVxub25saW5lLW1vZGU9dHJ1ZVxuZGlmZmljdWx0eT1lYXN5XG5nYW1lbW9kZT1zdXJ2aXZhbFxubWF4LXBsYXllcnM9MjBcblwiXCJcIiIKfQ==
```

## Links

`java`,`minecraft`,`runtime`,`pterodactyl`

---

Version:`8-21`

IT ToolsA collection of handy online it-tools for developers.

jellyfinJellyfin is a Free Software Media System that puts you in control of managing and streaming your media.

### On this page

ConfigurationBase64LinksTags