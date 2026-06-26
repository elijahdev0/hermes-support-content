---
title: "Cloud Commander | Dokploy"
source: "https://docs.dokploy.com/docs/templates/cloudcommander"
category: dokploy-docs
created: "2026-06-25T17:21:43.965Z"
---

Cloud Commander | Dokploy

# Cloud Commander

Copy as Markdown

Cloud Commander is a file manager for the web. It includes a command-line console and a text editor. Cloud Commander helps you manage your server and work with files, directories and programs in a web browser.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  cloudcmd:
    image: coderaiser/cloudcmd:18.5.1
    ports:
      - "80"
    environment:
      - CLOUDCMD_ROOT=/mnt/fs
      - CLOUDCMD_AUTH=true
      - CLOUDCMD_USERNAME=${USERNAME}
      - CLOUDCMD_PASSWORD=${PASSWORD}
    volumes:
      - /root:/root
      - /:/mnt/fs
```

```
[variables]
USERNAME = "user"
PASSWORD = "${password:16}"

[config]
[[config.domains]]
serviceName = "cloudcmd"
port = 80
host = "${domain}"

[config.env]
USERNAME = "${USERNAME}"
PASSWORD = "${PASSWORD}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBjbG91ZGNtZDpcbiAgICBpbWFnZTogY29kZXJhaXNlci9jbG91ZGNtZDoxOC41LjFcbiAgICBwb3J0czpcbiAgICAgIC0gXCI4MFwiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIENMT1VEQ01EX1JPT1Q9L21udC9mc1xuICAgICAgLSBDTE9VRENNRF9BVVRIPXRydWVcbiAgICAgIC0gQ0xPVURDTURfVVNFUk5BTUU9JHtVU0VSTkFNRX1cbiAgICAgIC0gQ0xPVURDTURfUEFTU1dPUkQ9JHtQQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSAvcm9vdDovcm9vdFxuICAgICAgLSAvOi9tbnQvZnMgIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5VU0VSTkFNRSA9IFwidXNlclwiXG5QQVNTV09SRCA9IFwiJHtwYXNzd29yZDoxNn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY2xvdWRjbWRcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblVTRVJOQU1FID0gXCIke1VTRVJOQU1FfVwiXG5QQVNTV09SRCA9IFwiJHtQQVNTV09SRH1cIiAiCn0=
```

## Links

`file-manager`,`web-based`,`console`

---

Version:`18.5.1`

Cloud9Cloud9 is a cloud-based integrated development environment (IDE) designed for developers to code, build, and debug applications collaboratively in real time.

Cloudflare DDNSA small, feature-rich, and robust Cloudflare DDNS updater.

### On this page

ConfigurationBase64LinksTags