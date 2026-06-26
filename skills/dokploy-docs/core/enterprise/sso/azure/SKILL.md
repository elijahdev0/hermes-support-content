---
title: "Azure AD (Microsoft Entra ID) | Dokploy"
source: "https://docs.dokploy.com/docs/core/enterprise/sso/azure"
category: dokploy-docs
created: "2026-06-25T17:16:11.092Z"
---

Azure AD (Microsoft Entra ID) | Dokploy

# Azure AD (Microsoft Entra ID)

Copy as Markdown

Configure SSO with Azure AD / Microsoft Entra ID (OIDC or SAML)

SSO (OIDC)SAML

## 1. Register an application in Azure

1. Log in to the Azure Portal.
2. Go to Microsoft Entra ID (or Azure Active Directory) → App registrations → New registration.
3. Enter a Name (e.g. Dokploy), choose supported account types, and set Redirect URI to Web with a placeholder for now (e.g.`https://your-dokploy-domain.com/api/auth/callback/myorg-name-azure`).
4. Register and note the Application (client) ID and Directory (tenant) ID.
5. Go to Certificates & secrets → New client secret, create a secret and note its Value (you won’t see it again).
6. The Issuer URL for OpenID Connect is:`https://login.microsoftonline.com/{tenant-id}/v2.0`(replace`{tenant-id}` with your Directory (tenant) ID). Some setups expect a trailing slash.

## 2. Configure Dokploy

Enter:

- Provider: myorg-name-azure (unique name for this provider)
- Issuer URL:`https://login.microsoftonline.com/YOUR_TENANT_ID/v2.0`(use your Directory (tenant) ID; add a trailing slash if required for discovery)
- Domain: the domain users use to authenticate via Azure AD (e.g. your organization domain like`acme.com`), not the Dokploy instance URL
- Client ID: the Application (client) ID from Azure
- Client Secret: the client secret value from Certificates & secrets
- Scopes: openid email profile

## 3. Configure Azure

Under Web → Redirect URIs, add:

- `https://your-dokploy-domain.com/api/auth/callback/myorg-name-azure`

Under Front-channel logout URL (optional), you can set:

- `https://your-dokploy-domain.com`

## Troubleshooting (OIDC)

- Save.
- Redirect URI mismatch — Ensure the callback URL in Dokploy matches exactly what is configured in Azure (including protocol and path). Use the same Provider value in the path (e.g.`.../api/auth/callback/myorg-name-azure`).
- Invalid client — Double-check Application (client) ID and client secret. Confirm the secret has not expired under Certificates & secrets.
- Tenant — Use the correct Directory (tenant) ID in the Issuer URL. For multi-tenant apps, you may use`common` instead of the tenant ID (e.g.`https://login.microsoftonline.com/common/v2.0`).
- Scopes — Ensure the app registration has the right API permissions (e.g. OpenID permissions, User.Read) if required for`openid`,`email`, and`profile`.

## 1. Create an Enterprise Application (SAML) in Azure

1. Log in to the Azure Portal.
2. Go to Microsoft Entra ID → Enterprise applications → New application → Create your own application (or Non-gallery application).
3. Enter a Name (e.g. Dokploy) and create.
4. Go to Single sign-on → SAML.
5. Note the Identifier (Entity ID) and Login URL (SSO URL). Under SAML Certificates, download or copy the Certificate (Base64) (x509) and download the Federation Metadata XML file.

## 2. Configure Dokploy

Enter:

- Provider: myorg-name-azure-saml (unique name for this provider)
- Issuer URL: the Azure SAML Entity ID (Identifier) from the Enterprise application (eg.`https://sts.windows.net/YOUR_TENANT_ID/`).
- SSO URL: the Azure Login URL (Single Sign-On URL) (eg.`https://login.microsoftonline.com/YOUR_TENANT_ID/saml2`)
- Certificate: the IdP signing certificate (x509 Base64) from Azure
- Federation Metadata XML: the Federation Metadata XML file from Azure
- Domain: the domain users use to authenticate via Azure AD (e.g. your organization domain like`acme.com`), not the Dokploy instance URL

## 3. Configure Azure (SAML)

1. Save.
2. In your Enterprise application, go to Single sign-on → SAML.
3. Under Basic SAML Configuration, set Identifier (Entity ID) if required (SP Entity ID from Dokploy) (eg.`https://your-dokploy-instance.com`).
4. Set Reply URL (Assertion Consumer Service URL) to your Dokploy SAML ACS URL (eg.`https://your-dokploy-instance.com/api/auth/sso/saml2/callback/myorg-name-azure-saml`).
5. Save.

## Troubleshooting (SAML)

- ACS URL mismatch — Ensure the Reply URL (ACS) in Azure matches exactly what Dokploy provides (including protocol and path).
- Certificate — Use the Certificate (Base64) from Azure; paste as-is or convert to PEM if Dokploy expects PEM.
- Entity ID — The Entity ID in Dokploy must match the Identifier (Entity ID) of the Azure Enterprise application.

For help with your setup, contact us.

Auth0Configure SSO with Auth0 (OIDC or SAML)

KeycloakConfigure SSO with Keycloak

### On this page

1. Register an application in Azure2. Configure Dokploy3. Configure AzureTroubleshooting (OIDC)1. Create an Enterprise Application (SAML) in Azure2. Configure Dokploy3. Configure Azure (SAML)Troubleshooting (SAML)