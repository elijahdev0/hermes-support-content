---
title: "Registry | Dokploy"
source: "https://docs.dokploy.com/docs/core/registry"
category: dokploy-docs
created: "2026-06-25T17:21:38.073Z"
---

Registry | Dokploy

# Registry

Copy as Markdown

Configure your registry settings to store your images and artifacts.

Dokploy offers a UI to connect to any Docker Registry.

## Registry Settings

You need to fill the form with the following details:

- Registry Name: Enter a name for your registry eg.`My Registry`.
- Username: Enter the username you want to use to connect to your registry.
- Password: Enter the password you want to use to connect to your registry.
- Image Prefix(Optional): Useful when using Cluster feature, to tag your images with a prefix eg.`dokploy` will convert to`dokploy/my-app:latest`.
- Registry URL: Enter the URL of your registry eg.`https://index.docker.io/v1`.

This approach allows you to authenticate and store your credentials on the machine, making it convenient when using multiple applications. You won't need to provide credentials for each one individually. It also enables seamless login to remote servers. If no server is selected, Dokploy will default to using its own server.

WebhookConfigure webhook notifications for your applications.

Digital OceanConfigure a Digital Ocean Container Registry to store your images and artifacts.

### On this page

Registry Settings