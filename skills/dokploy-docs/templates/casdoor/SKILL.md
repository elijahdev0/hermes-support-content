---
title: "Casdoor | Dokploy"
source: "https://docs.dokploy.com/docs/templates/casdoor"
category: dokploy-docs
created: "2026-06-25T17:21:43.962Z"
---

Casdoor | Dokploy

# Casdoor

Copy as Markdown

An open-source UI-first Identity and Access Management (IAM) / Single-Sign-On (SSO) platform with web UI supporting OAuth 2.0, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, and more.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  casdoor:
    image: casbin/casdoor:latest
    environment:
      - RUNNING_IN_DOCKER=true
    volumes:
      - ../files/app.conf:/conf/app.conf
      - ../files/init_data.json:/init_data.json
      - casdoor-data:/data
    depends_on:
      casdoor-db:
        condition: service_healthy
    restart: unless-stopped

  casdoor-db:
    image: postgres:16
    environment:
      - POSTGRES_USER=casdoor
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_DB=casdoor
    volumes:
      - casdoor-postgres-data:/var/lib/postgresql/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U casdoor -d casdoor"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

volumes:
  casdoor-postgres-data:
  casdoor-data:
```

```
[variables]
postgres_password = "${password:32}"
admin_password = "${password:16}"
jwt_secret = "${password:64}"
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "casdoor"
port = 8000
host = "${main_domain}"

[config.env]
POSTGRES_PASSWORD = "${postgres_password}"
ADMIN_FIRST_LOGIN_PASSWD = "${admin_password}"

[[config.mounts]]
filePath = "app.conf"
content = """
appname = casdoor
httpport = 8000
runmode = prod
SessionOn = true
copyrequestbody = true
driverName = postgres
dataSourceName = user=casdoor password=${postgres_password} host=casdoor-db port=5432 sslmode=disable dbname=casdoor
dbName = casdoor
showSql = false
redisEndpoint =
defaultStorageProvider =
isCloudIntranet = false
authState = "casdoor"
socks5Proxy = "127.0.0.1:10808"
verificationCodeTimeout = 10
initData = "./init_data.json"
logPostOnly = true
isUsernameLowered = false
origin = "https://${main_domain}"
staticBaseUrl = "https://cdn.casbin.org"
isDemoMode = false
batchSize = 100
enableGzip = true
ldapServerPort = 389
radiusServerPort = 1812
radiusSecret = "secret"
quota = {"organization": -1, "user": -1, "application": -1, "provider": -1}
logConfig = {"filename": "logs/casdoor.log", "maxdays":99999, "perm":"0770"}
initDataFile = "./init_data.json"
frontendBaseDir = "../web/build"
"""

[[config.mounts]]
filePath = "init_data.json"
content = """
{
  "organizations": [
    {
      "owner": "admin",
      "name": "built-in",
      "createdTime": "2021-01-01T00:00:00Z",
      "displayName": "Built-in Organization",
      "websiteUrl": "https://casdoor.org",
      "favicon": "https://cdn.casbin.org/img/casbin/favicon.ico",
      "passwordType": "plain",
      "passwordOptions": ["AtLeast6"],
      "countryCode": "US",
      "defaultAvatar": "https://cdn.casbin.org/img/casbin/user.png",
      "defaultApplication": "app-built-in",
      "tags": [],
      "languages": ["en"],
      "themeData": {
        "isCompact": false,
        "isEnabled": false,
        "themeType": "default",
        "colorPrimary": "#1976d2",
        "borderRadius": 6,
        "isRoundedButton": false,
        "isGradientButton": false,
        "themeAlgorithm": "default"
      },
      "masterPassword": "",
      "initScore": 2000,
      "enableSoftDeletion": false,
      "isProfilePublic": false,
      "mfaItems": [],
      "accountItems": [
        {
          "name": "Organization",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Admin"
        },
        {
          "name": "ID",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Immutable"
        },
        {
          "name": "Name",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Admin"
        },
        {
          "name": "Display name",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Avatar",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "User type",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Admin"
        },
        {
          "name": "Password",
          "visible": true,
          "viewRule": "Self",
          "modifyRule": "Self"
        },
        {
          "name": "Email",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Phone",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Country/Region",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Location",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Affiliation",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Title",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Homepage",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Bio",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Tag",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Admin"
        },
        {
          "name": "Language",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Gender",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Birthday",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Education",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Self"
        },
        {
          "name": "Score",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Admin"
        },
        {
          "name": "Karma",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Admin"
        },
        {
          "name": "Ranking",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Admin"
        },
        {
          "name": "Signup application",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Admin"
        },
        {
          "name": "Roles",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Immutable"
        },
        {
          "name": "Permissions",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Immutable"
        },
        {
          "name": "Groups",
          "visible": true,
          "viewRule": "Public",
          "modifyRule": "Admin"
        },
        {
          "name": "3rd-party logins",
          "visible": true,
          "viewRule": "Self",
          "modifyRule": "Self"
        },
        {
          "name": "Properties",
          "visible": false,
          "viewRule": "Admin",
          "modifyRule": "Admin"
        },
        {
          "name": "Is admin",
          "visible": true,
          "viewRule": "Admin",
          "modifyRule": "Admin"
        },
        {
          "name": "Is forbidden",
          "visible": true,
          "viewRule": "Admin",
          "modifyRule": "Admin"
        },
        {
          "name": "Is deleted",
          "visible": true,
          "viewRule": "Admin",
          "modifyRule": "Admin"
        },
        {
          "name": "Multi-factor authentication",
          "visible": true,
          "viewRule": "Self",
          "modifyRule": "Self"
        },
        {
          "name": "WebAuthn credentials",
          "visible": true,
          "viewRule": "Self",
          "modifyRule": "Self"
        },
        {
          "name": "Managed accounts",
          "visible": true,
          "viewRule": "Self",
          "modifyRule": "Self"
        }
      ]
    }
  ],
  "users": [
    {
      "owner": "built-in",
      "name": "admin",
      "createdTime": "2021-01-01T00:00:00Z",
      "updatedTime": "2021-01-01T00:00:00Z",
      "id": "admin",
      "type": "normal-user",
      "password": "${admin_password}",
      "passwordSalt": "",
      "displayName": "Admin",
      "firstName": "",
      "lastName": "",
      "avatar": "https://cdn.casbin.org/img/casbin/user.png",
      "permanentAvatar": "",
      "email": "[email protected]",
      "emailVerified": true,
      "phone": "",
      "location": "",
      "address": [],
      "affiliation": "Example Inc.",
      "title": "Administrator",
      "idCardType": "",
      "idCard": "",
      "homepage": "",
      "bio": "",
      "tag": "staff",
      "region": "US",
      "language": "en",
      "gender": "",
      "birthday": "",
      "education": "",
      "score": 2000,
      "karma": 0,
      "ranking": 1,
      "isDefaultAvatar": false,
      "isOnline": false,
      "isAdmin": true,
      "isGlobalAdmin": true,
      "isForbidden": false,
      "isDeleted": false,
      "signupApplication": "app-built-in",
      "hash": "",
      "preHash": "",
      "createdIp": "",
      "lastSigninTime": "",
      "lastSigninIp": "",
      "github": "",
      "google": "",
      "qq": "",
      "wechat": "",
      "facebook": "",
      "dingtalk": "",
      "weibo": "",
      "gitee": "",
      "linkedin": "",
      "wecom": "",
      "lark": "",
      "gitlab": "",
      "adfs": "",
      "baidu": "",
      "alipay": "",
      "casdoor": "",
      "infoflow": "",
      "apple": "",
      "azuread": "",
      "slack": "",
      "steam": "",
      "bilibili": "",
      "okta": "",
      "douyin": "",
      "custom": "",
      "webauthnCredentials": [],
      "preferredMfaType": "",
      "recoveryCodes": [],
      "totpSecret": "",
      "mfaPhoneEnabled": false,
      "mfaEmailEnabled": false,
      "ldap": "",
      "properties": {},
      "roles": [],
      "permissions": [],
      "groups": [],
      "lastSigninWrongTime": "",
      "signinWrongTimes": 0,
      "managedAccounts": []
    }
  ],
  "applications": [
    {
      "owner": "built-in",
      "name": "app-built-in",
      "createdTime": "2021-01-01T00:00:00Z",
      "displayName": "Casdoor",
      "logo": "https://cdn.casbin.org/img/casbin/favicon.ico",
      "homepageUrl": "https://${main_domain}",
      "description": "Casdoor - A UI-first Identity Access Management (IAM) / Single-Sign-On (SSO) platform",
      "organization": "built-in",
      "cert": "",
      "enablePassword": true,
      "enableSignUp": true,
      "enableSigninSession": false,
      "enableAutoSignin": false,
      "enableCodeSignin": false,
      "enableSamlCompress": false,
      "enableWebAuthn": false,
      "enableLinkWithEmail": false,
      "samlReplyUrl": "",
      "providers": [],
      "signupItems": [
        {
          "name": "ID",
          "visible": false,
          "required": true,
          "prompted": false,
          "rule": "Random"
        },
        {
          "name": "Username",
          "visible": true,
          "required": true,
          "prompted": false,
          "rule": "None"
        },
        {
          "name": "Display name",
          "visible": true,
          "required": true,
          "prompted": false,
          "rule": "None"
        },
        {
          "name": "Password",
          "visible": true,
          "required": true,
          "prompted": false,
          "rule": "None"
        },
        {
          "name": "Confirm password",
          "visible": true,
          "required": true,
          "prompted": false,
          "rule": "None"
        },
        {
          "name": "Email",
          "visible": true,
          "required": true,
          "prompted": false,
          "rule": "None"
        },
        {
          "name": "Phone",
          "visible": true,
          "required": true,
          "prompted": false,
          "rule": "None"
        },
        {
          "name": "Agreement",
          "visible": true,
          "required": true,
          "prompted": false,
          "rule": "None"
        }
      ],
      "grantTypes": [
        "authorization_code",
        "password",
        "client_credentials",
        "token",
        "id_token"
      ],
      "organizationObj": {
        "owner": "admin",
        "name": "built-in",
        "createdTime": "2021-01-01T00:00:00Z",
        "displayName": "Built-in Organization"
      },
      "tags": [],
      "clientId": "${jwt_secret}",
      "clientSecret": "${jwt_secret}",
      "redirectUris": ["https://${main_domain}/callback"],
      "tokenFormat": "JWT",
      "tokenFields": [],
      "expireInHours": 168,
      "refreshExpireInHours": 168,
      "signupUrl": "",
      "signinUrl": "",
      "forgetUrl": "",
      "affiliationUrl": "",
      "termsOfUse": "",
      "privacyPolicy": "",
      "tokenFields": [],
      "themeData": {
        "isCompact": false,
        "isEnabled": false,
        "themeType": "default",
        "colorPrimary": "#1976d2",
        "borderRadius": 6,
        "isRoundedButton": false,
        "isGradientButton": false,
        "themeAlgorithm": "default"
      },
      "formCss": "",
      "formCssMobile": "",
      "formOffset": 2,
      "formSideHtml": "",
      "formBackgroundUrl": ""
    }
  ],
  "certs": [],
  "providers": [],
  "ldaps": [],
  "models": [],
  "permissions": [],
  "roles": [],
  "groups": [],
  "enforcers": [],
  "tokens": [],
  "sessions": [],
  "payments": [],
  "products": [],
  "resources": [],
  "synceers": [],
  "adapters": [],
  "webhooks": [],
  "subscriptions": [],
  "plans": [],
  "pricings": [],
  "invitations": []
}
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBjYXNkb29yOlxuICAgIGltYWdlOiBjYXNiaW4vY2FzZG9vcjpsYXRlc3RcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUlVOTklOR19JTl9ET0NLRVI9dHJ1ZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL2FwcC5jb25mOi9jb25mL2FwcC5jb25mXG4gICAgICAtIC4uL2ZpbGVzL2luaXRfZGF0YS5qc29uOi9pbml0X2RhdGEuanNvblxuICAgICAgLSBjYXNkb29yLWRhdGE6L2RhdGFcbiAgICBkZXBlbmRzX29uOlxuICAgICAgY2FzZG9vci1kYjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gIGNhc2Rvb3ItZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE2XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX1VTRVI9Y2FzZG9vclxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgLSBQT1NUR1JFU19EQj1jYXNkb29yXG4gICAgdm9sdW1lczpcbiAgICAgIC0gY2FzZG9vci1wb3N0Z3Jlcy1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5IC1VIGNhc2Rvb3IgLWQgY2FzZG9vclwiXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcbiAgICAgIHN0YXJ0X3BlcmlvZDogMzBzXG5cbnZvbHVtZXM6XG4gIGNhc2Rvb3ItcG9zdGdyZXMtZGF0YTpcbiAgY2FzZG9vci1kYXRhOiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmFkbWluX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5qd3Rfc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjY0fVwiXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImNhc2Rvb3JcIlxucG9ydCA9IDgwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtwb3N0Z3Jlc19wYXNzd29yZH1cIlxuQURNSU5fRklSU1RfTE9HSU5fUEFTU1dEID0gXCIke2FkbWluX3Bhc3N3b3JkfVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiYXBwLmNvbmZcIlxuY29udGVudCA9IFwiXCJcIlxuYXBwbmFtZSA9IGNhc2Rvb3Jcbmh0dHBwb3J0ID0gODAwMFxucnVubW9kZSA9IHByb2RcblNlc3Npb25PbiA9IHRydWVcbmNvcHlyZXF1ZXN0Ym9keSA9IHRydWVcbmRyaXZlck5hbWUgPSBwb3N0Z3Jlc1xuZGF0YVNvdXJjZU5hbWUgPSB1c2VyPWNhc2Rvb3IgcGFzc3dvcmQ9JHtwb3N0Z3Jlc19wYXNzd29yZH0gaG9zdD1jYXNkb29yLWRiIHBvcnQ9NTQzMiBzc2xtb2RlPWRpc2FibGUgZGJuYW1lPWNhc2Rvb3JcbmRiTmFtZSA9IGNhc2Rvb3JcbnNob3dTcWwgPSBmYWxzZVxucmVkaXNFbmRwb2ludCA9XG5kZWZhdWx0U3RvcmFnZVByb3ZpZGVyID1cbmlzQ2xvdWRJbnRyYW5ldCA9IGZhbHNlXG5hdXRoU3RhdGUgPSBcImNhc2Rvb3JcIlxuc29ja3M1UHJveHkgPSBcIjEyNy4wLjAuMToxMDgwOFwiXG52ZXJpZmljYXRpb25Db2RlVGltZW91dCA9IDEwXG5pbml0RGF0YSA9IFwiLi9pbml0X2RhdGEuanNvblwiXG5sb2dQb3N0T25seSA9IHRydWVcbmlzVXNlcm5hbWVMb3dlcmVkID0gZmFsc2Vcbm9yaWdpbiA9IFwiaHR0cHM6Ly8ke21haW5fZG9tYWlufVwiXG5zdGF0aWNCYXNlVXJsID0gXCJodHRwczovL2Nkbi5jYXNiaW4ub3JnXCJcbmlzRGVtb01vZGUgPSBmYWxzZVxuYmF0Y2hTaXplID0gMTAwXG5lbmFibGVHemlwID0gdHJ1ZVxubGRhcFNlcnZlclBvcnQgPSAzODlcbnJhZGl1c1NlcnZlclBvcnQgPSAxODEyXG5yYWRpdXNTZWNyZXQgPSBcInNlY3JldFwiXG5xdW90YSA9IHtcIm9yZ2FuaXphdGlvblwiOiAtMSwgXCJ1c2VyXCI6IC0xLCBcImFwcGxpY2F0aW9uXCI6IC0xLCBcInByb3ZpZGVyXCI6IC0xfVxubG9nQ29uZmlnID0ge1wiZmlsZW5hbWVcIjogXCJsb2dzL2Nhc2Rvb3IubG9nXCIsIFwibWF4ZGF5c1wiOjk5OTk5LCBcInBlcm1cIjpcIjA3NzBcIn1cbmluaXREYXRhRmlsZSA9IFwiLi9pbml0X2RhdGEuanNvblwiXG5mcm9udGVuZEJhc2VEaXIgPSBcIi4uL3dlYi9idWlsZFwiXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCJpbml0X2RhdGEuanNvblwiXG5jb250ZW50ID0gXCJcIlwiXG57XG4gIFwib3JnYW5pemF0aW9uc1wiOiBbXG4gICAge1xuICAgICAgXCJvd25lclwiOiBcImFkbWluXCIsXG4gICAgICBcIm5hbWVcIjogXCJidWlsdC1pblwiLFxuICAgICAgXCJjcmVhdGVkVGltZVwiOiBcIjIwMjEtMDEtMDFUMDA6MDA6MDBaXCIsXG4gICAgICBcImRpc3BsYXlOYW1lXCI6IFwiQnVpbHQtaW4gT3JnYW5pemF0aW9uXCIsXG4gICAgICBcIndlYnNpdGVVcmxcIjogXCJodHRwczovL2Nhc2Rvb3Iub3JnXCIsXG4gICAgICBcImZhdmljb25cIjogXCJodHRwczovL2Nkbi5jYXNiaW4ub3JnL2ltZy9jYXNiaW4vZmF2aWNvbi5pY29cIixcbiAgICAgIFwicGFzc3dvcmRUeXBlXCI6IFwicGxhaW5cIixcbiAgICAgIFwicGFzc3dvcmRPcHRpb25zXCI6IFtcIkF0TGVhc3Q2XCJdLFxuICAgICAgXCJjb3VudHJ5Q29kZVwiOiBcIlVTXCIsXG4gICAgICBcImRlZmF1bHRBdmF0YXJcIjogXCJodHRwczovL2Nkbi5jYXNiaW4ub3JnL2ltZy9jYXNiaW4vdXNlci5wbmdcIixcbiAgICAgIFwiZGVmYXVsdEFwcGxpY2F0aW9uXCI6IFwiYXBwLWJ1aWx0LWluXCIsXG4gICAgICBcInRhZ3NcIjogW10sXG4gICAgICBcImxhbmd1YWdlc1wiOiBbXCJlblwiXSxcbiAgICAgIFwidGhlbWVEYXRhXCI6IHtcbiAgICAgICAgXCJpc0NvbXBhY3RcIjogZmFsc2UsXG4gICAgICAgIFwiaXNFbmFibGVkXCI6IGZhbHNlLFxuICAgICAgICBcInRoZW1lVHlwZVwiOiBcImRlZmF1bHRcIixcbiAgICAgICAgXCJjb2xvclByaW1hcnlcIjogXCIjMTk3NmQyXCIsXG4gICAgICAgIFwiYm9yZGVyUmFkaXVzXCI6IDYsXG4gICAgICAgIFwiaXNSb3VuZGVkQnV0dG9uXCI6IGZhbHNlLFxuICAgICAgICBcImlzR3JhZGllbnRCdXR0b25cIjogZmFsc2UsXG4gICAgICAgIFwidGhlbWVBbGdvcml0aG1cIjogXCJkZWZhdWx0XCJcbiAgICAgIH0sXG4gICAgICBcIm1hc3RlclBhc3N3b3JkXCI6IFwiXCIsXG4gICAgICBcImluaXRTY29yZVwiOiAyMDAwLFxuICAgICAgXCJlbmFibGVTb2Z0RGVsZXRpb25cIjogZmFsc2UsXG4gICAgICBcImlzUHJvZmlsZVB1YmxpY1wiOiBmYWxzZSxcbiAgICAgIFwibWZhSXRlbXNcIjogW10sXG4gICAgICBcImFjY291bnRJdGVtc1wiOiBbXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCJPcmdhbml6YXRpb25cIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInZpZXdSdWxlXCI6IFwiUHVibGljXCIsXG4gICAgICAgICAgXCJtb2RpZnlSdWxlXCI6IFwiQWRtaW5cIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiSURcIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInZpZXdSdWxlXCI6IFwiUHVibGljXCIsXG4gICAgICAgICAgXCJtb2RpZnlSdWxlXCI6IFwiSW1tdXRhYmxlXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIk5hbWVcIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInZpZXdSdWxlXCI6IFwiUHVibGljXCIsXG4gICAgICAgICAgXCJtb2RpZnlSdWxlXCI6IFwiQWRtaW5cIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiRGlzcGxheSBuYW1lXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlB1YmxpY1wiLFxuICAgICAgICAgIFwibW9kaWZ5UnVsZVwiOiBcIlNlbGZcIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiQXZhdGFyXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlB1YmxpY1wiLFxuICAgICAgICAgIFwibW9kaWZ5UnVsZVwiOiBcIlNlbGZcIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiVXNlciB0eXBlXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlB1YmxpY1wiLFxuICAgICAgICAgIFwibW9kaWZ5UnVsZVwiOiBcIkFkbWluXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIlBhc3N3b3JkXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlNlbGZcIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJTZWxmXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIkVtYWlsXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlB1YmxpY1wiLFxuICAgICAgICAgIFwibW9kaWZ5UnVsZVwiOiBcIlNlbGZcIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiUGhvbmVcIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInZpZXdSdWxlXCI6IFwiUHVibGljXCIsXG4gICAgICAgICAgXCJtb2RpZnlSdWxlXCI6IFwiU2VsZlwiXG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCJDb3VudHJ5L1JlZ2lvblwiLFxuICAgICAgICAgIFwidmlzaWJsZVwiOiB0cnVlLFxuICAgICAgICAgIFwidmlld1J1bGVcIjogXCJQdWJsaWNcIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJTZWxmXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIkxvY2F0aW9uXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlB1YmxpY1wiLFxuICAgICAgICAgIFwibW9kaWZ5UnVsZVwiOiBcIlNlbGZcIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiQWZmaWxpYXRpb25cIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInZpZXdSdWxlXCI6IFwiUHVibGljXCIsXG4gICAgICAgICAgXCJtb2RpZnlSdWxlXCI6IFwiU2VsZlwiXG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCJUaXRsZVwiLFxuICAgICAgICAgIFwidmlzaWJsZVwiOiB0cnVlLFxuICAgICAgICAgIFwidmlld1J1bGVcIjogXCJQdWJsaWNcIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJTZWxmXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIkhvbWVwYWdlXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlB1YmxpY1wiLFxuICAgICAgICAgIFwibW9kaWZ5UnVsZVwiOiBcIlNlbGZcIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiQmlvXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlB1YmxpY1wiLFxuICAgICAgICAgIFwibW9kaWZ5UnVsZVwiOiBcIlNlbGZcIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiVGFnXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlB1YmxpY1wiLFxuICAgICAgICAgIFwibW9kaWZ5UnVsZVwiOiBcIkFkbWluXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIkxhbmd1YWdlXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlB1YmxpY1wiLFxuICAgICAgICAgIFwibW9kaWZ5UnVsZVwiOiBcIlNlbGZcIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiR2VuZGVyXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlB1YmxpY1wiLFxuICAgICAgICAgIFwibW9kaWZ5UnVsZVwiOiBcIlNlbGZcIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiQmlydGhkYXlcIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInZpZXdSdWxlXCI6IFwiUHVibGljXCIsXG4gICAgICAgICAgXCJtb2RpZnlSdWxlXCI6IFwiU2VsZlwiXG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCJFZHVjYXRpb25cIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInZpZXdSdWxlXCI6IFwiUHVibGljXCIsXG4gICAgICAgICAgXCJtb2RpZnlSdWxlXCI6IFwiU2VsZlwiXG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCJTY29yZVwiLFxuICAgICAgICAgIFwidmlzaWJsZVwiOiB0cnVlLFxuICAgICAgICAgIFwidmlld1J1bGVcIjogXCJQdWJsaWNcIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJBZG1pblwiXG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCJLYXJtYVwiLFxuICAgICAgICAgIFwidmlzaWJsZVwiOiB0cnVlLFxuICAgICAgICAgIFwidmlld1J1bGVcIjogXCJQdWJsaWNcIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJBZG1pblwiXG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCJSYW5raW5nXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlB1YmxpY1wiLFxuICAgICAgICAgIFwibW9kaWZ5UnVsZVwiOiBcIkFkbWluXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIlNpZ251cCBhcHBsaWNhdGlvblwiLFxuICAgICAgICAgIFwidmlzaWJsZVwiOiB0cnVlLFxuICAgICAgICAgIFwidmlld1J1bGVcIjogXCJQdWJsaWNcIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJBZG1pblwiXG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCJSb2xlc1wiLFxuICAgICAgICAgIFwidmlzaWJsZVwiOiB0cnVlLFxuICAgICAgICAgIFwidmlld1J1bGVcIjogXCJQdWJsaWNcIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJJbW11dGFibGVcIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiUGVybWlzc2lvbnNcIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInZpZXdSdWxlXCI6IFwiUHVibGljXCIsXG4gICAgICAgICAgXCJtb2RpZnlSdWxlXCI6IFwiSW1tdXRhYmxlXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIkdyb3Vwc1wiLFxuICAgICAgICAgIFwidmlzaWJsZVwiOiB0cnVlLFxuICAgICAgICAgIFwidmlld1J1bGVcIjogXCJQdWJsaWNcIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJBZG1pblwiXG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCIzcmQtcGFydHkgbG9naW5zXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlNlbGZcIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJTZWxmXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIlByb3BlcnRpZXNcIixcbiAgICAgICAgICBcInZpc2libGVcIjogZmFsc2UsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIkFkbWluXCIsXG4gICAgICAgICAgXCJtb2RpZnlSdWxlXCI6IFwiQWRtaW5cIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiSXMgYWRtaW5cIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInZpZXdSdWxlXCI6IFwiQWRtaW5cIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJBZG1pblwiXG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCJJcyBmb3JiaWRkZW5cIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInZpZXdSdWxlXCI6IFwiQWRtaW5cIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJBZG1pblwiXG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCJJcyBkZWxldGVkXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIkFkbWluXCIsXG4gICAgICAgICAgXCJtb2RpZnlSdWxlXCI6IFwiQWRtaW5cIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiTXVsdGktZmFjdG9yIGF1dGhlbnRpY2F0aW9uXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlNlbGZcIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJTZWxmXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIldlYkF1dGhuIGNyZWRlbnRpYWxzXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJ2aWV3UnVsZVwiOiBcIlNlbGZcIixcbiAgICAgICAgICBcIm1vZGlmeVJ1bGVcIjogXCJTZWxmXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIk1hbmFnZWQgYWNjb3VudHNcIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInZpZXdSdWxlXCI6IFwiU2VsZlwiLFxuICAgICAgICAgIFwibW9kaWZ5UnVsZVwiOiBcIlNlbGZcIlxuICAgICAgICB9XG4gICAgICBdXG4gICAgfVxuICBdLFxuICBcInVzZXJzXCI6IFtcbiAgICB7XG4gICAgICBcIm93bmVyXCI6IFwiYnVpbHQtaW5cIixcbiAgICAgIFwibmFtZVwiOiBcImFkbWluXCIsXG4gICAgICBcImNyZWF0ZWRUaW1lXCI6IFwiMjAyMS0wMS0wMVQwMDowMDowMFpcIixcbiAgICAgIFwidXBkYXRlZFRpbWVcIjogXCIyMDIxLTAxLTAxVDAwOjAwOjAwWlwiLFxuICAgICAgXCJpZFwiOiBcImFkbWluXCIsXG4gICAgICBcInR5cGVcIjogXCJub3JtYWwtdXNlclwiLFxuICAgICAgXCJwYXNzd29yZFwiOiBcIiR7YWRtaW5fcGFzc3dvcmR9XCIsXG4gICAgICBcInBhc3N3b3JkU2FsdFwiOiBcIlwiLFxuICAgICAgXCJkaXNwbGF5TmFtZVwiOiBcIkFkbWluXCIsXG4gICAgICBcImZpcnN0TmFtZVwiOiBcIlwiLFxuICAgICAgXCJsYXN0TmFtZVwiOiBcIlwiLFxuICAgICAgXCJhdmF0YXJcIjogXCJodHRwczovL2Nkbi5jYXNiaW4ub3JnL2ltZy9jYXNiaW4vdXNlci5wbmdcIixcbiAgICAgIFwicGVybWFuZW50QXZhdGFyXCI6IFwiXCIsXG4gICAgICBcImVtYWlsXCI6IFwiYWRtaW5AZXhhbXBsZS5jb21cIixcbiAgICAgIFwiZW1haWxWZXJpZmllZFwiOiB0cnVlLFxuICAgICAgXCJwaG9uZVwiOiBcIlwiLFxuICAgICAgXCJsb2NhdGlvblwiOiBcIlwiLFxuICAgICAgXCJhZGRyZXNzXCI6IFtdLFxuICAgICAgXCJhZmZpbGlhdGlvblwiOiBcIkV4YW1wbGUgSW5jLlwiLFxuICAgICAgXCJ0aXRsZVwiOiBcIkFkbWluaXN0cmF0b3JcIixcbiAgICAgIFwiaWRDYXJkVHlwZVwiOiBcIlwiLFxuICAgICAgXCJpZENhcmRcIjogXCJcIixcbiAgICAgIFwiaG9tZXBhZ2VcIjogXCJcIixcbiAgICAgIFwiYmlvXCI6IFwiXCIsXG4gICAgICBcInRhZ1wiOiBcInN0YWZmXCIsXG4gICAgICBcInJlZ2lvblwiOiBcIlVTXCIsXG4gICAgICBcImxhbmd1YWdlXCI6IFwiZW5cIixcbiAgICAgIFwiZ2VuZGVyXCI6IFwiXCIsXG4gICAgICBcImJpcnRoZGF5XCI6IFwiXCIsXG4gICAgICBcImVkdWNhdGlvblwiOiBcIlwiLFxuICAgICAgXCJzY29yZVwiOiAyMDAwLFxuICAgICAgXCJrYXJtYVwiOiAwLFxuICAgICAgXCJyYW5raW5nXCI6IDEsXG4gICAgICBcImlzRGVmYXVsdEF2YXRhclwiOiBmYWxzZSxcbiAgICAgIFwiaXNPbmxpbmVcIjogZmFsc2UsXG4gICAgICBcImlzQWRtaW5cIjogdHJ1ZSxcbiAgICAgIFwiaXNHbG9iYWxBZG1pblwiOiB0cnVlLFxuICAgICAgXCJpc0ZvcmJpZGRlblwiOiBmYWxzZSxcbiAgICAgIFwiaXNEZWxldGVkXCI6IGZhbHNlLFxuICAgICAgXCJzaWdudXBBcHBsaWNhdGlvblwiOiBcImFwcC1idWlsdC1pblwiLFxuICAgICAgXCJoYXNoXCI6IFwiXCIsXG4gICAgICBcInByZUhhc2hcIjogXCJcIixcbiAgICAgIFwiY3JlYXRlZElwXCI6IFwiXCIsXG4gICAgICBcImxhc3RTaWduaW5UaW1lXCI6IFwiXCIsXG4gICAgICBcImxhc3RTaWduaW5JcFwiOiBcIlwiLFxuICAgICAgXCJnaXRodWJcIjogXCJcIixcbiAgICAgIFwiZ29vZ2xlXCI6IFwiXCIsXG4gICAgICBcInFxXCI6IFwiXCIsXG4gICAgICBcIndlY2hhdFwiOiBcIlwiLFxuICAgICAgXCJmYWNlYm9va1wiOiBcIlwiLFxuICAgICAgXCJkaW5ndGFsa1wiOiBcIlwiLFxuICAgICAgXCJ3ZWlib1wiOiBcIlwiLFxuICAgICAgXCJnaXRlZVwiOiBcIlwiLFxuICAgICAgXCJsaW5rZWRpblwiOiBcIlwiLFxuICAgICAgXCJ3ZWNvbVwiOiBcIlwiLFxuICAgICAgXCJsYXJrXCI6IFwiXCIsXG4gICAgICBcImdpdGxhYlwiOiBcIlwiLFxuICAgICAgXCJhZGZzXCI6IFwiXCIsXG4gICAgICBcImJhaWR1XCI6IFwiXCIsXG4gICAgICBcImFsaXBheVwiOiBcIlwiLFxuICAgICAgXCJjYXNkb29yXCI6IFwiXCIsXG4gICAgICBcImluZm9mbG93XCI6IFwiXCIsXG4gICAgICBcImFwcGxlXCI6IFwiXCIsXG4gICAgICBcImF6dXJlYWRcIjogXCJcIixcbiAgICAgIFwic2xhY2tcIjogXCJcIixcbiAgICAgIFwic3RlYW1cIjogXCJcIixcbiAgICAgIFwiYmlsaWJpbGlcIjogXCJcIixcbiAgICAgIFwib2t0YVwiOiBcIlwiLFxuICAgICAgXCJkb3V5aW5cIjogXCJcIixcbiAgICAgIFwiY3VzdG9tXCI6IFwiXCIsXG4gICAgICBcIndlYmF1dGhuQ3JlZGVudGlhbHNcIjogW10sXG4gICAgICBcInByZWZlcnJlZE1mYVR5cGVcIjogXCJcIixcbiAgICAgIFwicmVjb3ZlcnlDb2Rlc1wiOiBbXSxcbiAgICAgIFwidG90cFNlY3JldFwiOiBcIlwiLFxuICAgICAgXCJtZmFQaG9uZUVuYWJsZWRcIjogZmFsc2UsXG4gICAgICBcIm1mYUVtYWlsRW5hYmxlZFwiOiBmYWxzZSxcbiAgICAgIFwibGRhcFwiOiBcIlwiLFxuICAgICAgXCJwcm9wZXJ0aWVzXCI6IHt9LFxuICAgICAgXCJyb2xlc1wiOiBbXSxcbiAgICAgIFwicGVybWlzc2lvbnNcIjogW10sXG4gICAgICBcImdyb3Vwc1wiOiBbXSxcbiAgICAgIFwibGFzdFNpZ25pbldyb25nVGltZVwiOiBcIlwiLFxuICAgICAgXCJzaWduaW5Xcm9uZ1RpbWVzXCI6IDAsXG4gICAgICBcIm1hbmFnZWRBY2NvdW50c1wiOiBbXVxuICAgIH1cbiAgXSxcbiAgXCJhcHBsaWNhdGlvbnNcIjogW1xuICAgIHtcbiAgICAgIFwib3duZXJcIjogXCJidWlsdC1pblwiLFxuICAgICAgXCJuYW1lXCI6IFwiYXBwLWJ1aWx0LWluXCIsXG4gICAgICBcImNyZWF0ZWRUaW1lXCI6IFwiMjAyMS0wMS0wMVQwMDowMDowMFpcIixcbiAgICAgIFwiZGlzcGxheU5hbWVcIjogXCJDYXNkb29yXCIsXG4gICAgICBcImxvZ29cIjogXCJodHRwczovL2Nkbi5jYXNiaW4ub3JnL2ltZy9jYXNiaW4vZmF2aWNvbi5pY29cIixcbiAgICAgIFwiaG9tZXBhZ2VVcmxcIjogXCJodHRwczovLyR7bWFpbl9kb21haW59XCIsXG4gICAgICBcImRlc2NyaXB0aW9uXCI6IFwiQ2FzZG9vciAtIEEgVUktZmlyc3QgSWRlbnRpdHkgQWNjZXNzIE1hbmFnZW1lbnQgKElBTSkgLyBTaW5nbGUtU2lnbi1PbiAoU1NPKSBwbGF0Zm9ybVwiLFxuICAgICAgXCJvcmdhbml6YXRpb25cIjogXCJidWlsdC1pblwiLFxuICAgICAgXCJjZXJ0XCI6IFwiXCIsXG4gICAgICBcImVuYWJsZVBhc3N3b3JkXCI6IHRydWUsXG4gICAgICBcImVuYWJsZVNpZ25VcFwiOiB0cnVlLFxuICAgICAgXCJlbmFibGVTaWduaW5TZXNzaW9uXCI6IGZhbHNlLFxuICAgICAgXCJlbmFibGVBdXRvU2lnbmluXCI6IGZhbHNlLFxuICAgICAgXCJlbmFibGVDb2RlU2lnbmluXCI6IGZhbHNlLFxuICAgICAgXCJlbmFibGVTYW1sQ29tcHJlc3NcIjogZmFsc2UsXG4gICAgICBcImVuYWJsZVdlYkF1dGhuXCI6IGZhbHNlLFxuICAgICAgXCJlbmFibGVMaW5rV2l0aEVtYWlsXCI6IGZhbHNlLFxuICAgICAgXCJzYW1sUmVwbHlVcmxcIjogXCJcIixcbiAgICAgIFwicHJvdmlkZXJzXCI6IFtdLFxuICAgICAgXCJzaWdudXBJdGVtc1wiOiBbXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCJJRFwiLFxuICAgICAgICAgIFwidmlzaWJsZVwiOiBmYWxzZSxcbiAgICAgICAgICBcInJlcXVpcmVkXCI6IHRydWUsXG4gICAgICAgICAgXCJwcm9tcHRlZFwiOiBmYWxzZSxcbiAgICAgICAgICBcInJ1bGVcIjogXCJSYW5kb21cIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiVXNlcm5hbWVcIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInJlcXVpcmVkXCI6IHRydWUsXG4gICAgICAgICAgXCJwcm9tcHRlZFwiOiBmYWxzZSxcbiAgICAgICAgICBcInJ1bGVcIjogXCJOb25lXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIkRpc3BsYXkgbmFtZVwiLFxuICAgICAgICAgIFwidmlzaWJsZVwiOiB0cnVlLFxuICAgICAgICAgIFwicmVxdWlyZWRcIjogdHJ1ZSxcbiAgICAgICAgICBcInByb21wdGVkXCI6IGZhbHNlLFxuICAgICAgICAgIFwicnVsZVwiOiBcIk5vbmVcIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiUGFzc3dvcmRcIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInJlcXVpcmVkXCI6IHRydWUsXG4gICAgICAgICAgXCJwcm9tcHRlZFwiOiBmYWxzZSxcbiAgICAgICAgICBcInJ1bGVcIjogXCJOb25lXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIkNvbmZpcm0gcGFzc3dvcmRcIixcbiAgICAgICAgICBcInZpc2libGVcIjogdHJ1ZSxcbiAgICAgICAgICBcInJlcXVpcmVkXCI6IHRydWUsXG4gICAgICAgICAgXCJwcm9tcHRlZFwiOiBmYWxzZSxcbiAgICAgICAgICBcInJ1bGVcIjogXCJOb25lXCJcbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgIFwibmFtZVwiOiBcIkVtYWlsXCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJyZXF1aXJlZFwiOiB0cnVlLFxuICAgICAgICAgIFwicHJvbXB0ZWRcIjogZmFsc2UsXG4gICAgICAgICAgXCJydWxlXCI6IFwiTm9uZVwiXG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICBcIm5hbWVcIjogXCJQaG9uZVwiLFxuICAgICAgICAgIFwidmlzaWJsZVwiOiB0cnVlLFxuICAgICAgICAgIFwicmVxdWlyZWRcIjogdHJ1ZSxcbiAgICAgICAgICBcInByb21wdGVkXCI6IGZhbHNlLFxuICAgICAgICAgIFwicnVsZVwiOiBcIk5vbmVcIlxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgXCJuYW1lXCI6IFwiQWdyZWVtZW50XCIsXG4gICAgICAgICAgXCJ2aXNpYmxlXCI6IHRydWUsXG4gICAgICAgICAgXCJyZXF1aXJlZFwiOiB0cnVlLFxuICAgICAgICAgIFwicHJvbXB0ZWRcIjogZmFsc2UsXG4gICAgICAgICAgXCJydWxlXCI6IFwiTm9uZVwiXG4gICAgICAgIH1cbiAgICAgIF0sXG4gICAgICBcImdyYW50VHlwZXNcIjogW1xuICAgICAgICBcImF1dGhvcml6YXRpb25fY29kZVwiLFxuICAgICAgICBcInBhc3N3b3JkXCIsXG4gICAgICAgIFwiY2xpZW50X2NyZWRlbnRpYWxzXCIsXG4gICAgICAgIFwidG9rZW5cIixcbiAgICAgICAgXCJpZF90b2tlblwiXG4gICAgICBdLFxuICAgICAgXCJvcmdhbml6YXRpb25PYmpcIjoge1xuICAgICAgICBcIm93bmVyXCI6IFwiYWRtaW5cIixcbiAgICAgICAgXCJuYW1lXCI6IFwiYnVpbHQtaW5cIixcbiAgICAgICAgXCJjcmVhdGVkVGltZVwiOiBcIjIwMjEtMDEtMDFUMDA6MDA6MDBaXCIsXG4gICAgICAgIFwiZGlzcGxheU5hbWVcIjogXCJCdWlsdC1pbiBPcmdhbml6YXRpb25cIlxuICAgICAgfSxcbiAgICAgIFwidGFnc1wiOiBbXSxcbiAgICAgIFwiY2xpZW50SWRcIjogXCIke2p3dF9zZWNyZXR9XCIsXG4gICAgICBcImNsaWVudFNlY3JldFwiOiBcIiR7and0X3NlY3JldH1cIixcbiAgICAgIFwicmVkaXJlY3RVcmlzXCI6IFtcImh0dHBzOi8vJHttYWluX2RvbWFpbn0vY2FsbGJhY2tcIl0sXG4gICAgICBcInRva2VuRm9ybWF0XCI6IFwiSldUXCIsXG4gICAgICBcInRva2VuRmllbGRzXCI6IFtdLFxuICAgICAgXCJleHBpcmVJbkhvdXJzXCI6IDE2OCxcbiAgICAgIFwicmVmcmVzaEV4cGlyZUluSG91cnNcIjogMTY4LFxuICAgICAgXCJzaWdudXBVcmxcIjogXCJcIixcbiAgICAgIFwic2lnbmluVXJsXCI6IFwiXCIsXG4gICAgICBcImZvcmdldFVybFwiOiBcIlwiLFxuICAgICAgXCJhZmZpbGlhdGlvblVybFwiOiBcIlwiLFxuICAgICAgXCJ0ZXJtc09mVXNlXCI6IFwiXCIsXG4gICAgICBcInByaXZhY3lQb2xpY3lcIjogXCJcIixcbiAgICAgIFwidG9rZW5GaWVsZHNcIjogW10sXG4gICAgICBcInRoZW1lRGF0YVwiOiB7XG4gICAgICAgIFwiaXNDb21wYWN0XCI6IGZhbHNlLFxuICAgICAgICBcImlzRW5hYmxlZFwiOiBmYWxzZSxcbiAgICAgICAgXCJ0aGVtZVR5cGVcIjogXCJkZWZhdWx0XCIsXG4gICAgICAgIFwiY29sb3JQcmltYXJ5XCI6IFwiIzE5NzZkMlwiLFxuICAgICAgICBcImJvcmRlclJhZGl1c1wiOiA2LFxuICAgICAgICBcImlzUm91bmRlZEJ1dHRvblwiOiBmYWxzZSxcbiAgICAgICAgXCJpc0dyYWRpZW50QnV0dG9uXCI6IGZhbHNlLFxuICAgICAgICBcInRoZW1lQWxnb3JpdGhtXCI6IFwiZGVmYXVsdFwiXG4gICAgICB9LFxuICAgICAgXCJmb3JtQ3NzXCI6IFwiXCIsXG4gICAgICBcImZvcm1Dc3NNb2JpbGVcIjogXCJcIixcbiAgICAgIFwiZm9ybU9mZnNldFwiOiAyLFxuICAgICAgXCJmb3JtU2lkZUh0bWxcIjogXCJcIixcbiAgICAgIFwiZm9ybUJhY2tncm91bmRVcmxcIjogXCJcIlxuICAgIH1cbiAgXSxcbiAgXCJjZXJ0c1wiOiBbXSxcbiAgXCJwcm92aWRlcnNcIjogW10sXG4gIFwibGRhcHNcIjogW10sXG4gIFwibW9kZWxzXCI6IFtdLFxuICBcInBlcm1pc3Npb25zXCI6IFtdLFxuICBcInJvbGVzXCI6IFtdLFxuICBcImdyb3Vwc1wiOiBbXSxcbiAgXCJlbmZvcmNlcnNcIjogW10sXG4gIFwidG9rZW5zXCI6IFtdLFxuICBcInNlc3Npb25zXCI6IFtdLFxuICBcInBheW1lbnRzXCI6IFtdLFxuICBcInByb2R1Y3RzXCI6IFtdLFxuICBcInJlc291cmNlc1wiOiBbXSxcbiAgXCJzeW5jZWVyc1wiOiBbXSxcbiAgXCJhZGFwdGVyc1wiOiBbXSxcbiAgXCJ3ZWJob29rc1wiOiBbXSxcbiAgXCJzdWJzY3JpcHRpb25zXCI6IFtdLFxuICBcInBsYW5zXCI6IFtdLFxuICBcInByaWNpbmdzXCI6IFtdLFxuICBcImludml0YXRpb25zXCI6IFtdXG59XG5cIlwiXCJcbiIKfQ==
```

## Links

`authentication`,`authorization`,`oauth2`,`oidc`,`sso`,`saml`,`identity-management`,`access-management`,`security`

---

Version:`latest`

CarboneCarbone is a high-performance, self-hosted document generation engine. It allows you to generate reports, invoices, and documents in various formats (e.g., PDF, DOCX, XLSX) using JSON data and template-based rendering.

Change DetectionChangedetection.io is an intelligent tool designed to monitor changes on websites. Perfect for smart shoppers, data journalists, research engineers, data scientists, and security researchers.

### On this page

ConfigurationBase64LinksTags