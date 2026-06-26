---
title: "Change Detection | Dokploy"
source: "https://docs.dokploy.com/docs/templates/changedetection"
category: dokploy-docs
created: "2026-06-25T17:21:43.962Z"
---

Change Detection | Dokploy

# Change Detection

Copy as Markdown

Changedetection.io is an intelligent tool designed to monitor changes on websites. Perfect for smart shoppers, data journalists, research engineers, data scientists, and security researchers.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  changedetection:
    image: ghcr.io/dgtlmoon/changedetection.io:0.49
    restart: unless-stopped
    ports:
      - 5000
    volumes:
      - datastore:/datastore

volumes:
  datastore:
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "changedetection"
port = 5000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBjaGFuZ2VkZXRlY3Rpb246XG4gICAgaW1hZ2U6IGdoY3IuaW8vZGd0bG1vb24vY2hhbmdlZGV0ZWN0aW9uLmlvOjAuNDlcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSA1MDAwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGF0YXN0b3JlOi9kYXRhc3RvcmVcblxudm9sdW1lczpcbiAgZGF0YXN0b3JlOiAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY2hhbmdlZGV0ZWN0aW9uXCJcbnBvcnQgPSA1MDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiICIKfQ==
```

## Links

`Monitoring`,`Data`,`Notifications`

---

Version:`0.49`

CasdoorAn open-source UI-first Identity and Access Management (IAM) / Single-Sign-On (SSO) platform with web UI supporting OAuth 2.0, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, and more.

ChatwootOpen-source customer engagement platform that provides a shared inbox for teams, live chat, and omnichannel support.

### On this page

ConfigurationBase64LinksTags