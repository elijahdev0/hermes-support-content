---
title: "Flatnotes (TOTP) | Dokploy"
source: "https://docs.dokploy.com/docs/templates/flatnotes-totp"
category: dokploy-docs
created: "2026-06-25T17:21:47.359Z"
---

Flatnotes (TOTP) | Dokploy

# Flatnotes (TOTP)

Copy as Markdown

Flatnotes with TOTP authentication enabled (username + password + one-time passcode).

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  flatnotes:
    image: dullage/flatnotes:latest
    restart: unless-stopped
    environment:
      PUID: ${PUID}
      PGID: ${PGID}
      FLATNOTES_AUTH_TYPE: "totp"
      FLATNOTES_USERNAME: ${FLATNOTES_USERNAME}
      FLATNOTES_PASSWORD: ${FLATNOTES_PASSWORD}
      FLATNOTES_SECRET_KEY: ${FLATNOTES_SECRET_KEY}
      FLATNOTES_TOTP_KEY: ${FLATNOTES_TOTP_KEY}
      FLATNOTES_SESSION_EXPIRY_DAYS: ${FLATNOTES_SESSION_EXPIRY_DAYS}
      FLATNOTES_PATH_PREFIX: ${FLATNOTES_PATH_PREFIX}
    expose:
      - 8080
    volumes:
      - flatnotes-data:/data

volumes:
  flatnotes-data: {}
```

```
[variables]
main_domain = "${domain}"
username = "${username}"
password = "${password:16}"
secret_key = "${password:32}"
totp_key = "${password:32}"

[config]
[[config.domains]]
serviceName = "flatnotes"
port = 8080
host = "${main_domain}"
path = "/"

[config.env]
PUID = "1000"
PGID = "1000"
FLATNOTES_AUTH_TYPE = "totp"
FLATNOTES_USERNAME = "${username}"
FLATNOTES_PASSWORD = "${password}"
FLATNOTES_SECRET_KEY = "${secret_key}"
FLATNOTES_TOTP_KEY = "${totp_key}"
FLATNOTES_SESSION_EXPIRY_DAYS = "30"
FLATNOTES_PATH_PREFIX = ""

[[config.mounts]]
name = "flatnotes-data"
mountPath = "/data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGZsYXRub3RlczpcbiAgICBpbWFnZTogZHVsbGFnZS9mbGF0bm90ZXM6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBVSUQ6ICR7UFVJRH1cbiAgICAgIFBHSUQ6ICR7UEdJRH1cbiAgICAgIEZMQVROT1RFU19BVVRIX1RZUEU6IFwidG90cFwiXG4gICAgICBGTEFUTk9URVNfVVNFUk5BTUU6ICR7RkxBVE5PVEVTX1VTRVJOQU1FfVxuICAgICAgRkxBVE5PVEVTX1BBU1NXT1JEOiAke0ZMQVROT1RFU19QQVNTV09SRH1cbiAgICAgIEZMQVROT1RFU19TRUNSRVRfS0VZOiAke0ZMQVROT1RFU19TRUNSRVRfS0VZfVxuICAgICAgRkxBVE5PVEVTX1RPVFBfS0VZOiAke0ZMQVROT1RFU19UT1RQX0tFWX1cbiAgICAgIEZMQVROT1RFU19TRVNTSU9OX0VYUElSWV9EQVlTOiAke0ZMQVROT1RFU19TRVNTSU9OX0VYUElSWV9EQVlTfVxuICAgICAgRkxBVE5PVEVTX1BBVEhfUFJFRklYOiAke0ZMQVROT1RFU19QQVRIX1BSRUZJWH1cbiAgICBleHBvc2U6XG4gICAgICAtIDgwODBcbiAgICB2b2x1bWVzOlxuICAgICAgLSBmbGF0bm90ZXMtZGF0YTovZGF0YVxuXG52b2x1bWVzOlxuICBmbGF0bm90ZXMtZGF0YToge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG51c2VybmFtZSA9IFwiJHt1c2VybmFtZX1cIlxucGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbnNlY3JldF9rZXkgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbnRvdHBfa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJmbGF0bm90ZXNcIlxucG9ydCA9IDgwODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbnBhdGggPSBcIi9cIlxuXG5bY29uZmlnLmVudl1cblBVSUQgPSBcIjEwMDBcIlxuUEdJRCA9IFwiMTAwMFwiXG5GTEFUTk9URVNfQVVUSF9UWVBFID0gXCJ0b3RwXCJcbkZMQVROT1RFU19VU0VSTkFNRSA9IFwiJHt1c2VybmFtZX1cIlxuRkxBVE5PVEVTX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkfVwiXG5GTEFUTk9URVNfU0VDUkVUX0tFWSA9IFwiJHtzZWNyZXRfa2V5fVwiXG5GTEFUTk9URVNfVE9UUF9LRVkgPSBcIiR7dG90cF9rZXl9XCJcbkZMQVROT1RFU19TRVNTSU9OX0VYUElSWV9EQVlTID0gXCIzMFwiXG5GTEFUTk9URVNfUEFUSF9QUkVGSVggPSBcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5uYW1lID0gXCJmbGF0bm90ZXMtZGF0YVwiXG5tb3VudFBhdGggPSBcIi9kYXRhXCJcbiIKfQ==
```

## Links

`notes`,`productivity`,`markdown`,`self-hosted`,`totp`,`2fa`

---

Version:`latest`

FlatnotesA self-hosted, modern note-taking web app that saves your notes as plain text Markdown files.

FlowiseFlowise is an open-source UI visual tool to build and run LLM-powered applications.

### On this page

ConfigurationBase64LinksTags