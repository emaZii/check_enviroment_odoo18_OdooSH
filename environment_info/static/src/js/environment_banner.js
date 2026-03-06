/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";


const style = document.createElement("style");
style.textContent = `
    .o_environment_banner {
        width: 100%;
        text-align: center;
        padding: 5px 16px;
        font-weight: 700;
        font-size: 12px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .o_environment_banner_pulse {
        animation: env-pulse 2.5s ease-in-out infinite;
    }
    @keyframes env-pulse {
        0%, 100% { opacity: 1; }
        50%       { opacity: 0.65; }
    }
`;
document.head.appendChild(style);


const ENV_CONFIG = {
    production: {
        label: "PRODUCTION",
        color: "#1b5e20",
        bg: "#e8f5e9",
        border: "#a5d6a7",
        pulse: false,
    },
    staging: {
        label: "STAGING",
        color: "#bf360c",
        bg: "#fff3e0",
        border: "#ffcc80",
        pulse: true,
    },
    dev: {
        label: "DEVELOPMENT",
        color: "#0d47a1",
        bg: "#e3f2fd",
        border: "#90caf9",
        pulse: false,
    },
};


class EnvironmentBanner extends Component {
    static template = "environment_banner.Banner";
    static props = ["*"];

    setup() {
        const stage = window.__odoo_env_stage || "production";
        const config = ENV_CONFIG[stage] || ENV_CONFIG["production"];

        console.log("[EnvironmentBanner] stage =", stage);

        this.state = useState({
            loaded: true,
            stage: stage,
            ...config,
        });
    }
}


registry.category("systray").add(
    "environment_banner",
    { Component: EnvironmentBanner, sequence: 1 },
    { force: true }
);
