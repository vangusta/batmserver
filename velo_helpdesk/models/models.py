# -*- coding: utf-8 -*-

from odoo import models, fields, api

class velo_helpdesk(models.Model):
	_inherit = 'helpdesk.ticket'
	_description = 'Model Menu Helpdesk ticket'

	ticket = fields.Char(string="Ticket Number")
	impact_to = fields.Many2one('res.users', string="Impact to")
	parent_ticket = fields.Many2one('helpdesk.ticket', string="Parent Ticket")
	service = fields.Many2one('pop.service.coverage', string="Service")
	pop = fields.Char(related='service.pop_name', string="POP Name")
	pop_state = fields.Char(string="POP State" ,compute="_pop_state")

	saverity = fields.Char(string="Saverity")
	problem = fields.Char(string="Problem")
	characteristic = fields.Char(string="Characteristic")
	business_priority = fields.Char(string="Business Priority")
	duration = fields.Char(string="Total Duration (Minutes)")

	segment = fields.Char(string="Segment")
	problem_segment = fields.Char(string="Problem Segment")
	sub_problem_category = fields.Char(string="Sub Problem Category")
	service_impact = fields.Selection([('single', 'Single'), ('pop', 'POP'), ('regional_pop', 'Regional POP')], string="Service Impact")
	problem_description = fields.Char(string="Problem Description")

	assign_to = fields.Many2one("res.users", string="Assign To")
	progress = fields.Integer(string="Progress")
	internal_status = fields.Char(string="Internal Status")
	department = fields.Many2one('hr.department',string="Department")
	progress_action_details = fields.Char(string="Progress Action Details")
	supporting_file = fields.Binary(string="Supporting File")

	helpdesk_customer_ids = fields.One2many('helpdesk.customer','helpdesk_customer_id', string="Helpdesk Customer")
	helpdesk_internal_ids = fields.One2many('helpdesk.internal','helpdesk_internal_id', string="Helpdesk Internal")
	helpdesk_partner_ids = fields.One2many('helpdesk.partner','helpdesk_partner_id', string="Helpdesk Partner")
	helpdesk_ticket_list_ids = fields.One2many('helpdesk.ticket.list','helpdesk_ticket_list_id', string="Helpdesk Ticket List")




	@api.model
	def _pop_state(self):
		pop_id = self.service
		pop_state = self.env['pop.service.coverage'].search([('pop_id', '=', pop_id)])
		self.pop_state = pop_state.state

class velo_helpdesk_customer(models.Model):
	_name = 'helpdesk.customer'
	_description = 'Model Menu Helpdesk customer status'

	helpdesk_customer_id = fields.Many2one('helpdesk.ticket', string="Helpdesk Cust")
	status = fields.Char(string="Status")
	start_time = fields.Datetime(string="Start Time")
	finish_time = fields.Datetime(string="Finish Time")
	duration = fields.Float(string="Duration")


class velo_helpdesk_internal(models.Model):
	_name = 'helpdesk.internal'
	_description = 'Model Menu Helpdesk Internal status'

	helpdesk_internal_id = fields.Many2one('helpdesk.ticket', string="Helpdesk Int")
	exception_report = fields.Boolean(string="Exception Report")
	status = fields.Char(string="Status")
	start_time = fields.Datetime(string="Start Time")
	finish_time = fields.Datetime(string="Finish Time")
	action = fields.Char(string="Action")
	progress = fields.Char(string="Progress")
	pic = fields.Char(string="PIC")
	supporting_file = fields.Char(string="Supporting File")

class velo_helpdesk_partner(models.Model):
	_name = 'helpdesk.partner'
	_description = 'Model Menu Helpdesk Partner'

	helpdesk_partner_id = fields.Many2one('helpdesk.ticket', string="Helpdesk Partner")
	partner = fields.Many2one("res.partner", string="Partner Name")
	circuit_id = fields.Char(string="Circuit ID")
	start_time = fields.Datetime(string="Start Time")
	finish_time = fields.Datetime(string="Finish Time")
	duration = fields.Float(string="Duration")

class velo_helpdesk_ticket_list(models.Model):
	_name = 'helpdesk.ticket.list'
	_description = 'Model Menu Helpdesk Ticket List'

	helpdesk_ticket_list_id = fields.Many2one('helpdesk.ticket', string="Helpdesk Ticket List")
	helpdesk_ticket = fields.Char(string="Helpdesk Ticket")
	customer = fields.Many2one("res.partner", string="Customer")

