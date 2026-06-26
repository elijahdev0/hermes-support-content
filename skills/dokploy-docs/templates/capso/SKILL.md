---
title: "Cap.so | Dokploy"
source: "https://docs.dokploy.com/docs/templates/capso"
category: dokploy-docs
created: "2026-06-25T17:21:42.678Z"
---

Cap.so | Dokploy

# Cap.so

Copy as Markdown

Cap.so is a platform for web and desktop applications with MySQL and S3 storage. It provides a complete development environment with database and file storage capabilities.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  cap-web:
    image: ghcr.io/capsoftware/cap-web:latest
    restart: unless-stopped
    environment:
      DATABASE_URL: 'mysql://${MYSQL_USER}:${MYSQL_PASSWORD}@ps-mysql:3306/${MYSQL_DATABASE}?ssl={"rejectUnauthorized":false}'
      WEB_URL: "http://${DOMAIN}:3000"
      NEXTAUTH_URL: "http://${DOMAIN}:3000"
      DATABASE_ENCRYPTION_KEY: ${DATABASE_ENCRYPTION_KEY}
      NEXTAUTH_SECRET: ${NEXTAUTH_SECRET}
      CAP_AWS_ACCESS_KEY: ${CAP_AWS_ACCESS_KEY}
      CAP_AWS_SECRET_KEY: ${CAP_AWS_SECRET_KEY}
      CAP_AWS_BUCKET: ${CAP_AWS_BUCKET}
      CAP_AWS_REGION: ${CAP_AWS_REGION}
      S3_PUBLIC_ENDPOINT: "http://${DOMAIN}:3902"
      S3_INTERNAL_ENDPOINT: "http://minio:3902"
    expose:
      - 3000
    depends_on:
      - ps-mysql
      - minio

  ps-mysql:
    image: mysql:8.0
    restart: unless-stopped
    environment:
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_ROOT_HOST: "%"
    command:
      - --max_connections=1000
      - --default-authentication-plugin=mysql_native_password
    expose:
      - 3306
    volumes:
      - ps-mysql:/var/lib/mysql

  minio:
    image: quay.io/minio/minio:RELEASE.2025-05-24T17-08-30Z
    restart: unless-stopped
    command: server /bitnami/minio/data --address ":3902" --console-address ":3903"
    environment:
      MINIO_ROOT_USER: ${MINIO_ROOT_USER}
      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD}
    expose:
      - 3902
      - 3903
    volumes:
      - minio-data:/bitnami/minio/data
      - minio-certs:/certs
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3902/minio/health/ready"]
      interval: 30s
      timeout: 20s
      retries: 3

volumes:
  ps-mysql:
    driver: local
  minio-data:
    driver: local
  minio-certs:
    driver: local
```

```
[variables]
main_domain = "${domain}"
minio_domain_1 = "${domain}"
minio_domain_2 = "${domain}"
mysql_database = "planetscale"
mysql_user = "root"
cap_aws_bucket = "capso"
cap_aws_region = "us-east-1"

[config]
[[config.domains]]
serviceName = "cap-web"
port = 3000
host = "${main_domain}"
path = "/"

[[config.domains]]
serviceName = "minio"
port = 3902
host = "minio_domain_1"
path = "/"

[[config.domains]]
serviceName = "minio"
port = 3903
host = "minio_domain_2"
path = "/"

[config.env]
DOMAIN = "${main_domain}"
MYSQL_DATABASE = "${mysql_database}"
MYSQL_USER = "${mysql_user}"
MYSQL_PASSWORD = "${password:32}" # Password for MySQL user
MYSQL_ROOT_PASSWORD = "${password:32}" # Password for MySQL root user
DATABASE_ENCRYPTION_KEY = "${password:32}" # Encryption key for database
NEXTAUTH_SECRET = "${password:32}" # Secret for NextAuth authentication
CAP_AWS_ACCESS_KEY = "${password:16}" # Access key for S3/MinIO
CAP_AWS_SECRET_KEY = "${password:16}" # Secret key for S3/MinIO
CAP_AWS_BUCKET = "${cap_aws_bucket}"
CAP_AWS_REGION = "${cap_aws_region}"
MINIO_ROOT_USER = "${password:16}" # MinIO root user
MINIO_ROOT_PASSWORD = "${password:16}" # MinIO root password

[[config.mounts]]
filePath = "/certs"
content = ""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBjYXAtd2ViOlxuICAgIGltYWdlOiBnaGNyLmlvL2NhcHNvZnR3YXJlL2NhcC13ZWI6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERBVEFCQVNFX1VSTDogJ215c3FsOi8vJHtNWVNRTF9VU0VSfToke01ZU1FMX1BBU1NXT1JEfUBwcy1teXNxbDozMzA2LyR7TVlTUUxfREFUQUJBU0V9P3NzbD17XCJyZWplY3RVbmF1dGhvcml6ZWRcIjpmYWxzZX0nXG4gICAgICBXRUJfVVJMOiBcImh0dHA6Ly8ke0RPTUFJTn06MzAwMFwiXG4gICAgICBORVhUQVVUSF9VUkw6IFwiaHR0cDovLyR7RE9NQUlOfTozMDAwXCJcbiAgICAgIERBVEFCQVNFX0VOQ1JZUFRJT05fS0VZOiAke0RBVEFCQVNFX0VOQ1JZUFRJT05fS0VZfVxuICAgICAgTkVYVEFVVEhfU0VDUkVUOiAke05FWFRBVVRIX1NFQ1JFVH1cbiAgICAgIENBUF9BV1NfQUNDRVNTX0tFWTogJHtDQVBfQVdTX0FDQ0VTU19LRVl9XG4gICAgICBDQVBfQVdTX1NFQ1JFVF9LRVk6ICR7Q0FQX0FXU19TRUNSRVRfS0VZfVxuICAgICAgQ0FQX0FXU19CVUNLRVQ6ICR7Q0FQX0FXU19CVUNLRVR9XG4gICAgICBDQVBfQVdTX1JFR0lPTjogJHtDQVBfQVdTX1JFR0lPTn1cbiAgICAgIFMzX1BVQkxJQ19FTkRQT0lOVDogXCJodHRwOi8vJHtET01BSU59OjM5MDJcIlxuICAgICAgUzNfSU5URVJOQUxfRU5EUE9JTlQ6IFwiaHR0cDovL21pbmlvOjM5MDJcIlxuICAgIGV4cG9zZTpcbiAgICAgIC0gMzAwMFxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHBzLW15c3FsXG4gICAgICAtIG1pbmlvXG5cbiAgcHMtbXlzcWw6XG4gICAgaW1hZ2U6IG15c3FsOjguMFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNWVNRTF9EQVRBQkFTRTogJHtNWVNRTF9EQVRBQkFTRX1cbiAgICAgIE1ZU1FMX1JPT1RfUEFTU1dPUkQ6ICR7TVlTUUxfUk9PVF9QQVNTV09SRH1cbiAgICAgIE1ZU1FMX1JPT1RfSE9TVDogXCIlXCJcbiAgICBjb21tYW5kOlxuICAgICAgLSAtLW1heF9jb25uZWN0aW9ucz0xMDAwXG4gICAgICAtIC0tZGVmYXVsdC1hdXRoZW50aWNhdGlvbi1wbHVnaW49bXlzcWxfbmF0aXZlX3Bhc3N3b3JkXG4gICAgZXhwb3NlOlxuICAgICAgLSAzMzA2XG4gICAgdm9sdW1lczpcbiAgICAgIC0gcHMtbXlzcWw6L3Zhci9saWIvbXlzcWxcblxuICBtaW5pbzpcbiAgICBpbWFnZTogcXVheS5pby9taW5pby9taW5pbzpSRUxFQVNFLjIwMjUtMDUtMjRUMTctMDgtMzBaXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBjb21tYW5kOiBzZXJ2ZXIgL2JpdG5hbWkvbWluaW8vZGF0YSAtLWFkZHJlc3MgXCI6MzkwMlwiIC0tY29uc29sZS1hZGRyZXNzIFwiOjM5MDNcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgTUlOSU9fUk9PVF9VU0VSOiAke01JTklPX1JPT1RfVVNFUn1cbiAgICAgIE1JTklPX1JPT1RfUEFTU1dPUkQ6ICR7TUlOSU9fUk9PVF9QQVNTV09SRH1cbiAgICBleHBvc2U6XG4gICAgICAtIDM5MDJcbiAgICAgIC0gMzkwM1xuICAgIHZvbHVtZXM6XG4gICAgICAtIG1pbmlvLWRhdGE6L2JpdG5hbWkvbWluaW8vZGF0YVxuICAgICAgLSBtaW5pby1jZXJ0czovY2VydHNcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcImN1cmxcIiwgXCItZlwiLCBcImh0dHA6Ly9sb2NhbGhvc3Q6MzkwMi9taW5pby9oZWFsdGgvcmVhZHlcIl1cbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDIwc1xuICAgICAgcmV0cmllczogM1xuXG52b2x1bWVzOlxuICBwcy1teXNxbDpcbiAgICBkcml2ZXI6IGxvY2FsXG4gIG1pbmlvLWRhdGE6XG4gICAgZHJpdmVyOiBsb2NhbFxuICBtaW5pby1jZXJ0czpcbiAgICBkcml2ZXI6IGxvY2FsXG4iLAogICJjb25maWciOiAiIFt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbm1pbmlvX2RvbWFpbl8xID0gXCIke2RvbWFpbn1cIlxubWluaW9fZG9tYWluXzIgPSBcIiR7ZG9tYWlufVwiXG5teXNxbF9kYXRhYmFzZSA9IFwicGxhbmV0c2NhbGVcIlxubXlzcWxfdXNlciA9IFwicm9vdFwiXG5jYXBfYXdzX2J1Y2tldCA9IFwiY2Fwc29cIlxuY2FwX2F3c19yZWdpb24gPSBcInVzLWVhc3QtMVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjYXAtd2ViXCJcbnBvcnQgPSAzMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5wYXRoID0gXCIvXCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibWluaW9cIlxucG9ydCA9IDM5MDJcbmhvc3QgPSBcIm1pbmlvX2RvbWFpbl8xXCJcbnBhdGggPSBcIi9cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJtaW5pb1wiXG5wb3J0ID0gMzkwM1xuaG9zdCA9IFwibWluaW9fZG9tYWluXzJcIlxucGF0aCA9IFwiL1wiXG5cbltjb25maWcuZW52XVxuRE9NQUlOID0gXCIke21haW5fZG9tYWlufVwiXG5NWVNRTF9EQVRBQkFTRSA9IFwiJHtteXNxbF9kYXRhYmFzZX1cIlxuTVlTUUxfVVNFUiA9IFwiJHtteXNxbF91c2VyfVwiXG5NWVNRTF9QQVNTV09SRCA9IFwiJHtwYXNzd29yZDozMn1cIiAjIFBhc3N3b3JkIGZvciBNeVNRTCB1c2VyXG5NWVNRTF9ST09UX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjMyfVwiICMgUGFzc3dvcmQgZm9yIE15U1FMIHJvb3QgdXNlclxuREFUQUJBU0VfRU5DUllQVElPTl9LRVkgPSBcIiR7cGFzc3dvcmQ6MzJ9XCIgIyBFbmNyeXB0aW9uIGtleSBmb3IgZGF0YWJhc2Vcbk5FWFRBVVRIX1NFQ1JFVCA9IFwiJHtwYXNzd29yZDozMn1cIiAjIFNlY3JldCBmb3IgTmV4dEF1dGggYXV0aGVudGljYXRpb25cbkNBUF9BV1NfQUNDRVNTX0tFWSA9IFwiJHtwYXNzd29yZDoxNn1cIiAjIEFjY2VzcyBrZXkgZm9yIFMzL01pbklPXG5DQVBfQVdTX1NFQ1JFVF9LRVkgPSBcIiR7cGFzc3dvcmQ6MTZ9XCIgIyBTZWNyZXQga2V5IGZvciBTMy9NaW5JT1xuQ0FQX0FXU19CVUNLRVQgPSBcIiR7Y2FwX2F3c19idWNrZXR9XCJcbkNBUF9BV1NfUkVHSU9OID0gXCIke2NhcF9hd3NfcmVnaW9ufVwiXG5NSU5JT19ST09UX1VTRVIgPSBcIiR7cGFzc3dvcmQ6MTZ9XCIgIyBNaW5JTyByb290IHVzZXJcbk1JTklPX1JPT1RfUEFTU1dPUkQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCIgIyBNaW5JTyByb290IHBhc3N3b3JkXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL2NlcnRzXCJcbmNvbnRlbnQgPSBcIlwiIgp9
```

## Links

`web`,`s3`,`mysql`,`development`,`self-hosted`

---

Version:`latest`

Calibre-WebCalibre-Web is a web app providing a clean interface for browsing, reading, and managing your eBooks library using an existing Calibre database.

CarboneCarbone is a high-performance, self-hosted document generation engine. It allows you to generate reports, invoices, and documents in various formats (e.g., PDF, DOCX, XLSX) using JSON data and template-based rendering.

### On this page

ConfigurationBase64LinksTags