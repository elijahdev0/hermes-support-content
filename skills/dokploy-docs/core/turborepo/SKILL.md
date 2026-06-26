---
title: "Turborepo | Dokploy"
source: "https://docs.dokploy.com/docs/core/turborepo"
category: dokploy-docs
created: "2026-06-25T17:21:39.216Z"
---

Turborepo | Dokploy

Examples

# Turborepo

Copy as Markdown

Deploy a simple Turborepo application.

This repository contains an example of turborepo application that is deployed on Dokploy.

Use Git Provider in Your Application:

- Repository:`https://github.com/Dokploy/examples.git`
- Branch:`main`
- Build path:`/turborepo`(Nixpacks)

Environment Variables:

- Add environment variables to the env tab.

```
NIXPACKS_TURBO_APP_NAME="web"
NIXPACKS_BUILD_CMD="turbo run build --filter=web"
NIXPACKS_START_CMD="turbo run start --filter=web"
```

Click on Deploy:

- Deploy your application by clicking the deploy button.

Generate a Domain:

Click on generate domain button.

A new domain will be generated for you.

Set Port`3000`

You can use this domain to access your application.

If you need further assistance, join our Discord server.

TanstackDeploy a simple Tanstack application.

Vite ReactDeploy a simple Vite React application.