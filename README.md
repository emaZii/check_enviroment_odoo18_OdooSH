# Environment Banner for Odoo 18 (Odoo.sh)

Displays a color-coded banner in the Odoo backend to clearly indicate the current environment — **production**, **staging**, or **development** — using the `ODOO_STAGE` variable automatically set by Odoo.sh.

---

## How it works

Odoo.sh automatically sets the `ODOO_STAGE` environment variable on every branch:

| Branch type | `ODOO_STAGE` value | Banner |
|---|---|---|
| Production | `production` | 🟢 Green |
| Staging | `staging` | 🟠 Orange (animated pulse) |
| Development | `dev` | 🔵 Blue |

At page load, a QWeb template reads `ODOO_STAGE` via a Python model and injects the value directly into the HTML `<head>`. An OWL component registered in the systray reads this value and renders the banner — **no RPC call needed**.

---

## Features

- Zero configuration — works automatically on all Odoo.sh branches
- Banner color changes based on the environment
- Staging banner has a subtle pulse animation to draw attention
- Can be disabled without uninstalling via a system parameter
- Hourly cron job logs `ODOO_STAGE` and the current git branch to the server logs

---

## Installation

1. Copy the `environment_info` folder into your Odoo addons directory
2. Push to your Odoo.sh repository
3. Go to **Apps → Update App List**
4. Search for **Environment Banner** and click **Install**

---

## Disabling the banner

To hide the banner without uninstalling the module, go to:

**Settings → Technical → Parameters → System Parameters**

Find or create the key `environment_banner.enabled` and set the value to `False`.

Set it back to `True` to re-enable.

---

## Cron job

The module includes a scheduled action that runs every hour and logs the current environment info:

```
INFO ... === ENVIRONMENT BANNER === ODOO_STAGE = 'staging' | BRANCH = 'my-branch-name'
```

To change the interval, go to **Settings → Technical → Automation → Scheduled Actions** and edit **Environment Banner: Log Environment Info**.

---

## Module structure

```
environment_info/
├── __init__.py
├── __manifest__.py
├── data/
│   └── cron.xml
├── models/
│   ├── __init__.py
│   └── res_config.py
├── security/
│   └── ir.model.access.csv
├── static/
│   └── src/
│       ├── js/
│       │   └── environment_banner.js
│       └── xml/
│           └── environment_banner.xml
└── views/
    └── templates.xml
```

---

## Compatibility

| Odoo version | Odoo.sh | Self-hosted |
|---|---|---|
| 18.0 | ✅ | ⚠️ `ODOO_STAGE` must be set manually |

On self-hosted instances `ODOO_STAGE` is not set automatically. You can set it manually in your server environment or `odoo.conf` equivalent before starting Odoo.

---

## License

LGPL-3
