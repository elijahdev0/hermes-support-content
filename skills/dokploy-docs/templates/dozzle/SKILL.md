---
title: "Dozzle | Dokploy"
source: "https://docs.dokploy.com/docs/templates/dozzle"
category: dokploy-docs
created: "2026-06-25T17:21:46.246Z"
---

Dozzle | Dokploy

# Dozzle

Copy as Markdown

Dozzle is a lightweight, real-time log viewer for Docker containers.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  dozzle:
    image: amir20/dozzle:latest
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    expose:
      - 8080
```

```
[variables]
main_domain = "${domain}"
docker_socket = "/var/run/docker.sock"

[config]
[[config.domains]]
serviceName = "dozzle"
port = 8080
host = "${main_domain}"

[config.env]
DOZZLE_USERNAME = "${username}"
DOZZLE_PASSWORD = "${password:16}"

[[config.mounts]]
source = "${docker_socket}"
target = "/var/run/docker.sock"
read_only = true
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkb3p6bGU6XG4gICAgaW1hZ2U6IGFtaXIyMC9kb3p6bGU6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSAvdmFyL3J1bi9kb2NrZXIuc29jazovdmFyL3J1bi9kb2NrZXIuc29jazpyb1xuICAgIGV4cG9zZTpcbiAgICAgIC0gODA4MFxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRvY2tlcl9zb2NrZXQgPSBcIi92YXIvcnVuL2RvY2tlci5zb2NrXCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImRvenpsZVwiXG5wb3J0ID0gODA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkRPWlpMRV9VU0VSTkFNRSA9IFwiJHt1c2VybmFtZX1cIlxuRE9aWkxFX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zb3VyY2UgPSBcIiR7ZG9ja2VyX3NvY2tldH1cIlxudGFyZ2V0ID0gXCIvdmFyL3J1bi9kb2NrZXIuc29ja1wiXG5yZWFkX29ubHkgPSB0cnVlXG4iCn0=
```

## Links

`monitoring`,`logs`,`docker`

---

Version:`latest`

Double Zero00 is a self hostable SES dashboard for sending and monitoring emails with AWS

DragonflyDragonfly is a drop-in Redis replacement that is designed for heavy data workloads running on modern cloud hardware.

### On this page

ConfigurationBase64LinksTags