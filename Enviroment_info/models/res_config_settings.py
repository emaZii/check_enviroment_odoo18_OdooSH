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

    @api.model
    def log_enviroment(self):
        stage = os.environ.get('ODOO_STAGE', 'NON IMPOSTATA')
        branch = os.environ.get('GITHUB_BRANCH', 'NON IMPOSTATA')
        _logger.info("=== ENVIRONMENT BANNER === ODOO_STAGE = '%s'", stage)
        _logger.info("=== ENVIRONMENT BANNER === GITHUB_BRANCH = '%s'", branch)
            
