# -*- coding: utf-8 -*-

from odoo import models, fields, api


class velo_osc(models.Model):
    _name = 'osc'
    _description = 'Model Menu OSC'
    _rec_name = 'name'

    @api.depends('leads_acquired_ids')
    def _leads_acquired(self):
        for a in self:
            a.leads_acquired =  len(a.leads_acquired_ids)

    name = fields.Char(string='Campaign Name')
    campaign_scheduled = fields.Datetime(string="Campaign Schedule")
    campaign_done = fields.Datetime(string="Campaign Done")
    campaign_duration = fields.Integer(string="Campaign Duration")
    pop_location = fields.Many2one("pop.service.coverage",string="POP Location")
    expected_leads = fields.Integer(string='Expected Leads')
    leads_acquired = fields.Integer(string='Leads Acquired', compute="_leads_acquired")
    program = fields.Many2one("velo.program",string='Program')
    leads_acquired_ids = fields.One2many("osc.leads.acquired","leads_acquired_id",string='Leads Acquired')
    campaign_cost_ids = fields.One2many("osc.campaign.cost","campaign_cost_id",string='Campaign Cost')
    forecast_ids = fields.One2many("osc.budget.forecast","forecast_id",string='Budget Forecast')


class velo_osc_leads_acquired(models.Model):
    _name = 'osc.leads.acquired'
    _description = 'Model Menu Leads Acquired'
    _rec_name = 'company'

    leads_acquired_id = fields.Many2one("osc",string='Leads Acquired')
    company = fields.Many2one('res.partner',string='Company Name')
    pop = fields.Many2one('pop.service.coverage',string="POP")
    budget = fields.Float(string="Budget")
    existing = fields.Char(string="Existing")
    pop_location = fields.Many2one("pop.service.coverage",string="POP Location")
    sales_pipeline = fields.Many2one('crm.lead',string='Sales Pipeline')
    remarks = fields.Char(string='Remarks')


class velo_campaign_cost(models.Model):
    _name = 'osc.campaign.cost'
    _description = 'Model Menu Campaign Cost'
    _rec_name = 'cost_name'

    campaign_cost_id = fields.Many2one("osc",string='Campaign Cost')
    cost_name = fields.Float(string='Cost Name')
    cost = fields.Float(string="COST")
    qty = fields.Integer(string="Quantity")
    desc = fields.Char(string="Desc")
    total_costs = fields.Float(string="Total Costs") 

class velo_budget_forecast(models.Model):
    _name = 'osc.budget.forecast'
    _description = 'Model Menu Budget Forecast'
    _rec_name = 'cost_name'

    forecast_id = fields.Many2one("osc",string='Budget Forecast')
    cost_name = fields.Float(string='Cost Name')
    cost = fields.Float(string="COST")
    qty = fields.Integer(string="Quantity")
    desc = fields.Char(string="Desc")
    total_costs = fields.Float(string="Total Costs")

