import os
from odoo import api, models


class EnvironmentBanner(models.AbstractModel):
    _name = 'environment.banner'
    _description = 'Environment Banner Helper'

    @api.model
    def get_stage(self):
        stage = os.environ.get('ODOO_STAGE', 'production')
        if stage not in ('production', 'staging', 'dev'):
            stage = 'production'
        return stage