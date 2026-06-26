---
title: "AdGuard Home | Dokploy"
source: "https://docs.dokploy.com/docs/templates/adguardhome"
category: dokploy-docs
created: "2026-06-25T17:21:40.413Z"
---

AdGuard Home | Dokploy

# AdGuard Home

Copy as Markdown

AdGuard Home is a comprehensive solution designed to enhance your online browsing experience by eliminating all kinds of ads, from annoying banners and pop-ups to intrusive video ads. It provides privacy protection, browsing security, and parental control features while maintaining website functionality.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  adguardhome:
    image: adguard/adguardhome:latest
    restart: unless-stopped
    ports:
      - "53:53/tcp" # DNS
      - "53:53/udp" # DNS
      - "67:67/udp" # DHCP Server
      - "68:68/tcp" # DHCP Client
      - "853:853/tcp" # DNS over TLS, DNS-over-QUIC
      - "853:853/udp" # DNS over TLS, DNS-over-QUIC
      - "6060:6060/tcp" # HTTP (pprof)
    volumes:
      - adguardhome-work:/opt/adguardhome/work
      - adguardhome-conf:/opt/adguardhome/conf

volumes:
  adguardhome-work: {}
  adguardhome-conf: {}
```

```
[variables]
main_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "adguardhome"
port = 3000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhZGd1YXJkaG9tZTpcbiAgICBpbWFnZTogYWRndWFyZC9hZGd1YXJkaG9tZTpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSBcIjUzOjUzL3RjcFwiICMgRE5TXG4gICAgICAtIFwiNTM6NTMvdWRwXCIgIyBETlNcbiAgICAgIC0gXCI2Nzo2Ny91ZHBcIiAjIERIQ1AgU2VydmVyXG4gICAgICAtIFwiNjg6NjgvdGNwXCIgIyBESENQIENsaWVudFxuICAgICAgLSBcIjg1Mzo4NTMvdGNwXCIgIyBETlMgb3ZlciBUTFMsIEROUy1vdmVyLVFVSUNcbiAgICAgIC0gXCI4NTM6ODUzL3VkcFwiICMgRE5TIG92ZXIgVExTLCBETlMtb3Zlci1RVUlDXG4gICAgICAtIFwiNjA2MDo2MDYwL3RjcFwiICMgSFRUUCAocHByb2YpXG4gICAgdm9sdW1lczpcbiAgICAgIC0gYWRndWFyZGhvbWUtd29yazovb3B0L2FkZ3VhcmRob21lL3dvcmtcbiAgICAgIC0gYWRndWFyZGhvbWUtY29uZjovb3B0L2FkZ3VhcmRob21lL2NvbmZcblxudm9sdW1lczpcbiAgYWRndWFyZGhvbWUtd29yazoge31cbiAgYWRndWFyZGhvbWUtY29uZjoge30iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFkZ3VhcmRob21lXCJcbnBvcnQgPSAzMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbiIKfQ==
```

## Links

`privacy`,`security`,`dns`,`ad-blocking`

---

Version:`latest`

Actual BudgetA super fast and privacy-focused app for managing your finances.

AdminerAdminer is a comprehensive database management tool that supports MySQL, MariaDB, PostgreSQL, SQLite, MS SQL, Oracle, Elasticsearch, MongoDB and others. It provides a clean interface for efficient database operations, with strong security features and extensive customization options.

### On this page

ConfigurationBase64LinksTags