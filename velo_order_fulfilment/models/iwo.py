# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class velo_order_iwo(models.Model):
	_name = 'order.iwo'
	_description = 'IWO'
	_rec_name =  'name'


	def action_proses(self):
		self.state = 'submit'

	def action_rcf(self):
		self.state = 'confirm'

	def action_preview(self):
		self.state = 'submit'

	def action_cancel(self):
		self.state = 'draft'

	name = fields.Char(string="Name")
	registration_date = fields.Date(string="Registration Date")
	iwo_issue_date = fields.Date(string="IWO Issue Date")

	signed_reg_form = fields.Boolean(string="Signed Reg Form")
	signed_final_quotation = fields.Boolean(string="Signed Final Quotation")
	approve_gp_price = fields.Boolean(string="Approve GP/Price")
	marketing_associate_doc = fields.Boolean(string="Marketing Associate Doc")
	cita = fields.Boolean(string="CITA")

	customer_name = fields.Many2one("res.partner",string="Customer Name")
	customer_code = fields.Char(related="customer_name.id_object",string="Customer Code")
	npwp = fields.Char(string="NPWP")
	activation_address = fields.Char(related="customer_name.street",string="Activation Address")
	billing_address = fields.Char(related="customer_name.street",string="Billing Address")
	phone = fields.Char(related="customer_name.phone",string="Phone / Fax")
	admin_contact = fields.Char(string="Admin Contact / Position")
	admin_email = fields.Char(string="Email")
	installation_contact = fields.Char(string="Installation")
	installation_email = fields.Char(string="Email")
	billing_contact = fields.Char(string="Billing")
	billing_email = fields.Char(string="Email")

	category_of_solution = fields.Selection([('network_service', 'Network Service'), ('value_added_service', 'Value Added Service'), ('managed_service', 'Managed Service'), ('system_integration', 'System Integration')],string="Category of Solution")
	type_of_service = fields.Selection([('internet_bandwidth','Internet Bandwidth'), ('vpn_mpls','VPN / MPLS'), ('collocation','Collocation'), ('broadband','Broadband'), ('network_management','Network Management'), ('hosted_application','Hosted Application'), ('seat_management','Seat Management'), ('bussines_continuity','Bussines Continuity'), ('system_integration','System Integration'), ('others','Others')],string="Type of Service")

	service_details = fields.Char(string="Service Details")
	remarks = fields.Char(string="Remarks")
	pop = fields.Char(string="POP")
	expected_activation_date = fields.Date(string="Expected Activation Date")
	am = fields.Char(string="AM")

	registration_fee = fields.Float(string="Registration Fee")
	monthly_subscription_fee = fields.Float(string="Monthly Subscription Fee")
	others_fee = fields.Float(string="Others Fee (Trading/Project/BOD")
	total_selling_price = fields.Float(string="Total Selling Price")
	montly_fee = fields.Float(string="1st Montly Fee / Billing Fee")
	billing_fee = fields.Float(string="1st Billing Fee")
	standart_tariff = fields.Float(string="Standart Tariff / Cost Price")
	average_discount = fields.Float(string="Average Discount")
	average_gp = fields.Float(string="Average GP")
	iwo_id = fields.Many2one('order.fulfilment',string="IWO")

	state = fields.Selection([('draft','Draft'),('submit','Submited'),('confirm','Confirmed')], string="State", default='draft')