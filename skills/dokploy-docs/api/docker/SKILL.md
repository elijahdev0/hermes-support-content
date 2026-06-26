---
title: "Docker | Dokploy"
source: "https://docs.dokploy.com/docs/api/docker"
category: dokploy-docs
created: "2026-06-25T17:16:08.645Z"
---

Docker | Dokploy

# Docker

Copy as Markdown

## Docker get Containers

loading...

GET

/`docker.getContainers`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

serverId?string

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
curl -X GET "https://your-dokploy-instance.com/api/docker.getContainers"
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

## Docker restart Container

loading...

POST

/`docker.restartContainer`

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

containerId*string

Match`^[a-zA-Z0-9.\-_]+$`

Length`1 <= length`

serverId?string

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
curl -X POST "https://your-dokploy-instance.com/api/docker.restartContainer" \  -H "Content-Type: application/json" \  -d '{    "containerId": "string"  }'
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

## Docker start Container

loading...

POST

/`docker.startContainer`

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

containerId*string

Match`^[a-zA-Z0-9.\-_]+$`

Length`1 <= length`

serverId?string

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
curl -X POST "https://your-dokploy-instance.com/api/docker.startContainer" \  -H "Content-Type: application/json" \  -d '{    "containerId": "string"  }'
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

## Docker stop Container

loading...

POST

/`docker.stopContainer`

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

containerId*string

Match`^[a-zA-Z0-9.\-_]+$`

Length`1 <= length`

serverId?string

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
curl -X POST "https://your-dokploy-instance.com/api/docker.stopContainer" \  -H "Content-Type: application/json" \  -d '{    "containerId": "string"  }'
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

## Docker kill Container

loading...

POST

/`docker.killContainer`

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

containerId*string

Match`^[a-zA-Z0-9.\-_]+$`

Length`1 <= length`

serverId?string

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
curl -X POST "https://your-dokploy-instance.com/api/docker.killContainer" \  -H "Content-Type: application/json" \  -d '{    "containerId": "string"  }'
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

## Docker remove Container

loading...

POST

/`docker.removeContainer`

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

containerId*string

Match`^[a-zA-Z0-9.\-_]+$`

Length`1 <= length`

serverId?string

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
curl -X POST "https://your-dokploy-instance.com/api/docker.removeContainer" \  -H "Content-Type: application/json" \  -d '{    "containerId": "string"  }'
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

## Docker get Config

loading...

GET

/`docker.getConfig`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

containerId*string

Match`^[a-zA-Z0-9.\-_]+$`

Length`1 <= length`

serverId?string

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
curl -X GET "https://your-dokploy-instance.com/api/docker.getConfig?containerId=string"
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

## Docker get Containers By App Name Match

loading...

GET

/`docker.getContainersByAppNameMatch`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

appType?string

Value in`"stack" | "docker-compose"`

appName*string

Match`^[a-zA-Z0-9.\-_]+$`

Length`1 <= length`

serverId?string

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
curl -X GET "https://your-dokploy-instance.com/api/docker.getContainersByAppNameMatch?appName=string"
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

## Docker get Containers By App Label

loading...

GET

/`docker.getContainersByAppLabel`

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

Match`^[a-zA-Z0-9.\-_]+$`

Length`1 <= length`

serverId?string

type*string

Value in`"standalone" | "swarm"`

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
curl -X GET "https://your-dokploy-instance.com/api/docker.getContainersByAppLabel?appName=string&type=standalone"
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

## Docker get Stack Containers By App Name

loading...

GET

/`docker.getStackContainersByAppName`

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

Match`^[a-zA-Z0-9.\-_]+$`

Length`1 <= length`

serverId?string

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
curl -X GET "https://your-dokploy-instance.com/api/docker.getStackContainersByAppName?appName=string"
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

## Docker get Service Containers By App Name

loading...

GET

/`docker.getServiceContainersByAppName`

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

Match`^[a-zA-Z0-9.\-_]+$`

Length`1 <= length`

serverId?string

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
curl -X GET "https://your-dokploy-instance.com/api/docker.getServiceContainersByAppName?appName=string"
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

## Docker upload File To Container

loading...

POST

/`docker.uploadFileToContainer`

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

containerId*string

Match`^[a-zA-Z0-9.\-_]+$`

Length`1 <= length`

file*file

Format`binary`

destinationPath*string

Match`^[a-zA-Z0-9.\-_/]+$`

Length`1 <= length`

serverId?string

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
curl -X POST "https://your-dokploy-instance.com/api/docker.uploadFileToContainer" \  -F containerId="string" \  -F file="string" \  -F destinationPath="string"
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

```
curl -X GET "https://your-dokploy-instance.com/api/docker.getContainers"
```

```
curl -X POST "https://your-dokploy-instance.com/api/docker.restartContainer" \
  -H "Content-Type: application/json" \
  -d '{
    "containerId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/docker.startContainer" \
  -H "Content-Type: application/json" \
  -d '{
    "containerId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/docker.stopContainer" \
  -H "Content-Type: application/json" \
  -d '{
    "containerId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/docker.killContainer" \
  -H "Content-Type: application/json" \
  -d '{
    "containerId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/docker.removeContainer" \
  -H "Content-Type: application/json" \
  -d '{
    "containerId": "string"
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/docker.getConfig?containerId=string"
```

```
curl -X GET "https://your-dokploy-instance.com/api/docker.getContainersByAppNameMatch?appName=string"
```

```
curl -X GET "https://your-dokploy-instance.com/api/docker.getContainersByAppLabel?appName=string&type=standalone"
```

```
curl -X GET "https://your-dokploy-instance.com/api/docker.getStackContainersByAppName?appName=string"
```

```
curl -X GET "https://your-dokploy-instance.com/api/docker.getServiceContainersByAppName?appName=string"
```

```
curl -X POST "https://your-dokploy-instance.com/api/docker.uploadFileToContainer" \
  -F containerId="string" \
  -F file="string" \
  -F destinationPath="string"
```