---
title: "CommaFeed | Dokploy"
source: "https://docs.dokploy.com/docs/templates/commafeed"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

CommaFeed | Dokploy

# CommaFeed

Copy as Markdown

CommaFeed is an open-source feed reader and news aggregator, designed to be lightweight and extensible, with PostgreSQL as its database.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  commafeed:
    image: athou/commafeed:latest-h2
    restart: unless-stopped
    volumes:
      - ../files/commafeed-data:/commafeed/data
    ports:
      - 8082
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "commafeed"
port = 8082
host = "${main_domain}"

[config.env]
# No environment variables specified for CommaFeed; add if needed
# Example: COMMAFEED_ADMIN_USER = "${username}"
# Example: COMMAFEED_ADMIN_PASSWORD = "${password:32}"

[[config.mounts]]
filePath = "/files/commafeed-data"
content = ""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBjb21tYWZlZWQ6XG4gICAgaW1hZ2U6IGF0aG91L2NvbW1hZmVlZDpsYXRlc3QtaDJcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL2NvbW1hZmVlZC1kYXRhOi9jb21tYWZlZWQvZGF0YVxuICAgIHBvcnRzOlxuICAgICAgLSA4MDgyXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY29tbWFmZWVkXCJcbnBvcnQgPSA4MDgyXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuIyBObyBlbnZpcm9ubWVudCB2YXJpYWJsZXMgc3BlY2lmaWVkIGZvciBDb21tYUZlZWQ7IGFkZCBpZiBuZWVkZWRcbiMgRXhhbXBsZTogQ09NTUFGRUVEX0FETUlOX1VTRVIgPSBcIiR7dXNlcm5hbWV9XCJcbiMgRXhhbXBsZTogQ09NTUFGRUVEX0FETUlOX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL2ZpbGVzL2NvbW1hZmVlZC1kYXRhXCJcbmNvbnRlbnQgPSBcIlwiIgp9
```

## Links

`feed-reader`,`news-aggregator`,`rss`

---

Version:`latest`

Collabora OfficeCollabora Online is a powerful, flexible, and secure online office suite designed to break free from vendor lock-in and put you in full control of your documents.

CommentoCommento is a comments widget designed to enhance the interaction on your website. It allows your readers to contribute to the discussion by upvoting comments that add value and downvoting those that don't. The widget supports markdown formatting and provides moderation tools to manage conversations.

### On this page

ConfigurationBase64LinksTags