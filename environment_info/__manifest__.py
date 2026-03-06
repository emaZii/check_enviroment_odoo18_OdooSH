{
    'name': 'Environment Banner',
    'version': '18.0.1.0.0',
    'summary': 'Shows a banner indicating the current environment (staging/production)',
    'category': 'Technical',
    'depends': ['base_setup', 'web'],
    'data': [
        #'views/templates.xml',
        'data/cron.xml',
    ],
    'assets': {
        'web.assets_backend': [
            #'Enviroment_info/static/src/js/environment_banner.js',
            #'Enviroment_info/static/src/xml/enviroment_banner.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}