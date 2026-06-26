---
title: "Google Cloud Storage | Dokploy"
source: "https://docs.dokploy.com/docs/core/cloud-storage"
category: dokploy-docs
created: "2026-06-25T17:16:11.091Z"
---

Google Cloud Storage | Dokploy

S3 Destinations

# Google Cloud Storage

Copy as Markdown

Configure Google Cloud Storage buckets for backup storage. This includes setting up access keys, secret keys, bucket names, regions, and endpoints.

Google Cloud Storage provides a simple and cost-effective way to store and retrieve data. It is a cloud-based service that allows you to store and retrieve data from anywhere in the world. This is a great option for storing backups, as it is easy to set up and manage.

1. Navigate to the Cloud Storage console and create a new bucket with preferred name.
2. Navigate to the IAM & Admin and create a new service account. Assign a role`Storage Admin` to the service account.
3. Return to Cloud Storage again, and click`Settings` on the left navigation menu.
4. Click`Interoperability` tab. This is where you will create Amazon S3-compatible ID and access keys.
5. Copy the value in`Storage URI`. You will need this for the Endpoint value in Dokploy.
6. Under`Service account HMAC`, click`Create a key for a service account`. Select the service account you created earlier and click`Create`. You will get an Access Key and a Secret Key.

Now copy the following variables:

| (from) Cloud Storage | (to) Dokploy | Example value |
| --- | --- | --- |
| `Access Key` | `Access Key ID` | `f3811c6d27415a9s6cv943b6743ad784` |
| `Secret` | `Secret Access Key` | `aa55ee40b4049e93b7252bf698408cc22a3c2856d2530s7c1cb7670e318f15e58` |
| `Location` | `Region` | `us-central1, etc` it will depend on the region you are using. |
| `Endpoint` | `Endpoint` | `https://storage.googleapis.com`. The value in`Storage URI`. |
| `Bucket Name` | `Bucket` | `dokploy-backups` use the name of the bucket you created. |

Test the connection and you should see a success message.

Backblaze B2Configure buckets from Backblaze B2 for backup storage. This includes setting up access keys, secret keys, bucket names, regions, and endpoints.

Cloudflare R2Configure R2 buckets for backup storage. This includes setting up access keys, secret keys, bucket names, regions, and endpoints.