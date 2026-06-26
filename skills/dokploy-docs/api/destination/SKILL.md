---
title: "Destination | Dokploy"
source: "https://docs.dokploy.com/docs/api/destination"
category: dokploy-docs
created: "2026-06-25T17:16:08.645Z"
---

Destination | Dokploy

# Destination

Copy as Markdown

## Destination create

loading...

POST

/`destination.create`

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

provider*string|null

accessKey*string

bucket*string

region*string

endpoint*string

secretAccessKey*string

additionalFlags*array |null

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
curl -X POST "https://your-dokploy-instance.com/api/destination.create" \  -H "Content-Type: application/json" \  -d '{    "name": "string",    "provider": "string",    "accessKey": "string",    "bucket": "string",    "region": "string",    "endpoint": "string",    "secretAccessKey": "string",    "additionalFlags": []  }'
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

## Destination test Connection

loading...

POST

/`destination.testConnection`

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

provider*string|null

accessKey*string

bucket*string

region*string

endpoint*string

secretAccessKey*string

additionalFlags*array |null

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
curl -X POST "https://your-dokploy-instance.com/api/destination.testConnection" \  -H "Content-Type: application/json" \  -d '{    "name": "string",    "provider": "string",    "accessKey": "string",    "bucket": "string",    "region": "string",    "endpoint": "string",    "secretAccessKey": "string",    "additionalFlags": []  }'
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

## Destination one

loading...

GET

/`destination.one`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

destinationId*string

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
curl -X GET "https://your-dokploy-instance.com/api/destination.one?destinationId=string"
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

## Destination all

loading...

GET

/`destination.all`

Send

Authorization

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

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
curl -X GET "https://your-dokploy-instance.com/api/destination.all"
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

## Destination remove

loading...

POST

/`destination.remove`

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

destinationId*string

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
curl -X POST "https://your-dokploy-instance.com/api/destination.remove" \  -H "Content-Type: application/json" \  -d '{    "destinationId": "string"  }'
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

## Destination update

loading...

POST

/`destination.update`

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

accessKey*string

bucket*string

region*string

endpoint*string

secretAccessKey*string

destinationId*string

provider*string|null

additionalFlags*array |null

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
curl -X POST "https://your-dokploy-instance.com/api/destination.update" \  -H "Content-Type: application/json" \  -d '{    "name": "string",    "accessKey": "string",    "bucket": "string",    "region": "string",    "endpoint": "string",    "secretAccessKey": "string",    "destinationId": "string",    "provider": "string",    "additionalFlags": []  }'
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

DeploymentPrevious Page

DockerNext Page

```
curl -X POST "https://your-dokploy-instance.com/api/destination.create" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "string",
    "provider": "string",
    "accessKey": "string",
    "bucket": "string",
    "region": "string",
    "endpoint": "string",
    "secretAccessKey": "string",
    "additionalFlags": []
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/destination.testConnection" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "string",
    "provider": "string",
    "accessKey": "string",
    "bucket": "string",
    "region": "string",
    "endpoint": "string",
    "secretAccessKey": "string",
    "additionalFlags": []
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/destination.one?destinationId=string"
```

```
curl -X GET "https://your-dokploy-instance.com/api/destination.all"
```

```
curl -X POST "https://your-dokploy-instance.com/api/destination.remove" \
  -H "Content-Type: application/json" \
  -d '{
    "destinationId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/destination.update" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "string",
    "accessKey": "string",
    "bucket": "string",
    "region": "string",
    "endpoint": "string",
    "secretAccessKey": "string",
    "destinationId": "string",
    "provider": "string",
    "additionalFlags": []
  }'
```