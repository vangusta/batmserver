# -*- coding: utf-8 -*-

from odoo import models, fields, api

class velo_helpdesk_pinalty(models.Model):
	_name = 'helpdesk.pinalty'
	_description = 'Model Menu Helpdesk pinalty'
	_rec_name  = 'call_time'

	call_time = fields.Datetime(string="Call Time")
	helpdesk_ticket = fields.Many2one("helpdesk.ticket", string="Helpdesk Ticket")
	ticket_number = fields.Char(related="helpdesk_ticket.ticket", string="Ticket Number")
	customer = fields.Many2one(related="helpdesk_ticket.partner_id", string="Customer")
	solved = fields.Datetime(string="Solved")
	total_outage = fields.Float(string="Total Outage")
	entire_pinalty = fields.Float(string="Entire Pinalty")
	monthly_tarif = fields.Float(string="Monthly Tarif")
	amount = fields.Float(string="Amount")
	sub_problem_category = fields.Char(string="Sub Problem Category")

       