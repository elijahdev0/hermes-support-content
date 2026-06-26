---
title: "Keycloak | Dokploy"
source: "https://docs.dokploy.com/docs/core/enterprise/sso/keycloak"
category: dokploy-docs
created: "2026-06-25T17:16:11.092Z"
---

Keycloak | Dokploy

# Keycloak

Copy as Markdown

Configure SSO with Keycloak

## 1. Create a client in Keycloak

1. Log in to your Keycloak Admin Console.
2. Select your realm (or create one).
3. Go to Clients → Create client.
4. Set Client ID (e.g.`my-client-id`) and Client type to OpenID Connect.
5. Set Root URL to your Dokploy base URL, e.g.`https://your-dokploy-domain.com`.
6. Save.
7. Open the client, set Access type to confidential, then open the Credentials tab and note the Secret.
8. From Realm settings → OpenID Endpoint Configuration, note the Issuer (e.g.`https://keycloak.example.com/realms/your-realm`).

## 2. Configure Dokploy

Enter:

- Provider: my-client-id (Unique)
- Issuer URL: your Keycloak realm URL (e.g.`https://keycloak.example.com/realms/your-realm`)
- Domain: the domain users use to authenticate via Keycloak (e.g. your organization domain like`acme.com`), not the Dokploy instance URL
- Client ID: my-client-id
- Client Secret: the secret from the Keycloak client Credentials tab
- Scopes: openid email profile

## 3. Configure Keycloak

Set Valid redirect URIs to your Dokploy callback URL, for example:

- `https://your-dokploy-domain.com/api/auth/callback/my-client-id`

Set Valid post logout redirect URIs to:

- `https://your-dokploy-domain.com`

Set Allowed Origins to:

- `https://your-dokploy-domain.com`

## Troubleshooting

- Save changes.
- Redirect URI mismatch — Ensure the callback URL in Dokploy matches exactly what is configured in Keycloak (including protocol and path). Use the same Provider value in the path (e.g.`.../api/auth/callback/myorg-name-keycloak`).
- Invalid client — Double-check Client ID and Client Secret, and that the client is enabled and set to confidential access.
- Scopes — Ensure the client is configured to request`openid` and, if required,`email` and`profile`.
- Attribute mapping — If user email or name is missing, map Keycloak attributes (e.g. email, preferred_username) in Dokploy if your setup supports it.

For help with your setup, contact us.

Azure AD (Microsoft Entra ID)Configure SSO with Azure AD / Microsoft Entra ID (OIDC or SAML)

OktaConfigure SSO with Okta (OIDC or SAML)

### On this page

1. Create a client in Keycloak2. Configure Dokploy3. Configure KeycloakTroubleshooting