# -*- coding: utf-8 -*-

from odoo import models, fields, api


class velo_vsd(models.Model):
    _name = 'vsd'
    _description = 'Model Menu VSD'
    _rec_name = 'name'

    @api.depends('leads_acquired_ids')
    def _leads_acquired(self):
        for a in self:
            a.leads_acquired =  len(a.leads_acquired_ids)

    name = fields.Char(string='Campaign Name')
    campaign_scheduled = fields.Datetime(string="Campaign Schedule")
    campaign_done = fields.Datetime(string="Campaign Done")
    partner = fields.Many2one("res.partner",string="Partner")
    program = fields.Many2one("velo.program",string="Program")
    expected_leads = fields.Integer(string='Expected Leads')
    leads_acquired = fields.Integer(string='Leads Acquired', compute="_leads_acquired")
    industry = fields.Many2one("pop.type",string='Industry')
    regional = fields.Many2one("pop.regional",string='Regional')
    leads_acquired_ids = fields.One2many("vsd.leads.acquired","leads_acquired_id",string='Leads Acquired')
    campaign_cost_ids = fields.One2many("vsd.campaign.cost","campaign_cost_id",string='Campaign Cost')
    forecast_ids = fields.One2many("vsd.budget.forecast","forecast_id",string='Budget Forecast')


class velo_vsd_leads_acquired(models.Model):
    _name = 'vsd.leads.acquired'
    _description = 'Model Menu Leads Acquired'
    _rec_name = 'company'

    leads_acquired_id = fields.Many2one("vsd",string='Leads Acquired')
    company = fields.Many2one('res.partner',string='Company Name')
    pop = fields.Many2one('pop.service.coverage',string="POP")
    budget = fields.Float(string="Budget")
    existing = fields.Char(string="Existing")
    pop_location = fields.Many2one("pop.service.coverage",string="POP Location")
    sales_pipeline = fields.Many2one('crm.lead',string='Sales Pipeline')
    remarks = fields.Char(string='Remarks')


class velo_campaign_cost(models.Model):
    _name = 'vsd.campaign.cost'
    _description = 'Model Menu Campaign Cost'
    _rec_name = 'cost_name'

    campaign_cost_id = fields.Many2one("vsd",string='Campaign Cost')
    cost_name = fields.Float(string='Cost Name')
    cost = fields.Float(string="COST")
    qty = fields.Integer(string="Quantity")
    desc = fields.Char(string="Desc")
    total_costs = fields.Float(string="Total Costs") 

class velo_budget_forecast(models.Model):
    _name = 'vsd.budget.forecast'
    _description = 'Model Menu Budget Forecast'
    _rec_name = 'cost_name'

    forecast_id = fields.Many2one("vsd",string='Budget Forecast')
    cost_name = fields.Float(string='Cost Name')
    cost = fields.Float(string="COST")
    qty = fields.Integer(string="Quantity")
    desc = fields.Char(string="Desc")
    total_costs = fields.Float(string="Total Costs")

