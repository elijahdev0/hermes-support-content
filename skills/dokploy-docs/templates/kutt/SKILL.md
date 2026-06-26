---
title: "Kutt | Dokploy"
source: "https://docs.dokploy.com/docs/templates/kutt"
category: dokploy-docs
created: "2026-06-25T17:21:50.891Z"
---

Kutt | Dokploy

# Kutt

Copy as Markdown

Kutt is a modern URL shortener with support for custom domains. Create and edit links, view statistics, manage users, and more.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  kutt:
    image: kutt/kutt:main
    volumes:
      - kutt_db_data:/var/lib/kutt
      - ./kutt/custom:/kutt/custom
    environment:
      DB_FILENAME: "/var/lib/kutt/data.sqlite"
      JWT_SECRET: ${JWT_SECRET}
      DEFAULT_DOMAIN: ${DEFAULT_DOMAIN}
      TRUST_PROXY: ${TRUST_PROXY}
      DISALLOW_ANONYMOUS_LINKS: ${DISALLOW_ANONYMOUS_LINKS}
      CUSTOM_DOMAIN_USE_HTTPS: ${CUSTOM_DOMAIN_USE_HTTPS}
      MAIL_ENABLED: ${MAIL_ENABLED}
      MAIL_HOST: ${MAIL_HOST}
      MAIL_PORT: ${MAIL_PORT}
      MAIL_SECURE: ${MAIL_SECURE}
      MAIL_USER: ${MAIL_USER}
      MAIL_FROM: ${MAIL_FROM}
      MAIL_PASSWORD: ${MAIL_PASSWORD}
      CONTACT_EMAIL: ${CONTACT_EMAIL}

volumes:
  kutt_db_data: {}
```

```
[variables]
main_domain = "${domain}"
jwt_secret = "${password:32}"

[config]
env = [
    "JWT_SECRET=${jwt_secret}",
    "DEFAULT_DOMAIN=${main_domain}",
    "TRUST_PROXY=false",
    "DISALLOW_ANONYMOUS_LINKS=true",
    "CUSTOM_DOMAIN_USE_HTTPS=true",
    "MAIL_ENABLED=false",
    "MAIL_HOST=''",
    "MAIL_PORT='22'",
    "MAIL_SECURE=true",
    "MAIL_USER=''",
    "MAIL_FROM=''",
    "MAIL_PASSWORD=''",
    "CONTACT_EMAIL=''"
]
mounts = []

[[config.domains]]
serviceName = "kutt"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBrdXR0OlxuICAgIGltYWdlOiBrdXR0L2t1dHQ6bWFpblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGt1dHRfZGJfZGF0YTovdmFyL2xpYi9rdXR0XG4gICAgICAtIC4va3V0dC9jdXN0b206L2t1dHQvY3VzdG9tXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBEQl9GSUxFTkFNRTogXCIvdmFyL2xpYi9rdXR0L2RhdGEuc3FsaXRlXCJcbiAgICAgIEpXVF9TRUNSRVQ6ICR7SldUX1NFQ1JFVH1cbiAgICAgIERFRkFVTFRfRE9NQUlOOiAke0RFRkFVTFRfRE9NQUlOfVxuICAgICAgVFJVU1RfUFJPWFk6ICR7VFJVU1RfUFJPWFl9XG4gICAgICBESVNBTExPV19BTk9OWU1PVVNfTElOS1M6ICR7RElTQUxMT1dfQU5PTllNT1VTX0xJTktTfVxuICAgICAgQ1VTVE9NX0RPTUFJTl9VU0VfSFRUUFM6ICR7Q1VTVE9NX0RPTUFJTl9VU0VfSFRUUFN9XG4gICAgICBNQUlMX0VOQUJMRUQ6ICR7TUFJTF9FTkFCTEVEfVxuICAgICAgTUFJTF9IT1NUOiAke01BSUxfSE9TVH1cbiAgICAgIE1BSUxfUE9SVDogJHtNQUlMX1BPUlR9XG4gICAgICBNQUlMX1NFQ1VSRTogJHtNQUlMX1NFQ1VSRX1cbiAgICAgIE1BSUxfVVNFUjogJHtNQUlMX1VTRVJ9XG4gICAgICBNQUlMX0ZST006ICR7TUFJTF9GUk9NfVxuICAgICAgTUFJTF9QQVNTV09SRDogJHtNQUlMX1BBU1NXT1JEfVxuICAgICAgQ09OVEFDVF9FTUFJTDogJHtDT05UQUNUX0VNQUlMfVxuXG52b2x1bWVzOlxuICBrdXR0X2RiX2RhdGE6IHt9IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmp3dF9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgICBcIkpXVF9TRUNSRVQ9JHtqd3Rfc2VjcmV0fVwiLFxuICAgIFwiREVGQVVMVF9ET01BSU49JHttYWluX2RvbWFpbn1cIixcbiAgICBcIlRSVVNUX1BST1hZPWZhbHNlXCIsXG4gICAgXCJESVNBTExPV19BTk9OWU1PVVNfTElOS1M9dHJ1ZVwiLFxuICAgIFwiQ1VTVE9NX0RPTUFJTl9VU0VfSFRUUFM9dHJ1ZVwiLFxuICAgIFwiTUFJTF9FTkFCTEVEPWZhbHNlXCIsXG4gICAgXCJNQUlMX0hPU1Q9JydcIixcbiAgICBcIk1BSUxfUE9SVD0nMjInXCIsXG4gICAgXCJNQUlMX1NFQ1VSRT10cnVlXCIsXG4gICAgXCJNQUlMX1VTRVI9JydcIixcbiAgICBcIk1BSUxfRlJPTT0nJ1wiLFxuICAgIFwiTUFJTF9QQVNTV09SRD0nJ1wiLFxuICAgIFwiQ09OVEFDVF9FTUFJTD0nJ1wiXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJrdXR0XCJcbnBvcnQgPSAzXzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIiIKfQ==
```

## Links

`link-shortener`,`link-sharing`

---

Version:`latest`

Komari MonitorA lightweight, self-hosted server monitoring tool for tracking server performance.

LangflowLangflow is a low-code app builder for RAG and multi-agent AI applications. It's Python-based and agnostic to any model, API, or database.

### On this page

ConfigurationBase64LinksTags