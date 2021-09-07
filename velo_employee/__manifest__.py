# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# fix
{
    'name': 'Employee & User',
    'version': '1.1',
    'category': 'hr_employee',
    'sequence': 75,
    'summary': 'Employee & User',
    'description': "",
    'website': 'https://velo.co.id/',
    'author': 'Tim BATM',
    'images': [
        'images/hr_department.jpeg',
        'images/hr_employee.jpeg',
        'images/hr_job_position.jpeg',
        'static/src/img/default_image.png',
    ],
    'depends': [
        'hr'
    ],
    'data': [
        'views/menu.xml',
    ],
    'sequence': 2,
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'qweb': ['static/src/xml/hr_templates.xml'],
}
