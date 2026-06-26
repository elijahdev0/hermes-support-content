---
title: "Formbricks | Dokploy"
source: "https://docs.dokploy.com/docs/templates/formbricks"
category: dokploy-docs
created: "2026-06-25T17:21:48.521Z"
---

Formbricks | Dokploy

# Formbricks

Copy as Markdown

Formbricks is an open-source survey and form platform for collecting user data.

## Configuration

docker-compose.ymltemplate.toml

```
x-environment: &environment
  environment:
    WEBAPP_URL: ${WEBAPP_URL}
    NEXTAUTH_URL: ${NEXTAUTH_URL}
    DATABASE_URL: "postgresql://postgres:postgres@postgres:5432/formbricks?schema=public"
    NEXTAUTH_SECRET: ${NEXTAUTH_SECRET}
    ENCRYPTION_KEY: ${ENCRYPTION_KEY}
    CRON_SECRET: ${CRON_SECRET}
    EMAIL_VERIFICATION_DISABLED: 1
    PASSWORD_RESET_DISABLED: 1
    S3_FORCE_PATH_STYLE: 0

services:
  postgres:
    restart: always
    image: pgvector/pgvector:pg17
    volumes:
      - postgres:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=postgres

  formbricks:
    restart: always
    image: ghcr.io/formbricks/formbricks:v3.1.5
    depends_on:
      - postgres
    ports:
      - 3000
    volumes:
      - ../files/uploads:/home/nextjs/apps/web/uploads/
    <<: *environment

volumes:
  postgres:
    driver: local
  uploads:
```

```
[variables]
main_domain = "${domain}"
secret_base = "${base64:64}"
encryption_key = "${password:32}"
cron_secret = "${base64:32}"

[config]
env = [
  "WEBAPP_URL=http://${main_domain}",
  "NEXTAUTH_URL=http://${main_domain}",
  "NEXTAUTH_SECRET=${secret_base}",
  "ENCRYPTION_KEY=${encryption_key}",
  "CRON_SECRET=${cron_secret}",
]
mounts = []

[[config.domains]]
serviceName = "formbricks"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIngtZW52aXJvbm1lbnQ6ICZlbnZpcm9ubWVudFxuICBlbnZpcm9ubWVudDpcbiAgICBXRUJBUFBfVVJMOiAke1dFQkFQUF9VUkx9XG4gICAgTkVYVEFVVEhfVVJMOiAke05FWFRBVVRIX1VSTH1cbiAgICBEQVRBQkFTRV9VUkw6IFwicG9zdGdyZXNxbDovL3Bvc3RncmVzOnBvc3RncmVzQHBvc3RncmVzOjU0MzIvZm9ybWJyaWNrcz9zY2hlbWE9cHVibGljXCJcbiAgICBORVhUQVVUSF9TRUNSRVQ6ICR7TkVYVEFVVEhfU0VDUkVUfVxuICAgIEVOQ1JZUFRJT05fS0VZOiAke0VOQ1JZUFRJT05fS0VZfVxuICAgIENST05fU0VDUkVUOiAke0NST05fU0VDUkVUfVxuICAgIEVNQUlMX1ZFUklGSUNBVElPTl9ESVNBQkxFRDogMVxuICAgIFBBU1NXT1JEX1JFU0VUX0RJU0FCTEVEOiAxXG4gICAgUzNfRk9SQ0VfUEFUSF9TVFlMRTogMFxuXG5zZXJ2aWNlczpcbiAgcG9zdGdyZXM6XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgaW1hZ2U6IHBndmVjdG9yL3BndmVjdG9yOnBnMTdcbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3JlczovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkQ9cG9zdGdyZXNcblxuXG4gIGZvcm1icmlja3M6XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgaW1hZ2U6IGdoY3IuaW8vZm9ybWJyaWNrcy9mb3JtYnJpY2tzOnYzLjEuNVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHBvc3RncmVzXG4gICAgcG9ydHM6XG4gICAgICAtIDMwMDBcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy91cGxvYWRzOi9ob21lL25leHRqcy9hcHBzL3dlYi91cGxvYWRzL1xuICAgIDw8OiAqZW52aXJvbm1lbnRcblxudm9sdW1lczpcbiAgcG9zdGdyZXM6XG4gICAgZHJpdmVyOiBsb2NhbFxuICB1cGxvYWRzOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnNlY3JldF9iYXNlID0gXCIke2Jhc2U2NDo2NH1cIlxuZW5jcnlwdGlvbl9rZXkgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmNyb25fc2VjcmV0ID0gXCIke2Jhc2U2NDozMn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICBcIldFQkFQUF9VUkw9aHR0cDovLyR7bWFpbl9kb21haW59XCIsXG4gIFwiTkVYVEFVVEhfVVJMPWh0dHA6Ly8ke21haW5fZG9tYWlufVwiLFxuICBcIk5FWFRBVVRIX1NFQ1JFVD0ke3NlY3JldF9iYXNlfVwiLFxuICBcIkVOQ1JZUFRJT05fS0VZPSR7ZW5jcnlwdGlvbl9rZXl9XCIsXG4gIFwiQ1JPTl9TRUNSRVQ9JHtjcm9uX3NlY3JldH1cIixcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImZvcm1icmlja3NcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`forms`,`analytics`

---

Version:`v3.1.3`

ForgejoForgejo is a self-hosted lightweight software forge. Easy to install and low maintenance, it just does the job

Frappe HRFeature rich HR & Payroll software. 100% FOSS and customizable.

### On this page

ConfigurationBase64LinksTags