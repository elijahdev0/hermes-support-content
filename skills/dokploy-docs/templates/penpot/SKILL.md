---
title: "Penpot | Dokploy"
source: "https://docs.dokploy.com/docs/templates/penpot"
category: dokploy-docs
created: "2026-06-25T17:21:56.646Z"
---

Penpot | Dokploy

# Penpot

Copy as Markdown

Penpot is the web-based open-source design tool that bridges the gap between designers and developers.

## Configuration

docker-compose.ymltemplate.toml

```
## Common flags:
# demo-users
# email-verification
# log-emails
# log-invitation-tokens
# login-with-github
# login-with-gitlab
# login-with-google
# login-with-ldap
# login-with-oidc
# login-with-password
# prepl-server
# registration
# secure-session-cookies
# smtp
# smtp-debug
# telemetry
# webhooks
##
## You can read more about all available flags and other
## environment variables here:
## https://help.penpot.app/technical-guide/configuration/#advanced-configuration
#
# WARNING: if you're exposing Penpot to the internet, you should remove the flags
# 'disable-secure-session-cookies' and 'disable-email-verification'

volumes:
  penpot_postgres_v15:
  penpot_assets:
  penpot_traefik:
  # penpot_minio:

services:

  penpot-frontend:
    image: "penpotapp/frontend:2.6.1"
    restart: always
    ports:
      - 8080
      - 9001

    volumes:
      - penpot_assets:/opt/data/assets

    depends_on:
      - penpot-backend
      - penpot-exporter

    environment:
      PENPOT_FLAGS: disable-email-verification enable-smtp enable-prepl-server disable-secure-session-cookies

  penpot-backend:
    image: "penpotapp/backend:2.6.1"
    restart: always

    volumes:
      - penpot_assets:/opt/data/assets

    depends_on:
      - penpot-postgres
      - penpot-redis

    ## Configuration envronment variables for the backend
    ## container.

    environment:
      PENPOT_PUBLIC_URI: http://${DOMAIN_NAME}
      PENPOT_FLAGS: disable-email-verification enable-smtp enable-prepl-server disable-secure-session-cookies

      ## Penpot SECRET KEY. It serves as a master key from which other keys for subsystems
      ## (eg http sessions, or invitations) are derived.
      ##
      ## If you leave it commented, all created sessions and invitations will
      ## become invalid on container restart.
      ##
      ## If you going to uncomment this, we recommend to use a trully randomly generated
      ## 512 bits base64 encoded string here.  You can generate one with:
      ##
      ## python3 -c "import secrets; print(secrets.token_urlsafe(64))"

      # PENPOT_SECRET_KEY: my-insecure-key

      ## The PREPL host. Mainly used for external programatic access to penpot backend
      ## (example: admin). By default it will listen on `localhost` but if you are going to use
      ## the `admin`, you will need to uncomment this and set the host to `0.0.0.0`.

      # PENPOT_PREPL_HOST: 0.0.0.0

      ## Database connection parameters. Don't touch them unless you are using custom
      ## postgresql connection parameters.

      PENPOT_DATABASE_URI: postgresql://penpot-postgres/penpot
      PENPOT_DATABASE_USERNAME: penpot
      PENPOT_DATABASE_PASSWORD: penpot

      ## Redis is used for the websockets notifications. Don't touch unless the redis
      ## container has different parameters or different name.

      PENPOT_REDIS_URI: redis://penpot-redis/0

      ## Default configuration for assets storage: using filesystem based with all files
      ## stored in a docker volume.

      PENPOT_ASSETS_STORAGE_BACKEND: assets-fs
      PENPOT_STORAGE_ASSETS_FS_DIRECTORY: /opt/data/assets

      ## Also can be configured to to use a S3 compatible storage
      ## service like MiniIO. Look below for minio service setup.

      # AWS_ACCESS_KEY_ID: <KEY_ID>
      # AWS_SECRET_ACCESS_KEY: <ACCESS_KEY>
      # PENPOT_ASSETS_STORAGE_BACKEND: assets-s3
      # PENPOT_STORAGE_ASSETS_S3_ENDPOINT: http://penpot-minio:9000
      # PENPOT_STORAGE_ASSETS_S3_BUCKET: <BUKET_NAME>

      ## Telemetry. When enabled, a periodical process will send anonymous data about this
      ## instance. Telemetry data will enable us to learn how the application is used,
      ## based on real scenarios. If you want to help us, please leave it enabled. You can
      ## audit what data we send with the code available on github.

      PENPOT_TELEMETRY_ENABLED: true

      ## Example SMTP/Email configuration. By default, emails are sent to the mailcatch
      ## service, but for production usage it is recommended to setup a real SMTP
      ## provider. Emails are used to confirm user registrations & invitations. Look below
      ## how the mailcatch service is configured.

      PENPOT_SMTP_DEFAULT_FROM: [email protected]
      PENPOT_SMTP_DEFAULT_REPLY_TO: [email protected]
      PENPOT_SMTP_HOST: penpot-mailcatch
      PENPOT_SMTP_PORT: 1025
      PENPOT_SMTP_USERNAME:
      PENPOT_SMTP_PASSWORD:
      PENPOT_SMTP_TLS: false
      PENPOT_SMTP_SSL: false

  penpot-exporter:
    image: "penpotapp/exporter:2.6.1"
    restart: always

    environment:
      # Don't touch it; this uses an internal docker network to
      # communicate with the frontend.
      PENPOT_PUBLIC_URI: http://penpot-frontend

      ## Redis is used for the websockets notifications.
      PENPOT_REDIS_URI: redis://penpot-redis/0

  penpot-postgres:
    image: "postgres:15"
    restart: always
    stop_signal: SIGINT

    volumes:
      - penpot_postgres_v15:/var/lib/postgresql/data

    environment:
      - POSTGRES_INITDB_ARGS=--data-checksums
      - POSTGRES_DB=penpot
      - POSTGRES_USER=penpot
      - POSTGRES_PASSWORD=penpot

  penpot-redis:
    image: redis:7.2
    restart: always

  ## A mailcatch service, used as temporal SMTP server. You can access via HTTP to the
  ## port 1080 for read all emails the penpot platform has sent. Should be only used as a
  ## temporal solution while no real SMTP provider is configured.

  penpot-mailcatch:
    image: sj26/mailcatcher:latest
    restart: always
    expose:
      - '1025'
    ports:
      - 1080

  ## Example configuration of MiniIO (S3 compatible object storage service); If you don't
  ## have preference, then just use filesystem, this is here just for the completeness.

  # minio:
  #   image: "minio/minio:latest"
  #   command: minio server /mnt/data --console-address ":9001"
  #   restart: always
  #
  #   volumes:
  #     - "penpot_minio:/mnt/data"
  #
  #   environment:
  #     - MINIO_ROOT_USER=minioadmin
  #     - MINIO_ROOT_PASSWORD=minioadmin
  #
  #   ports:
  #     - 9000:9000
  #     - 9001:9001
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "penpot-frontend"
port = 8080
host = "${main_domain}"

[config.env]
DOMAIN_NAME = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMjIENvbW1vbiBmbGFnczpcbiMgZGVtby11c2Vyc1xuIyBlbWFpbC12ZXJpZmljYXRpb25cbiMgbG9nLWVtYWlsc1xuIyBsb2ctaW52aXRhdGlvbi10b2tlbnNcbiMgbG9naW4td2l0aC1naXRodWJcbiMgbG9naW4td2l0aC1naXRsYWJcbiMgbG9naW4td2l0aC1nb29nbGVcbiMgbG9naW4td2l0aC1sZGFwXG4jIGxvZ2luLXdpdGgtb2lkY1xuIyBsb2dpbi13aXRoLXBhc3N3b3JkXG4jIHByZXBsLXNlcnZlclxuIyByZWdpc3RyYXRpb25cbiMgc2VjdXJlLXNlc3Npb24tY29va2llc1xuIyBzbXRwXG4jIHNtdHAtZGVidWdcbiMgdGVsZW1ldHJ5XG4jIHdlYmhvb2tzXG4jI1xuIyMgWW91IGNhbiByZWFkIG1vcmUgYWJvdXQgYWxsIGF2YWlsYWJsZSBmbGFncyBhbmQgb3RoZXJcbiMjIGVudmlyb25tZW50IHZhcmlhYmxlcyBoZXJlOlxuIyMgaHR0cHM6Ly9oZWxwLnBlbnBvdC5hcHAvdGVjaG5pY2FsLWd1aWRlL2NvbmZpZ3VyYXRpb24vI2FkdmFuY2VkLWNvbmZpZ3VyYXRpb25cbiNcbiMgV0FSTklORzogaWYgeW91J3JlIGV4cG9zaW5nIFBlbnBvdCB0byB0aGUgaW50ZXJuZXQsIHlvdSBzaG91bGQgcmVtb3ZlIHRoZSBmbGFnc1xuIyAnZGlzYWJsZS1zZWN1cmUtc2Vzc2lvbi1jb29raWVzJyBhbmQgJ2Rpc2FibGUtZW1haWwtdmVyaWZpY2F0aW9uJ1xuXG52b2x1bWVzOlxuICBwZW5wb3RfcG9zdGdyZXNfdjE1OlxuICBwZW5wb3RfYXNzZXRzOlxuICBwZW5wb3RfdHJhZWZpazpcbiAgIyBwZW5wb3RfbWluaW86XG5cbnNlcnZpY2VzOlxuXG4gIHBlbnBvdC1mcm9udGVuZDpcbiAgICBpbWFnZTogXCJwZW5wb3RhcHAvZnJvbnRlbmQ6Mi42LjFcIlxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIHBvcnRzOlxuICAgICAgLSA4MDgwXG4gICAgICAtIDkwMDFcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBlbnBvdF9hc3NldHM6L29wdC9kYXRhL2Fzc2V0c1xuXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcGVucG90LWJhY2tlbmRcbiAgICAgIC0gcGVucG90LWV4cG9ydGVyXG5cblxuXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQRU5QT1RfRkxBR1M6IGRpc2FibGUtZW1haWwtdmVyaWZpY2F0aW9uIGVuYWJsZS1zbXRwIGVuYWJsZS1wcmVwbC1zZXJ2ZXIgZGlzYWJsZS1zZWN1cmUtc2Vzc2lvbi1jb29raWVzXG5cbiAgcGVucG90LWJhY2tlbmQ6XG4gICAgaW1hZ2U6IFwicGVucG90YXBwL2JhY2tlbmQ6Mi42LjFcIlxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcGVucG90X2Fzc2V0czovb3B0L2RhdGEvYXNzZXRzXG5cbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBwZW5wb3QtcG9zdGdyZXNcbiAgICAgIC0gcGVucG90LXJlZGlzXG5cblxuXG4gICAgIyMgQ29uZmlndXJhdGlvbiBlbnZyb25tZW50IHZhcmlhYmxlcyBmb3IgdGhlIGJhY2tlbmRcbiAgICAjIyBjb250YWluZXIuXG5cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBFTlBPVF9QVUJMSUNfVVJJOiBodHRwOi8vJHtET01BSU5fTkFNRX1cbiAgICAgIFBFTlBPVF9GTEFHUzogZGlzYWJsZS1lbWFpbC12ZXJpZmljYXRpb24gZW5hYmxlLXNtdHAgZW5hYmxlLXByZXBsLXNlcnZlciBkaXNhYmxlLXNlY3VyZS1zZXNzaW9uLWNvb2tpZXNcblxuICAgICAgIyMgUGVucG90IFNFQ1JFVCBLRVkuIEl0IHNlcnZlcyBhcyBhIG1hc3RlciBrZXkgZnJvbSB3aGljaCBvdGhlciBrZXlzIGZvciBzdWJzeXN0ZW1zXG4gICAgICAjIyAoZWcgaHR0cCBzZXNzaW9ucywgb3IgaW52aXRhdGlvbnMpIGFyZSBkZXJpdmVkLlxuICAgICAgIyNcbiAgICAgICMjIElmIHlvdSBsZWF2ZSBpdCBjb21tZW50ZWQsIGFsbCBjcmVhdGVkIHNlc3Npb25zIGFuZCBpbnZpdGF0aW9ucyB3aWxsXG4gICAgICAjIyBiZWNvbWUgaW52YWxpZCBvbiBjb250YWluZXIgcmVzdGFydC5cbiAgICAgICMjXG4gICAgICAjIyBJZiB5b3UgZ29pbmcgdG8gdW5jb21tZW50IHRoaXMsIHdlIHJlY29tbWVuZCB0byB1c2UgYSB0cnVsbHkgcmFuZG9tbHkgZ2VuZXJhdGVkXG4gICAgICAjIyA1MTIgYml0cyBiYXNlNjQgZW5jb2RlZCBzdHJpbmcgaGVyZS4gIFlvdSBjYW4gZ2VuZXJhdGUgb25lIHdpdGg6XG4gICAgICAjI1xuICAgICAgIyMgcHl0aG9uMyAtYyBcImltcG9ydCBzZWNyZXRzOyBwcmludChzZWNyZXRzLnRva2VuX3VybHNhZmUoNjQpKVwiXG5cbiAgICAgICMgUEVOUE9UX1NFQ1JFVF9LRVk6IG15LWluc2VjdXJlLWtleVxuXG4gICAgICAjIyBUaGUgUFJFUEwgaG9zdC4gTWFpbmx5IHVzZWQgZm9yIGV4dGVybmFsIHByb2dyYW1hdGljIGFjY2VzcyB0byBwZW5wb3QgYmFja2VuZFxuICAgICAgIyMgKGV4YW1wbGU6IGFkbWluKS4gQnkgZGVmYXVsdCBpdCB3aWxsIGxpc3RlbiBvbiBgbG9jYWxob3N0YCBidXQgaWYgeW91IGFyZSBnb2luZyB0byB1c2VcbiAgICAgICMjIHRoZSBgYWRtaW5gLCB5b3Ugd2lsbCBuZWVkIHRvIHVuY29tbWVudCB0aGlzIGFuZCBzZXQgdGhlIGhvc3QgdG8gYDAuMC4wLjBgLlxuXG4gICAgICAjIFBFTlBPVF9QUkVQTF9IT1NUOiAwLjAuMC4wXG5cbiAgICAgICMjIERhdGFiYXNlIGNvbm5lY3Rpb24gcGFyYW1ldGVycy4gRG9uJ3QgdG91Y2ggdGhlbSB1bmxlc3MgeW91IGFyZSB1c2luZyBjdXN0b21cbiAgICAgICMjIHBvc3RncmVzcWwgY29ubmVjdGlvbiBwYXJhbWV0ZXJzLlxuXG4gICAgICBQRU5QT1RfREFUQUJBU0VfVVJJOiBwb3N0Z3Jlc3FsOi8vcGVucG90LXBvc3RncmVzL3BlbnBvdFxuICAgICAgUEVOUE9UX0RBVEFCQVNFX1VTRVJOQU1FOiBwZW5wb3RcbiAgICAgIFBFTlBPVF9EQVRBQkFTRV9QQVNTV09SRDogcGVucG90XG5cbiAgICAgICMjIFJlZGlzIGlzIHVzZWQgZm9yIHRoZSB3ZWJzb2NrZXRzIG5vdGlmaWNhdGlvbnMuIERvbid0IHRvdWNoIHVubGVzcyB0aGUgcmVkaXNcbiAgICAgICMjIGNvbnRhaW5lciBoYXMgZGlmZmVyZW50IHBhcmFtZXRlcnMgb3IgZGlmZmVyZW50IG5hbWUuXG5cbiAgICAgIFBFTlBPVF9SRURJU19VUkk6IHJlZGlzOi8vcGVucG90LXJlZGlzLzBcblxuICAgICAgIyMgRGVmYXVsdCBjb25maWd1cmF0aW9uIGZvciBhc3NldHMgc3RvcmFnZTogdXNpbmcgZmlsZXN5c3RlbSBiYXNlZCB3aXRoIGFsbCBmaWxlc1xuICAgICAgIyMgc3RvcmVkIGluIGEgZG9ja2VyIHZvbHVtZS5cblxuICAgICAgUEVOUE9UX0FTU0VUU19TVE9SQUdFX0JBQ0tFTkQ6IGFzc2V0cy1mc1xuICAgICAgUEVOUE9UX1NUT1JBR0VfQVNTRVRTX0ZTX0RJUkVDVE9SWTogL29wdC9kYXRhL2Fzc2V0c1xuXG4gICAgICAjIyBBbHNvIGNhbiBiZSBjb25maWd1cmVkIHRvIHRvIHVzZSBhIFMzIGNvbXBhdGlibGUgc3RvcmFnZVxuICAgICAgIyMgc2VydmljZSBsaWtlIE1pbmlJTy4gTG9vayBiZWxvdyBmb3IgbWluaW8gc2VydmljZSBzZXR1cC5cblxuICAgICAgIyBBV1NfQUNDRVNTX0tFWV9JRDogPEtFWV9JRD5cbiAgICAgICMgQVdTX1NFQ1JFVF9BQ0NFU1NfS0VZOiA8QUNDRVNTX0tFWT5cbiAgICAgICMgUEVOUE9UX0FTU0VUU19TVE9SQUdFX0JBQ0tFTkQ6IGFzc2V0cy1zM1xuICAgICAgIyBQRU5QT1RfU1RPUkFHRV9BU1NFVFNfUzNfRU5EUE9JTlQ6IGh0dHA6Ly9wZW5wb3QtbWluaW86OTAwMFxuICAgICAgIyBQRU5QT1RfU1RPUkFHRV9BU1NFVFNfUzNfQlVDS0VUOiA8QlVLRVRfTkFNRT5cblxuICAgICAgIyMgVGVsZW1ldHJ5LiBXaGVuIGVuYWJsZWQsIGEgcGVyaW9kaWNhbCBwcm9jZXNzIHdpbGwgc2VuZCBhbm9ueW1vdXMgZGF0YSBhYm91dCB0aGlzXG4gICAgICAjIyBpbnN0YW5jZS4gVGVsZW1ldHJ5IGRhdGEgd2lsbCBlbmFibGUgdXMgdG8gbGVhcm4gaG93IHRoZSBhcHBsaWNhdGlvbiBpcyB1c2VkLFxuICAgICAgIyMgYmFzZWQgb24gcmVhbCBzY2VuYXJpb3MuIElmIHlvdSB3YW50IHRvIGhlbHAgdXMsIHBsZWFzZSBsZWF2ZSBpdCBlbmFibGVkLiBZb3UgY2FuXG4gICAgICAjIyBhdWRpdCB3aGF0IGRhdGEgd2Ugc2VuZCB3aXRoIHRoZSBjb2RlIGF2YWlsYWJsZSBvbiBnaXRodWIuXG5cbiAgICAgIFBFTlBPVF9URUxFTUVUUllfRU5BQkxFRDogdHJ1ZVxuXG4gICAgICAjIyBFeGFtcGxlIFNNVFAvRW1haWwgY29uZmlndXJhdGlvbi4gQnkgZGVmYXVsdCwgZW1haWxzIGFyZSBzZW50IHRvIHRoZSBtYWlsY2F0Y2hcbiAgICAgICMjIHNlcnZpY2UsIGJ1dCBmb3IgcHJvZHVjdGlvbiB1c2FnZSBpdCBpcyByZWNvbW1lbmRlZCB0byBzZXR1cCBhIHJlYWwgU01UUFxuICAgICAgIyMgcHJvdmlkZXIuIEVtYWlscyBhcmUgdXNlZCB0byBjb25maXJtIHVzZXIgcmVnaXN0cmF0aW9ucyAmIGludml0YXRpb25zLiBMb29rIGJlbG93XG4gICAgICAjIyBob3cgdGhlIG1haWxjYXRjaCBzZXJ2aWNlIGlzIGNvbmZpZ3VyZWQuXG5cbiAgICAgIFBFTlBPVF9TTVRQX0RFRkFVTFRfRlJPTTogbm8tcmVwbHlAZXhhbXBsZS5jb21cbiAgICAgIFBFTlBPVF9TTVRQX0RFRkFVTFRfUkVQTFlfVE86IG5vLXJlcGx5QGV4YW1wbGUuY29tXG4gICAgICBQRU5QT1RfU01UUF9IT1NUOiBwZW5wb3QtbWFpbGNhdGNoXG4gICAgICBQRU5QT1RfU01UUF9QT1JUOiAxMDI1XG4gICAgICBQRU5QT1RfU01UUF9VU0VSTkFNRTpcbiAgICAgIFBFTlBPVF9TTVRQX1BBU1NXT1JEOlxuICAgICAgUEVOUE9UX1NNVFBfVExTOiBmYWxzZVxuICAgICAgUEVOUE9UX1NNVFBfU1NMOiBmYWxzZVxuXG4gIHBlbnBvdC1leHBvcnRlcjpcbiAgICBpbWFnZTogXCJwZW5wb3RhcHAvZXhwb3J0ZXI6Mi42LjFcIlxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuXG5cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgRG9uJ3QgdG91Y2ggaXQ7IHRoaXMgdXNlcyBhbiBpbnRlcm5hbCBkb2NrZXIgbmV0d29yayB0b1xuICAgICAgIyBjb21tdW5pY2F0ZSB3aXRoIHRoZSBmcm9udGVuZC5cbiAgICAgIFBFTlBPVF9QVUJMSUNfVVJJOiBodHRwOi8vcGVucG90LWZyb250ZW5kXG5cbiAgICAgICMjIFJlZGlzIGlzIHVzZWQgZm9yIHRoZSB3ZWJzb2NrZXRzIG5vdGlmaWNhdGlvbnMuXG4gICAgICBQRU5QT1RfUkVESVNfVVJJOiByZWRpczovL3BlbnBvdC1yZWRpcy8wXG5cbiAgcGVucG90LXBvc3RncmVzOlxuICAgIGltYWdlOiBcInBvc3RncmVzOjE1XCJcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBzdG9wX3NpZ25hbDogU0lHSU5UXG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSBwZW5wb3RfcG9zdGdyZXNfdjE1Oi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuXG5cblxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19JTklUREJfQVJHUz0tLWRhdGEtY2hlY2tzdW1zXG4gICAgICAtIFBPU1RHUkVTX0RCPXBlbnBvdFxuICAgICAgLSBQT1NUR1JFU19VU0VSPXBlbnBvdFxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD1wZW5wb3RcblxuICBwZW5wb3QtcmVkaXM6XG4gICAgaW1hZ2U6IHJlZGlzOjcuMlxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuXG5cbiAgIyMgQSBtYWlsY2F0Y2ggc2VydmljZSwgdXNlZCBhcyB0ZW1wb3JhbCBTTVRQIHNlcnZlci4gWW91IGNhbiBhY2Nlc3MgdmlhIEhUVFAgdG8gdGhlXG4gICMjIHBvcnQgMTA4MCBmb3IgcmVhZCBhbGwgZW1haWxzIHRoZSBwZW5wb3QgcGxhdGZvcm0gaGFzIHNlbnQuIFNob3VsZCBiZSBvbmx5IHVzZWQgYXMgYVxuICAjIyB0ZW1wb3JhbCBzb2x1dGlvbiB3aGlsZSBubyByZWFsIFNNVFAgcHJvdmlkZXIgaXMgY29uZmlndXJlZC5cblxuICBwZW5wb3QtbWFpbGNhdGNoOlxuICAgIGltYWdlOiBzajI2L21haWxjYXRjaGVyOmxhdGVzdFxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGV4cG9zZTpcbiAgICAgIC0gJzEwMjUnXG4gICAgcG9ydHM6XG4gICAgICAtIDEwODBcblxuXG4gICMjIEV4YW1wbGUgY29uZmlndXJhdGlvbiBvZiBNaW5pSU8gKFMzIGNvbXBhdGlibGUgb2JqZWN0IHN0b3JhZ2Ugc2VydmljZSk7IElmIHlvdSBkb24ndFxuICAjIyBoYXZlIHByZWZlcmVuY2UsIHRoZW4ganVzdCB1c2UgZmlsZXN5c3RlbSwgdGhpcyBpcyBoZXJlIGp1c3QgZm9yIHRoZSBjb21wbGV0ZW5lc3MuXG5cbiAgIyBtaW5pbzpcbiAgIyAgIGltYWdlOiBcIm1pbmlvL21pbmlvOmxhdGVzdFwiXG4gICMgICBjb21tYW5kOiBtaW5pbyBzZXJ2ZXIgL21udC9kYXRhIC0tY29uc29sZS1hZGRyZXNzIFwiOjkwMDFcIlxuICAjICAgcmVzdGFydDogYWx3YXlzXG4gICNcbiAgIyAgIHZvbHVtZXM6XG4gICMgICAgIC0gXCJwZW5wb3RfbWluaW86L21udC9kYXRhXCJcbiAgI1xuICAjICAgZW52aXJvbm1lbnQ6XG4gICMgICAgIC0gTUlOSU9fUk9PVF9VU0VSPW1pbmlvYWRtaW5cbiAgIyAgICAgLSBNSU5JT19ST09UX1BBU1NXT1JEPW1pbmlvYWRtaW5cbiAgI1xuICAjICAgcG9ydHM6XG4gICMgICAgIC0gOTAwMDo5MDAwXG4gICMgICAgIC0gOTAwMTo5MDAxXG5cblxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInBlbnBvdC1mcm9udGVuZFwiXG5wb3J0ID0gODA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkRPTUFJTl9OQU1FID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`design`,`collaboration`

---

Version:`2.3.2`

PeerDBData integration platform that synchronizes and federates data across databases with a unified API.

PeppermintPeppermint is a modern, open-source API development platform that helps you build, test and document your APIs.

### On this page

ConfigurationBase64LinksTags