---
title: "Unifi Network | Dokploy"
source: "https://docs.dokploy.com/docs/templates/unifi"
category: dokploy-docs
created: "2026-06-25T17:22:01.419Z"
---

Unifi Network | Dokploy

# Unifi Network

Copy as Markdown

Unifi Network is an open-source enterprise network management platform for wireless networks.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  unifi-network-application:
    image: lscr.io/linuxserver/unifi-network-application:latest
    environment:
      - PUID=1000 # User ID
      - PGID=1000 # Group ID
      - TZ=Etc/UTC # Timezone
      - MONGO_HOST=unifi-db
      - MONGO_USER=unifi
      - MONGO_PASS=unifi_password
      - MONGO_PORT=27017
      - MONGO_DBNAME=unifi
      - MEM_LIMIT=1024
      - MEM_STARTUP=1024
      - MONGO_TLS= #optional  # MongoDB TLS setting
      - MONGO_AUTHSOURCE= #optional  # MongoDB authentication source
    volumes: # Volumes to mount in the container
      - ../files/config:/config # Map host directory to container directory
    ports:
      - 8443:8443 # HTTPS portal
      # - 3478:3478/udp # STUN service
      # - 10001:10001/udp # UniFi AP discovery
      # - 8080:8080 # HTTP portal
      # - 1900:1900/udp #optional  # For DLNA
      # - 8843:8843 #optional  # HTTPS guest portal
      # - 8880:8880 #optional  # HTTP guest portal
      # - 6789:6789 #optional  # Mobile speed test port
      # - 5514:5514/udp #optional  # Remote syslog port
    restart: unless-stopped
    depends_on:
      - unifi-db

  unifi-db:
    image: mongo:4.4
    volumes:
      - ../files/db/data:/data/db
      - ../files/init-mongo.sh:/docker-entrypoint-initdb.d/init-mongo.sh:ro
    ports:
      - 27017
    restart: unless-stopped
```

```
variables = {}

[config]
domains = []
env = {}

[[config.mounts]]
filePath = "init-mongo.sh"
content = """
#!/bin/bash
mongo <<EOF
use unifi
db.createUser({
user: "unifi",
pwd: "unifi_password",
roles: [
    { db: "unifi", role: "dbOwner" },
    { db: "unifi_stat", role: "dbOwner" }
]
})
EOF
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB1bmlmaS1uZXR3b3JrLWFwcGxpY2F0aW9uOlxuICAgIGltYWdlOiBsc2NyLmlvL2xpbnV4c2VydmVyL3VuaWZpLW5ldHdvcmstYXBwbGljYXRpb246bGF0ZXN0XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBVSUQ9MTAwMCAjIFVzZXIgSURcbiAgICAgIC0gUEdJRD0xMDAwICMgR3JvdXAgSURcbiAgICAgIC0gVFo9RXRjL1VUQyAjIFRpbWV6b25lXG4gICAgICAtIE1PTkdPX0hPU1Q9dW5pZmktZGJcbiAgICAgIC0gTU9OR09fVVNFUj11bmlmaVxuICAgICAgLSBNT05HT19QQVNTPXVuaWZpX3Bhc3N3b3JkXG4gICAgICAtIE1PTkdPX1BPUlQ9MjcwMTdcbiAgICAgIC0gTU9OR09fREJOQU1FPXVuaWZpXG4gICAgICAtIE1FTV9MSU1JVD0xMDI0XG4gICAgICAtIE1FTV9TVEFSVFVQPTEwMjRcbiAgICAgIC0gTU9OR09fVExTPSAjb3B0aW9uYWwgICMgTW9uZ29EQiBUTFMgc2V0dGluZ1xuICAgICAgLSBNT05HT19BVVRIU09VUkNFPSAjb3B0aW9uYWwgICMgTW9uZ29EQiBhdXRoZW50aWNhdGlvbiBzb3VyY2VcbiAgICB2b2x1bWVzOiAjIFZvbHVtZXMgdG8gbW91bnQgaW4gdGhlIGNvbnRhaW5lclxuICAgICAgLSAuLi9maWxlcy9jb25maWc6L2NvbmZpZyAjIE1hcCBob3N0IGRpcmVjdG9yeSB0byBjb250YWluZXIgZGlyZWN0b3J5XG4gICAgcG9ydHM6XG4gICAgICAtIDg0NDM6ODQ0MyAjIEhUVFBTIHBvcnRhbFxuICAgICAgIyAtIDM0Nzg6MzQ3OC91ZHAgIyBTVFVOIHNlcnZpY2VcbiAgICAgICMgLSAxMDAwMToxMDAwMS91ZHAgIyBVbmlGaSBBUCBkaXNjb3ZlcnlcbiAgICAgICMgLSA4MDgwOjgwODAgIyBIVFRQIHBvcnRhbFxuICAgICAgIyAtIDE5MDA6MTkwMC91ZHAgI29wdGlvbmFsICAjIEZvciBETE5BXG4gICAgICAjIC0gODg0Mzo4ODQzICNvcHRpb25hbCAgIyBIVFRQUyBndWVzdCBwb3J0YWxcbiAgICAgICMgLSA4ODgwOjg4ODAgI29wdGlvbmFsICAjIEhUVFAgZ3Vlc3QgcG9ydGFsXG4gICAgICAjIC0gNjc4OTo2Nzg5ICNvcHRpb25hbCAgIyBNb2JpbGUgc3BlZWQgdGVzdCBwb3J0XG4gICAgICAjIC0gNTUxNDo1NTE0L3VkcCAjb3B0aW9uYWwgICMgUmVtb3RlIHN5c2xvZyBwb3J0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSB1bmlmaS1kYlxuXG5cbiAgdW5pZmktZGI6XG4gICAgaW1hZ2U6IG1vbmdvOjQuNFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL2RiL2RhdGE6L2RhdGEvZGJcbiAgICAgIC0gLi4vZmlsZXMvaW5pdC1tb25nby5zaDovZG9ja2VyLWVudHJ5cG9pbnQtaW5pdGRiLmQvaW5pdC1tb25nby5zaDpyb1xuICAgIHBvcnRzOlxuICAgICAgLSAyNzAxN1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cblxuIiwKICAiY29uZmlnIjogInZhcmlhYmxlcyA9IHt9XG5cbltjb25maWddXG5kb21haW5zID0gW11cbmVudiA9IHt9XG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiaW5pdC1tb25nby5zaFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIS9iaW4vYmFzaFxubW9uZ28gPDxFT0ZcbnVzZSB1bmlmaVxuZGIuY3JlYXRlVXNlcih7XG51c2VyOiBcInVuaWZpXCIsXG5wd2Q6IFwidW5pZmlfcGFzc3dvcmRcIixcbnJvbGVzOiBbXG4gICAgeyBkYjogXCJ1bmlmaVwiLCByb2xlOiBcImRiT3duZXJcIiB9LFxuICAgIHsgZGI6IFwidW5pZmlfc3RhdFwiLCByb2xlOiBcImRiT3duZXJcIiB9XG5dXG59KVxuRU9GIFxuXCJcIlwiXG4iCn0=
```

## Links

`self-hosted`,`networking`

---

Version:`11.6.6`

UmamiUmami is a simple, fast, privacy-focused alternative to Google Analytics.

UnleashOpen-source feature management platform

### On this page

ConfigurationBase64LinksTags