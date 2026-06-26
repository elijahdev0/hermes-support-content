---
title: "Authelia | Dokploy"
source: "https://docs.dokploy.com/docs/templates/authelia"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

Authelia | Dokploy

# Authelia

Copy as Markdown

The Single Sign-On Multi-Factor portal for web apps. An open-source authentication and authorization server providing 2FA and SSO via web portal.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  authelia:
    image: authelia/authelia:latest
    restart: unless-stopped
    volumes:
      - authelia_config:/config
      - ../files/configuration.yml:/config/configuration.yml:ro
      - ../files/users_database.yml:/config/users_database.yml
    environment:
      AUTHELIA_JWT_SECRET: $JWT_SECRET
      AUTHELIA_SESSION_SECRET: $SESSION_SECRET
      AUTHELIA_STORAGE_ENCRYPTION_KEY: $STORAGE_ENCRYPTION_KEY
      AUTHELIA_STORAGE_POSTGRES_PASSWORD: $POSTGRES_PASSWORD
    depends_on:
      redis:
        condition: service_healthy
      postgres:
        condition: service_healthy
    ports:
      - 9091

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data
    command: redis-server --save 60 1 --loglevel warning --requirepass $REDIS_PASSWORD
    environment:
      REDIS_PASSWORD: $REDIS_PASSWORD
    healthcheck:
      test: ["CMD", "redis-cli", "--raw", "incr", "ping"]
      interval: 10s
      timeout: 3s
      retries: 5

  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: authelia
      POSTGRES_USER: authelia
      POSTGRES_PASSWORD: $POSTGRES_PASSWORD
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U authelia -d authelia"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

volumes:
  authelia_config:
  redis_data:
  postgres_data:
```

```
[variables]
main_domain = "${domain}"
jwt_secret = "${password:64}"
session_secret = "${password:64}"
storage_encryption_key = "${password:64}"
redis_password = "${password:32}"
postgres_password = "${password:32}"
admin_username = "${username}"
admin_email = "${email}"
admin_password = "AdminPass123!"
admin_password_hash = "$argon2id$v=19$m=65536,t=3,p=4$170PGJ1MskQyxfFknfBPFQ$VqD1/pqC3fBHo+Zk58bC2xQm1ltOFTr0w2wx93vJgC4"

[config]
[[config.domains]]
serviceName = "authelia"
port = 9091
host = "${main_domain}"
path = "/"

[config.env]
JWT_SECRET = "${jwt_secret}"
SESSION_SECRET = "${session_secret}"
STORAGE_ENCRYPTION_KEY = "${storage_encryption_key}"
REDIS_PASSWORD = "${redis_password}"
POSTGRES_PASSWORD = "${postgres_password}"
admin_username = "${admin_username}"
admin_email = "${admin_email}"

[[config.mounts]]
filePath = "configuration.yml"
content = """
###############################################################
#                   Authelia configuration                    #
###############################################################

# DEFAULT ADMIN CREDENTIALS:
# Username: (auto-generated, check users_database.yml)
# Password: AdminPass123!
# Email: (auto-generated)
#
# IMPORTANT: Change the password after first login!
# SECURITY NOTE: This template starts with one-factor auth for easier setup.
# After configuring SMTP/notifications, change the policy to 'two_factor'

# Server Configuration
server:
  address: 'tcp://0.0.0.0:9091'
  headers:
    csp_template: ''

# Log Configuration
log:
  level: info
  format: text

# Theme
theme: auto

# TOTP Configuration
totp:
  disable: false
  issuer: authelia.com
  algorithm: sha1
  digits: 6
  period: 30
  skew: 1
  secret_size: 32

# WebAuthn/FIDO2 Configuration
webauthn:
  disable: false
  timeout: 60s
  display_name: Authelia
  attestation_conveyance_preference: indirect
  user_verification: preferred

# NTP Configuration
ntp:
  address: 'time.cloudflare.com:123'
  version: 4
  max_desync: 3s
  disable_startup_check: false
  disable_failure: false

# Authentication Backend Configuration
authentication_backend:
  password_reset:
    disable: false
    custom_url: ''
  refresh_interval: 5m
  file:
    path: /config/users_database.yml
    watch: false
    search:
      email: false
      case_insensitive: false
    password:
      algorithm: argon2
      argon2:
        variant: argon2id
        iterations: 3
        memory: 65536
        parallelism: 4
        key_length: 32
        salt_length: 16

# Password Policy
password_policy:
  standard:
    enabled: false
    min_length: 8
    max_length: 0
    require_uppercase: true
    require_lowercase: true
    require_number: true
    require_special: true
  zxcvbn:
    enabled: false
    min_score: 3

# Session Configuration
session:
  name: authelia_session
  domain: ${main_domain}
  same_site: lax
  secret: ${session_secret}
  expiration: 1h
  inactivity: 5m
  remember_me_duration: 1M
  redis:
    host: redis
    port: 6379
    password: ${redis_password}
    database_index: 0
    maximum_active_connections: 8
    minimum_idle_connections: 0

# Storage Configuration
storage:
  encryption_key: ${storage_encryption_key}
  postgres:
    host: postgres
    port: 5432
    database: authelia
    schema: public
    username: authelia
    password: ${postgres_password}
    timeout: 5s

# Notifier Configuration
notifier:
  disable_startup_check: true
  filesystem:
    filename: /config/notification.txt

# Regulation Configuration
regulation:
  max_retries: 3
  find_time: 10m
  ban_time: 12h

# Access Control Configuration - MODIFIED FOR EASIER INITIAL SETUP
access_control:
  default_policy: deny
  rules:
    - domain: ${main_domain}
      policy: one_factor  # Changed from one_factor to two_factor for production
"""

[[config.mounts]]
filePath = "users_database.yml"
content = """
###############################################################
#                         Users Database                     #
###############################################################

# DEFAULT LOGIN CREDENTIALS:
# Username: (generated from username helper)
# Password: AdminPass123!
# Email: (generated from email helper)
#
# IMPORTANT: Change the default password after first login!
# To generate a new password hash, run:
# docker run authelia/authelia:latest authelia hash-password 'your-new-password'

users:
  ${admin_username}:
    disabled: false
    displayname: "Authelia Admin"
    password: "${admin_password_hash}"
    email: ${admin_email}
    groups:
      - admins
      - dev
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBhdXRoZWxpYTpcbiAgICBpbWFnZTogYXV0aGVsaWEvYXV0aGVsaWE6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBhdXRoZWxpYV9jb25maWc6L2NvbmZpZ1xuICAgICAgLSAuLi9maWxlcy9jb25maWd1cmF0aW9uLnltbDovY29uZmlnL2NvbmZpZ3VyYXRpb24ueW1sOnJvXG4gICAgICAtIC4uL2ZpbGVzL3VzZXJzX2RhdGFiYXNlLnltbDovY29uZmlnL3VzZXJzX2RhdGFiYXNlLnltbFxuICAgIGVudmlyb25tZW50OlxuICAgICAgQVVUSEVMSUFfSldUX1NFQ1JFVDogJEpXVF9TRUNSRVRcbiAgICAgIEFVVEhFTElBX1NFU1NJT05fU0VDUkVUOiAkU0VTU0lPTl9TRUNSRVRcbiAgICAgIEFVVEhFTElBX1NUT1JBR0VfRU5DUllQVElPTl9LRVk6ICRTVE9SQUdFX0VOQ1JZUFRJT05fS0VZXG4gICAgICBBVVRIRUxJQV9TVE9SQUdFX1BPU1RHUkVTX1BBU1NXT1JEOiAkUE9TVEdSRVNfUEFTU1dPUkRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgcmVkaXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgICBwb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICBwb3J0czpcbiAgICAgIC0gOTA5MVxuXG4gIHJlZGlzOlxuICAgIGltYWdlOiByZWRpczo3LWFscGluZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcmVkaXNfZGF0YTovZGF0YVxuICAgIGNvbW1hbmQ6IHJlZGlzLXNlcnZlciAtLXNhdmUgNjAgMSAtLWxvZ2xldmVsIHdhcm5pbmcgLS1yZXF1aXJlcGFzcyAkUkVESVNfUEFTU1dPUkRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFJFRElTX1BBU1NXT1JEOiAkUkVESVNfUEFTU1dPUkRcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcInJlZGlzLWNsaVwiLCBcIi0tcmF3XCIsIFwiaW5jclwiLCBcInBpbmdcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDNzXG4gICAgICByZXRyaWVzOiA1XG5cbiAgcG9zdGdyZXM6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE2LWFscGluZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcG9zdGdyZXNfZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTX0RCOiBhdXRoZWxpYVxuICAgICAgUE9TVEdSRVNfVVNFUjogYXV0aGVsaWFcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAkUE9TVEdSRVNfUEFTU1dPUkRcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgYXV0aGVsaWEgLWQgYXV0aGVsaWFcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICBzdGFydF9wZXJpb2Q6IDMwc1xuXG52b2x1bWVzOlxuICBhdXRoZWxpYV9jb25maWc6XG4gIHJlZGlzX2RhdGE6XG4gIHBvc3RncmVzX2RhdGE6IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmp3dF9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6NjR9XCJcbnNlc3Npb25fc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjY0fVwiXG5zdG9yYWdlX2VuY3J5cHRpb25fa2V5ID0gXCIke3Bhc3N3b3JkOjY0fVwiXG5yZWRpc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmFkbWluX3VzZXJuYW1lID0gXCIke3VzZXJuYW1lfVwiXG5hZG1pbl9lbWFpbCA9IFwiJHtlbWFpbH1cIlxuYWRtaW5fcGFzc3dvcmQgPSBcIkFkbWluUGFzczEyMyFcIlxuYWRtaW5fcGFzc3dvcmRfaGFzaCA9IFwiJGFyZ29uMmlkJHY9MTkkbT02NTUzNix0PTMscD00JDE3MFBHSjFNc2tReXhmRmtuZkJQRlEkVnFEMS9wcUMzZkJIbytaazU4YkMyeFFtMWx0T0ZUcjB3Mnd4OTN2SmdDNFwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhdXRoZWxpYVwiXG5wb3J0ID0gOTA5MVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxucGF0aCA9IFwiL1wiXG5cbltjb25maWcuZW52XVxuSldUX1NFQ1JFVCA9IFwiJHtqd3Rfc2VjcmV0fVwiXG5TRVNTSU9OX1NFQ1JFVCA9IFwiJHtzZXNzaW9uX3NlY3JldH1cIlxuU1RPUkFHRV9FTkNSWVBUSU9OX0tFWSA9IFwiJHtzdG9yYWdlX2VuY3J5cHRpb25fa2V5fVwiXG5SRURJU19QQVNTV09SRCA9IFwiJHtyZWRpc19wYXNzd29yZH1cIlxuUE9TVEdSRVNfUEFTU1dPUkQgPSBcIiR7cG9zdGdyZXNfcGFzc3dvcmR9XCJcbmFkbWluX3VzZXJuYW1lID0gXCIke2FkbWluX3VzZXJuYW1lfVwiXG5hZG1pbl9lbWFpbCA9IFwiJHthZG1pbl9lbWFpbH1cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcImNvbmZpZ3VyYXRpb24ueW1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjI1xuIyAgICAgICAgICAgICAgICAgICBBdXRoZWxpYSBjb25maWd1cmF0aW9uICAgICAgICAgICAgICAgICAgICAjXG4jIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyNcblxuIyBERUZBVUxUIEFETUlOIENSRURFTlRJQUxTOlxuIyBVc2VybmFtZTogKGF1dG8tZ2VuZXJhdGVkLCBjaGVjayB1c2Vyc19kYXRhYmFzZS55bWwpXG4jIFBhc3N3b3JkOiBBZG1pblBhc3MxMjMhXG4jIEVtYWlsOiAoYXV0by1nZW5lcmF0ZWQpXG4jXG4jIElNUE9SVEFOVDogQ2hhbmdlIHRoZSBwYXNzd29yZCBhZnRlciBmaXJzdCBsb2dpbiFcbiMgU0VDVVJJVFkgTk9URTogVGhpcyB0ZW1wbGF0ZSBzdGFydHMgd2l0aCBvbmUtZmFjdG9yIGF1dGggZm9yIGVhc2llciBzZXR1cC5cbiMgQWZ0ZXIgY29uZmlndXJpbmcgU01UUC9ub3RpZmljYXRpb25zLCBjaGFuZ2UgdGhlIHBvbGljeSB0byAndHdvX2ZhY3RvcidcblxuIyBTZXJ2ZXIgQ29uZmlndXJhdGlvblxuc2VydmVyOlxuICBhZGRyZXNzOiAndGNwOi8vMC4wLjAuMDo5MDkxJ1xuICBoZWFkZXJzOlxuICAgIGNzcF90ZW1wbGF0ZTogJydcblxuIyBMb2cgQ29uZmlndXJhdGlvblxubG9nOlxuICBsZXZlbDogaW5mb1xuICBmb3JtYXQ6IHRleHRcblxuIyBUaGVtZVxudGhlbWU6IGF1dG9cblxuIyBUT1RQIENvbmZpZ3VyYXRpb25cbnRvdHA6XG4gIGRpc2FibGU6IGZhbHNlXG4gIGlzc3VlcjogYXV0aGVsaWEuY29tXG4gIGFsZ29yaXRobTogc2hhMVxuICBkaWdpdHM6IDZcbiAgcGVyaW9kOiAzMFxuICBza2V3OiAxXG4gIHNlY3JldF9zaXplOiAzMlxuXG4jIFdlYkF1dGhuL0ZJRE8yIENvbmZpZ3VyYXRpb25cbndlYmF1dGhuOlxuICBkaXNhYmxlOiBmYWxzZVxuICB0aW1lb3V0OiA2MHNcbiAgZGlzcGxheV9uYW1lOiBBdXRoZWxpYVxuICBhdHRlc3RhdGlvbl9jb252ZXlhbmNlX3ByZWZlcmVuY2U6IGluZGlyZWN0XG4gIHVzZXJfdmVyaWZpY2F0aW9uOiBwcmVmZXJyZWRcblxuIyBOVFAgQ29uZmlndXJhdGlvblxubnRwOlxuICBhZGRyZXNzOiAndGltZS5jbG91ZGZsYXJlLmNvbToxMjMnXG4gIHZlcnNpb246IDRcbiAgbWF4X2Rlc3luYzogM3NcbiAgZGlzYWJsZV9zdGFydHVwX2NoZWNrOiBmYWxzZVxuICBkaXNhYmxlX2ZhaWx1cmU6IGZhbHNlXG5cbiMgQXV0aGVudGljYXRpb24gQmFja2VuZCBDb25maWd1cmF0aW9uXG5hdXRoZW50aWNhdGlvbl9iYWNrZW5kOlxuICBwYXNzd29yZF9yZXNldDpcbiAgICBkaXNhYmxlOiBmYWxzZVxuICAgIGN1c3RvbV91cmw6ICcnXG4gIHJlZnJlc2hfaW50ZXJ2YWw6IDVtXG4gIGZpbGU6XG4gICAgcGF0aDogL2NvbmZpZy91c2Vyc19kYXRhYmFzZS55bWxcbiAgICB3YXRjaDogZmFsc2VcbiAgICBzZWFyY2g6XG4gICAgICBlbWFpbDogZmFsc2VcbiAgICAgIGNhc2VfaW5zZW5zaXRpdmU6IGZhbHNlXG4gICAgcGFzc3dvcmQ6XG4gICAgICBhbGdvcml0aG06IGFyZ29uMlxuICAgICAgYXJnb24yOlxuICAgICAgICB2YXJpYW50OiBhcmdvbjJpZFxuICAgICAgICBpdGVyYXRpb25zOiAzXG4gICAgICAgIG1lbW9yeTogNjU1MzZcbiAgICAgICAgcGFyYWxsZWxpc206IDRcbiAgICAgICAga2V5X2xlbmd0aDogMzJcbiAgICAgICAgc2FsdF9sZW5ndGg6IDE2XG5cbiMgUGFzc3dvcmQgUG9saWN5XG5wYXNzd29yZF9wb2xpY3k6XG4gIHN0YW5kYXJkOlxuICAgIGVuYWJsZWQ6IGZhbHNlXG4gICAgbWluX2xlbmd0aDogOFxuICAgIG1heF9sZW5ndGg6IDBcbiAgICByZXF1aXJlX3VwcGVyY2FzZTogdHJ1ZVxuICAgIHJlcXVpcmVfbG93ZXJjYXNlOiB0cnVlXG4gICAgcmVxdWlyZV9udW1iZXI6IHRydWVcbiAgICByZXF1aXJlX3NwZWNpYWw6IHRydWVcbiAgenhjdmJuOlxuICAgIGVuYWJsZWQ6IGZhbHNlXG4gICAgbWluX3Njb3JlOiAzXG5cbiMgU2Vzc2lvbiBDb25maWd1cmF0aW9uXG5zZXNzaW9uOlxuICBuYW1lOiBhdXRoZWxpYV9zZXNzaW9uXG4gIGRvbWFpbjogJHttYWluX2RvbWFpbn1cbiAgc2FtZV9zaXRlOiBsYXhcbiAgc2VjcmV0OiAke3Nlc3Npb25fc2VjcmV0fVxuICBleHBpcmF0aW9uOiAxaFxuICBpbmFjdGl2aXR5OiA1bVxuICByZW1lbWJlcl9tZV9kdXJhdGlvbjogMU1cbiAgcmVkaXM6XG4gICAgaG9zdDogcmVkaXNcbiAgICBwb3J0OiA2Mzc5XG4gICAgcGFzc3dvcmQ6ICR7cmVkaXNfcGFzc3dvcmR9XG4gICAgZGF0YWJhc2VfaW5kZXg6IDBcbiAgICBtYXhpbXVtX2FjdGl2ZV9jb25uZWN0aW9uczogOFxuICAgIG1pbmltdW1faWRsZV9jb25uZWN0aW9uczogMFxuXG4jIFN0b3JhZ2UgQ29uZmlndXJhdGlvblxuc3RvcmFnZTpcbiAgZW5jcnlwdGlvbl9rZXk6ICR7c3RvcmFnZV9lbmNyeXB0aW9uX2tleX1cbiAgcG9zdGdyZXM6XG4gICAgaG9zdDogcG9zdGdyZXNcbiAgICBwb3J0OiA1NDMyXG4gICAgZGF0YWJhc2U6IGF1dGhlbGlhXG4gICAgc2NoZW1hOiBwdWJsaWNcbiAgICB1c2VybmFtZTogYXV0aGVsaWFcbiAgICBwYXNzd29yZDogJHtwb3N0Z3Jlc19wYXNzd29yZH1cbiAgICB0aW1lb3V0OiA1c1xuXG4jIE5vdGlmaWVyIENvbmZpZ3VyYXRpb25cbm5vdGlmaWVyOlxuICBkaXNhYmxlX3N0YXJ0dXBfY2hlY2s6IHRydWVcbiAgZmlsZXN5c3RlbTpcbiAgICBmaWxlbmFtZTogL2NvbmZpZy9ub3RpZmljYXRpb24udHh0XG5cbiMgUmVndWxhdGlvbiBDb25maWd1cmF0aW9uXG5yZWd1bGF0aW9uOlxuICBtYXhfcmV0cmllczogM1xuICBmaW5kX3RpbWU6IDEwbVxuICBiYW5fdGltZTogMTJoXG5cbiMgQWNjZXNzIENvbnRyb2wgQ29uZmlndXJhdGlvbiAtIE1PRElGSUVEIEZPUiBFQVNJRVIgSU5JVElBTCBTRVRVUFxuYWNjZXNzX2NvbnRyb2w6XG4gIGRlZmF1bHRfcG9saWN5OiBkZW55XG4gIHJ1bGVzOlxuICAgIC0gZG9tYWluOiAke21haW5fZG9tYWlufVxuICAgICAgcG9saWN5OiBvbmVfZmFjdG9yICAjIENoYW5nZWQgZnJvbSBvbmVfZmFjdG9yIHRvIHR3b19mYWN0b3IgZm9yIHByb2R1Y3Rpb25cblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcInVzZXJzX2RhdGFiYXNlLnltbFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyNcbiMgICAgICAgICAgICAgICAgICAgICAgICAgVXNlcnMgRGF0YWJhc2UgICAgICAgICAgICAgICAgICAgICAjXG4jIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyNcblxuIyBERUZBVUxUIExPR0lOIENSRURFTlRJQUxTOlxuIyBVc2VybmFtZTogKGdlbmVyYXRlZCBmcm9tIHVzZXJuYW1lIGhlbHBlcilcbiMgUGFzc3dvcmQ6IEFkbWluUGFzczEyMyFcbiMgRW1haWw6IChnZW5lcmF0ZWQgZnJvbSBlbWFpbCBoZWxwZXIpXG4jXG4jIElNUE9SVEFOVDogQ2hhbmdlIHRoZSBkZWZhdWx0IHBhc3N3b3JkIGFmdGVyIGZpcnN0IGxvZ2luIVxuIyBUbyBnZW5lcmF0ZSBhIG5ldyBwYXNzd29yZCBoYXNoLCBydW46XG4jIGRvY2tlciBydW4gYXV0aGVsaWEvYXV0aGVsaWE6bGF0ZXN0IGF1dGhlbGlhIGhhc2gtcGFzc3dvcmQgJ3lvdXItbmV3LXBhc3N3b3JkJ1xuXG51c2VyczpcbiAgJHthZG1pbl91c2VybmFtZX06XG4gICAgZGlzYWJsZWQ6IGZhbHNlXG4gICAgZGlzcGxheW5hbWU6IFwiQXV0aGVsaWEgQWRtaW5cIlxuICAgIHBhc3N3b3JkOiBcIiR7YWRtaW5fcGFzc3dvcmRfaGFzaH1cIlxuICAgIGVtYWlsOiAke2FkbWluX2VtYWlsfVxuICAgIGdyb3VwczpcbiAgICAgIC0gYWRtaW5zXG4gICAgICAtIGRldlxuXCJcIlwiXG4iCn0=
```

## Links

`authentication`,`authorization`,`2fa`,`sso`,`security`,`reverse-proxy`,`ldap`

---

Version:`latest`

AudiobookshelfAudiobookshelf is a self-hosted server designed to manage and play your audiobooks and podcasts. It works best when you have an organized directory structure.

AuthentikAuthentik is an open-source Identity Provider for authentication and authorization. It provides a comprehensive solution for managing user authentication, authorization, and identity federation with support for SAML, OAuth2, OIDC, and more.

### On this page

ConfigurationBase64LinksTags