---
title: "Pushover | Dokploy"
source: "https://docs.dokploy.com/docs/core/pushover"
category: dokploy-docs
created: "2026-06-25T17:21:38.073Z"
---

Pushover | Dokploy

Notifications

# Pushover

Copy as Markdown

Configure Pushover notifications for your applications.

Pushover notifications are a great way to stay up to date with important events in your Dokploy panel. You can choose to receive notifications for specific events or all events.

## Pushover Notifications

To start receiving Pushover notifications, you need to fill the form with the following details:

Priority: Enter the priority of the notification (-2 to 2, default: 0).

- `-2`: Lowest priority (no sound/vibration)
- `-1`: Low priority (no sound/vibration)
- `0`: Normal priority (default)
- `1`: High priority (bypasses quiet hours)
- `2`: Emergency priority (requires acknowledgment)

For emergency priority (2), you must also provide:

- Retry: How often (in seconds) Pushover will retry the notification. Minimum 30 seconds.
- Expire: How long (in seconds) to keep retrying. Maximum 10800 seconds (3 hours).

To setup the Pushover notifications, you can read the Pushover Documentation.

NtfyConfigure ntfy notifications for your applications.

WebhookConfigure webhook notifications for your applications.

### On this page

Pushover Notifications