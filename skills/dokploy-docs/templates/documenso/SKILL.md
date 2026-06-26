---
title: "Documenso | Dokploy"
source: "https://docs.dokploy.com/docs/templates/documenso"
category: dokploy-docs
created: "2026-06-25T17:21:46.245Z"
---

Documenso | Dokploy

# Documenso

Copy as Markdown

Documenso is the open source alternative to DocuSign for signing documents digitally

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  postgres:
    image: postgres:16

    volumes:
      - documenso-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=documenso
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=documenso
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U documenso"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s

  documenso:
    image: documenso/documenso:v1.12.10
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      - PORT=${DOCUMENSO_PORT}
      - NEXTAUTH_URL=http://${DOCUMENSO_HOST}
      - NEXTAUTH_SECRET=${NEXTAUTH_SECRET}
      - NEXT_PRIVATE_ENCRYPTION_KEY=${NEXT_PRIVATE_ENCRYPTION_KEY}
      - NEXT_PRIVATE_ENCRYPTION_SECONDARY_KEY=${NEXT_PRIVATE_ENCRYPTION_SECONDARY_KEY}
      - NEXT_PUBLIC_WEBAPP_URL=http://${DOCUMENSO_HOST}
      - NEXT_PRIVATE_DATABASE_URL=postgres://documenso:password@postgres:5432/documenso
      - NEXT_PRIVATE_DIRECT_DATABASE_URL=postgres://documenso:password@postgres:5432/documenso
      - NEXT_PUBLIC_UPLOAD_TRANSPORT=database
      - NEXT_PRIVATE_SMTP_TRANSPORT=smtp-auth
      - NEXT_PRIVATE_SIGNING_TRANSPORT=local
      - NEXT_PRIVATE_SIGNING_LOCAL_FILE_PATH=/app/certs/cert.p12
      - NEXT_PRIVATE_SIGNING_LOCAL_FILE_PASSPHRASE=${NEXT_PRIVATE_SIGNING_LOCAL_FILE_PASSPHRASE}
      - CERT_VALID_DAYS=${CERT_VALID_DAYS:-365}
      - CERT_INFO_COUNTRY_NAME=${CERT_INFO_COUNTRY_NAME:-US}
      - CERT_INFO_STATE_OR_PROVIDENCE=${CERT_INFO_STATE_OR_PROVIDENCE:-State}
      - CERT_INFO_LOCALITY_NAME=${CERT_INFO_LOCALITY_NAME:-City}
      - CERT_INFO_ORGANIZATION_NAME=${CERT_INFO_ORGANIZATION_NAME:-Organization}
      - CERT_INFO_ORGANIZATIONAL_UNIT=${CERT_INFO_ORGANIZATIONAL_UNIT:-IT Department}
      - CERT_INFO_EMAIL=${CERT_INFO_EMAIL:[email protected]}
      - DOCUMENSO_HOST=${DOCUMENSO_HOST}
    ports:
      - ${DOCUMENSO_PORT}
    entrypoint:
      - /bin/sh
      - -c
      - |
        CERT_PASSPHRASE="$${NEXT_PRIVATE_SIGNING_LOCAL_FILE_PASSPHRASE}"

        # Save original working directory
        ORIGINAL_DIR="$$(pwd)"

        # Find openssl binary (should be available in v1.12.10+)
        OPENSSL_CMD="$$(which openssl 2>/dev/null || command -v openssl 2>/dev/null || echo '/usr/bin/openssl')"

        # Verify openssl is available
        if ! $$OPENSSL_CMD version >/dev/null 2>&1; then
          echo "Error: OpenSSL not found. Please use Documenso image v1.12.10 or later."
          exit 1
        fi

        # Create certificate directory - use /app/certs (writable by user 1001)
        CERT_DIR="/app/certs"
        mkdir -p "$$CERT_DIR" || {
          # Fallback to tmp if app directory not writable
          CERT_DIR="/tmp/certs"
          mkdir -p "$$CERT_DIR"
          echo "Warning: Using fallback directory: $$CERT_DIR"
        }

        touch /tmp/cert_info_path
        cat <<EOF > /tmp/cert_info_path
        [ req ]
        distinguished_name = req_distinguished_name
        prompt = no
        [ req_distinguished_name ]
        C            = $${CERT_INFO_COUNTRY_NAME}
        ST           = $${CERT_INFO_STATE_OR_PROVIDENCE}
        L            = $${CERT_INFO_LOCALITY_NAME}
        O            = $${CERT_INFO_ORGANIZATION_NAME}
        OU           = $${CERT_INFO_ORGANIZATIONAL_UNIT}
        CN           = $${DOCUMENSO_HOST}
        emailAddress = $${CERT_INFO_EMAIL}
        EOF

        cd "$$CERT_DIR"

        $$OPENSSL_CMD genrsa -out private.key 2048

        $$OPENSSL_CMD req \
          -new \
          -x509 \
          -key private.key \
          -out certificate.crt \
          -days $${CERT_VALID_DAYS} \
          -config /tmp/cert_info_path

        $$OPENSSL_CMD pkcs12 \
          -export \
          -out cert.p12 \
          -inkey private.key \
          -in certificate.crt \
          -legacy \
          -passout pass:"$$CERT_PASSPHRASE"

        # Set permissions (may fail if not root, but will work in Coolify)
        chown 1001:1001 cert.p12 private.key certificate.crt 2>/dev/null || true
        chmod 400 cert.p12 private.key certificate.crt

        # Update environment variable if directory changed
        if [ "$$CERT_DIR" != "/app/certs" ]; then
          export NEXT_PRIVATE_SIGNING_LOCAL_FILE_PATH="$$CERT_DIR/cert.p12"
        fi

        # Return to original directory before starting application
        cd "$$ORIGINAL_DIR"

        ./start.sh

volumes:
  documenso-data:
```

```
[variables]
main_domain = "${domain}"
nextauth_secret = "${base64:32}"
encryption_key = "${password:32}"
secondary_encryption_key = "${password:64}"

[config]
env = [
  "DOCUMENSO_HOST=${main_domain}",
  "DOCUMENSO_PORT=3000",
  "NEXTAUTH_SECRET=${nextauth_secret}",
  "NEXT_PRIVATE_ENCRYPTION_KEY=${encryption_key}",
  "NEXT_PRIVATE_ENCRYPTION_SECONDARY_KEY=${secondary_encryption_key}",
]
mounts = []

[[config.domains]]
serviceName = "documenso"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTZcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRvY3VtZW5zby1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19VU0VSPWRvY3VtZW5zb1xuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD1wYXNzd29yZFxuICAgICAgLSBQT1NUR1JFU19EQj1kb2N1bWVuc29cbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgZG9jdW1lbnNvXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgICAgc3RhcnRfcGVyaW9kOiAxMHNcblxuICBkb2N1bWVuc286XG4gICAgaW1hZ2U6IGRvY3VtZW5zby9kb2N1bWVuc286djEuMTIuMTBcbiAgICBkZXBlbmRzX29uOlxuICAgICAgcG9zdGdyZXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPUlQ9JHtET0NVTUVOU09fUE9SVH1cbiAgICAgIC0gTkVYVEFVVEhfVVJMPWh0dHA6Ly8ke0RPQ1VNRU5TT19IT1NUfVxuICAgICAgLSBORVhUQVVUSF9TRUNSRVQ9JHtORVhUQVVUSF9TRUNSRVR9XG4gICAgICAtIE5FWFRfUFJJVkFURV9FTkNSWVBUSU9OX0tFWT0ke05FWFRfUFJJVkFURV9FTkNSWVBUSU9OX0tFWX1cbiAgICAgIC0gTkVYVF9QUklWQVRFX0VOQ1JZUFRJT05fU0VDT05EQVJZX0tFWT0ke05FWFRfUFJJVkFURV9FTkNSWVBUSU9OX1NFQ09OREFSWV9LRVl9XG4gICAgICAtIE5FWFRfUFVCTElDX1dFQkFQUF9VUkw9aHR0cDovLyR7RE9DVU1FTlNPX0hPU1R9XG4gICAgICAtIE5FWFRfUFJJVkFURV9EQVRBQkFTRV9VUkw9cG9zdGdyZXM6Ly9kb2N1bWVuc286cGFzc3dvcmRAcG9zdGdyZXM6NTQzMi9kb2N1bWVuc29cbiAgICAgIC0gTkVYVF9QUklWQVRFX0RJUkVDVF9EQVRBQkFTRV9VUkw9cG9zdGdyZXM6Ly9kb2N1bWVuc286cGFzc3dvcmRAcG9zdGdyZXM6NTQzMi9kb2N1bWVuc29cbiAgICAgIC0gTkVYVF9QVUJMSUNfVVBMT0FEX1RSQU5TUE9SVD1kYXRhYmFzZVxuICAgICAgLSBORVhUX1BSSVZBVEVfU01UUF9UUkFOU1BPUlQ9c210cC1hdXRoXG4gICAgICAtIE5FWFRfUFJJVkFURV9TSUdOSU5HX1RSQU5TUE9SVD1sb2NhbFxuICAgICAgLSBORVhUX1BSSVZBVEVfU0lHTklOR19MT0NBTF9GSUxFX1BBVEg9L2FwcC9jZXJ0cy9jZXJ0LnAxMlxuICAgICAgLSBORVhUX1BSSVZBVEVfU0lHTklOR19MT0NBTF9GSUxFX1BBU1NQSFJBU0U9JHtORVhUX1BSSVZBVEVfU0lHTklOR19MT0NBTF9GSUxFX1BBU1NQSFJBU0V9XG4gICAgICAtIENFUlRfVkFMSURfREFZUz0ke0NFUlRfVkFMSURfREFZUzotMzY1fVxuICAgICAgLSBDRVJUX0lORk9fQ09VTlRSWV9OQU1FPSR7Q0VSVF9JTkZPX0NPVU5UUllfTkFNRTotVVN9XG4gICAgICAtIENFUlRfSU5GT19TVEFURV9PUl9QUk9WSURFTkNFPSR7Q0VSVF9JTkZPX1NUQVRFX09SX1BST1ZJREVOQ0U6LVN0YXRlfVxuICAgICAgLSBDRVJUX0lORk9fTE9DQUxJVFlfTkFNRT0ke0NFUlRfSU5GT19MT0NBTElUWV9OQU1FOi1DaXR5fVxuICAgICAgLSBDRVJUX0lORk9fT1JHQU5JWkFUSU9OX05BTUU9JHtDRVJUX0lORk9fT1JHQU5JWkFUSU9OX05BTUU6LU9yZ2FuaXphdGlvbn1cbiAgICAgIC0gQ0VSVF9JTkZPX09SR0FOSVpBVElPTkFMX1VOSVQ9JHtDRVJUX0lORk9fT1JHQU5JWkFUSU9OQUxfVU5JVDotSVQgRGVwYXJ0bWVudH1cbiAgICAgIC0gQ0VSVF9JTkZPX0VNQUlMPSR7Q0VSVF9JTkZPX0VNQUlMOi1hZG1pbkBleGFtcGxlLmNvbX1cbiAgICAgIC0gRE9DVU1FTlNPX0hPU1Q9JHtET0NVTUVOU09fSE9TVH1cbiAgICBwb3J0czpcbiAgICAgIC0gJHtET0NVTUVOU09fUE9SVH1cbiAgICBlbnRyeXBvaW50OlxuICAgICAgLSAvYmluL3NoXG4gICAgICAtIC1jXG4gICAgICAtIHxcbiAgICAgICAgQ0VSVF9QQVNTUEhSQVNFPVwiJCR7TkVYVF9QUklWQVRFX1NJR05JTkdfTE9DQUxfRklMRV9QQVNTUEhSQVNFfVwiXG4gICAgICAgIFxuICAgICAgICAjIFNhdmUgb3JpZ2luYWwgd29ya2luZyBkaXJlY3RvcnlcbiAgICAgICAgT1JJR0lOQUxfRElSPVwiJCQocHdkKVwiXG4gICAgICAgIFxuICAgICAgICAjIEZpbmQgb3BlbnNzbCBiaW5hcnkgKHNob3VsZCBiZSBhdmFpbGFibGUgaW4gdjEuMTIuMTArKVxuICAgICAgICBPUEVOU1NMX0NNRD1cIiQkKHdoaWNoIG9wZW5zc2wgMj4vZGV2L251bGwgfHwgY29tbWFuZCAtdiBvcGVuc3NsIDI+L2Rldi9udWxsIHx8IGVjaG8gJy91c3IvYmluL29wZW5zc2wnKVwiXG4gICAgICAgIFxuICAgICAgICAjIFZlcmlmeSBvcGVuc3NsIGlzIGF2YWlsYWJsZVxuICAgICAgICBpZiAhICQkT1BFTlNTTF9DTUQgdmVyc2lvbiA+L2Rldi9udWxsIDI+JjE7IHRoZW5cbiAgICAgICAgICBlY2hvIFwiRXJyb3I6IE9wZW5TU0wgbm90IGZvdW5kLiBQbGVhc2UgdXNlIERvY3VtZW5zbyBpbWFnZSB2MS4xMi4xMCBvciBsYXRlci5cIlxuICAgICAgICAgIGV4aXQgMVxuICAgICAgICBmaVxuICAgICAgICBcbiAgICAgICAgIyBDcmVhdGUgY2VydGlmaWNhdGUgZGlyZWN0b3J5IC0gdXNlIC9hcHAvY2VydHMgKHdyaXRhYmxlIGJ5IHVzZXIgMTAwMSlcbiAgICAgICAgQ0VSVF9ESVI9XCIvYXBwL2NlcnRzXCJcbiAgICAgICAgbWtkaXIgLXAgXCIkJENFUlRfRElSXCIgfHwge1xuICAgICAgICAgICMgRmFsbGJhY2sgdG8gdG1wIGlmIGFwcCBkaXJlY3Rvcnkgbm90IHdyaXRhYmxlXG4gICAgICAgICAgQ0VSVF9ESVI9XCIvdG1wL2NlcnRzXCJcbiAgICAgICAgICBta2RpciAtcCBcIiQkQ0VSVF9ESVJcIlxuICAgICAgICAgIGVjaG8gXCJXYXJuaW5nOiBVc2luZyBmYWxsYmFjayBkaXJlY3Rvcnk6ICQkQ0VSVF9ESVJcIlxuICAgICAgICB9XG4gICAgICAgIFxuICAgICAgICB0b3VjaCAvdG1wL2NlcnRfaW5mb19wYXRoXG4gICAgICAgIGNhdCA8PEVPRiA+IC90bXAvY2VydF9pbmZvX3BhdGhcbiAgICAgICAgWyByZXEgXVxuICAgICAgICBkaXN0aW5ndWlzaGVkX25hbWUgPSByZXFfZGlzdGluZ3Vpc2hlZF9uYW1lXG4gICAgICAgIHByb21wdCA9IG5vXG4gICAgICAgIFsgcmVxX2Rpc3Rpbmd1aXNoZWRfbmFtZSBdXG4gICAgICAgIEMgICAgICAgICAgICA9ICQke0NFUlRfSU5GT19DT1VOVFJZX05BTUV9XG4gICAgICAgIFNUICAgICAgICAgICA9ICQke0NFUlRfSU5GT19TVEFURV9PUl9QUk9WSURFTkNFfVxuICAgICAgICBMICAgICAgICAgICAgPSAkJHtDRVJUX0lORk9fTE9DQUxJVFlfTkFNRX1cbiAgICAgICAgTyAgICAgICAgICAgID0gJCR7Q0VSVF9JTkZPX09SR0FOSVpBVElPTl9OQU1FfVxuICAgICAgICBPVSAgICAgICAgICAgPSAkJHtDRVJUX0lORk9fT1JHQU5JWkFUSU9OQUxfVU5JVH1cbiAgICAgICAgQ04gICAgICAgICAgID0gJCR7RE9DVU1FTlNPX0hPU1R9XG4gICAgICAgIGVtYWlsQWRkcmVzcyA9ICQke0NFUlRfSU5GT19FTUFJTH1cbiAgICAgICAgRU9GXG5cbiAgICAgICAgY2QgXCIkJENFUlRfRElSXCJcbiAgICAgICAgXG4gICAgICAgICQkT1BFTlNTTF9DTUQgZ2VucnNhIC1vdXQgcHJpdmF0ZS5rZXkgMjA0OFxuICAgICAgICBcbiAgICAgICAgJCRPUEVOU1NMX0NNRCByZXEgXFxcbiAgICAgICAgICAtbmV3IFxcXG4gICAgICAgICAgLXg1MDkgXFxcbiAgICAgICAgICAta2V5IHByaXZhdGUua2V5IFxcXG4gICAgICAgICAgLW91dCBjZXJ0aWZpY2F0ZS5jcnQgXFxcbiAgICAgICAgICAtZGF5cyAkJHtDRVJUX1ZBTElEX0RBWVN9IFxcXG4gICAgICAgICAgLWNvbmZpZyAvdG1wL2NlcnRfaW5mb19wYXRoXG4gICAgICAgIFxuICAgICAgICAkJE9QRU5TU0xfQ01EIHBrY3MxMiBcXFxuICAgICAgICAgIC1leHBvcnQgXFxcbiAgICAgICAgICAtb3V0IGNlcnQucDEyIFxcXG4gICAgICAgICAgLWlua2V5IHByaXZhdGUua2V5IFxcXG4gICAgICAgICAgLWluIGNlcnRpZmljYXRlLmNydCBcXFxuICAgICAgICAgIC1sZWdhY3kgXFxcbiAgICAgICAgICAtcGFzc291dCBwYXNzOlwiJCRDRVJUX1BBU1NQSFJBU0VcIlxuICAgICAgICBcbiAgICAgICAgIyBTZXQgcGVybWlzc2lvbnMgKG1heSBmYWlsIGlmIG5vdCByb290LCBidXQgd2lsbCB3b3JrIGluIENvb2xpZnkpXG4gICAgICAgIGNob3duIDEwMDE6MTAwMSBjZXJ0LnAxMiBwcml2YXRlLmtleSBjZXJ0aWZpY2F0ZS5jcnQgMj4vZGV2L251bGwgfHwgdHJ1ZVxuICAgICAgICBjaG1vZCA0MDAgY2VydC5wMTIgcHJpdmF0ZS5rZXkgY2VydGlmaWNhdGUuY3J0XG4gICAgICAgIFxuICAgICAgICAjIFVwZGF0ZSBlbnZpcm9ubWVudCB2YXJpYWJsZSBpZiBkaXJlY3RvcnkgY2hhbmdlZFxuICAgICAgICBpZiBbIFwiJCRDRVJUX0RJUlwiICE9IFwiL2FwcC9jZXJ0c1wiIF07IHRoZW5cbiAgICAgICAgICBleHBvcnQgTkVYVF9QUklWQVRFX1NJR05JTkdfTE9DQUxfRklMRV9QQVRIPVwiJCRDRVJUX0RJUi9jZXJ0LnAxMlwiXG4gICAgICAgIGZpXG4gICAgICAgIFxuICAgICAgICAjIFJldHVybiB0byBvcmlnaW5hbCBkaXJlY3RvcnkgYmVmb3JlIHN0YXJ0aW5nIGFwcGxpY2F0aW9uXG4gICAgICAgIGNkIFwiJCRPUklHSU5BTF9ESVJcIlxuICAgICAgICBcbiAgICAgICAgLi9zdGFydC5zaFxuXG52b2x1bWVzOlxuICBkb2N1bWVuc28tZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5uZXh0YXV0aF9zZWNyZXQgPSBcIiR7YmFzZTY0OjMyfVwiXG5lbmNyeXB0aW9uX2tleSA9IFwiJHtwYXNzd29yZDozMn1cIlxuc2Vjb25kYXJ5X2VuY3J5cHRpb25fa2V5ID0gXCIke3Bhc3N3b3JkOjY0fVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiRE9DVU1FTlNPX0hPU1Q9JHttYWluX2RvbWFpbn1cIixcbiAgXCJET0NVTUVOU09fUE9SVD0zMDAwXCIsXG4gIFwiTkVYVEFVVEhfU0VDUkVUPSR7bmV4dGF1dGhfc2VjcmV0fVwiLFxuICBcIk5FWFRfUFJJVkFURV9FTkNSWVBUSU9OX0tFWT0ke2VuY3J5cHRpb25fa2V5fVwiLFxuICBcIk5FWFRfUFJJVkFURV9FTkNSWVBUSU9OX1NFQ09OREFSWV9LRVk9JHtzZWNvbmRhcnlfZW5jcnlwdGlvbl9rZXl9XCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJkb2N1bWVuc29cIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`document-signing`

---

Version:`v1.5.6`

DocmostDocmost, is an open-source collaborative wiki and documentation software.

DocusealDocuseal is a self-hosted document management system.

### On this page

ConfigurationBase64LinksTags