# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class velo_promo(models.Model):
    _name = 'velo.promo'
    _description = 'Promotion'
    _rec_name =  'name'

    promo_type = fields.Many2one('velo.promo.type', string="Promo Type")
    name = fields.Many2one('velo.program', string="Program Name")
    promo_id = fields.Char(string="Promo ID")
    start_period = fields.Date(string="Promo Schedule")
    finish_period = fields.Date(string="Promo Done", store=True, compute='_get_end_date', inverse='_set_end_date')
    duration = fields.Float(string="Promo Duration", digits=(6, 2), help="Durasi Hari")
    # pop_id = fields.Char(related="pop_name.pop_id", string="POP ID")
    pop_name = fields.Many2one('pop.service.coverage', string='POP/Industry Cluster')
    leads_generated = fields.Integer(string="Leads Generated")
    tarif_acquired = fields.Integer(string="Tariff Acquired (OB)")
    # attendees_count = fields.Integer(string="Jumlah Peserta", compute='_get_attendees_count', store=True)
    total_attendance = fields.Integer(string="Total Attendance", compute='_get_attendees_count', store=True)
    market_potential_ids = fields.One2many('velo.market.potential','market_potential_id', string='Market Potential')
    leads_acquired_ids = fields.One2many('velo.leads.acquired','leads_acquired_id', string='Leads Acquired')
    promo_costs_ids = fields.One2many('velo.promo.costs','promo_costs_id', string='Promo Costs')

    # location = fields.Many2one('velo.location', string='Location')
    # tipe = fields.Many2one('pop.type', string='Type')
    # content = fields.Html('Promotion Content')
    # roadshow_number = fields.Char('Roadshow Number')
    # propsal_date = fields.Date(string="Propsal Date")
    # prepared_by = fields.Many2one('res.users',string="Prepared by")
    state = fields.Selection([('active','Active')], string="State", default='active')
    
    # pop_fo = fields.Char('POP FO')
    # total_customers = fields.Integer('Total Customers')
    # competitor = fields.Char('Competitor')
    # provider = fields.Char('Provider')
    # biznet = fields.Char('Biznet')
    # cbn = fields.Char('CBN')
    # backhaul = fields.Char('Backhaul')
    # potentials = fields.Integer('Potentials')
    # am = fields.Char('A/M')
    # penetration = fields.Char('Penetration')
    # opex = fields.Integer('OPEX')
    # utization = fields.Integer('Utization')
    # total_revenue = fields.Integer('Total Revenue')

    @api.depends('market_potential_ids')
    def _get_attendees_count(self):
        for r in self:
            # Mengupdate field attendees_count berdasarkan jumlah record di tabel peserta 
            r.total_attendance = len(r.market_potential_ids)


    @api.depends('start_period', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_period and r.duration): 
                r.finish_period = r.start_period
                continue

            start = fields.Datetime.from_string(r.start_period)
            duration = timedelta(days=r.duration, seconds=-1)
            r.finish_period = start + duration
    
    def _set_end_date(self):
        for r in self:
            if not (r.start_period and r.finish_period):
                continue
    
            start_date = fields.Datetime.from_string(r.start_period)
            end_date = fields.Datetime.from_string(r.finish_period)
            r.duration = (end_date - start_date).days + 1
    

class VeloMarketPotential(models.Model):
    _name = 'velo.market.potential'
    _description = 'Velo Market Potential'

    potential_name = fields.Many2one('res.partner', string="Potential Name")
    existing_provider = fields.Char(string="Existing Provider")
    contract_expiry = fields.Date(string="Contract Expiry")
    tarif_acquired = fields.Integer(string="Tariff Acquired (OB)")
    sales_pipeline = fields.Char(string="Sales Pipeline")
    Attendance = state = fields.Selection([
        ('y', 'Y'),
        ('n','N'),
        ], string='Attendance', default='y')
    request_followup = fields.Boolean(string="Request Follow Up")
    cold_leads = fields.Boolean(string="Cold Leads")
    market_potential_id = fields.Many2one('velo.promo', string='Market Potential')


    @api.onchange('potential_name')
    def _potential_name(self):
        if self.potential_name:
            self.existing_provider = self.potential_name.tenant_existing_provider

class VeloLeadsAcquired(models.Model):
    _name = 'velo.leads.acquired'
    _description = 'Velo Leads Acquired'

    company_name = fields.Many2one('res.partner', string="Company Name")
    pop = fields.Many2one('pop.service.coverage', string="POP")
    tarif_acquired = fields.Integer(string="Tariff Acquired (OB)")
    existing = fields.Char(string="Existing")
    sales_pipeline = fields.Char(string="Sales Pipeline")
    remarks = fields.Char(string="Remarks")
    leads_acquired_id = fields.Many2one('velo.promo', string='Leads Acquired')

class VeloPromoCosts(models.Model):
    _name = 'velo.promo.costs'
    _description = 'Velo Promo Costs'

    cost_name = fields.Char(string="Cost Name")
    cost = fields.Integer(string="COST")
    quantity = fields.Integer(string="Quantity")
    desc = fields.Char(string="Desc")
    total_costs = fields.Integer(string="Total Costs", compute='_total_costs_promo')
    promo_costs_id = fields.Many2one('velo.promo', string="Promo Costs")

    @api.depends('total_costs')
    def _total_costs_promo(self):
        self.total_costs = self.cost * self.quantity


class Pop(models.Model):
    _name = 'velo.pop'
    _description = 'POP'
    _rec_name =  'name'

    name = fields.Char('Name')

class velo_location(models.Model):
    _name = 'velo.location'
    _description = 'Location'
    _rec_name =  'name'

    name = fields.Char('Name')

class velo_tip(models.Model):
    _name = 'velo.tipe'
    _description = 'Tipe'
    _rec_name =  'name'

    name = fields.Char('Name')

class promo_type(models.Model):
    _name = 'velo.promo.type'
    _description = "Promo Type"

    name = fields.Char("Name")


class velo_relation(models.Model):
    _name = 'velo.relation'
    _description = 'Relation'
    _rec_name =  'name'

    relation_promo_type = fields.Many2one('velo.promo.type', string="Promo Type")
    relation_promo_code = fields.Char(string="Promo Code")
    name = fields.Many2one('velo.program', string="Program Name")
    relation_promo_id = fields.Char(string="Promo ID")
    start_period = fields.Date(string="Promo Schedule", default=fields.Date.today)
    finish_period = fields.Date(string="Promo Done", store=True, compute='_get_end_date', inverse='_set_end_date', default=fields.Date.today)
    duration = fields.Float(string="Promo Duration", digits=(6, 2), help="Durasi Hari")
    relation_pop_name = fields.Many2one('pop.service.coverage', string='POP/Industry Cluster')
    relation_leads_generated = fields.Integer(string="Leads Generated")
    relation_tarif_acquired = fields.Integer(string="Tariff Acquired (OB)")
    relation_total_attendance = fields.Integer(string="Total Attendance")
    relation_market_potential_ids = fields.One2many('velo.market.potential.relation','relation_market_potential_id', string='Market Potential')
    relation_leads_acquired_ids = fields.One2many('velo.leads.acquired.relation','relation_leads_acquired_id', string='Leads Acquired')
    relation_promo_costs_ids = fields.One2many('velo.promo.costs.relation','relation_promo_costs_id', string='Promo Costs')
    state = fields.Selection([('active','Active')], string="State", default='active')

    @api.depends('start_period', 'duration')
    def _get_end_date(self):
        for r in self:
            # Pengecekan jika field duration tidak diisi, maka field end_date akan di update sama seperti field start_date
            if not (r.start_period and r.duration): 
                r.finish_period = r.start_period
                continue

            start = fields.Datetime.from_string(r.start_period)
            duration = timedelta(days=r.duration, seconds=-1)
            r.finish_period = start + duration
    
    def _set_end_date(self):
        for r in self:
            if not (r.start_period and r.finish_period):
                continue
    
            start_date = fields.Datetime.from_string(r.start_period)
            end_date = fields.Datetime.from_string(r.finish_period)
            r.duration = (end_date - start_date).days + 1

class VeloMarketPotentialRelation(models.Model):
    _name = 'velo.market.potential.relation'
    _description = 'Velo Market Potential Relation'

    relation_potential_name = fields.Many2one('res.partner', string="Potential Name")
    relation_existing_provider = fields.Char(string="Existing Provider")
    relation_contract_expiry = fields.Date(string="Contract Expiry")
    relation_tarif_acquired = fields.Integer(string="Tariff Acquired (OB)")
    relation_sales_pipeline = fields.Char(string="Sales Pipeline")
    relation_Attendance = fields.Char(string="Attendance")
    relation_request_followup = fields.Boolean(string="Request Follow Up")
    relation_cold_leads = fields.Boolean(string="Cold Leads")
    relation_market_potential_id = fields.Many2one('velo.relation', string='Market Potential')

    @api.onchange('relation_potential_name')
    def _potential_name(self):
        if self.relation_potential_name:
            self.relation_existing_provider = self.relation_potential_name.tenant_existing_provider

class VeloLeadsAcquiredRelation(models.Model):
    _name = 'velo.leads.acquired.relation'
    _description = 'Velo Leads Acquired Relation'

    relation_company_name = fields.Many2one('res.partner', string="Company Name")
    relation_pop = fields.Many2one('pop.service.coverage', string="POP")
    relation_tarif_acquired = fields.Integer(string="Tariff Acquired (OB)")
    relation_existing = fields.Char(string="Existing")
    relation_sales_pipeline = fields.Char(string="Sales Pipeline")
    relation_remarks = fields.Char(string="Remarks")
    relation_leads_acquired_id = fields.Many2one('velo.relation', string='Leads Acquired')

class VeloPromoCosts(models.Model):
    _name = 'velo.promo.costs.relation'
    _description = 'Velo Promo Costs'

    relation_cost_name = fields.Char(string="Cost Name")
    relation_cost = fields.Integer(string="COST")
    relation_quantity = fields.Integer(string="Quantity")
    relation_desc = fields.Char(string="Desc")
    relation_total_costs = fields.Integer(string="Total Costs", compute="_total_costs_relation")
    relation_promo_costs_id = fields.Many2one('velo.relation', string="Promo Costs")

    @api.depends('relation_total_costs')
    def _total_costs_relation(self):
        self.relation_total_costs = self.relation_cost * self.relation_quantity 




