# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class velo_order_acmrf(models.Model):
	_name = 'order.acmrf'
	_description = 'ACMRF'
	_rec_name =  'name'

	def action_proses(self):
		self.state = 'active'

	def action_cancel(self):
		self.state = 'draft'

	name = fields.Char(string="Name")
	company_name = fields.Many2one("res.partner",string="Company Name")
	company_address = fields.Char(related="company_name.street",string="Company Address")
	company_phone = fields.Char(related="company_name.phone",string="Phone")
	brand_name = fields.Many2one(related="company_name.brand_object",string="Branch Name")

	activation_date = fields.Date(string="Activation Date")
	invoice_date = fields.Date(string="Start Invoice Date")
	contract_tarif = fields.Float(string="Contract Tarif")
	tect_cp = fields.Char(string="Tech Contact person")
	bill_cp = fields.Char(string="Billing Contact Person")

	iwo_ref = fields.Many2one("order.iwo",string="IWO Ref No")
	product_type = fields.Many2one("product.product", string="Product Type")
	capacity = fields.Char(string="Capacity")
	rack_server = fields.Char(string="Rack/Server")
	other1 = fields.Char(string="Other")

	cabling_installation = fields.Many2one("product.product", string="Cabling Installation")
	number_of_pulled = fields.Char(string="Number of Pulled")
	specification = fields.Char(string="Specification")
	preference_partner = fields.Many2one("res.partner",string="Preference Partner")

	ups_voltage_regulator = fields.Many2one("product.product", string="UPS / Voltage_regulator")
	specification = fields.Char(string="Specification")
	preference_partner = fields.Many2one("res.partner",string="Preference Partner")

	antena_tower = fields.Many2one("product.product", string="Antena Tower")
	specification = fields.Char(string="Specification")
	preference_partner = fields.Many2one("res.partner",string="Preference Partner")

	grounding = fields.Many2one("product.product", string="Grounding")
	specification = fields.Char(string="Specification")
	preference_partner = fields.Many2one("res.partner",string="Preference Partner")

	other2 = fields.Char(string="Other")

	state = fields.Selection([('draft','Draft'),('active','Active')], string="State", default='draft')
