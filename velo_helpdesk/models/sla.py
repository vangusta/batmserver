# -*- coding: utf-8 -*-

from odoo import models, fields, api

class velo_helpdesk_sla(models.Model):
	_name = 'helpdesk.sla.report'
	_description = 'Model Menu Helpdesk SLA'
	_rec_name  = 'customer'

	customer = fields.Many2one("res.partner", string="Customer")
	period_start = fields.Datetime(string="Period Start")
	period_end = fields.Datetime(string="Period End")
	upload_network_topology = fields.Binary(string="Upload Network Topology")
	upload_traffic_utilization = fields.Binary(string="Upload Traffic Utilization")

       