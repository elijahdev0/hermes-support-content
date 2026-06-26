---
title: "Mysql | Dokploy"
source: "https://docs.dokploy.com/docs/api/mysql"
category: dokploy-docs
created: "2026-06-25T17:16:08.646Z"
---

Mysql | Dokploy

# Mysql

Copy as Markdown

## Mysql create

loading...

POST

/`mysql.create`

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

## Mysql one

loading...

GET

/`mysql.one`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

mysqlId*string

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

## Mysql start

loading...

POST

/`mysql.start`

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

mysqlId*string

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

## Mysql stop

loading...

POST

/`mysql.stop`

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

mysqlId*string

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

## Mysql save External Port

loading...

POST

/`mysql.saveExternalPort`

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

mysqlId*string

externalPort*number|null

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

## Mysql deploy

loading...

POST

/`mysql.deploy`

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

mysqlId*string

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

## Mysql change Status

loading...

POST

/`mysql.changeStatus`

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

mysqlId*string

applicationStatus*string

Value in`"idle" | "running" | "done" | "error"`

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

## Mysql reload

loading...

POST

/`mysql.reload`

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

mysqlId*string

appName*string

Match`^[a-zA-Z0-9._-]+$`

Length`1 <= length <= 63`

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

## Mysql remove

loading...

POST

/`mysql.remove`

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

mysqlId*string

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

## Mysql save Environment

loading...

POST

/`mysql.saveEnvironment`

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

mysqlId*string

env*string|null

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

## Mysql update

loading...

POST

/`mysql.update`

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

## Mysql change Password

loading...

POST

/`mysql.changePassword`

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

mysqlId*string

Length`1 <= length`

password*string

Match`^[a-zA-Z0-9@#%^&*()_+\-=[\]{}|;:,.<>?~`]*$`

Length`1 <= length`

type?string

Default`"user"`

Value in`"user" | "root"`

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.changePassword" \  -H "Content-Type: application/json" \  -d '{    "mysqlId": "string",    "password": "string"  }'
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

## Mysql move

loading...

POST

/`mysql.move`

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

mysqlId*string

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

## Mysql rebuild

loading...

POST

/`mysql.rebuild`

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

mysqlId*string

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

## Mysql search

loading...

GET

/`mysql.search`

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
curl -X GET "https://your-dokploy-instance.com/api/mysql.search"
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

## Mysql read Logs

loading...

GET

/`mysql.readLogs`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

mysqlId*string

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
curl -X GET "https://your-dokploy-instance.com/api/mysql.readLogs?mysqlId=string"
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

MountsPrevious Page

OrganizationNext Page

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
curl -X POST "https://your-dokploy-instance.com/api/mysql.changePassword" \
  -H "Content-Type: application/json" \
  -d '{
    "mysqlId": "string",
    "password": "string"
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

```
curl -X GET "https://your-dokploy-instance.com/api/mysql.search"
```

```
curl -X GET "https://your-dokploy-instance.com/api/mysql.readLogs?mysqlId=string"
```