---
title: "Open Journal Systems | Dokploy"
source: "https://docs.dokploy.com/docs/templates/ojs"
category: dokploy-docs
created: "2026-06-25T17:21:54.355Z"
---

Open Journal Systems | Dokploy

# Open Journal Systems

Copy as Markdown

Open Journal Systems (OJS) is a journal management and publishing system that has been developed by the Public Knowledge Project through its federally funded efforts to expand and improve access to research.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  db:
    image: mariadb:11.4
    environment:
      MYSQL_ROOT_PASSWORD: "${MYSQL_ROOT_PASSWORD}"
      MYSQL_DATABASE: "${OJS_DB_NAME}"
      MYSQL_USER: "${OJS_DB_USER}"
      MYSQL_PASSWORD: "${OJS_DB_PASSWORD}"
    volumes:
      - ojs-db-data:/var/lib/mysql
    restart: unless-stopped

  ojs:
    image: "pkpofficial/ojs:3_3_0-21"
    hostname: "${COMPOSE_PROJECT_NAME}"
    ports:
      - 80
      - 443
    volumes:
      - /etc/localtime:/etc/localtime
      - ojs-private-files:/var/www/files
      - ojs-public-files:/var/www/html/public
    depends_on:
      - db
    restart: unless-stopped

volumes:
  ojs-db-data: {}
  ojs-private-files: {}
  ojs-public-files: {}
```

```
[variables]
main_domain = "${domain}"
ojs_password = "${password:16}"
mysql_root_password = "${password:16}"
ojs_db_password = "${password:16}"

[config]
env = [
    "COMPOSE_PROJECT_NAME=ojs",
    "MYSQL_ROOT_PASSWORD=${mysql_root_password}",
    "OJS_DB_NAME=ojs",
    "OJS_DB_USER=ojs",
    "OJS_DB_PASSWORD=${ojs_db_password}",
    "OJS_DB_HOST=db",
    "OJS_DB_DRIVER=mysqli",
    "OJS_CLI_INSTALL=0"
]

[[config.domains]]
serviceName = "ojs"
port = 80
host = "${main_domain}"

# OJS will create its own config.inc.php during installation
# No custom mounts needed - OJS handles configuration through the web installer
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGRiOlxuICAgIGltYWdlOiBtYXJpYWRiOjExLjRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE1ZU1FMX1JPT1RfUEFTU1dPUkQ6IFwiJHtNWVNRTF9ST09UX1BBU1NXT1JEfVwiXG4gICAgICBNWVNRTF9EQVRBQkFTRTogXCIke09KU19EQl9OQU1FfVwiXG4gICAgICBNWVNRTF9VU0VSOiBcIiR7T0pTX0RCX1VTRVJ9XCJcbiAgICAgIE1ZU1FMX1BBU1NXT1JEOiBcIiR7T0pTX0RCX1BBU1NXT1JEfVwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gb2pzLWRiLWRhdGE6L3Zhci9saWIvbXlzcWxcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gIG9qczpcbiAgICBpbWFnZTogXCJwa3BvZmZpY2lhbC9vanM6M18zXzAtMjFcIlxuICAgIGhvc3RuYW1lOiBcIiR7Q09NUE9TRV9QUk9KRUNUX05BTUV9XCJcbiAgICBwb3J0czpcbiAgICAgIC0gODBcbiAgICAgIC0gNDQzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gL2V0Yy9sb2NhbHRpbWU6L2V0Yy9sb2NhbHRpbWVcbiAgICAgIC0gb2pzLXByaXZhdGUtZmlsZXM6L3Zhci93d3cvZmlsZXNcbiAgICAgIC0gb2pzLXB1YmxpYy1maWxlczovdmFyL3d3dy9odG1sL3B1YmxpY1xuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGRiXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxudm9sdW1lczpcbiAgb2pzLWRiLWRhdGE6IHt9XG4gIG9qcy1wcml2YXRlLWZpbGVzOiB7fVxuICBvanMtcHVibGljLWZpbGVzOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbm9qc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoxNn1cIlxubXlzcWxfcm9vdF9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoxNn1cIlxub2pzX2RiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gICAgXCJDT01QT1NFX1BST0pFQ1RfTkFNRT1vanNcIixcbiAgICBcIk1ZU1FMX1JPT1RfUEFTU1dPUkQ9JHtteXNxbF9yb290X3Bhc3N3b3JkfVwiLFxuICAgIFwiT0pTX0RCX05BTUU9b2pzXCIsXG4gICAgXCJPSlNfREJfVVNFUj1vanNcIixcbiAgICBcIk9KU19EQl9QQVNTV09SRD0ke29qc19kYl9wYXNzd29yZH1cIixcbiAgICBcIk9KU19EQl9IT1NUPWRiXCIsXG4gICAgXCJPSlNfREJfRFJJVkVSPW15c3FsaVwiLFxuICAgIFwiT0pTX0NMSV9JTlNUQUxMPTBcIlxuXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJvanNcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbiMgT0pTIHdpbGwgY3JlYXRlIGl0cyBvd24gY29uZmlnLmluYy5waHAgZHVyaW5nIGluc3RhbGxhdGlvblxuIyBObyBjdXN0b20gbW91bnRzIG5lZWRlZCAtIE9KUyBoYW5kbGVzIGNvbmZpZ3VyYXRpb24gdGhyb3VnaCB0aGUgd2ViIGluc3RhbGxlclxuIgp9
```

## Links

`publishing`,`journal`,`research`,`academic`

---

Version:`3.3.0-21`

OdooOdoo is a free and open source business management software that helps you manage your company's operations.

Omni-ToolsOmni-Tools is a collection of useful tools in a single self-hosted web application.

### On this page

ConfigurationBase64LinksTags