import os
from odoo import http
from odoo.http import request


class EnvironmentBannerController(http.Controller):

    #@http.route('/web/environment_banner/info', type='json', auth='user')
    def get_environment_info(self):
        pass
