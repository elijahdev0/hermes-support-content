---
title: "Schedule | Dokploy"
source: "https://docs.dokploy.com/docs/api/schedule"
category: dokploy-docs
created: "2026-06-25T17:16:08.646Z"
---

Schedule | Dokploy

# Schedule

Copy as Markdown

## Schedule create

loading...

POST

/`schedule.create`

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

scheduleId?string

name*string

description?string|null

cronExpression*string

appName?string

serviceName?string|null

shellType?string

Value in`"bash" | "sh"`

scheduleType?string

Value in`"application" | "compose" | "server" | "dokploy-server"`

command*string

script?string|null

applicationId?string|null

composeId?string|null

serverId?string|null

organizationId?string|null

enabled?boolean

timezone?string|null

createdAt?string

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
curl -X POST "https://your-dokploy-instance.com/api/schedule.create" \  -H "Content-Type: application/json" \  -d '{    "name": "string",    "cronExpression": "string",    "command": "string"  }'
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

## Schedule update

loading...

POST

/`schedule.update`

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

scheduleId*string

Length`1 <= length`

name*string

description?string|null

cronExpression*string

appName?string

serviceName?string|null

shellType?string

Value in`"bash" | "sh"`

scheduleType?string

Value in`"application" | "compose" | "server" | "dokploy-server"`

command*string

script?string|null

applicationId?string|null

composeId?string|null

serverId?string|null

organizationId?string|null

enabled?boolean

timezone?string|null

createdAt?string

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
curl -X POST "https://your-dokploy-instance.com/api/schedule.update" \  -H "Content-Type: application/json" \  -d '{    "scheduleId": "string",    "name": "string",    "cronExpression": "string",    "command": "string"  }'
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

## Schedule delete

loading...

POST

/`schedule.delete`

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

scheduleId*string

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
curl -X POST "https://your-dokploy-instance.com/api/schedule.delete" \  -H "Content-Type: application/json" \  -d '{    "scheduleId": "string"  }'
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

## Schedule list

loading...

GET

/`schedule.list`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

id*string

scheduleType*string

Value in`"application" | "compose" | "server" | "dokploy-server"`

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
curl -X GET "https://your-dokploy-instance.com/api/schedule.list?id=string&scheduleType=application"
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

## Schedule one

loading...

GET

/`schedule.one`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

scheduleId*string

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
curl -X GET "https://your-dokploy-instance.com/api/schedule.one?scheduleId=string"
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

## Schedule run Manually

loading...

POST

/`schedule.runManually`

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

scheduleId*string

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
curl -X POST "https://your-dokploy-instance.com/api/schedule.runManually" \  -H "Content-Type: application/json" \  -d '{    "scheduleId": "string"  }'
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

RollbackPrevious Page

SecurityNext Page

```
curl -X POST "https://your-dokploy-instance.com/api/schedule.create" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "string",
    "cronExpression": "string",
    "command": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/schedule.update" \
  -H "Content-Type: application/json" \
  -d '{
    "scheduleId": "string",
    "name": "string",
    "cronExpression": "string",
    "command": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/schedule.delete" \
  -H "Content-Type: application/json" \
  -d '{
    "scheduleId": "string"
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/schedule.list?id=string&scheduleType=application"
```

```
curl -X GET "https://your-dokploy-instance.com/api/schedule.one?scheduleId=string"
```

```
curl -X POST "https://your-dokploy-instance.com/api/schedule.runManually" \
  -H "Content-Type: application/json" \
  -d '{
    "scheduleId": "string"
  }'
```