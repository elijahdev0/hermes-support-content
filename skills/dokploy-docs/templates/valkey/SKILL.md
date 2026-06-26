---
title: "Valkey | Dokploy"
source: "https://docs.dokploy.com/docs/templates/valkey"
category: dokploy-docs
created: "2026-06-25T17:22:01.420Z"
---

Valkey | Dokploy

# Valkey

Copy as Markdown

Valkey is an open-source fork of Redis, backed by AWS and the Linux Foundation. It provides a high-performance, in-memory data structure store with Redis compatibility.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  valkey:
    image: valkey/valkey:8.1.4
    restart: unless-stopped
    ports:
      - 6379
    volumes:
      - ../files/valkey.conf:/etc/valkey/valkey.conf
      - valkey-data:/data
    command: valkey-server /etc/valkey/valkey.conf
    environment:
      - VALKEY_PASSWORD=${VALKEY_PASSWORD}
    healthcheck:
      test: ["CMD-SHELL", "valkey-cli -a \"$$VALKEY_PASSWORD\" ping | grep PONG"]
      interval: 10s
      timeout: 3s
      retries: 5
      start_period: 10s

volumes:
  valkey-data: {}
```

```
[variables]
valkey_password = "${password:32}"

[config]
env = [
  "VALKEY_PASSWORD=${valkey_password}"
]
mounts = []

[[config.mounts]]
filePath = "valkey.conf"
content = """
# Valkey configuration file
# For more information, see: https://github.com/valkey-io/valkey

# Network
bind 0.0.0.0
port 6379
protected-mode yes

# General
daemonize no
supervised no
pidfile /data/valkey.pid
loglevel notice
logfile ""

# Snapshotting
save 900 1
save 300 10
save 60 10000
stop-writes-on-bgsave-error yes
rdbcompression yes
rdbchecksum yes
dbfilename dump.rdb
dir /data

# Replication
replica-serve-stale-data yes
replica-read-only yes

# Security
requirepass ${valkey_password}

# Memory management
maxmemory-policy noeviction

# Append only file
appendonly yes
appendfilename "appendonly.aof"
appendfsync everysec
no-appendfsync-on-rewrite no
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHZhbGtleTpcbiAgICBpbWFnZTogdmFsa2V5L3ZhbGtleTo4LjEuNFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDYzNzlcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy92YWxrZXkuY29uZjovZXRjL3ZhbGtleS92YWxrZXkuY29uZlxuICAgICAgLSB2YWxrZXktZGF0YTovZGF0YVxuICAgIGNvbW1hbmQ6IHZhbGtleS1zZXJ2ZXIgL2V0Yy92YWxrZXkvdmFsa2V5LmNvbmZcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gVkFMS0VZX1BBU1NXT1JEPSR7VkFMS0VZX1BBU1NXT1JEfVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwidmFsa2V5LWNsaSAtYSBcXFwiJCRWQUxLRVlfUEFTU1dPUkRcXFwiIHBpbmcgfCBncmVwIFBPTkdcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDNzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICBzdGFydF9wZXJpb2Q6IDEwc1xuXG52b2x1bWVzOlxuICB2YWxrZXktZGF0YToge31cblxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG52YWxrZXlfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJWQUxLRVlfUEFTU1dPUkQ9JHt2YWxrZXlfcGFzc3dvcmR9XCJcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwidmFsa2V5LmNvbmZcIlxuY29udGVudCA9IFwiXCJcIlxuIyBWYWxrZXkgY29uZmlndXJhdGlvbiBmaWxlXG4jIEZvciBtb3JlIGluZm9ybWF0aW9uLCBzZWU6IGh0dHBzOi8vZ2l0aHViLmNvbS92YWxrZXktaW8vdmFsa2V5XG5cbiMgTmV0d29ya1xuYmluZCAwLjAuMC4wXG5wb3J0IDYzNzlcbnByb3RlY3RlZC1tb2RlIHllc1xuXG4jIEdlbmVyYWxcbmRhZW1vbml6ZSBub1xuc3VwZXJ2aXNlZCBub1xucGlkZmlsZSAvZGF0YS92YWxrZXkucGlkXG5sb2dsZXZlbCBub3RpY2VcbmxvZ2ZpbGUgXCJcIlxuXG4jIFNuYXBzaG90dGluZ1xuc2F2ZSA5MDAgMVxuc2F2ZSAzMDAgMTBcbnNhdmUgNjAgMTAwMDBcbnN0b3Atd3JpdGVzLW9uLWJnc2F2ZS1lcnJvciB5ZXNcbnJkYmNvbXByZXNzaW9uIHllc1xucmRiY2hlY2tzdW0geWVzXG5kYmZpbGVuYW1lIGR1bXAucmRiXG5kaXIgL2RhdGFcblxuIyBSZXBsaWNhdGlvblxucmVwbGljYS1zZXJ2ZS1zdGFsZS1kYXRhIHllc1xucmVwbGljYS1yZWFkLW9ubHkgeWVzXG5cbiMgU2VjdXJpdHlcbnJlcXVpcmVwYXNzICR7dmFsa2V5X3Bhc3N3b3JkfVxuXG4jIE1lbW9yeSBtYW5hZ2VtZW50XG5tYXhtZW1vcnktcG9saWN5IG5vZXZpY3Rpb25cblxuIyBBcHBlbmQgb25seSBmaWxlXG5hcHBlbmRvbmx5IHllc1xuYXBwZW5kZmlsZW5hbWUgXCJhcHBlbmRvbmx5LmFvZlwiXG5hcHBlbmRmc3luYyBldmVyeXNlY1xubm8tYXBwZW5kZnN5bmMtb24tcmV3cml0ZSBub1xuYXV0by1hb2YtcmV3cml0ZS1wZXJjZW50YWdlIDEwMFxuYXV0by1hb2YtcmV3cml0ZS1taW4tc2l6ZSA2NG1iXG5cIlwiXCJcblxuIgp9
```

## Links

`database`,`cache`,`redis`,`in-memory`

---

Version:`8.1.4`

useSendOpen source alternative to Resend, Sendgrid, Postmark etc.

VaultVault is a tool for securely accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, certificates, and more. Vault provides a unified interface to any secret, while providing tight access control and recording a detailed audit log. To sign in: In the Vault UI, select 'Token' as the authentication method (not GitHub), then enter the root token from the VAULT_DEV_ROOT_TOKEN_ID environment variable (auto-generated).

### On this page

ConfigurationBase64LinksTags