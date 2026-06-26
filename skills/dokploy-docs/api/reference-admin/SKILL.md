---
title: "Admin | Dokploy"
source: "https://docs.dokploy.com/docs/api/reference-admin"
category: dokploy-docs
created: "2026-06-25T17:21:34.548Z"
---

Admin | Dokploy

# Admin

Copy as Markdown

loading...

POST

/`admin.setupMonitoring`

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

metricsConfig*object

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
curl -X POST "https://your-dokploy-instance.com/api/admin.setupMonitoring" \  -H "Content-Type: application/json" \  -d '{    "metricsConfig": {      "server": {        "refreshRate": 2,        "port": 1,        "token": "string",        "urlCallback": "http://example.com",        "retentionDays": 1,        "cronJob": "string",        "thresholds": {          "cpu": 0,          "memory": 0        }      },      "containers": {        "refreshRate": 2,        "services": {}      }    }  }'
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