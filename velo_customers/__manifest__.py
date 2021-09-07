# -*- coding: utf-8 -*-
{
    'name': "Customers",

    'summary': """
        Customers""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Tim BATM",
    'website': "https://batmandiri.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # fix
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','velo_service_coverage','sale_subscription','crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'security/security.xml',
        'views/views.xml',
        'views/tenant_views.xml',
        'views/pop_pic_views.xml',
        # 'data/summary_data.xml',
        'views/customer_overview_views.xml',
        'views/potential_overview_views.xml',
        'views/menu_views.xml',
        'views/pic_am_views.xml',
    ],
    'sequence':5,
    'application':True,
    'installable': True,
    'auto_install': False,
}