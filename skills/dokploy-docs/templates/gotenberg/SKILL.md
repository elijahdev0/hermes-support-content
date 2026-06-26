---
title: "Gotenberg | Dokploy"
source: "https://docs.dokploy.com/docs/templates/gotenberg"
category: dokploy-docs
created: "2026-06-25T17:21:49.749Z"
---

Gotenberg | Dokploy

# Gotenberg

Copy as Markdown

Gotenberg is a Docker-powered stateless API for PDF files.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  gotenberg:
    image: gotenberg/gotenberg:latest
    environment:
      # NOTE: requires the --api-enable-basic-auth option in "command"
      #       make sure to also change the credentials in Dokploy environment
      GOTENBERG_API_BASIC_AUTH_USERNAME: ${GOTENBERG_API_BASIC_AUTH_USERNAME}
      GOTENBERG_API_BASIC_AUTH_PASSWORD: ${GOTENBERG_API_BASIC_AUTH_PASSWORD}
    command:
      - gotenberg
      # See the full list of options at https://gotenberg.dev/docs/configuration

      # Examples:
      # - --api-timeout=60s
      # - --chromium-auto-start
      - --api-enable-basic-auth
      - --api-disable-health-check-logging
    restart: unless-stopped
```

```
[variables]
main_domain = "${domain}"
username = "gotenberg"
password = "changethis"

[config]
env = [
  "GOTENBERG_API_BASIC_AUTH_USERNAME=${username}",
  "GOTENBERG_API_BASIC_AUTH_PASSWORD=${password}",
]
mounts = []

[[config.domains]]
serviceName = "gotenberg"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBnb3RlbmJlcmc6XG4gICAgaW1hZ2U6IGdvdGVuYmVyZy9nb3RlbmJlcmc6bGF0ZXN0XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAjIE5PVEU6IHJlcXVpcmVzIHRoZSAtLWFwaS1lbmFibGUtYmFzaWMtYXV0aCBvcHRpb24gaW4gXCJjb21tYW5kXCJcbiAgICAgICMgICAgICAgbWFrZSBzdXJlIHRvIGFsc28gY2hhbmdlIHRoZSBjcmVkZW50aWFscyBpbiBEb2twbG95IGVudmlyb25tZW50XG4gICAgICBHT1RFTkJFUkdfQVBJX0JBU0lDX0FVVEhfVVNFUk5BTUU6ICR7R09URU5CRVJHX0FQSV9CQVNJQ19BVVRIX1VTRVJOQU1FfVxuICAgICAgR09URU5CRVJHX0FQSV9CQVNJQ19BVVRIX1BBU1NXT1JEOiAke0dPVEVOQkVSR19BUElfQkFTSUNfQVVUSF9QQVNTV09SRH1cbiAgICBjb21tYW5kOlxuICAgICAgLSBnb3RlbmJlcmdcbiAgICAgICMgU2VlIHRoZSBmdWxsIGxpc3Qgb2Ygb3B0aW9ucyBhdCBodHRwczovL2dvdGVuYmVyZy5kZXYvZG9jcy9jb25maWd1cmF0aW9uXG5cbiAgICAgICMgRXhhbXBsZXM6XG4gICAgICAjIC0gLS1hcGktdGltZW91dD02MHNcbiAgICAgICMgLSAtLWNocm9taXVtLWF1dG8tc3RhcnRcbiAgICAgIC0gLS1hcGktZW5hYmxlLWJhc2ljLWF1dGhcbiAgICAgIC0gLS1hcGktZGlzYWJsZS1oZWFsdGgtY2hlY2stbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxudXNlcm5hbWUgPSBcImdvdGVuYmVyZ1wiXG5wYXNzd29yZCA9IFwiY2hhbmdldGhpc1wiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiR09URU5CRVJHX0FQSV9CQVNJQ19BVVRIX1VTRVJOQU1FPSR7dXNlcm5hbWV9XCIsXG4gIFwiR09URU5CRVJHX0FQSV9CQVNJQ19BVVRIX1BBU1NXT1JEPSR7cGFzc3dvcmR9XCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJnb3RlbmJlcmdcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`api`,`backend`,`pdf`,`tools`

---

Version:`latest`

WhatsApp API Multi Device VersionWhatsApp API Multi Device Version the open-source, self-hosted whatsapp api. Send a chat, image and voice note with your own server.

GrafanaGrafana is an open source platform for data visualization and monitoring.

### On this page

ConfigurationBase64LinksTags