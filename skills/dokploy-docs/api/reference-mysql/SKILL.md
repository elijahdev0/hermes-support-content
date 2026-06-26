---
title: "Mysql | Dokploy"
source: "https://docs.dokploy.com/docs/api/reference-mysql"
category: dokploy-docs
created: "2026-06-25T17:21:35.748Z"
---

Mysql | Dokploy

# Mysql

Copy as Markdown

loading...

POST

/`mysql.create`

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

Default`"mysql:8"`

environmentId*string

description?string|null

databaseName*string

Length`1 <= length`

databaseUser*string

Length`1 <= length`

databasePassword*string

Match`^[a-zA-Z0-9@#%^&*()_+\-=[\]{}|;:,.<>?~`]*$`

databaseRootPassword?string

Match`^[a-zA-Z0-9@#%^&*()_+\-=[\]{}|;:,.<>?~`]*$`

serverId?string|null

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.create" \  -H "Content-Type: application/json" \  -d '{    "name": "string",    "environmentId": "string",    "databaseName": "string",    "databaseUser": "string",    "databasePassword": "string"  }'
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

/`mysql.one`

Send

Authorization

Query

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Query Parameters

mysqlId*string

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
curl -X GET "https://your-dokploy-instance.com/api/mysql.one?mysqlId=string"
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

/`mysql.start`

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

mysqlId*string

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.start" \  -H "Content-Type: application/json" \  -d '{    "mysqlId": "string"  }'
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

/`mysql.stop`

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

mysqlId*string

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.stop" \  -H "Content-Type: application/json" \  -d '{    "mysqlId": "string"  }'
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

/`mysql.saveExternalPort`

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

mysqlId*string

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.saveExternalPort" \  -H "Content-Type: application/json" \  -d '{    "mysqlId": "string",    "externalPort": 0  }'
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

/`mysql.deploy`

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

mysqlId*string

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.deploy" \  -H "Content-Type: application/json" \  -d '{    "mysqlId": "string"  }'
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

/`mysql.changeStatus`

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

mysqlId*string

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.changeStatus" \  -H "Content-Type: application/json" \  -d '{    "mysqlId": "string",    "applicationStatus": "idle"  }'
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

/`mysql.reload`

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

mysqlId*string

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.reload" \  -H "Content-Type: application/json" \  -d '{    "mysqlId": "string",    "appName": "string"  }'
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

/`mysql.remove`

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

mysqlId*string

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.remove" \  -H "Content-Type: application/json" \  -d '{    "mysqlId": "string"  }'
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

/`mysql.saveEnvironment`

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

mysqlId*string

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.saveEnvironment" \  -H "Content-Type: application/json" \  -d '{    "mysqlId": "string",    "env": "string"  }'
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

/`mysql.update`

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

mysqlId*string

Length`1 <= length`

name?string

Length`1 <= length`

appName?string

Match`^[a-zA-Z0-9._-]+$`

Length`1 <= length <= 63`

description?string|null

databaseName?string

Length`1 <= length`

databaseUser?string

Length`1 <= length`

databasePassword?string

Match`^[a-zA-Z0-9@#%^&*()_+\-=[\]{}|;:,.<>?~`]*$`

databaseRootPassword?string

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.update" \  -H "Content-Type: application/json" \  -d '{    "mysqlId": "string"  }'
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

/`mysql.move`

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

mysqlId*string

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.move" \  -H "Content-Type: application/json" \  -d '{    "mysqlId": "string",    "targetEnvironmentId": "string"  }'
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

/`mysql.rebuild`

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

mysqlId*string

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.rebuild" \  -H "Content-Type: application/json" \  -d '{    "mysqlId": "string"  }'
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
curl -X POST "https://your-dokploy-instance.com/api/mysql.create" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "string",
    "environmentId": "string",
    "databaseName": "string",
    "databaseUser": "string",
    "databasePassword": "string"
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/mysql.one?mysqlId=string"
```

```
curl -X POST "https://your-dokploy-instance.com/api/mysql.start" \
  -H "Content-Type: application/json" \
  -d '{
    "mysqlId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mysql.stop" \
  -H "Content-Type: application/json" \
  -d '{
    "mysqlId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mysql.saveExternalPort" \
  -H "Content-Type: application/json" \
  -d '{
    "mysqlId": "string",
    "externalPort": 0
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mysql.deploy" \
  -H "Content-Type: application/json" \
  -d '{
    "mysqlId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mysql.changeStatus" \
  -H "Content-Type: application/json" \
  -d '{
    "mysqlId": "string",
    "applicationStatus": "idle"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mysql.reload" \
  -H "Content-Type: application/json" \
  -d '{
    "mysqlId": "string",
    "appName": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mysql.remove" \
  -H "Content-Type: application/json" \
  -d '{
    "mysqlId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mysql.saveEnvironment" \
  -H "Content-Type: application/json" \
  -d '{
    "mysqlId": "string",
    "env": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mysql.update" \
  -H "Content-Type: application/json" \
  -d '{
    "mysqlId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mysql.move" \
  -H "Content-Type: application/json" \
  -d '{
    "mysqlId": "string",
    "targetEnvironmentId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/mysql.rebuild" \
  -H "Content-Type: application/json" \
  -d '{
    "mysqlId": "string"
  }'
```