---
title: "AWS S3 | Dokploy"
source: "https://docs.dokploy.com/docs/core/aws-s3"
category: dokploy-docs
created: "2026-06-25T17:16:11.090Z"
---

AWS S3 | Dokploy

S3 Destinations

# AWS S3

Copy as Markdown

Configure S3 buckets for backup storage. This includes setting up access keys, secret keys, bucket names, regions, and endpoints.

AWS provides a simple and cost-effective way to store and retrieve data. It is a cloud-based service that allows you to store and retrieve data from anywhere in the world. This is a great option for storing backups, as it is easy to set up and manage.

1. Create a new bucket and set any name you want.
2. Search for`IAM` in the search bar.
3. Click on`Policies` in the left menu.
4. Click on`Create Policy`.
5. Select`JSON` and paste the following policy: Make sure to replace the bucket name with your bucket name.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowListBucket",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::bucket-name"
    },
    {
      "Sid": "AllowBucketObjectActions",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      // Make sure to set the name of your bucket
      "Resource": "arn:aws:s3:::bucket-name/*"
    }
  ]
}
```

1. Click on`Review Policy`.
2. Assign a name to the policy.
3. Click on`Create Policy`.
4. Click on User Group and assign a Name.
5. Click on`Add User to Group`.
6. Add the user you want to assign to the group.
7. In the`Attached Policies` section, filter by type`Customer Managed` and select the policy you created.
8. Click on`Attach Policy`.
9. Go to`Users` and select the user you've assigned to the group.
10. Go to Security Credentials.
11. Click on`Create Access Key`.
12. Select`Programmatic Access`.
13. Click on`Create New Access Key`.

Now copy the following variables:

- `Access Key`->`Access Key (Dokploy)`= eg.`AK2AV244NFLS5JTUZ554`
- `Secret Key`->`Secret Key (Dokploy)`= eg.`I0GWCo9fSGOr7z6Lh+NvHmSsaE+62Vwk2ua2CEwR`
- `Bucket`->`Bucket (Dokploy)`= eg.`dokploy-backups` use the name of the bucket you created.
- `Region`->`Region (Dokploy)`= eg.`us-east-1, us-west-2, etc` it will depend on the region you are using.
- `Endpoint`->`Endpoint (Dokploy) (Optional)`= eg.`https://s3..amazonaws.com` you will find this endpoint in the Bucket Card at the Home Page.

Test the connection and you should see a success message.

Backblaze B2Configure buckets from Backblaze B2 for backup storage. This includes setting up access keys, secret keys, bucket names, regions, and endpoints.