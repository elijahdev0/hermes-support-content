---
title: "Connection | Dokploy"
source: "https://docs.dokploy.com/docs/core/databases/connection"
category: dokploy-docs
created: "2026-06-25T17:16:11.091Z"
---

Connection | Dokploy

Databases

# Connection

Copy as Markdown

Learn how to connect to your database using Dokploy.

This section explains how to configure database access for applications in Dokploy, including both internal connections within your network and external connections accessible over the internet.

### Internal Credentials

Used for connecting to the database from within the same network, without exposing the database to the internet.

- User: Username for the database access.
- Password: Secure password for database access.
- Database Name: The name of the database to connect to.
- Internal Host: The hostname or internal identifier for the database within the network.
- Internal Port (Container): The port used within the container to connect to the database.
- Internal Connection URL: The full connection string used internally to connect to the database.

### External Credentials

Enables the database to be reachable from the internet, necessary for remote management or external applications.

- External Port (Internet): Assign a port that is not currently used by another service to expose the database externally.

#### Steps to Configure External Access

1. Ensure the external port is available and not in conflict with other services.
2. Enter the external port you wish to use to expose your database.
3. The system will automatically generate an external connection URL, which can be used to access the database from any database management tool over the internet, like phpMyAdmin, MySQL Workbench, PgAdmin, etc.

### Important Note

For security reasons, internal credentials should be used for applications running within the same network or environment to prevent unauthorized access. External credentials should only be used when necessary and with proper security measures in place, such as VPNs or IP whitelisting.

RestoreLearn how to restore your databases in Dokploy, with options for restoring from S3 buckets.

MariaDBThis guide will cover how to connect from Beekeeper Studio to your mariadb databases in dokploy.

### On this page

Internal CredentialsExternal CredentialsSteps to Configure External AccessImportant Note