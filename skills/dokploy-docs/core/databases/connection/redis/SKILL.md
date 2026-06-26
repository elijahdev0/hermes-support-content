---
title: "Redis | Dokploy"
source: "https://docs.dokploy.com/docs/core/databases/connection/redis"
category: dokploy-docs
created: "2026-06-25T17:16:11.091Z"
---

Redis | Dokploy

# Redis

Copy as Markdown

This guide will cover how to connect from RedisInsight to your redis databases in dokploy.

1. Download and install RedisInsight RedisInsight.
2. Go to your`redis` databases.
3. In External Credentials, enter the`External Port (Internet)` make sure the port is not in use by another service eg.`6379` and click`Save`.
4. It will display the`External Connection URL` eg. [email protected]`redis://user::6379/database`.

Open RedisInsight and follow the steps:

1. Add Redis Database.
2. Enter the`Host` eg.`1.2.4.5`.
3. Enter the`Port` eg.`6379`.
4. Enter the username eg.`default`.
5. Enter the`Password` eg.`password`.
6. Click on`Save`.

Done! now you can manage the database from RedisInsight.

PG AdminThis guide will cover how to connect from pgAdmin to your postgres databases in dokploy.

11tyDeploy a simple 11ty application.