---
title: "Deployments | Dokploy"
source: "https://docs.dokploy.com/docs/core/remote-servers/deployments"
category: dokploy-docs
created: "2026-06-25T17:21:38.073Z"
---

Deployments | Dokploy

# Deployments

Copy as Markdown

Configure and set up your remote server deployment

To get started with remote servers, you'll need to configure the initial setup for your remote server.

## Server Setup

The server setup process prepares the necessary environment for securely and efficiently deploying applications.

Important

Root access to the server is required. We currently do not support non-root deployments.

If your remote server is configured with a different shell (other than bash), you must configure bash as the default shell, as Dokploy has been developed and tested with bash.

We provide two main actions to configure your server:

- Modify Script: Allows you to view and customize the installation script that will be executed on your server. You can adjust it according to your specific needs.
- Setup Server: Initiates the configuration process on the remote server. When clicked, it will open a modal window showing real-time logs of the script execution.

Example of the server setup logs:

Build ServerLearn how to configure a custom build server to compile your applications separately from your deployment servers.

SecuritySecurity features of Dokploy

### On this page

Server Setup