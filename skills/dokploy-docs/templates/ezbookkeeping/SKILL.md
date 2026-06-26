---
title: "EZBookkeeping | Dokploy"
source: "https://docs.dokploy.com/docs/templates/ezbookkeeping"
category: dokploy-docs
created: "2026-06-25T17:21:47.358Z"
---

EZBookkeeping | Dokploy

# EZBookkeeping

Copy as Markdown

EZBookkeeping is a self-hosted bookkeeping application that helps you manage your personal and business finances. It provides features for tracking income, expenses, accounts, and generating financial reports.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  mysql:
    image: mysql:8.0
    restart: unless-stopped
    environment:
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
      - MYSQL_DATABASE=${MYSQL_DATABASE}
      - MYSQL_USER=${MYSQL_USER}
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}
    volumes:
      - mysql-data:/var/lib/mysql
  ezbookkeeping:
    image: mayswind/ezbookkeeping
    restart: unless-stopped
    depends_on:
      - mysql
    environment:
      - EBK_SERVER_DOMAIN=${EBK_SERVER_DOMAIN}
      - EBK_SERVER_ENABLE_GZIP=${EBK_SERVER_ENABLE_GZIP}
      - EBK_DATABASE_TYPE=${EBK_DATABASE_TYPE}
      - EBK_DATABASE_HOST=${EBK_DATABASE_HOST}
      - EBK_DATABASE_NAME=${EBK_DATABASE_NAME}
      - EBK_DATABASE_USER=${EBK_DATABASE_USER}
      - EBK_DATABASE_PASSWD=${EBK_DATABASE_PASSWD}
      - EBK_LOG_MODE=${EBK_LOG_MODE}
      - EBK_SECURITY_SECRET_KEY=${EBK_SECURITY_SECRET_KEY}
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - storage:/ezbookkeeping/storage
      - logs:/ezbookkeeping/log
volumes:
  mysql-data: {}
  storage: {}
  logs: {}
```

```
[variables]
main_domain = "${domain}"
db_name = "ezbookkeeping"
db_user = "ezbookkeeping"
db_pass = "${password:32}"
root_pass = "${password:32}"
secret_key = "${password:64}"

[config]
[[config.domains]]
serviceName = "ezbookkeeping"
port = 8080
host = "${main_domain}"

[config.env]
MYSQL_ROOT_PASSWORD = "${root_pass}"
MYSQL_DATABASE = "${db_name}"
MYSQL_USER = "${db_user}"
MYSQL_PASSWORD = "${db_pass}"
EBK_SERVER_DOMAIN = "${main_domain}"
EBK_SERVER_ENABLE_GZIP = "true"
EBK_DATABASE_TYPE = "mysql"
EBK_DATABASE_HOST = "mysql:3306"
EBK_DATABASE_NAME = "${db_name}"
EBK_DATABASE_USER = "${db_user}"
EBK_DATABASE_PASSWD = "${db_pass}"
EBK_LOG_MODE = "file"
# Security secret key used for application protection
EBK_SECURITY_SECRET_KEY = "${secret_key}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBteXNxbDpcbiAgICBpbWFnZTogbXlzcWw6OC4wXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTVlTUUxfUk9PVF9QQVNTV09SRD0ke01ZU1FMX1JPT1RfUEFTU1dPUkR9XG4gICAgICAtIE1ZU1FMX0RBVEFCQVNFPSR7TVlTUUxfREFUQUJBU0V9XG4gICAgICAtIE1ZU1FMX1VTRVI9JHtNWVNRTF9VU0VSfVxuICAgICAgLSBNWVNRTF9QQVNTV09SRD0ke01ZU1FMX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIG15c3FsLWRhdGE6L3Zhci9saWIvbXlzcWxcbiAgZXpib29ra2VlcGluZzpcbiAgICBpbWFnZTogbWF5c3dpbmQvZXpib29ra2VlcGluZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gbXlzcWxcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gRUJLX1NFUlZFUl9ET01BSU49JHtFQktfU0VSVkVSX0RPTUFJTn1cbiAgICAgIC0gRUJLX1NFUlZFUl9FTkFCTEVfR1pJUD0ke0VCS19TRVJWRVJfRU5BQkxFX0daSVB9XG4gICAgICAtIEVCS19EQVRBQkFTRV9UWVBFPSR7RUJLX0RBVEFCQVNFX1RZUEV9XG4gICAgICAtIEVCS19EQVRBQkFTRV9IT1NUPSR7RUJLX0RBVEFCQVNFX0hPU1R9XG4gICAgICAtIEVCS19EQVRBQkFTRV9OQU1FPSR7RUJLX0RBVEFCQVNFX05BTUV9XG4gICAgICAtIEVCS19EQVRBQkFTRV9VU0VSPSR7RUJLX0RBVEFCQVNFX1VTRVJ9XG4gICAgICAtIEVCS19EQVRBQkFTRV9QQVNTV0Q9JHtFQktfREFUQUJBU0VfUEFTU1dEfVxuICAgICAgLSBFQktfTE9HX01PREU9JHtFQktfTE9HX01PREV9XG4gICAgICAtIEVCS19TRUNVUklUWV9TRUNSRVRfS0VZPSR7RUJLX1NFQ1VSSVRZX1NFQ1JFVF9LRVl9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gL2V0Yy9sb2NhbHRpbWU6L2V0Yy9sb2NhbHRpbWU6cm9cbiAgICAgIC0gc3RvcmFnZTovZXpib29ra2VlcGluZy9zdG9yYWdlXG4gICAgICAtIGxvZ3M6L2V6Ym9va2tlZXBpbmcvbG9nXG52b2x1bWVzOlxuICBteXNxbC1kYXRhOiB7fVxuICBzdG9yYWdlOiB7fVxuICBsb2dzOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX25hbWUgPSBcImV6Ym9va2tlZXBpbmdcIlxuZGJfdXNlciA9IFwiZXpib29ra2VlcGluZ1wiXG5kYl9wYXNzID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5yb290X3Bhc3MgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbnNlY3JldF9rZXkgPSBcIiR7cGFzc3dvcmQ6NjR9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImV6Ym9va2tlZXBpbmdcIlxucG9ydCA9IDgwODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5NWVNRTF9ST09UX1BBU1NXT1JEID0gXCIke3Jvb3RfcGFzc31cIlxuTVlTUUxfREFUQUJBU0UgPSBcIiR7ZGJfbmFtZX1cIlxuTVlTUUxfVVNFUiA9IFwiJHtkYl91c2VyfVwiXG5NWVNRTF9QQVNTV09SRCA9IFwiJHtkYl9wYXNzfVwiXG5FQktfU0VSVkVSX0RPTUFJTiA9IFwiJHttYWluX2RvbWFpbn1cIlxuRUJLX1NFUlZFUl9FTkFCTEVfR1pJUCA9IFwidHJ1ZVwiXG5FQktfREFUQUJBU0VfVFlQRSA9IFwibXlzcWxcIlxuRUJLX0RBVEFCQVNFX0hPU1QgPSBcIm15c3FsOjMzMDZcIlxuRUJLX0RBVEFCQVNFX05BTUUgPSBcIiR7ZGJfbmFtZX1cIlxuRUJLX0RBVEFCQVNFX1VTRVIgPSBcIiR7ZGJfdXNlcn1cIlxuRUJLX0RBVEFCQVNFX1BBU1NXRCA9IFwiJHtkYl9wYXNzfVwiXG5FQktfTE9HX01PREUgPSBcImZpbGVcIlxuIyBTZWN1cml0eSBzZWNyZXQga2V5IHVzZWQgZm9yIGFwcGxpY2F0aW9uIHByb3RlY3Rpb25cbkVCS19TRUNVUklUWV9TRUNSRVRfS0VZID0gXCIke3NlY3JldF9rZXl9XCJcblxuW1tjb25maWcubW91bnRzXV0gIgp9
```

## Links

`bookkeeping`,`finance`,`accounting`,`self-hosted`,`personal-finance`,`business-finance`

---

Version:`latest`

ExcalidrawExcalidraw is a free and open source online diagramming tool that lets you easily create and share beautiful diagrams.

File BrowserFilebrowser is a standalone file manager for uploading, deleting, previewing, renaming, and editing files, with support for multiple users, each with their own directory.

### On this page

ConfigurationBase64LinksTags