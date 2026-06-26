---
title: "StreamFlow | Dokploy"
source: "https://docs.dokploy.com/docs/templates/streamflow"
category: dokploy-docs
created: "2026-06-25T17:21:59.115Z"
---

StreamFlow | Dokploy

# StreamFlow

Copy as Markdown

StreamFlow is a multi-platform live streaming web application that enables simultaneous RTMP streaming to YouTube, Facebook, and other platforms with video gallery, scheduled streaming, and real-time monitoring.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  streamflow:
    build:
      context: https://github.com/bangtutorial/streamflow.git
    restart: unless-stopped
    environment:
      - PORT=7575
      - SESSION_SECRET=${SESSION_SECRET}
      - NODE_ENV=production
      - TZ=${TIMEZONE}
    volumes:
      - streamflow-db:/app/db
      - streamflow-logs:/app/logs
      - streamflow-uploads:/app/public/uploads
    ports:
      - 7575

volumes:
  streamflow-db: {}
  streamflow-logs: {}
  streamflow-uploads: {}
```

```
[variables]
main_domain = "${domain}"
session_secret = "${password:64}"

[config]
[[config.domains]]
serviceName = "streamflow"
port = 7575
host = "${main_domain}"

[config.env]
SESSION_SECRET = "${session_secret}"
TIMEZONE = "Asia/Jakarta"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBzdHJlYW1mbG93OlxuICAgIGJ1aWxkOlxuICAgICAgY29udGV4dDogaHR0cHM6Ly9naXRodWIuY29tL2Jhbmd0dXRvcmlhbC9zdHJlYW1mbG93LmdpdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPUlQ9NzU3NVxuICAgICAgLSBTRVNTSU9OX1NFQ1JFVD0ke1NFU1NJT05fU0VDUkVUfVxuICAgICAgLSBOT0RFX0VOVj1wcm9kdWN0aW9uXG4gICAgICAtIFRaPSR7VElNRVpPTkV9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gc3RyZWFtZmxvdy1kYjovYXBwL2RiXG4gICAgICAtIHN0cmVhbWZsb3ctbG9nczovYXBwL2xvZ3NcbiAgICAgIC0gc3RyZWFtZmxvdy11cGxvYWRzOi9hcHAvcHVibGljL3VwbG9hZHNcbiAgICBwb3J0czpcbiAgICAgIC0gNzU3NVxuXG52b2x1bWVzOlxuICBzdHJlYW1mbG93LWRiOiB7fVxuICBzdHJlYW1mbG93LWxvZ3M6IHt9XG4gIHN0cmVhbWZsb3ctdXBsb2Fkczoge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5zZXNzaW9uX3NlY3JldCA9IFwiJHtwYXNzd29yZDo2NH1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwic3RyZWFtZmxvd1wiXG5wb3J0ID0gNzU3NVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblNFU1NJT05fU0VDUkVUID0gXCIke3Nlc3Npb25fc2VjcmV0fVwiXG5USU1FWk9ORSA9IFwiQXNpYS9KYWthcnRhXCJcblxuW1tjb25maWcubW91bnRzXV1cbiIKfQ==
```

## Links

`streaming`,`rtmp`,`video`,`live-streaming`,`media`

---

Version:`2.1`

StrapiOpen-source headless CMS to build powerful APIs with built-in content management.

StrapiOpen-source headless CMS to build powerful APIs with built-in content management.

### On this page

ConfigurationBase64LinksTags