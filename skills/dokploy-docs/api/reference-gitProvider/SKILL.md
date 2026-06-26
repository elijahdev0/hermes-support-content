---
title: "Git Provider | Dokploy"
source: "https://docs.dokploy.com/docs/api/reference-gitProvider"
category: dokploy-docs
created: "2026-06-25T17:21:34.550Z"
---

Git Provider | Dokploy

# Git Provider

Copy as Markdown

loading...

GET

/`gitProvider.getAll`

Send

Authorization

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

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
curl -X GET "https://your-dokploy-instance.com/api/gitProvider.getAll"
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

/`gitProvider.remove`

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

gitProviderId*string

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
curl -X POST "https://your-dokploy-instance.com/api/gitProvider.remove" \  -H "Content-Type: application/json" \  -d '{    "gitProviderId": "string"  }'
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
curl -X GET "https://your-dokploy-instance.com/api/gitProvider.getAll"
```

```
curl -X POST "https://your-dokploy-instance.com/api/gitProvider.remove" \
  -H "Content-Type: application/json" \
  -d '{
    "gitProviderId": "string"
  }'
```