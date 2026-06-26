---
title: "Vault | Dokploy"
source: "https://docs.dokploy.com/docs/templates/vault"
category: dokploy-docs
created: "2026-06-25T17:22:01.420Z"
---

Vault | Dokploy

# Vault

Copy as Markdown

Vault is a tool for securely accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, certificates, and more. Vault provides a unified interface to any secret, while providing tight access control and recording a detailed audit log. To sign in: In the Vault UI, select 'Token' as the authentication method (not GitHub), then enter the root token from the VAULT_DEV_ROOT_TOKEN_ID environment variable (auto-generated).

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  vault:
    image: hashicorp/vault:latest
    container_name: vault
    cap_add:
      - IPC_LOCK
    environment:
      VAULT_DEV_ROOT_TOKEN_ID: "${VAULT_DEV_ROOT_TOKEN_ID}"
      VAULT_DEV_LISTEN_ADDRESS: "${VAULT_DEV_LISTEN_ADDRESS}"
    ports:
      - "8200"
    volumes:
      - vault-data:/vault/file
    command: "server -dev -dev-root-token-id=${VAULT_DEV_ROOT_TOKEN_ID} -dev-listen-address=${VAULT_DEV_LISTEN_ADDRESS}"

volumes:
  vault-data:
```

```
[variables]
main_domain = "${domain}"
root_token = "${password:32}"

[config]

[[config.domains]]
serviceName = "vault"
port = 8200
host = "${main_domain}"

[config.env]
VAULT_DEV_ROOT_TOKEN_ID = "${root_token}"
VAULT_DEV_LISTEN_ADDRESS = "0.0.0.0:8200"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHZhdWx0OlxuICAgIGltYWdlOiBoYXNoaWNvcnAvdmF1bHQ6bGF0ZXN0XG4gICAgY29udGFpbmVyX25hbWU6IHZhdWx0XG4gICAgY2FwX2FkZDpcbiAgICAgIC0gSVBDX0xPQ0tcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFZBVUxUX0RFVl9ST09UX1RPS0VOX0lEOiBcIiR7VkFVTFRfREVWX1JPT1RfVE9LRU5fSUR9XCJcbiAgICAgIFZBVUxUX0RFVl9MSVNURU5fQUREUkVTUzogXCIke1ZBVUxUX0RFVl9MSVNURU5fQUREUkVTU31cIlxuICAgIHBvcnRzOlxuICAgICAgLSBcIjgyMDBcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIHZhdWx0LWRhdGE6L3ZhdWx0L2ZpbGVcbiAgICBjb21tYW5kOiBcInNlcnZlciAtZGV2IC1kZXYtcm9vdC10b2tlbi1pZD0ke1ZBVUxUX0RFVl9ST09UX1RPS0VOX0lEfSAtZGV2LWxpc3Rlbi1hZGRyZXNzPSR7VkFVTFRfREVWX0xJU1RFTl9BRERSRVNTfVwiXG5cbnZvbHVtZXM6XG4gIHZhdWx0LWRhdGE6XG5cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5yb290X3Rva2VuID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInZhdWx0XCJcbnBvcnQgPSA4MjAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuVkFVTFRfREVWX1JPT1RfVE9LRU5fSUQgPSBcIiR7cm9vdF90b2tlbn1cIlxuVkFVTFRfREVWX0xJU1RFTl9BRERSRVNTID0gXCIwLjAuMC4wOjgyMDBcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuXG4iCn0=
```

## Links

`security`,`secrets`,`devops`,`infrastructure`

---

Version:`latest`

ValkeyValkey is an open-source fork of Redis, backed by AWS and the Linux Foundation. It provides a high-performance, in-memory data structure store with Redis compatibility.

VaultwardenUnofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs

### On this page

ConfigurationBase64LinksTags