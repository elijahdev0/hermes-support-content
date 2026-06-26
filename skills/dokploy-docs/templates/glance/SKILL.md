---
title: "Glance | Dokploy"
source: "https://docs.dokploy.com/docs/templates/glance"
category: dokploy-docs
created: "2026-06-25T17:21:48.522Z"
---

Glance | Dokploy

# Glance

Copy as Markdown

A self-hosted dashboard that puts all your feeds in one place. Features RSS feeds, weather, bookmarks, site monitoring, and more in a minimal, fast interface.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  glance:
    image: glanceapp/glance
    volumes:
      - ../files/app/config/:/app/config
      - ../files/app/assets:/app/assets
      # Optionally, also mount docker socket if you want to use the docker containers widget
      # - /var/run/docker.sock:/var/run/docker.sock:ro
    ports:
      - 8080
    env_file: .env
```

```
[variables]
main_domain = "${domain}"

[config]
env = []

[[config.domains]]
serviceName = "glance"
port = 8_080
host = "${main_domain}"

[[config.mounts]]
filePath = "/app/config/glance.yml"
content = """
branding:
  hide-footer: true
  logo-text: P

pages:
  - name: Home
    columns:
      - size: small
        widgets:
          - type: calendar

          - type: releases
            show-source-icon: true
            repositories:
              - Dokploy/dokploy
              - n8n-io/n8n
              - Budibase/budibase
              - home-assistant/core
              - tidbyt/pixlet

          - type: twitch-channels
            channels:
              - nmplol
              - extraemily
              - qtcinderella
              - ludwig
              - timthetatman
              - mizkif

      - size: full
        widgets:
          - type: hacker-news

          - type: videos
            style: grid-cards
            channels:
              - UC3GzdWYwUYI1ACxuP9Nm-eg
              - UCGbg3DjQdcqWwqOLHpYHXIg
              - UC24RSoLcjiNZbQcT54j5l7Q
            limit: 3

          - type: rss
            limit: 10
            collapse-after: 3
            cache: 3h
            feeds:
              - url: https://daringfireball.net/feeds/main
                title: Daring Fireball

      - size: small
        widgets:
          - type: weather
            location: Gansevoort, New York, United States
            show-area-name: false
            units: imperial
            hour-format: 12h

          - type: markets
            markets:
              - symbol: SPY
                name: S&P 500
              - symbol: VOO
                name: Vanguard
              - symbol: BTC-USD
                name: Bitcoin
              - symbol: ETH-USD
                name: Etherium
              - symbol: NVDA
                name: NVIDIA
              - symbol: AAPL
                name: Apple
              - symbol: MSFT
                name: Microsoft
              - symbol: GOOGL
                name: Google
              - symbol: AMD
                name: AMD
              - symbol: TSLA
                name: Tesla
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBnbGFuY2U6XG4gICAgaW1hZ2U6IGdsYW5jZWFwcC9nbGFuY2VcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9hcHAvY29uZmlnLzovYXBwL2NvbmZpZ1xuICAgICAgLSAuLi9maWxlcy9hcHAvYXNzZXRzOi9hcHAvYXNzZXRzXG4gICAgICAjIE9wdGlvbmFsbHksIGFsc28gbW91bnQgZG9ja2VyIHNvY2tldCBpZiB5b3Ugd2FudCB0byB1c2UgdGhlIGRvY2tlciBjb250YWluZXJzIHdpZGdldFxuICAgICAgIyAtIC92YXIvcnVuL2RvY2tlci5zb2NrOi92YXIvcnVuL2RvY2tlci5zb2NrOnJvXG4gICAgcG9ydHM6XG4gICAgICAtIDgwODBcbiAgICBlbnZfZmlsZTogLmVudiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJnbGFuY2VcIlxucG9ydCA9IDhfMDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL2FwcC9jb25maWcvZ2xhbmNlLnltbFwiXG5jb250ZW50ID0gXCJcIlwiXG5icmFuZGluZzpcbiAgaGlkZS1mb290ZXI6IHRydWVcbiAgbG9nby10ZXh0OiBQXG5cbnBhZ2VzOlxuICAtIG5hbWU6IEhvbWVcbiAgICBjb2x1bW5zOlxuICAgICAgLSBzaXplOiBzbWFsbFxuICAgICAgICB3aWRnZXRzOlxuICAgICAgICAgIC0gdHlwZTogY2FsZW5kYXJcblxuICAgICAgICAgIC0gdHlwZTogcmVsZWFzZXNcbiAgICAgICAgICAgIHNob3ctc291cmNlLWljb246IHRydWVcbiAgICAgICAgICAgIHJlcG9zaXRvcmllczpcbiAgICAgICAgICAgICAgLSBEb2twbG95L2Rva3Bsb3lcbiAgICAgICAgICAgICAgLSBuOG4taW8vbjhuXG4gICAgICAgICAgICAgIC0gQnVkaWJhc2UvYnVkaWJhc2VcbiAgICAgICAgICAgICAgLSBob21lLWFzc2lzdGFudC9jb3JlXG4gICAgICAgICAgICAgIC0gdGlkYnl0L3BpeGxldFxuXG4gICAgICAgICAgLSB0eXBlOiB0d2l0Y2gtY2hhbm5lbHNcbiAgICAgICAgICAgIGNoYW5uZWxzOlxuICAgICAgICAgICAgICAtIG5tcGxvbFxuICAgICAgICAgICAgICAtIGV4dHJhZW1pbHlcbiAgICAgICAgICAgICAgLSBxdGNpbmRlcmVsbGFcbiAgICAgICAgICAgICAgLSBsdWR3aWdcbiAgICAgICAgICAgICAgLSB0aW10aGV0YXRtYW5cbiAgICAgICAgICAgICAgLSBtaXpraWZcblxuICAgICAgLSBzaXplOiBmdWxsXG4gICAgICAgIHdpZGdldHM6XG4gICAgICAgICAgLSB0eXBlOiBoYWNrZXItbmV3c1xuXG4gICAgICAgICAgLSB0eXBlOiB2aWRlb3NcbiAgICAgICAgICAgIHN0eWxlOiBncmlkLWNhcmRzXG4gICAgICAgICAgICBjaGFubmVsczpcbiAgICAgICAgICAgICAgLSBVQzNHemRXWXdVWUkxQUN4dVA5Tm0tZWdcbiAgICAgICAgICAgICAgLSBVQ0diZzNEalFkY3FXd3FPTEhwWUhYSWdcbiAgICAgICAgICAgICAgLSBVQzI0UlNvTGNqaU5aYlFjVDU0ajVsN1FcbiAgICAgICAgICAgIGxpbWl0OiAzXG5cbiAgICAgICAgICAtIHR5cGU6IHJzc1xuICAgICAgICAgICAgbGltaXQ6IDEwXG4gICAgICAgICAgICBjb2xsYXBzZS1hZnRlcjogM1xuICAgICAgICAgICAgY2FjaGU6IDNoXG4gICAgICAgICAgICBmZWVkczpcbiAgICAgICAgICAgICAgLSB1cmw6IGh0dHBzOi8vZGFyaW5nZmlyZWJhbGwubmV0L2ZlZWRzL21haW5cbiAgICAgICAgICAgICAgICB0aXRsZTogRGFyaW5nIEZpcmViYWxsXG4gICAgICAgIFxuICAgICAgLSBzaXplOiBzbWFsbFxuICAgICAgICB3aWRnZXRzOlxuICAgICAgICAgIC0gdHlwZTogd2VhdGhlclxuICAgICAgICAgICAgbG9jYXRpb246IEdhbnNldm9vcnQsIE5ldyBZb3JrLCBVbml0ZWQgU3RhdGVzXG4gICAgICAgICAgICBzaG93LWFyZWEtbmFtZTogZmFsc2VcbiAgICAgICAgICAgIHVuaXRzOiBpbXBlcmlhbFxuICAgICAgICAgICAgaG91ci1mb3JtYXQ6IDEyaFxuXG4gICAgICAgICAgLSB0eXBlOiBtYXJrZXRzXG4gICAgICAgICAgICBtYXJrZXRzOlxuICAgICAgICAgICAgICAtIHN5bWJvbDogU1BZXG4gICAgICAgICAgICAgICAgbmFtZTogUyZQIDUwMFxuICAgICAgICAgICAgICAtIHN5bWJvbDogVk9PXG4gICAgICAgICAgICAgICAgbmFtZTogVmFuZ3VhcmRcbiAgICAgICAgICAgICAgLSBzeW1ib2w6IEJUQy1VU0RcbiAgICAgICAgICAgICAgICBuYW1lOiBCaXRjb2luXG4gICAgICAgICAgICAgIC0gc3ltYm9sOiBFVEgtVVNEXG4gICAgICAgICAgICAgICAgbmFtZTogRXRoZXJpdW1cbiAgICAgICAgICAgICAgLSBzeW1ib2w6IE5WREFcbiAgICAgICAgICAgICAgICBuYW1lOiBOVklESUFcbiAgICAgICAgICAgICAgLSBzeW1ib2w6IEFBUExcbiAgICAgICAgICAgICAgICBuYW1lOiBBcHBsZVxuICAgICAgICAgICAgICAtIHN5bWJvbDogTVNGVFxuICAgICAgICAgICAgICAgIG5hbWU6IE1pY3Jvc29mdFxuICAgICAgICAgICAgICAtIHN5bWJvbDogR09PR0xcbiAgICAgICAgICAgICAgICBuYW1lOiBHb29nbGVcbiAgICAgICAgICAgICAgLSBzeW1ib2w6IEFNRFxuICAgICAgICAgICAgICAgIG5hbWU6IEFNRFxuICAgICAgICAgICAgICAtIHN5bWJvbDogVFNMQVxuICAgICAgICAgICAgICAgIG5hbWU6IFRlc2xhIFxuXCJcIlwiXG4iCn0=
```

## Links

`dashboard`,`monitoring`,`widgets`,`rss`

---

Version:`latest`

GitLab CEGitLab Community Edition is a free and open source platform for managing Git repositories, CI/CD pipelines, and project management.

GlitchtipGlitchtip is simple, open source error tracking

### On this page

ConfigurationBase64LinksTags