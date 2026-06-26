---
title: "Omni-Tools | Dokploy"
source: "https://docs.dokploy.com/docs/templates/omni-tools"
category: dokploy-docs
created: "2026-06-25T17:21:54.355Z"
---

Omni-Tools | Dokploy

# Omni-Tools

Copy as Markdown

Omni-Tools is a collection of useful tools in a single self-hosted web application.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  omni-tools:
    image: iib0011/omni-tools:latest
    restart: unless-stopped
    ports:
      - 80
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "omni-tools"
port = 80
host = "${main_domain}"

[config.env]
# API Key
LOCIZE_API_KEY = ""

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBvbW5pLXRvb2xzOlxuICAgIGltYWdlOiBpaWIwMDExL29tbmktdG9vbHM6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gODBcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJvbW5pLXRvb2xzXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbiMgQVBJIEtleVxuTE9DSVpFX0FQSV9LRVkgPSBcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG4iCn0=
```

## Links

`tools`,`utilities`,`collection`,`self-hosted`

---

Version:`latest`

Open Journal SystemsOpen Journal Systems (OJS) is a journal management and publishing system that has been developed by the Public Knowledge Project through its federally funded efforts to expand and improve access to research.

OneDevGit server with CI/CD, kanban, and packages. Seamless integration. Unparalleled experience.

### On this page

ConfigurationBase64LinksTags