---
title: "Appsmith | Dokploy"
source: "https://docs.dokploy.com/docs/templates/appsmith"
category: dokploy-docs
created: "2026-06-25T17:21:41.528Z"
---

Appsmith | Dokploy

# Appsmith

Copy as Markdown

Appsmith is a free and open source platform for building internal tools and applications.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  appsmith:
    image: appsmith/appsmith-ee:v1.94
    volumes:
      - appsmith-data:/appsmith-stacks
    restart: unless-stopped

volumes:
  appsmith-data:
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "appsmith"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhcHBzbWl0aDpcbiAgICBpbWFnZTogYXBwc21pdGgvYXBwc21pdGgtZWU6djEuOTRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBhcHBzbWl0aC1kYXRhOi9hcHBzbWl0aC1zdGFja3NcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG52b2x1bWVzOlxuICBhcHBzbWl0aC1kYXRhOiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYXBwc21pdGhcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`cms`

---

Version:`v1.94`

Apprise APIApprise API provides a simple interface for sending notifications to almost all of the most popular notification services available to us today.

AppwriteAppwrite is an end-to-end platform for building Web, Mobile, Native, or Backend apps, packaged as a set of Docker microservices. It includes both a backend server and a fully integrated hosting solution for deploying static and server-side rendered frontends. Appwrite abstracts the complexity and repetitiveness required to build modern apps from scratch and allows you to build secure, full-stack applications faster. Using Appwrite, you can easily integrate your app with user authentication and multiple sign-in methods, a database for storing and querying users and team data, storage and file management, image manipulation, Cloud Functions, messaging, and more services.

### On this page

ConfigurationBase64LinksTags