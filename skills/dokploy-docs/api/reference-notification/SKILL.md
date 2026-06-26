---
title: "Notification | Dokploy"
source: "https://docs.dokploy.com/docs/api/reference-notification"
category: dokploy-docs
created: "2026-06-25T17:21:35.748Z"
---

Notification | Dokploy

# Notification

Copy as Markdown

loading...

POST

/`notification.createSlack`

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

appBuildError*boolean

databaseBackup*boolean

dokployBackup*boolean

volumeBackup*boolean

dokployRestart*boolean

name*string

appDeploy*boolean

dockerCleanup*boolean

serverThreshold*boolean

webhookUrl*string

Length`1 <= length`

channel*string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.createSlack" \  -H "Content-Type: application/json" \  -d '{    "appBuildError": true,    "databaseBackup": true,    "dokployBackup": true,    "volumeBackup": true,    "dokployRestart": true,    "name": "string",    "appDeploy": true,    "dockerCleanup": true,    "serverThreshold": true,    "webhookUrl": "string",    "channel": "string"  }'
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

/`notification.updateSlack`

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

appBuildError?boolean

databaseBackup?boolean

dokployBackup?boolean

volumeBackup?boolean

dokployRestart?boolean

name?string

appDeploy?boolean

dockerCleanup?boolean

serverThreshold?boolean

webhookUrl?string

Length`1 <= length`

channel?string

notificationId*string

Length`1 <= length`

slackId*string

organizationId?string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.updateSlack" \  -H "Content-Type: application/json" \  -d '{    "notificationId": "string",    "slackId": "string"  }'
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

/`notification.testSlackConnection`

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

webhookUrl*string

Length`1 <= length`

channel*string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.testSlackConnection" \  -H "Content-Type: application/json" \  -d '{    "webhookUrl": "string",    "channel": "string"  }'
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

/`notification.createTelegram`

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

appBuildError*boolean

databaseBackup*boolean

dokployBackup*boolean

volumeBackup*boolean

dokployRestart*boolean

name*string

appDeploy*boolean

dockerCleanup*boolean

serverThreshold*boolean

botToken*string

Length`1 <= length`

chatId*string

Length`1 <= length`

messageThreadId*string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.createTelegram" \  -H "Content-Type: application/json" \  -d '{    "appBuildError": true,    "databaseBackup": true,    "dokployBackup": true,    "volumeBackup": true,    "dokployRestart": true,    "name": "string",    "appDeploy": true,    "dockerCleanup": true,    "serverThreshold": true,    "botToken": "string",    "chatId": "string",    "messageThreadId": "string"  }'
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

/`notification.updateTelegram`

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

appBuildError?boolean

databaseBackup?boolean

dokployBackup?boolean

volumeBackup?boolean

dokployRestart?boolean

name?string

appDeploy?boolean

dockerCleanup?boolean

serverThreshold?boolean

botToken?string

Length`1 <= length`

chatId?string

Length`1 <= length`

messageThreadId?string

notificationId*string

Length`1 <= length`

telegramId*string

Length`1 <= length`

organizationId?string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.updateTelegram" \  -H "Content-Type: application/json" \  -d '{    "notificationId": "string",    "telegramId": "string"  }'
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

/`notification.testTelegramConnection`

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

botToken*string

Length`1 <= length`

chatId*string

Length`1 <= length`

messageThreadId*string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.testTelegramConnection" \  -H "Content-Type: application/json" \  -d '{    "botToken": "string",    "chatId": "string",    "messageThreadId": "string"  }'
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

/`notification.createDiscord`

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

appBuildError*boolean

databaseBackup*boolean

dokployBackup*boolean

volumeBackup*boolean

dokployRestart*boolean

name*string

appDeploy*boolean

dockerCleanup*boolean

serverThreshold*boolean

webhookUrl*string

Length`1 <= length`

decoration*boolean

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
curl -X POST "https://your-dokploy-instance.com/api/notification.createDiscord" \  -H "Content-Type: application/json" \  -d '{    "appBuildError": true,    "databaseBackup": true,    "dokployBackup": true,    "volumeBackup": true,    "dokployRestart": true,    "name": "string",    "appDeploy": true,    "dockerCleanup": true,    "serverThreshold": true,    "webhookUrl": "string",    "decoration": true  }'
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

/`notification.updateDiscord`

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

appBuildError?boolean

databaseBackup?boolean

dokployBackup?boolean

volumeBackup?boolean

dokployRestart?boolean

name?string

appDeploy?boolean

dockerCleanup?boolean

serverThreshold?boolean

webhookUrl?string

Length`1 <= length`

decoration?boolean

notificationId*string

Length`1 <= length`

discordId*string

Length`1 <= length`

organizationId?string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.updateDiscord" \  -H "Content-Type: application/json" \  -d '{    "notificationId": "string",    "discordId": "string"  }'
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

/`notification.testDiscordConnection`

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

webhookUrl*string

Length`1 <= length`

decoration?boolean

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
curl -X POST "https://your-dokploy-instance.com/api/notification.testDiscordConnection" \  -H "Content-Type: application/json" \  -d '{    "webhookUrl": "string"  }'
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

/`notification.createEmail`

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

appBuildError*boolean

databaseBackup*boolean

dokployBackup*boolean

volumeBackup*boolean

dokployRestart*boolean

name*string

appDeploy*boolean

dockerCleanup*boolean

serverThreshold*boolean

smtpServer*string

Length`1 <= length`

smtpPort*number

Range`1 <= value`

username*string

Length`1 <= length`

password*string

Length`1 <= length`

fromAddress*string

Length`1 <= length`

toAddresses*array 

Items`1 <= items`

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
curl -X POST "https://your-dokploy-instance.com/api/notification.createEmail" \  -H "Content-Type: application/json" \  -d '{    "appBuildError": true,    "databaseBackup": true,    "dokployBackup": true,    "volumeBackup": true,    "dokployRestart": true,    "name": "string",    "appDeploy": true,    "dockerCleanup": true,    "serverThreshold": true,    "smtpServer": "string",    "smtpPort": 1,    "username": "string",    "password": "string",    "fromAddress": "string",    "toAddresses": [      "string"    ]  }'
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

/`notification.updateEmail`

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

appBuildError?boolean

databaseBackup?boolean

dokployBackup?boolean

volumeBackup?boolean

dokployRestart?boolean

name?string

appDeploy?boolean

dockerCleanup?boolean

serverThreshold?boolean

smtpServer?string

Length`1 <= length`

smtpPort?number

Range`1 <= value`

username?string

Length`1 <= length`

password?string

Length`1 <= length`

fromAddress?string

Length`1 <= length`

toAddresses?array 

Items`1 <= items`

notificationId*string

Length`1 <= length`

emailId*string

Length`1 <= length`

organizationId?string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.updateEmail" \  -H "Content-Type: application/json" \  -d '{    "notificationId": "string",    "emailId": "string"  }'
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

/`notification.testEmailConnection`

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

smtpServer*string

Length`1 <= length`

smtpPort*number

Range`1 <= value`

username*string

Length`1 <= length`

password*string

Length`1 <= length`

toAddresses*array 

Items`1 <= items`

fromAddress*string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.testEmailConnection" \  -H "Content-Type: application/json" \  -d '{    "smtpServer": "string",    "smtpPort": 1,    "username": "string",    "password": "string",    "toAddresses": [      "string"    ],    "fromAddress": "string"  }'
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

/`notification.remove`

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

notificationId*string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.remove" \  -H "Content-Type: application/json" \  -d '{    "notificationId": "string"  }'
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

/`notification.one`

Send

Authorization

Query

## Authorization

`x-api-key `

x-api-key 

API key authentication. Use YOUR-GENERATED-API-KEY

In:`header`

## Query Parameters

notificationId*string

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
curl -X GET "https://your-dokploy-instance.com/api/notification.one?notificationId=string"
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

GET

/`notification.all`

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
curl -X GET "https://your-dokploy-instance.com/api/notification.all"
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

/`notification.receiveNotification`

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

ServerType?string

Default`"Dokploy"`

Value in`"Dokploy" | "Remote"`

Type*string

Value in`"Memory" | "CPU"`

Value*number

Threshold*number

Message*string

Timestamp*string

Token*string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.receiveNotification" \  -H "Content-Type: application/json" \  -d '{    "Type": "Memory",    "Value": 0,    "Threshold": 0,    "Message": "string",    "Timestamp": "string",    "Token": "string"  }'
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

/`notification.createGotify`

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

appBuildError*boolean

databaseBackup*boolean

dokployBackup*boolean

volumeBackup*boolean

dokployRestart*boolean

name*string

appDeploy*boolean

dockerCleanup*boolean

serverUrl*string

Length`1 <= length`

appToken*string

Length`1 <= length`

priority*number

Range`1 <= value`

decoration*boolean

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
curl -X POST "https://your-dokploy-instance.com/api/notification.createGotify" \  -H "Content-Type: application/json" \  -d '{    "appBuildError": true,    "databaseBackup": true,    "dokployBackup": true,    "volumeBackup": true,    "dokployRestart": true,    "name": "string",    "appDeploy": true,    "dockerCleanup": true,    "serverUrl": "string",    "appToken": "string",    "priority": 1,    "decoration": true  }'
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

/`notification.updateGotify`

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

appBuildError?boolean

databaseBackup?boolean

dokployBackup?boolean

volumeBackup?boolean

dokployRestart?boolean

name?string

appDeploy?boolean

dockerCleanup?boolean

serverUrl?string

Length`1 <= length`

appToken?string

Length`1 <= length`

priority?number

Range`1 <= value`

decoration?boolean

notificationId*string

Length`1 <= length`

gotifyId*string

Length`1 <= length`

organizationId?string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.updateGotify" \  -H "Content-Type: application/json" \  -d '{    "notificationId": "string",    "gotifyId": "string"  }'
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

/`notification.testGotifyConnection`

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

serverUrl*string

Length`1 <= length`

appToken*string

Length`1 <= length`

priority*number

Range`1 <= value`

decoration?boolean

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
curl -X POST "https://your-dokploy-instance.com/api/notification.testGotifyConnection" \  -H "Content-Type: application/json" \  -d '{    "serverUrl": "string",    "appToken": "string",    "priority": 1  }'
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

/`notification.createNtfy`

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

appBuildError*boolean

databaseBackup*boolean

dokployBackup*boolean

volumeBackup*boolean

dokployRestart*boolean

name*string

appDeploy*boolean

dockerCleanup*boolean

serverUrl*string

Length`1 <= length`

topic*string

Length`1 <= length`

accessToken*string

priority*number

Range`1 <= value`

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
curl -X POST "https://your-dokploy-instance.com/api/notification.createNtfy" \  -H "Content-Type: application/json" \  -d '{    "appBuildError": true,    "databaseBackup": true,    "dokployBackup": true,    "volumeBackup": true,    "dokployRestart": true,    "name": "string",    "appDeploy": true,    "dockerCleanup": true,    "serverUrl": "string",    "topic": "string",    "accessToken": "string",    "priority": 1  }'
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

/`notification.updateNtfy`

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

appBuildError?boolean

databaseBackup?boolean

dokployBackup?boolean

volumeBackup?boolean

dokployRestart?boolean

name?string

appDeploy?boolean

dockerCleanup?boolean

serverUrl?string

Length`1 <= length`

topic?string

Length`1 <= length`

accessToken?string

priority?number

Range`1 <= value`

notificationId*string

Length`1 <= length`

ntfyId*string

Length`1 <= length`

organizationId?string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.updateNtfy" \  -H "Content-Type: application/json" \  -d '{    "notificationId": "string",    "ntfyId": "string"  }'
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

/`notification.testNtfyConnection`

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

serverUrl*string

Length`1 <= length`

topic*string

Length`1 <= length`

accessToken*string

priority*number

Range`1 <= value`

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
curl -X POST "https://your-dokploy-instance.com/api/notification.testNtfyConnection" \  -H "Content-Type: application/json" \  -d '{    "serverUrl": "string",    "topic": "string",    "accessToken": "string",    "priority": 1  }'
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

/`notification.createLark`

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

appBuildError*boolean

databaseBackup*boolean

dokployBackup*boolean

volumeBackup*boolean

dokployRestart*boolean

name*string

appDeploy*boolean

dockerCleanup*boolean

serverThreshold*boolean

webhookUrl*string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.createLark" \  -H "Content-Type: application/json" \  -d '{    "appBuildError": true,    "databaseBackup": true,    "dokployBackup": true,    "volumeBackup": true,    "dokployRestart": true,    "name": "string",    "appDeploy": true,    "dockerCleanup": true,    "serverThreshold": true,    "webhookUrl": "string"  }'
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

/`notification.updateLark`

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

appBuildError?boolean

databaseBackup?boolean

dokployBackup?boolean

volumeBackup?boolean

dokployRestart?boolean

name?string

appDeploy?boolean

dockerCleanup?boolean

serverThreshold?boolean

webhookUrl?string

Length`1 <= length`

notificationId*string

Length`1 <= length`

larkId*string

Length`1 <= length`

organizationId?string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.updateLark" \  -H "Content-Type: application/json" \  -d '{    "notificationId": "string",    "larkId": "string"  }'
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

/`notification.testLarkConnection`

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

webhookUrl*string

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
curl -X POST "https://your-dokploy-instance.com/api/notification.testLarkConnection" \  -H "Content-Type: application/json" \  -d '{    "webhookUrl": "string"  }'
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

/`notification.createPushover`

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

appBuildError?boolean

databaseBackup?boolean

dokployBackup?boolean

volumeBackup?boolean

dokployRestart?boolean

name*string

appDeploy?boolean

dockerCleanup?boolean

serverThreshold?boolean

userKey*string

Length`1 <= length`

apiToken*string

Length`1 <= length`

priority?number

Default`0`

Range`-2 <= value <= 2`

retry?number|null

expire?number|null

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
curl -X POST "https://your-dokploy-instance.com/api/notification.createPushover" \  -H "Content-Type: application/json" \  -d '{    "name": "string",    "userKey": "string",    "apiToken": "string"  }'
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

/`notification.updatePushover`

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

notificationId*string

Length`1 <= length`

pushoverId*string

Length`1 <= length`

organizationId?string

userKey?string

Length`1 <= length`

apiToken?string

Length`1 <= length`

priority?number

Range`-2 <= value <= 2`

retry?number|null

expire?number|null

appBuildError?boolean

databaseBackup?boolean

dokployBackup?boolean

volumeBackup?boolean

dokployRestart?boolean

name?string

appDeploy?boolean

dockerCleanup?boolean

serverThreshold?boolean

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
curl -X POST "https://your-dokploy-instance.com/api/notification.updatePushover" \  -H "Content-Type: application/json" \  -d '{    "notificationId": "string",    "pushoverId": "string"  }'
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

/`notification.testPushoverConnection`

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

userKey*string

Length`1 <= length`

apiToken*string

Length`1 <= length`

priority*number

Range`-2 <= value <= 2`

retry?number|null

expire?number|null

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
curl -X POST "https://your-dokploy-instance.com/api/notification.testPushoverConnection" \  -H "Content-Type: application/json" \  -d '{    "userKey": "string",    "apiToken": "string",    "priority": -2  }'
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

/`notification.getEmailProviders`

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
curl -X GET "https://your-dokploy-instance.com/api/notification.getEmailProviders"
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

```
curl -X POST "https://your-dokploy-instance.com/api/notification.createSlack" \
  -H "Content-Type: application/json" \
  -d '{
    "appBuildError": true,
    "databaseBackup": true,
    "dokployBackup": true,
    "volumeBackup": true,
    "dokployRestart": true,
    "name": "string",
    "appDeploy": true,
    "dockerCleanup": true,
    "serverThreshold": true,
    "webhookUrl": "string",
    "channel": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.updateSlack" \
  -H "Content-Type: application/json" \
  -d '{
    "notificationId": "string",
    "slackId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.testSlackConnection" \
  -H "Content-Type: application/json" \
  -d '{
    "webhookUrl": "string",
    "channel": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.createTelegram" \
  -H "Content-Type: application/json" \
  -d '{
    "appBuildError": true,
    "databaseBackup": true,
    "dokployBackup": true,
    "volumeBackup": true,
    "dokployRestart": true,
    "name": "string",
    "appDeploy": true,
    "dockerCleanup": true,
    "serverThreshold": true,
    "botToken": "string",
    "chatId": "string",
    "messageThreadId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.updateTelegram" \
  -H "Content-Type: application/json" \
  -d '{
    "notificationId": "string",
    "telegramId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.testTelegramConnection" \
  -H "Content-Type: application/json" \
  -d '{
    "botToken": "string",
    "chatId": "string",
    "messageThreadId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.createDiscord" \
  -H "Content-Type: application/json" \
  -d '{
    "appBuildError": true,
    "databaseBackup": true,
    "dokployBackup": true,
    "volumeBackup": true,
    "dokployRestart": true,
    "name": "string",
    "appDeploy": true,
    "dockerCleanup": true,
    "serverThreshold": true,
    "webhookUrl": "string",
    "decoration": true
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.updateDiscord" \
  -H "Content-Type: application/json" \
  -d '{
    "notificationId": "string",
    "discordId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.testDiscordConnection" \
  -H "Content-Type: application/json" \
  -d '{
    "webhookUrl": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.createEmail" \
  -H "Content-Type: application/json" \
  -d '{
    "appBuildError": true,
    "databaseBackup": true,
    "dokployBackup": true,
    "volumeBackup": true,
    "dokployRestart": true,
    "name": "string",
    "appDeploy": true,
    "dockerCleanup": true,
    "serverThreshold": true,
    "smtpServer": "string",
    "smtpPort": 1,
    "username": "string",
    "password": "string",
    "fromAddress": "string",
    "toAddresses": [
      "string"
    ]
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.updateEmail" \
  -H "Content-Type: application/json" \
  -d '{
    "notificationId": "string",
    "emailId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.testEmailConnection" \
  -H "Content-Type: application/json" \
  -d '{
    "smtpServer": "string",
    "smtpPort": 1,
    "username": "string",
    "password": "string",
    "toAddresses": [
      "string"
    ],
    "fromAddress": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.remove" \
  -H "Content-Type: application/json" \
  -d '{
    "notificationId": "string"
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/notification.one?notificationId=string"
```

```
curl -X GET "https://your-dokploy-instance.com/api/notification.all"
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.receiveNotification" \
  -H "Content-Type: application/json" \
  -d '{
    "Type": "Memory",
    "Value": 0,
    "Threshold": 0,
    "Message": "string",
    "Timestamp": "string",
    "Token": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.createGotify" \
  -H "Content-Type: application/json" \
  -d '{
    "appBuildError": true,
    "databaseBackup": true,
    "dokployBackup": true,
    "volumeBackup": true,
    "dokployRestart": true,
    "name": "string",
    "appDeploy": true,
    "dockerCleanup": true,
    "serverUrl": "string",
    "appToken": "string",
    "priority": 1,
    "decoration": true
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.updateGotify" \
  -H "Content-Type: application/json" \
  -d '{
    "notificationId": "string",
    "gotifyId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.testGotifyConnection" \
  -H "Content-Type: application/json" \
  -d '{
    "serverUrl": "string",
    "appToken": "string",
    "priority": 1
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.createNtfy" \
  -H "Content-Type: application/json" \
  -d '{
    "appBuildError": true,
    "databaseBackup": true,
    "dokployBackup": true,
    "volumeBackup": true,
    "dokployRestart": true,
    "name": "string",
    "appDeploy": true,
    "dockerCleanup": true,
    "serverUrl": "string",
    "topic": "string",
    "accessToken": "string",
    "priority": 1
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.updateNtfy" \
  -H "Content-Type: application/json" \
  -d '{
    "notificationId": "string",
    "ntfyId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.testNtfyConnection" \
  -H "Content-Type: application/json" \
  -d '{
    "serverUrl": "string",
    "topic": "string",
    "accessToken": "string",
    "priority": 1
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.createLark" \
  -H "Content-Type: application/json" \
  -d '{
    "appBuildError": true,
    "databaseBackup": true,
    "dokployBackup": true,
    "volumeBackup": true,
    "dokployRestart": true,
    "name": "string",
    "appDeploy": true,
    "dockerCleanup": true,
    "serverThreshold": true,
    "webhookUrl": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.updateLark" \
  -H "Content-Type: application/json" \
  -d '{
    "notificationId": "string",
    "larkId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.testLarkConnection" \
  -H "Content-Type: application/json" \
  -d '{
    "webhookUrl": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.createPushover" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "string",
    "userKey": "string",
    "apiToken": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.updatePushover" \
  -H "Content-Type: application/json" \
  -d '{
    "notificationId": "string",
    "pushoverId": "string"
  }'
```

```
curl -X POST "https://your-dokploy-instance.com/api/notification.testPushoverConnection" \
  -H "Content-Type: application/json" \
  -d '{
    "userKey": "string",
    "apiToken": "string",
    "priority": -2
  }'
```

```
curl -X GET "https://your-dokploy-instance.com/api/notification.getEmailProviders"
```