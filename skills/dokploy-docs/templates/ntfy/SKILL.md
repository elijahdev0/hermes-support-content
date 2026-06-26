---
title: "NTFY | Dokploy"
source: "https://docs.dokploy.com/docs/templates/ntfy"
category: dokploy-docs
created: "2026-06-25T17:21:54.355Z"
---

NTFY | Dokploy

# NTFY

Copy as Markdown

ntfy lets you send push notifications to your phone or desktop via scripts from any computer, using simple HTTP PUT or POST requests.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  ntfy:
    image: binwiederhier/ntfy
    restart: unless-stopped
    command:
      - serve
    ports:
      - "${HTTP_PORT}"
    volumes:
      - ntfy-data:/var/lib/ntfy
      - ntfy-cache:/var/cache/ntfy
      - ../files/server.yml:/etc/ntfy/server.yml:ro
      - ../files/templates:/etc/ntfy/templates:ro
    healthcheck:
      test: ["CMD-SHELL", "wget -q --tries=1 http://localhost:${HTTP_PORT}/v1/health -O - | grep -Eo '\"healthy\"\\s*:\\s*true' || exit 1"]
      interval: 60s
      timeout: 10s
      retries: 3
      start_period: 40s

volumes:
  ntfy-data:
  ntfy-cache:
```

```
[variables]
ntfy_domain = "${domain}"
ntfy_http_port = "80"

[[config.domains]]
serviceName = "ntfy"
host = "${ntfy_domain}"
port = 80
path = "/"

[config.env]
HTTP_PORT = "${ntfy_http_port}"

# This is an example, you'll need to add manually any templates you want to use
# Should be preserved as we use the ../files/templates solution
[[config.mounts]]
filePath = "/templates/myapp.yml"
content = """
title: |
  {{- if eq .status "firing" }}
    {{- if gt .percent 90.0 }}🚨 Critical alert
    {{- else }}⚠️ Alert{{- end }}
  {{- else if eq .status "resolved" }}
  ✅ Alert resolved
  {{- end }}
message: |
  Status: {{ .status }}
  Type: {{ .type | upper }} ({{ .percent }}%)
  Server: {{ .server }}
"""

[[config.mounts]]
filePath = "/server.yml"
content = """
# ntfy server config file
#
# Please refer to the documentation at https://ntfy.sh/docs/config/ for details.
# All options also support underscores (_) instead of dashes (-) to comply with the YAML spec.

# Public facing base URL of the service (e.g. https://ntfy.sh or https://ntfy.example.com)
#
# This setting is required for any of the following features:
# - attachments (to return a download URL)
# - e-mail sending (for the topic URL in the email footer)
# - iOS push notifications for self-hosted servers (to calculate the Firebase poll_request topic)
# - Matrix Push Gateway (to validate that the pushkey is correct)
#
base-url: https://${ntfy_domain}

# Listen address for the HTTP & HTTPS web server. If "listen-https" is set, you must also
# set "key-file" and "cert-file". Format: [<ip>]:<port>, e.g. "1.2.3.4:8080".
#
# To listen on all interfaces, you may omit the IP address, e.g. ":443".
# To disable HTTP, set "listen-http" to "-".
#
listen-http: ":${ntfy_http_port}"
# listen-https: ":443"

# Listen on a Unix socket, e.g. /var/lib/ntfy/ntfy.sock
# This can be useful to avoid port issues on local systems, and to simplify permissions.
#
# listen-unix: <socket-path>
# listen-unix-mode: <linux permissions, e.g. 0700>

# Path to the private key & cert file for the HTTPS web server. Not used if "listen-https" is not set.
#
# key-file: ""
# cert-file: ""

# If set, also publish messages to a Firebase Cloud Messaging (FCM) topic for your app.
# This is optional and only required to save battery when using the Android app.
#
# firebase-key-file: <filename>

# If "cache-file" is set, messages are cached in a local SQLite database instead of only in-memory.
# This allows for service restarts without losing messages in support of the since= parameter.
#
# The "cache-duration" parameter defines the duration for which messages will be buffered
# before they are deleted. This is required to support the "since=..." and "poll=1" parameter.
# To disable the cache entirely (on-disk/in-memory), set "cache-duration" to 0.
# The cache file is created automatically, provided that the correct permissions are set.
#
# The "cache-startup-queries" parameter allows you to run commands when the database is initialized,
# e.g. to enable WAL mode (see https://phiresky.github.io/blog/2020/sqlite-performance-tuning/)).
# Example:
#    cache-startup-queries: |
#       pragma journal_mode = WAL;
#       pragma synchronous = normal;
#       pragma temp_store = memory;
#       pragma busy_timeout = 15000;
#       vacuum;
#
# The "cache-batch-size" and "cache-batch-timeout" parameter allow enabling async batch writing
# of messages. If set, messages will be queued and written to the database in batches of the given
# size, or after the given timeout. This is only required for high volume servers.
#
# Debian/RPM package users:
#   Use /var/cache/ntfy/cache.db as cache file to avoid permission issues. The package
#   creates this folder for you.
#
# Check your permissions:
#   If you are running ntfy with systemd, make sure this cache file is owned by the
#   ntfy user and group by running: chown ntfy.ntfy <filename>.
#
cache-file: /var/cache/ntfy/cache.db
cache-duration: "12h"
# cache-startup-queries:
# cache-batch-size: 0
# cache-batch-timeout: "0ms"

# If set, access to the ntfy server and API can be controlled on a granular level using
# the 'ntfy user' and 'ntfy access' commands. See the --help pages for details, or check the docs.
#
# - auth-file is the SQLite user/access database; it is created automatically if it doesn't already exist
# - auth-default-access defines the default/fallback access if no access control entry is found; it can be
#   set to "read-write" (default), "read-only", "write-only" or "deny-all".
# - auth-startup-queries allows you to run commands when the database is initialized, e.g. to enable
#   WAL mode. This is similar to cache-startup-queries. See above for details.
# - auth-users is a list of users that are automatically created when the server starts.
#   Each entry is in the format "<username>:<password-hash>:<role>", e.g. "phil:$2a$10$YLiO8U21sX1uhZamTLJXHuxgVC0Z/GKISibrKCLohPgtG7yIxSk4C:user"
#   Use 'ntfy user hash' to generate the password hash from a password.
# - auth-access is a list of access control entries that are automatically created when the server starts.
#   Each entry is in the format "<username>:<topic-pattern>:<access>", e.g. "phil:mytopic:rw" or "phil:phil-*:rw".
# - auth-tokens is a list of access tokens that are automatically created when the server starts.
#   Each entry is in the format "<username>:<token>[:<label>]", e.g. "phil:tk_1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef:My token".
#   Use 'ntfy token generate' to generate a new access token.
#
# Debian/RPM package users:
#   Use /var/lib/ntfy/user.db as user database to avoid permission issues. The package
#   creates this folder for you.
#
# Check your permissions:
#   If you are running ntfy with systemd, make sure this user database file is owned by the
#   ntfy user and group by running: chown ntfy.ntfy <filename>.
#
auth-file: /var/lib/ntfy/user.db
auth-default-access: "read-write"
# auth-startup-queries:
auth-users: []
  # - "<username>:<password-hash>:<role>"
auth-access: []
  # - "<username>:<topic-pattern>:<access>"
auth-tokens: []
  # - "<username>:<token>[:<label>]"

# If set, the X-Forwarded-For header (or whatever is configured in proxy-forwarded-header) is used to determine
# the visitor IP address instead of the remote address of the connection.
#
# WARNING: If you are behind a proxy, you must set this, otherwise all visitors are rate-limited
#          as if they are one.
#
# - behind-proxy makes it so that the real visitor IP address is extracted from the header defined in
#   proxy-forwarded-header. Without this, the remote address of the incoming connection is used.
# - proxy-forwarded-header is the header to use to identify visitors. It may be a single IP address (e.g. 1.2.3.4),
#   a comma-separated list of IP addresses (e.g. "1.2.3.4, 5.6.7.8"), or an RFC 7239-style header (e.g. "for=1.2.3.4;by=proxy.example.com, for=5.6.7.8").
# - proxy-trusted-hosts is a comma-separated list of IP addresses, hostnames or CIDRs that are removed from the forwarded header
#   to determine the real IP address. This is only useful if there are multiple proxies involved that add themselves to
#   the forwarded header.
#
behind-proxy: true
# proxy-forwarded-header: "X-Forwarded-For"
# proxy-trusted-hosts:

# If enabled, clients can attach files to notifications as attachments. Minimum settings to enable attachments
# are "attachment-cache-dir" and "base-url".
#
# - attachment-cache-dir is the cache directory for attached files
# - attachment-total-size-limit is the limit of the on-disk attachment cache directory (total size)
# - attachment-file-size-limit is the per-file attachment size limit (e.g. 300k, 2M, 100M)
# - attachment-expiry-duration is the duration after which uploaded attachments will be deleted (e.g. 3h, 20h)
#
# attachment-cache-dir:
# attachment-total-size-limit: "5G"
# attachment-file-size-limit: "15M"
# attachment-expiry-duration: "3h"

# Template directory for message templates.
#
# When "X-Template: <name>" (aliases: "Template: <name>", "Tpl: <name>") or "?template=<name>" is set, transform the message
# based on one of the built-in pre-defined templates, or on a template defined in the "template-dir" directory.
#
# Template files must have the ".yml" extension and must be formatted as YAML. They may contain "title" and "message" keys,
# which are interpreted as Go templates.
#
# Example template file (e.g. /etc/ntfy/templates/grafana.yml):
#   title: |
#     {{- if eq .status "firing" }}
#     {{ .title | default "Alert firing" }}
#     {{- else if eq .status "resolved" }}
#     {{ .title | default "Alert resolved" }}
#     {{- end }}
#   message: |
#     {{ .message | trunc 2000 }}
#
template-dir: "/etc/ntfy/templates"

# If enabled, allow outgoing e-mail notifications via the 'X-Email' header. If this header is set,
# messages will additionally be sent out as e-mail using an external SMTP server.
#
# As of today, only SMTP servers with plain text auth (or no auth at all), and STARTLS are supported.
# Please also refer to the rate limiting settings below (visitor-email-limit-burst & visitor-email-limit-burst).
#
# - smtp-sender-addr is the hostname:port of the SMTP server
# - smtp-sender-from is the e-mail address of the sender
# - smtp-sender-user/smtp-sender-pass are the username and password of the SMTP user (leave blank for no auth)
#
# smtp-sender-addr:
# smtp-sender-from:
# smtp-sender-user:
# smtp-sender-pass:

# If enabled, ntfy will launch a lightweight SMTP server for incoming messages. Once configured, users can send
# emails to a topic e-mail address to publish messages to a topic.
#
# - smtp-server-listen defines the IP address and port the SMTP server will listen on, e.g. :25 or 1.2.3.4:25
# - smtp-server-domain is the e-mail domain, e.g. ntfy.sh
# - smtp-server-addr-prefix is an optional prefix for the e-mail addresses to prevent spam. If set to "ntfy-",
#   for instance, only e-mails to [email protected] will be accepted. If this is not set, all emails to
#   [email protected] will be accepted (which may be a spam problem).
#
# smtp-server-listen:
# smtp-server-domain:
# smtp-server-addr-prefix:

# Web Push support (background notifications for browsers)
#
# If enabled, allows the ntfy web app to receive push notifications, even when the web app is closed. When enabled, users
# can enable background notifications in the web app. Once enabled, ntfy will forward published messages to the push
# endpoint, which will then forward it to the browser.
#
# You must configure web-push-public/private key, web-push-file, and web-push-email-address below to enable Web Push.
# Run "ntfy webpush keys" to generate the keys.
#
# - web-push-public-key is the generated VAPID public key, e.g. AA1234BBCCddvveekaabcdfqwertyuiopasdfghjklzxcvbnm1234567890
# - web-push-private-key is the generated VAPID private key, e.g. AA2BB1234567890abcdefzxcvbnm1234567890
# - web-push-file is a database file to keep track of browser subscription endpoints, e.g. /var/cache/ntfy/webpush.db
# - web-push-email-address is the admin email address send to the push provider, e.g. [email protected]
# - web-push-startup-queries is an optional list of queries to run on startup`
# - web-push-expiry-warning-duration defines the duration after which unused subscriptions are sent a warning (default is 55d`)
# - web-push-expiry-duration defines the duration after which unused subscriptions will expire (default is 60d)
#
# web-push-public-key:
# web-push-private-key:
# web-push-file:
# web-push-email-address:
# web-push-startup-queries:
# web-push-expiry-warning-duration: "55d"
# web-push-expiry-duration: "60d"

# If enabled, ntfy can perform voice calls via Twilio via the "X-Call" header.
#
# - twilio-account is the Twilio account SID, e.g. AC***
# - twilio-auth-token is the Twilio auth token, e.g. af***
# - twilio-phone-number is the outgoing phone number you purchased, e.g. +18***
# - twilio-verify-service is the Twilio Verify service SID, e.g. VA***
#
# twilio-account:
# twilio-auth-token:
# twilio-phone-number:
# twilio-verify-service:

# Interval in which keepalive messages are sent to the client. This is to prevent
# intermediaries closing the connection for inactivity.
#
# Note that the Android app has a hardcoded timeout at 77s, so it should be less than that.
#
# keepalive-interval: "45s"

# Interval in which the manager prunes old messages, deletes topics
# and prints the stats.
#
manager-interval: "12h"

# Defines topic names that are not allowed, because they are otherwise used. There are a few default topics
# that cannot be used (e.g. app, account, settings, ...). To extend the default list, define them here.
#
# Example:
#   disallowed-topics:
#     - about
#     - pricing
#     - contact
#
# disallowed-topics:

# Defines the root path of the web app, or disables the web app entirely.
#
# Can be any simple path, e.g. "/", "/app", or "/ntfy". For backwards-compatibility reasons,
# the values "app" (maps to "/"), "home" (maps to "/app"), or "disable" (maps to "") to disable
# the web app entirely.
#
# web-root: /

# Various feature flags used to control the web app, and API access, mainly around user and
# account management.
#
# - enable-signup allows users to sign up via the web app, or API
# - enable-login allows users to log in via the web app, or API
# - require-login redirects users to the login page if they are not logged in (disallows web app access without login)
# - enable-reservations allows users to reserve topics (if their tier allows it)
#
enable-signup: false
require-login: false
enable-login: true
enable-reservations: false

# Server URL of a Firebase/APNS-connected ntfy server (likely "https://ntfy.sh").
#
# iOS users:
#   If you use the iOS ntfy app, you MUST configure this to receive timely notifications. You'll like want this:
#   upstream-base-url: "https://ntfy.sh"
#
# If set, all incoming messages will publish a "poll_request" message to the configured upstream server, containing
# the message ID of the original message, instructing the iOS app to poll this server for the actual message contents.
# This is to prevent the upstream server and Firebase/APNS from being able to read the message.
#
# - upstream-base-url is the base URL of the upstream server. Should be "https://ntfy.sh".
# - upstream-access-token is the token used to authenticate with the upstream server. This is only required
#   if you exceed the upstream rate limits, or the uptream server requires authentication.
#
upstream-base-url: "https://ntfy.sh"
# upstream-access-token:

# Configures message-specific limits
#
# - message-size-limit defines the max size of a message body. Please note message sizes >4K are NOT RECOMMENDED,
#   and largely untested. If FCM and/or APNS is used, the limit should stay 4K, because their limits are around that size.
#   If you increase this size limit regardless, FCM and APNS will NOT work for large messages.
# - message-delay-limit defines the max delay of a message when using the "Delay" header.
#
# message-size-limit: "4k"
# message-delay-limit: "3d"

# Rate limiting: Total number of topics before the server rejects new topics.
#
# global-topic-limit: 15000

# Rate limiting: Number of subscriptions per visitor (IP address)
#
# visitor-subscription-limit: 30

# Rate limiting: Allowed GET/PUT/POST requests per second, per visitor:
# - visitor-request-limit-burst is the initial bucket of requests each visitor has
# - visitor-request-limit-replenish is the rate at which the bucket is refilled
# - visitor-request-limit-exempt-hosts is a comma-separated list of hostnames, IPs or CIDRs to be
#   exempt from request rate limiting. Hostnames are resolved at the time the server is started.
#   Example: "1.2.3.4,ntfy.example.com,8.7.6.0/24"
#
# visitor-request-limit-burst: 60
# visitor-request-limit-replenish: "5s"
# visitor-request-limit-exempt-hosts: ""

# Rate limiting: Hard daily limit of messages per visitor and day. The limit is reset
# every day at midnight UTC. If the limit is not set (or set to zero), the request
# limit (see above) governs the upper limit.
#
# visitor-message-daily-limit: 0

# Rate limiting: Allowed emails per visitor:
# - visitor-email-limit-burst is the initial bucket of emails each visitor has
# - visitor-email-limit-replenish is the rate at which the bucket is refilled
#
# visitor-email-limit-burst: 16
# visitor-email-limit-replenish: "1h"

# Rate limiting: IPv4/IPv6 address prefix bits used for rate limiting
# - visitor-prefix-bits-ipv4: number of bits of the IPv4 address to use for rate limiting (default: 32, full address)
# - visitor-prefix-bits-ipv6: number of bits of the IPv6 address to use for rate limiting (default: 64, /64 subnet)
#
# This is used to group visitors by their IP address or subnet. For example, if you set visitor-prefix-bits-ipv4 to 24,
# all visitors in the 1.2.3.0/24 network are treated as one.
#
# By default, ntfy uses the full IPv4 address (32 bits) and the /64 subnet of the IPv6 address (64 bits).
#
# visitor-prefix-bits-ipv4: 32
# visitor-prefix-bits-ipv6: 64

# Rate limiting: Attachment size and bandwidth limits per visitor:
# - visitor-attachment-total-size-limit is the total storage limit used for attachments per visitor
# - visitor-attachment-daily-bandwidth-limit is the total daily attachment download/upload traffic limit per visitor
#
# visitor-attachment-total-size-limit: "100M"
# visitor-attachment-daily-bandwidth-limit: "500M"

# Rate limiting: Enable subscriber-based rate limiting (mostly used for UnifiedPush)
#
# If subscriber-based rate limiting is enabled, messages published on UnifiedPush topics** (topics starting with "up")
# will be counted towards the "rate visitor" of the topic. A "rate visitor" is the first subscriber to the topic.
#
# Once enabled, a client subscribing to UnifiedPush topics via HTTP stream, or websockets, will be automatically registered as
# a "rate visitor", i.e. the visitor whose rate limits will be used when publishing on this topic. Note that setting the rate visitor
# requires **read-write permission** on the topic.
#
# If this setting is enabled, publishing to UnifiedPush topics will lead to a HTTP 507 response if
# no "rate visitor" has been previously registered. This is to avoid burning the publisher's "visitor-message-daily-limit".
#
# visitor-subscriber-rate-limiting: false

# Payments integration via Stripe
#
# - stripe-secret-key is the key used for the Stripe API communication. Setting this values
#   enables payments in the ntfy web app (e.g. Upgrade dialog). See https://dashboard.stripe.com/apikeys.
# - stripe-webhook-key is the key required to validate the authenticity of incoming webhooks from Stripe.
#   Webhooks are essential up keep the local database in sync with the payment provider. See https://dashboard.stripe.com/webhooks.
# - billing-contact is an email address or website displayed in the "Upgrade tier" dialog to let people reach
#   out with billing questions. If unset, nothing will be displayed.
#
# stripe-secret-key:
# stripe-webhook-key:
# billing-contact:

# Metrics
#
# ntfy can expose Prometheus-style metrics via a /metrics endpoint, or on a dedicated listen IP/port.
# Metrics may be considered sensitive information, so before you enable them, be sure you know what you are
# doing, and/or secure access to the endpoint in your reverse proxy.
#
# - enable-metrics enables the /metrics endpoint for the default ntfy server (i.e. HTTP, HTTPS and/or Unix socket)
# - metrics-listen-http exposes the metrics endpoint via a dedicated [IP]:port. If set, this option implicitly
#   enables metrics as well, e.g. "10.0.1.1:9090" or ":9090"
#
# enable-metrics: false
# metrics-listen-http: ":9090"

# Profiling
#
# ntfy can expose Go's net/http/pprof endpoints to support profiling of the ntfy server. If enabled, ntfy will listen
# on a dedicated listen IP/port, which can be accessed via the web browser on http://<ip>:<port>/debug/pprof/.
# This can be helpful to expose bottlenecks, and visualize call flows. See https://pkg.go.dev/net/http/pprof for details.
#
# profile-listen-http:

# Logging options
#
# By default, ntfy logs to the console (stderr), with an "info" log level, and in a human-readable text format.
# ntfy supports five different log levels, can also write to a file, log as JSON, and even supports granular
# log level overrides for easier debugging. Some options (log-level and log-level-overrides) can be hot reloaded
# by calling "kill -HUP $pid" or "systemctl reload ntfy".
#
# - log-format defines the output format, can be "text" (default) or "json"
# - log-file is a filename to write logs to. If this is not set, ntfy logs to stderr.
# - log-level defines the default log level, can be one of "trace", "debug", "info" (default), "warn" or "error".
#   Be aware that "debug" (and particularly "trace") can be VERY CHATTY. Only turn them on briefly for debugging purposes.
# - log-level-overrides lets you override the log level if certain fields match. This is incredibly powerful
#   for debugging certain parts of the system (e.g. only the account management, or only a certain visitor).
#   This is an array of strings in the format:
#      - "field=value -> level" to match a value exactly, e.g. "tag=manager -> trace"
#      - "field -> level" to match any value, e.g. "time_taken_ms -> debug"
#   Warning: Using log-level-overrides has a performance penalty. Only use it for temporary debugging.
#
# Check your permissions:
#   If you are running ntfy with systemd, make sure this log file is owned by the
#   ntfy user and group by running: chown ntfy.ntfy <filename>.
#
# Example (good for production):
#   log-level: info
#   log-format: json
#   log-file: /var/log/ntfy.log
#
# Example level overrides (for debugging, only use temporarily):
#   log-level-overrides:
#      - "tag=manager -> trace"
#      - "visitor_ip=1.2.3.4 -> debug"
#      - "time_taken_ms -> debug"
#
# log-level: info
# log-level-overrides:
# log-format: text
# log-file:
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBudGZ5OlxuICAgIGltYWdlOiBiaW53aWVkZXJoaWVyL250ZnlcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGNvbW1hbmQ6XG4gICAgICAtIHNlcnZlXG4gICAgcG9ydHM6XG4gICAgICAtIFwiJHtIVFRQX1BPUlR9XCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBudGZ5LWRhdGE6L3Zhci9saWIvbnRmeVxuICAgICAgLSBudGZ5LWNhY2hlOi92YXIvY2FjaGUvbnRmeVxuICAgICAgLSAuLi9maWxlcy9zZXJ2ZXIueW1sOi9ldGMvbnRmeS9zZXJ2ZXIueW1sOnJvXG4gICAgICAtIC4uL2ZpbGVzL3RlbXBsYXRlczovZXRjL250ZnkvdGVtcGxhdGVzOnJvXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJ3Z2V0IC1xIC0tdHJpZXM9MSBodHRwOi8vbG9jYWxob3N0OiR7SFRUUF9QT1JUfS92MS9oZWFsdGggLU8gLSB8IGdyZXAgLUVvICdcXFwiaGVhbHRoeVxcXCJcXFxccyo6XFxcXHMqdHJ1ZScgfHwgZXhpdCAxXCJdXG4gICAgICBpbnRlcnZhbDogNjBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDNcbiAgICAgIHN0YXJ0X3BlcmlvZDogNDBzXG5cbnZvbHVtZXM6XG4gIG50ZnktZGF0YTpcbiAgbnRmeS1jYWNoZTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubnRmeV9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5udGZ5X2h0dHBfcG9ydCA9IFwiODBcIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJudGZ5XCJcbmhvc3QgPSBcIiR7bnRmeV9kb21haW59XCJcbnBvcnQgPSA4MFxucGF0aCA9IFwiL1wiXG5cbltjb25maWcuZW52XVxuSFRUUF9QT1JUID0gXCIke250ZnlfaHR0cF9wb3J0fVwiXG5cbiMgVGhpcyBpcyBhbiBleGFtcGxlLCB5b3UnbGwgbmVlZCB0byBhZGQgbWFudWFsbHkgYW55IHRlbXBsYXRlcyB5b3Ugd2FudCB0byB1c2VcbiPCoFNob3VsZCBiZSBwcmVzZXJ2ZWQgYXMgd2UgdXNlIHRoZSAuLi9maWxlcy90ZW1wbGF0ZXMgc29sdXRpb25cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL3RlbXBsYXRlcy9teWFwcC55bWxcIlxuY29udGVudCA9IFwiXCJcIlxudGl0bGU6IHxcbiAge3stIGlmIGVxIC5zdGF0dXMgXCJmaXJpbmdcIiB9fVxuICAgIHt7LSBpZiBndCAucGVyY2VudCA5MC4wIH198J+aqCBDcml0aWNhbCBhbGVydFxuICAgIHt7LSBlbHNlIH194pqg77iPIEFsZXJ0e3stIGVuZCB9fVxuICB7ey0gZWxzZSBpZiBlcSAuc3RhdHVzIFwicmVzb2x2ZWRcIiB9fVxuICDinIUgQWxlcnQgcmVzb2x2ZWRcbiAge3stIGVuZCB9fVxubWVzc2FnZTogfFxuICBTdGF0dXM6IHt7IC5zdGF0dXMgfX1cbiAgVHlwZToge3sgLnR5cGUgfCB1cHBlciB9fSAoe3sgLnBlcmNlbnQgfX0lKVxuICBTZXJ2ZXI6IHt7IC5zZXJ2ZXIgfX1cblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi9zZXJ2ZXIueW1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMgbnRmeSBzZXJ2ZXIgY29uZmlnIGZpbGVcbiNcbiMgUGxlYXNlIHJlZmVyIHRvIHRoZSBkb2N1bWVudGF0aW9uIGF0IGh0dHBzOi8vbnRmeS5zaC9kb2NzL2NvbmZpZy8gZm9yIGRldGFpbHMuXG4jIEFsbCBvcHRpb25zIGFsc28gc3VwcG9ydCB1bmRlcnNjb3JlcyAoXykgaW5zdGVhZCBvZiBkYXNoZXMgKC0pIHRvIGNvbXBseSB3aXRoIHRoZSBZQU1MIHNwZWMuXG5cbiMgUHVibGljIGZhY2luZyBiYXNlIFVSTCBvZiB0aGUgc2VydmljZSAoZS5nLiBodHRwczovL250Znkuc2ggb3IgaHR0cHM6Ly9udGZ5LmV4YW1wbGUuY29tKVxuI1xuIyBUaGlzIHNldHRpbmcgaXMgcmVxdWlyZWQgZm9yIGFueSBvZiB0aGUgZm9sbG93aW5nIGZlYXR1cmVzOlxuIyAtIGF0dGFjaG1lbnRzICh0byByZXR1cm4gYSBkb3dubG9hZCBVUkwpXG4jIC0gZS1tYWlsIHNlbmRpbmcgKGZvciB0aGUgdG9waWMgVVJMIGluIHRoZSBlbWFpbCBmb290ZXIpXG4jIC0gaU9TIHB1c2ggbm90aWZpY2F0aW9ucyBmb3Igc2VsZi1ob3N0ZWQgc2VydmVycyAodG8gY2FsY3VsYXRlIHRoZSBGaXJlYmFzZSBwb2xsX3JlcXVlc3QgdG9waWMpXG4jIC0gTWF0cml4IFB1c2ggR2F0ZXdheSAodG8gdmFsaWRhdGUgdGhhdCB0aGUgcHVzaGtleSBpcyBjb3JyZWN0KVxuI1xuYmFzZS11cmw6IGh0dHBzOi8vJHtudGZ5X2RvbWFpbn1cblxuIyBMaXN0ZW4gYWRkcmVzcyBmb3IgdGhlIEhUVFAgJiBIVFRQUyB3ZWIgc2VydmVyLiBJZiBcImxpc3Rlbi1odHRwc1wiIGlzIHNldCwgeW91IG11c3QgYWxzb1xuIyBzZXQgXCJrZXktZmlsZVwiIGFuZCBcImNlcnQtZmlsZVwiLiBGb3JtYXQ6IFs8aXA+XTo8cG9ydD4sIGUuZy4gXCIxLjIuMy40OjgwODBcIi5cbiNcbiMgVG8gbGlzdGVuIG9uIGFsbCBpbnRlcmZhY2VzLCB5b3UgbWF5IG9taXQgdGhlIElQIGFkZHJlc3MsIGUuZy4gXCI6NDQzXCIuXG4jIFRvIGRpc2FibGUgSFRUUCwgc2V0IFwibGlzdGVuLWh0dHBcIiB0byBcIi1cIi5cbiNcbmxpc3Rlbi1odHRwOiBcIjoke250ZnlfaHR0cF9wb3J0fVwiXG4jIGxpc3Rlbi1odHRwczogXCI6NDQzXCJcblxuIyBMaXN0ZW4gb24gYSBVbml4IHNvY2tldCwgZS5nLiAvdmFyL2xpYi9udGZ5L250Znkuc29ja1xuIyBUaGlzIGNhbiBiZSB1c2VmdWwgdG8gYXZvaWQgcG9ydCBpc3N1ZXMgb24gbG9jYWwgc3lzdGVtcywgYW5kIHRvIHNpbXBsaWZ5IHBlcm1pc3Npb25zLlxuI1xuIyBsaXN0ZW4tdW5peDogPHNvY2tldC1wYXRoPlxuIyBsaXN0ZW4tdW5peC1tb2RlOiA8bGludXggcGVybWlzc2lvbnMsIGUuZy4gMDcwMD5cblxuIyBQYXRoIHRvIHRoZSBwcml2YXRlIGtleSAmIGNlcnQgZmlsZSBmb3IgdGhlIEhUVFBTIHdlYiBzZXJ2ZXIuIE5vdCB1c2VkIGlmIFwibGlzdGVuLWh0dHBzXCIgaXMgbm90IHNldC5cbiNcbiMga2V5LWZpbGU6IFwiXCJcbiMgY2VydC1maWxlOiBcIlwiXG5cbiMgSWYgc2V0LCBhbHNvIHB1Ymxpc2ggbWVzc2FnZXMgdG8gYSBGaXJlYmFzZSBDbG91ZCBNZXNzYWdpbmcgKEZDTSkgdG9waWMgZm9yIHlvdXIgYXBwLlxuIyBUaGlzIGlzIG9wdGlvbmFsIGFuZCBvbmx5IHJlcXVpcmVkIHRvIHNhdmUgYmF0dGVyeSB3aGVuIHVzaW5nIHRoZSBBbmRyb2lkIGFwcC5cbiNcbiMgZmlyZWJhc2Uta2V5LWZpbGU6IDxmaWxlbmFtZT5cblxuIyBJZiBcImNhY2hlLWZpbGVcIiBpcyBzZXQsIG1lc3NhZ2VzIGFyZSBjYWNoZWQgaW4gYSBsb2NhbCBTUUxpdGUgZGF0YWJhc2UgaW5zdGVhZCBvZiBvbmx5IGluLW1lbW9yeS5cbiMgVGhpcyBhbGxvd3MgZm9yIHNlcnZpY2UgcmVzdGFydHMgd2l0aG91dCBsb3NpbmcgbWVzc2FnZXMgaW4gc3VwcG9ydCBvZiB0aGUgc2luY2U9IHBhcmFtZXRlci5cbiNcbiMgVGhlIFwiY2FjaGUtZHVyYXRpb25cIiBwYXJhbWV0ZXIgZGVmaW5lcyB0aGUgZHVyYXRpb24gZm9yIHdoaWNoIG1lc3NhZ2VzIHdpbGwgYmUgYnVmZmVyZWRcbiMgYmVmb3JlIHRoZXkgYXJlIGRlbGV0ZWQuIFRoaXMgaXMgcmVxdWlyZWQgdG8gc3VwcG9ydCB0aGUgXCJzaW5jZT0uLi5cIiBhbmQgXCJwb2xsPTFcIiBwYXJhbWV0ZXIuXG4jIFRvIGRpc2FibGUgdGhlIGNhY2hlIGVudGlyZWx5IChvbi1kaXNrL2luLW1lbW9yeSksIHNldCBcImNhY2hlLWR1cmF0aW9uXCIgdG8gMC5cbiMgVGhlIGNhY2hlIGZpbGUgaXMgY3JlYXRlZCBhdXRvbWF0aWNhbGx5LCBwcm92aWRlZCB0aGF0IHRoZSBjb3JyZWN0IHBlcm1pc3Npb25zIGFyZSBzZXQuXG4jXG4jIFRoZSBcImNhY2hlLXN0YXJ0dXAtcXVlcmllc1wiIHBhcmFtZXRlciBhbGxvd3MgeW91IHRvIHJ1biBjb21tYW5kcyB3aGVuIHRoZSBkYXRhYmFzZSBpcyBpbml0aWFsaXplZCxcbiMgZS5nLiB0byBlbmFibGUgV0FMIG1vZGUgKHNlZSBodHRwczovL3BoaXJlc2t5LmdpdGh1Yi5pby9ibG9nLzIwMjAvc3FsaXRlLXBlcmZvcm1hbmNlLXR1bmluZy8pKS5cbiMgRXhhbXBsZTpcbiMgICAgY2FjaGUtc3RhcnR1cC1xdWVyaWVzOiB8XG4jICAgICAgIHByYWdtYSBqb3VybmFsX21vZGUgPSBXQUw7XG4jICAgICAgIHByYWdtYSBzeW5jaHJvbm91cyA9IG5vcm1hbDtcbiMgICAgICAgcHJhZ21hIHRlbXBfc3RvcmUgPSBtZW1vcnk7XG4jICAgICAgIHByYWdtYSBidXN5X3RpbWVvdXQgPSAxNTAwMDtcbiMgICAgICAgdmFjdXVtO1xuI1xuIyBUaGUgXCJjYWNoZS1iYXRjaC1zaXplXCIgYW5kIFwiY2FjaGUtYmF0Y2gtdGltZW91dFwiIHBhcmFtZXRlciBhbGxvdyBlbmFibGluZyBhc3luYyBiYXRjaCB3cml0aW5nXG4jIG9mIG1lc3NhZ2VzLiBJZiBzZXQsIG1lc3NhZ2VzIHdpbGwgYmUgcXVldWVkIGFuZCB3cml0dGVuIHRvIHRoZSBkYXRhYmFzZSBpbiBiYXRjaGVzIG9mIHRoZSBnaXZlblxuIyBzaXplLCBvciBhZnRlciB0aGUgZ2l2ZW4gdGltZW91dC4gVGhpcyBpcyBvbmx5IHJlcXVpcmVkIGZvciBoaWdoIHZvbHVtZSBzZXJ2ZXJzLlxuI1xuIyBEZWJpYW4vUlBNIHBhY2thZ2UgdXNlcnM6XG4jICAgVXNlIC92YXIvY2FjaGUvbnRmeS9jYWNoZS5kYiBhcyBjYWNoZSBmaWxlIHRvIGF2b2lkIHBlcm1pc3Npb24gaXNzdWVzLiBUaGUgcGFja2FnZVxuIyAgIGNyZWF0ZXMgdGhpcyBmb2xkZXIgZm9yIHlvdS5cbiNcbiMgQ2hlY2sgeW91ciBwZXJtaXNzaW9uczpcbiMgICBJZiB5b3UgYXJlIHJ1bm5pbmcgbnRmeSB3aXRoIHN5c3RlbWQsIG1ha2Ugc3VyZSB0aGlzIGNhY2hlIGZpbGUgaXMgb3duZWQgYnkgdGhlXG4jICAgbnRmeSB1c2VyIGFuZCBncm91cCBieSBydW5uaW5nOiBjaG93biBudGZ5Lm50ZnkgPGZpbGVuYW1lPi5cbiNcbmNhY2hlLWZpbGU6IC92YXIvY2FjaGUvbnRmeS9jYWNoZS5kYlxuY2FjaGUtZHVyYXRpb246IFwiMTJoXCJcbiMgY2FjaGUtc3RhcnR1cC1xdWVyaWVzOlxuIyBjYWNoZS1iYXRjaC1zaXplOiAwXG4jIGNhY2hlLWJhdGNoLXRpbWVvdXQ6IFwiMG1zXCJcblxuIyBJZiBzZXQsIGFjY2VzcyB0byB0aGUgbnRmeSBzZXJ2ZXIgYW5kIEFQSSBjYW4gYmUgY29udHJvbGxlZCBvbiBhIGdyYW51bGFyIGxldmVsIHVzaW5nXG4jIHRoZSAnbnRmeSB1c2VyJyBhbmQgJ250ZnkgYWNjZXNzJyBjb21tYW5kcy4gU2VlIHRoZSAtLWhlbHAgcGFnZXMgZm9yIGRldGFpbHMsIG9yIGNoZWNrIHRoZSBkb2NzLlxuI1xuIyAtIGF1dGgtZmlsZSBpcyB0aGUgU1FMaXRlIHVzZXIvYWNjZXNzIGRhdGFiYXNlOyBpdCBpcyBjcmVhdGVkIGF1dG9tYXRpY2FsbHkgaWYgaXQgZG9lc24ndCBhbHJlYWR5IGV4aXN0XG4jIC0gYXV0aC1kZWZhdWx0LWFjY2VzcyBkZWZpbmVzIHRoZSBkZWZhdWx0L2ZhbGxiYWNrIGFjY2VzcyBpZiBubyBhY2Nlc3MgY29udHJvbCBlbnRyeSBpcyBmb3VuZDsgaXQgY2FuIGJlXG4jICAgc2V0IHRvIFwicmVhZC13cml0ZVwiIChkZWZhdWx0KSwgXCJyZWFkLW9ubHlcIiwgXCJ3cml0ZS1vbmx5XCIgb3IgXCJkZW55LWFsbFwiLlxuIyAtIGF1dGgtc3RhcnR1cC1xdWVyaWVzIGFsbG93cyB5b3UgdG8gcnVuIGNvbW1hbmRzIHdoZW4gdGhlIGRhdGFiYXNlIGlzIGluaXRpYWxpemVkLCBlLmcuIHRvIGVuYWJsZVxuIyAgIFdBTCBtb2RlLiBUaGlzIGlzIHNpbWlsYXIgdG8gY2FjaGUtc3RhcnR1cC1xdWVyaWVzLiBTZWUgYWJvdmUgZm9yIGRldGFpbHMuXG4jIC0gYXV0aC11c2VycyBpcyBhIGxpc3Qgb2YgdXNlcnMgdGhhdCBhcmUgYXV0b21hdGljYWxseSBjcmVhdGVkIHdoZW4gdGhlIHNlcnZlciBzdGFydHMuXG4jICAgRWFjaCBlbnRyeSBpcyBpbiB0aGUgZm9ybWF0IFwiPHVzZXJuYW1lPjo8cGFzc3dvcmQtaGFzaD46PHJvbGU+XCIsIGUuZy4gXCJwaGlsOiQyYSQxMCRZTGlPOFUyMXNYMXVoWmFtVExKWEh1eGdWQzBaL0dLSVNpYnJLQ0xvaFBndEc3eUl4U2s0Qzp1c2VyXCJcbiMgICBVc2UgJ250ZnkgdXNlciBoYXNoJyB0byBnZW5lcmF0ZSB0aGUgcGFzc3dvcmQgaGFzaCBmcm9tIGEgcGFzc3dvcmQuXG4jIC0gYXV0aC1hY2Nlc3MgaXMgYSBsaXN0IG9mIGFjY2VzcyBjb250cm9sIGVudHJpZXMgdGhhdCBhcmUgYXV0b21hdGljYWxseSBjcmVhdGVkIHdoZW4gdGhlIHNlcnZlciBzdGFydHMuXG4jICAgRWFjaCBlbnRyeSBpcyBpbiB0aGUgZm9ybWF0IFwiPHVzZXJuYW1lPjo8dG9waWMtcGF0dGVybj46PGFjY2Vzcz5cIiwgZS5nLiBcInBoaWw6bXl0b3BpYzpyd1wiIG9yIFwicGhpbDpwaGlsLSo6cndcIi5cbiMgLSBhdXRoLXRva2VucyBpcyBhIGxpc3Qgb2YgYWNjZXNzIHRva2VucyB0aGF0IGFyZSBhdXRvbWF0aWNhbGx5IGNyZWF0ZWQgd2hlbiB0aGUgc2VydmVyIHN0YXJ0cy5cbiMgICBFYWNoIGVudHJ5IGlzIGluIHRoZSBmb3JtYXQgXCI8dXNlcm5hbWU+Ojx0b2tlbj5bOjxsYWJlbD5dXCIsIGUuZy4gXCJwaGlsOnRrXzEyMzQ1Njc4OTBhYmNkZWYxMjM0NTY3ODkwYWJjZGVmMTIzNDU2Nzg5MGFiY2RlZjEyMzQ1Njc4OTBhYmNkZWY6TXkgdG9rZW5cIi5cbiMgICBVc2UgJ250ZnkgdG9rZW4gZ2VuZXJhdGUnIHRvIGdlbmVyYXRlIGEgbmV3IGFjY2VzcyB0b2tlbi5cbiNcbiMgRGViaWFuL1JQTSBwYWNrYWdlIHVzZXJzOlxuIyAgIFVzZSAvdmFyL2xpYi9udGZ5L3VzZXIuZGIgYXMgdXNlciBkYXRhYmFzZSB0byBhdm9pZCBwZXJtaXNzaW9uIGlzc3Vlcy4gVGhlIHBhY2thZ2VcbiMgICBjcmVhdGVzIHRoaXMgZm9sZGVyIGZvciB5b3UuXG4jXG4jIENoZWNrIHlvdXIgcGVybWlzc2lvbnM6XG4jICAgSWYgeW91IGFyZSBydW5uaW5nIG50Znkgd2l0aCBzeXN0ZW1kLCBtYWtlIHN1cmUgdGhpcyB1c2VyIGRhdGFiYXNlIGZpbGUgaXMgb3duZWQgYnkgdGhlXG4jICAgbnRmeSB1c2VyIGFuZCBncm91cCBieSBydW5uaW5nOiBjaG93biBudGZ5Lm50ZnkgPGZpbGVuYW1lPi5cbiNcbmF1dGgtZmlsZTogL3Zhci9saWIvbnRmeS91c2VyLmRiXG5hdXRoLWRlZmF1bHQtYWNjZXNzOiBcInJlYWQtd3JpdGVcIlxuIyBhdXRoLXN0YXJ0dXAtcXVlcmllczpcbmF1dGgtdXNlcnM6IFtdXG4gICMgLSBcIjx1c2VybmFtZT46PHBhc3N3b3JkLWhhc2g+Ojxyb2xlPlwiXG5hdXRoLWFjY2VzczogW11cbiAgIyAtIFwiPHVzZXJuYW1lPjo8dG9waWMtcGF0dGVybj46PGFjY2Vzcz5cIlxuYXV0aC10b2tlbnM6IFtdXG4gICMgLSBcIjx1c2VybmFtZT46PHRva2VuPls6PGxhYmVsPl1cIlxuXG4jIElmIHNldCwgdGhlIFgtRm9yd2FyZGVkLUZvciBoZWFkZXIgKG9yIHdoYXRldmVyIGlzIGNvbmZpZ3VyZWQgaW4gcHJveHktZm9yd2FyZGVkLWhlYWRlcikgaXMgdXNlZCB0byBkZXRlcm1pbmVcbiMgdGhlIHZpc2l0b3IgSVAgYWRkcmVzcyBpbnN0ZWFkIG9mIHRoZSByZW1vdGUgYWRkcmVzcyBvZiB0aGUgY29ubmVjdGlvbi5cbiNcbiMgV0FSTklORzogSWYgeW91IGFyZSBiZWhpbmQgYSBwcm94eSwgeW91IG11c3Qgc2V0IHRoaXMsIG90aGVyd2lzZSBhbGwgdmlzaXRvcnMgYXJlIHJhdGUtbGltaXRlZFxuIyAgICAgICAgICBhcyBpZiB0aGV5IGFyZSBvbmUuXG4jXG4jIC0gYmVoaW5kLXByb3h5IG1ha2VzIGl0IHNvIHRoYXQgdGhlIHJlYWwgdmlzaXRvciBJUCBhZGRyZXNzIGlzIGV4dHJhY3RlZCBmcm9tIHRoZSBoZWFkZXIgZGVmaW5lZCBpblxuIyAgIHByb3h5LWZvcndhcmRlZC1oZWFkZXIuIFdpdGhvdXQgdGhpcywgdGhlIHJlbW90ZSBhZGRyZXNzIG9mIHRoZSBpbmNvbWluZyBjb25uZWN0aW9uIGlzIHVzZWQuXG4jIC0gcHJveHktZm9yd2FyZGVkLWhlYWRlciBpcyB0aGUgaGVhZGVyIHRvIHVzZSB0byBpZGVudGlmeSB2aXNpdG9ycy4gSXQgbWF5IGJlIGEgc2luZ2xlIElQIGFkZHJlc3MgKGUuZy4gMS4yLjMuNCksXG4jICAgYSBjb21tYS1zZXBhcmF0ZWQgbGlzdCBvZiBJUCBhZGRyZXNzZXMgKGUuZy4gXCIxLjIuMy40LCA1LjYuNy44XCIpLCBvciBhbiBSRkMgNzIzOS1zdHlsZSBoZWFkZXIgKGUuZy4gXCJmb3I9MS4yLjMuNDtieT1wcm94eS5leGFtcGxlLmNvbSwgZm9yPTUuNi43LjhcIikuXG4jIC0gcHJveHktdHJ1c3RlZC1ob3N0cyBpcyBhIGNvbW1hLXNlcGFyYXRlZCBsaXN0IG9mIElQIGFkZHJlc3NlcywgaG9zdG5hbWVzIG9yIENJRFJzIHRoYXQgYXJlIHJlbW92ZWQgZnJvbSB0aGUgZm9yd2FyZGVkIGhlYWRlclxuIyAgIHRvIGRldGVybWluZSB0aGUgcmVhbCBJUCBhZGRyZXNzLiBUaGlzIGlzIG9ubHkgdXNlZnVsIGlmIHRoZXJlIGFyZSBtdWx0aXBsZSBwcm94aWVzIGludm9sdmVkIHRoYXQgYWRkIHRoZW1zZWx2ZXMgdG9cbiMgICB0aGUgZm9yd2FyZGVkIGhlYWRlci5cbiNcbmJlaGluZC1wcm94eTogdHJ1ZVxuIyBwcm94eS1mb3J3YXJkZWQtaGVhZGVyOiBcIlgtRm9yd2FyZGVkLUZvclwiXG4jIHByb3h5LXRydXN0ZWQtaG9zdHM6XG5cbiMgSWYgZW5hYmxlZCwgY2xpZW50cyBjYW4gYXR0YWNoIGZpbGVzIHRvIG5vdGlmaWNhdGlvbnMgYXMgYXR0YWNobWVudHMuIE1pbmltdW0gc2V0dGluZ3MgdG8gZW5hYmxlIGF0dGFjaG1lbnRzXG4jIGFyZSBcImF0dGFjaG1lbnQtY2FjaGUtZGlyXCIgYW5kIFwiYmFzZS11cmxcIi5cbiNcbiMgLSBhdHRhY2htZW50LWNhY2hlLWRpciBpcyB0aGUgY2FjaGUgZGlyZWN0b3J5IGZvciBhdHRhY2hlZCBmaWxlc1xuIyAtIGF0dGFjaG1lbnQtdG90YWwtc2l6ZS1saW1pdCBpcyB0aGUgbGltaXQgb2YgdGhlIG9uLWRpc2sgYXR0YWNobWVudCBjYWNoZSBkaXJlY3RvcnkgKHRvdGFsIHNpemUpXG4jIC0gYXR0YWNobWVudC1maWxlLXNpemUtbGltaXQgaXMgdGhlIHBlci1maWxlIGF0dGFjaG1lbnQgc2l6ZSBsaW1pdCAoZS5nLiAzMDBrLCAyTSwgMTAwTSlcbiMgLSBhdHRhY2htZW50LWV4cGlyeS1kdXJhdGlvbiBpcyB0aGUgZHVyYXRpb24gYWZ0ZXIgd2hpY2ggdXBsb2FkZWQgYXR0YWNobWVudHMgd2lsbCBiZSBkZWxldGVkIChlLmcuIDNoLCAyMGgpXG4jXG4jIGF0dGFjaG1lbnQtY2FjaGUtZGlyOlxuIyBhdHRhY2htZW50LXRvdGFsLXNpemUtbGltaXQ6IFwiNUdcIlxuIyBhdHRhY2htZW50LWZpbGUtc2l6ZS1saW1pdDogXCIxNU1cIlxuIyBhdHRhY2htZW50LWV4cGlyeS1kdXJhdGlvbjogXCIzaFwiXG5cbiMgVGVtcGxhdGUgZGlyZWN0b3J5IGZvciBtZXNzYWdlIHRlbXBsYXRlcy5cbiNcbiMgV2hlbiBcIlgtVGVtcGxhdGU6IDxuYW1lPlwiIChhbGlhc2VzOiBcIlRlbXBsYXRlOiA8bmFtZT5cIiwgXCJUcGw6IDxuYW1lPlwiKSBvciBcIj90ZW1wbGF0ZT08bmFtZT5cIiBpcyBzZXQsIHRyYW5zZm9ybSB0aGUgbWVzc2FnZVxuIyBiYXNlZCBvbiBvbmUgb2YgdGhlIGJ1aWx0LWluIHByZS1kZWZpbmVkIHRlbXBsYXRlcywgb3Igb24gYSB0ZW1wbGF0ZSBkZWZpbmVkIGluIHRoZSBcInRlbXBsYXRlLWRpclwiIGRpcmVjdG9yeS5cbiNcbiMgVGVtcGxhdGUgZmlsZXMgbXVzdCBoYXZlIHRoZSBcIi55bWxcIiBleHRlbnNpb24gYW5kIG11c3QgYmUgZm9ybWF0dGVkIGFzIFlBTUwuIFRoZXkgbWF5IGNvbnRhaW4gXCJ0aXRsZVwiIGFuZCBcIm1lc3NhZ2VcIiBrZXlzLFxuIyB3aGljaCBhcmUgaW50ZXJwcmV0ZWQgYXMgR28gdGVtcGxhdGVzLlxuI1xuIyBFeGFtcGxlIHRlbXBsYXRlIGZpbGUgKGUuZy4gL2V0Yy9udGZ5L3RlbXBsYXRlcy9ncmFmYW5hLnltbCk6XG4jICAgdGl0bGU6IHxcbiMgICAgIHt7LSBpZiBlcSAuc3RhdHVzIFwiZmlyaW5nXCIgfX1cbiMgICAgIHt7IC50aXRsZSB8IGRlZmF1bHQgXCJBbGVydCBmaXJpbmdcIiB9fVxuIyAgICAge3stIGVsc2UgaWYgZXEgLnN0YXR1cyBcInJlc29sdmVkXCIgfX1cbiMgICAgIHt7IC50aXRsZSB8IGRlZmF1bHQgXCJBbGVydCByZXNvbHZlZFwiIH19XG4jICAgICB7ey0gZW5kIH19XG4jICAgbWVzc2FnZTogfFxuIyAgICAge3sgLm1lc3NhZ2UgfCB0cnVuYyAyMDAwIH19XG4jXG50ZW1wbGF0ZS1kaXI6IFwiL2V0Yy9udGZ5L3RlbXBsYXRlc1wiXG5cbiMgSWYgZW5hYmxlZCwgYWxsb3cgb3V0Z29pbmcgZS1tYWlsIG5vdGlmaWNhdGlvbnMgdmlhIHRoZSAnWC1FbWFpbCcgaGVhZGVyLiBJZiB0aGlzIGhlYWRlciBpcyBzZXQsXG4jIG1lc3NhZ2VzIHdpbGwgYWRkaXRpb25hbGx5IGJlIHNlbnQgb3V0IGFzIGUtbWFpbCB1c2luZyBhbiBleHRlcm5hbCBTTVRQIHNlcnZlci5cbiNcbiMgQXMgb2YgdG9kYXksIG9ubHkgU01UUCBzZXJ2ZXJzIHdpdGggcGxhaW4gdGV4dCBhdXRoIChvciBubyBhdXRoIGF0IGFsbCksIGFuZCBTVEFSVExTIGFyZSBzdXBwb3J0ZWQuXG4jIFBsZWFzZSBhbHNvIHJlZmVyIHRvIHRoZSByYXRlIGxpbWl0aW5nIHNldHRpbmdzIGJlbG93ICh2aXNpdG9yLWVtYWlsLWxpbWl0LWJ1cnN0ICYgdmlzaXRvci1lbWFpbC1saW1pdC1idXJzdCkuXG4jXG4jIC0gc210cC1zZW5kZXItYWRkciBpcyB0aGUgaG9zdG5hbWU6cG9ydCBvZiB0aGUgU01UUCBzZXJ2ZXJcbiMgLSBzbXRwLXNlbmRlci1mcm9tIGlzIHRoZSBlLW1haWwgYWRkcmVzcyBvZiB0aGUgc2VuZGVyXG4jIC0gc210cC1zZW5kZXItdXNlci9zbXRwLXNlbmRlci1wYXNzIGFyZSB0aGUgdXNlcm5hbWUgYW5kIHBhc3N3b3JkIG9mIHRoZSBTTVRQIHVzZXIgKGxlYXZlIGJsYW5rIGZvciBubyBhdXRoKVxuI1xuIyBzbXRwLXNlbmRlci1hZGRyOlxuIyBzbXRwLXNlbmRlci1mcm9tOlxuIyBzbXRwLXNlbmRlci11c2VyOlxuIyBzbXRwLXNlbmRlci1wYXNzOlxuXG4jIElmIGVuYWJsZWQsIG50Znkgd2lsbCBsYXVuY2ggYSBsaWdodHdlaWdodCBTTVRQIHNlcnZlciBmb3IgaW5jb21pbmcgbWVzc2FnZXMuIE9uY2UgY29uZmlndXJlZCwgdXNlcnMgY2FuIHNlbmRcbiMgZW1haWxzIHRvIGEgdG9waWMgZS1tYWlsIGFkZHJlc3MgdG8gcHVibGlzaCBtZXNzYWdlcyB0byBhIHRvcGljLlxuI1xuIyAtIHNtdHAtc2VydmVyLWxpc3RlbiBkZWZpbmVzIHRoZSBJUCBhZGRyZXNzIGFuZCBwb3J0IHRoZSBTTVRQIHNlcnZlciB3aWxsIGxpc3RlbiBvbiwgZS5nLiA6MjUgb3IgMS4yLjMuNDoyNVxuIyAtIHNtdHAtc2VydmVyLWRvbWFpbiBpcyB0aGUgZS1tYWlsIGRvbWFpbiwgZS5nLiBudGZ5LnNoXG4jIC0gc210cC1zZXJ2ZXItYWRkci1wcmVmaXggaXMgYW4gb3B0aW9uYWwgcHJlZml4IGZvciB0aGUgZS1tYWlsIGFkZHJlc3NlcyB0byBwcmV2ZW50IHNwYW0uIElmIHNldCB0byBcIm50ZnktXCIsXG4jICAgZm9yIGluc3RhbmNlLCBvbmx5IGUtbWFpbHMgdG8gbnRmeS0kdG9waWNAbnRmeS5zaCB3aWxsIGJlIGFjY2VwdGVkLiBJZiB0aGlzIGlzIG5vdCBzZXQsIGFsbCBlbWFpbHMgdG9cbiMgICAkdG9waWNAbnRmeS5zaCB3aWxsIGJlIGFjY2VwdGVkICh3aGljaCBtYXkgYmUgYSBzcGFtIHByb2JsZW0pLlxuI1xuIyBzbXRwLXNlcnZlci1saXN0ZW46XG4jIHNtdHAtc2VydmVyLWRvbWFpbjpcbiMgc210cC1zZXJ2ZXItYWRkci1wcmVmaXg6XG5cbiMgV2ViIFB1c2ggc3VwcG9ydCAoYmFja2dyb3VuZCBub3RpZmljYXRpb25zIGZvciBicm93c2VycylcbiNcbiMgSWYgZW5hYmxlZCwgYWxsb3dzIHRoZSBudGZ5IHdlYiBhcHAgdG8gcmVjZWl2ZSBwdXNoIG5vdGlmaWNhdGlvbnMsIGV2ZW4gd2hlbiB0aGUgd2ViIGFwcCBpcyBjbG9zZWQuIFdoZW4gZW5hYmxlZCwgdXNlcnNcbiMgY2FuIGVuYWJsZSBiYWNrZ3JvdW5kIG5vdGlmaWNhdGlvbnMgaW4gdGhlIHdlYiBhcHAuIE9uY2UgZW5hYmxlZCwgbnRmeSB3aWxsIGZvcndhcmQgcHVibGlzaGVkIG1lc3NhZ2VzIHRvIHRoZSBwdXNoXG4jIGVuZHBvaW50LCB3aGljaCB3aWxsIHRoZW4gZm9yd2FyZCBpdCB0byB0aGUgYnJvd3Nlci5cbiNcbiMgWW91IG11c3QgY29uZmlndXJlIHdlYi1wdXNoLXB1YmxpYy9wcml2YXRlIGtleSwgd2ViLXB1c2gtZmlsZSwgYW5kIHdlYi1wdXNoLWVtYWlsLWFkZHJlc3MgYmVsb3cgdG8gZW5hYmxlIFdlYiBQdXNoLlxuIyBSdW4gXCJudGZ5IHdlYnB1c2gga2V5c1wiIHRvIGdlbmVyYXRlIHRoZSBrZXlzLlxuI1xuIyAtIHdlYi1wdXNoLXB1YmxpYy1rZXkgaXMgdGhlIGdlbmVyYXRlZCBWQVBJRCBwdWJsaWMga2V5LCBlLmcuIEFBMTIzNEJCQ0NkZHZ2ZWVrYWFiY2RmcXdlcnR5dWlvcGFzZGZnaGprbHp4Y3Zibm0xMjM0NTY3ODkwXG4jIC0gd2ViLXB1c2gtcHJpdmF0ZS1rZXkgaXMgdGhlIGdlbmVyYXRlZCBWQVBJRCBwcml2YXRlIGtleSwgZS5nLiBBQTJCQjEyMzQ1Njc4OTBhYmNkZWZ6eGN2Ym5tMTIzNDU2Nzg5MFxuIyAtIHdlYi1wdXNoLWZpbGUgaXMgYSBkYXRhYmFzZSBmaWxlIHRvIGtlZXAgdHJhY2sgb2YgYnJvd3NlciBzdWJzY3JpcHRpb24gZW5kcG9pbnRzLCBlLmcuIC92YXIvY2FjaGUvbnRmeS93ZWJwdXNoLmRiXG4jIC0gd2ViLXB1c2gtZW1haWwtYWRkcmVzcyBpcyB0aGUgYWRtaW4gZW1haWwgYWRkcmVzcyBzZW5kIHRvIHRoZSBwdXNoIHByb3ZpZGVyLCBlLmcuIHN5c2FkbWluQGV4YW1wbGUuY29tXG4jIC0gd2ViLXB1c2gtc3RhcnR1cC1xdWVyaWVzIGlzIGFuIG9wdGlvbmFsIGxpc3Qgb2YgcXVlcmllcyB0byBydW4gb24gc3RhcnR1cGBcbiMgLSB3ZWItcHVzaC1leHBpcnktd2FybmluZy1kdXJhdGlvbiBkZWZpbmVzIHRoZSBkdXJhdGlvbiBhZnRlciB3aGljaCB1bnVzZWQgc3Vic2NyaXB0aW9ucyBhcmUgc2VudCBhIHdhcm5pbmcgKGRlZmF1bHQgaXMgNTVkYClcbiMgLSB3ZWItcHVzaC1leHBpcnktZHVyYXRpb24gZGVmaW5lcyB0aGUgZHVyYXRpb24gYWZ0ZXIgd2hpY2ggdW51c2VkIHN1YnNjcmlwdGlvbnMgd2lsbCBleHBpcmUgKGRlZmF1bHQgaXMgNjBkKVxuI1xuIyB3ZWItcHVzaC1wdWJsaWMta2V5OlxuIyB3ZWItcHVzaC1wcml2YXRlLWtleTpcbiMgd2ViLXB1c2gtZmlsZTpcbiMgd2ViLXB1c2gtZW1haWwtYWRkcmVzczpcbiMgd2ViLXB1c2gtc3RhcnR1cC1xdWVyaWVzOlxuIyB3ZWItcHVzaC1leHBpcnktd2FybmluZy1kdXJhdGlvbjogXCI1NWRcIlxuIyB3ZWItcHVzaC1leHBpcnktZHVyYXRpb246IFwiNjBkXCJcblxuIyBJZiBlbmFibGVkLCBudGZ5IGNhbiBwZXJmb3JtIHZvaWNlIGNhbGxzIHZpYSBUd2lsaW8gdmlhIHRoZSBcIlgtQ2FsbFwiIGhlYWRlci5cbiNcbiMgLSB0d2lsaW8tYWNjb3VudCBpcyB0aGUgVHdpbGlvIGFjY291bnQgU0lELCBlLmcuIEFDKioqXG4jIC0gdHdpbGlvLWF1dGgtdG9rZW4gaXMgdGhlIFR3aWxpbyBhdXRoIHRva2VuLCBlLmcuIGFmKioqXG4jIC0gdHdpbGlvLXBob25lLW51bWJlciBpcyB0aGUgb3V0Z29pbmcgcGhvbmUgbnVtYmVyIHlvdSBwdXJjaGFzZWQsIGUuZy4gKzE4KioqXG4jIC0gdHdpbGlvLXZlcmlmeS1zZXJ2aWNlIGlzIHRoZSBUd2lsaW8gVmVyaWZ5IHNlcnZpY2UgU0lELCBlLmcuIFZBKioqXG4jXG4jIHR3aWxpby1hY2NvdW50OlxuIyB0d2lsaW8tYXV0aC10b2tlbjpcbiMgdHdpbGlvLXBob25lLW51bWJlcjpcbiMgdHdpbGlvLXZlcmlmeS1zZXJ2aWNlOlxuXG4jIEludGVydmFsIGluIHdoaWNoIGtlZXBhbGl2ZSBtZXNzYWdlcyBhcmUgc2VudCB0byB0aGUgY2xpZW50LiBUaGlzIGlzIHRvIHByZXZlbnRcbiMgaW50ZXJtZWRpYXJpZXMgY2xvc2luZyB0aGUgY29ubmVjdGlvbiBmb3IgaW5hY3Rpdml0eS5cbiNcbiMgTm90ZSB0aGF0IHRoZSBBbmRyb2lkIGFwcCBoYXMgYSBoYXJkY29kZWQgdGltZW91dCBhdCA3N3MsIHNvIGl0IHNob3VsZCBiZSBsZXNzIHRoYW4gdGhhdC5cbiNcbiMga2VlcGFsaXZlLWludGVydmFsOiBcIjQ1c1wiXG5cbiMgSW50ZXJ2YWwgaW4gd2hpY2ggdGhlIG1hbmFnZXIgcHJ1bmVzIG9sZCBtZXNzYWdlcywgZGVsZXRlcyB0b3BpY3NcbiMgYW5kIHByaW50cyB0aGUgc3RhdHMuXG4jXG5tYW5hZ2VyLWludGVydmFsOiBcIjEyaFwiXG5cbiMgRGVmaW5lcyB0b3BpYyBuYW1lcyB0aGF0IGFyZSBub3QgYWxsb3dlZCwgYmVjYXVzZSB0aGV5IGFyZSBvdGhlcndpc2UgdXNlZC4gVGhlcmUgYXJlIGEgZmV3IGRlZmF1bHQgdG9waWNzXG4jIHRoYXQgY2Fubm90IGJlIHVzZWQgKGUuZy4gYXBwLCBhY2NvdW50LCBzZXR0aW5ncywgLi4uKS4gVG8gZXh0ZW5kIHRoZSBkZWZhdWx0IGxpc3QsIGRlZmluZSB0aGVtIGhlcmUuXG4jXG4jIEV4YW1wbGU6XG4jICAgZGlzYWxsb3dlZC10b3BpY3M6XG4jICAgICAtIGFib3V0XG4jICAgICAtIHByaWNpbmdcbiMgICAgIC0gY29udGFjdFxuI1xuIyBkaXNhbGxvd2VkLXRvcGljczpcblxuIyBEZWZpbmVzIHRoZSByb290IHBhdGggb2YgdGhlIHdlYiBhcHAsIG9yIGRpc2FibGVzIHRoZSB3ZWIgYXBwIGVudGlyZWx5LlxuI1xuIyBDYW4gYmUgYW55IHNpbXBsZSBwYXRoLCBlLmcuIFwiL1wiLCBcIi9hcHBcIiwgb3IgXCIvbnRmeVwiLiBGb3IgYmFja3dhcmRzLWNvbXBhdGliaWxpdHkgcmVhc29ucyxcbiMgdGhlIHZhbHVlcyBcImFwcFwiIChtYXBzIHRvIFwiL1wiKSwgXCJob21lXCIgKG1hcHMgdG8gXCIvYXBwXCIpLCBvciBcImRpc2FibGVcIiAobWFwcyB0byBcIlwiKSB0byBkaXNhYmxlXG4jIHRoZSB3ZWIgYXBwIGVudGlyZWx5LlxuI1xuIyB3ZWItcm9vdDogL1xuXG4jIFZhcmlvdXMgZmVhdHVyZSBmbGFncyB1c2VkIHRvIGNvbnRyb2wgdGhlIHdlYiBhcHAsIGFuZCBBUEkgYWNjZXNzLCBtYWlubHkgYXJvdW5kIHVzZXIgYW5kXG4jIGFjY291bnQgbWFuYWdlbWVudC5cbiNcbiMgLSBlbmFibGUtc2lnbnVwIGFsbG93cyB1c2VycyB0byBzaWduIHVwIHZpYSB0aGUgd2ViIGFwcCwgb3IgQVBJXG4jIC0gZW5hYmxlLWxvZ2luIGFsbG93cyB1c2VycyB0byBsb2cgaW4gdmlhIHRoZSB3ZWIgYXBwLCBvciBBUElcbiMgLSByZXF1aXJlLWxvZ2luIHJlZGlyZWN0cyB1c2VycyB0byB0aGUgbG9naW4gcGFnZSBpZiB0aGV5IGFyZSBub3QgbG9nZ2VkIGluIChkaXNhbGxvd3Mgd2ViIGFwcCBhY2Nlc3Mgd2l0aG91dCBsb2dpbilcbiMgLSBlbmFibGUtcmVzZXJ2YXRpb25zIGFsbG93cyB1c2VycyB0byByZXNlcnZlIHRvcGljcyAoaWYgdGhlaXIgdGllciBhbGxvd3MgaXQpXG4jXG5lbmFibGUtc2lnbnVwOiBmYWxzZVxucmVxdWlyZS1sb2dpbjogZmFsc2VcbmVuYWJsZS1sb2dpbjogdHJ1ZVxuZW5hYmxlLXJlc2VydmF0aW9uczogZmFsc2VcblxuIyBTZXJ2ZXIgVVJMIG9mIGEgRmlyZWJhc2UvQVBOUy1jb25uZWN0ZWQgbnRmeSBzZXJ2ZXIgKGxpa2VseSBcImh0dHBzOi8vbnRmeS5zaFwiKS5cbiNcbiMgaU9TIHVzZXJzOlxuIyAgIElmIHlvdSB1c2UgdGhlIGlPUyBudGZ5IGFwcCwgeW91IE1VU1QgY29uZmlndXJlIHRoaXMgdG8gcmVjZWl2ZSB0aW1lbHkgbm90aWZpY2F0aW9ucy4gWW91J2xsIGxpa2Ugd2FudCB0aGlzOlxuIyAgIHVwc3RyZWFtLWJhc2UtdXJsOiBcImh0dHBzOi8vbnRmeS5zaFwiXG4jXG4jIElmIHNldCwgYWxsIGluY29taW5nIG1lc3NhZ2VzIHdpbGwgcHVibGlzaCBhIFwicG9sbF9yZXF1ZXN0XCIgbWVzc2FnZSB0byB0aGUgY29uZmlndXJlZCB1cHN0cmVhbSBzZXJ2ZXIsIGNvbnRhaW5pbmdcbiMgdGhlIG1lc3NhZ2UgSUQgb2YgdGhlIG9yaWdpbmFsIG1lc3NhZ2UsIGluc3RydWN0aW5nIHRoZSBpT1MgYXBwIHRvIHBvbGwgdGhpcyBzZXJ2ZXIgZm9yIHRoZSBhY3R1YWwgbWVzc2FnZSBjb250ZW50cy5cbiMgVGhpcyBpcyB0byBwcmV2ZW50IHRoZSB1cHN0cmVhbSBzZXJ2ZXIgYW5kIEZpcmViYXNlL0FQTlMgZnJvbSBiZWluZyBhYmxlIHRvIHJlYWQgdGhlIG1lc3NhZ2UuXG4jXG4jIC0gdXBzdHJlYW0tYmFzZS11cmwgaXMgdGhlIGJhc2UgVVJMIG9mIHRoZSB1cHN0cmVhbSBzZXJ2ZXIuIFNob3VsZCBiZSBcImh0dHBzOi8vbnRmeS5zaFwiLlxuIyAtIHVwc3RyZWFtLWFjY2Vzcy10b2tlbiBpcyB0aGUgdG9rZW4gdXNlZCB0byBhdXRoZW50aWNhdGUgd2l0aCB0aGUgdXBzdHJlYW0gc2VydmVyLiBUaGlzIGlzIG9ubHkgcmVxdWlyZWRcbiMgICBpZiB5b3UgZXhjZWVkIHRoZSB1cHN0cmVhbSByYXRlIGxpbWl0cywgb3IgdGhlIHVwdHJlYW0gc2VydmVyIHJlcXVpcmVzIGF1dGhlbnRpY2F0aW9uLlxuI1xudXBzdHJlYW0tYmFzZS11cmw6IFwiaHR0cHM6Ly9udGZ5LnNoXCJcbiMgdXBzdHJlYW0tYWNjZXNzLXRva2VuOlxuXG4jIENvbmZpZ3VyZXMgbWVzc2FnZS1zcGVjaWZpYyBsaW1pdHNcbiNcbiMgLSBtZXNzYWdlLXNpemUtbGltaXQgZGVmaW5lcyB0aGUgbWF4IHNpemUgb2YgYSBtZXNzYWdlIGJvZHkuIFBsZWFzZSBub3RlIG1lc3NhZ2Ugc2l6ZXMgPjRLIGFyZSBOT1QgUkVDT01NRU5ERUQsXG4jICAgYW5kIGxhcmdlbHkgdW50ZXN0ZWQuIElmIEZDTSBhbmQvb3IgQVBOUyBpcyB1c2VkLCB0aGUgbGltaXQgc2hvdWxkIHN0YXkgNEssIGJlY2F1c2UgdGhlaXIgbGltaXRzIGFyZSBhcm91bmQgdGhhdCBzaXplLlxuIyAgIElmIHlvdSBpbmNyZWFzZSB0aGlzIHNpemUgbGltaXQgcmVnYXJkbGVzcywgRkNNIGFuZCBBUE5TIHdpbGwgTk9UIHdvcmsgZm9yIGxhcmdlIG1lc3NhZ2VzLlxuIyAtIG1lc3NhZ2UtZGVsYXktbGltaXQgZGVmaW5lcyB0aGUgbWF4IGRlbGF5IG9mIGEgbWVzc2FnZSB3aGVuIHVzaW5nIHRoZSBcIkRlbGF5XCIgaGVhZGVyLlxuI1xuIyBtZXNzYWdlLXNpemUtbGltaXQ6IFwiNGtcIlxuIyBtZXNzYWdlLWRlbGF5LWxpbWl0OiBcIjNkXCJcblxuIyBSYXRlIGxpbWl0aW5nOiBUb3RhbCBudW1iZXIgb2YgdG9waWNzIGJlZm9yZSB0aGUgc2VydmVyIHJlamVjdHMgbmV3IHRvcGljcy5cbiNcbiMgZ2xvYmFsLXRvcGljLWxpbWl0OiAxNTAwMFxuXG4jIFJhdGUgbGltaXRpbmc6IE51bWJlciBvZiBzdWJzY3JpcHRpb25zIHBlciB2aXNpdG9yIChJUCBhZGRyZXNzKVxuI1xuIyB2aXNpdG9yLXN1YnNjcmlwdGlvbi1saW1pdDogMzBcblxuIyBSYXRlIGxpbWl0aW5nOiBBbGxvd2VkIEdFVC9QVVQvUE9TVCByZXF1ZXN0cyBwZXIgc2Vjb25kLCBwZXIgdmlzaXRvcjpcbiMgLSB2aXNpdG9yLXJlcXVlc3QtbGltaXQtYnVyc3QgaXMgdGhlIGluaXRpYWwgYnVja2V0IG9mIHJlcXVlc3RzIGVhY2ggdmlzaXRvciBoYXNcbiMgLSB2aXNpdG9yLXJlcXVlc3QtbGltaXQtcmVwbGVuaXNoIGlzIHRoZSByYXRlIGF0IHdoaWNoIHRoZSBidWNrZXQgaXMgcmVmaWxsZWRcbiMgLSB2aXNpdG9yLXJlcXVlc3QtbGltaXQtZXhlbXB0LWhvc3RzIGlzIGEgY29tbWEtc2VwYXJhdGVkIGxpc3Qgb2YgaG9zdG5hbWVzLCBJUHMgb3IgQ0lEUnMgdG8gYmVcbiMgICBleGVtcHQgZnJvbSByZXF1ZXN0IHJhdGUgbGltaXRpbmcuIEhvc3RuYW1lcyBhcmUgcmVzb2x2ZWQgYXQgdGhlIHRpbWUgdGhlIHNlcnZlciBpcyBzdGFydGVkLlxuIyAgIEV4YW1wbGU6IFwiMS4yLjMuNCxudGZ5LmV4YW1wbGUuY29tLDguNy42LjAvMjRcIlxuI1xuIyB2aXNpdG9yLXJlcXVlc3QtbGltaXQtYnVyc3Q6IDYwXG4jIHZpc2l0b3ItcmVxdWVzdC1saW1pdC1yZXBsZW5pc2g6IFwiNXNcIlxuIyB2aXNpdG9yLXJlcXVlc3QtbGltaXQtZXhlbXB0LWhvc3RzOiBcIlwiXG5cbiMgUmF0ZSBsaW1pdGluZzogSGFyZCBkYWlseSBsaW1pdCBvZiBtZXNzYWdlcyBwZXIgdmlzaXRvciBhbmQgZGF5LiBUaGUgbGltaXQgaXMgcmVzZXRcbiMgZXZlcnkgZGF5IGF0IG1pZG5pZ2h0IFVUQy4gSWYgdGhlIGxpbWl0IGlzIG5vdCBzZXQgKG9yIHNldCB0byB6ZXJvKSwgdGhlIHJlcXVlc3RcbiMgbGltaXQgKHNlZSBhYm92ZSkgZ292ZXJucyB0aGUgdXBwZXIgbGltaXQuXG4jXG4jIHZpc2l0b3ItbWVzc2FnZS1kYWlseS1saW1pdDogMFxuXG4jIFJhdGUgbGltaXRpbmc6IEFsbG93ZWQgZW1haWxzIHBlciB2aXNpdG9yOlxuIyAtIHZpc2l0b3ItZW1haWwtbGltaXQtYnVyc3QgaXMgdGhlIGluaXRpYWwgYnVja2V0IG9mIGVtYWlscyBlYWNoIHZpc2l0b3IgaGFzXG4jIC0gdmlzaXRvci1lbWFpbC1saW1pdC1yZXBsZW5pc2ggaXMgdGhlIHJhdGUgYXQgd2hpY2ggdGhlIGJ1Y2tldCBpcyByZWZpbGxlZFxuI1xuIyB2aXNpdG9yLWVtYWlsLWxpbWl0LWJ1cnN0OiAxNlxuIyB2aXNpdG9yLWVtYWlsLWxpbWl0LXJlcGxlbmlzaDogXCIxaFwiXG5cbiMgUmF0ZSBsaW1pdGluZzogSVB2NC9JUHY2IGFkZHJlc3MgcHJlZml4IGJpdHMgdXNlZCBmb3IgcmF0ZSBsaW1pdGluZ1xuIyAtIHZpc2l0b3ItcHJlZml4LWJpdHMtaXB2NDogbnVtYmVyIG9mIGJpdHMgb2YgdGhlIElQdjQgYWRkcmVzcyB0byB1c2UgZm9yIHJhdGUgbGltaXRpbmcgKGRlZmF1bHQ6IDMyLCBmdWxsIGFkZHJlc3MpXG4jIC0gdmlzaXRvci1wcmVmaXgtYml0cy1pcHY2OiBudW1iZXIgb2YgYml0cyBvZiB0aGUgSVB2NiBhZGRyZXNzIHRvIHVzZSBmb3IgcmF0ZSBsaW1pdGluZyAoZGVmYXVsdDogNjQsIC82NCBzdWJuZXQpXG4jXG4jIFRoaXMgaXMgdXNlZCB0byBncm91cCB2aXNpdG9ycyBieSB0aGVpciBJUCBhZGRyZXNzIG9yIHN1Ym5ldC4gRm9yIGV4YW1wbGUsIGlmIHlvdSBzZXQgdmlzaXRvci1wcmVmaXgtYml0cy1pcHY0IHRvIDI0LFxuIyBhbGwgdmlzaXRvcnMgaW4gdGhlIDEuMi4zLjAvMjQgbmV0d29yayBhcmUgdHJlYXRlZCBhcyBvbmUuXG4jXG4jIEJ5IGRlZmF1bHQsIG50ZnkgdXNlcyB0aGUgZnVsbCBJUHY0IGFkZHJlc3MgKDMyIGJpdHMpIGFuZCB0aGUgLzY0IHN1Ym5ldCBvZiB0aGUgSVB2NiBhZGRyZXNzICg2NCBiaXRzKS5cbiNcbiMgdmlzaXRvci1wcmVmaXgtYml0cy1pcHY0OiAzMlxuIyB2aXNpdG9yLXByZWZpeC1iaXRzLWlwdjY6IDY0XG5cbiMgUmF0ZSBsaW1pdGluZzogQXR0YWNobWVudCBzaXplIGFuZCBiYW5kd2lkdGggbGltaXRzIHBlciB2aXNpdG9yOlxuIyAtIHZpc2l0b3ItYXR0YWNobWVudC10b3RhbC1zaXplLWxpbWl0IGlzIHRoZSB0b3RhbCBzdG9yYWdlIGxpbWl0IHVzZWQgZm9yIGF0dGFjaG1lbnRzIHBlciB2aXNpdG9yXG4jIC0gdmlzaXRvci1hdHRhY2htZW50LWRhaWx5LWJhbmR3aWR0aC1saW1pdCBpcyB0aGUgdG90YWwgZGFpbHkgYXR0YWNobWVudCBkb3dubG9hZC91cGxvYWQgdHJhZmZpYyBsaW1pdCBwZXIgdmlzaXRvclxuI1xuIyB2aXNpdG9yLWF0dGFjaG1lbnQtdG90YWwtc2l6ZS1saW1pdDogXCIxMDBNXCJcbiMgdmlzaXRvci1hdHRhY2htZW50LWRhaWx5LWJhbmR3aWR0aC1saW1pdDogXCI1MDBNXCJcblxuIyBSYXRlIGxpbWl0aW5nOiBFbmFibGUgc3Vic2NyaWJlci1iYXNlZCByYXRlIGxpbWl0aW5nIChtb3N0bHkgdXNlZCBmb3IgVW5pZmllZFB1c2gpXG4jXG4jIElmIHN1YnNjcmliZXItYmFzZWQgcmF0ZSBsaW1pdGluZyBpcyBlbmFibGVkLCBtZXNzYWdlcyBwdWJsaXNoZWQgb24gVW5pZmllZFB1c2ggdG9waWNzKiogKHRvcGljcyBzdGFydGluZyB3aXRoIFwidXBcIilcbiMgd2lsbCBiZSBjb3VudGVkIHRvd2FyZHMgdGhlIFwicmF0ZSB2aXNpdG9yXCIgb2YgdGhlIHRvcGljLiBBIFwicmF0ZSB2aXNpdG9yXCIgaXMgdGhlIGZpcnN0IHN1YnNjcmliZXIgdG8gdGhlIHRvcGljLlxuI1xuIyBPbmNlIGVuYWJsZWQsIGEgY2xpZW50IHN1YnNjcmliaW5nIHRvIFVuaWZpZWRQdXNoIHRvcGljcyB2aWEgSFRUUCBzdHJlYW0sIG9yIHdlYnNvY2tldHMsIHdpbGwgYmUgYXV0b21hdGljYWxseSByZWdpc3RlcmVkIGFzXG4jIGEgXCJyYXRlIHZpc2l0b3JcIiwgaS5lLiB0aGUgdmlzaXRvciB3aG9zZSByYXRlIGxpbWl0cyB3aWxsIGJlIHVzZWQgd2hlbiBwdWJsaXNoaW5nIG9uIHRoaXMgdG9waWMuIE5vdGUgdGhhdCBzZXR0aW5nIHRoZSByYXRlIHZpc2l0b3JcbiMgcmVxdWlyZXMgKipyZWFkLXdyaXRlIHBlcm1pc3Npb24qKiBvbiB0aGUgdG9waWMuXG4jXG4jIElmIHRoaXMgc2V0dGluZyBpcyBlbmFibGVkLCBwdWJsaXNoaW5nIHRvIFVuaWZpZWRQdXNoIHRvcGljcyB3aWxsIGxlYWQgdG8gYSBIVFRQIDUwNyByZXNwb25zZSBpZlxuIyBubyBcInJhdGUgdmlzaXRvclwiIGhhcyBiZWVuIHByZXZpb3VzbHkgcmVnaXN0ZXJlZC4gVGhpcyBpcyB0byBhdm9pZCBidXJuaW5nIHRoZSBwdWJsaXNoZXIncyBcInZpc2l0b3ItbWVzc2FnZS1kYWlseS1saW1pdFwiLlxuI1xuIyB2aXNpdG9yLXN1YnNjcmliZXItcmF0ZS1saW1pdGluZzogZmFsc2VcblxuIyBQYXltZW50cyBpbnRlZ3JhdGlvbiB2aWEgU3RyaXBlXG4jXG4jIC0gc3RyaXBlLXNlY3JldC1rZXkgaXMgdGhlIGtleSB1c2VkIGZvciB0aGUgU3RyaXBlIEFQSSBjb21tdW5pY2F0aW9uLiBTZXR0aW5nIHRoaXMgdmFsdWVzXG4jICAgZW5hYmxlcyBwYXltZW50cyBpbiB0aGUgbnRmeSB3ZWIgYXBwIChlLmcuIFVwZ3JhZGUgZGlhbG9nKS4gU2VlIGh0dHBzOi8vZGFzaGJvYXJkLnN0cmlwZS5jb20vYXBpa2V5cy5cbiMgLSBzdHJpcGUtd2ViaG9vay1rZXkgaXMgdGhlIGtleSByZXF1aXJlZCB0byB2YWxpZGF0ZSB0aGUgYXV0aGVudGljaXR5IG9mIGluY29taW5nIHdlYmhvb2tzIGZyb20gU3RyaXBlLlxuIyAgIFdlYmhvb2tzIGFyZSBlc3NlbnRpYWwgdXAga2VlcCB0aGUgbG9jYWwgZGF0YWJhc2UgaW4gc3luYyB3aXRoIHRoZSBwYXltZW50IHByb3ZpZGVyLiBTZWUgaHR0cHM6Ly9kYXNoYm9hcmQuc3RyaXBlLmNvbS93ZWJob29rcy5cbiMgLSBiaWxsaW5nLWNvbnRhY3QgaXMgYW4gZW1haWwgYWRkcmVzcyBvciB3ZWJzaXRlIGRpc3BsYXllZCBpbiB0aGUgXCJVcGdyYWRlIHRpZXJcIiBkaWFsb2cgdG8gbGV0IHBlb3BsZSByZWFjaFxuIyAgIG91dCB3aXRoIGJpbGxpbmcgcXVlc3Rpb25zLiBJZiB1bnNldCwgbm90aGluZyB3aWxsIGJlIGRpc3BsYXllZC5cbiNcbiMgc3RyaXBlLXNlY3JldC1rZXk6XG4jIHN0cmlwZS13ZWJob29rLWtleTpcbiMgYmlsbGluZy1jb250YWN0OlxuXG4jIE1ldHJpY3NcbiNcbiMgbnRmeSBjYW4gZXhwb3NlIFByb21ldGhldXMtc3R5bGUgbWV0cmljcyB2aWEgYSAvbWV0cmljcyBlbmRwb2ludCwgb3Igb24gYSBkZWRpY2F0ZWQgbGlzdGVuIElQL3BvcnQuXG4jIE1ldHJpY3MgbWF5IGJlIGNvbnNpZGVyZWQgc2Vuc2l0aXZlIGluZm9ybWF0aW9uLCBzbyBiZWZvcmUgeW91IGVuYWJsZSB0aGVtLCBiZSBzdXJlIHlvdSBrbm93IHdoYXQgeW91IGFyZVxuIyBkb2luZywgYW5kL29yIHNlY3VyZSBhY2Nlc3MgdG8gdGhlIGVuZHBvaW50IGluIHlvdXIgcmV2ZXJzZSBwcm94eS5cbiNcbiMgLSBlbmFibGUtbWV0cmljcyBlbmFibGVzIHRoZSAvbWV0cmljcyBlbmRwb2ludCBmb3IgdGhlIGRlZmF1bHQgbnRmeSBzZXJ2ZXIgKGkuZS4gSFRUUCwgSFRUUFMgYW5kL29yIFVuaXggc29ja2V0KVxuIyAtIG1ldHJpY3MtbGlzdGVuLWh0dHAgZXhwb3NlcyB0aGUgbWV0cmljcyBlbmRwb2ludCB2aWEgYSBkZWRpY2F0ZWQgW0lQXTpwb3J0LiBJZiBzZXQsIHRoaXMgb3B0aW9uIGltcGxpY2l0bHlcbiMgICBlbmFibGVzIG1ldHJpY3MgYXMgd2VsbCwgZS5nLiBcIjEwLjAuMS4xOjkwOTBcIiBvciBcIjo5MDkwXCJcbiNcbiMgZW5hYmxlLW1ldHJpY3M6IGZhbHNlXG4jIG1ldHJpY3MtbGlzdGVuLWh0dHA6IFwiOjkwOTBcIlxuXG4jIFByb2ZpbGluZ1xuI1xuIyBudGZ5IGNhbiBleHBvc2UgR28ncyBuZXQvaHR0cC9wcHJvZiBlbmRwb2ludHMgdG8gc3VwcG9ydCBwcm9maWxpbmcgb2YgdGhlIG50Znkgc2VydmVyLiBJZiBlbmFibGVkLCBudGZ5IHdpbGwgbGlzdGVuXG4jIG9uIGEgZGVkaWNhdGVkIGxpc3RlbiBJUC9wb3J0LCB3aGljaCBjYW4gYmUgYWNjZXNzZWQgdmlhIHRoZSB3ZWIgYnJvd3NlciBvbiBodHRwOi8vPGlwPjo8cG9ydD4vZGVidWcvcHByb2YvLlxuIyBUaGlzIGNhbiBiZSBoZWxwZnVsIHRvIGV4cG9zZSBib3R0bGVuZWNrcywgYW5kIHZpc3VhbGl6ZSBjYWxsIGZsb3dzLiBTZWUgaHR0cHM6Ly9wa2cuZ28uZGV2L25ldC9odHRwL3Bwcm9mIGZvciBkZXRhaWxzLlxuI1xuIyBwcm9maWxlLWxpc3Rlbi1odHRwOlxuXG4jIExvZ2dpbmcgb3B0aW9uc1xuI1xuIyBCeSBkZWZhdWx0LCBudGZ5IGxvZ3MgdG8gdGhlIGNvbnNvbGUgKHN0ZGVyciksIHdpdGggYW4gXCJpbmZvXCIgbG9nIGxldmVsLCBhbmQgaW4gYSBodW1hbi1yZWFkYWJsZSB0ZXh0IGZvcm1hdC5cbiMgbnRmeSBzdXBwb3J0cyBmaXZlIGRpZmZlcmVudCBsb2cgbGV2ZWxzLCBjYW4gYWxzbyB3cml0ZSB0byBhIGZpbGUsIGxvZyBhcyBKU09OLCBhbmQgZXZlbiBzdXBwb3J0cyBncmFudWxhclxuIyBsb2cgbGV2ZWwgb3ZlcnJpZGVzIGZvciBlYXNpZXIgZGVidWdnaW5nLiBTb21lIG9wdGlvbnMgKGxvZy1sZXZlbCBhbmQgbG9nLWxldmVsLW92ZXJyaWRlcykgY2FuIGJlIGhvdCByZWxvYWRlZFxuIyBieSBjYWxsaW5nIFwia2lsbCAtSFVQICRwaWRcIiBvciBcInN5c3RlbWN0bCByZWxvYWQgbnRmeVwiLlxuI1xuIyAtIGxvZy1mb3JtYXQgZGVmaW5lcyB0aGUgb3V0cHV0IGZvcm1hdCwgY2FuIGJlIFwidGV4dFwiIChkZWZhdWx0KSBvciBcImpzb25cIlxuIyAtIGxvZy1maWxlIGlzIGEgZmlsZW5hbWUgdG8gd3JpdGUgbG9ncyB0by4gSWYgdGhpcyBpcyBub3Qgc2V0LCBudGZ5IGxvZ3MgdG8gc3RkZXJyLlxuIyAtIGxvZy1sZXZlbCBkZWZpbmVzIHRoZSBkZWZhdWx0IGxvZyBsZXZlbCwgY2FuIGJlIG9uZSBvZiBcInRyYWNlXCIsIFwiZGVidWdcIiwgXCJpbmZvXCIgKGRlZmF1bHQpLCBcIndhcm5cIiBvciBcImVycm9yXCIuXG4jICAgQmUgYXdhcmUgdGhhdCBcImRlYnVnXCIgKGFuZCBwYXJ0aWN1bGFybHkgXCJ0cmFjZVwiKSBjYW4gYmUgVkVSWSBDSEFUVFkuIE9ubHkgdHVybiB0aGVtIG9uIGJyaWVmbHkgZm9yIGRlYnVnZ2luZyBwdXJwb3Nlcy5cbiMgLSBsb2ctbGV2ZWwtb3ZlcnJpZGVzIGxldHMgeW91IG92ZXJyaWRlIHRoZSBsb2cgbGV2ZWwgaWYgY2VydGFpbiBmaWVsZHMgbWF0Y2guIFRoaXMgaXMgaW5jcmVkaWJseSBwb3dlcmZ1bFxuIyAgIGZvciBkZWJ1Z2dpbmcgY2VydGFpbiBwYXJ0cyBvZiB0aGUgc3lzdGVtIChlLmcuIG9ubHkgdGhlIGFjY291bnQgbWFuYWdlbWVudCwgb3Igb25seSBhIGNlcnRhaW4gdmlzaXRvcikuXG4jICAgVGhpcyBpcyBhbiBhcnJheSBvZiBzdHJpbmdzIGluIHRoZSBmb3JtYXQ6XG4jICAgICAgLSBcImZpZWxkPXZhbHVlIC0+IGxldmVsXCIgdG8gbWF0Y2ggYSB2YWx1ZSBleGFjdGx5LCBlLmcuIFwidGFnPW1hbmFnZXIgLT4gdHJhY2VcIlxuIyAgICAgIC0gXCJmaWVsZCAtPiBsZXZlbFwiIHRvIG1hdGNoIGFueSB2YWx1ZSwgZS5nLiBcInRpbWVfdGFrZW5fbXMgLT4gZGVidWdcIlxuIyAgIFdhcm5pbmc6IFVzaW5nIGxvZy1sZXZlbC1vdmVycmlkZXMgaGFzIGEgcGVyZm9ybWFuY2UgcGVuYWx0eS4gT25seSB1c2UgaXQgZm9yIHRlbXBvcmFyeSBkZWJ1Z2dpbmcuXG4jXG4jIENoZWNrIHlvdXIgcGVybWlzc2lvbnM6XG4jICAgSWYgeW91IGFyZSBydW5uaW5nIG50Znkgd2l0aCBzeXN0ZW1kLCBtYWtlIHN1cmUgdGhpcyBsb2cgZmlsZSBpcyBvd25lZCBieSB0aGVcbiMgICBudGZ5IHVzZXIgYW5kIGdyb3VwIGJ5IHJ1bm5pbmc6IGNob3duIG50ZnkubnRmeSA8ZmlsZW5hbWU+LlxuI1xuIyBFeGFtcGxlIChnb29kIGZvciBwcm9kdWN0aW9uKTpcbiMgICBsb2ctbGV2ZWw6IGluZm9cbiMgICBsb2ctZm9ybWF0OiBqc29uXG4jICAgbG9nLWZpbGU6IC92YXIvbG9nL250ZnkubG9nXG4jXG4jIEV4YW1wbGUgbGV2ZWwgb3ZlcnJpZGVzIChmb3IgZGVidWdnaW5nLCBvbmx5IHVzZSB0ZW1wb3JhcmlseSk6XG4jICAgbG9nLWxldmVsLW92ZXJyaWRlczpcbiMgICAgICAtIFwidGFnPW1hbmFnZXIgLT4gdHJhY2VcIlxuIyAgICAgIC0gXCJ2aXNpdG9yX2lwPTEuMi4zLjQgLT4gZGVidWdcIlxuIyAgICAgIC0gXCJ0aW1lX3Rha2VuX21zIC0+IGRlYnVnXCJcbiNcbiMgbG9nLWxldmVsOiBpbmZvXG4jIGxvZy1sZXZlbC1vdmVycmlkZXM6XG4jIGxvZy1mb3JtYXQ6IHRleHRcbiMgbG9nLWZpbGU6XG5cIlwiXCJcbiIKfQ==
```

## Links

`alerting`,`alerts`,`api`,`notifications`,`self-hosted`

---

Version:`latest`

NotifuseOpen-source newsletter and notification platform that empowers teams to create, send, and track communications at scale.

Obsidian LiveSyncObsidian LiveSync with CouchDB for real-time note synchronization.

### On this page

ConfigurationBase64LinksTags