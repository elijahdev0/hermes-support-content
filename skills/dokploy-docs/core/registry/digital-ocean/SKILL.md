---
title: "Digital Ocean | Dokploy"
source: "https://docs.dokploy.com/docs/core/registry/digital-ocean"
category: dokploy-docs
created: "2026-06-25T17:21:38.073Z"
---

Digital Ocean | Dokploy

# Digital Ocean

Copy as Markdown

Configure a Digital Ocean Container Registry to store your images and artifacts.

To configure a Digital Ocean Container Registry, you need to fill the form with the following details:

1. Insert the Registry Name eg.`My Registry`.
2. Go to`https://cloud.digitalocean.com/registry/new` and click on`Create a Container Registry`.
3. Insert a lowercase name eg.`dokploy-username`.
4. Click on`Create Registry`.
5. Click on`Actions` and then`Download Docker Credentials`.
6. In Permissions select`Read` and`Write`.
7. Open the downloaded file and copy the auth value and type as`Password` in Dokploy Modal.
8. Go to`https://cloud.digitalocean.com/account/api/tokens` and click on`Generate New Token`.
9. In permissions select`Registry`.
10. Click on`Create`.
11. Copy the`access token` and paste it in Dokploy Modal as a`Username` field.
12. (Optional) If you pretend to use Cluster Feature, make sure to set a`Image Prefix`.
13. Registry URL: set`registry.digitalocean.com`
14. Click on`Test` to make sure everything is working.
15. Click on`Create` to save the registry.

RegistryConfigure your registry settings to store your images and artifacts.

Docker HubConfigure Docker Hub to store your images and artifacts.