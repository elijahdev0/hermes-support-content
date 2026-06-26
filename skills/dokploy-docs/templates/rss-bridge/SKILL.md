---
title: "RSS-Bridge | Dokploy"
source: "https://docs.dokploy.com/docs/templates/rss-bridge"
category: dokploy-docs
created: "2026-06-25T17:21:57.938Z"
---

RSS-Bridge | Dokploy

# RSS-Bridge

Copy as Markdown

RSS-Bridge is a PHP project capable of generating Atom feeds for websites that don't have one.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  rss-bridge:
    image: rssbridge/rss-bridge:latest
    restart: unless-stopped
    expose:
      - 80
    volumes:
      - rssbridge-config:/config

volumes:
  rssbridge-config: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "rss-bridge"
port = 80
host = "${main_domain}"

[config.env]

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHJzcy1icmlkZ2U6XG4gICAgaW1hZ2U6IHJzc2JyaWRnZS9yc3MtYnJpZGdlOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZXhwb3NlOlxuICAgICAgLSA4MFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHJzc2JyaWRnZS1jb25maWc6L2NvbmZpZ1xuXG52b2x1bWVzOlxuICByc3NicmlkZ2UtY29uZmlnOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInJzcy1icmlkZ2VcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuXG5bW2NvbmZpZy5tb3VudHNdXVxuIgp9
```

## Links

`rss`,`feeds`,`news`,`content`

---

Version:`latest`

RoundcubeFree and open source webmail software for the masses, written in PHP.

RSSHubRSSHub is the world's largest RSS network, consisting of over 5,000 global instances.RSSHub delivers millions of contents aggregated from all kinds of sources, our vibrant open source community is ensuring the deliver of RSSHub's new routes, new features and bug fixes.

### On this page

ConfigurationBase64LinksTags