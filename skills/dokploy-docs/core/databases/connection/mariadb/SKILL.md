---
title: "MariaDB | Dokploy"
source: "https://docs.dokploy.com/docs/core/databases/connection/mariadb"
category: dokploy-docs
created: "2026-06-25T17:16:11.091Z"
---

MariaDB | Dokploy

# MariaDB

Copy as Markdown

This guide will cover how to connect from Beekeeper Studio to your mariadb databases in dokploy.

1. Download and install Beekeeper Studio Beekeeper Studio.
2. Go to your`mariadb` databases.
3. In External Credentials, enter the`External Port (Internet)` make sure the port is not in use by another service eg.`3307` and click`Save`.
4. It will display the`External Connection URL` eg. [email protected]`mysql://user::3306/database`.

Open Beekeeper Studio and follow the steps:

1. Click on`Add New Server`.
2. Select`MariaDB` as the`Database Type`.
3. Use`Import URL` to enter the`External Connection URL` from Dokploy eg. [email protected]`mysql://user::3306/database`.
4. Click on`Connect`.
5. Click on`Save`.

Done! now you can manage the database from Beekeeper Studio.

ConnectionLearn how to connect to your database using Dokploy.

Mongo CompassThis guide will cover how to configure a Mongo Compass connection for your applications in dokploy or panel.