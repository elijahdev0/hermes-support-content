---
title: "Audiobookshelf | Dokploy"
source: "https://docs.dokploy.com/docs/templates/audiobookshelf"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

Audiobookshelf | Dokploy

# Audiobookshelf

Copy as Markdown

Audiobookshelf is a self-hosted server designed to manage and play your audiobooks and podcasts. It works best when you have an organized directory structure.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  audiobookshelf:
    image: ghcr.io/advplyr/audiobookshelf:2.19.4
    restart: unless-stopped
    ports:
      - 80
    environment:
      - TZ=UTC
    volumes:
      - config:/config
      - metadata:/metadata
      - ${AUDIOBOOKS_PATH}:/audiobooks

volumes:
  config: {}
  metadata: {}
```

```
[variables]
main_domain = "${domain}"
audiobooks_path = "/path/to/your/audiobooks"

[config]
[[config.domains]]
serviceName = "audiobookshelf"
port = 80
host = "${main_domain}"

[config.env]
AUDIOBOOKS_PATH = "${audiobooks_path}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhdWRpb2Jvb2tzaGVsZjpcbiAgICBpbWFnZTogZ2hjci5pby9hZHZwbHlyL2F1ZGlvYm9va3NoZWxmOjIuMTkuNFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDgwXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFRaPVVUQ1xuICAgIHZvbHVtZXM6XG4gICAgICAtIGNvbmZpZzovY29uZmlnXG4gICAgICAtIG1ldGFkYXRhOi9tZXRhZGF0YVxuICAgICAgLSAke0FVRElPQk9PS1NfUEFUSH06L2F1ZGlvYm9va3Ncblxudm9sdW1lczpcbiAgY29uZmlnOiB7fVxuICBtZXRhZGF0YToge30gIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmF1ZGlvYm9va3NfcGF0aCA9IFwiL3BhdGgvdG8veW91ci9hdWRpb2Jvb2tzXCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImF1ZGlvYm9va3NoZWxmXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkFVRElPQk9PS1NfUEFUSCA9IFwiJHthdWRpb2Jvb2tzX3BhdGh9XCIgIgp9
```

## Links

`media`,`audiobooks`,`podcasts`

---

Version:`2.19.4`

ArgillaArgilla is a robust platform designed to help engineers and data scientists streamline the management of machine learning data workflows. It simplifies tasks like data labeling, annotation, and quality control.

AutheliaThe Single Sign-On Multi-Factor portal for web apps. An open-source authentication and authorization server providing 2FA and SSO via web portal.

### On this page

ConfigurationBase64LinksTags