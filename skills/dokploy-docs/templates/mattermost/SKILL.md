---
title: "Mattermost | Dokploy"
source: "https://docs.dokploy.com/docs/templates/mattermost"
category: dokploy-docs
created: "2026-06-25T17:21:52.047Z"
---

Mattermost | Dokploy

# Mattermost

Copy as Markdown

A single point of collaboration. Designed specifically for digital operations.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  postgres:
    image: postgres:17
    restart: unless-stopped
    security_opt:
      - no-new-privileges:true
    pids_limit: 100
    read_only: true
    tmpfs:
      - /tmp
      - /var/run/postgresql
    volumes:
      - mattermostDbData:/var/lib/postgresql/data
    environment:
      - TZ
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_DB

  mattermost:
    depends_on:
      - postgres
    image: mattermost/mattermost-team-edition:10.6.1
    restart: unless-stopped
    security_opt:
      - no-new-privileges:true
    pids_limit: 200
    read_only: false
    tmpfs:
      - /tmp
    volumes:
      - mattermostconf:/mattermost/config:rw
      - mattermostdata:/mattermost/data:rw
      - mattermostlogs:/mattermost/logs:rw
      - mattermostplugsin:/mattermost/plugins:rw
      - mattermostclientplugins:/mattermost/client/plugins:rw
      - mattermostBleveIndexes:/mattermost/bleve-indexes:rw

    environment:
      - DOMAIN
      - TZ
      - POSTGRES_USER
      - POSTGRES_PASSWORD
      - POSTGRES_DB
      - MM_SQLSETTINGS_DRIVERNAME
      - MM_SQLSETTINGS_DATASOURCE
      - MM_BLEVESETTINGS_INDEXDIR
      - MM_SERVICESETTINGS_SITEURL
      - APP_PORT

volumes:
  mattermostDbData:
    driver: local
  mattermostconf:
    driver: local
  mattermostdata:
    driver: local
  mattermostlogs:
    driver: local
  mattermostplugsin:
    driver: local
  mattermostclientplugins:
    driver: local
  mattermostBleveIndexes:
    driver: local
```

```
[variables]
main_domain = "${domain}"

[config]
env = [
"Domain=${main_domain}",
"POSTGRES_USER=mmuser",
"POSTGRES_PASSWORD=${password:32}",
"POSTGRES_DB=mattermost",
"MM_SQLSETTINGS_DRIVERNAME=postgres",
"MM_SQLSETTINGS_DATASOURCE=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}?sslmode=disable&connect_timeout=10",
"APP_PORT=8065",
"TZ=UTC",
]
mounts = []

[[config.domains]]
serviceName = "mattermost"
port = 8065
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTdcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHNlY3VyaXR5X29wdDpcbiAgICAgIC0gbm8tbmV3LXByaXZpbGVnZXM6dHJ1ZVxuICAgIHBpZHNfbGltaXQ6IDEwMFxuICAgIHJlYWRfb25seTogdHJ1ZVxuICAgIHRtcGZzOlxuICAgICAgLSAvdG1wXG4gICAgICAtIC92YXIvcnVuL3Bvc3RncmVzcWxcbiAgICB2b2x1bWVzOlxuICAgICAgLSBtYXR0ZXJtb3N0RGJEYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBUWlxuICAgICAgLSBQT1NUR1JFU19VU0VSXG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEXG4gICAgICAtIFBPU1RHUkVTX0RCXG5cbiAgbWF0dGVybW9zdDpcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBwb3N0Z3Jlc1xuICAgIGltYWdlOiBtYXR0ZXJtb3N0L21hdHRlcm1vc3QtdGVhbS1lZGl0aW9uOjEwLjYuMVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgc2VjdXJpdHlfb3B0OlxuICAgICAgLSBuby1uZXctcHJpdmlsZWdlczp0cnVlXG4gICAgcGlkc19saW1pdDogMjAwXG4gICAgcmVhZF9vbmx5OiBmYWxzZVxuICAgIHRtcGZzOlxuICAgICAgLSAvdG1wXG4gICAgdm9sdW1lczpcbiAgICAgIC0gbWF0dGVybW9zdGNvbmY6L21hdHRlcm1vc3QvY29uZmlnOnJ3XG4gICAgICAtIG1hdHRlcm1vc3RkYXRhOi9tYXR0ZXJtb3N0L2RhdGE6cndcbiAgICAgIC0gbWF0dGVybW9zdGxvZ3M6L21hdHRlcm1vc3QvbG9nczpyd1xuICAgICAgLSBtYXR0ZXJtb3N0cGx1Z3NpbjovbWF0dGVybW9zdC9wbHVnaW5zOnJ3XG4gICAgICAtIG1hdHRlcm1vc3RjbGllbnRwbHVnaW5zOi9tYXR0ZXJtb3N0L2NsaWVudC9wbHVnaW5zOnJ3XG4gICAgICAtIG1hdHRlcm1vc3RCbGV2ZUluZGV4ZXM6L21hdHRlcm1vc3QvYmxldmUtaW5kZXhlczpyd1xuICAgICAgXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIERPTUFJTlxuICAgICAgLSBUWlxuICAgICAgLSBQT1NUR1JFU19VU0VSXG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEXG4gICAgICAtIFBPU1RHUkVTX0RCXG4gICAgICAtIE1NX1NRTFNFVFRJTkdTX0RSSVZFUk5BTUVcbiAgICAgIC0gTU1fU1FMU0VUVElOR1NfREFUQVNPVVJDRVxuICAgICAgLSBNTV9CTEVWRVNFVFRJTkdTX0lOREVYRElSXG4gICAgICAtIE1NX1NFUlZJQ0VTRVRUSU5HU19TSVRFVVJMXG4gICAgICAtIEFQUF9QT1JUXG5cblxudm9sdW1lczpcbiAgbWF0dGVybW9zdERiRGF0YTpcbiAgICBkcml2ZXI6IGxvY2FsXG4gIG1hdHRlcm1vc3Rjb25mOlxuICAgIGRyaXZlcjogbG9jYWxcbiAgbWF0dGVybW9zdGRhdGE6XG4gICAgZHJpdmVyOiBsb2NhbFxuICBtYXR0ZXJtb3N0bG9nczpcbiAgICBkcml2ZXI6IGxvY2FsXG4gIG1hdHRlcm1vc3RwbHVnc2luOlxuICAgIGRyaXZlcjogbG9jYWxcbiAgbWF0dGVybW9zdGNsaWVudHBsdWdpbnM6XG4gICAgZHJpdmVyOiBsb2NhbFxuICBtYXR0ZXJtb3N0QmxldmVJbmRleGVzOlxuICAgIGRyaXZlcjogbG9jYWxcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXG5cIkRvbWFpbj0ke21haW5fZG9tYWlufVwiLFxuXCJQT1NUR1JFU19VU0VSPW1tdXNlclwiLFxuXCJQT1NUR1JFU19QQVNTV09SRD0ke3Bhc3N3b3JkOjMyfVwiLFxuXCJQT1NUR1JFU19EQj1tYXR0ZXJtb3N0XCIsXG5cIk1NX1NRTFNFVFRJTkdTX0RSSVZFUk5BTUU9cG9zdGdyZXNcIixcblwiTU1fU1FMU0VUVElOR1NfREFUQVNPVVJDRT1wb3N0Z3JlczovLyR7UE9TVEdSRVNfVVNFUn06JHtQT1NUR1JFU19QQVNTV09SRH1AcG9zdGdyZXM6NTQzMi8ke1BPU1RHUkVTX0RCfT9zc2xtb2RlPWRpc2FibGUmY29ubmVjdF90aW1lb3V0PTEwXCIsXG5cIkFQUF9QT1JUPTgwNjVcIixcblwiVFo9VVRDXCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJtYXR0ZXJtb3N0XCJcbnBvcnQgPSA4MDY1XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`chat`,`self-hosted`

---

Version:`10.6.1`

MailpitMailpit is a tiny, self-contained, and secure email & SMTP testing tool with API for developers.

MauticMautic is the world's largest open-source marketing automation project. It allows you to automate the process of finding and nurturing contacts through landing pages and forms, sending email, text messages, web notifications, and tracking your contacts.

### On this page

ConfigurationBase64LinksTags