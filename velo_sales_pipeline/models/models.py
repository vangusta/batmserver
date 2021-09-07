# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class lead(models.Model):
    _inherit = 'crm.lead'

    stage_id_name = fields.Char(related="stage_id.name", string="stage name")
    stage_id_id = fields.Many2one(related="stage_id", string="stage name")

    relationship_crm= fields.Boolean(string="Relationship")
    budget_crm= fields.Boolean(string="Budget")
    price_crm= fields.Boolean(string="Price")
    service_delivery_crm = fields.Boolean(string="Service Delivery")
    
    space = fields.Char(' ', readonly=True)
    opportunity_stage = fields.Char('Opportunity Stage')
    opportunity_stage1 = fields.Integer(string="Opportunity Progress", compute="_compute_opportunity_stage", store=True) # 

    opportunity_stage_budget = fields.Boolean(string="Budget", default=True)
    opportunity_stage_solution_fit = fields.Boolean(string="Solution Fit")
    opportunity_stage_service_delivery = fields.Boolean(string="Service Delivery")
    opportunity_stage_pricing = fields.Boolean(string="Pricing")
    opportunity_stage_relationship = fields.Boolean(string="Relationship")
    closing_days = fields.Integer('Days to Closing', default=90)
    expected_closing_countdown = fields.Integer('Expected Closing', compute='_compute_duration', inverse='_inverse_duration', store=True)



    @api.onchange('expected_closing_countdown')
    def _onchange_duration(self):
        self._inverse_duration()

    @api.depends('date_deadline')
    def _compute_duration(self):
        now = datetime.now()
        date_now = now.date()
        for rec in self:
            rec.expected_closing_countdown = rec._get_duration(date_now, rec.date_deadline)

    def _inverse_duration(self):
        for rec in self:
            if fields.Date.today() and rec.expected_closing_countdown:
                rec.date_deadline = fields.Date.today() + relativedelta(days=rec.expected_closing_countdown)

    def _get_duration(self, date_now, date_deadline):
        now = datetime.now()
        date_now = now.date()
        if not date_now or not date_deadline:
            return 0
        dt = date_deadline - date_now
        return dt.days

    @api.depends('date_deadline')
    def process_countdown_deadline(self):
        for rec in self.search([('state', '!=', 'Expired')]):
            if rec.mcu_expiry and rec.mcu_expiry <= fields.Date.today():
                rec.write({'state': 'Expired'})

    @api.onchange('partner_id', 'opportunity_stage_budget', 'opportunity_stage_solution_fit', 'opportunity_stage_service_delivery', 'opportunity_stage_pricing', 'opportunity_stage_relationship')
    def onchange_potential_opportunity(self):
        for rec in self:
            if rec.partner_id:
                rec.partner_id.opportunity_stage_budget = rec.opportunity_stage_budget
                rec.partner_id.opportunity_stage_solution_fit = rec.opportunity_stage_solution_fit
                rec.partner_id.opportunity_stage_service_delivery = rec.opportunity_stage_service_delivery
                rec.partner_id.opportunity_stage_pricing = rec.opportunity_stage_pricing
                rec.partner_id.opportunity_stage_relationship = rec.opportunity_stage_relationship

    def action_confirm_mcfb_to_mcfc(self):
        for rec in self:
            rec.stage_id = 6
            rec.opportunity_stage_solution_fit = True
            rec.partner_id.opportunity_stage_solution_fit = True
            rec.closing_days = 60

    def action_confirm_mcfc_to_sf(self):
        for rec in self:
            rec.stage_id = 7
            rec.closing_days = 30

    def action_back_sf_to_mcfb(self):
        for rec in self:
            rec.stage_id = 5
            rec.opportunity_stage_solution_fit = False
            rec.partner_id.opportunity_stage_solution_fit = False
            rec.closing_days = 90


    @api.depends('opportunity_stage_budget', 'opportunity_stage_service_delivery', 'opportunity_stage_solution_fit','opportunity_stage_pricing','opportunity_stage_relationship')
    def _compute_opportunity_stage(self):
        budget = 20
        service_delivery = 20
        solution_fit = 20
        pricing = 20
        relationship = 20
        for rec in self:
            if rec.opportunity_stage_budget == True:
                rec.opportunity_stage1= budget
            if rec.opportunity_stage_service_delivery == True:
                rec.opportunity_stage1= service_delivery
            if rec.opportunity_stage_solution_fit == True:
                rec.opportunity_stage1= solution_fit
            if rec.opportunity_stage_pricing == True:
                rec.opportunity_stage1= pricing
            if rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1= relationship

            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True:
                  rec.opportunity_stage1= budget + service_delivery
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_solution_fit == True:
                  rec.opportunity_stage1= budget + solution_fit
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_pricing == True:
                  rec.opportunity_stage1= budget + pricing
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_relationship == True:
                  rec.opportunity_stage1= budget + relationship
          
            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True:
                  rec.opportunity_stage1= service_delivery + solution_fit
            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_pricing == True:
                  rec.opportunity_stage1= service_delivery + pricing
            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_relationship == True:
                  rec.opportunity_stage1= service_delivery + relationship
            if rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True:
                 rec.opportunity_stage1= solution_fit + pricing
            if rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_relationship == True:
                 rec.opportunity_stage1= solution_fit + relationship
            if rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                  rec.opportunity_stage1= pricing + relationship
            
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True:
                rec.opportunity_stage1= budget + service_delivery + solution_fit
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_pricing == True:
                rec.opportunity_stage1= budget + service_delivery + pricing
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1= budget + service_delivery + relationship
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True:
                rec.opportunity_stage1= budget + solution_fit + pricing
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1= budget + solution_fit + relationship
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1= budget + pricing + relationship

            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True:
                rec.opportunity_stage1= service_delivery + solution_fit + pricing
            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1= service_delivery + solution_fit + relationship
            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1= service_delivery + pricing + relationship
            if rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1= solution_fit + pricing + relationship
            
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True:
                rec.opportunity_stage1= budget + service_delivery + solution_fit + pricing
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1= budget + service_delivery + solution_fit + relationship
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1= budget + service_delivery + pricing + relationship
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1= budget + solution_fit + pricing + relationship
            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1= service_delivery + solution_fit + pricing + relationship
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1= budget + service_delivery + solution_fit + pricing + relationship
            if rec.opportunity_stage_budget == False and rec.opportunity_stage_service_delivery == False and rec.opportunity_stage_solution_fit == False and rec.opportunity_stage_pricing == False and rec.opportunity_stage_relationship == False:
                rec.opportunity_stage1= 0