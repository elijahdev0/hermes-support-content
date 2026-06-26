---
title: "Carbone | Dokploy"
source: "https://docs.dokploy.com/docs/templates/carbone"
category: dokploy-docs
created: "2026-06-25T17:21:42.678Z"
---

Carbone | Dokploy

# Carbone

Copy as Markdown

Carbone is a high-performance, self-hosted document generation engine. It allows you to generate reports, invoices, and documents in various formats (e.g., PDF, DOCX, XLSX) using JSON data and template-based rendering.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  carbone:
    image: carbone/carbone-ee:full-4.25.5
    restart: unless-stopped
    environment:
      - CARBONE_EE_LICENSE=${CARBONE_KEY}
      - CARBONE_EE_STUDIO=true
    ports:
      - 4000
    volumes:
      - template:/app/template

volumes:
  template:
```

```
[variables]
main_domain = "${domain}"
carbone_key = "${password:32}"

[config]
[[config.domains]]
serviceName = "carbone"
port = 4000
host = "${main_domain}"

[config.env]
CARBONE_KEY = "${carbone_key}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBjYXJib25lOlxuICAgIGltYWdlOiBjYXJib25lL2NhcmJvbmUtZWU6ZnVsbC00LjI1LjVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBDQVJCT05FX0VFX0xJQ0VOU0U9JHtDQVJCT05FX0tFWX1cbiAgICAgIC0gQ0FSQk9ORV9FRV9TVFVESU89dHJ1ZVxuICAgIHBvcnRzOlxuICAgICAgLSA0MDAwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gdGVtcGxhdGU6L2FwcC90ZW1wbGF0ZVxuXG52b2x1bWVzOlxuICB0ZW1wbGF0ZTogIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmNhcmJvbmVfa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjYXJib25lXCJcbnBvcnQgPSA0MDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuQ0FSQk9ORV9LRVkgPSBcIiR7Y2FyYm9uZV9rZXl9XCIgIgp9
```

## Links

`Document Generation`,`Automation`,`Reporting`,`Productivity`

---

Version:`4.25.5`

Cap.soCap.so is a platform for web and desktop applications with MySQL and S3 storage. It provides a complete development environment with database and file storage capabilities.

CasdoorAn open-source UI-first Identity and Access Management (IAM) / Single-Sign-On (SSO) platform with web UI supporting OAuth 2.0, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, and more.

### On this page

ConfigurationBase64LinksTags