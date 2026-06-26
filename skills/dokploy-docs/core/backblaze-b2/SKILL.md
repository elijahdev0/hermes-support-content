---
title: "Backblaze B2 | Dokploy"
source: "https://docs.dokploy.com/docs/core/backblaze-b2"
category: dokploy-docs
created: "2026-06-25T17:16:11.090Z"
---

Backblaze B2 | Dokploy

S3 Destinations

# Backblaze B2

Copy as Markdown

Configure buckets from Backblaze B2 for backup storage. This includes setting up access keys, secret keys, bucket names, regions, and endpoints.

Backblaze B2 is a cloud-based service that allows you to store and retrieve data from anywhere in the world. This is a great option for storing backups, as it is easy to set up and manage.

## Backblaze B2 Example Bucket

1. Create a new bucket and set any name you want.
2. Go to`Application Keys` and create a new key.
3. Set a Key Name.
4. Set the Allow Access to Bucket(s) to`All Buckets` or`Specific Buckets`.
5. Set type of access`Read & Write` Permission.

Now copy the following variables:

- `Access Key`->`Access Key (Dokploy)`= eg.`002s6acf2639910000d000005`
- `Secret Key`->`Secret Key (Dokploy)`= eg.`K00+rIsWqPMhmcgqcyOyb9bqby7pbpE`
- `Region`->`Region (Dokploy)`= eg.`eu-central-003, us-east-005, us-west-002, us-west-001, us-west-004, etc` it will depend on the region you are using.
- `Endpoint`->`Endpoint (Dokploy)`= eg.`https://s3.us-west-002.backblazeb2.com` you will find this endpoint in the Bucket Card at the Home Page.
- `Bucket`->`Bucket (Dokploy)`= eg.`dokploy-backups` use the name of the bucket you created.

Test the connection and you should see a success message.

AWS S3Configure S3 buckets for backup storage. This includes setting up access keys, secret keys, bucket names, regions, and endpoints.

Google Cloud StorageConfigure Google Cloud Storage buckets for backup storage. This includes setting up access keys, secret keys, bucket names, regions, and endpoints.

### On this page

Backblaze B2 Example Bucket