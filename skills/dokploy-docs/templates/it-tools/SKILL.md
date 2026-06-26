---
title: "IT Tools | Dokploy"
source: "https://docs.dokploy.com/docs/templates/it-tools"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

IT Tools | Dokploy

# IT Tools

Copy as Markdown

A collection of handy online it-tools for developers.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  it-tools:
    image: corentinth/it-tools:latest
    healthcheck:
      test: ["CMD", "curl", "-f", "http://127.0.0.1:80"]
      interval: 30s
      timeout: 10s
      retries: 3
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "it-tools"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBpdC10b29sczpcbiAgICBpbWFnZTogY29yZW50aW50aC9pdC10b29sczpsYXRlc3RcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcImN1cmxcIiwgXCItZlwiLCBcImh0dHA6Ly8xMjcuMC4wLjE6ODBcIl1cbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogM1xuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IHt9XG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJpdC10b29sc1wiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`developer`,`tools`

---

Version:`latest`

IPFS (Kubo)IPFS (Kubo) is a decentralized peer-to-peer file sharing and storage network node. Host your own IPFS gateway and API.

Java Runtime (Multi-Version)Configurable Java runtime environment supporting versions 8, 11, 16, 17, and 21. Perfect for Minecraft servers, Spring Boot apps, and custom Java applications.

### On this page

ConfigurationBase64LinksTags