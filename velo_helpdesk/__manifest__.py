# -*- coding: utf-8 -*-
{
    'name': "Helpdesk",

    'summary': """
        Velo Helpdesk""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Tim BATM",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','helpdesk','velo_customers'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/pinalty.xml',
        'views/sla.xml',
        'views/report_graph.xml',
    ],
    'sequence':11,
    'application':True,
    'installable': True,
    'auto_install': False,
}