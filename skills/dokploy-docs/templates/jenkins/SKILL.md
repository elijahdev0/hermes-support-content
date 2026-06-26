---
title: "jenkins | Dokploy"
source: "https://docs.dokploy.com/docs/templates/jenkins"
category: dokploy-docs
created: "2026-06-25T17:21:50.890Z"
---

jenkins | Dokploy

# jenkins

Copy as Markdown

Jenkins is a free, open-source automation server that helps developers build, test, and deploy software by automating repetitive tasks in the software delivery pipeline.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  jenkins:
    image: jenkins/jenkins:latest
    volumes:
      - jenkins-home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    ports:
      - 8080

volumes:
  jenkins-home: {}
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "jenkins"
port = 8080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGplbmtpbnM6XG4gICAgaW1hZ2U6IGplbmtpbnMvamVua2luczpsYXRlc3RcbiAgICB2b2x1bWVzOlxuICAgICAgLSBqZW5raW5zLWhvbWU6L3Zhci9qZW5raW5zX2hvbWVcbiAgICAgIC0gL3Zhci9ydW4vZG9ja2VyLnNvY2s6L3Zhci9ydW4vZG9ja2VyLnNvY2tcbiAgICBwb3J0czpcbiAgICAgIC0gODA4MFxuXG52b2x1bWVzOlxuICBqZW5raW5zLWhvbWU6IHt9IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IHt9XG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJqZW5raW5zXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbiIKfQ==
```

## Links

`ci-cd`,`devops`,`automation`,`pipelines`,`open-source`

---

Version:`latest`

jellyfinJellyfin is a Free Software Media System that puts you in control of managing and streaming your media.

KaneoKaneo - an open source project management platform focused on simplicity and efficiency. Self-host it, customize it, make it yours.

### On this page

ConfigurationBase64LinksTags