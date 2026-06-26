---
title: "Minepanel | Dokploy"
source: "https://docs.dokploy.com/docs/templates/minepanel"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

Minepanel | Dokploy

# Minepanel

Copy as Markdown

Web panel for managing Minecraft servers with Docker. Create, configure, start/stop, and monitor multiple instances from a modern UI.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  backend:
    image: ketbom/minepanel-backend:1.7.1
    restart: unless-stopped
    environment:
      - NODE_ENV=production
      - FRONTEND_URL=${FRONTEND_URL}
      - JWT_SECRET=${JWT_SECRET}
      - CLIENT_PASSWORD=${CLIENT_PASSWORD}
      - CLIENT_USERNAME=${CLIENT_USERNAME}
      - BASE_DIR=${BASE_DIR}
    volumes:
      - minepanel-servers:/app/servers
      - minepanel-data:/app/data
      - /var/run/docker.sock:/var/run/docker.sock

  frontend:
    image: ketbom/minepanel-frontend:1.7.1
    restart: unless-stopped
    environment:
      - NEXT_PUBLIC_BACKEND_URL=${NEXT_PUBLIC_BACKEND_URL}
      - NEXT_PUBLIC_DEFAULT_LANGUAGE=${NEXT_PUBLIC_DEFAULT_LANGUAGE}
    depends_on:
      - backend

volumes:
  minepanel-servers:
  minepanel-data:
```

```
[variables]
main_domain = "${domain}"
jwt_secret = "${base64:32}"
client_username = "admin"
client_password = "${password:16}"
default_language = "en"

[config]
mounts = []

[[config.domains]]
serviceName = "frontend"
port = 3_000
host = "${main_domain}"

[[config.domains]]
serviceName = "backend"
port = 8_091
host = "api-${main_domain}"

[config.env]
JWT_SECRET = "${jwt_secret}"
CLIENT_USERNAME = "${client_username}"
CLIENT_PASSWORD = "${client_password}"
FRONTEND_URL = "http://${main_domain}"
NEXT_PUBLIC_BACKEND_URL = "http://api-${main_domain}"
NEXT_PUBLIC_DEFAULT_LANGUAGE = "${default_language}"
BASE_DIR = "/app"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBiYWNrZW5kOlxuICAgIGltYWdlOiBrZXRib20vbWluZXBhbmVsLWJhY2tlbmQ6MS43LjFcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBOT0RFX0VOVj1wcm9kdWN0aW9uXG4gICAgICAtIEZST05URU5EX1VSTD0ke0ZST05URU5EX1VSTH1cbiAgICAgIC0gSldUX1NFQ1JFVD0ke0pXVF9TRUNSRVR9XG4gICAgICAtIENMSUVOVF9QQVNTV09SRD0ke0NMSUVOVF9QQVNTV09SRH1cbiAgICAgIC0gQ0xJRU5UX1VTRVJOQU1FPSR7Q0xJRU5UX1VTRVJOQU1FfVxuICAgICAgLSBCQVNFX0RJUj0ke0JBU0VfRElSfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIG1pbmVwYW5lbC1zZXJ2ZXJzOi9hcHAvc2VydmVyc1xuICAgICAgLSBtaW5lcGFuZWwtZGF0YTovYXBwL2RhdGFcbiAgICAgIC0gL3Zhci9ydW4vZG9ja2VyLnNvY2s6L3Zhci9ydW4vZG9ja2VyLnNvY2tcblxuICBmcm9udGVuZDpcbiAgICBpbWFnZToga2V0Ym9tL21pbmVwYW5lbC1mcm9udGVuZDoxLjcuMVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE5FWFRfUFVCTElDX0JBQ0tFTkRfVVJMPSR7TkVYVF9QVUJMSUNfQkFDS0VORF9VUkx9XG4gICAgICAtIE5FWFRfUFVCTElDX0RFRkFVTFRfTEFOR1VBR0U9JHtORVhUX1BVQkxJQ19ERUZBVUxUX0xBTkdVQUdFfVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGJhY2tlbmRcblxudm9sdW1lczpcbiAgbWluZXBhbmVsLXNlcnZlcnM6XG4gIG1pbmVwYW5lbC1kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmp3dF9zZWNyZXQgPSBcIiR7YmFzZTY0OjMyfVwiXG5jbGllbnRfdXNlcm5hbWUgPSBcImFkbWluXCJcbmNsaWVudF9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoxNn1cIlxuZGVmYXVsdF9sYW5ndWFnZSA9IFwiZW5cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZnJvbnRlbmRcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImJhY2tlbmRcIlxucG9ydCA9IDhfMDkxXG5ob3N0ID0gXCJhcGktJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkpXVF9TRUNSRVQgPSBcIiR7and0X3NlY3JldH1cIlxuQ0xJRU5UX1VTRVJOQU1FID0gXCIke2NsaWVudF91c2VybmFtZX1cIlxuQ0xJRU5UX1BBU1NXT1JEID0gXCIke2NsaWVudF9wYXNzd29yZH1cIlxuRlJPTlRFTkRfVVJMID0gXCJodHRwOi8vJHttYWluX2RvbWFpbn1cIlxuTkVYVF9QVUJMSUNfQkFDS0VORF9VUkwgPSBcImh0dHA6Ly9hcGktJHttYWluX2RvbWFpbn1cIlxuTkVYVF9QVUJMSUNfREVGQVVMVF9MQU5HVUFHRSA9IFwiJHtkZWZhdWx0X2xhbmd1YWdlfVwiXG5CQVNFX0RJUiA9IFwiL2FwcFwiXG4iCn0=
```

## Links

`gaming`,`minecraft`,`server-management`,`docker`

---

Version:`1.7.1`

MeTubeMeTube is a web-based YouTube downloader that allows downloading videos and audio using yt-dlp.

MinioMinio is an open source object storage server compatible with Amazon S3 cloud storage service.

### On this page

ConfigurationBase64LinksTags