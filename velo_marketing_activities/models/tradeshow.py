# -*- coding: utf-8 -*-

from odoo import models, fields, api


class velo_tradeshow(models.Model):
    _name = 'tradeshow'
    _description = 'Model Menu Tradeshow'
    _rec_name = 'name'

    @api.depends('leads_acquired_ids')
    def _leads_acquired(self):
        for a in self:
            a.leads_acquired =  len(a.leads_acquired_ids)

    name = fields.Char(string='Tradeshow Name')
    campaign_scheduled = fields.Datetime(string="Campaign Schedule")
    campaign_duration = fields.Integer(string="Campaign Duration")
    location = fields.Many2one("pop.regional",string="Location")
    industry = fields.Many2one("pop.type",string="Industry")
    expected_leads = fields.Integer(string='Expected Leads')
    leads_acquired = fields.Integer(string='Leads Acquired', compute="_leads_acquired")
    
    leads_acquired_ids = fields.One2many("tradeshow.leads.acquired","leads_acquired_id",string='Leads Acquired')
    campaign_cost_ids = fields.One2many("tradeshow.campaign.cost","campaign_cost_id",string='Campaign Cost')


class velo_tradeshow_leads_acquired(models.Model):
    _name = 'tradeshow.leads.acquired'
    _description = 'Model Menu Leads Acquired'
    _rec_name = 'company'

    leads_acquired_id = fields.Many2one("tradeshow",string='Leads Acquired')
    company = fields.Many2one('res.partner',string='Company Name')
    industry = fields.Many2one("pop.type",string="Industry")
    budget = fields.Float(string="Budget")
    existing = fields.Char(string="Existing")
    sales_pipeline = fields.Many2one('crm.lead',string='Sales Pipeline')
    remarks = fields.Char(string='Remarks')


class velo_campaign_cost(models.Model):
    _name = 'tradeshow.campaign.cost'
    _description = 'Model Menu Campaign Cost'
    _rec_name = 'cost_name'

    campaign_cost_id = fields.Many2one("tradeshow",string='Campaign Cost')
    cost_name = fields.Float(string='Cost Name')
    cost = fields.Float(string="COST")
    qty = fields.Integer(string="Quantity")
    desc = fields.Char(string="Desc")
    total_costs = fields.Float(string="Total Costs") 


