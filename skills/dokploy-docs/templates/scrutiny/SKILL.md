---
title: "Scrutiny | Dokploy"
source: "https://docs.dokploy.com/docs/templates/scrutiny"
category: dokploy-docs
created: "2026-06-25T17:21:59.113Z"
---

Scrutiny | Dokploy

# Scrutiny

Copy as Markdown

Hard Drive S.M.A.R.T Monitoring, Historical Trends & Real World Failure Thresholds

## Configuration

docker-compose.ymltemplate.toml

```
services:
  scrutiny:
    restart: unless-stopped
    container_name: scrutiny
    image: ghcr.io/analogj/scrutiny:master-omnibus
    cap_add:
      - SYS_RAWIO
    ports:
      - 8080  # webapp
      - 8086  # influxDB admin
    volumes:
      - /run/udev:/run/udev:ro
      - ./config:/opt/scrutiny/config
      - ./influxdb:/opt/scrutiny/influxdb
    devices:
      - "/dev/sda"
      - "/dev/sdb"

# PROXMOX USERS: Proxmox LXCs don't have access to S.M.A.R.T data, while this may be possible on VMs using PCI passthrough,
# there's another way which is to run the scrutiny collector on proxmox host and have it send data to the scrutiny webapp running in an LXC or VM
# so basically you can use the following commented docker-compose (web+db) and run the collector directly on the proxmox host (guide: https://github.com/AnalogJ/scrutiny/blob/master/docs/INSTALL_HUB_SPOKE.md#setting-up-a-spoke-without-docker)

# services:
#   influxdb:
#     restart: unless-stopped
#     image: influxdb:2.2
#     ports:
#       - '8086:8086'
#     volumes:
#       - './influxdb:/var/lib/influxdb2'
#     healthcheck:
#       test: ["CMD", "curl", "-f", "http://localhost:8086/health"]
#       interval: 5s
#       timeout: 10s
#       retries: 20
#
#
#   web:
#     restart: unless-stopped
#     image: 'ghcr.io/analogj/scrutiny:master-web'
#     ports:
#       - '8080:8080'
#     volumes:
#       - './config:/opt/scrutiny/config'
#     environment:
#       SCRUTINY_WEB_INFLUXDB_HOST: 'influxdb'
#     depends_on:
#       influxdb:
#         condition: service_healthy
#     healthcheck:
#       test: ["CMD", "curl", "-f", "http://localhost:8080/api/health"]
#       interval: 5s
#       timeout: 10s
#       retries: 20
#       start_period: 10s
```

```
[config]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBzY3J1dGlueTpcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGNvbnRhaW5lcl9uYW1lOiBzY3J1dGlueVxuICAgIGltYWdlOiBnaGNyLmlvL2FuYWxvZ2ovc2NydXRpbnk6bWFzdGVyLW9tbmlidXNcbiAgICBjYXBfYWRkOlxuICAgICAgLSBTWVNfUkFXSU9cbiAgICBwb3J0czpcbiAgICAgIC0gODA4MCAgIyB3ZWJhcHBcbiAgICAgIC0gODA4NiAgIyBpbmZsdXhEQiBhZG1pblxuICAgIHZvbHVtZXM6XG4gICAgICAtIC9ydW4vdWRldjovcnVuL3VkZXY6cm9cbiAgICAgIC0gLi9jb25maWc6L29wdC9zY3J1dGlueS9jb25maWdcbiAgICAgIC0gLi9pbmZsdXhkYjovb3B0L3NjcnV0aW55L2luZmx1eGRiXG4gICAgZGV2aWNlczpcbiAgICAgIC0gXCIvZGV2L3NkYVwiXG4gICAgICAtIFwiL2Rldi9zZGJcIlxuXG4jIFBST1hNT1ggVVNFUlM6IFByb3htb3ggTFhDcyBkb24ndCBoYXZlIGFjY2VzcyB0byBTLk0uQS5SLlQgZGF0YSwgd2hpbGUgdGhpcyBtYXkgYmUgcG9zc2libGUgb24gVk1zIHVzaW5nIFBDSSBwYXNzdGhyb3VnaCxcbiMgdGhlcmUncyBhbm90aGVyIHdheSB3aGljaCBpcyB0byBydW4gdGhlIHNjcnV0aW55IGNvbGxlY3RvciBvbiBwcm94bW94IGhvc3QgYW5kIGhhdmUgaXQgc2VuZCBkYXRhIHRvIHRoZSBzY3J1dGlueSB3ZWJhcHAgcnVubmluZyBpbiBhbiBMWEMgb3IgVk1cbiMgc28gYmFzaWNhbGx5IHlvdSBjYW4gdXNlIHRoZSBmb2xsb3dpbmcgY29tbWVudGVkIGRvY2tlci1jb21wb3NlICh3ZWIrZGIpIGFuZCBydW4gdGhlIGNvbGxlY3RvciBkaXJlY3RseSBvbiB0aGUgcHJveG1veCBob3N0IChndWlkZTogaHR0cHM6Ly9naXRodWIuY29tL0FuYWxvZ0ovc2NydXRpbnkvYmxvYi9tYXN0ZXIvZG9jcy9JTlNUQUxMX0hVQl9TUE9LRS5tZCNzZXR0aW5nLXVwLWEtc3Bva2Utd2l0aG91dC1kb2NrZXIpXG5cbiMgc2VydmljZXM6XG4jICAgaW5mbHV4ZGI6XG4jICAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuIyAgICAgaW1hZ2U6IGluZmx1eGRiOjIuMlxuIyAgICAgcG9ydHM6XG4jICAgICAgIC0gJzgwODY6ODA4NidcbiMgICAgIHZvbHVtZXM6XG4jICAgICAgIC0gJy4vaW5mbHV4ZGI6L3Zhci9saWIvaW5mbHV4ZGIyJ1xuIyAgICAgaGVhbHRoY2hlY2s6XG4jICAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcImN1cmxcIiwgXCItZlwiLCBcImh0dHA6Ly9sb2NhbGhvc3Q6ODA4Ni9oZWFsdGhcIl1cbiMgICAgICAgaW50ZXJ2YWw6IDVzXG4jICAgICAgIHRpbWVvdXQ6IDEwc1xuIyAgICAgICByZXRyaWVzOiAyMFxuIyBcbiMgXG4jICAgd2ViOlxuIyAgICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiMgICAgIGltYWdlOiAnZ2hjci5pby9hbmFsb2dqL3NjcnV0aW55Om1hc3Rlci13ZWInXG4jICAgICBwb3J0czpcbiMgICAgICAgLSAnODA4MDo4MDgwJ1xuIyAgICAgdm9sdW1lczpcbiMgICAgICAgLSAnLi9jb25maWc6L29wdC9zY3J1dGlueS9jb25maWcnXG4jICAgICBlbnZpcm9ubWVudDpcbiMgICAgICAgU0NSVVRJTllfV0VCX0lORkxVWERCX0hPU1Q6ICdpbmZsdXhkYidcbiMgICAgIGRlcGVuZHNfb246XG4jICAgICAgIGluZmx1eGRiOlxuIyAgICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4jICAgICBoZWFsdGhjaGVjazpcbiMgICAgICAgdGVzdDogW1wiQ01EXCIsIFwiY3VybFwiLCBcIi1mXCIsIFwiaHR0cDovL2xvY2FsaG9zdDo4MDgwL2FwaS9oZWFsdGhcIl1cbiMgICAgICAgaW50ZXJ2YWw6IDVzXG4jICAgICAgIHRpbWVvdXQ6IDEwc1xuIyAgICAgICByZXRyaWVzOiAyMFxuIyAgICAgICBzdGFydF9wZXJpb2Q6IDEwc1xuIiwKICAiY29uZmlnIjogIltjb25maWddIgp9
```

## Links

`monitoring`,`NAS`

---

Version:`latest`

RyotA self-hosted platform for tracking various media types including movies, TV shows, video games, books, audiobooks, and more.

ScryptedScrypted is a home automation platform that integrates with various smart home devices and provides NVR capabilities for video surveillance.

### On this page

ConfigurationBase64LinksTags