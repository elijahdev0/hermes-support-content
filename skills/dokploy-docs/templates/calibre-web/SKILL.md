---
title: "Calibre-Web | Dokploy"
source: "https://docs.dokploy.com/docs/templates/calibre-web"
category: dokploy-docs
created: "2026-06-25T17:21:42.678Z"
---

Calibre-Web | Dokploy

# Calibre-Web

Copy as Markdown

Calibre-Web is a web app providing a clean interface for browsing, reading, and managing your eBooks library using an existing Calibre database.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  calibre-web:
    image: lscr.io/linuxserver/calibre-web:latest
    restart: unless-stopped
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      # - DOCKER_MODS=linuxserver/mods:universal-calibre # optional
      - OAUTHLIB_RELAX_TOKEN_SCOPE=1 # optional
    volumes:
      - calibre-config:/config
      - calibre-books:/books
      - ../files/startup-scripts:/custom-cont-init.d:ro # optional, comment out if you have your own metadata.db file, otherwise it will be created

volumes:
  calibre-config: {}
  calibre-books: {}
```

```
[variables]
main_domain = "${domain}"

[config]

[[config.domains]]
serviceName = "calibre-web"
port = 8083
host = "${main_domain}"

[config.env]
PUID = "1000"
PGID = "1000"
TZ = "Etc/UTC"
DOCKER_MODS = "linuxserver/mods:universal-calibre"
OAUTHLIB_RELAX_TOKEN_SCOPE = "1"

[[config.mounts]]
filePath = "startup-scripts/metadata-db-generator.sh"
content = """
#!/bin/bash

FILE=/books/metadata.db
PUID=1000
PGID=1000

if test -f "$FILE"; then
    echo "$FILE already exists, skipping generation."
else
    echo "$FILE does not exists, downloading..."
    # download empty database from the calibre-web repo
    curl -L -O --output-dir /books https://github.com/janeczku/calibre-web/raw/refs/heads/master/library/metadata.db
    echo "$FILE downloaded, setting permissions..."
    chmod a+w $FILE
    # this is needed for uploads, you can remove it if you don't want to allow uploads
    chown $PUID:$PGID /books
    echo "Permissions fixed, use /books as library path"
fi
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBjYWxpYnJlLXdlYjpcbiAgICBpbWFnZTogbHNjci5pby9saW51eHNlcnZlci9jYWxpYnJlLXdlYjpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQVUlEPTEwMDBcbiAgICAgIC0gUEdJRD0xMDAwXG4gICAgICAtIFRaPUV0Yy9VVENcbiAgICAgICMgLSBET0NLRVJfTU9EUz1saW51eHNlcnZlci9tb2RzOnVuaXZlcnNhbC1jYWxpYnJlICMgb3B0aW9uYWxcbiAgICAgIC0gT0FVVEhMSUJfUkVMQVhfVE9LRU5fU0NPUEU9MSAjIG9wdGlvbmFsXG4gICAgdm9sdW1lczpcbiAgICAgIC0gY2FsaWJyZS1jb25maWc6L2NvbmZpZ1xuICAgICAgLSBjYWxpYnJlLWJvb2tzOi9ib29rc1xuICAgICAgLSAuLi9maWxlcy9zdGFydHVwLXNjcmlwdHM6L2N1c3RvbS1jb250LWluaXQuZDpybyAjIG9wdGlvbmFsLCBjb21tZW50IG91dCBpZiB5b3UgaGF2ZSB5b3VyIG93biBtZXRhZGF0YS5kYiBmaWxlLCBvdGhlcndpc2UgaXQgd2lsbCBiZSBjcmVhdGVkXG5cbnZvbHVtZXM6XG4gIGNhbGlicmUtY29uZmlnOiB7fVxuICBjYWxpYnJlLWJvb2tzOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY2FsaWJyZS13ZWJcIlxucG9ydCA9IDgwODNcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5QVUlEID0gXCIxMDAwXCJcblBHSUQgPSBcIjEwMDBcIlxuVFogPSBcIkV0Yy9VVENcIlxuRE9DS0VSX01PRFMgPSBcImxpbnV4c2VydmVyL21vZHM6dW5pdmVyc2FsLWNhbGlicmVcIlxuT0FVVEhMSUJfUkVMQVhfVE9LRU5fU0NPUEUgPSBcIjFcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcInN0YXJ0dXAtc2NyaXB0cy9tZXRhZGF0YS1kYi1nZW5lcmF0b3Iuc2hcIlxuY29udGVudCA9IFwiXCJcIlxuIyEvYmluL2Jhc2hcblxuRklMRT0vYm9va3MvbWV0YWRhdGEuZGJcblBVSUQ9MTAwMFxuUEdJRD0xMDAwXG5cbmlmIHRlc3QgLWYgXCIkRklMRVwiOyB0aGVuXG4gICAgZWNobyBcIiRGSUxFIGFscmVhZHkgZXhpc3RzLCBza2lwcGluZyBnZW5lcmF0aW9uLlwiXG5lbHNlXG4gICAgZWNobyBcIiRGSUxFIGRvZXMgbm90IGV4aXN0cywgZG93bmxvYWRpbmcuLi5cIlxuICAgICMgZG93bmxvYWQgZW1wdHkgZGF0YWJhc2UgZnJvbSB0aGUgY2FsaWJyZS13ZWIgcmVwb1xuICAgIGN1cmwgLUwgLU8gLS1vdXRwdXQtZGlyIC9ib29rcyBodHRwczovL2dpdGh1Yi5jb20vamFuZWN6a3UvY2FsaWJyZS13ZWIvcmF3L3JlZnMvaGVhZHMvbWFzdGVyL2xpYnJhcnkvbWV0YWRhdGEuZGJcbiAgICBlY2hvIFwiJEZJTEUgZG93bmxvYWRlZCwgc2V0dGluZyBwZXJtaXNzaW9ucy4uLlwiXG4gICAgY2htb2QgYSt3ICRGSUxFXG4gICAgIyB0aGlzIGlzIG5lZWRlZCBmb3IgdXBsb2FkcywgeW91IGNhbiByZW1vdmUgaXQgaWYgeW91IGRvbid0IHdhbnQgdG8gYWxsb3cgdXBsb2Fkc1xuICAgIGNob3duICRQVUlEOiRQR0lEIC9ib29rc1xuICAgIGVjaG8gXCJQZXJtaXNzaW9ucyBmaXhlZCwgdXNlIC9ib29rcyBhcyBsaWJyYXJ5IHBhdGhcIlxuZmlcblwiXCJcIlxuIgp9
```

## Links

`ebooks`,`media`,`library`,`self-hosted`

---

Version:`latest`

CalibreCalibre is a comprehensive e-book management tool designed to organize, convert, and read your e-book collection. It supports most of the major e-book formats and is compatible with various e-book reader devices.

Cap.soCap.so is a platform for web and desktop applications with MySQL and S3 storage. It provides a complete development environment with database and file storage capabilities.

### On this page

ConfigurationBase64LinksTags