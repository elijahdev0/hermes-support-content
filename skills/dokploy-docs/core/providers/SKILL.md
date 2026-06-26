---
title: "Providers | Dokploy"
source: "https://docs.dokploy.com/docs/core/providers"
category: dokploy-docs
created: "2026-06-25T17:21:38.073Z"
---

Providers | Dokploy

# Providers

Copy as Markdown

Learn how to use providers in your application or docker compose.

Dokploy offers several deployment methods, streamlining the process whether you're utilizing GitHub, any Git provider, Docker, or automated deployments.

1. GitHub
2. Gitlab
3. Bitbucket
4. Gitea
5. Git
6. Docker (Only Applications)
7. Drag and Drop .zip (Only Applications)
8. Raw (Only Docker Compose)

## GitHub, Gitlab, Bitbucket, Gitea

1. Github Guide.
2. Gitlab guide.
3. Bitbucket guide.
4. Gitea guide.

## Git

For deployments from any Git repository, whether public or private, you can use either SSH or HTTPS:

### Public Repositories (HTTPS)

1. Enter the repository URL in`HTTPS URL`.
2. Type the branch name.
3. Click on`Save`.

### Private Repositories

For private repositories, is required to first create an SSH Key The Steps are almost similar for all providers.

1. Go to SSH Keys Section and click on`Create SSH Key`.
2. Click on`Generate RSA SSH Key` and copy the`Public Key`.
3. Go to your Git Provider, either Github, Gitlab, Bitbucket, Gitea or any other.
4. Go to`Settings` and search for`SSH Keys`.
5. Click on`Add SSH Key`.
6. Paste the SSH Key and click on`Add Key`.

You can then copy the SSH key and paste it into the settings of your account.

This is for Github, but the same applies for Gitlab, Bitbucket, Gitea, etc.

This enables you to pull repositories from your private repository, a method consistent across nearly all providers, remember to use the SSH URL [email protected]`:user/repo.git` and not the HTTPS URL`https://github.com/user/repo.git`.

## Docker (Applications)

For Docker deployments you have two options:

1. Login to your registry using the Registry Section and it automatically will pull the image from the registry in the case of a private registry.
2. Provide the username and password directly in the application settings.

## Drag and Drop .zip (Applications)

You can upload a zip file directly from your computer and trigger a deployment.

## Raw (Docker Compose)

You specify a docker compose file directly in the code editor and trigger a deployment.

Normal

Volume BackupsLearn how to backup your volumes using Dokploy's Volume Backups feature

Watch PathsLearn how to use watch paths in your application or docker compose.

### On this page

GitHub, Gitlab, Bitbucket, GiteaGitPublic Repositories (HTTPS)Private RepositoriesDocker (Applications)Drag and Drop .zip (Applications)Raw (Docker Compose)