# -*- coding: utf-8 -*-
{
    'name': "Account Management",

    'summary': """
        Marketing Activities""",

    'description': """
        mass_mailing
    """,

    'website': 'https://velo.co.id/',
    'author': 'Tim BATM',

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','mass_mailing','velo_customers'],

    'data': [
        'security/ir.model.access.csv',
        'data/summary_data.xml',
        'views/views.xml',
        'views/telemarketing.xml',
        'views/osc_views.xml',
        'views/vsd_views.xml',
        'views/tradeshow_views.xml',
        'views/velomania_views.xml',
        'views/marketing_overview_views.xml',
    ],
 
    'sequence': 4,
    'installable': True,
    'application': True,
    'auto_install': False,
}