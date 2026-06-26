---
title: "Reset Password & 2FA | Dokploy"
source: "https://docs.dokploy.com/docs/core/reset-password"
category: dokploy-docs
created: "2026-06-25T17:21:39.216Z"
---

Reset Password & 2FA | Dokploy

# Reset Password & 2FA

Copy as Markdown

Reset your password to access your Dokploy account and disable 2FA.

## Reset Password

To reset your password, follow these steps:

Log in to your VPS.

Run the command below to get the container ID of the dokploy container.

```
docker ps
```

Run command below to open a shell in the dokploy container.

```
 docker exec -it <container-id> bash -c "pnpm run reset-password"
```

It will display a random password. Copy it and use it to access again to the dashboard.

## Reset 2FA

To disable 2FA, follow these steps:

To reset your 2FA, follow these steps:

Log in to your VPS.

Run the command below to get the container ID of the dokploy container.

```
docker ps
```

Run command below to open a shell in the dokploy container.

```
 docker exec -it <container-id> bash -c "pnpm run reset-2fa"
```

You can now login again without having to supply a 2FA code.

Manual InstallationLearn how to manually install Dokploy on your server.

UninstallLearn how to uninstall Dokploy on your server

### On this page

Reset PasswordReset 2FA