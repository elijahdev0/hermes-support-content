---
title: "Port | Dokploy"
source: "https://docs.dokploy.com/docs/api/reference-port"
category: dokploy-docs
created: "2026-06-25T17:21:35.748Z"
---

Port | Dokploy

# Port

Copy as Markdown

loading...

POST

/`port.create`

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

publishedPort*number

publishMode*string

Default`"ingress"`

Value in`"ingress" | "host"`

targetPort*number

protocol*string

Default`"tcp"`

Value in`"tcp" | "udp"`

applicationId*string

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
curl -X POST "https://your-dokploy-instance.com/api/port.create" \  -H "Content-Type: application/json" \  -d '{    "publishedPort": 0,    "publishMode": "ingress",    "targetPort": 0,    "protocol": "tcp",    "applicationId": "string"  }'
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

/`port.one`

Send

Authorization

Query

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Query Parameters

portId*string

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
curl -X GET "https://your-dokploy-instance.com/api/port.one?portId=string"
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

/`port.delete`

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

portId*string

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
curl -X POST "https://your-dokploy-instance.com/api/port.delete" \  -H "Content-Type: application/json" \  -d '{    "portId": "string"  }'
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

/`port.update`

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

portId*string

Length`1 <= length`

publishedPort*number

publishMode*string

Default`"ingress"`

Value in`"ingress" | "host"`

targetPort*number

protocol*string

Default`"tcp"`

Value in`"tcp" | "udp"`

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
curl -X POST "https://your-dokploy-instance.com/api/port.update" \  -H "Content-Type: application/json" \  -d '{    "portId": "string",    "publishedPort": 0,    "publishMode": "ingress",    "targetPort": 0,    "protocol": "tcp"  }'
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

OrganizationPrevious Page

PostgresNext Page

```
curl -X POST "https://your-dokploy-instance.com/api/port.create" \
  -H "Content-Type: application/json" \
  -d '{
    "publishedPort": 0,
    "publishMode": "ingress",
    "targetPort": 0,
    "protocol": "tcp",
    "applicationId": "string"
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/port.one?portId=string"
```

```
curl -X POST "https://your-dokploy-instance.com/api/port.delete" \
  -H "Content-Type: application/json" \
  -d '{
    "portId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/port.update" \
  -H "Content-Type: application/json" \
  -d '{
    "portId": "string",
    "publishedPort": 0,
    "publishMode": "ingress",
    "targetPort": 0,
    "protocol": "tcp"
  }'
```