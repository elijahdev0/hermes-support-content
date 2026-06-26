---
title: "Cockpit | Dokploy"
source: "https://docs.dokploy.com/docs/templates/cockpit"
category: dokploy-docs
created: "2026-06-25T17:21:43.965Z"
---

Cockpit | Dokploy

# Cockpit

Copy as Markdown

Cockpit is a headless content platform designed to streamline the creation, connection, and delivery of content for creators, marketers, and developers. It is built with an API-first approach, enabling limitless digital solutions.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  cockpit:
    image: cockpithq/cockpit:core-2.11.0
    ports:
      - "80"
    environment:
      - COCKPIT_SESSION_NAME=cockpit
      - COCKPIT_SALT=${SALT}
      - COCKPIT_DATABASE_SERVER=mongodb://${MONGO_USERNAME}:${MONGO_PASSWORD}@mongo:27017
      - COCKPIT_DATABASE_NAME=cockpit
    volumes:
      - html:/var/www/html
      - data:/var/www/html/storage/data
    depends_on:
      - mongo

  mongo:
    image: mongo:4
    environment:
      - MONGO_INITDB_ROOT_PASSWORD=${MONGO_PASSWORD}
      - MONGO_INITDB_ROOT_USERNAME=${MONGO_USERNAME}
    volumes:
      - mongo-data:/data/db

volumes:
  html:
  data:
  mongo-data:
```

```
[variables]
SALT = "${password:32}"
MONGO_PASSWORD = "${password:16}"

[config]
[[config.domains]]
serviceName = "cockpit"
port = 80
host = "${domain}"

[config.env]
SALT = "${SALT}"
MONGO_PASSWORD = "${MONGO_PASSWORD}"
MONGO_USERNAME = "mongo"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBjb2NrcGl0OlxuICAgIGltYWdlOiBjb2NrcGl0aHEvY29ja3BpdDpjb3JlLTIuMTEuMFxuICAgIHBvcnRzOlxuICAgICAgLSBcIjgwXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQ09DS1BJVF9TRVNTSU9OX05BTUU9Y29ja3BpdFxuICAgICAgLSBDT0NLUElUX1NBTFQ9JHtTQUxUfVxuICAgICAgLSBDT0NLUElUX0RBVEFCQVNFX1NFUlZFUj1tb25nb2RiOi8vJHtNT05HT19VU0VSTkFNRX06JHtNT05HT19QQVNTV09SRH1AbW9uZ286MjcwMTdcbiAgICAgIC0gQ09DS1BJVF9EQVRBQkFTRV9OQU1FPWNvY2twaXRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBodG1sOi92YXIvd3d3L2h0bWxcbiAgICAgIC0gZGF0YTovdmFyL3d3dy9odG1sL3N0b3JhZ2UvZGF0YVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIG1vbmdvXG5cbiAgbW9uZ286XG4gICAgaW1hZ2U6IG1vbmdvOjRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTU9OR09fSU5JVERCX1JPT1RfUEFTU1dPUkQ9JHtNT05HT19QQVNTV09SRH1cbiAgICAgIC0gTU9OR09fSU5JVERCX1JPT1RfVVNFUk5BTUU9JHtNT05HT19VU0VSTkFNRX1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBtb25nby1kYXRhOi9kYXRhL2RiXG5cbnZvbHVtZXM6XG4gIGh0bWw6XG4gIGRhdGE6XG4gIG1vbmdvLWRhdGE6ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxuU0FMVCA9IFwiJHtwYXNzd29yZDozMn1cIlxuTU9OR09fUEFTU1dPUkQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcblxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY29ja3BpdFwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuU0FMVCA9IFwiJHtTQUxUfVwiXG5NT05HT19QQVNTV09SRCA9IFwiJHtNT05HT19QQVNTV09SRH1cIiBcbk1PTkdPX1VTRVJOQU1FID0gXCJtb25nb1wiIgp9
```

## Links

`cms`,`content-management`,`api`

---

Version:`core-2.11.0`

CloudreveSelf-hosted file management and sharing system with multi-cloud storage support. Compatible with local, OneDrive, S3, and various cloud providers.

CoderCoder is an open-source cloud development environment (CDE) that you host in your cloud or on-premises.

### On this page

ConfigurationBase64LinksTags