# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# fix
{
    'name': 'Marketing Program',
    'version': '1.1',
    'category': 'CRM',
    'sequence': 75,
    'summary': 'Program and Promotion',
    'description': "",
    'website': 'https://velo.co.id/',
    'author': 'Tim BATM',
    'images': [
    ],
    'depends': [
        'product',
        'crm',
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/program_promotion.xml',
        'views/promotion.xml',
        'views/overview.xml',
    ],
    'sequence':3,
    'installable': True,
    'application': True,
    'auto_install': False,
}
