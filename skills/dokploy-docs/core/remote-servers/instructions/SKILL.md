---
title: "Deploy Server | Dokploy"
source: "https://docs.dokploy.com/docs/core/remote-servers/instructions"
category: dokploy-docs
created: "2026-06-25T17:21:38.073Z"
---

Deploy Server | Dokploy

# Deploy Server

Copy as Markdown

Step-by-step guide to setup a remote server and deploy applications on a VPS.

Remote servers allows you to deploy your apps remotely to different servers without needing to build and run them where the Dokploy UI is installed.

## Requirements

1. To install Dokploy UI, follow the installation guide.

If your remote server is configured with a different shell (other than bash), you must configure bash as the default shell, as Dokploy has been developed and tested with bash.

Create an SSH key by going to`/dashboard/settings/ssh-keys` and add a new key. Be sure to copy the public key.

Decide which remote server to deploy your apps on. We recommend these reliable providers:

When creating the server, it should ask for SSH keys. Ideally, use your computer's public key and the key you generated in the previous step. Here's how to add the public key in Hostinger:

The steps are similar across other providers.

Copy the server’s IP address and ensure you know the username (often`root`). Fill in all fields and click`Create`.

To test connectivity, open the server dropdown and click`Enter Terminal`. If everything is correct, you should be able to interact with the remote server.

Click`Setup Server` to proceed. There are two tabs: SSH Keys and Deployments. This guide explains the easy way, but you can follow the manual process via the Dokploy UI if you prefer.

Click`Deployments`, then`Setup Server`. If everything is correct, you should see output similar to this:

You only need to run this setup once. If Dokploy updates later, check the release notes to see if rerunning this command is required.

You're ready to deploy your apps! Let's test it out:

To check which server an app belongs to, you’ll see the server name at the top. If no server is selected, it defaults to`Dokploy Server`. Click`Deploy` to start building your app on the remote server. You can check the`Logs` tab to see the build process. For this example, we’ll use a test repo: Repo:`https://github.com/Dokploy/examples.git` Branch:`main` Build Path:`/astro`

Once the build is done, go to`Domains` and create a free domain. Just click`Create` and you’re good to go! 🎊

IntroductionDeploy your apps to multiple servers remotely.

Build ServerLearn how to configure a custom build server to compile your applications separately from your deployment servers.

### On this page

Requirements