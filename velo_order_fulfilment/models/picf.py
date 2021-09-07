# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class velo_order_picf(models.Model):
	_name = 'order.picf'
	_description = 'PICF'
	_rec_name =  'name'

	def action_proses(self):
		self.state = 'active'

	def action_cancel(self):
		self.state = 'draft'


	name = fields.Char(string="Name")
	company_name = fields.Many2one("res.partner",string="Company Name")
	company_address = fields.Char(related="company_name.street",string="Company Address")
	company_phone = fields.Char(related="company_name.phone",string="Phone")
	company_email = fields.Char(related="company_name.email",string="Email")
	
	current_service = fields.Char(string="Current Service")
	current_provider = fields.Char(string="Current Provider")
	challenges = fields.Char(string="challenges/Issues")

	type_of_service = fields.Selection([('internet', 'Internet'), ('data_center_cloud', 'Data center / Cloud'), ('vpn_vsat', 'VPN/VSAT'), ('managed_service', 'Managed Service')],string="Type of Service")

	bandwide_capacity = fields.Many2one("product.product", string="Bandwide Capacity")
	type_of_lasmile = fields.Many2one("product.product", string="Type of Lasmile")
	reachable_service_coverage = fields.Many2one("product.product", string="Reachable Service Coverage")
	topology = fields.Many2one("product.product", string="Topology")
	backup_coverage = fields.Many2one("product.product", string="Backup Coverage")
		
	cpe_requirement = fields.Selection([('routers', 'Routers'), ('proxy', 'Proxy'), ('firewall', 'Firewall'), ('switch', 'Switch')],string="CPE Requirement")
	lasmine_requirement = fields.Selection([('cabling', 'Cabling'), ('antena', 'Antena'), ('pole', 'Pole (Tower)'), ('other', 'Other')],string="Lasmine Requirement")

	migration_from_existing = fields.Char(string="Migration from Existing")

	availability = fields.Char(string="Availability")
	bw_guarantee = fields.Char(string="BW Guarantee")
	support = fields.Char(string="support")
	other1 = fields.Char(string="others")
	other2 = fields.Char(string="others")

	specific_requirements = fields.Char(string="Specific Requirements")
	
	registration_date = fields.Date(string="Registration Date")
	reference_po_number = fields.Char(string="Reference/PO Number")
	expected_activated_date = fields.Date(string="Expected Activated Date")
	acceptence_date = fields.Date(string="Acceptence Date")

	state = fields.Selection([('draft','Draft'),('active','Active')], string="State", default='draft')
	pcif_id = fields.Many2one('order.fulfilment',string="PCIF")