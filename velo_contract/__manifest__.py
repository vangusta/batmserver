# -*- coding: utf-8 -*-
{
    'name': "Contract",

    'summary': """
        sale_subcription""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Tim BATM",
    'website': "https://batmandiri.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','sale_subscription','velo_service_coverage','velo_customers'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    'sequence':10,
    'application':True,
    'installable': True,
    'auto_install': False,
}