---
title: "I Hate Money | Dokploy"
source: "https://docs.dokploy.com/docs/templates/ihatemoney"
category: dokploy-docs
created: "2026-06-25T17:21:49.751Z"
---

I Hate Money | Dokploy

# I Hate Money

Copy as Markdown

I Hate Money is a web application for managing shared expenses among groups of people. It helps you track who owes what to whom, making it easy to split bills and manage group finances.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.9"

services:
  ihatemoney:
    image: ihatemoney/ihatemoney:latest
    environment:
      - DEBUG=False
      - ACTIVATE_DEMO_PROJECT=True
      - ACTIVATE_ADMIN_DASHBOARD=False
      - ADMIN_PASSWORD=${ADMIN_PASSWORD}
      - ALLOW_PUBLIC_PROJECT_CREATION=True
      - BABEL_DEFAULT_TIMEZONE=UTC
      - GREENLET_TEST_CPP=no
      - MAIL_DEFAULT_SENDER=Budget manager <[email protected]>
      - MAIL_PASSWORD=${MAIL_PASSWORD} # used for mail service auth
      - MAIL_PORT=25
      - MAIL_SERVER=localhost
      - MAIL_USE_SSL=False
      - MAIL_USE_TLS=False
      - MAIL_USERNAME=${MAIL_USERNAME} # used for mail service auth
      - SECRET_KEY=${SECRET_KEY} # used for session security
      - SESSION_COOKIE_SECURE=True
      - SHOW_ADMIN_EMAIL=True
      - SQLALCHEMY_DATABASE_URI=sqlite:////database/ihatemoney.db
      - SQLALCHEMY_TRACK_MODIFICATIONS=False
      - APPLICATION_ROOT=/
      - ENABLE_CAPTCHA=False
      - LEGAL_LINK=
      - PORT=8000
      - PUID=0
      - PGID=0
    volumes:
      - ../files/sqlite-db:/database
```

```
[variables]
main_domain = "${domain}"
ADMIN_PASSWORD = "${password:32}"
MAIL_USERNAME = "${username}"
MAIL_PASSWORD = "${password:32}"
SECRET_KEY = "${password:64}"

[config]
[[config.domains]]
serviceName = "ihatemoney"
port = 8000
host = "${main_domain}"

[config.env]
DEBUG = "False"
ACTIVATE_DEMO_PROJECT = "True"
ACTIVATE_ADMIN_DASHBOARD = "False"
ADMIN_PASSWORD = "${ADMIN_PASSWORD}" # used for admin access
ALLOW_PUBLIC_PROJECT_CREATION = "True"
BABEL_DEFAULT_TIMEZONE = "UTC"
GREENLET_TEST_CPP = "no"
MAIL_DEFAULT_SENDER = "Budget manager <[email protected]>"
MAIL_PASSWORD = "${MAIL_PASSWORD}" # used for mail service auth
MAIL_PORT = "25"
MAIL_SERVER = "localhost"
MAIL_USE_SSL = "False"
MAIL_USE_TLS = "False"
MAIL_USERNAME = "${MAIL_USERNAME}" # used for mail service auth
SECRET_KEY = "${SECRET_KEY}" # used for session security
SESSION_COOKIE_SECURE = "True"
SHOW_ADMIN_EMAIL = "True"
SQLALCHEMY_DATABASE_URI = "sqlite:////database/ihatemoney.db"
SQLALCHEMY_TRACK_MODIFICATIONS = "False"
APPLICATION_ROOT = "/"
ENABLE_CAPTCHA = "False"
LEGAL_LINK = ""
PORT = "8000"
PUID = "0"
PGID = "0"

[[config.mounts]]
volumeName = "sqlite-db"
mountPath = "/database"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy45XCJcblxuc2VydmljZXM6XG4gIGloYXRlbW9uZXk6XG4gICAgaW1hZ2U6IGloYXRlbW9uZXkvaWhhdGVtb25leTpsYXRlc3RcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gREVCVUc9RmFsc2VcbiAgICAgIC0gQUNUSVZBVEVfREVNT19QUk9KRUNUPVRydWVcbiAgICAgIC0gQUNUSVZBVEVfQURNSU5fREFTSEJPQVJEPUZhbHNlXG4gICAgICAtIEFETUlOX1BBU1NXT1JEPSR7QURNSU5fUEFTU1dPUkR9XG4gICAgICAtIEFMTE9XX1BVQkxJQ19QUk9KRUNUX0NSRUFUSU9OPVRydWVcbiAgICAgIC0gQkFCRUxfREVGQVVMVF9USU1FWk9ORT1VVENcbiAgICAgIC0gR1JFRU5MRVRfVEVTVF9DUFA9bm9cbiAgICAgIC0gTUFJTF9ERUZBVUxUX1NFTkRFUj1CdWRnZXQgbWFuYWdlciA8YWRtaW5AZXhhbXBsZS5jb20+XG4gICAgICAtIE1BSUxfUEFTU1dPUkQ9JHtNQUlMX1BBU1NXT1JEfSAjIHVzZWQgZm9yIG1haWwgc2VydmljZSBhdXRoXG4gICAgICAtIE1BSUxfUE9SVD0yNVxuICAgICAgLSBNQUlMX1NFUlZFUj1sb2NhbGhvc3RcbiAgICAgIC0gTUFJTF9VU0VfU1NMPUZhbHNlXG4gICAgICAtIE1BSUxfVVNFX1RMUz1GYWxzZVxuICAgICAgLSBNQUlMX1VTRVJOQU1FPSR7TUFJTF9VU0VSTkFNRX0gIyB1c2VkIGZvciBtYWlsIHNlcnZpY2UgYXV0aFxuICAgICAgLSBTRUNSRVRfS0VZPSR7U0VDUkVUX0tFWX0gIyB1c2VkIGZvciBzZXNzaW9uIHNlY3VyaXR5XG4gICAgICAtIFNFU1NJT05fQ09PS0lFX1NFQ1VSRT1UcnVlXG4gICAgICAtIFNIT1dfQURNSU5fRU1BSUw9VHJ1ZVxuICAgICAgLSBTUUxBTENIRU1ZX0RBVEFCQVNFX1VSST1zcWxpdGU6Ly8vL2RhdGFiYXNlL2loYXRlbW9uZXkuZGJcbiAgICAgIC0gU1FMQUxDSEVNWV9UUkFDS19NT0RJRklDQVRJT05TPUZhbHNlXG4gICAgICAtIEFQUExJQ0FUSU9OX1JPT1Q9L1xuICAgICAgLSBFTkFCTEVfQ0FQVENIQT1GYWxzZVxuICAgICAgLSBMRUdBTF9MSU5LPVxuICAgICAgLSBQT1JUPTgwMDBcbiAgICAgIC0gUFVJRD0wXG4gICAgICAtIFBHSUQ9MFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL3NxbGl0ZS1kYjovZGF0YWJhc2VcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5BRE1JTl9QQVNTV09SRCA9IFwiJHtwYXNzd29yZDozMn1cIlxuTUFJTF9VU0VSTkFNRSA9IFwiJHt1c2VybmFtZX1cIlxuTUFJTF9QQVNTV09SRCA9IFwiJHtwYXNzd29yZDozMn1cIlxuU0VDUkVUX0tFWSA9IFwiJHtwYXNzd29yZDo2NH1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiaWhhdGVtb25leVwiXG5wb3J0ID0gODAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkRFQlVHID0gXCJGYWxzZVwiXG5BQ1RJVkFURV9ERU1PX1BST0pFQ1QgPSBcIlRydWVcIlxuQUNUSVZBVEVfQURNSU5fREFTSEJPQVJEID0gXCJGYWxzZVwiXG5BRE1JTl9QQVNTV09SRCA9IFwiJHtBRE1JTl9QQVNTV09SRH1cIiAjIHVzZWQgZm9yIGFkbWluIGFjY2Vzc1xuQUxMT1dfUFVCTElDX1BST0pFQ1RfQ1JFQVRJT04gPSBcIlRydWVcIlxuQkFCRUxfREVGQVVMVF9USU1FWk9ORSA9IFwiVVRDXCJcbkdSRUVOTEVUX1RFU1RfQ1BQID0gXCJub1wiXG5NQUlMX0RFRkFVTFRfU0VOREVSID0gXCJCdWRnZXQgbWFuYWdlciA8YWRtaW5AZXhhbXBsZS5jb20+XCJcbk1BSUxfUEFTU1dPUkQgPSBcIiR7TUFJTF9QQVNTV09SRH1cIiAjIHVzZWQgZm9yIG1haWwgc2VydmljZSBhdXRoXG5NQUlMX1BPUlQgPSBcIjI1XCJcbk1BSUxfU0VSVkVSID0gXCJsb2NhbGhvc3RcIlxuTUFJTF9VU0VfU1NMID0gXCJGYWxzZVwiXG5NQUlMX1VTRV9UTFMgPSBcIkZhbHNlXCJcbk1BSUxfVVNFUk5BTUUgPSBcIiR7TUFJTF9VU0VSTkFNRX1cIiAjIHVzZWQgZm9yIG1haWwgc2VydmljZSBhdXRoXG5TRUNSRVRfS0VZID0gXCIke1NFQ1JFVF9LRVl9XCIgIyB1c2VkIGZvciBzZXNzaW9uIHNlY3VyaXR5XG5TRVNTSU9OX0NPT0tJRV9TRUNVUkUgPSBcIlRydWVcIlxuU0hPV19BRE1JTl9FTUFJTCA9IFwiVHJ1ZVwiXG5TUUxBTENIRU1ZX0RBVEFCQVNFX1VSSSA9IFwic3FsaXRlOi8vLy9kYXRhYmFzZS9paGF0ZW1vbmV5LmRiXCJcblNRTEFMQ0hFTVlfVFJBQ0tfTU9ESUZJQ0FUSU9OUyA9IFwiRmFsc2VcIlxuQVBQTElDQVRJT05fUk9PVCA9IFwiL1wiXG5FTkFCTEVfQ0FQVENIQSA9IFwiRmFsc2VcIlxuTEVHQUxfTElOSyA9IFwiXCJcblBPUlQgPSBcIjgwMDBcIlxuUFVJRCA9IFwiMFwiXG5QR0lEID0gXCIwXCJcblxuW1tjb25maWcubW91bnRzXV1cbnZvbHVtZU5hbWUgPSBcInNxbGl0ZS1kYlwiXG5tb3VudFBhdGggPSBcIi9kYXRhYmFzZVwiXG4iCn0=
```

## Links

`budget`,`finance`,`expense-sharing`,`self-hosted`,`money-management`,`group-finances`

---

Version:`latest`

i18n Blog (Kuno)Kuno is an internationalized blogging platform with a backend built in Go and a frontend in Next.js.

imgproxyimgproxy is a fast and secure image processing server, fronted by nginx with built-in response caching for repeated transformations.

### On this page

ConfigurationBase64LinksTags