---
title: "Snapp | Dokploy"
source: "https://docs.dokploy.com/docs/templates/snapp"
category: dokploy-docs
created: "2026-06-25T17:21:59.114Z"
---

Snapp | Dokploy

# Snapp

Copy as Markdown

Snapp is a self-hosted screenshot sharing service with user management and authentication.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  snapp:
    image: uraniadev/snapp:0.9-rc-020
    ports:
      - 3000
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - DATABASE_PROVIDER=${DATABASE_PROVIDER}
      - TOKEN_SECRET=${TOKEN_SECRET} # API Key for authentication token
      - ORIGIN=${ORIGIN}
      - DISABLED_EMAIL_AND_PASSWORD=${DISABLED_EMAIL_AND_PASSWORD}
      - LOG_LEVEL=${LOG_LEVEL}
      - PORT=${PORT}
      - ADMIN_USERNAME=${ADMIN_USERNAME}
      - ADMIN_EMAIL=${ADMIN_EMAIL}
      - ADMIN_PASSWORD=${ADMIN_PASSWORD}
      - ENABLE_SIGNUP=${ENABLE_SIGNUP}
      - ENABLED_MFA=${ENABLED_MFA}
      - PUBLIC_URL=${PUBLIC_URL}
      - APPNAME=${APPNAME}
      - PUBLIC_EXTRA_GROUPS_EDITABLE=${PUBLIC_EXTRA_GROUPS_EDITABLE}
      - URLS_VIA_GROUPS_ONLY=${URLS_VIA_GROUPS_ONLY}
      - HOST=${HOST}
    volumes:
      - ../files/snapp-db:/app/db.sqlite
volumes:
  snapp-db: {}
```

```
[variables]
main_domain = "${domain}"
token_secret = "${password:32}"

[config]
[[config.domains]]
serviceName = "snapp"
port = 3000
host = "${main_domain}"

[config.env]
DATABASE_URL = "file:./db.sqlite"
DATABASE_PROVIDER = "sqlite" # Options: postgres | mysql | sqlite
DISABLED_EMAIL_AND_PASSWORD = "false"
LOG_LEVEL = "debug"
ORIGIN = "http://${main_domain}"
PORT = "3000"
ADMIN_USERNAME = "admin"
ADMIN_EMAIL = "[email protected]"
ADMIN_PASSWORD = "${password:16}"
TOKEN_SECRET = "${token_secret}" # API Key for authentication token
ENABLE_SIGNUP = "true"
ENABLED_MFA = "false"
PUBLIC_URL = "${main_domain}"
APPNAME = "Snapp"
PUBLIC_EXTRA_GROUPS_EDITABLE = "true"
URLS_VIA_GROUPS_ONLY = "false"
HOST = "0.0.0.0"

[[config.mounts]]
filePath = "/files/snapp-db/db.sqlite"
content = """
# SQLite database file for Snapp
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBzbmFwcDpcbiAgICBpbWFnZTogdXJhbmlhZGV2L3NuYXBwOjAuOS1yYy0wMjBcbiAgICBwb3J0czpcbiAgICAgIC0gMzAwMFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBEQVRBQkFTRV9VUkw9JHtEQVRBQkFTRV9VUkx9XG4gICAgICAtIERBVEFCQVNFX1BST1ZJREVSPSR7REFUQUJBU0VfUFJPVklERVJ9XG4gICAgICAtIFRPS0VOX1NFQ1JFVD0ke1RPS0VOX1NFQ1JFVH0gIyBBUEkgS2V5IGZvciBhdXRoZW50aWNhdGlvbiB0b2tlblxuICAgICAgLSBPUklHSU49JHtPUklHSU59XG4gICAgICAtIERJU0FCTEVEX0VNQUlMX0FORF9QQVNTV09SRD0ke0RJU0FCTEVEX0VNQUlMX0FORF9QQVNTV09SRH1cbiAgICAgIC0gTE9HX0xFVkVMPSR7TE9HX0xFVkVMfVxuICAgICAgLSBQT1JUPSR7UE9SVH1cbiAgICAgIC0gQURNSU5fVVNFUk5BTUU9JHtBRE1JTl9VU0VSTkFNRX1cbiAgICAgIC0gQURNSU5fRU1BSUw9JHtBRE1JTl9FTUFJTH1cbiAgICAgIC0gQURNSU5fUEFTU1dPUkQ9JHtBRE1JTl9QQVNTV09SRH1cbiAgICAgIC0gRU5BQkxFX1NJR05VUD0ke0VOQUJMRV9TSUdOVVB9XG4gICAgICAtIEVOQUJMRURfTUZBPSR7RU5BQkxFRF9NRkF9XG4gICAgICAtIFBVQkxJQ19VUkw9JHtQVUJMSUNfVVJMfVxuICAgICAgLSBBUFBOQU1FPSR7QVBQTkFNRX1cbiAgICAgIC0gUFVCTElDX0VYVFJBX0dST1VQU19FRElUQUJMRT0ke1BVQkxJQ19FWFRSQV9HUk9VUFNfRURJVEFCTEV9XG4gICAgICAtIFVSTFNfVklBX0dST1VQU19PTkxZPSR7VVJMU19WSUFfR1JPVVBTX09OTFl9XG4gICAgICAtIEhPU1Q9JHtIT1NUfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL3NuYXBwLWRiOi9hcHAvZGIuc3FsaXRlXG52b2x1bWVzOlxuICBzbmFwcC1kYjoge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG50b2tlbl9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInNuYXBwXCIgXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkRBVEFCQVNFX1VSTCA9IFwiZmlsZTouL2RiLnNxbGl0ZVwiXG5EQVRBQkFTRV9QUk9WSURFUiA9IFwic3FsaXRlXCIgIyBPcHRpb25zOiBwb3N0Z3JlcyB8IG15c3FsIHwgc3FsaXRlXG5ESVNBQkxFRF9FTUFJTF9BTkRfUEFTU1dPUkQgPSBcImZhbHNlXCJcbkxPR19MRVZFTCA9IFwiZGVidWdcIlxuT1JJR0lOID0gXCJodHRwOi8vJHttYWluX2RvbWFpbn1cIlxuUE9SVCA9IFwiMzAwMFwiXG5BRE1JTl9VU0VSTkFNRSA9IFwiYWRtaW5cIlxuQURNSU5fRU1BSUwgPSBcImluZm9AZXhhbXBsZS5vcmdcIlxuQURNSU5fUEFTU1dPUkQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcblRPS0VOX1NFQ1JFVCA9IFwiJHt0b2tlbl9zZWNyZXR9XCIgIyBBUEkgS2V5IGZvciBhdXRoZW50aWNhdGlvbiB0b2tlblxuRU5BQkxFX1NJR05VUCA9IFwidHJ1ZVwiXG5FTkFCTEVEX01GQSA9IFwiZmFsc2VcIlxuUFVCTElDX1VSTCA9IFwiJHttYWluX2RvbWFpbn1cIlxuQVBQTkFNRSA9IFwiU25hcHBcIlxuUFVCTElDX0VYVFJBX0dST1VQU19FRElUQUJMRSA9IFwidHJ1ZVwiXG5VUkxTX1ZJQV9HUk9VUFNfT05MWSA9IFwiZmFsc2VcIlxuSE9TVCA9IFwiMC4wLjAuMFwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL2ZpbGVzL3NuYXBwLWRiL2RiLnNxbGl0ZVwiXG5jb250ZW50ID0gXCJcIlwiXG4jIFNRTGl0ZSBkYXRhYmFzZSBmaWxlIGZvciBTbmFwcFxuXCJcIlwiIgp9
```

## Links

`screenshot`,`sharing`,`self-hosted`,`authentication`

---

Version:`0.9-rc-020`

SlashSlash is a modern, self-hosted bookmarking service and link shortener that helps you organize and share your favorite links.

SoketiSoketi is your simple, fast, and resilient open-source WebSockets server.

### On this page

ConfigurationBase64LinksTags