# -*- coding: utf-8 -*-

from odoo import models, fields, api


class velo_velomania(models.Model):
    _name = 'velomania'
    _description = 'Model Menu velomania'
    _rec_name = 'name'

    @api.depends('event_attendance_ids')
    def _leads_acquired(self):
        for a in self:
            a.leads_acquired =  len(a.event_attendance_ids)

    name = fields.Char(string='Campaign Name')
    campaign_scheduled = fields.Datetime(string="Campaign Schedule")
    campaign_duration = fields.Integer(string="Campaign Duration")
    industry = fields.Many2one("pop.type",string='Industry')
    location = fields.Many2one("pop.regional",string="Location")
    regional = fields.Many2one("pop.regional",string='Regional')
    expected_leads = fields.Integer(string='Expected Leads')
    leads_acquired = fields.Integer(string='Leads Acquired', compute="_leads_acquired")

    expected_invitation = fields.Many2one('res.partner',string='Expected Invitation')
    expected_confirmation = fields.Many2one('res.partner',string='Expected Confirmation')
    expected_attendant = fields.Many2one('res.partner',string='Expected Attendant')
    actual_invitation_sent = fields.Many2one('res.partner',string='Actual Invitation Sent')
    actual_confirmation = fields.Many2one('res.partner',string='Actual Confirmation')
    actual_attendance = fields.Many2one('res.partner',string='Actual Attendance')
    invitation_expected = fields.Many2one('res.partner',string='Invitation Expected/Actual Ratio')
    confirmation_expected = fields.Many2one('res.partner',string='Confirmation Expected/Actual Ratio')
    attendance_expected = fields.Many2one('res.partner',string='Attendance Expected/Actual Ratio')
    budget = fields.Many2one('res.partner',string='Budget/Actual Cost Ratio')

    campaign_cost_ids = fields.One2many("velomania.campaign.cost","campaign_cost_id",string='Campaign Cost')
    # event_summary_ids = fields.One2many("velomania.event.summary","event_summary_ids",string='Event Summary')
    event_attendance_ids = fields.One2many("velomania.event.attendance","event_attendance_id",string='Event Attendance')
    forecast_ids = fields.One2many("velomania.budget.forecast","forecast_id",string='Budget Forecast')

class velo_campaign_cost(models.Model):
    _name = 'velomania.campaign.cost'
    _description = 'Model Menu Campaign Cost'
    _rec_name = 'cost_name'

    campaign_cost_id = fields.Many2one("velomania",string='Campaign Cost')
    cost_name = fields.Float(string='Cost Name')
    cost = fields.Float(string="COST")
    qty = fields.Integer(string="Quantity")
    desc = fields.Char(string="Desc")
    total_costs = fields.Float(string="Total Costs")
 

class velo_velomania_event_attendance(models.Model):
    _name = 'velomania.event.attendance'
    _description = 'Model Menu Event Attendance'
    _rec_name = 'company'

    event_attendance_id = fields.Many2one("velomania",string='Event Attendance')
    contact_name = fields.Many2one('res.partner',string='Contact Name', domain="[('contact', '=', 1)]" )
    company = fields.Many2one('res.partner',string='Company Name')
    budget = fields.Float(string="Budget")
    work_function = fields.Char(string="Work Function")
    work_level = fields.Char(string="Work Level")
    remarks = fields.Char(string='Remarks')

class velo_budget_forecast(models.Model):
    _name = 'velomania.budget.forecast'
    _description = 'Model Menu Budget Forecast'
    _rec_name = 'cost_name'

    forecast_id = fields.Many2one("velomania",string='Budget Forecast')
    cost_name = fields.Float(string='Cost Name')
    cost = fields.Float(string="COST")
    qty = fields.Integer(string="Quantity")
    desc = fields.Char(string="Desc")
    total_costs = fields.Float(string="Total Costs")

