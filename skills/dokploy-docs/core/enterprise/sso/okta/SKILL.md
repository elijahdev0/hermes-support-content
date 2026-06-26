---
title: "Okta | Dokploy"
source: "https://docs.dokploy.com/docs/core/enterprise/sso/okta"
category: dokploy-docs
created: "2026-06-25T17:21:36.901Z"
---

Okta | Dokploy

# Okta

Copy as Markdown

Configure SSO with Okta (OIDC or SAML)

SSO (OIDC)SAML

## 1. Create an application in Okta

1. Log in to the Okta Admin Console(or your Okta domain).
2. Go to Applications → Applications → Create App Integration.
3. Choose OIDC - OpenID Connect and Web Application, then create it.
4. Note your Client ID and Client Secret (under General or Client credentials).
5. Note your Okta domain (e.g.`https://your-domain.okta.com`) and, if using a custom authorization server, its issuer (e.g.`https://your-domain.okta.com/oauth2/default`) or go to Security → API → Authorization Servers and note the Issuer (e.g.`https://your-domain.okta.com`).

## 2. Configure Dokploy

Enter:

- Provider: myorg-name-okta (unique name for this provider)
- Issuer URL: your Okta issuer URL (e.g.`https://your-domain.okta.com`)
- Domain: the domain users use to authenticate via Okta (e.g. your organization domain like`acme.com`), not the Dokploy instance URL
- Client ID: from the Okta application
- Client Secret: from the Okta application
- Scopes: openid email profile

## 3. Configure Okta

Set Sign-in redirect URIs to your Dokploy callback URL, for example:

- `https://your-dokploy-domain.com/api/auth/callback/myorg-name-okta`

Set Sign-out redirect URIs (optional) to:

- `https://your-dokploy-domain.com`

## Troubleshooting (OIDC)

- Save.
- Redirect URI mismatch — Ensure the callback URL in Dokploy matches exactly what is configured in Okta (including protocol and path). Use the same Provider value in the path (e.g.`.../api/auth/callback/myorg-name-okta`).
- Invalid client — Double-check Client ID and Client Secret, and that the application is a Web Application with the correct grant types (e.g. Authorization Code).
- Issuer URL — Use the full issuer URL for your authorization server (e.g.`https://your-domain.okta.com`).
- Scopes — Ensure the Okta authorization server is configured to allow`openid`, and if needed`email` and`profile`.

## 1. Create a SAML application in Okta

1. Log in to the Okta Admin Console(or your Okta domain).
2. Go to Applications → Applications → Create App Integration.
3. Choose SAML 2.0 and create it.
4. Enter an App name (e.g. Dokploy). Under Configure SAML, in the Single sign-on URL field, set the SAML ACS URL (eg.`https://your-dokploy-instance.com/api/auth/sso/saml2/callback/myorg-name-okta-saml`) and in the Audience URI (SP Entity ID) field, set the SP Entity ID (eg.`https://your-dokploy-instance.com`).
5. Next & Save.

## 2. Configure Dokploy

Enter:

- Provider: myorg-name-okta-saml (unique name for this provider)
- Issuer URL: the Okta Identity Provider issuer (Entity ID) located in`Sign On` tab called`Issuer`(eg.`http://www.okta.com/exkzq3acyuEtIuNrW697`)
- SSO URL: the Okta Identity Provider single sign-on URL located in`Sign On` tab called`Single sign-on URL`(eg.`https://trial-2804699.okta.com/app/trial-2802699_something/exkzqi3cyuEtIuNrW697/sso/saml`)
- Certificate: go to`Signing Certificate` tab and download the certificate active (x509) and paste it in the`Certificate` field.
- Federation Metadata XML: copy the idp metadata XML from the certificate active and paste it in the`Metadata XML` field.
- Domain: the domain users use to authenticate via Okta (e.g. your organization domain like`acme.com`), not the Dokploy instance URL

## Troubleshooting (SAML)

- Save.
- ACS URL mismatch — Ensure the Single sign-on URL (ACS) in Okta matches exactly what Dokploy provides (including protocol and path).
- Certificate — Use the x509 certificate from Okta’s IdP metadata (PEM or Base64); ensure it is the one used to sign assertions.
- Entity ID — The Entity ID in Dokploy must match the Identity Provider issuer in Okta.

For help with your setup, contact us.

KeycloakConfigure SSO with Keycloak

ZitadelConfigure SSO with Zitadel

### On this page

1. Create an application in Okta2. Configure Dokploy3. Configure OktaTroubleshooting (OIDC)1. Create a SAML application in Okta2. Configure DokployTroubleshooting (SAML)