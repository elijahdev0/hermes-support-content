---
title: "Scrypted | Dokploy"
source: "https://docs.dokploy.com/docs/templates/scrypted"
category: dokploy-docs
created: "2026-06-25T17:21:59.113Z"
---

Scrypted | Dokploy

# Scrypted

Copy as Markdown

Scrypted is a home automation platform that integrates with various smart home devices and provides NVR capabilities for video surveillance.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  scrypted:
    image: ghcr.io/koush/scrypted:latest
    environment:
      - SCRYPTED_WEBHOOK_UPDATE_AUTHORIZATION=${SCRYPTED_WEBHOOK_UPDATE_AUTHORIZATION}
      - SCRYPTED_WEBHOOK_UPDATE=http://${main_domain}:10444/v1/update
    volumes:
      - ../files/scrypted-volume:/server/volume
      # Optional NVR volume, uncomment if needed
      # - ../files/nvr:/nvr
    restart: unless-stopped
    logging:
      driver: "none"
```

```
[variables]
main_domain = "${domain}"
SCRYPTED_WEBHOOK_UPDATE_AUTHORIZATION = "${password:32}"

[config]
[[config.domains]]
serviceName = "scrypted"
port = 11080
host = "${main_domain}"

[config.env]
# Scrypted service environment variables
# SCRYPTED_WEBHOOK_UPDATE_AUTHORIZATION: API key for Scrypted webhook updates
SCRYPTED_WEBHOOK_UPDATE_AUTHORIZATION = "${SCRYPTED_WEBHOOK_UPDATE_AUTHORIZATION}"
SCRYPTED_WEBHOOK_UPDATE = "http://${main_domain}:10444/v1/update"

[[config.mounts]]
filePath = "/files/scrypted-volume"
content = ""

# Optional NVR volume, uncomment if needed
# [[config.mounts]]
# filePath = "/files/nvr"
# content = ""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBzY3J5cHRlZDpcbiAgICBpbWFnZTogZ2hjci5pby9rb3VzaC9zY3J5cHRlZDpsYXRlc3RcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gU0NSWVBURURfV0VCSE9PS19VUERBVEVfQVVUSE9SSVpBVElPTj0ke1NDUllQVEVEX1dFQkhPT0tfVVBEQVRFX0FVVEhPUklaQVRJT059XG4gICAgICAtIFNDUllQVEVEX1dFQkhPT0tfVVBEQVRFPWh0dHA6Ly8ke21haW5fZG9tYWlufToxMDQ0NC92MS91cGRhdGVcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9zY3J5cHRlZC12b2x1bWU6L3NlcnZlci92b2x1bWVcbiAgICAgICMgT3B0aW9uYWwgTlZSIHZvbHVtZSwgdW5jb21tZW50IGlmIG5lZWRlZFxuICAgICAgIyAtIC4uL2ZpbGVzL252cjovbnZyXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBsb2dnaW5nOlxuICAgICAgZHJpdmVyOiBcIm5vbmVcIlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblNDUllQVEVEX1dFQkhPT0tfVVBEQVRFX0FVVEhPUklaQVRJT04gPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInNjcnlwdGVkXCJcbnBvcnQgPSAxMTA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbiMgU2NyeXB0ZWQgc2VydmljZSBlbnZpcm9ubWVudCB2YXJpYWJsZXNcbiMgU0NSWVBURURfV0VCSE9PS19VUERBVEVfQVVUSE9SSVpBVElPTjogQVBJIGtleSBmb3IgU2NyeXB0ZWQgd2ViaG9vayB1cGRhdGVzXG5TQ1JZUFRFRF9XRUJIT09LX1VQREFURV9BVVRIT1JJWkFUSU9OID0gXCIke1NDUllQVEVEX1dFQkhPT0tfVVBEQVRFX0FVVEhPUklaQVRJT059XCJcblNDUllQVEVEX1dFQkhPT0tfVVBEQVRFID0gXCJodHRwOi8vJHttYWluX2RvbWFpbn06MTA0NDQvdjEvdXBkYXRlXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvZmlsZXMvc2NyeXB0ZWQtdm9sdW1lXCJcbmNvbnRlbnQgPSBcIlwiXG5cbiMgT3B0aW9uYWwgTlZSIHZvbHVtZSwgdW5jb21tZW50IGlmIG5lZWRlZFxuIyBbW2NvbmZpZy5tb3VudHNdXVxuIyBmaWxlUGF0aCA9IFwiL2ZpbGVzL252clwiXG4jIGNvbnRlbnQgPSBcIlwiIgp9
```

## Links

`home-automation`,`nvr`,`smart-home`,`surveillance`

---

Version:`latest`

ScrutinyHard Drive S.M.A.R.T Monitoring, Historical Trends & Real World Failure Thresholds

SeafileOpen source cloud storage system for file sync, share and document collaboration

### On this page

ConfigurationBase64LinksTags