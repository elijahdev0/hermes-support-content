---
title: "Minio | Dokploy"
source: "https://docs.dokploy.com/docs/templates/minio"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

Minio | Dokploy

# Minio

Copy as Markdown

Minio is an open source object storage server compatible with Amazon S3 cloud storage service.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  minio:
    # after RELEASE.2025-04-22T22-12-26Z, minio removed most of the admin UI, if you want to use the admin UI, uncomment the line below
    # image: minio/minio:RELEASE.2025-04-22T22-12-26Z
    # if you uncommented the line above, comment the line below
    image: minio/minio
    restart: unless-stopped
    volumes:
      # by default, the MinIO container will use a volume named minio-data
      # to store its data. This volume is created automatically by Docker.
      # If you want to use a local directory instead, uncomment the line below
      # and specify the path to your local directory.
      # (be warned that ../files is pointing to a subdirectory of /etc/dokploy/compose in dokploy)
      # - ../files/minio-data:/data
      # if you uncommented the line above, comment the line below and the volumes section at the end
      - minio-data:/data
    environment:
      - MINIO_ROOT_USER=${MINIO_ROOT_USER}
      - MINIO_ROOT_PASSWORD=${MINIO_ROOT_PASSWORD}
      - MINIO_BROWSER_REDIRECT_URL=${MINIO_BROWSER_REDIRECT_URL}
    command: server /data --console-address ":9001"
    ports:
      # by default, the MinIO container will use port 9000 to expose its API
      # and port 9001 to expose its web console
      # minio requires port to be specified when making a request to the API
      - 9000:9000
    expose:
      - 9001

# comment the line below if you specified a local directory in the volumes section of the minio service
volumes:
  minio-data:
```

```
[variables]
main_domain = "${domain}"
api_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "minio"
port = 9_001
host = "${main_domain}"

[config.env]
MINIO_ROOT_USER = "minioadmin"
MINIO_ROOT_PASSWORD = "${password:16}"
MINIO_BROWSER_REDIRECT_URL = "http://${main_domain}"
MINIO_BROWSER_REDIRECT = "false"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBtaW5pbzpcbiAgICAjIGFmdGVyIFJFTEVBU0UuMjAyNS0wNC0yMlQyMi0xMi0yNlosIG1pbmlvIHJlbW92ZWQgbW9zdCBvZiB0aGUgYWRtaW4gVUksIGlmIHlvdSB3YW50IHRvIHVzZSB0aGUgYWRtaW4gVUksIHVuY29tbWVudCB0aGUgbGluZSBiZWxvd1xuICAgICMgaW1hZ2U6IG1pbmlvL21pbmlvOlJFTEVBU0UuMjAyNS0wNC0yMlQyMi0xMi0yNlpcbiAgICAjIGlmIHlvdSB1bmNvbW1lbnRlZCB0aGUgbGluZSBhYm92ZSwgY29tbWVudCB0aGUgbGluZSBiZWxvd1xuICAgIGltYWdlOiBtaW5pby9taW5pb1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgICMgYnkgZGVmYXVsdCwgdGhlIE1pbklPIGNvbnRhaW5lciB3aWxsIHVzZSBhIHZvbHVtZSBuYW1lZCBtaW5pby1kYXRhXG4gICAgICAjIHRvIHN0b3JlIGl0cyBkYXRhLiBUaGlzIHZvbHVtZSBpcyBjcmVhdGVkIGF1dG9tYXRpY2FsbHkgYnkgRG9ja2VyLlxuICAgICAgIyBJZiB5b3Ugd2FudCB0byB1c2UgYSBsb2NhbCBkaXJlY3RvcnkgaW5zdGVhZCwgdW5jb21tZW50IHRoZSBsaW5lIGJlbG93XG4gICAgICAjIGFuZCBzcGVjaWZ5IHRoZSBwYXRoIHRvIHlvdXIgbG9jYWwgZGlyZWN0b3J5LlxuICAgICAgIyAoYmUgd2FybmVkIHRoYXQgLi4vZmlsZXMgaXMgcG9pbnRpbmcgdG8gYSBzdWJkaXJlY3Rvcnkgb2YgL2V0Yy9kb2twbG95L2NvbXBvc2UgaW4gZG9rcGxveSlcbiAgICAgICMgLSAuLi9maWxlcy9taW5pby1kYXRhOi9kYXRhXG4gICAgICAjIGlmIHlvdSB1bmNvbW1lbnRlZCB0aGUgbGluZSBhYm92ZSwgY29tbWVudCB0aGUgbGluZSBiZWxvdyBhbmQgdGhlIHZvbHVtZXMgc2VjdGlvbiBhdCB0aGUgZW5kXG4gICAgICAtIG1pbmlvLWRhdGE6L2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTUlOSU9fUk9PVF9VU0VSPSR7TUlOSU9fUk9PVF9VU0VSfVxuICAgICAgLSBNSU5JT19ST09UX1BBU1NXT1JEPSR7TUlOSU9fUk9PVF9QQVNTV09SRH1cbiAgICAgIC0gTUlOSU9fQlJPV1NFUl9SRURJUkVDVF9VUkw9JHtNSU5JT19CUk9XU0VSX1JFRElSRUNUX1VSTH1cbiAgICBjb21tYW5kOiBzZXJ2ZXIgL2RhdGEgLS1jb25zb2xlLWFkZHJlc3MgXCI6OTAwMVwiXG4gICAgcG9ydHM6XG4gICAgICAjIGJ5IGRlZmF1bHQsIHRoZSBNaW5JTyBjb250YWluZXIgd2lsbCB1c2UgcG9ydCA5MDAwIHRvIGV4cG9zZSBpdHMgQVBJXG4gICAgICAjIGFuZCBwb3J0IDkwMDEgdG8gZXhwb3NlIGl0cyB3ZWIgY29uc29sZVxuICAgICAgIyBtaW5pbyByZXF1aXJlcyBwb3J0IHRvIGJlIHNwZWNpZmllZCB3aGVuIG1ha2luZyBhIHJlcXVlc3QgdG8gdGhlIEFQSVxuICAgICAgLSA5MDAwOjkwMDBcbiAgICBleHBvc2U6XG4gICAgICAtIDkwMDFcblxuIyBjb21tZW50IHRoZSBsaW5lIGJlbG93IGlmIHlvdSBzcGVjaWZpZWQgYSBsb2NhbCBkaXJlY3RvcnkgaW4gdGhlIHZvbHVtZXMgc2VjdGlvbiBvZiB0aGUgbWluaW8gc2VydmljZVxudm9sdW1lczpcbiAgbWluaW8tZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5hcGlfZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibWluaW9cIlxucG9ydCA9IDlfMDAxXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuTUlOSU9fUk9PVF9VU0VSID0gXCJtaW5pb2FkbWluXCJcbk1JTklPX1JPT1RfUEFTU1dPUkQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbk1JTklPX0JST1dTRVJfUkVESVJFQ1RfVVJMID0gXCJodHRwOi8vJHttYWluX2RvbWFpbn1cIlxuTUlOSU9fQlJPV1NFUl9SRURJUkVDVCA9IFwiZmFsc2VcIlxuIgp9
```

## Links

`storage`

---

Version:`latest`

MinepanelWeb panel for managing Minecraft servers with Docker. Create, configure, start/stop, and monitor multiple instances from a modern UI.

Misaka Danmu ServerA self-hosted danmaku (bullet comments) server for live streaming and video platforms.

### On this page

ConfigurationBase64LinksTags