---
title: "Lobe Chat | Dokploy"
source: "https://docs.dokploy.com/docs/templates/lobe-chat"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

Lobe Chat | Dokploy

# Lobe Chat

Copy as Markdown

Lobe Chat - an open-source, modern-design AI chat framework.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  lobe-chat:
    image: lobehub/lobe-chat:v1.26.1
    restart: always
    ports:
      - 3210
    environment:
      OPENAI_API_KEY: sk-xxxx
      OPENAI_PROXY_URL: https://api-proxy.com/v1
      ACCESS_CODE: lobe66
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "lobe-chat"
port = 3_210
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBsb2JlLWNoYXQ6XG4gICAgaW1hZ2U6IGxvYmVodWIvbG9iZS1jaGF0OnYxLjI2LjFcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBwb3J0czpcbiAgICAgIC0gMzIxMFxuICAgIGVudmlyb25tZW50OlxuICAgICAgT1BFTkFJX0FQSV9LRVk6IHNrLXh4eHhcbiAgICAgIE9QRU5BSV9QUk9YWV9VUkw6IGh0dHBzOi8vYXBpLXByb3h5LmNvbS92MVxuICAgICAgQUNDRVNTX0NPREU6IGxvYmU2NiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSB7fVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibG9iZS1jaGF0XCJcbnBvcnQgPSAzXzIxMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`IA`,`chat`

---

Version:`v1.26.1`

LivekitLiveKit is an open source platform for developers building realtime media applications.

LodestoneA free, open source server hosting tool for Minecraft and other multiplayers games.

### On this page

ConfigurationBase64LinksTags