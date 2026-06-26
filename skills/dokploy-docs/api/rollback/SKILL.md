---
title: "Rollback | Dokploy"
source: "https://docs.dokploy.com/docs/api/rollback"
category: dokploy-docs
created: "2026-06-25T17:16:08.646Z"
---

Rollback | Dokploy

# Rollback

Copy as Markdown

## Rollback delete

loading...

POST

/`rollback.delete`

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

rollbackId*string

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
curl -X POST "https://your-dokploy-instance.com/api/rollback.delete" \  -H "Content-Type: application/json" \  -d '{    "rollbackId": "string"  }'
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

## Rollback rollback

loading...

POST

/`rollback.rollback`

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

rollbackId*string

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
curl -X POST "https://your-dokploy-instance.com/api/rollback.rollback" \  -H "Content-Type: application/json" \  -d '{    "rollbackId": "string"  }'
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

RegistryPrevious Page

ScheduleNext Page

```
curl -X POST "https://your-dokploy-instance.com/api/rollback.delete" \
  -H "Content-Type: application/json" \
  -d '{
    "rollbackId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/rollback.rollback" \
  -H "Content-Type: application/json" \
  -d '{
    "rollbackId": "string"
  }'
```