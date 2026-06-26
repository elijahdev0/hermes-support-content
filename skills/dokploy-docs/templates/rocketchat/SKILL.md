---
title: "Rocketchat | Dokploy"
source: "https://docs.dokploy.com/docs/templates/rocketchat"
category: dokploy-docs
created: "2026-06-25T17:21:57.938Z"
---

Rocketchat | Dokploy

# Rocketchat

Copy as Markdown

Rocket.Chat is a free and open-source web chat platform that allows you to build and manage your own chat applications.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  rocketchat:
    image: registry.rocket.chat/rocketchat/rocket.chat:6.9.2
    restart: always
    environment:
      MONGO_URL: "mongodb://mongodb:27017/rocketchat?replicaSet=rs0"
      MONGO_OPLOG_URL: "mongodb://mongodb:27017/local?replicaSet=rs0"
      ROOT_URL: ${ROOT_URL:-http://${ROCKETCHAT_HOST}:${ROCKETCHAT_PORT}}
      PORT: ${ROCKETCHAT_PORT}
      DEPLOY_METHOD: docker
      DEPLOY_PLATFORM:
      REG_TOKEN:
    depends_on:
      - mongodb

  mongodb:
    image: docker.io/bitnami/mongodb:5.0
    restart: always
    volumes:
      - mongodb_data:/bitnami/mongodb
    environment:
      MONGODB_REPLICA_SET_MODE: primary
      MONGODB_REPLICA_SET_NAME: rs0
      MONGODB_PORT_NUMBER: 27017
      MONGODB_INITIAL_PRIMARY_HOST: mongodb
      MONGODB_INITIAL_PRIMARY_PORT_NUMBER: 27017
      MONGODB_ADVERTISED_HOSTNAME: mongodb
      MONGODB_ENABLE_JOURNAL: true
      ALLOW_EMPTY_PASSWORD: yes

volumes:
  mongodb_data: { driver: local }
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "rocketchat"
port = 3_000
host = "${main_domain}"

[config.env]
ROCKETCHAT_HOST = "${main_domain}"
ROCKETCHAT_PORT = "3000"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICByb2NrZXRjaGF0OlxuICAgIGltYWdlOiByZWdpc3RyeS5yb2NrZXQuY2hhdC9yb2NrZXRjaGF0L3JvY2tldC5jaGF0OjYuOS4yXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNT05HT19VUkw6IFwibW9uZ29kYjovL21vbmdvZGI6MjcwMTcvcm9ja2V0Y2hhdD9yZXBsaWNhU2V0PXJzMFwiXG4gICAgICBNT05HT19PUExPR19VUkw6IFwibW9uZ29kYjovL21vbmdvZGI6MjcwMTcvbG9jYWw/cmVwbGljYVNldD1yczBcIlxuICAgICAgUk9PVF9VUkw6ICR7Uk9PVF9VUkw6LWh0dHA6Ly8ke1JPQ0tFVENIQVRfSE9TVH06JHtST0NLRVRDSEFUX1BPUlR9fVxuICAgICAgUE9SVDogJHtST0NLRVRDSEFUX1BPUlR9XG4gICAgICBERVBMT1lfTUVUSE9EOiBkb2NrZXJcbiAgICAgIERFUExPWV9QTEFURk9STTpcbiAgICAgIFJFR19UT0tFTjpcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBtb25nb2RiXG5cbiAgbW9uZ29kYjpcbiAgICBpbWFnZTogZG9ja2VyLmlvL2JpdG5hbWkvbW9uZ29kYjo1LjBcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBtb25nb2RiX2RhdGE6L2JpdG5hbWkvbW9uZ29kYlxuICAgIGVudmlyb25tZW50OlxuICAgICAgTU9OR09EQl9SRVBMSUNBX1NFVF9NT0RFOiBwcmltYXJ5XG4gICAgICBNT05HT0RCX1JFUExJQ0FfU0VUX05BTUU6IHJzMFxuICAgICAgTU9OR09EQl9QT1JUX05VTUJFUjogMjcwMTdcbiAgICAgIE1PTkdPREJfSU5JVElBTF9QUklNQVJZX0hPU1Q6IG1vbmdvZGJcbiAgICAgIE1PTkdPREJfSU5JVElBTF9QUklNQVJZX1BPUlRfTlVNQkVSOiAyNzAxN1xuICAgICAgTU9OR09EQl9BRFZFUlRJU0VEX0hPU1ROQU1FOiBtb25nb2RiXG4gICAgICBNT05HT0RCX0VOQUJMRV9KT1VSTkFMOiB0cnVlXG4gICAgICBBTExPV19FTVBUWV9QQVNTV09SRDogeWVzXG5cblxudm9sdW1lczpcbiAgbW9uZ29kYl9kYXRhOiB7IGRyaXZlcjogbG9jYWwgfVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInJvY2tldGNoYXRcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuUk9DS0VUQ0hBVF9IT1NUID0gXCIke21haW5fZG9tYWlufVwiXG5ST0NLRVRDSEFUX1BPUlQgPSBcIjMwMDBcIlxuIgp9
```

## Links

`chat`

---

Version:`6.9.2`

Docker RegistryDistribution implementation for storing and distributing of Docker container images and artifacts.

RoteRote is an open-source multi-platform personal note system featuring an open API, full data ownership, and effortless Docker deployment.

### On this page

ConfigurationBase64LinksTags