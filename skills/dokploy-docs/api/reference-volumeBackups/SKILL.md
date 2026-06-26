---
title: "Volume Backups | Dokploy"
source: "https://docs.dokploy.com/docs/api/reference-volumeBackups"
category: dokploy-docs
created: "2026-06-25T17:21:35.749Z"
---

Volume Backups | Dokploy

# Volume Backups

Copy as Markdown

loading...

GET

/`volumeBackups.list`

Send

Authorization

Query

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Query Parameters

id*string

Length`1 <= length`

volumeBackupType*string

Value in`"application" | "postgres" | "mysql" | "mariadb" | "mongo" | "redis" | "compose" | "libsql"`

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
curl -X GET "https://your-dokploy-instance.com/api/volumeBackups.list?id=string&volumeBackupType=application"
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

/`volumeBackups.create`

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

volumeName*string

prefix*string

serviceType?string

Value in`"application" | "postgres" | "mysql" | "mariadb" | "mongo" | "redis" | "compose" | "libsql"`

appName?string

serviceName?string|null

turnOff?boolean

cronExpression*string

keepLatestCount?number|null

enabled?boolean|null

applicationId?string|null

postgresId?string|null

mariadbId?string|null

mongoId?string|null

mysqlId?string|null

redisId?string|null

libsqlId?string|null

composeId?string|null

createdAt?string

destinationId*string

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
curl -X POST "https://your-dokploy-instance.com/api/volumeBackups.create" \  -H "Content-Type: application/json" \  -d '{    "name": "string",    "volumeName": "string",    "prefix": "string",    "cronExpression": "string",    "destinationId": "string"  }'
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

/`volumeBackups.one`

Send

Authorization

Query

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Query Parameters

volumeBackupId*string

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
curl -X GET "https://your-dokploy-instance.com/api/volumeBackups.one?volumeBackupId=string"
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

/`volumeBackups.delete`

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

volumeBackupId*string

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
curl -X POST "https://your-dokploy-instance.com/api/volumeBackups.delete" \  -H "Content-Type: application/json" \  -d '{    "volumeBackupId": "string"  }'
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

/`volumeBackups.update`

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

volumeName*string

prefix*string

serviceType?string

Value in`"application" | "postgres" | "mysql" | "mariadb" | "mongo" | "redis" | "compose" | "libsql"`

appName?string

serviceName?string|null

turnOff?boolean

cronExpression*string

keepLatestCount?number|null

enabled?boolean|null

applicationId?string|null

postgresId?string|null

mariadbId?string|null

mongoId?string|null

mysqlId?string|null

redisId?string|null

libsqlId?string|null

composeId?string|null

createdAt?string

destinationId*string

volumeBackupId*string

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
curl -X POST "https://your-dokploy-instance.com/api/volumeBackups.update" \  -H "Content-Type: application/json" \  -d '{    "name": "string",    "volumeName": "string",    "prefix": "string",    "cronExpression": "string",    "destinationId": "string",    "volumeBackupId": "string"  }'
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

/`volumeBackups.runManually`

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

volumeBackupId*string

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
curl -X POST "https://your-dokploy-instance.com/api/volumeBackups.runManually" \  -H "Content-Type: application/json" \  -d '{    "volumeBackupId": "string"  }'
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

UserPrevious Page

RegistryNext Page

```
curl -X GET "https://your-dokploy-instance.com/api/volumeBackups.list?id=string&volumeBackupType=application"
```

```
curl -X POST "https://your-dokploy-instance.com/api/volumeBackups.create" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "string",
    "volumeName": "string",
    "prefix": "string",
    "cronExpression": "string",
    "destinationId": "string"
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/volumeBackups.one?volumeBackupId=string"
```

```
curl -X POST "https://your-dokploy-instance.com/api/volumeBackups.delete" \
  -H "Content-Type: application/json" \
  -d '{
    "volumeBackupId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/volumeBackups.update" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "string",
    "volumeName": "string",
    "prefix": "string",
    "cronExpression": "string",
    "destinationId": "string",
    "volumeBackupId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/volumeBackups.runManually" \
  -H "Content-Type: application/json" \
  -d '{
    "volumeBackupId": "string"
  }'
```