---
title: "Zitadel | Dokploy"
source: "https://docs.dokploy.com/docs/core/enterprise/sso/zitadel"
category: dokploy-docs
created: "2026-06-25T17:21:36.901Z"
---

Zitadel | Dokploy

# Zitadel

Copy as Markdown

Configure SSO with Zitadel

## 1. Create an application in Zitadel

Add the following Redirect URI:

- `https://your-dokploy-domain.com/api/auth/sso/callback/{providerId}` Replace`{providerId}` with the unique identifier you will use in Dokploy (e.g.`zitadel`).

Add the Post Logout URI:

- `https://your-dokploy-domain.com`

## 2. Get your Issuer URL

Your Zitadel issuer URL is the base domain of your instance, for example:

- Copy the Client ID and generate + copy the Client Secret before closing the dialog.
- Cloud:`https://your-instance.zitadel.cloud`
- Self-hosted:`https://zitadel.yourdomain.com`

Dokploy will automatically fetch the OpenID Connect discovery document from`{issuer}/.well-known/openid-configuration`.

## 3. Configure Dokploy

Enter:

- Provider ID:`zitadel`(must match the`{providerId}` used in the Redirect URI above)
- Issuer URL: your Zitadel base URL (e.g.`https://your-instance.zitadel.cloud`)
- Domains: email domain(s) of your users (e.g.`acme.com`)
- Client ID: the Client ID from Zitadel
- Client Secret: the Client Secret from Zitadel
- Scopes: leave empty (defaults to`openid email profile`)

## 4. Verify the Redirect URI in Zitadel

Make sure the Redirect URI configured in your Zitadel application matches exactly the Callback URL shown in Dokploy:

```
https://your-dokploy-domain.com/api/auth/sso/callback/zitadel
```

If they differ, update the Redirect URI in the Zitadel application settings.

## Troubleshooting

- Save.
- Redirect URI mismatch — The Redirect URI in Zitadel must match the Callback URL in Dokploy exactly, including the`{providerId}` path segment.
- Invalid client — Verify the Client ID and Client Secret are correct and that the application is active in Zitadel.
- Authentication method — Zitadel must be set to CODE (Authentication Method: Basic). PKCE is not supported for server-side applications.
- HTTPS required — Zitadel requires HTTPS for Redirect URIs in production. Enable Development Mode in your Zitadel instance only if testing with HTTP.
- User not found — Ensure the user exists in the Zitadel project and that the`email` scope is included.

For help with your setup, contact us.

OktaConfigure SSO with Okta (OIDC or SAML)

WhitelabelingRebrand Dokploy with your application name, logos, colors, and custom links

### On this page

1. Create an application in Zitadel2. Get your Issuer URL3. Configure Dokploy4. Verify the Redirect URI in ZitadelTroubleshooting