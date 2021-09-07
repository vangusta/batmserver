# -*- coding: utf-8 -*-
{
    'name': "Order Fulfilment",

    'summary': """
        Sales order""",

    'description': """
        Sales order
    """,

    'website': 'https://velo.co.id/',
    'author': 'Tim BATM',
    'category': 'Sales',
    'version': '0.1',
    'depends': ['base','sale_management','velo_customers','velo_service_coverage'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'sequences/so_sequence.xml',
        'views/acc_views.xml',
        'views/acmrf_views.xml',
        'views/bcrf_views.xml',
        'views/cperf_views.xml',
        'views/iwo_views.xml',
        'views/picf_views.xml',
        'views/sale_order_views.xml',
    ],

    'sequence':8,
    'application':True,
    'installable': True,
    'auto_install': False,
}