---
title: "Docker Hub | Dokploy"
source: "https://docs.dokploy.com/docs/core/registry/dockerhub"
category: dokploy-docs
created: "2026-06-25T17:21:38.073Z"
---

Docker Hub | Dokploy

# Docker Hub

Copy as Markdown

Configure Docker Hub to store your images and artifacts.

To configure a Docker Hub registry, you need to fill the form with the following details:

1. Insert the Registry Name eg.`My Registry`.
2. Insert the Username eg.`dockerhub_username`.
3. Insert the Password, you can use your own dockerhub password or generate a token here`https://app.docker.com/settings/personal-access-tokens`
4. Click on Generate Token.
5. Insert the Token Description eg.`dockerhub_token`.
6. In permissions make sure to select`Read` and`Write`.
7. Click on`Create`.
8. Copy the`access token` and paste it in Dokploy`Docker Hub` Modal section.
9. (Optional) If you pretend to use Cluster Feature, make sure to set a`Image Prefix` and`Registry URL`.
10. Click on`Test` to make sure everything is working.
11. Click on`Create` to save the registry.

Digital OceanConfigure a Digital Ocean Container Registry to store your images and artifacts.

GHCRConfigure GitHub Container Registry to store your images and artifacts.