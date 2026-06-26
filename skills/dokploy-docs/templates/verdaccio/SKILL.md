---
title: "Verdaccio | Dokploy"
source: "https://docs.dokploy.com/docs/templates/verdaccio"
category: dokploy-docs
created: "2026-06-25T17:22:01.420Z"
---

Verdaccio | Dokploy

# Verdaccio

Copy as Markdown

A lightweight Node.js private proxy registry

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  verdaccio:
    image: verdaccio/verdaccio:6
    environment:
      - VERDACCIO_PORT=4873
    ports:
      - 4873
    volumes:
      - verdaccio_storage:/verdaccio/storage
      - verdaccio_plugins:/verdaccio/plugins
      - ../files/conf:/verdaccio/conf

volumes:
  verdaccio_storage:
  verdaccio_plugins:
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "verdaccio"
port = 4873
host = "${main_domain}"

[[config.mounts]]
filePath = "/conf/config.yaml"
content = """
#
# This is the default configuration file. It allows all users to do anything,
# please read carefully the documentation and best practices to
# improve security.
#
# Look here for more config file examples:
# https://github.com/verdaccio/verdaccio/blob/master/docker-examples/README.md
#
# Read about the best practices
# https://verdaccio.org/docs/best

# Path to a directory with all packages
storage: /verdaccio/storage/data

# Path to a directory with plugins to include, the plugins folder has the higher priority for loading plugins
# Disable this folder to avoid warnings if is not used
plugins: /verdaccio/plugins

# Web UI settings
# https://verdaccio.org/docs/webui
web:
  title: Verdaccio
  # Disable complete web UI
  # enabled: false
  # Custom colors for header background and font
  # primaryColor: "#4b5e40"
  # Custom logos and favicon
  # logo: ./path/to/logo.png
  # logoDark: ./path/to/logoDark.png
  # favicon: ./path/to/favicon.ico
  # Disable gravatar support
  # gravatar: false
  # By default, packages are ordered ascending
  # sort_packages: asc | desc
  # Convert your UI to the dark side
  # darkMode: true
  # html_cache: true
  # By default, all features are displayed
  # login: true
  # showInfo: true
  # showSettings: true
  # In combination with darkMode you can force specific theme
  # showThemeSwitch: true
  # showFooter: true
  # showSearch: true
  # showRaw: true
  # showDownloadTarball: true
  # showUplinks: true
  #
  # HTML tags injected before ends </head>
  # metaScripts:
  #   - '<script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>'
  #   - '<script type="text/javascript" src="https://browser.sentry-cdn.com/5.15.5/bundle.min.js"></script>'
  #   - '<meta name="robots" content="noindex">'
  #
  # HTML tags injected as first child in <body>
  # scriptsBodyBefore:
  #   - '<div id="myId">html before webpack scripts</div>'
  #
  # HTML tags injected as last child in </body>
  # scriptsBodyAfter:
  #   - '<script type="text/javascript" src="https://my.company.com/customJS.min.js"></script>'
  #
  # Public path for template manifest scripts (only manifest)
  # publicPath: http://somedomain.org/

# Settings for authentication plugin
# https://verdaccio.org/docs/configuration#authentication
auth:
  htpasswd:
    file: /verdaccio/storage/htpasswd
    # Maximum amount of users allowed to register, defaults to "+inf".
    # You can set this to -1 to disable registration.
    max_users: 1

# A list of other known repositories we can talk to
# https://verdaccio.org/docs/configuration#uplinks
uplinks:
  npmjs:
    url: https://registry.npmjs.org/

# Learn how to protect your packages
# https://verdaccio.org/docs/protect-your-dependencies/
# https://verdaccio.org/docs/configuration#packages
packages:
  '@*/*':
    # scoped packages
    access: $all
    publish: $authenticated
    unpublish: $authenticated
    proxy: npmjs

  '**':
    # allow all users (including non-authenticated users) to read and
    # publish all packages
    #
    # you can specify usernames/groupnames (depending on your auth plugin)
    # and three keywords: "$all", "$anonymous", "$authenticated"
    access: $all

    # allow all known users to publish/unpublish packages
    # (anyone can register by default, remember?)
    publish: $authenticated
    unpublish: $authenticated

    # if package is not available locally, proxy requests to 'npmjs' registry
    proxy: npmjs

# To improve your security configuration and avoid dependency confusion
# consider removing the proxy property for private packages
# https://verdaccio.org/docs/best#remove-proxy-to-increase-security-at-private-packages

# https://verdaccio.org/docs/configuration#server
# You can specify HTTP/1.1 server keep alive timeout in seconds for incoming connections.
# A value of 0 makes the http server behave similarly to Node.js versions prior to 8.0.0, which did not have a keep-alive timeout.
# WORKAROUND: Through given configuration you can workaround following issue https://github.com/verdaccio/verdaccio/issues/301. Set to 0 in case 60 is not enough.
server:
  keepAliveTimeout: 60
  # The pluginPrefix replaces the default plugins prefix which is `verdaccio`. Please don't include `-`. If `something` is provided
  # the resolved package will be `something-xxxx`.
  # pluginPrefix: something
  # A regex for the password validation /.{3}$/ (3 characters min)
  # An example to limit to 10 characters minimum
  # passwordValidationRegex: /.{10}$/
  # Allow `req.ip` to resolve properly when Verdaccio is behind a proxy or load-balancer
  # https://expressjs.com/en/guide/behind-proxies.html
  # trustProxy: '127.0.0.1'

# https://verdaccio.org/docs/configuration#offline-publish
# publish:
#   allow_offline: false
#   check_owners: false
#   keep_readmes: 'latest' | 'tagged' | 'all'

# Define public URL of registry in combination with VERDACCIO_PUBLIC_URL environment variable
# https://verdaccio.org/docs/configuration#url-prefix
# url_prefix: /verdaccio/
#
# Examples:
# VERDACCIO_PUBLIC_URL='https://somedomain.org'
# url_prefix: '/my_prefix'
# // url -> https://somedomain.org/my_prefix/
#
# VERDACCIO_PUBLIC_URL='https://somedomain.org'
# url_prefix: '/'
# // url -> https://somedomain.org/
#
# VERDACCIO_PUBLIC_URL='https://somedomain.org/first_prefix'
# url_prefix: '/second_prefix'
# // url -> https://somedomain.org/second_prefix/

# Security settings
# https://verdaccio.org/docs/configuration#security
# security:
#   api:
#     legacy: true
#     jwt:
#       sign:
#         expiresIn: 29d
#       verify:
#         someProp: [value]
#   web:
#     sign:
#       expiresIn: 1h # 1 hour by default
#     verify:
#       someProp: [value]

# https://verdaccio.org/docs/configuration#user-rate-limit
# userRateLimit:
#   windowMs: 50000
#   max: 1000

# https://verdaccio.org/docs/configuration#max-body-size
# max_body_size: 10mb

# https://verdaccio.org/docs/configuration#listen-port
# listen:
#   - localhost:4873            # default value
#   - http://localhost:4873     # same thing
#   - 0.0.0.0:4873              # listen on all addresses (INADDR_ANY)
#   - https://example.org:4873  # if you want to use https
#   - "[::1]:4873"              # ipv6
#   - unix:/tmp/verdaccio.sock  # unix socket

# The HTTPS configuration is useful if you do not consider use a HTTP Proxy
# https://verdaccio.org/docs/configuration#https
# https:
#   key: ./path/verdaccio-key.pem
#   cert: ./path/verdaccio-cert.pem
#   ca: ./path/verdaccio-csr.pem

# https://verdaccio.org/docs/configuration#proxy
# http_proxy: http://something.local/
# https_proxy: https://something.local/
# no_proxy: localhost,127.0.0.1,server.local

# https://verdaccio.org/docs/configuration#notifications
# notify:
#   method: 'POST'
#   headers: '[{ "Content-Type": "application/json" }]'
#   endpoint: 'https://usagge.hipchat.com/v2/room/3729485/notification?auth_token=mySecretToken'
#   content: '{"color":"green","message":"New package published: * {{ name }}*","notify":true,"message_format":"text"}'

# Settings for middleware plugins
# https://verdaccio.org/docs/plugins#middleware-configuration
middlewares:
  audit:
    enabled: true
    # timeout: 10000

# Log settings
# https://verdaccio.org/docs/logger
# Redaction: https://getpino.io/#/docs/redaction
# Synchronous logging: https://getpino.io/#/docs/asynchronous
log:
  type: stdout
  format: pretty
  level: http
#  redact:
#    paths: ['req.header.authorization','req.header.cookie','req.remoteAddress','req.remotePort','ip','remoteIP','user','msg']
#    censor: '<redacted>'
#  sync: true

# Feature flags (experimental settings that can be changed or removed in the future)
# https://verdaccio.org/docs/configuration#experiments
# experiments:
#  # Support for npm token command
#  token: false
#  # Enable tarball URL redirect for hosting tarball with a different server.
#  # The tarball_url_redirect can be a template string
#  tarball_url_redirect: 'https://mycdn.com/verdaccio/${packageName}/${filename}'
#  # The tarball_url_redirect can be a function, takes packageName and filename and returns the url,
#  # when working with a js configuration file
#  tarball_url_redirect(packageName, filename) {
#    const signedUrl = // generate a signed url
#    return signedUrl;
#  }
# Renamed from "experiments" to "flags" in next major release
# flags:
#  changePassword: true
#  searchRemote: true

# Translate your registry, API and web UI
# List of the available translations https://github.com/verdaccio/verdaccio/blob/master/packages/plugins/ui-theme/src/i18n/ABOUT_TRANSLATIONS.md
i18n:
    web: en-US
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHZlcmRhY2NpbzpcbiAgICBpbWFnZTogdmVyZGFjY2lvL3ZlcmRhY2Npbzo2XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFZFUkRBQ0NJT19QT1JUPTQ4NzNcbiAgICBwb3J0czpcbiAgICAgIC0gNDg3M1xuICAgIHZvbHVtZXM6XG4gICAgICAtIHZlcmRhY2Npb19zdG9yYWdlOi92ZXJkYWNjaW8vc3RvcmFnZVxuICAgICAgLSB2ZXJkYWNjaW9fcGx1Z2luczovdmVyZGFjY2lvL3BsdWdpbnNcbiAgICAgIC0gLi4vZmlsZXMvY29uZjovdmVyZGFjY2lvL2NvbmZcblxudm9sdW1lczpcbiAgdmVyZGFjY2lvX3N0b3JhZ2U6XG4gIHZlcmRhY2Npb19wbHVnaW5zOiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ2ZXJkYWNjaW9cIlxucG9ydCA9IDQ4NzNcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvY29uZi9jb25maWcueWFtbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jXG4jIFRoaXMgaXMgdGhlIGRlZmF1bHQgY29uZmlndXJhdGlvbiBmaWxlLiBJdCBhbGxvd3MgYWxsIHVzZXJzIHRvIGRvIGFueXRoaW5nLFxuIyBwbGVhc2UgcmVhZCBjYXJlZnVsbHkgdGhlIGRvY3VtZW50YXRpb24gYW5kIGJlc3QgcHJhY3RpY2VzIHRvXG4jIGltcHJvdmUgc2VjdXJpdHkuXG4jXG4jIExvb2sgaGVyZSBmb3IgbW9yZSBjb25maWcgZmlsZSBleGFtcGxlczpcbiMgaHR0cHM6Ly9naXRodWIuY29tL3ZlcmRhY2Npby92ZXJkYWNjaW8vYmxvYi9tYXN0ZXIvZG9ja2VyLWV4YW1wbGVzL1JFQURNRS5tZFxuI1xuIyBSZWFkIGFib3V0IHRoZSBiZXN0IHByYWN0aWNlc1xuIyBodHRwczovL3ZlcmRhY2Npby5vcmcvZG9jcy9iZXN0XG5cbiMgUGF0aCB0byBhIGRpcmVjdG9yeSB3aXRoIGFsbCBwYWNrYWdlc1xuc3RvcmFnZTogL3ZlcmRhY2Npby9zdG9yYWdlL2RhdGFcblxuIyBQYXRoIHRvIGEgZGlyZWN0b3J5IHdpdGggcGx1Z2lucyB0byBpbmNsdWRlLCB0aGUgcGx1Z2lucyBmb2xkZXIgaGFzIHRoZSBoaWdoZXIgcHJpb3JpdHkgZm9yIGxvYWRpbmcgcGx1Z2luc1xuIyBEaXNhYmxlIHRoaXMgZm9sZGVyIHRvIGF2b2lkIHdhcm5pbmdzIGlmIGlzIG5vdCB1c2VkXG5wbHVnaW5zOiAvdmVyZGFjY2lvL3BsdWdpbnNcblxuIyBXZWIgVUkgc2V0dGluZ3NcbiMgaHR0cHM6Ly92ZXJkYWNjaW8ub3JnL2RvY3Mvd2VidWlcbndlYjpcbiAgdGl0bGU6IFZlcmRhY2Npb1xuICAjIERpc2FibGUgY29tcGxldGUgd2ViIFVJXG4gICMgZW5hYmxlZDogZmFsc2VcbiAgIyBDdXN0b20gY29sb3JzIGZvciBoZWFkZXIgYmFja2dyb3VuZCBhbmQgZm9udFxuICAjIHByaW1hcnlDb2xvcjogXCIjNGI1ZTQwXCJcbiAgIyBDdXN0b20gbG9nb3MgYW5kIGZhdmljb25cbiAgIyBsb2dvOiAuL3BhdGgvdG8vbG9nby5wbmdcbiAgIyBsb2dvRGFyazogLi9wYXRoL3RvL2xvZ29EYXJrLnBuZ1xuICAjIGZhdmljb246IC4vcGF0aC90by9mYXZpY29uLmljb1xuICAjIERpc2FibGUgZ3JhdmF0YXIgc3VwcG9ydFxuICAjIGdyYXZhdGFyOiBmYWxzZVxuICAjIEJ5IGRlZmF1bHQsIHBhY2thZ2VzIGFyZSBvcmRlcmVkIGFzY2VuZGluZ1xuICAjIHNvcnRfcGFja2FnZXM6IGFzYyB8IGRlc2NcbiAgIyBDb252ZXJ0IHlvdXIgVUkgdG8gdGhlIGRhcmsgc2lkZVxuICAjIGRhcmtNb2RlOiB0cnVlXG4gICMgaHRtbF9jYWNoZTogdHJ1ZVxuICAjIEJ5IGRlZmF1bHQsIGFsbCBmZWF0dXJlcyBhcmUgZGlzcGxheWVkXG4gICMgbG9naW46IHRydWVcbiAgIyBzaG93SW5mbzogdHJ1ZVxuICAjIHNob3dTZXR0aW5nczogdHJ1ZVxuICAjIEluIGNvbWJpbmF0aW9uIHdpdGggZGFya01vZGUgeW91IGNhbiBmb3JjZSBzcGVjaWZpYyB0aGVtZVxuICAjIHNob3dUaGVtZVN3aXRjaDogdHJ1ZVxuICAjIHNob3dGb290ZXI6IHRydWVcbiAgIyBzaG93U2VhcmNoOiB0cnVlXG4gICMgc2hvd1JhdzogdHJ1ZVxuICAjIHNob3dEb3dubG9hZFRhcmJhbGw6IHRydWVcbiAgIyBzaG93VXBsaW5rczogdHJ1ZVxuICAjXG4gICMgSFRNTCB0YWdzIGluamVjdGVkIGJlZm9yZSBlbmRzIDwvaGVhZD5cbiAgIyBtZXRhU2NyaXB0czpcbiAgIyAgIC0gJzxzY3JpcHQgdHlwZT1cInRleHQvamF2YXNjcmlwdFwiIHNyYz1cImh0dHBzOi8vY29kZS5qcXVlcnkuY29tL2pxdWVyeS0zLjUuMS5zbGltLm1pbi5qc1wiPjwvc2NyaXB0PidcbiAgIyAgIC0gJzxzY3JpcHQgdHlwZT1cInRleHQvamF2YXNjcmlwdFwiIHNyYz1cImh0dHBzOi8vYnJvd3Nlci5zZW50cnktY2RuLmNvbS81LjE1LjUvYnVuZGxlLm1pbi5qc1wiPjwvc2NyaXB0PidcbiAgIyAgIC0gJzxtZXRhIG5hbWU9XCJyb2JvdHNcIiBjb250ZW50PVwibm9pbmRleFwiPidcbiAgI1xuICAjIEhUTUwgdGFncyBpbmplY3RlZCBhcyBmaXJzdCBjaGlsZCBpbiA8Ym9keT5cbiAgIyBzY3JpcHRzQm9keUJlZm9yZTpcbiAgIyAgIC0gJzxkaXYgaWQ9XCJteUlkXCI+aHRtbCBiZWZvcmUgd2VicGFjayBzY3JpcHRzPC9kaXY+J1xuICAjXG4gICMgSFRNTCB0YWdzIGluamVjdGVkIGFzIGxhc3QgY2hpbGQgaW4gPC9ib2R5PlxuICAjIHNjcmlwdHNCb2R5QWZ0ZXI6XG4gICMgICAtICc8c2NyaXB0IHR5cGU9XCJ0ZXh0L2phdmFzY3JpcHRcIiBzcmM9XCJodHRwczovL215LmNvbXBhbnkuY29tL2N1c3RvbUpTLm1pbi5qc1wiPjwvc2NyaXB0PidcbiAgI1xuICAjIFB1YmxpYyBwYXRoIGZvciB0ZW1wbGF0ZSBtYW5pZmVzdCBzY3JpcHRzIChvbmx5IG1hbmlmZXN0KVxuICAjIHB1YmxpY1BhdGg6IGh0dHA6Ly9zb21lZG9tYWluLm9yZy9cblxuIyBTZXR0aW5ncyBmb3IgYXV0aGVudGljYXRpb24gcGx1Z2luXG4jIGh0dHBzOi8vdmVyZGFjY2lvLm9yZy9kb2NzL2NvbmZpZ3VyYXRpb24jYXV0aGVudGljYXRpb25cbmF1dGg6XG4gIGh0cGFzc3dkOlxuICAgIGZpbGU6IC92ZXJkYWNjaW8vc3RvcmFnZS9odHBhc3N3ZFxuICAgICMgTWF4aW11bSBhbW91bnQgb2YgdXNlcnMgYWxsb3dlZCB0byByZWdpc3RlciwgZGVmYXVsdHMgdG8gXCIraW5mXCIuXG4gICAgIyBZb3UgY2FuIHNldCB0aGlzIHRvIC0xIHRvIGRpc2FibGUgcmVnaXN0cmF0aW9uLlxuICAgIG1heF91c2VyczogMVxuXG4jIEEgbGlzdCBvZiBvdGhlciBrbm93biByZXBvc2l0b3JpZXMgd2UgY2FuIHRhbGsgdG9cbiMgaHR0cHM6Ly92ZXJkYWNjaW8ub3JnL2RvY3MvY29uZmlndXJhdGlvbiN1cGxpbmtzXG51cGxpbmtzOlxuICBucG1qczpcbiAgICB1cmw6IGh0dHBzOi8vcmVnaXN0cnkubnBtanMub3JnL1xuXG4jIExlYXJuIGhvdyB0byBwcm90ZWN0IHlvdXIgcGFja2FnZXNcbiMgaHR0cHM6Ly92ZXJkYWNjaW8ub3JnL2RvY3MvcHJvdGVjdC15b3VyLWRlcGVuZGVuY2llcy9cbiMgaHR0cHM6Ly92ZXJkYWNjaW8ub3JnL2RvY3MvY29uZmlndXJhdGlvbiNwYWNrYWdlc1xucGFja2FnZXM6XG4gICdAKi8qJzpcbiAgICAjIHNjb3BlZCBwYWNrYWdlc1xuICAgIGFjY2VzczogJGFsbFxuICAgIHB1Ymxpc2g6ICRhdXRoZW50aWNhdGVkXG4gICAgdW5wdWJsaXNoOiAkYXV0aGVudGljYXRlZFxuICAgIHByb3h5OiBucG1qc1xuXG4gICcqKic6XG4gICAgIyBhbGxvdyBhbGwgdXNlcnMgKGluY2x1ZGluZyBub24tYXV0aGVudGljYXRlZCB1c2VycykgdG8gcmVhZCBhbmRcbiAgICAjIHB1Ymxpc2ggYWxsIHBhY2thZ2VzXG4gICAgI1xuICAgICMgeW91IGNhbiBzcGVjaWZ5IHVzZXJuYW1lcy9ncm91cG5hbWVzIChkZXBlbmRpbmcgb24geW91ciBhdXRoIHBsdWdpbilcbiAgICAjIGFuZCB0aHJlZSBrZXl3b3JkczogXCIkYWxsXCIsIFwiJGFub255bW91c1wiLCBcIiRhdXRoZW50aWNhdGVkXCJcbiAgICBhY2Nlc3M6ICRhbGxcblxuICAgICMgYWxsb3cgYWxsIGtub3duIHVzZXJzIHRvIHB1Ymxpc2gvdW5wdWJsaXNoIHBhY2thZ2VzXG4gICAgIyAoYW55b25lIGNhbiByZWdpc3RlciBieSBkZWZhdWx0LCByZW1lbWJlcj8pXG4gICAgcHVibGlzaDogJGF1dGhlbnRpY2F0ZWRcbiAgICB1bnB1Ymxpc2g6ICRhdXRoZW50aWNhdGVkXG5cbiAgICAjIGlmIHBhY2thZ2UgaXMgbm90IGF2YWlsYWJsZSBsb2NhbGx5LCBwcm94eSByZXF1ZXN0cyB0byAnbnBtanMnIHJlZ2lzdHJ5XG4gICAgcHJveHk6IG5wbWpzXG5cbiMgVG8gaW1wcm92ZSB5b3VyIHNlY3VyaXR5IGNvbmZpZ3VyYXRpb24gYW5kIGF2b2lkIGRlcGVuZGVuY3kgY29uZnVzaW9uXG4jIGNvbnNpZGVyIHJlbW92aW5nIHRoZSBwcm94eSBwcm9wZXJ0eSBmb3IgcHJpdmF0ZSBwYWNrYWdlc1xuIyBodHRwczovL3ZlcmRhY2Npby5vcmcvZG9jcy9iZXN0I3JlbW92ZS1wcm94eS10by1pbmNyZWFzZS1zZWN1cml0eS1hdC1wcml2YXRlLXBhY2thZ2VzXG5cbiMgaHR0cHM6Ly92ZXJkYWNjaW8ub3JnL2RvY3MvY29uZmlndXJhdGlvbiNzZXJ2ZXJcbiMgWW91IGNhbiBzcGVjaWZ5IEhUVFAvMS4xIHNlcnZlciBrZWVwIGFsaXZlIHRpbWVvdXQgaW4gc2Vjb25kcyBmb3IgaW5jb21pbmcgY29ubmVjdGlvbnMuXG4jIEEgdmFsdWUgb2YgMCBtYWtlcyB0aGUgaHR0cCBzZXJ2ZXIgYmVoYXZlIHNpbWlsYXJseSB0byBOb2RlLmpzIHZlcnNpb25zIHByaW9yIHRvIDguMC4wLCB3aGljaCBkaWQgbm90IGhhdmUgYSBrZWVwLWFsaXZlIHRpbWVvdXQuXG4jIFdPUktBUk9VTkQ6IFRocm91Z2ggZ2l2ZW4gY29uZmlndXJhdGlvbiB5b3UgY2FuIHdvcmthcm91bmQgZm9sbG93aW5nIGlzc3VlIGh0dHBzOi8vZ2l0aHViLmNvbS92ZXJkYWNjaW8vdmVyZGFjY2lvL2lzc3Vlcy8zMDEuIFNldCB0byAwIGluIGNhc2UgNjAgaXMgbm90IGVub3VnaC5cbnNlcnZlcjpcbiAga2VlcEFsaXZlVGltZW91dDogNjBcbiAgIyBUaGUgcGx1Z2luUHJlZml4IHJlcGxhY2VzIHRoZSBkZWZhdWx0IHBsdWdpbnMgcHJlZml4IHdoaWNoIGlzIGB2ZXJkYWNjaW9gLiBQbGVhc2UgZG9uJ3QgaW5jbHVkZSBgLWAuIElmIGBzb21ldGhpbmdgIGlzIHByb3ZpZGVkXG4gICMgdGhlIHJlc29sdmVkIHBhY2thZ2Ugd2lsbCBiZSBgc29tZXRoaW5nLXh4eHhgLlxuICAjIHBsdWdpblByZWZpeDogc29tZXRoaW5nXG4gICMgQSByZWdleCBmb3IgdGhlIHBhc3N3b3JkIHZhbGlkYXRpb24gLy57M30kLyAoMyBjaGFyYWN0ZXJzIG1pbilcbiAgIyBBbiBleGFtcGxlIHRvIGxpbWl0IHRvIDEwIGNoYXJhY3RlcnMgbWluaW11bVxuICAjIHBhc3N3b3JkVmFsaWRhdGlvblJlZ2V4OiAvLnsxMH0kL1xuICAjIEFsbG93IGByZXEuaXBgIHRvIHJlc29sdmUgcHJvcGVybHkgd2hlbiBWZXJkYWNjaW8gaXMgYmVoaW5kIGEgcHJveHkgb3IgbG9hZC1iYWxhbmNlclxuICAjIGh0dHBzOi8vZXhwcmVzc2pzLmNvbS9lbi9ndWlkZS9iZWhpbmQtcHJveGllcy5odG1sXG4gICMgdHJ1c3RQcm94eTogJzEyNy4wLjAuMSdcblxuIyBodHRwczovL3ZlcmRhY2Npby5vcmcvZG9jcy9jb25maWd1cmF0aW9uI29mZmxpbmUtcHVibGlzaFxuIyBwdWJsaXNoOlxuIyAgIGFsbG93X29mZmxpbmU6IGZhbHNlXG4jICAgY2hlY2tfb3duZXJzOiBmYWxzZVxuIyAgIGtlZXBfcmVhZG1lczogJ2xhdGVzdCcgfCAndGFnZ2VkJyB8ICdhbGwnXG5cbiMgRGVmaW5lIHB1YmxpYyBVUkwgb2YgcmVnaXN0cnkgaW4gY29tYmluYXRpb24gd2l0aCBWRVJEQUNDSU9fUFVCTElDX1VSTCBlbnZpcm9ubWVudCB2YXJpYWJsZVxuIyBodHRwczovL3ZlcmRhY2Npby5vcmcvZG9jcy9jb25maWd1cmF0aW9uI3VybC1wcmVmaXhcbiMgdXJsX3ByZWZpeDogL3ZlcmRhY2Npby9cbiNcbiMgRXhhbXBsZXM6XG4jIFZFUkRBQ0NJT19QVUJMSUNfVVJMPSdodHRwczovL3NvbWVkb21haW4ub3JnJ1xuIyB1cmxfcHJlZml4OiAnL215X3ByZWZpeCdcbiMgLy8gdXJsIC0+IGh0dHBzOi8vc29tZWRvbWFpbi5vcmcvbXlfcHJlZml4L1xuI1xuIyBWRVJEQUNDSU9fUFVCTElDX1VSTD0naHR0cHM6Ly9zb21lZG9tYWluLm9yZydcbiMgdXJsX3ByZWZpeDogJy8nXG4jIC8vIHVybCAtPiBodHRwczovL3NvbWVkb21haW4ub3JnL1xuI1xuIyBWRVJEQUNDSU9fUFVCTElDX1VSTD0naHR0cHM6Ly9zb21lZG9tYWluLm9yZy9maXJzdF9wcmVmaXgnXG4jIHVybF9wcmVmaXg6ICcvc2Vjb25kX3ByZWZpeCdcbiMgLy8gdXJsIC0+IGh0dHBzOi8vc29tZWRvbWFpbi5vcmcvc2Vjb25kX3ByZWZpeC9cblxuIyBTZWN1cml0eSBzZXR0aW5nc1xuIyBodHRwczovL3ZlcmRhY2Npby5vcmcvZG9jcy9jb25maWd1cmF0aW9uI3NlY3VyaXR5XG4jIHNlY3VyaXR5OlxuIyAgIGFwaTpcbiMgICAgIGxlZ2FjeTogdHJ1ZVxuIyAgICAgand0OlxuIyAgICAgICBzaWduOlxuIyAgICAgICAgIGV4cGlyZXNJbjogMjlkXG4jICAgICAgIHZlcmlmeTpcbiMgICAgICAgICBzb21lUHJvcDogW3ZhbHVlXVxuIyAgIHdlYjpcbiMgICAgIHNpZ246XG4jICAgICAgIGV4cGlyZXNJbjogMWggIyAxIGhvdXIgYnkgZGVmYXVsdFxuIyAgICAgdmVyaWZ5OlxuIyAgICAgICBzb21lUHJvcDogW3ZhbHVlXVxuXG4jIGh0dHBzOi8vdmVyZGFjY2lvLm9yZy9kb2NzL2NvbmZpZ3VyYXRpb24jdXNlci1yYXRlLWxpbWl0XG4jIHVzZXJSYXRlTGltaXQ6XG4jICAgd2luZG93TXM6IDUwMDAwXG4jICAgbWF4OiAxMDAwXG5cbiMgaHR0cHM6Ly92ZXJkYWNjaW8ub3JnL2RvY3MvY29uZmlndXJhdGlvbiNtYXgtYm9keS1zaXplXG4jIG1heF9ib2R5X3NpemU6IDEwbWJcblxuIyBodHRwczovL3ZlcmRhY2Npby5vcmcvZG9jcy9jb25maWd1cmF0aW9uI2xpc3Rlbi1wb3J0XG4jIGxpc3RlbjpcbiMgICAtIGxvY2FsaG9zdDo0ODczICAgICAgICAgICAgIyBkZWZhdWx0IHZhbHVlXG4jICAgLSBodHRwOi8vbG9jYWxob3N0OjQ4NzMgICAgICMgc2FtZSB0aGluZ1xuIyAgIC0gMC4wLjAuMDo0ODczICAgICAgICAgICAgICAjIGxpc3RlbiBvbiBhbGwgYWRkcmVzc2VzIChJTkFERFJfQU5ZKVxuIyAgIC0gaHR0cHM6Ly9leGFtcGxlLm9yZzo0ODczICAjIGlmIHlvdSB3YW50IHRvIHVzZSBodHRwc1xuIyAgIC0gXCJbOjoxXTo0ODczXCIgICAgICAgICAgICAgICMgaXB2NlxuIyAgIC0gdW5peDovdG1wL3ZlcmRhY2Npby5zb2NrICAjIHVuaXggc29ja2V0XG5cbiMgVGhlIEhUVFBTIGNvbmZpZ3VyYXRpb24gaXMgdXNlZnVsIGlmIHlvdSBkbyBub3QgY29uc2lkZXIgdXNlIGEgSFRUUCBQcm94eVxuIyBodHRwczovL3ZlcmRhY2Npby5vcmcvZG9jcy9jb25maWd1cmF0aW9uI2h0dHBzXG4jIGh0dHBzOlxuIyAgIGtleTogLi9wYXRoL3ZlcmRhY2Npby1rZXkucGVtXG4jICAgY2VydDogLi9wYXRoL3ZlcmRhY2Npby1jZXJ0LnBlbVxuIyAgIGNhOiAuL3BhdGgvdmVyZGFjY2lvLWNzci5wZW1cblxuIyBodHRwczovL3ZlcmRhY2Npby5vcmcvZG9jcy9jb25maWd1cmF0aW9uI3Byb3h5XG4jIGh0dHBfcHJveHk6IGh0dHA6Ly9zb21ldGhpbmcubG9jYWwvXG4jIGh0dHBzX3Byb3h5OiBodHRwczovL3NvbWV0aGluZy5sb2NhbC9cbiMgbm9fcHJveHk6IGxvY2FsaG9zdCwxMjcuMC4wLjEsc2VydmVyLmxvY2FsXG5cbiMgaHR0cHM6Ly92ZXJkYWNjaW8ub3JnL2RvY3MvY29uZmlndXJhdGlvbiNub3RpZmljYXRpb25zXG4jIG5vdGlmeTpcbiMgICBtZXRob2Q6ICdQT1NUJ1xuIyAgIGhlYWRlcnM6ICdbeyBcIkNvbnRlbnQtVHlwZVwiOiBcImFwcGxpY2F0aW9uL2pzb25cIiB9XSdcbiMgICBlbmRwb2ludDogJ2h0dHBzOi8vdXNhZ2dlLmhpcGNoYXQuY29tL3YyL3Jvb20vMzcyOTQ4NS9ub3RpZmljYXRpb24/YXV0aF90b2tlbj1teVNlY3JldFRva2VuJ1xuIyAgIGNvbnRlbnQ6ICd7XCJjb2xvclwiOlwiZ3JlZW5cIixcIm1lc3NhZ2VcIjpcIk5ldyBwYWNrYWdlIHB1Ymxpc2hlZDogKiB7eyBuYW1lIH19KlwiLFwibm90aWZ5XCI6dHJ1ZSxcIm1lc3NhZ2VfZm9ybWF0XCI6XCJ0ZXh0XCJ9J1xuXG4jIFNldHRpbmdzIGZvciBtaWRkbGV3YXJlIHBsdWdpbnNcbiMgaHR0cHM6Ly92ZXJkYWNjaW8ub3JnL2RvY3MvcGx1Z2lucyNtaWRkbGV3YXJlLWNvbmZpZ3VyYXRpb25cbm1pZGRsZXdhcmVzOlxuICBhdWRpdDpcbiAgICBlbmFibGVkOiB0cnVlXG4gICAgIyB0aW1lb3V0OiAxMDAwMFxuXG4jIExvZyBzZXR0aW5nc1xuIyBodHRwczovL3ZlcmRhY2Npby5vcmcvZG9jcy9sb2dnZXJcbiMgUmVkYWN0aW9uOiBodHRwczovL2dldHBpbm8uaW8vIy9kb2NzL3JlZGFjdGlvblxuIyBTeW5jaHJvbm91cyBsb2dnaW5nOiBodHRwczovL2dldHBpbm8uaW8vIy9kb2NzL2FzeW5jaHJvbm91c1xubG9nOlxuICB0eXBlOiBzdGRvdXRcbiAgZm9ybWF0OiBwcmV0dHlcbiAgbGV2ZWw6IGh0dHBcbiMgIHJlZGFjdDpcbiMgICAgcGF0aHM6IFsncmVxLmhlYWRlci5hdXRob3JpemF0aW9uJywncmVxLmhlYWRlci5jb29raWUnLCdyZXEucmVtb3RlQWRkcmVzcycsJ3JlcS5yZW1vdGVQb3J0JywnaXAnLCdyZW1vdGVJUCcsJ3VzZXInLCdtc2cnXVxuIyAgICBjZW5zb3I6ICc8cmVkYWN0ZWQ+J1xuIyAgc3luYzogdHJ1ZVxuXG4jIEZlYXR1cmUgZmxhZ3MgKGV4cGVyaW1lbnRhbCBzZXR0aW5ncyB0aGF0IGNhbiBiZSBjaGFuZ2VkIG9yIHJlbW92ZWQgaW4gdGhlIGZ1dHVyZSlcbiMgaHR0cHM6Ly92ZXJkYWNjaW8ub3JnL2RvY3MvY29uZmlndXJhdGlvbiNleHBlcmltZW50c1xuIyBleHBlcmltZW50czpcbiMgICMgU3VwcG9ydCBmb3IgbnBtIHRva2VuIGNvbW1hbmRcbiMgIHRva2VuOiBmYWxzZVxuIyAgIyBFbmFibGUgdGFyYmFsbCBVUkwgcmVkaXJlY3QgZm9yIGhvc3RpbmcgdGFyYmFsbCB3aXRoIGEgZGlmZmVyZW50IHNlcnZlci5cbiMgICMgVGhlIHRhcmJhbGxfdXJsX3JlZGlyZWN0IGNhbiBiZSBhIHRlbXBsYXRlIHN0cmluZ1xuIyAgdGFyYmFsbF91cmxfcmVkaXJlY3Q6ICdodHRwczovL215Y2RuLmNvbS92ZXJkYWNjaW8vJHtwYWNrYWdlTmFtZX0vJHtmaWxlbmFtZX0nXG4jICAjIFRoZSB0YXJiYWxsX3VybF9yZWRpcmVjdCBjYW4gYmUgYSBmdW5jdGlvbiwgdGFrZXMgcGFja2FnZU5hbWUgYW5kIGZpbGVuYW1lIGFuZCByZXR1cm5zIHRoZSB1cmwsXG4jICAjIHdoZW4gd29ya2luZyB3aXRoIGEganMgY29uZmlndXJhdGlvbiBmaWxlXG4jICB0YXJiYWxsX3VybF9yZWRpcmVjdChwYWNrYWdlTmFtZSwgZmlsZW5hbWUpIHtcbiMgICAgY29uc3Qgc2lnbmVkVXJsID0gLy8gZ2VuZXJhdGUgYSBzaWduZWQgdXJsXG4jICAgIHJldHVybiBzaWduZWRVcmw7XG4jICB9XG4jIFJlbmFtZWQgZnJvbSBcImV4cGVyaW1lbnRzXCIgdG8gXCJmbGFnc1wiIGluIG5leHQgbWFqb3IgcmVsZWFzZVxuIyBmbGFnczpcbiMgIGNoYW5nZVBhc3N3b3JkOiB0cnVlXG4jICBzZWFyY2hSZW1vdGU6IHRydWVcblxuIyBUcmFuc2xhdGUgeW91ciByZWdpc3RyeSwgQVBJIGFuZCB3ZWIgVUlcbiMgTGlzdCBvZiB0aGUgYXZhaWxhYmxlIHRyYW5zbGF0aW9ucyBodHRwczovL2dpdGh1Yi5jb20vdmVyZGFjY2lvL3ZlcmRhY2Npby9ibG9iL21hc3Rlci9wYWNrYWdlcy9wbHVnaW5zL3VpLXRoZW1lL3NyYy9pMThuL0FCT1VUX1RSQU5TTEFUSU9OUy5tZFxuaTE4bjpcbiAgICB3ZWI6IGVuLVVTXG5cIlwiXCIiCn0=
```

## Links

`node.js`,`package-repository`,`npm`

---

Version:`6`

VaultwardenUnofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs

VikunjaVikunja is a self-hosted, open-source to-do list application to organize tasks, projects, and notes.

### On this page

ConfigurationBase64LinksTags