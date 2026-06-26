---
title: "Application | Dokploy"
source: "https://docs.dokploy.com/docs/api/application"
category: dokploy-docs
created: "2026-06-25T17:16:08.644Z"
---

Application | Dokploy

# Application

Copy as Markdown

## Application create

loading...

POST

/`application.create`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

name*string

Length`1 <= length`

appName?string

Match`^[a-zA-Z0-9._-]+$`

Length`1 <= length <= 63`

description?string|null

environmentId*string

serverId?string|null

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.create" \  -H "Content-Type: application/json" \  -d '{    "name": "string",    "environmentId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application one

loading...

GET

/`application.one`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

applicationId*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 404application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X GET "https://your-dokploy-instance.com/api/application.one?applicationId=string"
```

200400401403404500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "NOT_FOUND",
  "message": "Not found",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application reload

loading...

POST

/`application.reload`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

appName*string

Match`^[a-zA-Z0-9._-]+$`

Length`1 <= length <= 63`

applicationId*string

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.reload" \  -H "Content-Type: application/json" \  -d '{    "appName": "string",    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application delete

loading...

POST

/`application.delete`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.delete" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application stop

loading...

POST

/`application.stop`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.stop" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application start

loading...

POST

/`application.start`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.start" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application redeploy

loading...

POST

/`application.redeploy`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

title?string

description?string

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.redeploy" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application save Environment

loading...

POST

/`application.saveEnvironment`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

env*string|null

buildArgs*string|null

buildSecrets*string|null

createEnvFile*boolean

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveEnvironment" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string",    "env": "string",    "buildArgs": "string",    "buildSecrets": "string",    "createEnvFile": true  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application save Build Type

loading...

POST

/`application.saveBuildType`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

buildType*string

Value in`"dockerfile" | "heroku_buildpacks" | "paketo_buildpacks" | "nixpacks" | "static" | "railpack"`

dockerfile*string|null

dockerContextPath*string|null

dockerBuildStage*string|null

herokuVersion*string|null

railpackVersion*string|null

publishDirectory?string|null

isStaticSpa?boolean|null

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveBuildType" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string",    "buildType": "dockerfile",    "dockerfile": "string",    "dockerContextPath": "string",    "dockerBuildStage": "string",    "herokuVersion": "string",    "railpackVersion": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application save Github Provider

loading...

POST

/`application.saveGithubProvider`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

repository*string|null

owner*string|null

buildPath*string|null

githubId*string|null

branch*string

Match`^[a-zA-Z0-9._\-/]+$`

Length`1 <= length`

triggerType*string

Default`"push"`

Value in`"push" | "tag"`

enableSubmodules?boolean

watchPaths?array |null

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveGithubProvider" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string",    "repository": "string",    "owner": "string",    "buildPath": "string",    "githubId": "string",    "branch": "string",    "triggerType": "push"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application save Gitlab Provider

loading...

POST

/`application.saveGitlabProvider`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

gitlabBuildPath*string|null

gitlabOwner*string|null

gitlabRepository*string|null

gitlabId*string|null

gitlabProjectId*number|null

gitlabPathNamespace*string|null

gitlabBranch*string

Match`^[a-zA-Z0-9._\-/]+$`

Length`1 <= length`

enableSubmodules?boolean

watchPaths?array |null

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveGitlabProvider" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string",    "gitlabBuildPath": "string",    "gitlabOwner": "string",    "gitlabRepository": "string",    "gitlabId": "string",    "gitlabProjectId": 0,    "gitlabPathNamespace": "string",    "gitlabBranch": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application save Bitbucket Provider

loading...

POST

/`application.saveBitbucketProvider`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

bitbucketBuildPath*string|null

bitbucketOwner*string|null

bitbucketRepository*string|null

bitbucketRepositorySlug*string|null

bitbucketId*string|null

applicationId*string

bitbucketBranch*string

Match`^[a-zA-Z0-9._\-/]+$`

Length`1 <= length`

enableSubmodules?boolean

watchPaths?array |null

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveBitbucketProvider" \  -H "Content-Type: application/json" \  -d '{    "bitbucketBuildPath": "string",    "bitbucketOwner": "string",    "bitbucketRepository": "string",    "bitbucketRepositorySlug": "string",    "bitbucketId": "string",    "applicationId": "string",    "bitbucketBranch": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application save Gitea Provider

loading...

POST

/`application.saveGiteaProvider`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

giteaBuildPath*string|null

giteaOwner*string|null

giteaRepository*string|null

giteaId*string|null

giteaBranch*string

Match`^[a-zA-Z0-9._\-/]+$`

Length`1 <= length`

enableSubmodules?boolean

watchPaths?array |null

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveGiteaProvider" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string",    "giteaBuildPath": "string",    "giteaOwner": "string",    "giteaRepository": "string",    "giteaId": "string",    "giteaBranch": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application save Docker Provider

loading...

POST

/`application.saveDockerProvider`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

dockerImage*string|null

applicationId*string

username*string|null

password*string|null

registryUrl*string|null

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveDockerProvider" \  -H "Content-Type: application/json" \  -d '{    "dockerImage": "string",    "applicationId": "string",    "username": "string",    "password": "string",    "registryUrl": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application save Git Provider

loading...

POST

/`application.saveGitProvider`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

customGitBuildPath*string|null

customGitUrl*string|null

watchPaths*array |null

enableSubmodules?boolean

customGitBranch*string

Match`^[a-zA-Z0-9._\-/]+$`

Length`1 <= length`

customGitSSHKeyId?string|null

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveGitProvider" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string",    "customGitBuildPath": "string",    "customGitUrl": "string",    "watchPaths": [      "string"    ],    "customGitBranch": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application disconnect Git Provider

loading...

POST

/`application.disconnectGitProvider`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.disconnectGitProvider" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application mark Running

loading...

POST

/`application.markRunning`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.markRunning" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application update

loading...

POST

/`application.update`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

name?string

Length`1 <= length`

appName?string

Match`^[a-zA-Z0-9._-]+$`

Length`1 <= length <= 63`

description?string|null

env?string|null

previewEnv?string|null

watchPaths?array |null

previewBuildArgs?string|null

previewBuildSecrets?string|null

previewLabels?array |null

previewWildcard?string|null

previewPort?number|null

previewHttps?boolean

previewPath?string|null

previewCertificateType?string

Value in`"letsencrypt" | "none" | "custom"`

previewCustomCertResolver?string|null

previewLimit?number|null

isPreviewDeploymentsActive?boolean|null

previewRequireCollaboratorPermissions?boolean|null

rollbackActive?boolean|null

buildArgs?string|null

buildSecrets?string|null

memoryReservation?string|null

memoryLimit?string|null

cpuReservation?string|null

cpuLimit?string|null

title?string|null

enabled?boolean|null

subtitle?string|null

command?string|null

args?array |null

icon?string | null|null

refreshToken?string|null

sourceType?string

Value in`"github" | "docker" | "git" | "gitlab" | "bitbucket" | "gitea" | "drop"`

cleanCache?boolean|null

repository?string|null

owner?string|null

branch?string|null

buildPath?string|null

triggerType?string|null

autoDeploy?boolean|null

gitlabProjectId?number|null

gitlabRepository?string|null

gitlabOwner?string|null

gitlabBranch?string|null

gitlabBuildPath?string|null

gitlabPathNamespace?string|null

giteaRepository?string|null

giteaOwner?string|null

giteaBranch?string|null

giteaBuildPath?string|null

bitbucketRepository?string|null

bitbucketRepositorySlug?string|null

bitbucketOwner?string|null

bitbucketBranch?string|null

bitbucketBuildPath?string|null

username?string|null

password?string|null

dockerImage?string|null

registryUrl?string|null

customGitUrl?string|null

customGitBranch?string|null

customGitBuildPath?string|null

customGitSSHKeyId?string|null

enableSubmodules?boolean

dockerfile?string|null

dockerContextPath?string|null

dockerBuildStage?string|null

dropBuildPath?string|null

healthCheckSwarm?object | null|null

restartPolicySwarm?object | null|null

placementSwarm?object | null|null

updateConfigSwarm?object | null|null

rollbackConfigSwarm?object | null|null

modeSwarm?object | null|null

labelsSwarm?object | null|null

networkSwarm?array | null|null

stopGracePeriodSwarm?number | null|null

endpointSpecSwarm?object | null|null

ulimitsSwarm?array | null|null

replicas?number

applicationStatus?string

Value in`"idle" | "running" | "done" | "error"`

buildType?string

Value in`"dockerfile" | "heroku_buildpacks" | "paketo_buildpacks" | "nixpacks" | "static" | "railpack"`

railpackVersion?string|null

herokuVersion?string|null

publishDirectory?string|null

isStaticSpa?boolean|null

createEnvFile?boolean

createdAt?string

registryId?string|null

rollbackRegistryId?string|null

environmentId?string

githubId?string|null

gitlabId?string|null

giteaId?string|null

bitbucketId?string|null

buildServerId?string|null

buildRegistryId?string|null

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.update" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application refresh Token

loading...

POST

/`application.refreshToken`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.refreshToken" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application deploy

loading...

POST

/`application.deploy`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

title?string

description?string

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.deploy" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application clean Queues

loading...

POST

/`application.cleanQueues`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.cleanQueues" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application clear Deployments

loading...

POST

/`application.clearDeployments`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.clearDeployments" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application kill Build

loading...

POST

/`application.killBuild`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.killBuild" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application read Traefik Config

loading...

GET

/`application.readTraefikConfig`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

applicationId*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 404application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X GET "https://your-dokploy-instance.com/api/application.readTraefikConfig?applicationId=string"
```

200400401403404500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "NOT_FOUND",
  "message": "Not found",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application drop Deployment

loading...

POST

/`application.dropDeployment`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`multipart/form-data`

applicationId*string

zip*file

Format`binary`

dropBuildPath?string

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.dropDeployment" \  -F applicationId="string" \  -F zip="string"
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application update Traefik Config

loading...

POST

/`application.updateTraefikConfig`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

traefikConfig*string

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.updateTraefikConfig" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string",    "traefikConfig": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application read App Monitoring

loading...

GET

/`application.readAppMonitoring`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

appName*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 404application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X GET "https://your-dokploy-instance.com/api/application.readAppMonitoring?appName=string"
```

200400401403404500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "NOT_FOUND",
  "message": "Not found",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application move

loading...

POST

/`application.move`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

targetEnvironmentId*string

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.move" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string",    "targetEnvironmentId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application cancel Deployment

loading...

POST

/`application.cancelDeployment`

Send

Authorization

Body

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Request Body

`application/json`

applicationId*string

Length`1 <= length`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X POST "https://your-dokploy-instance.com/api/application.cancelDeployment" \  -H "Content-Type: application/json" \  -d '{    "applicationId": "string"  }'
```

200400401403500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application search

loading...

GET

/`application.search`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

q?string

name?string

appName?string

description?string

repository?string

owner?string

dockerImage?string

projectId?string

environmentId?string

limit?number

Default`20`

Range`1 <= value <= 100`

offset?number

Default`0`

Range`0 <= value`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 404application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X GET "https://your-dokploy-instance.com/api/application.search"
```

200400401403404500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "NOT_FOUND",
  "message": "Not found",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

## Application read Logs

loading...

GET

/`application.readLogs`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

applicationId*string

Length`1 <= length`

tail?integer

Default`100`

Range`1 <= value <= 10000`

since?string

Default`"all"`

Match`^(all|\d+[smhd])$`

search?string

Match`^[a-zA-Z0-9 ._-]{0,500}$`

### Response Body

### 200application/json

### 400application/json

### 401application/json

### 403application/json

### 404application/json

### 500application/json

cURL

JavaScript

Go

Python

Java

C#

```
curl -X GET "https://your-dokploy-instance.com/api/application.readLogs?applicationId=string"
```

200400401403404500

```
{}
```

```
{
  "code": "BAD_REQUEST",
  "message": "Invalid input data",
  "issues": []
}
```

```
{
  "code": "UNAUTHORIZED",
  "message": "Authorization not provided",
  "issues": []
}
```

```
{
  "code": "FORBIDDEN",
  "message": "Insufficient access",
  "issues": []
}
```

```
{
  "code": "NOT_FOUND",
  "message": "Not found",
  "issues": []
}
```

```
{
  "code": "INTERNAL_SERVER_ERROR",
  "message": "Internal server error",
  "issues": []
}
```

AiPrevious Page

BackupNext Page

```
curl -X POST "https://your-dokploy-instance.com/api/application.create" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "string",
    "environmentId": "string"
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/application.one?applicationId=string"
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.reload" \
  -H "Content-Type: application/json" \
  -d '{
    "appName": "string",
    "applicationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.delete" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.stop" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.start" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.redeploy" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveEnvironment" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string",
    "env": "string",
    "buildArgs": "string",
    "buildSecrets": "string",
    "createEnvFile": true
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveBuildType" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string",
    "buildType": "dockerfile",
    "dockerfile": "string",
    "dockerContextPath": "string",
    "dockerBuildStage": "string",
    "herokuVersion": "string",
    "railpackVersion": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveGithubProvider" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string",
    "repository": "string",
    "owner": "string",
    "buildPath": "string",
    "githubId": "string",
    "branch": "string",
    "triggerType": "push"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveGitlabProvider" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string",
    "gitlabBuildPath": "string",
    "gitlabOwner": "string",
    "gitlabRepository": "string",
    "gitlabId": "string",
    "gitlabProjectId": 0,
    "gitlabPathNamespace": "string",
    "gitlabBranch": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveBitbucketProvider" \
  -H "Content-Type: application/json" \
  -d '{
    "bitbucketBuildPath": "string",
    "bitbucketOwner": "string",
    "bitbucketRepository": "string",
    "bitbucketRepositorySlug": "string",
    "bitbucketId": "string",
    "applicationId": "string",
    "bitbucketBranch": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveGiteaProvider" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string",
    "giteaBuildPath": "string",
    "giteaOwner": "string",
    "giteaRepository": "string",
    "giteaId": "string",
    "giteaBranch": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveDockerProvider" \
  -H "Content-Type: application/json" \
  -d '{
    "dockerImage": "string",
    "applicationId": "string",
    "username": "string",
    "password": "string",
    "registryUrl": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.saveGitProvider" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string",
    "customGitBuildPath": "string",
    "customGitUrl": "string",
    "watchPaths": [
      "string"
    ],
    "customGitBranch": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.disconnectGitProvider" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.markRunning" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.update" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.refreshToken" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.deploy" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.cleanQueues" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.clearDeployments" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.killBuild" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/application.readTraefikConfig?applicationId=string"
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.dropDeployment" \
  -F applicationId="string" \
  -F zip="string"
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.updateTraefikConfig" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string",
    "traefikConfig": "string"
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/application.readAppMonitoring?appName=string"
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.move" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string",
    "targetEnvironmentId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/application.cancelDeployment" \
  -H "Content-Type: application/json" \
  -d '{
    "applicationId": "string"
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/application.search"
```

```
curl -X GET "https://your-dokploy-instance.com/api/application.readLogs?applicationId=string"
```