# -*- coding: utf-8 -*-
{
    'name': "Product & Pricing",

    'summary': """
        Velo Product & Pricing Menu""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Tim BATM",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '1.1',

    'depends': ['base', 'sale', 'sale_management', 'helpdesk','velo_customers'],

    'data': [
        'security/ir.model.access.csv',
        'views/pricing_all_region.xml',
        'views/pricing_bali.xml',
        'views/pricing_jakarta.xml',
        'views/pricing_bandung.xml',
        'views/pricing_semarang.xml',
        'views/pricing_surabaya.xml',
        'views/pricing_yogyakarta.xml',
        'views/product_views.xml',
        'views/product_overview_views.xml',
        'views/product_validity.xml',
        'views/product_validitys.xml',
        'data/summary_data.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': ['static/src/xml/board.xml'],
    'sequence':2,
    'application': True,
    'installable': True,
}
