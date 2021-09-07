# -*- coding: utf-8 -*-
{
    'name': "Sales Pipeline",

    'summary': """
        Sales Pipeline""",

    'description': """
        CRM modul
    """,

    'website': 'https://velo.co.id/',
    'author': 'Tim BATM',

    'category': 'CRM',
    'version': '0.1',

    'depends': ['base','crm'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'data/crm_stage_data.xml',
    ],
    'sequence':6,
    'application':True,
    'installable': True,
    'auto_install': False,
}