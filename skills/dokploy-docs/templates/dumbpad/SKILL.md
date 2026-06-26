---
title: "DumbPad | Dokploy"
source: "https://docs.dokploy.com/docs/templates/dumbpad"
category: dokploy-docs
created: "2026-06-25T17:21:46.246Z"
---

DumbPad | Dokploy

# DumbPad

Copy as Markdown

DumbPad is a simple, self-hosted notepad service with PIN protection and no database required.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  dumbpad:
    image: dumbwareio/dumbpad:latest
    restart: unless-stopped
    ports:
      - 3000
    volumes:
      - dumbpad-data:/app/data

volumes:
  dumbpad-data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "dumbpad"
port = 3000
host = "${main_domain}"

[config.env]
NODE_ENV = "production"
SITE_TITLE = "DumbPad"
BASE_URL = "https://${main_domain}"
# Set a PIN (4-10 digits) for access protection. Leave empty to disable.
DUMBPAD_PIN = ""
LOCKOUT_TIME = "15"
MAX_ATTEMPTS = "5"
COOKIE_MAX_AGE = "24"
PAGE_HISTORY_COOKIE_AGE = "365"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBkdW1icGFkOlxuICAgIGltYWdlOiBkdW1id2FyZWlvL2R1bWJwYWQ6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gMzAwMFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGR1bWJwYWQtZGF0YTovYXBwL2RhdGFcblxudm9sdW1lczpcbiAgZHVtYnBhZC1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImR1bWJwYWRcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5OT0RFX0VOViA9IFwicHJvZHVjdGlvblwiXG5TSVRFX1RJVExFID0gXCJEdW1iUGFkXCJcbkJBU0VfVVJMID0gXCJodHRwczovLyR7bWFpbl9kb21haW59XCJcbiMgU2V0IGEgUElOICg0LTEwIGRpZ2l0cykgZm9yIGFjY2VzcyBwcm90ZWN0aW9uLiBMZWF2ZSBlbXB0eSB0byBkaXNhYmxlLlxuRFVNQlBBRF9QSU4gPSBcIlwiXG5MT0NLT1VUX1RJTUUgPSBcIjE1XCJcbk1BWF9BVFRFTVBUUyA9IFwiNVwiXG5DT09LSUVfTUFYX0FHRSA9IFwiMjRcIlxuUEFHRV9ISVNUT1JZX0NPT0tJRV9BR0UgPSBcIjM2NVwiXG5cbltbY29uZmlnLm1vdW50c11dXG4iCn0=
```

## Links

`notepad`,`self-hosted`,`simple`

---

Version:`latest`

DumbDropDumbDrop is a simple, self-hosted file sharing service with no database or authentication required.

Easy!AppointmentsEasy!Appointments is a highly customizable web application that allows customers to book appointments with you via a sophisticated web interface.

### On this page

ConfigurationBase64LinksTags