# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class velo_order_fulfilment(models.Model):
	_name = 'order.fulfilment'
	_description = 'Order Fulfilment Pipeline'
	_rec_name =  'name'

	def action_proses(self):
		self.state = 'active'

	def action_cancel(self):
		self.state = 'draft'

	def create_iwo(self):
		ctx = dict(self._context)
		ctx.update({'search_default_project_id': self.id})
		action = self.env['ir.actions.act_window'].for_xml_id('velo_order_fulfilment', 'action_velo_order_iwo')
		return dict(action, context=ctx)

	def create_cperf(self):
		ctx = dict(self._context)
		ctx.update({'search_default_project_id': self.id})
		action = self.env['ir.actions.act_window'].for_xml_id('velo_order_fulfilment', 'action_velo_order_cperf')
		return dict(action, context=ctx)

	def create_bcrf(self):
		ctx = dict(self._context)
		ctx.update({'search_default_project_id': self.id})
		action = self.env['ir.actions.act_window'].for_xml_id('velo_order_fulfilment', 'action_velo_order_bcrf')
		return dict(action, context=ctx)

	def create_acmrf(self):
		ctx = dict(self._context)
		ctx.update({'search_default_project_id': self.id})
		action = self.env['ir.actions.act_window'].for_xml_id('velo_order_fulfilment', 'action_velo_order_acmrf')
		return dict(action, context=ctx)

	def create_acc(self):
		ctx = dict(self._context)
		ctx.update({'search_default_project_id': self.id})
		action = self.env['ir.actions.act_window'].for_xml_id('velo_order_fulfilment', 'action_velo_order_acc')
		return dict(action, context=ctx)

	name = fields.Char(string="Name")
	company_name = fields.Many2one("res.partner",string="Company Name")
	company_address = fields.Char(related="company_name.street",string="Company Address")
	company_phone = fields.Char(related="company_name.phone",string="Phone")
	
	new_retention = fields.Many2one("order.retention",string="New / Retention")
	downgrade_upgrade = fields.Many2one("product.product",string="Downgrade / Upgrade")
	service_amount = fields.Float(string="Service Amount")
	contract_period = fields.Char(string="Contract Period")
	order_lines = fields.Many2many("product.product",string="Order Lines")

	pcif_ids = fields.One2many('order.picf', 'pcif_id', string="PCIF Ids")
	iwo_ids = fields.One2many('order.iwo', 'iwo_id', string="IWO Ids")
	acc_ids = fields.One2many('order.acc', 'acc_id', string="ACC Ids")

	state = fields.Selection([('request_service','Request Service'),('fulfilment','Fulfilment'),('activation','Activation'),('contract_signed','Contract Signed')], string="State", default='request_service')






class velo_order_retention(models.Model):
	_name = 'order.retention'
	_description = 'Order retention'
	_rec_name =  'name'


	name = fields.Char(string="Name")

