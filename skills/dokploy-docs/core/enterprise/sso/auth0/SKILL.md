---
title: "Auth0 | Dokploy"
source: "https://docs.dokploy.com/docs/core/enterprise/sso/auth0"
category: dokploy-docs
created: "2026-06-25T17:16:11.092Z"
---

Auth0 | Dokploy

# Auth0

Copy as Markdown

Configure SSO with Auth0 (OIDC or SAML)

SSO (OIDC)SAML

## 1. Create an application in Auth0

1. Log in to the Auth0 Dashboard.
2. Go to Applications → Applications → Create Application.
3. Choose Regular Web Application and create it.
4. Note your Domain, Client ID, and Client Secret.

## 2. Configure Dokploy

Enter:

- Provider: myorg-name-auth0 (Unique)
- Issuer URL:`https://YOUR_AUTH0_DOMAIN/`(Make sure add the trailing slash)
- Domain: the domain users use to authenticate via Auth0 (e.g. your organization domain like`acme.com`), not the Dokploy instance URL
- Client ID: from Auth0 application
- Client Secret: from Auth0 application
- Scopes: openid email profile

## 3. Configure Auth0

Set Allowed Callback URLs to your Dokploy URL, for example:

- `https://your-dokploy-domain.com/api/auth/callback/myorg-name-auth0`

Set Allowed Logout URLs to:

- `https://your-dokploy-domain.com`

Set Allowed Origins to:

- `https://your-dokploy-domain.com`

## Troubleshooting (OIDC)

- Save changes.
- Redirect URI mismatch — Ensure the callback URL in Dokploy matches exactly what is configured in Auth0 (including protocol and path).
- Invalid client — Double-check Client ID and Client Secret, and that the application is a web application.
- Scopes — Ensure Auth0 is configured to return`openid` and, if required,`email` and`profile`.

## 1. Create a SAML application in Auth0

1. Log in to the Auth0 Dashboard.
2. Go to Applications → Applications → Create Application.
3. Choose Regular Web Application and create it.
4. In the application, go to Add Ons → enable SAML 2 Web App and configure it, in the settings specify this callback URL:`https://your-dokploy-domain.com/api/auth/sso/saml2/callback/myorg-name-auth0-saml`.
5. Next & Save.

## 2. Configure Dokploy

Enter:

- Provider: myorg-name-auth0-saml (unique name for this provider)
- Issuer URL: the Auth0 SAML Entity ID / Issuer located in`Add Ons` tab called`SAML 2 Web App` called`Entity ID`(e.g.`urn:auth0:your-tenant:your-app`)
- SSO URL: the Auth0 SAML Single Sign-On URL located in`Add Ons` tab called`SAML 2 Web App` called`Single Sign-On URL`(e.g.`https://dev-ladsadb.us.auth0.com/samlp/wgJe9bWmwhVnuAC7eNtyUsiou4b6wxuf`)
- Certificate: download the certificate active (x509) from the`Add Ons` tab called`SAML 2 Web App` called`Identity Provider Certificate` and paste it in the`Certificate` field.
- Federation Metadata XML: copy the Identity Provider Metadata XML from the certificate active and paste it in the`Metadata XML` field.
- Domain: the domain users use to authenticate via Auth0 (e.g. your organization domain like`acme.com`), not the Dokploy instance URL

## 3. Configure Auth0 (SAML)

In your Auth0 SAML application, set the Application Callback URL (ACS URL) to your Dokploy SAML ACS URL, for example:

- `https://your-dokploy-domain.com/api/auth/sso/saml2/callback/myorg-name-auth0-saml`

```
{
  "audience": "https://your-dokploy-domain.com/saml/metadata",
  "recipient": "https://your-dokploy-domain.com/api/auth/sso/saml2/callback/myorg-name-auth0-saml",
  "destination": "https://your-dokploy-domain.com/api/auth/sso/saml2/callback/myorg-name-auth0-saml",
  "signResponse": true,
  "signAssertion": true,
  "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
  "nameIdentifierProbes": [
    "email"
  ],
  "mappings": {
    "email": "email",
    "displayName": "name",
    "givenName": "given_name",
    "surname": "family_name"
  }
}
```

1. In the SAML 2 Web App add-on, open Settings and paste the following JSON in the Settings (Application Settings) field. Replace`https://your-dokploy-domain.com` with your Dokploy base URL and`myorg-name-auth0-saml` with the exact same provider name you entered in Dokploy in step 2 (the callback URL path must match), so Dokploy can read email, display name, and other attributes:
2. Save.

## Troubleshooting (SAML)

- ACS URL mismatch — Ensure the callback/ACS URL in Auth0 matches exactly what Dokploy provides (including protocol and path).
- Certificate — Use the full x509 certificate from Auth0 (PEM format); ensure no extra spaces or line breaks.
- Entity ID — The Entity ID in Dokploy must match the Issuer/Entity ID configured in Auth0.

For help with your setup, contact us.

Single Sign-On (SSO)Configure SSO with Auth0, Keycloak, or other OIDC/SAML providers

Azure AD (Microsoft Entra ID)Configure SSO with Azure AD / Microsoft Entra ID (OIDC or SAML)

### On this page

1. Create an application in Auth02. Configure Dokploy3. Configure Auth0Troubleshooting (OIDC)1. Create a SAML application in Auth02. Configure Dokploy3. Configure Auth0 (SAML)Troubleshooting (SAML)