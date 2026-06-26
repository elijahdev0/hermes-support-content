---
title: "AnonUpload | Dokploy"
source: "https://docs.dokploy.com/docs/templates/anonupload"
category: dokploy-docs
created: "2026-06-25T17:21:40.414Z"
---

AnonUpload | Dokploy

# AnonUpload

Copy as Markdown

AnonUpload is a secure, anonymous file sharing application that does not require a database. It is built with privacy as a priority, ensuring that the direct filename used is not displayed.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  anonupload:
    image: ghcr.io/supernova3339/anonfiles:1
    restart: unless-stopped
    ports:
      - 80
    environment:
      - ADMIN_EMAIL=${ADMIN_EMAIL}
      - ADMIN_PASSWORD=${ADMIN_PASSWORD}
      - CONTACT_EMAIL=${CONTACT_EMAIL}
    volumes:
      - uploads:/var/www/html/uploads

volumes:
  uploads: {}
```

```
[variables]
main_domain = "${domain}"
admin_email = "${email}"
admin_password = "${password:16}"
contact_email = "${email}"

[config]
[[config.domains]]
serviceName = "anonupload"
port = 80
host = "${main_domain}"

[config.env]
ADMIN_EMAIL = "${admin_email}"
ADMIN_PASSWORD = "${admin_password}"
CONTACT_EMAIL = "${contact_email}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhbm9udXBsb2FkOlxuICAgIGltYWdlOiBnaGNyLmlvL3N1cGVybm92YTMzMzkvYW5vbmZpbGVzOjFcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSA4MFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBBRE1JTl9FTUFJTD0ke0FETUlOX0VNQUlMfVxuICAgICAgLSBBRE1JTl9QQVNTV09SRD0ke0FETUlOX1BBU1NXT1JEfVxuICAgICAgLSBDT05UQUNUX0VNQUlMPSR7Q09OVEFDVF9FTUFJTH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSB1cGxvYWRzOi92YXIvd3d3L2h0bWwvdXBsb2Fkc1xuXG52b2x1bWVzOlxuICB1cGxvYWRzOiB7fSAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYWRtaW5fZW1haWwgPSBcIiR7ZW1haWx9XCJcbmFkbWluX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5jb250YWN0X2VtYWlsID0gXCIke2VtYWlsfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhbm9udXBsb2FkXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkFETUlOX0VNQUlMID0gXCIke2FkbWluX2VtYWlsfVwiXG5BRE1JTl9QQVNTV09SRCA9IFwiJHthZG1pbl9wYXNzd29yZH1cIlxuQ09OVEFDVF9FTUFJTCA9IFwiJHtjb250YWN0X2VtYWlsfVwiICIKfQ==
```

## Links

`file-sharing`,`privacy`

---

Version:`1`

AmpacheAmpache is a web-based audio/video streaming application and file manager allowing you to access your music & videos from anywhere, using almost any internet enabled device.

AnseAnse is an open-source alternative to ChatGPT web UI, supporting OpenAI-compatible APIs.

### On this page

ConfigurationBase64LinksTags