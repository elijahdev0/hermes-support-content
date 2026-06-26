---
title: "Redirects | Dokploy"
source: "https://docs.dokploy.com/docs/api/redirects"
category: dokploy-docs
created: "2026-06-25T17:16:08.646Z"
---

Redirects | Dokploy

# Redirects

Copy as Markdown

## Redirects create

loading...

POST

/`redirects.create`

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

regex*string

Length`1 <= length`

replacement*string

Length`1 <= length`

permanent*boolean

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
curl -X POST "https://your-dokploy-instance.com/api/redirects.create" \  -H "Content-Type: application/json" \  -d '{    "regex": "string",    "replacement": "string",    "permanent": true,    "applicationId": "string"  }'
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

## Redirects one

loading...

GET

/`redirects.one`

Send

Authorization

Query

### Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

### Query Parameters

redirectId*string

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
curl -X GET "https://your-dokploy-instance.com/api/redirects.one?redirectId=string"
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

## Redirects delete

loading...

POST

/`redirects.delete`

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

redirectId*string

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
curl -X POST "https://your-dokploy-instance.com/api/redirects.delete" \  -H "Content-Type: application/json" \  -d '{    "redirectId": "string"  }'
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

## Redirects update

loading...

POST

/`redirects.update`

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

redirectId*string

Length`1 <= length`

regex*string

Length`1 <= length`

replacement*string

Length`1 <= length`

permanent*boolean

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
curl -X POST "https://your-dokploy-instance.com/api/redirects.update" \  -H "Content-Type: application/json" \  -d '{    "redirectId": "string",    "regex": "string",    "replacement": "string",    "permanent": true  }'
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

ProjectPrevious Page

RedisNext Page

```
curl -X POST "https://your-dokploy-instance.com/api/redirects.create" \
  -H "Content-Type: application/json" \
  -d '{
    "regex": "string",
    "replacement": "string",
    "permanent": true,
    "applicationId": "string"
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/redirects.one?redirectId=string"
```

```
curl -X POST "https://your-dokploy-instance.com/api/redirects.delete" \
  -H "Content-Type: application/json" \
  -d '{
    "redirectId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/redirects.update" \
  -H "Content-Type: application/json" \
  -d '{
    "redirectId": "string",
    "regex": "string",
    "replacement": "string",
    "permanent": true
  }'
```