---
title: "OpenResty Manager | Dokploy"
source: "https://docs.dokploy.com/docs/templates/openresty-manager"
category: dokploy-docs
created: "2026-06-25T17:21:55.476Z"
---

OpenResty Manager | Dokploy

# OpenResty Manager

Copy as Markdown

The easiest using, powerful and beautiful OpenResty Manager (Nginx Enhanced Version) , open source alternative to OpenResty Edge, which can enable you to easily reverse proxy your websites with security running at home or internet, including Access Control, HTTP Flood Protection, Free SSL, without having to know too much about OpenResty or Let's Encrypt.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  openresty-manager:
   image: uusec/openresty-manager:latest
   restart: always
   volumes:
     - /etc/localtime:/etc/localtime:ro
     - /etc/resolv.conf:/etc/resolv.conf:ro
     - om_acme:/opt/om/acme
     - om_data:/opt/om/data
     - om_conf:/opt/om/nginx/conf

volumes:
  om_acme:
  om_data:
  om_conf:
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "openresty-manager"
port = 34567
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBvcGVucmVzdHktbWFuYWdlcjpcbiAgIGltYWdlOiB1dXNlYy9vcGVucmVzdHktbWFuYWdlcjpsYXRlc3RcbiAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgdm9sdW1lczpcbiAgICAgLSAvZXRjL2xvY2FsdGltZTovZXRjL2xvY2FsdGltZTpyb1xuICAgICAtIC9ldGMvcmVzb2x2LmNvbmY6L2V0Yy9yZXNvbHYuY29uZjpyb1xuICAgICAtIG9tX2FjbWU6L29wdC9vbS9hY21lXG4gICAgIC0gb21fZGF0YTovb3B0L29tL2RhdGFcbiAgICAgLSBvbV9jb25mOi9vcHQvb20vbmdpbngvY29uZlxuXG52b2x1bWVzOlxuICBvbV9hY21lOlxuICBvbV9kYXRhOlxuICBvbV9jb25mOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtdXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJvcGVucmVzdHktbWFuYWdlclwiXG5wb3J0ID0gMzQ1Njdcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`web`,`proxy`,`security`,`self-hosted`,`openresty`,`nginx`

---

Version:`1.2.0`

OpenPanelAn open-source web and product analytics platform that combines the power of Mixpanel with the ease of Plausible and one of the best Google Analytics replacements.

OpenSpeedTestOpenSpeedTest is a 100% browser-based HTML5 network performance estimation tool for accurately measuring network speed.

### On this page

ConfigurationBase64LinksTags