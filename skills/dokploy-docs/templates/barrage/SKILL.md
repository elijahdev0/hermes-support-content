---
title: "Barrage | Dokploy"
source: "https://docs.dokploy.com/docs/templates/barrage"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

Barrage | Dokploy

# Barrage

Copy as Markdown

Barrage is a minimalistic Deluge WebUI app with full mobile support. It features a responsive mobile-first design, allowing you to manage your torrents with ease from any device.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  barrage:
    image: maulik9898/barrage:0.3.0
    restart: unless-stopped
    ports:
      - 3000
    environment:
      - NEXTAUTH_SECRET=${NEXTAUTH_SECRET}
      - NEXTAUTH_URL=http://${DOMAIN}
      - DELUGE_URL=${DELUGE_URL}
      - DELUGE_PASSWORD=${DELUGE_PASSWORD}
      - BARRAGE_PASSWORD=${BARRAGE_PASSWORD}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "barrage"
port = 3000
host = "${main_domain}"

[config.env]
NEXTAUTH_SECRET = "${base64}"
NEXTAUTH_URL = "http://${main_domain}"
DELUGE_URL = "http://your-deluge-ip:8112"
DELUGE_PASSWORD = "${password:16}"
BARRAGE_PASSWORD = "${password:16}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBiYXJyYWdlOlxuICAgIGltYWdlOiBtYXVsaWs5ODk4L2JhcnJhZ2U6MC4zLjBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSAzMDAwXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE5FWFRBVVRIX1NFQ1JFVD0ke05FWFRBVVRIX1NFQ1JFVH1cbiAgICAgIC0gTkVYVEFVVEhfVVJMPWh0dHA6Ly8ke0RPTUFJTn1cbiAgICAgIC0gREVMVUdFX1VSTD0ke0RFTFVHRV9VUkx9XG4gICAgICAtIERFTFVHRV9QQVNTV09SRD0ke0RFTFVHRV9QQVNTV09SRH1cbiAgICAgIC0gQkFSUkFHRV9QQVNTV09SRD0ke0JBUlJBR0VfUEFTU1dPUkR9ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJiYXJyYWdlXCJcbnBvcnQgPSAzMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuTkVYVEFVVEhfU0VDUkVUID0gXCIke2Jhc2U2NH1cIlxuTkVYVEFVVEhfVVJMID0gXCJodHRwOi8vJHttYWluX2RvbWFpbn1cIlxuREVMVUdFX1VSTCA9IFwiaHR0cDovL3lvdXItZGVsdWdlLWlwOjgxMTJcIlxuREVMVUdFX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5CQVJSQUdFX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjE2fVwiICIKfQ==
```

## Links

`torrents`,`deluge`,`mobile`

---

Version:`0.3.0`

BaikalBaikal is a lightweight, self-hosted CalDAV and CardDAV server that enables users to manage calendars and contacts efficiently. It provides a simple and effective solution for syncing and sharing events, tasks, and address books across multiple devices.

BaserowBaserow is an open source database management tool that allows you to create and manage databases.

### On this page

ConfigurationBase64LinksTags