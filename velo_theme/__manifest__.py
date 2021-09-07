# -*- coding: utf-8 -*-
{
    'name': "Theme",

    'summary': """
        Velo Theme""",

    'description': """
        Theme for velo
    """,

    'author': "Tim BATM",
    'website': "http://www.yourcompany.com",

    'category': 'Theme',
    'version': '1.1',

    'depends': ['base','web_studio', 'velo_service_coverage', 'velo_customers', 'velo_employee',
                'velo_marketing_activities','velo_sales_pipeline','velo_retention_pipeline','velo_order_fulfilment',
                'velo_pop_pipeline','velo_contract','velo_helpdesk','velo_erp_interface','velo_product_pricing','velo_program_promotion'],

    'data': [
        'views/templates.xml',
        
        # 'security/marketing/marketing_security.xml',
        # 'security/marketing/maker1/ir.model.access.csv',
        # 'security/marketing/maker2/ir.model.access.csv',
        # 'security/marketing/checker/ir.model.access.csv',
        # 'security/marketing/advisor/ir.model.access.csv',
        # 'security/marketing/admin/ir.model.access.csv',
        # 'security/marketing/superadmin/ir.model.access.csv',

        # 'security/sales/sales_security.xml',
        # 'security/sales/maker1/ir.model.access.csv',
        # 'security/sales/maker2/ir.model.access.csv',
        # 'security/sales/checker/ir.model.access.csv',
        # 'security/sales/advisor/ir.model.access.csv',
        # 'security/sales/admin/ir.model.access.csv',
        # 'security/sales/superadmin/ir.model.access.csv',

        # 'security/finance/finance_security.xml',
        # 'security/finance/maker1/ir.model.access.csv',
        # 'security/finance/maker2/ir.model.access.csv',
        # 'security/finance/checker/ir.model.access.csv',
        # 'security/finance/advisor/ir.model.access.csv',
        # 'security/finance/admin/ir.model.access.csv',
        # 'security/finance/superadmin/ir.model.access.csv',

        # 'security/operation/operation_security.xml',
        # 'security/operation/maker1/ir.model.access.csv',
        # 'security/operation/maker2/ir.model.access.csv',
        # 'security/operation/checker/ir.model.access.csv',
        # 'security/operation/advisor/ir.model.access.csv',
        # 'security/operation/admin/ir.model.access.csv',
        # 'security/operation/superadmin/ir.model.access.csv',

        'security/spv/supervisor/ir.model.access.csv',
        'security/spv/supervisor_security.xml',

        'security/mng/manager/ir.model.access.csv',
        'security/mng/manager_security.xml',

        'security/am/am/ir.model.access.csv',
        'security/am/am_security.xml',

        # 'security/accounting_user/accounting_user/ir.model.access.csv',
        'security/accounting_user/accounting_user_security.xml',

         # 'security/am/am/ir.model.access.csv',
        'security/finance_user/finance_user_security.xml',

         # 'security/am/am/ir.model.access.csv',
        'security/management/management_security.xml',

         # 'security/am/am/ir.model.access.csv',
        'security/marketing_user/marketing_user_security.xml',

         # 'security/am/am/ir.model.access.csv',
        'security/operation_user/operation_user_security.xml',

         # 'security/am/am/ir.model.access.csv',
        'security/super_user/super_user_security.xml',




    ],
    'qweb': [
        'static/src/xml/base.xml',
        'static/src/xml/board.xml',
        'static/src/xml/base_ent.xml',
        'static/src/xml/web_base.xml',
        'static/src/xml/chart.xml',
    ],
    'sequence': 1,
    'application': True,
    'installable': True,
}
