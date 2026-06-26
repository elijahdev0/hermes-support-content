---
title: "Confluence | Dokploy"
source: "https://docs.dokploy.com/docs/templates/confluence"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

Confluence | Dokploy

# Confluence

Copy as Markdown

Confluence is a powerful team collaboration and knowledge-sharing tool. It allows you to create, organize, and collaborate on content in a centralized space. Designed for project management, documentation, and team communication, Confluence helps streamline workflows and enhances productivity.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  confluence:
    image: atlassian/confluence-server:8.6-ubuntu-jdk17
    ports:
      - "8090"
    volumes:
      - confluence-data:/var/atlassian/application-data/confluence
    environment:
      - JVM_MINIMUM_MEMORY=${JVM_MIN_MEM}
      - JVM_MAXIMUM_MEMORY=${JVM_MAX_MEM}
      - CATALINA_CONNECTOR_PROXYNAME=${DOMAIN}
      - CATALINA_CONNECTOR_SCHEME=http
      - CATALINA_CONNECTOR_SECURE=true

volumes:
  confluence-data:
```

```
[variables]
DOMAIN = "${domain}"
JVM_MIN_MEM = "2048m"
JVM_MAX_MEM = "4096m"

[config]
[[config.domains]]
serviceName = "confluence"
port = 8090
host = "${DOMAIN}"

[config.env]
JVM_MINIMUM_MEMORY = "${JVM_MIN_MEM}"
JVM_MAXIMUM_MEMORY = "${JVM_MAX_MEM}"
CATALINA_CONNECTOR_PROXYNAME = "${DOMAIN}"
CATALINA_CONNECTOR_SCHEME = "http"
CATALINA_CONNECTOR_SECURE = "true"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBjb25mbHVlbmNlOlxuICAgIGltYWdlOiBhdGxhc3NpYW4vY29uZmx1ZW5jZS1zZXJ2ZXI6OC42LXVidW50dS1qZGsxN1xuICAgIHBvcnRzOlxuICAgICAgLSBcIjgwOTBcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIGNvbmZsdWVuY2UtZGF0YTovdmFyL2F0bGFzc2lhbi9hcHBsaWNhdGlvbi1kYXRhL2NvbmZsdWVuY2VcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gSlZNX01JTklNVU1fTUVNT1JZPSR7SlZNX01JTl9NRU19XG4gICAgICAtIEpWTV9NQVhJTVVNX01FTU9SWT0ke0pWTV9NQVhfTUVNfVxuICAgICAgLSBDQVRBTElOQV9DT05ORUNUT1JfUFJPWFlOQU1FPSR7RE9NQUlOfVxuICAgICAgLSBDQVRBTElOQV9DT05ORUNUT1JfU0NIRU1FPWh0dHBcbiAgICAgIC0gQ0FUQUxJTkFfQ09OTkVDVE9SX1NFQ1VSRT10cnVlXG5cbnZvbHVtZXM6XG4gIGNvbmZsdWVuY2UtZGF0YTogIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5ET01BSU4gPSBcIiR7ZG9tYWlufVwiXG5KVk1fTUlOX01FTSA9IFwiMjA0OG1cIlxuSlZNX01BWF9NRU0gPSBcIjQwOTZtXCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImNvbmZsdWVuY2VcIlxucG9ydCA9IDgwOTBcbmhvc3QgPSBcIiR7RE9NQUlOfVwiXG5cbltjb25maWcuZW52XVxuSlZNX01JTklNVU1fTUVNT1JZID0gXCIke0pWTV9NSU5fTUVNfVwiXG5KVk1fTUFYSU1VTV9NRU1PUlkgPSBcIiR7SlZNX01BWF9NRU19XCJcbkNBVEFMSU5BX0NPTk5FQ1RPUl9QUk9YWU5BTUUgPSBcIiR7RE9NQUlOfVwiXG5DQVRBTElOQV9DT05ORUNUT1JfU0NIRU1FID0gXCJodHRwXCJcbkNBVEFMSU5BX0NPTk5FQ1RPUl9TRUNVUkUgPSBcInRydWVcIiAiCn0=
```

## Links

`collaboration`,`documentation`,`productivity`,`project-management`

---

Version:`8.6`

ConduwuitWell-maintained, featureful Matrix chat homeserver (fork of Conduit)

ConvertXConvertX is a service for converting media files, with optional user registration and file management features.

### On this page

ConfigurationBase64LinksTags