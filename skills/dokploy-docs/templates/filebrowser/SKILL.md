---
title: "File Browser | Dokploy"
source: "https://docs.dokploy.com/docs/templates/filebrowser"
category: dokploy-docs
created: "2026-06-25T17:21:47.358Z"
---

File Browser | Dokploy

# File Browser

Copy as Markdown

Filebrowser is a standalone file manager for uploading, deleting, previewing, renaming, and editing files, with support for multiple users, each with their own directory.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  filebrowser:
    image: hurlenko/filebrowser
    volumes:
      - filebrowser-data:/data
      - filebrowser-config:/config
    environment:
      - FB_BASEURL=${FB_BASEURL}
    restart: always

volumes:
  filebrowser-data:
  filebrowser-config:
```

```
[variables]
main_domain = "${domain}"

[config]
env = ["FB_BASEURL=/filebrowser"]
mounts = []

[[config.domains]]
serviceName = "filebrowser"
port = 8_080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBmaWxlYnJvd3NlcjpcbiAgICBpbWFnZTogaHVybGVua28vZmlsZWJyb3dzZXJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBmaWxlYnJvd3Nlci1kYXRhOi9kYXRhXG4gICAgICAtIGZpbGVicm93c2VyLWNvbmZpZzovY29uZmlnXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIEZCX0JBU0VVUkw9JHtGQl9CQVNFVVJMfVxuICAgIHJlc3RhcnQ6IGFsd2F5cyBcblxudm9sdW1lczpcbiAgZmlsZWJyb3dzZXItZGF0YTpcbiAgZmlsZWJyb3dzZXItY29uZmlnOlxuICAgICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXCJGQl9CQVNFVVJMPS9maWxlYnJvd3NlclwiXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZmlsZWJyb3dzZXJcIlxucG9ydCA9IDhfMDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`file-manager`,`storage`

---

Version:`2.31.2`

EZBookkeepingEZBookkeeping is a self-hosted bookkeeping application that helps you manage your personal and business finances. It provides features for tracking income, expenses, accounts, and generating financial reports.

FilestashFilestash is the enterprise-grade file manager connecting your storage with your identity provider and authorisations.

### On this page

ConfigurationBase64LinksTags