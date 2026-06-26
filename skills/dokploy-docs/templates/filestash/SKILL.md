---
title: "Filestash | Dokploy"
source: "https://docs.dokploy.com/docs/templates/filestash"
category: dokploy-docs
created: "2026-06-25T17:21:47.358Z"
---

Filestash | Dokploy

# Filestash

Copy as Markdown

Filestash is the enterprise-grade file manager connecting your storage with your identity provider and authorisations.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  app:
    image: machines/filestash:latest
    restart: always
    environment:
      - APPLICATION_URL=${APPLICATION_URL}
      - CANARY=${CANARY}
      - OFFICE_URL=${OFFICE_URL}
      - OFFICE_FILESTASH_URL=${OFFICE_FILESTASH_URL}
      - OFFICE_REWRITE_URL=${OFFICE_REWRITE_URL}
    ports:
      - 8334
    volumes:
      - filestash:/app/data/state/

  wopi_server:
    image: collabora/code:24.04.10.2.1
    restart: always
    environment:
      # Set below to "true" if you are using custom domain and want to enable SSL
      - extra_params=--o:ssl.enable=false
      - aliasgroup1=https://.*:443
    command:
      - /bin/bash
      - -c
      - |
          curl -o /usr/share/coolwsd/browser/dist/branding-desktop.css https://gist.githubusercontent.com/mickael-kerjean/bc1f57cd312cf04731d30185cc4e7ba2/raw/d706dcdf23c21441e5af289d871b33defc2770ea/destop.css
          /bin/su -s /bin/bash -c '/start-collabora-online.sh' cool
    user: root
    ports:
      - 9980

volumes:
  filestash:
```

```
[variables]
main_domain = "${domain}"

[[config.domains]]
serviceName = "app"
port = 8334
host = "${main_domain}"

[config.env]
APPLICATION_URL = "${main_domain}"
CANARY = "true"
OFFICE_URL = "http://wopi_server:9980"
OFFICE_FILESTASH_URL = "http://app:8334"
OFFICE_REWRITE_URL = "http://127.0.0.1:9980"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBhcHA6XG4gICAgaW1hZ2U6IG1hY2hpbmVzL2ZpbGVzdGFzaDpsYXRlc3RcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQVBQTElDQVRJT05fVVJMPSR7QVBQTElDQVRJT05fVVJMfVxuICAgICAgLSBDQU5BUlk9JHtDQU5BUll9XG4gICAgICAtIE9GRklDRV9VUkw9JHtPRkZJQ0VfVVJMfVxuICAgICAgLSBPRkZJQ0VfRklMRVNUQVNIX1VSTD0ke09GRklDRV9GSUxFU1RBU0hfVVJMfVxuICAgICAgLSBPRkZJQ0VfUkVXUklURV9VUkw9JHtPRkZJQ0VfUkVXUklURV9VUkx9XG4gICAgcG9ydHM6XG4gICAgICAtIDgzMzRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBmaWxlc3Rhc2g6L2FwcC9kYXRhL3N0YXRlL1xuXG4gIHdvcGlfc2VydmVyOlxuICAgIGltYWdlOiBjb2xsYWJvcmEvY29kZToyNC4wNC4xMC4yLjFcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgU2V0IGJlbG93IHRvIFwidHJ1ZVwiIGlmIHlvdSBhcmUgdXNpbmcgY3VzdG9tIGRvbWFpbiBhbmQgd2FudCB0byBlbmFibGUgU1NMXG4gICAgICAtIGV4dHJhX3BhcmFtcz0tLW86c3NsLmVuYWJsZT1mYWxzZVxuICAgICAgLSBhbGlhc2dyb3VwMT1odHRwczovLy4qOjQ0M1xuICAgIGNvbW1hbmQ6XG4gICAgICAtIC9iaW4vYmFzaFxuICAgICAgLSAtY1xuICAgICAgLSB8XG4gICAgICAgICAgY3VybCAtbyAvdXNyL3NoYXJlL2Nvb2x3c2QvYnJvd3Nlci9kaXN0L2JyYW5kaW5nLWRlc2t0b3AuY3NzIGh0dHBzOi8vZ2lzdC5naXRodWJ1c2VyY29udGVudC5jb20vbWlja2FlbC1rZXJqZWFuL2JjMWY1N2NkMzEyY2YwNDczMWQzMDE4NWNjNGU3YmEyL3Jhdy9kNzA2ZGNkZjIzYzIxNDQxZTVhZjI4OWQ4NzFiMzNkZWZjMjc3MGVhL2Rlc3RvcC5jc3NcbiAgICAgICAgICAvYmluL3N1IC1zIC9iaW4vYmFzaCAtYyAnL3N0YXJ0LWNvbGxhYm9yYS1vbmxpbmUuc2gnIGNvb2xcbiAgICB1c2VyOiByb290XG4gICAgcG9ydHM6XG4gICAgICAtIDk5ODBcblxudm9sdW1lczpcbiAgZmlsZXN0YXNoOiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFwcFwiXG5wb3J0ID0gODMzNFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkFQUExJQ0FUSU9OX1VSTCA9IFwiJHttYWluX2RvbWFpbn1cIlxuQ0FOQVJZID0gXCJ0cnVlXCJcbk9GRklDRV9VUkwgPSBcImh0dHA6Ly93b3BpX3NlcnZlcjo5OTgwXCJcbk9GRklDRV9GSUxFU1RBU0hfVVJMID0gXCJodHRwOi8vYXBwOjgzMzRcIlxuT0ZGSUNFX1JFV1JJVEVfVVJMID0gXCJodHRwOi8vMTI3LjAuMC4xOjk5ODBcIiIKfQ==
```

## Links

`file-manager`,`document-editor`,`self-hosted`

---

Version:`latest`

File BrowserFilebrowser is a standalone file manager for uploading, deleting, previewing, renaming, and editing files, with support for multiple users, each with their own directory.

FirecrawlFirecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data. It can crawl all accessible subpages and provide clean data for each.

### On this page

ConfigurationBase64LinksTags