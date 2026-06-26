---
title: "Double Zero | Dokploy"
source: "https://docs.dokploy.com/docs/templates/doublezero"
category: dokploy-docs
created: "2026-06-25T17:21:46.246Z"
---

Double Zero | Dokploy

# Double Zero

Copy as Markdown

00 is a self hostable SES dashboard for sending and monitoring emails with AWS

## Configuration

docker-compose.ymltemplate.toml

```
services:
  doublezero:
    restart: always
    image: liltechnomancer/double-zero:0.2.1
    volumes:
      - db-data:/var/lib/doublezero/data
    environment:
      AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID}
      AWS_SECRET_ACCESS_KEY: ${AWS_SECRET_ACCESS_KEY}
      AWS_REGION: ${AWS_REGION}
      SQS_URL: ${SQS_URL}
      SYSTEM_EMAIL: ${SYSTEM_EMAIL}
      SECRET_KEY_BASE: ${SECRET_KEY_BASE}
      PHX_HOST: ${DOUBLEZERO_HOST}
      DATABASE_PATH: ./00.db

volumes:
  db-data:
    driver: local
```

```
[variables]
main_domain = "${domain}"
secret_key_base = "${base64:64}"

[config]
env = [
  "DOUBLEZERO_HOST=${main_domain}",
  "DOUBLEZERO_PORT=4000",
  "SECRET_KEY_BASE=${secret_key_base}",
  "AWS_ACCESS_KEY_ID=your-aws-access-key",
  "AWS_SECRET_ACCESS_KEY=your-aws-secret-key",
  "AWS_REGION=your-aws-region",
  "SQS_URL=your-aws-sqs-url",
  "SYSTEM_EMAIL=",
]
mounts = []

[[config.domains]]
serviceName = "doublezero"
port = 4_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkb3VibGV6ZXJvOlxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGltYWdlOiBsaWx0ZWNobm9tYW5jZXIvZG91YmxlLXplcm86MC4yLjFcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYi1kYXRhOi92YXIvbGliL2RvdWJsZXplcm8vZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgQVdTX0FDQ0VTU19LRVlfSUQ6ICR7QVdTX0FDQ0VTU19LRVlfSUR9XG4gICAgICBBV1NfU0VDUkVUX0FDQ0VTU19LRVk6ICR7QVdTX1NFQ1JFVF9BQ0NFU1NfS0VZfVxuICAgICAgQVdTX1JFR0lPTjogJHtBV1NfUkVHSU9OfVxuICAgICAgU1FTX1VSTDogJHtTUVNfVVJMfVxuICAgICAgU1lTVEVNX0VNQUlMOiAke1NZU1RFTV9FTUFJTH1cbiAgICAgIFNFQ1JFVF9LRVlfQkFTRTogJHtTRUNSRVRfS0VZX0JBU0V9XG4gICAgICBQSFhfSE9TVDogJHtET1VCTEVaRVJPX0hPU1R9XG4gICAgICBEQVRBQkFTRV9QQVRIOiAuLzAwLmRiXG5cbnZvbHVtZXM6XG4gIGRiLWRhdGE6XG4gICAgZHJpdmVyOiBsb2NhbFxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnNlY3JldF9rZXlfYmFzZSA9IFwiJHtiYXNlNjQ6NjR9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJET1VCTEVaRVJPX0hPU1Q9JHttYWluX2RvbWFpbn1cIixcbiAgXCJET1VCTEVaRVJPX1BPUlQ9NDAwMFwiLFxuICBcIlNFQ1JFVF9LRVlfQkFTRT0ke3NlY3JldF9rZXlfYmFzZX1cIixcbiAgXCJBV1NfQUNDRVNTX0tFWV9JRD15b3VyLWF3cy1hY2Nlc3Mta2V5XCIsXG4gIFwiQVdTX1NFQ1JFVF9BQ0NFU1NfS0VZPXlvdXItYXdzLXNlY3JldC1rZXlcIixcbiAgXCJBV1NfUkVHSU9OPXlvdXItYXdzLXJlZ2lvblwiLFxuICBcIlNRU19VUkw9eW91ci1hd3Mtc3FzLXVybFwiLFxuICBcIlNZU1RFTV9FTUFJTD1cIixcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImRvdWJsZXplcm9cIlxucG9ydCA9IDRfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`email`

---

Version:`v0.2.1`

Domain LockerDomain Locker is an open-source tool for tracking domain expirations and sending renewal reminders.

DozzleDozzle is a lightweight, real-time log viewer for Docker containers.

### On this page

ConfigurationBase64LinksTags