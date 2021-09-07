# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class velo_order_bcrf(models.Model):
	_name = 'order.bcrf'
	_description = 'BCRF'
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
	product_type = fields.Many2one("product.product",string="Product Type")
	capacity = fields.Integer(string="Capacity")
	rack_server = fields.Char(string="Rack/Server")
	other = fields.Char(string="Other")

	backhaul = fields.Many2one("product.product", string="Backhaul")
	upgrade_downgrade_backhaul = fields.Many2one("product.product", string="Upgrade/Downgrade")
	nearend = fields.Many2one("product.product", string="Nearend")
	farend = fields.Char(string="Farend")
	existing_capacity_backhaul = fields.Char(string="Existing Capacity")
	new_capacity_backhaul = fields.Char(string="New Capacity")
	existing_capacity_cost_backhaul = fields.Char(string="Existing Capacity Cost/month")
	new_capacity_cost_backhaul = fields.Char(string="New Capacity Cost/month")
	effective_date_backhaul = fields.Date(string="Effective Date")
	increase_decrease_backhaul = fields.Char(string="Increase/Decrease(cost)")

	lastmile_direct = fields.Many2one("product.product", string="Lastmile/Direct")
	upgrade_downgrade_lastmile = fields.Many2one("product.product", string="Upgrade/Downgrade")
	existing_capacity_lastmile = fields.Char(string="Existing Capacity")
	new_capacity_lastmile = fields.Char(string="New Capacity")
	existing_capacity_cost_lastmile = fields.Char(string="Existing Capacity Cost/month")
	new_capacity_cost_lastmile = fields.Char(string="New Capacity Cost/month")
	effective_date_lastmile = fields.Date(string="Effective Date")
	increase_decrease_lastmile = fields.Char(string="Increase/Decrease(cost)")

	vpn_link = fields.Many2one("product.product", string="VPN Link")
	upgrade_downgrade_vpn = fields.Many2one("product.product", string="Upgrade/Downgrade")
	existing_capacity_vpn = fields.Char(string="Existing Capacity")
	new_capacity_vpn = fields.Char(string="New Capacity")
	existing_capacity_cost_vpn = fields.Char(string="Existing Capacity Cost/month")
	new_capacity_cost_vpn = fields.Char(string="New Capacity Cost/month")
	effective_date_vpn = fields.Date(string="Effective Date")
	increase_decrease_vpn = fields.Char(string="Increase/Decrease(cost)")

	vsat_link = fields.Many2one("product.product", string="VSAT Link")
	upgrade_downgrade_vsat = fields.Many2one("product.product", string="Upgrade/Downgrade")
	existing_capacity_vsat = fields.Char(string="Existing Capacity")
	new_capacity_vsat = fields.Char(string="New Capacity")
	existing_capacity_cost_vsat = fields.Char(string="Existing Capacity Cost/month")
	new_capacity_cost_vsat = fields.Char(string="New Capacity Cost/month")
	effective_date_vsat = fields.Date(string="Effective Date")
	increase_decrease_vsat = fields.Char(string="Increase/Decrease(cost)")

	state = fields.Selection([('draft','Draft'),('active','Active')], string="State", default='draft')

