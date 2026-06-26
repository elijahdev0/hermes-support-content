---
title: "Linkding | Dokploy"
source: "https://docs.dokploy.com/docs/templates/linkding"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

Linkding | Dokploy

# Linkding

Copy as Markdown

Linkding is a self-hosted bookmark manager with a clean and simple interface.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  linkding:
    image: sissbruecker/linkding:latest
    restart: unless-stopped
    ports:
      - 9090
    volumes:
      - ../files/linkding-data:/etc/linkding/data
```

```
[variables]
main_domain = "${domain}"
superuser_password = "${password:32}"
csrf_trusted_origins = "${domain}"
db_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "linkding"
port = 9090
host = "${main_domain}"

[config.env]
LD_CONTEXT_PATH = ""
LD_SUPERUSER_NAME = ""
LD_SUPERUSER_PASSWORD = "${superuser_password}"
LD_DISABLE_BACKGROUND_TASKS = "False"
LD_DISABLE_URL_VALIDATION = "False"
LD_ENABLE_AUTH_PROXY = "False"
LD_AUTH_PROXY_USERNAME_HEADER = ""
LD_AUTH_PROXY_LOGOUT_URL = ""
LD_CSRF_TRUSTED_ORIGINS = "${csrf_trusted_origins}"
LD_DB_ENGINE = ""
LD_DB_DATABASE = ""
LD_DB_USER = ""
LD_DB_PASSWORD = "${db_password}"
LD_DB_HOST = ""
LD_DB_PORT = ""
LD_DB_OPTIONS = "{}"

[[config.mounts]]
filePath = "/files/linkding-data"
content = ""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBsaW5rZGluZzpcbiAgICBpbWFnZTogc2lzc2JydWVja2VyL2xpbmtkaW5nOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDkwOTBcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9saW5rZGluZy1kYXRhOi9ldGMvbGlua2RpbmcvZGF0YVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnN1cGVydXNlcl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuY3NyZl90cnVzdGVkX29yaWdpbnMgPSBcIiR7ZG9tYWlufVwiXG5kYl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibGlua2RpbmdcIlxucG9ydCA9IDkwOTBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5MRF9DT05URVhUX1BBVEggPSBcIlwiXG5MRF9TVVBFUlVTRVJfTkFNRSA9IFwiXCJcbkxEX1NVUEVSVVNFUl9QQVNTV09SRCA9IFwiJHtzdXBlcnVzZXJfcGFzc3dvcmR9XCJcbkxEX0RJU0FCTEVfQkFDS0dST1VORF9UQVNLUyA9IFwiRmFsc2VcIlxuTERfRElTQUJMRV9VUkxfVkFMSURBVElPTiA9IFwiRmFsc2VcIlxuTERfRU5BQkxFX0FVVEhfUFJPWFkgPSBcIkZhbHNlXCJcbkxEX0FVVEhfUFJPWFlfVVNFUk5BTUVfSEVBREVSID0gXCJcIlxuTERfQVVUSF9QUk9YWV9MT0dPVVRfVVJMID0gXCJcIlxuTERfQ1NSRl9UUlVTVEVEX09SSUdJTlMgPSBcIiR7Y3NyZl90cnVzdGVkX29yaWdpbnN9XCJcbkxEX0RCX0VOR0lORSA9IFwiXCJcbkxEX0RCX0RBVEFCQVNFID0gXCJcIlxuTERfREJfVVNFUiA9IFwiXCJcbkxEX0RCX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiXG5MRF9EQl9IT1NUID0gXCJcIlxuTERfREJfUE9SVCA9IFwiXCJcbkxEX0RCX09QVElPTlMgPSBcInt9XCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvZmlsZXMvbGlua2RpbmctZGF0YVwiXG5jb250ZW50ID0gXCJcIiIKfQ==
```

## Links

`bookmark-manager`,`self-hosted`

---

Version:`latest`

LibreTranslateLibreTranslate is a free and open-source machine translation API, powered by Argos Translate. Self-hosted, no external dependencies, and supports multiple languages.

LinkStackLinkStack is an open-source link-in-bio platform for sharing multiple links using a customizable landing page.

### On this page

ConfigurationBase64LinksTags