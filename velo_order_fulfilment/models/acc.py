# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class velo_order_acc(models.Model):
	_name = 'order.acc'
	_description = 'ACC'
	_rec_name =  'name'

	def action_proses(self):
		self.state = 'active'

	def action_cancel(self):
		self.state = 'draft'

	name = fields.Char(string="Name")
	company_name = fields.Many2one("res.partner",string="Company Name")
	company_address = fields.Char(related="company_name.street",string="Company Address")
	company_phone = fields.Char(related="company_name.phone",string="Phone")
	cp = fields.Char(string="Name")
	activation_date = fields.Date(string="Activation Date")
	invoice_date = fields.Date(string="Start Invoice Date")
	contract_tarif = fields.Float(string="Contract Tarif")
	tect_cp = fields.Char(string="Tech Contact person")
	bill_cp = fields.Char(string="Billing Contact Person")

	iwo_ref = fields.Many2one("order.iwo",string="IWO Ref No")
	order_type = fields.Char(string="Order Type")

	ip_address = fields.Char(string="IP Address")
	subnet = fields.Char(string="Subnet")
	gateway = fields.Char(string="Gateway")
	dns = fields.Char(string="DNS")
	smtp = fields.Char(string="SMTP")
	mrtg = fields.Char(string="MRTG")
	lan = fields.Char(string="LAN")
	subnet2 = fields.Char(string="SUBNET")
	gateway2 = fields.Char(string="GATEWAY")
	dns2 = fields.Char(string="DNS 2")
	range_ip = fields.Char(string="Range IP")
	user = fields.Char(string="User")
	password = fields.Char(string="Password")

	router_firewall = fields.Char(string="Router / Filewall")
	hub_switch = fields.Char(string="Hub / Switch")
	access_point = fields.Char(string="Access Point")
	others = fields.Char(string="Others")
	acc_id = fields.Many2one('order.fulfilment',string="ACC")

	state = fields.Selection([('draft','Draft'),('active','Active')], string="State", default='draft')