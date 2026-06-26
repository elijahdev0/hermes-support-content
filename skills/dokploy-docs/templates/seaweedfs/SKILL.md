---
title: "SeaweedFS | Dokploy"
source: "https://docs.dokploy.com/docs/templates/seaweedfs"
category: dokploy-docs
created: "2026-06-25T17:21:59.113Z"
---

SeaweedFS | Dokploy

# SeaweedFS

Copy as Markdown

SeaweedFS is a fast distributed storage system for blobs, objects, and files. Features S3-compatible API, POSIX FUSE mount, and WebDAV support.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  master:
    image: chrislusf/seaweedfs:4.02
    command: >
      -v=0
      master
      -volumeSizeLimitMB=10240
      -ip=master
      -ip.bind=0.0.0.0
      -port=9333
      -mdir=/data/master
    volumes:
      - seaweedfs-master:/data/master
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://localhost:9333"]
      interval: 30s
      timeout: 10s
      retries: 3
    expose:
      - 9333
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M

  volume:
    image: chrislusf/seaweedfs:4.02
    command: >
      -v=0
      volume
      -mserver="master:9333"
      -port=8080
      -dir=/data/volume
      -max=100
    volumes:
      - seaweedfs-volume:/data/volume
    depends_on:
      master:
        condition: service_healthy
    restart: unless-stopped
    expose:
      - 8080
    deploy:
      resources:
        limits:
          memory: 1G
        reservations:
          memory: 512M

  filer:
    image: chrislusf/seaweedfs:4.02
    command: >
      -v=0
      filer
      -defaultReplicaPlacement=000
      -master="master:9333"
      -ip=filer
      -ip.bind=0.0.0.0
      -port=8888
    environment:
      - WEED_MASTER=master:9333
    volumes:
      - seaweedfs-filer:/data
    depends_on:
      - master
      - volume
    restart: unless-stopped
    # # Secure the GUI with username/password
    # labels:
    #   # htpasswd -nb admin admin
    #   - "traefik.http.middlewares.basic-auth.basicauth.users=admin:$$apr1$$aLLYxhdC$$ZAW26eJfBRC8qWjCkcZns."
    #   - "traefik.http.routers.service-name.middlewares=basic-auth"
    healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://localhost:8888"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          memory: 1G
        reservations:
          memory: 512M
    expose:
      - 8888

  s3:
    image: chrislusf/seaweedfs:4.02
    command: >
      -v=0
      s3
      -filer="filer:8888"
      -ip.bind=0.0.0.0
      -port=8333
    environment:
      - AWS_ACCESS_KEY_ID=${S3_ACCESS_KEY}
      - AWS_SECRET_ACCESS_KEY=${S3_SECRET_KEY}
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M
    expose:
      - 8333

volumes:
  seaweedfs-master:
  seaweedfs-volume:
  seaweedfs-filer:
```

```
[variables]
main_domain = "${domain}"
filer_domain = "filer.${domain}"
master_domain = "master.${domain}"
s3_domain = "s3.${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "filer"
port = 8888
host = "${filer_domain}"

[[config.domains]]
serviceName = "master"
port = 9333
host = "${master_domain}"

[[config.domains]]
serviceName = "s3"
port = 8333
host = "${s3_domain}"

[config.env]
S3_ACCESS_KEY = "admin"
S3_SECRET_KEY = "${password:16}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBtYXN0ZXI6XG4gICAgaW1hZ2U6IGNocmlzbHVzZi9zZWF3ZWVkZnM6NC4wMlxuICAgIGNvbW1hbmQ6ID5cbiAgICAgIC12PTBcbiAgICAgIG1hc3RlclxuICAgICAgLXZvbHVtZVNpemVMaW1pdE1CPTEwMjQwXG4gICAgICAtaXA9bWFzdGVyXG4gICAgICAtaXAuYmluZD0wLjAuMC4wXG4gICAgICAtcG9ydD05MzMzXG4gICAgICAtbWRpcj0vZGF0YS9tYXN0ZXJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBzZWF3ZWVkZnMtbWFzdGVyOi9kYXRhL21hc3RlclxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJ3Z2V0XCIsIFwiLXFcIiwgXCItLXNwaWRlclwiLCBcImh0dHA6Ly9sb2NhbGhvc3Q6OTMzM1wiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG4gICAgZXhwb3NlOlxuICAgICAgLSA5MzMzXG4gICAgZGVwbG95OlxuICAgICAgcmVzb3VyY2VzOlxuICAgICAgICBsaW1pdHM6XG4gICAgICAgICAgbWVtb3J5OiA1MTJNXG4gICAgICAgIHJlc2VydmF0aW9uczpcbiAgICAgICAgICBtZW1vcnk6IDI1Nk1cblxuICB2b2x1bWU6XG4gICAgaW1hZ2U6IGNocmlzbHVzZi9zZWF3ZWVkZnM6NC4wMlxuICAgIGNvbW1hbmQ6ID5cbiAgICAgIC12PTBcbiAgICAgIHZvbHVtZVxuICAgICAgLW1zZXJ2ZXI9XCJtYXN0ZXI6OTMzM1wiXG4gICAgICAtcG9ydD04MDgwXG4gICAgICAtZGlyPS9kYXRhL3ZvbHVtZVxuICAgICAgLW1heD0xMDBcbiAgICB2b2x1bWVzOlxuICAgICAgLSBzZWF3ZWVkZnMtdm9sdW1lOi9kYXRhL3ZvbHVtZVxuICAgIGRlcGVuZHNfb246XG4gICAgICBtYXN0ZXI6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBleHBvc2U6XG4gICAgICAtIDgwODBcbiAgICBkZXBsb3k6XG4gICAgICByZXNvdXJjZXM6XG4gICAgICAgIGxpbWl0czpcbiAgICAgICAgICBtZW1vcnk6IDFHXG4gICAgICAgIHJlc2VydmF0aW9uczpcbiAgICAgICAgICBtZW1vcnk6IDUxMk1cblxuICBmaWxlcjpcbiAgICBpbWFnZTogY2hyaXNsdXNmL3NlYXdlZWRmczo0LjAyXG4gICAgY29tbWFuZDogPlxuICAgICAgLXY9MFxuICAgICAgZmlsZXJcbiAgICAgIC1kZWZhdWx0UmVwbGljYVBsYWNlbWVudD0wMDBcbiAgICAgIC1tYXN0ZXI9XCJtYXN0ZXI6OTMzM1wiXG4gICAgICAtaXA9ZmlsZXJcbiAgICAgIC1pcC5iaW5kPTAuMC4wLjBcbiAgICAgIC1wb3J0PTg4ODhcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gV0VFRF9NQVNURVI9bWFzdGVyOjkzMzNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBzZWF3ZWVkZnMtZmlsZXI6L2RhdGFcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBtYXN0ZXJcbiAgICAgIC0gdm9sdW1lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICAjICMgU2VjdXJlIHRoZSBHVUkgd2l0aCB1c2VybmFtZS9wYXNzd29yZFxuICAgICMgbGFiZWxzOlxuICAgICMgICAjIGh0cGFzc3dkIC1uYiBhZG1pbiBhZG1pblxuICAgICMgICAtIFwidHJhZWZpay5odHRwLm1pZGRsZXdhcmVzLmJhc2ljLWF1dGguYmFzaWNhdXRoLnVzZXJzPWFkbWluOiQkYXByMSQkYUxMWXhoZEMkJFpBVzI2ZUpmQlJDOHFXakNrY1pucy5cIlxuICAgICMgICAtIFwidHJhZWZpay5odHRwLnJvdXRlcnMuc2VydmljZS1uYW1lLm1pZGRsZXdhcmVzPWJhc2ljLWF1dGhcIlxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwid2dldFwiLCBcIi1xXCIsIFwiLS1zcGlkZXJcIiwgXCJodHRwOi8vbG9jYWxob3N0Ojg4ODhcIl1cbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogM1xuICAgIGRlcGxveTpcbiAgICAgIHJlc291cmNlczpcbiAgICAgICAgbGltaXRzOlxuICAgICAgICAgIG1lbW9yeTogMUdcbiAgICAgICAgcmVzZXJ2YXRpb25zOlxuICAgICAgICAgIG1lbW9yeTogNTEyTVxuICAgIGV4cG9zZTpcbiAgICAgIC0gODg4OFxuXG4gIHMzOlxuICAgIGltYWdlOiBjaHJpc2x1c2Yvc2Vhd2VlZGZzOjQuMDJcbiAgICBjb21tYW5kOiA+XG4gICAgICAtdj0wXG4gICAgICBzM1xuICAgICAgLWZpbGVyPVwiZmlsZXI6ODg4OFwiXG4gICAgICAtaXAuYmluZD0wLjAuMC4wXG4gICAgICAtcG9ydD04MzMzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIEFXU19BQ0NFU1NfS0VZX0lEPSR7UzNfQUNDRVNTX0tFWX1cbiAgICAgIC0gQVdTX1NFQ1JFVF9BQ0NFU1NfS0VZPSR7UzNfU0VDUkVUX0tFWX1cbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGRlcGxveTpcbiAgICAgIHJlc291cmNlczpcbiAgICAgICAgbGltaXRzOlxuICAgICAgICAgIG1lbW9yeTogNTEyTVxuICAgICAgICByZXNlcnZhdGlvbnM6XG4gICAgICAgICAgbWVtb3J5OiAyNTZNXG4gICAgZXhwb3NlOlxuICAgICAgLSA4MzMzXG5cbnZvbHVtZXM6XG4gIHNlYXdlZWRmcy1tYXN0ZXI6XG4gIHNlYXdlZWRmcy12b2x1bWU6XG4gIHNlYXdlZWRmcy1maWxlcjpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5maWxlcl9kb21haW4gPSBcImZpbGVyLiR7ZG9tYWlufVwiXG5tYXN0ZXJfZG9tYWluID0gXCJtYXN0ZXIuJHtkb21haW59XCJcbnMzX2RvbWFpbiA9IFwiczMuJHtkb21haW59XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImZpbGVyXCJcbnBvcnQgPSA4ODg4XG5ob3N0ID0gXCIke2ZpbGVyX2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJtYXN0ZXJcIlxucG9ydCA9IDkzMzNcbmhvc3QgPSBcIiR7bWFzdGVyX2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJzM1wiXG5wb3J0ID0gODMzM1xuaG9zdCA9IFwiJHtzM19kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5TM19BQ0NFU1NfS0VZID0gXCJhZG1pblwiXG5TM19TRUNSRVRfS0VZID0gXCIke3Bhc3N3b3JkOjE2fVwiXG4iCn0=
```

## Links

`storage`,`s3`,`distributed`,`object-storage`,`file-system`

---

Version:`latest`

SearXNGSearXNG is a privacy-respecting, hackable metasearch engine that aggregates results from various search engines without tracking users.

ShlinkURL shortener that can be used to serve shortened URLs under your own domain.

### On this page

ConfigurationBase64LinksTags