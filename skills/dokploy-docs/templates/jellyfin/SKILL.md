---
title: "jellyfin | Dokploy"
source: "https://docs.dokploy.com/docs/templates/jellyfin"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

jellyfin | Dokploy

# jellyfin

Copy as Markdown

Jellyfin is a Free Software Media System that puts you in control of managing and streaming your media.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  jellyfin:
    image: jellyfin/jellyfin:10
    volumes:
      - config:/config
      - cache:/cache
      - media:/media
    restart: "unless-stopped"
    # Optional - alternative address used for autodiscovery
    environment:
      - JELLYFIN_PublishedServerUrl=http://${JELLYFIN_HOST}
    # Optional - may be necessary for docker healthcheck to pass if running in host network mode
    extra_hosts:
      - "host.docker.internal:host-gateway"
volumes:
  config:
  cache:
  media:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "jellyfin"
port = 8_096
host = "${main_domain}"

[config.env]
JELLYFIN_HOST = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBqZWxseWZpbjpcbiAgICBpbWFnZTogamVsbHlmaW4vamVsbHlmaW46MTBcbiAgICB2b2x1bWVzOlxuICAgICAgLSBjb25maWc6L2NvbmZpZ1xuICAgICAgLSBjYWNoZTovY2FjaGVcbiAgICAgIC0gbWVkaWE6L21lZGlhXG4gICAgcmVzdGFydDogXCJ1bmxlc3Mtc3RvcHBlZFwiXG4gICAgIyBPcHRpb25hbCAtIGFsdGVybmF0aXZlIGFkZHJlc3MgdXNlZCBmb3IgYXV0b2Rpc2NvdmVyeVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBKRUxMWUZJTl9QdWJsaXNoZWRTZXJ2ZXJVcmw9aHR0cDovLyR7SkVMTFlGSU5fSE9TVH1cbiAgICAjIE9wdGlvbmFsIC0gbWF5IGJlIG5lY2Vzc2FyeSBmb3IgZG9ja2VyIGhlYWx0aGNoZWNrIHRvIHBhc3MgaWYgcnVubmluZyBpbiBob3N0IG5ldHdvcmsgbW9kZVxuICAgIGV4dHJhX2hvc3RzOlxuICAgICAgLSBcImhvc3QuZG9ja2VyLmludGVybmFsOmhvc3QtZ2F0ZXdheVwiXG52b2x1bWVzOlxuICBjb25maWc6XG4gIGNhY2hlOlxuICBtZWRpYTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJqZWxseWZpblwiXG5wb3J0ID0gOF8wOTZcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5KRUxMWUZJTl9IT1NUID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`media system`

---

Version:`v10.9.7`

Java Runtime (Multi-Version)Configurable Java runtime environment supporting versions 8, 11, 16, 17, and 21. Perfect for Minecraft servers, Spring Boot apps, and custom Java applications.

jenkinsJenkins is a free, open-source automation server that helps developers build, test, and deploy software by automating repetitive tasks in the software delivery pipeline.

### On this page

ConfigurationBase64LinksTags