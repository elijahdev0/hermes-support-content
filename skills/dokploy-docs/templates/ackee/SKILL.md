---
title: "Ackee | Dokploy"
source: "https://docs.dokploy.com/docs/templates/ackee"
category: dokploy-docs
created: "2026-06-25T17:21:40.413Z"
---

Ackee | Dokploy

# Ackee

Copy as Markdown

Ackee is a self-hosted analytics tool for your website.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  ackee:
    image: electerious/ackee:3.4.2
    ports:
      - "3000"
    environment:
      - ACKEE_USERNAME=${ACKEE_USERNAME}
      - ACKEE_PASSWORD=${ACKEE_PASSWORD}
      - ACKEE_MONGODB=${ACKEE_MONGODB}

  mongo:
    image: mongo:4
    environment:
      - MONGO_INITDB_ROOT_PASSWORD=${MONGO_INITDB_ROOT_PASSWORD}
      - MONGO_INITDB_ROOT_USERNAME=mongo
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```

```
[variables]
ACKEE_USERNAME = "default"
ACKEE_PASSWORD = "${password:16}"
MONGO_INITDB_ROOT_PASSWORD = "${password:16}"
ACKEE_MONGODB = "mongodb://mongo:${MONGO_INITDB_ROOT_PASSWORD}@mongo:27017"

[config]
[[config.domains]]
serviceName = "ackee"
port = 3000
host = "${domain}"

[config.env]
ACKEE_USERNAME = "${ACKEE_USERNAME}"
ACKEE_PASSWORD = "${ACKEE_PASSWORD}"
ACKEE_MONGODB = "${ACKEE_MONGODB}"
MONGO_INITDB_ROOT_PASSWORD = "${MONGO_INITDB_ROOT_PASSWORD}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBhY2tlZTpcbiAgICBpbWFnZTogZWxlY3RlcmlvdXMvYWNrZWU6My40LjJcbiAgICBwb3J0czpcbiAgICAgIC0gXCIzMDAwXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQUNLRUVfVVNFUk5BTUU9JHtBQ0tFRV9VU0VSTkFNRX1cbiAgICAgIC0gQUNLRUVfUEFTU1dPUkQ9JHtBQ0tFRV9QQVNTV09SRH1cbiAgICAgIC0gQUNLRUVfTU9OR09EQj0ke0FDS0VFX01PTkdPREJ9XG4gIFxuICBtb25nbzpcbiAgICBpbWFnZTogbW9uZ286NFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBNT05HT19JTklUREJfUk9PVF9QQVNTV09SRD0ke01PTkdPX0lOSVREQl9ST09UX1BBU1NXT1JEfVxuICAgICAgLSBNT05HT19JTklUREJfUk9PVF9VU0VSTkFNRT1tb25nb1xuICAgIHZvbHVtZXM6XG4gICAgICAtIG1vbmdvLWRhdGE6L2RhdGEvZGJcblxuXG52b2x1bWVzOlxuICBtb25nby1kYXRhOlxuICAgICBcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxuQUNLRUVfVVNFUk5BTUUgPSBcImRlZmF1bHRcIlxuQUNLRUVfUEFTU1dPUkQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbk1PTkdPX0lOSVREQl9ST09UX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5BQ0tFRV9NT05HT0RCID0gXCJtb25nb2RiOi8vbW9uZ286JHtNT05HT19JTklUREJfUk9PVF9QQVNTV09SRH1AbW9uZ286MjcwMTdcIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYWNrZWVcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7ZG9tYWlufVwiXG5cblxuW2NvbmZpZy5lbnZdXG5BQ0tFRV9VU0VSTkFNRSA9IFwiJHtBQ0tFRV9VU0VSTkFNRX1cIlxuQUNLRUVfUEFTU1dPUkQgPSBcIiR7QUNLRUVfUEFTU1dPUkR9XCJcbkFDS0VFX01PTkdPREIgPSBcIiR7QUNLRUVfTU9OR09EQn1cIlxuTU9OR09fSU5JVERCX1JPT1RfUEFTU1dPUkQgPSBcIiR7TU9OR09fSU5JVERCX1JPT1RfUEFTU1dPUkR9XCJcblxuIgp9
```

## Instructions

## Instructions

We don't have nothing to show here....

## Links

`analytics`,`self-hosted`

---

Version:`latest`

IntroductionBrowse our collection of 388+ self-hosted open source templates

ActivepiecesOpen-source no-code business automation tool. An alternative to Zapier, Make.com, and Tray.

### On this page

ConfigurationBase64InstructionsInstructionsLinksTags