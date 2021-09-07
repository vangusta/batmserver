# -*- coding: utf-8 -*-

from odoo import models, fields, api

class velo_erp_interface(models.Model):
    _name = 'erp.interface.test'
    _description = 'Model Menu ERP Interface'
    _rec_name = 'name'

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")