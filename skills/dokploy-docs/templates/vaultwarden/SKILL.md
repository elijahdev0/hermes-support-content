---
title: "Vaultwarden | Dokploy"
source: "https://docs.dokploy.com/docs/templates/vaultwarden"
category: dokploy-docs
created: "2026-06-25T17:22:01.420Z"
---

Vaultwarden | Dokploy

# Vaultwarden

Copy as Markdown

Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs

## Configuration

docker-compose.ymltemplate.toml

```
# the webserver can take a while to start up, so don't be alarmed if it takes a few minutes to get a response
services:
  vaultwarden:
    image: vaultwarden/server:1.34.3
    restart: always
    environment:
      DOMAIN: ${DOMAIN}
      SIGNUPS_ALLOWED: ${SIGNUPS_ALLOWED}
    volumes:
      - vaultwarden:/data
    expose:
      - 80

volumes:
  vaultwarden:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "vaultwarden"
port = 80
host = "${main_domain}"

[config.env]
SIGNUPS_ALLOWED = "true"
DOMAIN = "https://${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgdGhlIHdlYnNlcnZlciBjYW4gdGFrZSBhIHdoaWxlIHRvIHN0YXJ0IHVwLCBzbyBkb24ndCBiZSBhbGFybWVkIGlmIGl0IHRha2VzIGEgZmV3IG1pbnV0ZXMgdG8gZ2V0IGEgcmVzcG9uc2VcbnNlcnZpY2VzOlxuICB2YXVsdHdhcmRlbjpcbiAgICBpbWFnZTogdmF1bHR3YXJkZW4vc2VydmVyOjEuMzQuM1xuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGVudmlyb25tZW50OlxuICAgICAgRE9NQUlOOiAke0RPTUFJTn1cbiAgICAgIFNJR05VUFNfQUxMT1dFRDogJHtTSUdOVVBTX0FMTE9XRUR9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gdmF1bHR3YXJkZW46L2RhdGFcbiAgICBleHBvc2U6XG4gICAgICAtIDgwXG5cbnZvbHVtZXM6XG4gIHZhdWx0d2FyZGVuOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInZhdWx0d2FyZGVuXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblNJR05VUFNfQUxMT1dFRCA9IFwidHJ1ZVwiXG5ET01BSU4gPSBcImh0dHBzOi8vJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`open-source`

---

Version:`1.34.3`

VaultVault is a tool for securely accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, certificates, and more. Vault provides a unified interface to any secret, while providing tight access control and recording a detailed audit log. To sign in: In the Vault UI, select 'Token' as the authentication method (not GitHub), then enter the root token from the VAULT_DEV_ROOT_TOKEN_ID environment variable (auto-generated).

VerdaccioA lightweight Node.js private proxy registry

### On this page

ConfigurationBase64LinksTags