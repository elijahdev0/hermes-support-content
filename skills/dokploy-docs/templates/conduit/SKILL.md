---
title: "Conduit | Dokploy"
source: "https://docs.dokploy.com/docs/templates/conduit"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

Conduit | Dokploy

# Conduit

Copy as Markdown

Conduit is a simple, fast and reliable chat server powered by Matrix

## Configuration

docker-compose.ymltemplate.toml

```
# From Conduit's official documentation: https://docs.conduit.rs/deploying/docker.html#docker-compose
version: '3'

services:
    homeserver:
        image: registry.gitlab.com/famedly/conduit/matrix-conduit:v0.9.0
        restart: unless-stopped
        volumes:
            - db:/var/lib/matrix-conduit/
        environment:
            CONDUIT_SERVER_NAME: ${MATRIX_SUBDOMAIN}
            CONDUIT_DATABASE_PATH: /var/lib/matrix-conduit/
            CONDUIT_DATABASE_BACKEND: rocksdb
            CONDUIT_PORT: 6167
            CONDUIT_MAX_REQUEST_SIZE: 20000000 # in bytes, ~20 MB
            CONDUIT_ALLOW_REGISTRATION: 'true'
            #CONDUIT_REGISTRATION_TOKEN: '' # require password for registration
            CONDUIT_ALLOW_FEDERATION: 'true'
            CONDUIT_ALLOW_CHECK_FOR_UPDATES: 'true'
            CONDUIT_TRUSTED_SERVERS: '["matrix.org"]'
            #CONDUIT_MAX_CONCURRENT_REQUESTS: 100
            CONDUIT_ADDRESS: 0.0.0.0
            CONDUIT_CONFIG: '' # Ignore this
volumes:
    db:
```

```
[variables]
main_domain = "${domain}"

[config]
env = ["MATRIX_SUBDOMAIN=${main_domain}"]
mounts = []

[[config.domains]]
serviceName = "homeserver"
port = 6_167
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgRnJvbSBDb25kdWl0J3Mgb2ZmaWNpYWwgZG9jdW1lbnRhdGlvbjogaHR0cHM6Ly9kb2NzLmNvbmR1aXQucnMvZGVwbG95aW5nL2RvY2tlci5odG1sI2RvY2tlci1jb21wb3NlXG52ZXJzaW9uOiAnMydcblxuc2VydmljZXM6XG4gICAgaG9tZXNlcnZlcjpcbiAgICAgICAgaW1hZ2U6IHJlZ2lzdHJ5LmdpdGxhYi5jb20vZmFtZWRseS9jb25kdWl0L21hdHJpeC1jb25kdWl0OnYwLjkuMFxuICAgICAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgICAgICB2b2x1bWVzOlxuICAgICAgICAgICAgLSBkYjovdmFyL2xpYi9tYXRyaXgtY29uZHVpdC9cbiAgICAgICAgZW52aXJvbm1lbnQ6XG4gICAgICAgICAgICBDT05EVUlUX1NFUlZFUl9OQU1FOiAke01BVFJJWF9TVUJET01BSU59XG4gICAgICAgICAgICBDT05EVUlUX0RBVEFCQVNFX1BBVEg6IC92YXIvbGliL21hdHJpeC1jb25kdWl0L1xuICAgICAgICAgICAgQ09ORFVJVF9EQVRBQkFTRV9CQUNLRU5EOiByb2Nrc2RiXG4gICAgICAgICAgICBDT05EVUlUX1BPUlQ6IDYxNjdcbiAgICAgICAgICAgIENPTkRVSVRfTUFYX1JFUVVFU1RfU0laRTogMjAwMDAwMDAgIyBpbiBieXRlcywgfjIwIE1CXG4gICAgICAgICAgICBDT05EVUlUX0FMTE9XX1JFR0lTVFJBVElPTjogJ3RydWUnXG4gICAgICAgICAgICAjQ09ORFVJVF9SRUdJU1RSQVRJT05fVE9LRU46ICcnICMgcmVxdWlyZSBwYXNzd29yZCBmb3IgcmVnaXN0cmF0aW9uXG4gICAgICAgICAgICBDT05EVUlUX0FMTE9XX0ZFREVSQVRJT046ICd0cnVlJ1xuICAgICAgICAgICAgQ09ORFVJVF9BTExPV19DSEVDS19GT1JfVVBEQVRFUzogJ3RydWUnXG4gICAgICAgICAgICBDT05EVUlUX1RSVVNURURfU0VSVkVSUzogJ1tcIm1hdHJpeC5vcmdcIl0nXG4gICAgICAgICAgICAjQ09ORFVJVF9NQVhfQ09OQ1VSUkVOVF9SRVFVRVNUUzogMTAwXG4gICAgICAgICAgICBDT05EVUlUX0FERFJFU1M6IDAuMC4wLjBcbiAgICAgICAgICAgIENPTkRVSVRfQ09ORklHOiAnJyAjIElnbm9yZSB0aGlzXG52b2x1bWVzOlxuICAgIGRiOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcIk1BVFJJWF9TVUJET01BSU49JHttYWluX2RvbWFpbn1cIl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImhvbWVzZXJ2ZXJcIlxucG9ydCA9IDZfMTY3XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`matrix`,`communication`

---

Version:`v0.9.0`

Commento++Commento++ is a free, open-source application designed to provide a fast, lightweight comments box that you can embed in your static website. It offers features like Markdown support, Disqus import, voting, automated spam detection, moderation tools, sticky comments, thread locking, and OAuth login.

ConduwuitWell-maintained, featureful Matrix chat homeserver (fork of Conduit)

### On this page

ConfigurationBase64LinksTags