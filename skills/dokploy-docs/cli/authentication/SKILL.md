---
title: "Authentication | Dokploy"
source: "https://docs.dokploy.com/docs/cli/authentication"
category: dokploy-docs
created: "2026-06-25T17:16:08.647Z"
---

Authentication | Dokploy

# Authentication

Copy as Markdown

A guide to authenticating with the Dokploy CLI

The Dokploy CLI uses a token-based authentication system. To authenticate, you'll need to create an access token and store it securely.

## Creating an Access Token

To create an access token, first you need to have permissions if you are admin you don't need permissions.

by default access token never expires.

You can go to`dashboard/settings/profile` and click on the`Generate` button.

## Storing the Access Token

Dokploy when you create an access token automatically will generate a config.json with the access token and the server url.

## Commands

1. `dokploy authenticate`- Authenticate with the Dokploy CLI.
2. `dokploy verify`- Verify if the access token is valid.

ApplicationA guide to using the Dokploy CLI to manage applications

DatabasesA guide to using the Dokploy CLI to manage databases

### On this page

Creating an Access TokenStoring the Access TokenCommands