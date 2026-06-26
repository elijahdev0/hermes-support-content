---
title: "Mongo | Dokploy"
source: "https://docs.dokploy.com/docs/api/reference-mongo"
category: dokploy-docs
created: "2026-06-25T17:21:34.550Z"
---

Mongo | Dokploy

# Mongo

Copy as Markdown

loading...

POST

/`mongo.create`

Send

Authorization

Body

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Request Body

`application/json`

name*string

Length`1 <= length`

appName?string

Match`^[a-zA-Z0-9._-]+$`

Length`1 <= length <= 63`

dockerImage?string

Default`"mongo:15"`

environmentId*string

description?string|null

databaseUser*string

Length`1 <= length`

databasePassword*string

Match`^[a-zA-Z0-9@#%^&*()_+\-=[\]{}|;:,.<>?~`]*$`

serverId?string|null

replicaSets?boolean|null

## Response Body

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
curl -X POST "https://your-dokploy-instance.com/api/mongo.create" \  -H "Content-Type: application/json" \  -d '{    "name": "string",    "environmentId": "string",    "databaseUser": "string",    "databasePassword": "string"  }'
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

loading...

GET

/`mongo.one`

Send

Authorization

Query

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Query Parameters

mongoId*string

Length`1 <= length`

## Response Body

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
curl -X GET "https://your-dokploy-instance.com/api/mongo.one?mongoId=string"
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

loading...

POST

/`mongo.start`

Send

Authorization

Body

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Request Body

`application/json`

mongoId*string

Length`1 <= length`

## Response Body

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
curl -X POST "https://your-dokploy-instance.com/api/mongo.start" \  -H "Content-Type: application/json" \  -d '{    "mongoId": "string"  }'
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

loading...

POST

/`mongo.stop`

Send

Authorization

Body

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Request Body

`application/json`

mongoId*string

Length`1 <= length`

## Response Body

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
curl -X POST "https://your-dokploy-instance.com/api/mongo.stop" \  -H "Content-Type: application/json" \  -d '{    "mongoId": "string"  }'
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

loading...

POST

/`mongo.saveExternalPort`

Send

Authorization

Body

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Request Body

`application/json`

mongoId*string

externalPort*number|null

## Response Body

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
curl -X POST "https://your-dokploy-instance.com/api/mongo.saveExternalPort" \  -H "Content-Type: application/json" \  -d '{    "mongoId": "string",    "externalPort": 0  }'
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

loading...

POST

/`mongo.deploy`

Send

Authorization

Body

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Request Body

`application/json`

mongoId*string

## Response Body

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
curl -X POST "https://your-dokploy-instance.com/api/mongo.deploy" \  -H "Content-Type: application/json" \  -d '{    "mongoId": "string"  }'
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

loading...

POST

/`mongo.changeStatus`

Send

Authorization

Body

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Request Body

`application/json`

mongoId*string

applicationStatus*string

Value in`"idle" | "running" | "done" | "error"`

## Response Body

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
curl -X POST "https://your-dokploy-instance.com/api/mongo.changeStatus" \  -H "Content-Type: application/json" \  -d '{    "mongoId": "string",    "applicationStatus": "idle"  }'
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

loading...

POST

/`mongo.reload`

Send

Authorization

Body

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Request Body

`application/json`

mongoId*string

appName*string

Match`^[a-zA-Z0-9._-]+$`

Length`1 <= length <= 63`

## Response Body

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
curl -X POST "https://your-dokploy-instance.com/api/mongo.reload" \  -H "Content-Type: application/json" \  -d '{    "mongoId": "string",    "appName": "string"  }'
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

loading...

POST

/`mongo.remove`

Send

Authorization

Body

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Request Body

`application/json`

mongoId*string

Length`1 <= length`

## Response Body

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
curl -X POST "https://your-dokploy-instance.com/api/mongo.remove" \  -H "Content-Type: application/json" \  -d '{    "mongoId": "string"  }'
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

loading...

POST

/`mongo.saveEnvironment`

Send

Authorization

Body

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Request Body

`application/json`

mongoId*string

env*string|null

## Response Body

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
curl -X POST "https://your-dokploy-instance.com/api/mongo.saveEnvironment" \  -H "Content-Type: application/json" \  -d '{    "mongoId": "string",    "env": "string"  }'
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

loading...

POST

/`mongo.update`

Send

Authorization

Body

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Request Body

`application/json`

mongoId*string

Length`1 <= length`

name?string

Length`1 <= length`

appName?string

Match`^[a-zA-Z0-9._-]+$`

Length`1 <= length <= 63`

description?string|null

databaseUser?string

Length`1 <= length`

databasePassword?string

Match`^[a-zA-Z0-9@#%^&*()_+\-=[\]{}|;:,.<>?~`]*$`

dockerImage?string

command?string|null

args?array |null

env?string|null

memoryReservation?string|null

memoryLimit?string|null

cpuReservation?string|null

cpuLimit?string|null

externalPort?number|null

applicationStatus?string

Value in`"idle" | "running" | "done" | "error"`

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

createdAt?string

environmentId?string

replicaSets?boolean|null

## Response Body

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
curl -X POST "https://your-dokploy-instance.com/api/mongo.update" \  -H "Content-Type: application/json" \  -d '{    "mongoId": "string"  }'
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

loading...

POST

/`mongo.move`

Send

Authorization

Body

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Request Body

`application/json`

mongoId*string

targetEnvironmentId*string

## Response Body

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
curl -X POST "https://your-dokploy-instance.com/api/mongo.move" \  -H "Content-Type: application/json" \  -d '{    "mongoId": "string",    "targetEnvironmentId": "string"  }'
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

loading...

POST

/`mongo.rebuild`

Send

Authorization

Body

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Request Body

`application/json`

mongoId*string

## Response Body

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
curl -X POST "https://your-dokploy-instance.com/api/mongo.rebuild" \  -H "Content-Type: application/json" \  -d '{    "mongoId": "string"  }'
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

MariadbPrevious Page

MountsNext Page

```
curl -X POST "https://your-dokploy-instance.com/api/mongo.create" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "string",
    "environmentId": "string",
    "databaseUser": "string",
    "databasePassword": "string"
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/mongo.one?mongoId=string"
```

```
curl -X POST "https://your-dokploy-instance.com/api/mongo.start" \
  -H "Content-Type: application/json" \
  -d '{
    "mongoId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mongo.stop" \
  -H "Content-Type: application/json" \
  -d '{
    "mongoId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mongo.saveExternalPort" \
  -H "Content-Type: application/json" \
  -d '{
    "mongoId": "string",
    "externalPort": 0
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mongo.deploy" \
  -H "Content-Type: application/json" \
  -d '{
    "mongoId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mongo.changeStatus" \
  -H "Content-Type: application/json" \
  -d '{
    "mongoId": "string",
    "applicationStatus": "idle"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mongo.reload" \
  -H "Content-Type: application/json" \
  -d '{
    "mongoId": "string",
    "appName": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mongo.remove" \
  -H "Content-Type: application/json" \
  -d '{
    "mongoId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mongo.saveEnvironment" \
  -H "Content-Type: application/json" \
  -d '{
    "mongoId": "string",
    "env": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mongo.update" \
  -H "Content-Type: application/json" \
  -d '{
    "mongoId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mongo.move" \
  -H "Content-Type: application/json" \
  -d '{
    "mongoId": "string",
    "targetEnvironmentId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mongo.rebuild" \
  -H "Content-Type: application/json" \
  -d '{
    "mongoId": "string"
  }'
```