---
title: "Flagsmith | Dokploy"
source: "https://docs.dokploy.com/docs/templates/flagsmith"
category: dokploy-docs
created: "2026-06-25T17:21:47.359Z"
---

Flagsmith | Dokploy

# Flagsmith

Copy as Markdown

Flagsmith is an open-source feature flagging and remote config service.

## Configuration

docker-compose.ymltemplate.toml

```
# See https://docs.flagsmith.com/deployment/docker for more information on running Flagsmith in Docker
# This Docker Compose file will run the entire Flagsmith Platform

volumes:
  pgdata:

services:
  postgres:
    image: postgres:15.5-alpine
    environment:
      POSTGRES_PASSWORD: ${DATABASE_PASSWORD}
      POSTGRES_DB: flagsmith
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -d flagsmith -U postgres"]
      interval: 2s
      timeout: 2s
      retries: 20
      start_period: 20s

  flagsmith:
    image: docker.flagsmith.com/flagsmith/flagsmith:2.177.1
    environment:
      # All environments variables are available here:
      # API: https://docs.flagsmith.com/deployment/locally-api#environment-variables
      # UI: https://docs.flagsmith.com/deployment/locally-frontend#environment-variables

      DATABASE_URL: postgresql://postgres:${DATABASE_PASSWORD}@postgres:5432/flagsmith
      USE_POSTGRES_FOR_ANALYTICS: "true" # Store API and Flag Analytics data in Postgres

      ENVIRONMENT: production # set to 'production' in production.
      DJANGO_ALLOWED_HOSTS: "*" # Change this in production
      FLAGSMITH_DOMAIN: ${FLAGSMITH_DOMAIN:-localhost:8000} # Change this in production
      DJANGO_SECRET_KEY: ${DJANGO_SECRET_KEY} # Change this in production
      # PREVENT_SIGNUP: 'true' # Uncomment to prevent additional signups
      # ALLOW_REGISTRATION_WITHOUT_INVITE: 'true'

      # Enable Task Processor
      TASK_RUN_METHOD: TASK_PROCESSOR # other options are: SYNCHRONOUSLY, SEPARATE_THREAD (default)
      PROMETHEUS_ENABLED: "true"

      # Uncomment if you want to enable Google OAuth. Note this does not turn Google OAuth on. You still need to use
      # Flagsmith on Flagsmith to enable it - https://docs.flagsmith.com/deployment/#oauth_google
      # DJANGO_SECURE_CROSS_ORIGIN_OPENER_POLICY: 'same-origin-allow-popups'

      # For more info on configuring E-Mails - https://docs.flagsmith.com/deployment/locally-api#environment-variables
      # Example SMTP:
      # EMAIL_BACKEND: django.core.mail.backends.smtp.EmailBackend
      # EMAIL_HOST: mail.example.com
      # SENDER_EMAIL: [email protected]
      # EMAIL_HOST_USER: [email protected]
      # EMAIL_HOST_PASSWORD: smtp_account_password
      # EMAIL_PORT: 587 # optional
      # EMAIL_USE_TLS: 'true' # optional
    ports:
      - 8000
    depends_on:
      postgres:
        condition: service_healthy

  # The flagsmith_processor service is only needed if TASK_RUN_METHOD set to TASK_PROCESSOR
  # in the application environment
  flagsmith-task-processor:
    image: docker.flagsmith.com/flagsmith/flagsmith:2.177.1
    environment:
      DATABASE_URL: postgresql://postgres:${DATABASE_PASSWORD}@postgres:5432/flagsmith
      USE_POSTGRES_FOR_ANALYTICS: "true"
      DJANGO_ALLOWED_HOSTS: "*"
      PROMETHEUS_ENABLED: "true"
    ports:
      - 8000
    depends_on:
      - flagsmith
    command: run-task-processor
```

```
[variables]
main_domain = "${domain}"
django_secret_key = "${password:8}"
database_password = "${password:16}"

[config]
env = [
  "DATABASE_PASSWORD=${database_password}",
  "DJANGO_SECRET_KEY=${django_secret_key}",
  "FLAGSMITH_DOMAIN=${main_domain}",
]
mounts = []

[[config.domains]]
serviceName = "flagsmith"
port = 8_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgU2VlIGh0dHBzOi8vZG9jcy5mbGFnc21pdGguY29tL2RlcGxveW1lbnQvZG9ja2VyIGZvciBtb3JlIGluZm9ybWF0aW9uIG9uIHJ1bm5pbmcgRmxhZ3NtaXRoIGluIERvY2tlclxuIyBUaGlzIERvY2tlciBDb21wb3NlIGZpbGUgd2lsbCBydW4gdGhlIGVudGlyZSBGbGFnc21pdGggUGxhdGZvcm1cblxudm9sdW1lczpcbiAgcGdkYXRhOlxuXG5cbnNlcnZpY2VzOlxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTUuNS1hbHBpbmVcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke0RBVEFCQVNFX1BBU1NXT1JEfVxuICAgICAgUE9TVEdSRVNfREI6IGZsYWdzbWl0aFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBnZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLWQgZmxhZ3NtaXRoIC1VIHBvc3RncmVzXCJdXG4gICAgICBpbnRlcnZhbDogMnNcbiAgICAgIHRpbWVvdXQ6IDJzXG4gICAgICByZXRyaWVzOiAyMFxuICAgICAgc3RhcnRfcGVyaW9kOiAyMHNcblxuICBmbGFnc21pdGg6XG4gICAgaW1hZ2U6IGRvY2tlci5mbGFnc21pdGguY29tL2ZsYWdzbWl0aC9mbGFnc21pdGg6Mi4xNzcuMVxuICAgIGVudmlyb25tZW50OlxuICAgICAgIyBBbGwgZW52aXJvbm1lbnRzIHZhcmlhYmxlcyBhcmUgYXZhaWxhYmxlIGhlcmU6XG4gICAgICAjIEFQSTogaHR0cHM6Ly9kb2NzLmZsYWdzbWl0aC5jb20vZGVwbG95bWVudC9sb2NhbGx5LWFwaSNlbnZpcm9ubWVudC12YXJpYWJsZXNcbiAgICAgICMgVUk6IGh0dHBzOi8vZG9jcy5mbGFnc21pdGguY29tL2RlcGxveW1lbnQvbG9jYWxseS1mcm9udGVuZCNlbnZpcm9ubWVudC12YXJpYWJsZXNcblxuICAgICAgREFUQUJBU0VfVVJMOiBwb3N0Z3Jlc3FsOi8vcG9zdGdyZXM6JHtEQVRBQkFTRV9QQVNTV09SRH1AcG9zdGdyZXM6NTQzMi9mbGFnc21pdGhcbiAgICAgIFVTRV9QT1NUR1JFU19GT1JfQU5BTFlUSUNTOiBcInRydWVcIiAjIFN0b3JlIEFQSSBhbmQgRmxhZyBBbmFseXRpY3MgZGF0YSBpbiBQb3N0Z3Jlc1xuXG4gICAgICBFTlZJUk9OTUVOVDogcHJvZHVjdGlvbiAjIHNldCB0byAncHJvZHVjdGlvbicgaW4gcHJvZHVjdGlvbi5cbiAgICAgIERKQU5HT19BTExPV0VEX0hPU1RTOiBcIipcIiAjIENoYW5nZSB0aGlzIGluIHByb2R1Y3Rpb25cbiAgICAgIEZMQUdTTUlUSF9ET01BSU46ICR7RkxBR1NNSVRIX0RPTUFJTjotbG9jYWxob3N0OjgwMDB9ICMgQ2hhbmdlIHRoaXMgaW4gcHJvZHVjdGlvblxuICAgICAgREpBTkdPX1NFQ1JFVF9LRVk6ICR7REpBTkdPX1NFQ1JFVF9LRVl9ICMgQ2hhbmdlIHRoaXMgaW4gcHJvZHVjdGlvblxuICAgICAgIyBQUkVWRU5UX1NJR05VUDogJ3RydWUnICMgVW5jb21tZW50IHRvIHByZXZlbnQgYWRkaXRpb25hbCBzaWdudXBzXG4gICAgICAjIEFMTE9XX1JFR0lTVFJBVElPTl9XSVRIT1VUX0lOVklURTogJ3RydWUnXG5cbiAgICAgICMgRW5hYmxlIFRhc2sgUHJvY2Vzc29yXG4gICAgICBUQVNLX1JVTl9NRVRIT0Q6IFRBU0tfUFJPQ0VTU09SICMgb3RoZXIgb3B0aW9ucyBhcmU6IFNZTkNIUk9OT1VTTFksIFNFUEFSQVRFX1RIUkVBRCAoZGVmYXVsdClcbiAgICAgIFBST01FVEhFVVNfRU5BQkxFRDogXCJ0cnVlXCJcblxuICAgICAgIyBVbmNvbW1lbnQgaWYgeW91IHdhbnQgdG8gZW5hYmxlIEdvb2dsZSBPQXV0aC4gTm90ZSB0aGlzIGRvZXMgbm90IHR1cm4gR29vZ2xlIE9BdXRoIG9uLiBZb3Ugc3RpbGwgbmVlZCB0byB1c2VcbiAgICAgICMgRmxhZ3NtaXRoIG9uIEZsYWdzbWl0aCB0byBlbmFibGUgaXQgLSBodHRwczovL2RvY3MuZmxhZ3NtaXRoLmNvbS9kZXBsb3ltZW50LyNvYXV0aF9nb29nbGVcbiAgICAgICMgREpBTkdPX1NFQ1VSRV9DUk9TU19PUklHSU5fT1BFTkVSX1BPTElDWTogJ3NhbWUtb3JpZ2luLWFsbG93LXBvcHVwcydcblxuICAgICAgIyBGb3IgbW9yZSBpbmZvIG9uIGNvbmZpZ3VyaW5nIEUtTWFpbHMgLSBodHRwczovL2RvY3MuZmxhZ3NtaXRoLmNvbS9kZXBsb3ltZW50L2xvY2FsbHktYXBpI2Vudmlyb25tZW50LXZhcmlhYmxlc1xuICAgICAgIyBFeGFtcGxlIFNNVFA6XG4gICAgICAjIEVNQUlMX0JBQ0tFTkQ6IGRqYW5nby5jb3JlLm1haWwuYmFja2VuZHMuc210cC5FbWFpbEJhY2tlbmRcbiAgICAgICMgRU1BSUxfSE9TVDogbWFpbC5leGFtcGxlLmNvbVxuICAgICAgIyBTRU5ERVJfRU1BSUw6IGZsYWdzbWl0aEBleGFtcGxlLmNvbVxuICAgICAgIyBFTUFJTF9IT1NUX1VTRVI6IGZsYWdzbWl0aEBleGFtcGxlLmNvbVxuICAgICAgIyBFTUFJTF9IT1NUX1BBU1NXT1JEOiBzbXRwX2FjY291bnRfcGFzc3dvcmRcbiAgICAgICMgRU1BSUxfUE9SVDogNTg3ICMgb3B0aW9uYWxcbiAgICAgICMgRU1BSUxfVVNFX1RMUzogJ3RydWUnICMgb3B0aW9uYWxcbiAgICBwb3J0czpcbiAgICAgIC0gODAwMFxuICAgIGRlcGVuZHNfb246XG4gICAgICBwb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcblxuICAjIFRoZSBmbGFnc21pdGhfcHJvY2Vzc29yIHNlcnZpY2UgaXMgb25seSBuZWVkZWQgaWYgVEFTS19SVU5fTUVUSE9EIHNldCB0byBUQVNLX1BST0NFU1NPUlxuICAjIGluIHRoZSBhcHBsaWNhdGlvbiBlbnZpcm9ubWVudFxuICBmbGFnc21pdGgtdGFzay1wcm9jZXNzb3I6XG4gICAgaW1hZ2U6IGRvY2tlci5mbGFnc21pdGguY29tL2ZsYWdzbWl0aC9mbGFnc21pdGg6Mi4xNzcuMVxuICAgIGVudmlyb25tZW50OlxuICAgICAgREFUQUJBU0VfVVJMOiBwb3N0Z3Jlc3FsOi8vcG9zdGdyZXM6JHtEQVRBQkFTRV9QQVNTV09SRH1AcG9zdGdyZXM6NTQzMi9mbGFnc21pdGhcbiAgICAgIFVTRV9QT1NUR1JFU19GT1JfQU5BTFlUSUNTOiBcInRydWVcIlxuICAgICAgREpBTkdPX0FMTE9XRURfSE9TVFM6IFwiKlwiXG4gICAgICBQUk9NRVRIRVVTX0VOQUJMRUQ6IFwidHJ1ZVwiXG4gICAgcG9ydHM6XG4gICAgICAtIDgwMDBcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBmbGFnc21pdGhcbiAgICBjb21tYW5kOiBydW4tdGFzay1wcm9jZXNzb3JcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5kamFuZ29fc2VjcmV0X2tleSA9IFwiJHtwYXNzd29yZDo4fVwiXG5kYXRhYmFzZV9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoxNn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICBcIkRBVEFCQVNFX1BBU1NXT1JEPSR7ZGF0YWJhc2VfcGFzc3dvcmR9XCIsXG4gIFwiREpBTkdPX1NFQ1JFVF9LRVk9JHtkamFuZ29fc2VjcmV0X2tleX1cIixcbiAgXCJGTEFHU01JVEhfRE9NQUlOPSR7bWFpbl9kb21haW59XCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJmbGFnc21pdGhcIlxucG9ydCA9IDhfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`feature-flag`,`feature-management`,`feature-toggle`,`remote-configuration`

---

Version:`2.177.1`

FiveM ServerA modded GTA V multiplayer server with optional txAdmin web interface for easy server management.

FlareSolverrFlareSolverr is a proxy server to bypass Cloudflare and DDoS-GUARD protection.

### On this page

ConfigurationBase64LinksTags