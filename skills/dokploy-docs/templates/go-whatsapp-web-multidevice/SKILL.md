---
title: "WhatsApp API Multi Device Version | Dokploy"
source: "https://docs.dokploy.com/docs/templates/go-whatsapp-web-multidevice"
category: dokploy-docs
created: "2026-06-25T17:21:49.749Z"
---

WhatsApp API Multi Device Version | Dokploy

# WhatsApp API Multi Device Version

Copy as Markdown

WhatsApp API Multi Device Version the open-source, self-hosted whatsapp api. Send a chat, image and voice note with your own server.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  whatsapp:
    image: aldinokemal2104/go-whatsapp-web-multidevice
    restart: always
    ports:
      - "3080"
    volumes:
      - whatsapp:/app/storages
    command:
      - rest
      - --basic-auth=${WA_USER}:${WA_PASSWORD}
      - --port=3080
      - --debug=true
      - --os=Chrome
      - --account-validation=false

volumes:
  whatsapp:
```

```
[variables]
main_domain = "${domain}"
wa_user = "admin"
wa_password = "${password:32}"

[config]
env = [
  "WA_USER=${wa_user}",
  "WA_PASSWORD=${wa_password}"
]

[[config.domains]]
serviceName = "whatsapp"
port = 3080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB3aGF0c2FwcDpcbiAgICBpbWFnZTogYWxkaW5va2VtYWwyMTA0L2dvLXdoYXRzYXBwLXdlYi1tdWx0aWRldmljZVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIHBvcnRzOlxuICAgICAgLSBcIjMwODBcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIHdoYXRzYXBwOi9hcHAvc3RvcmFnZXNcbiAgICBjb21tYW5kOlxuICAgICAgLSByZXN0XG4gICAgICAtIC0tYmFzaWMtYXV0aD0ke1dBX1VTRVJ9OiR7V0FfUEFTU1dPUkR9XG4gICAgICAtIC0tcG9ydD0zMDgwXG4gICAgICAtIC0tZGVidWc9dHJ1ZVxuICAgICAgLSAtLW9zPUNocm9tZVxuICAgICAgLSAtLWFjY291bnQtdmFsaWRhdGlvbj1mYWxzZVxuXG52b2x1bWVzOlxuICB3aGF0c2FwcDpcblxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbndhX3VzZXIgPSBcImFkbWluXCJcbndhX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiV0FfVVNFUj0ke3dhX3VzZXJ9XCIsXG4gIFwiV0FfUEFTU1dPUkQ9JHt3YV9wYXNzd29yZH1cIlxuXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ3aGF0c2FwcFwiXG5wb3J0ID0gMzA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`whatsapp`,`self-hosted`,`open-source`,`api`

---

Version:`latest`

GLPI ProjectThe most complete open source service management software

GotenbergGotenberg is a Docker-powered stateless API for PDF files.

### On this page

ConfigurationBase64LinksTags