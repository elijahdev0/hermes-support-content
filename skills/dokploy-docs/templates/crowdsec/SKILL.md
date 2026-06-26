---
title: "Crowdsec | Dokploy"
source: "https://docs.dokploy.com/docs/templates/crowdsec"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

Crowdsec | Dokploy

# Crowdsec

Copy as Markdown

CrowdSec provides open source solution for detecting and blocking malicious IPs, safeguarding both infrastructure and application security.

## Configuration

docker-compose.ymltemplate.toml

```
# --------------------------------------------------------------------------------
# note: this is the minimal crowdsec container
# this compose file prepared to work with two key remediation engines
# install and configure them via links below:
# traefik bouncer plugin | https://plugins.traefik.io/plugins/6335346ca4caa9ddeffda116/crowdsec-bouncer-traefik-plugin
# firewall bouncer (iptables) | https://docs.crowdsec.net/u/bouncers/firewall/
# --------------------------------------------------------------------------------
services:
  crowdsec:
    image: crowdsecurity/crowdsec:latest
    environment:
      GID: "${GID-1000}"
      COLLECTIONS: "crowdsecurity/linux crowdsecurity/traefik crowdsecurity/http-cve"
    volumes:
      - ../files/acquis.yaml:/etc/crowdsec/acquis.yaml # https://docs.crowdsec.net/u/getting_started/post_installation/acquisition_new/
      - crowdsec-db:/var/lib/crowdsec/data/
      - crowdsec-config:/etc/crowdsec/
      - /etc/dokploy/traefik/dynamic/access.log:/var/log/traefik/access.log:ro # make sure access log is enabled in dokploy
      - ${AUTH_LOG_PATH}:/var/log/ssh/auth.log:ro
      # - /var/log/fail2ban.log:/var/log/fail2ban/fail2ban.log:ro # uncomment if you have fail2ban installed on the system
    security_opt:
      - no-new-privileges:true
    # uncomment these two lines if you intent to use firewall bouncer installed natively on the host
    # ports:
    #  - "127.0.0.1:8080:8080" # local binding only, necessary for firewall-iptables-bouncer to connect to container's lapi
    labels:
      - traefik.enable=false
    restart: unless-stopped
volumes:
  crowdsec-db:
  crowdsec-config:
```

```
[variables]
auth_log_path = "/var/log/auth.log"

[config]
mounts = []
domains = []

[config.env]
AUTH_LOG_PATH = "${auth_log_path}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiMgbm90ZTogdGhpcyBpcyB0aGUgbWluaW1hbCBjcm93ZHNlYyBjb250YWluZXJcbiMgdGhpcyBjb21wb3NlIGZpbGUgcHJlcGFyZWQgdG8gd29yayB3aXRoIHR3byBrZXkgcmVtZWRpYXRpb24gZW5naW5lc1xuIyBpbnN0YWxsIGFuZCBjb25maWd1cmUgdGhlbSB2aWEgbGlua3MgYmVsb3c6XG4jIHRyYWVmaWsgYm91bmNlciBwbHVnaW4gfCBodHRwczovL3BsdWdpbnMudHJhZWZpay5pby9wbHVnaW5zLzYzMzUzNDZjYTRjYWE5ZGRlZmZkYTExNi9jcm93ZHNlYy1ib3VuY2VyLXRyYWVmaWstcGx1Z2luXG4jIGZpcmV3YWxsIGJvdW5jZXIgKGlwdGFibGVzKSB8IGh0dHBzOi8vZG9jcy5jcm93ZHNlYy5uZXQvdS9ib3VuY2Vycy9maXJld2FsbC9cbiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbnNlcnZpY2VzOlxuICBjcm93ZHNlYzpcbiAgICBpbWFnZTogY3Jvd2RzZWN1cml0eS9jcm93ZHNlYzpsYXRlc3RcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEdJRDogXCIke0dJRC0xMDAwfVwiXG4gICAgICBDT0xMRUNUSU9OUzogXCJjcm93ZHNlY3VyaXR5L2xpbnV4IGNyb3dkc2VjdXJpdHkvdHJhZWZpayBjcm93ZHNlY3VyaXR5L2h0dHAtY3ZlXCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9hY3F1aXMueWFtbDovZXRjL2Nyb3dkc2VjL2FjcXVpcy55YW1sICMgaHR0cHM6Ly9kb2NzLmNyb3dkc2VjLm5ldC91L2dldHRpbmdfc3RhcnRlZC9wb3N0X2luc3RhbGxhdGlvbi9hY3F1aXNpdGlvbl9uZXcvXG4gICAgICAtIGNyb3dkc2VjLWRiOi92YXIvbGliL2Nyb3dkc2VjL2RhdGEvXG4gICAgICAtIGNyb3dkc2VjLWNvbmZpZzovZXRjL2Nyb3dkc2VjL1xuICAgICAgLSAvZXRjL2Rva3Bsb3kvdHJhZWZpay9keW5hbWljL2FjY2Vzcy5sb2c6L3Zhci9sb2cvdHJhZWZpay9hY2Nlc3MubG9nOnJvICMgbWFrZSBzdXJlIGFjY2VzcyBsb2cgaXMgZW5hYmxlZCBpbiBkb2twbG95XG4gICAgICAtICR7QVVUSF9MT0dfUEFUSH06L3Zhci9sb2cvc3NoL2F1dGgubG9nOnJvXG4gICAgICAjIC0gL3Zhci9sb2cvZmFpbDJiYW4ubG9nOi92YXIvbG9nL2ZhaWwyYmFuL2ZhaWwyYmFuLmxvZzpybyAjIHVuY29tbWVudCBpZiB5b3UgaGF2ZSBmYWlsMmJhbiBpbnN0YWxsZWQgb24gdGhlIHN5c3RlbVxuICAgIHNlY3VyaXR5X29wdDpcbiAgICAgIC0gbm8tbmV3LXByaXZpbGVnZXM6dHJ1ZVxuICAgICMgdW5jb21tZW50IHRoZXNlIHR3byBsaW5lcyBpZiB5b3UgaW50ZW50IHRvIHVzZSBmaXJld2FsbCBib3VuY2VyIGluc3RhbGxlZCBuYXRpdmVseSBvbiB0aGUgaG9zdFxuICAgICMgcG9ydHM6IFxuICAgICMgIC0gXCIxMjcuMC4wLjE6ODA4MDo4MDgwXCIgIyBsb2NhbCBiaW5kaW5nIG9ubHksIG5lY2Vzc2FyeSBmb3IgZmlyZXdhbGwtaXB0YWJsZXMtYm91bmNlciB0byBjb25uZWN0IHRvIGNvbnRhaW5lcidzIGxhcGlcbiAgICBsYWJlbHM6XG4gICAgICAtIHRyYWVmaWsuZW5hYmxlPWZhbHNlXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbnZvbHVtZXM6XG4gIGNyb3dkc2VjLWRiOlxuICBjcm93ZHNlYy1jb25maWc6IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5hdXRoX2xvZ19wYXRoID0gXCIvdmFyL2xvZy9hdXRoLmxvZ1wiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuZG9tYWlucyA9IFtdXG5cbltjb25maWcuZW52XVxuQVVUSF9MT0dfUEFUSCA9IFwiJHthdXRoX2xvZ19wYXRofVwiIgp9
```

## Links

`security`,`firewall`

---

Version:`latest`

Crawl4AICrawl4AI is a modern AI-powered web crawler with support for screenshots, PDFs, JavaScript execution, and LLM-based extraction. Includes an interactive playground and MCP (Model Context Protocol) integration.

CupCup is a self-hosted Docker container management UI.

### On this page

ConfigurationBase64LinksTags