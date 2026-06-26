---
title: "FreshRSS | Dokploy"
source: "https://docs.dokploy.com/docs/templates/freshrss"
category: dokploy-docs
created: "2026-06-25T17:21:48.521Z"
---

FreshRSS | Dokploy

# FreshRSS

Copy as Markdown

A free, self-hostable RSS and Atom feed aggregator. Lightweight, easy to work with, powerful, and customizable with themes and extensions.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  freshrss:
    image: freshrss/freshrss:${FRESHRSS_VERSION:-latest}
    restart: unless-stopped
    volumes:
      # FreshRSS persistent data such as configuration and SQLite databases
      - freshrss_data:/var/www/FreshRSS/data
      # Optional volume for storing third-party extensions
      - freshrss_extensions:/var/www/FreshRSS/extensions
    ports:
      - "80"
    environment:
      # Server timezone
      TZ: ${TZ:-UTC}
      # Cron job to refresh feeds at specified minutes
      CRON_MIN: ${CRON_MIN:-13,43}
      # Production or development mode
      FRESHRSS_ENV: ${FRESHRSS_ENV:-production}
      # Copy logs to syslog
      COPY_LOG_TO_SYSLOG: ${COPY_LOG_TO_SYSLOG:-On}
      # Copy syslog to stderr for docker logs
      COPY_SYSLOG_TO_STDERR: ${COPY_SYSLOG_TO_STDERR:-On}
      # Optional auto-install parameters
      FRESHRSS_INSTALL: ${FRESHRSS_INSTALL:-}
      # Optional auto-create user parameters
      FRESHRSS_USER: ${FRESHRSS_USER:-}

volumes:
  freshrss_data:
  freshrss_extensions:
```

```
[variables]
main_domain = "${domain}"
timezone = "UTC"

[config.env]
FRESHRSS_VERSION = "latest"
TZ = "${timezone}"
CRON_MIN = "13,43"
FRESHRSS_ENV = "production"
COPY_LOG_TO_SYSLOG = "On"
COPY_SYSLOG_TO_STDERR = "On"

[config]
mounts = []

[[config.domains]]
serviceName = "freshrss"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBmcmVzaHJzczpcbiAgICBpbWFnZTogZnJlc2hyc3MvZnJlc2hyc3M6JHtGUkVTSFJTU19WRVJTSU9OOi1sYXRlc3R9XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgIyBGcmVzaFJTUyBwZXJzaXN0ZW50IGRhdGEgc3VjaCBhcyBjb25maWd1cmF0aW9uIGFuZCBTUUxpdGUgZGF0YWJhc2VzXG4gICAgICAtIGZyZXNocnNzX2RhdGE6L3Zhci93d3cvRnJlc2hSU1MvZGF0YVxuICAgICAgIyBPcHRpb25hbCB2b2x1bWUgZm9yIHN0b3JpbmcgdGhpcmQtcGFydHkgZXh0ZW5zaW9uc1xuICAgICAgLSBmcmVzaHJzc19leHRlbnNpb25zOi92YXIvd3d3L0ZyZXNoUlNTL2V4dGVuc2lvbnNcbiAgICBwb3J0czpcbiAgICAgIC0gXCI4MFwiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAjIFNlcnZlciB0aW1lem9uZVxuICAgICAgVFo6ICR7VFo6LVVUQ31cbiAgICAgICMgQ3JvbiBqb2IgdG8gcmVmcmVzaCBmZWVkcyBhdCBzcGVjaWZpZWQgbWludXRlc1xuICAgICAgQ1JPTl9NSU46ICR7Q1JPTl9NSU46LTEzLDQzfVxuICAgICAgIyBQcm9kdWN0aW9uIG9yIGRldmVsb3BtZW50IG1vZGVcbiAgICAgIEZSRVNIUlNTX0VOVjogJHtGUkVTSFJTU19FTlY6LXByb2R1Y3Rpb259XG4gICAgICAjIENvcHkgbG9ncyB0byBzeXNsb2dcbiAgICAgIENPUFlfTE9HX1RPX1NZU0xPRzogJHtDT1BZX0xPR19UT19TWVNMT0c6LU9ufVxuICAgICAgIyBDb3B5IHN5c2xvZyB0byBzdGRlcnIgZm9yIGRvY2tlciBsb2dzXG4gICAgICBDT1BZX1NZU0xPR19UT19TVERFUlI6ICR7Q09QWV9TWVNMT0dfVE9fU1RERVJSOi1Pbn1cbiAgICAgICMgT3B0aW9uYWwgYXV0by1pbnN0YWxsIHBhcmFtZXRlcnNcbiAgICAgIEZSRVNIUlNTX0lOU1RBTEw6ICR7RlJFU0hSU1NfSU5TVEFMTDotfVxuICAgICAgIyBPcHRpb25hbCBhdXRvLWNyZWF0ZSB1c2VyIHBhcmFtZXRlcnNcbiAgICAgIEZSRVNIUlNTX1VTRVI6ICR7RlJFU0hSU1NfVVNFUjotfVxuXG52b2x1bWVzOlxuICBmcmVzaHJzc19kYXRhOlxuICBmcmVzaHJzc19leHRlbnNpb25zOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnRpbWV6b25lID0gXCJVVENcIlxuXG5bY29uZmlnLmVudl1cbkZSRVNIUlNTX1ZFUlNJT04gPSBcImxhdGVzdFwiXG5UWiA9IFwiJHt0aW1lem9uZX1cIlxuQ1JPTl9NSU4gPSBcIjEzLDQzXCJcbkZSRVNIUlNTX0VOViA9IFwicHJvZHVjdGlvblwiXG5DT1BZX0xPR19UT19TWVNMT0cgPSBcIk9uXCJcbkNPUFlfU1lTTE9HX1RPX1NUREVSUiA9IFwiT25cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZnJlc2hyc3NcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiICIKfQ==
```

## Links

`rss`,`feed-reader`,`news`,`self-hosted`,`aggregator`,`reader`

---

Version:`latest`

FreeScoutFreeScout is a free open source help desk and shared inbox system. It's a self-hosted alternative to HelpScout, Zendesk, and similar services that allows you to manage customer communications through email and a clean web interface. FreeScout makes it easy to organize support requests, track customer conversations, and collaborate with your team.

Garage S3Garage is an open-source distributed object storage service tailored for self-hosting.

### On this page

ConfigurationBase64LinksTags