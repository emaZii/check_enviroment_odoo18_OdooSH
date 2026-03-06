import os
import logging
from odoo import api, models

_logger = logging.getLogger(__name__)

class EnvironmentBanner(models.Model):
    _name = 'environment.banner'
    _description = 'Environment Banner Helper'

    @api.model
    def get_stage(self):
        stage = os.environ.get('ODOO_STAGE', 'NON IMPOSTATA')
        #branch = os.environ.get('GITHUB_BRANCH', 'NON IMPOSTATA')
        #_logger.info("=== ENVIRONMENT BANNER === GITHUB_BRANCH = '%s'", branch)
        _logger.info("=== ENVIRONMENT BANNER === ODOO_STAGE = '%s'", stage)
        if stage not in ('production', 'staging', 'dev'):
            stage = 'NON IMPOSTATA'
        return stage
    
    @api.model
    def log_enviroment(self):
        stage = os.environ.get('ODOO_STAGE', 'NON IMPOSTATA')
        #branch = os.environ.get('GITHUB_BRANCH', 'NON IMPOSTATA')
        _logger.info("=== ENVIRONMENT BANNER === ODOO_STAGE = '%s'", stage)
        #_logger.info("=== ENVIRONMENT BANNER === GITHUB_BRANCH = '%s'", branch)