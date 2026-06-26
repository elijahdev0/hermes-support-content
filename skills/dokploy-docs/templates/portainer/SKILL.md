---
title: "Portainer | Dokploy"
source: "https://docs.dokploy.com/docs/templates/portainer"
category: dokploy-docs
created: "2026-06-25T17:21:56.648Z"
---

Portainer | Dokploy

# Portainer

Copy as Markdown

Portainer is a container management tool for deploying, troubleshooting, and securing applications across cloud, data centers, and IoT.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  portainer:
    image: portainer/portainer-ce:latest
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer-data:/data
    ports:
      - 9000

volumes:
  portainer-data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "portainer"
port = 9000
host = "${main_domain}"

[config.env]

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwb3J0YWluZXI6XG4gICAgaW1hZ2U6IHBvcnRhaW5lci9wb3J0YWluZXItY2U6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSAvdmFyL3J1bi9kb2NrZXIuc29jazovdmFyL3J1bi9kb2NrZXIuc29ja1xuICAgICAgLSBwb3J0YWluZXItZGF0YTovZGF0YVxuICAgIHBvcnRzOlxuICAgICAgLSA5MDAwXG5cbnZvbHVtZXM6XG4gIHBvcnRhaW5lci1kYXRhOiB7fSIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJwb3J0YWluZXJcIlxucG9ydCA9IDkwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5cbltbY29uZmlnLm1vdW50c11dIgp9
```

## Links

`cloud`,`monitoring`

---

Version:`latest`

PokePoke is an open-source, self-hosted alternative to YouTube. A privacy-focused video platform that allows you to watch and share videos without tracking.

Poste.ioComplete mail server solution with SMTP, IMAP, POP3, antispam, antivirus, web administration and webmail client.

### On this page

ConfigurationBase64LinksTags