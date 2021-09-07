# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class Program_pro(models.Model):
    _name = 'velo.program'
    _description = 'Program and Promotion'
    _rec_name =  'name'

    @api.depends('program_cost_ids')
    def _sum_total_costs(self):
        for a in self:
            a.sum_total_costs = sum(line.total_costs for line in a.program_cost_ids)

    name = fields.Char('Name')
    contract_period = fields.Integer('Contract Period')
    monthly_discount_duration = fields.Integer('Monthly Fee -  Discount%')
    discount_monthly_tariff = fields.Float('Monthly Fee - Discount Period (Month)')
    one_time_charge_discount = fields.Float('Onetime Fee - Discount Free')
    # customer_incentive = fields.Char('Customer Incentive')

    penetration = fields.Integer('Penetration')
    annual_tarif_increase = fields.Integer('Annual Tarif Increase')
    annual_customer_increase = fields.Integer('Annual Customer Increase')
    annual_marketing_budget = fields.Integer('Annual Marketing Budget')

    program_id = fields.Char('Program ID')
    # program_category = fields.Many2one('velo.program.category', string='Program Category')
    start_period = fields.Date(string="Validity Start")
    finish_period = fields.Date(string="Validity End")
    special_arrangement = fields.Integer('Special Arrangement')
    # program_type = fields.Many2one('velo.program.promo_type',string="Program Type")
    after = fields.Integer('After')
    desc = fields.Html('Gimmick')
    gimmick_desc = fields.Html('Gimmick Description')
    cost = fields.Float('Cost')
    state = fields.Selection([('active','Active')], string="State", default='active')
    # promo_ids = fields.One2many('velo.product.promo','promo_id',string="Promo Type")
    program_cost_ids = fields.One2many('velo.program.cost','program_cost_id',string="Program Cost")
    avaibility_ids = fields.One2many('pop.service.coverage','pop_program',string="Avaibility")
    sum_total_costs = fields.Float('Total', compute="_sum_total_costs")

class Program_cost(models.Model):
    _name = 'velo.program.cost'
    _description = 'Program Cost'
    _rec_name =  'name'

    program_cost_id = fields.Many2one('velo.program',string='Program Cost')
    name = fields.Char('Cost Name')
    cost = fields.Float('Cost')
    qty = fields.Integer('Quantity')
    desc = fields.Char('Description')
    total_costs = fields.Float('Total Cost')

class Program_avaibility(models.Model):
    _name = 'velo.avaibility'
    _description = 'Program Avaibility'
    _rec_name =  'name'

    avaibility_id = fields.Many2one('velo.program',string='Avaibility')
    name = fields.Many2one('pop.service.coverage','Name')

class Program_category(models.Model):
    _name = 'velo.program.category'
    _description = 'Program Category'
    _rec_name =  'name'

    name = fields.Char('Name')

class Program_type(models.Model):
    _name = 'velo.program.promo_type'
    _description = 'Promo Type'
    _rec_name =  'name'

    name = fields.Char('Name')

# class Program_product_promo(models.Model):
#     _name = 'velo.product.promo'
#     _description = 'Product Promo'

#     promo_id = fields.Many2one('velo.program',string='Product Promo')
#     old_product = fields.Many2one('product.product',string='Old Product')
#     new_product = fields.Many2one('product.product',string='New Product')


class overview_program_promotion(models.Model):
    _name = 'overview.program.promotion'
    _description = 'Overview Program Promotion'
    _rec_name = 'overview_program_promotion'

    @api.model
    def _ob(self):
        mcfb_sales = self.env['crm.lead'].search([('stage_id.name','ilike', 'MCF-B')])
        ob_sales = self.env['crm.lead'].search([('stage_id.name','ilike', 'Order Booking')])
        # sf_sales = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus')])
        # mcfc_sales = self.env['crm.lead'].search([('stage_id.name','ilike', 'MCF-C')])
       
        # average_sales = self.env['crm.lead'].search([])
        for i in self:
            i.mcfb = len(mcfb_sales)
            i.ob = len(ob_sales)
            # i.sf = len(sf_sales)
            # i.mcfc = len(mcfc_sales)
            
            # i.average_selling = int(len(average_sales))/4

    overview_program_promotion = fields.Char('Overview')
    
    bevelo_id = fields.Many2one('velo.program','BeVelo ID')
    bevelo = fields.Char(related="bevelo_id.name", string="BeVelo")
    bevelo_prog_categ = fields.Many2one('velo.program.category', string="Program Category")
    bevelo_prog_type = fields.Many2one('velo.program.promo_type', string="Program Type")
    bevelo_available_prog = fields.Integer('Available Program')
    bevelo_penetration = fields.Integer(related="bevelo_id.penetration", string='Penetration')
    bevelo_annual_tarif_increase = fields.Integer(related="bevelo_id.annual_tarif_increase", string='Annual Tarif Increase')
    bevelo_annual_customer_increase = fields.Integer(related="bevelo_id.annual_customer_increase", string='Annual Customer Increase')
    bevelo_annual_marketing_budget = fields.Integer(related="bevelo_id.annual_marketing_budget", string='Annual Marketing Budget')
    bevelo_contract_period = fields.Integer(related="bevelo_id.contract_period", string='Contract Period')
    bevelo_monthly_fee_discount = fields.Integer(related="bevelo_id.monthly_discount_duration", string='Monthly Fee -  Discount%')
    bevelo_monthly_fee_discount_period = fields.Float(related="bevelo_id.discount_monthly_tariff", string='Monthly Fee - Discount Period (Month)')
    bevelo_onetime_fee = fields.Float(related="bevelo_id.one_time_charge_discount", string='Onetime Fee - Discount Free')
    bevelo_gimmick = fields.Html(related="bevelo_id.desc", string="Gimmick")
    bevelo_special_arrangement = fields.Integer(related="bevelo_id.special_arrangement", string="Special Arrangement")
    bevelo_validity_start = fields.Date(related="bevelo_id.start_period", string="Validity Start")
    bevelo_validity_end = fields.Date(related="bevelo_id.finish_period", string="Validity End")

    lovevelo_id = fields.Many2one('velo.program','LoveVelo ID')
    lovevelo = fields.Char(related="lovevelo_id.name", string="LoveVelo")
    lovevelo_prog_categ = fields.Many2one('velo.program.category', string="Program Category")
    lovevelo_prog_type = fields.Many2one('velo.program.promo_type', string="Program Type")
    lovevelo_available_prog = fields.Integer('Available Program')
    lovevelo_penetration = fields.Integer(related="lovevelo_id.penetration", string='Penetration')
    lovevelo_annual_tarif_increase = fields.Integer(related="lovevelo_id.annual_tarif_increase", string='Annual Tarif Increase')
    lovevelo_annual_customer_increase = fields.Integer(related="lovevelo_id.annual_customer_increase", string='Annual Customer Increase')
    lovevelo_annual_marketing_budget = fields.Integer(related="lovevelo_id.annual_marketing_budget", string='Annual Marketing Budget')
    lovevelo_contract_period = fields.Integer(related="lovevelo_id.contract_period", string='Contract Period')
    lovevelo_monthly_fee_discount = fields.Integer(related="lovevelo_id.monthly_discount_duration", string='Monthly Fee - Discount%')
    lovevelo_monthly_fee_discount_period = fields.Float(related="lovevelo_id.discount_monthly_tariff", string='Monthly Fee - Discount Period (Month)')
    lovevelo_onetime_fee = fields.Float(related="lovevelo_id.one_time_charge_discount", string='Onetime Fee - Discount Free')
    lovevelo_gimmick = fields.Html(related="lovevelo_id.desc", string="Gimmick")
    lovevelo_special_arrangement = fields.Integer(related="lovevelo_id.special_arrangement", string="Special Arrangement")
    lovevelo_validity_start = fields.Date(related="lovevelo_id.start_period", string="Validity Start")
    lovevelo_validity_end = fields.Date(related="lovevelo_id.finish_period", string="Validity End")
    lovevelo_cold_leads = fields.Integer('Cold Leads')
    lovevelo_ob = fields.Integer('OB')

    velome_id = fields.Many2one('velo.program','velome ID')
    velome = fields.Char(related="velome_id.name", string="VeloMe")
    velome_prog_categ = fields.Many2one('velo.program.category', string="Program Category")
    velome_prog_type = fields.Many2one('velo.program.promo_type', string="Program Type")
    velome_available_prog = fields.Integer('Available Program')
    velome_penetration = fields.Integer(related="velome_id.penetration", string='Penetration')
    velome_annual_tarif_increase = fields.Integer(related="velome_id.annual_tarif_increase", string='Annual Tarif Increase')
    velome_annual_customer_increase = fields.Integer(related="velome_id.annual_customer_increase", string='Annual Customer Increase')
    velome_annual_marketing_budget = fields.Integer(related="velome_id.annual_marketing_budget", string='Annual Marketing Budget')
    velome_contract_period = fields.Integer(related="velome_id.contract_period", string='Contract Period')
    velome_monthly_fee_discount = fields.Integer(related="velome_id.monthly_discount_duration", string='Monthly Fee -  Discount%')
    velome_monthly_fee_discount_period = fields.Float(related="velome_id.discount_monthly_tariff", string='Monthly Fee -  Discount Period (Month)')
    velome_onetime_fee = fields.Float(related="velome_id.one_time_charge_discount", string='Onetime Fee')
    velome_gimmick = fields.Html(related="velome_id.desc", string="Gimmick")
    velome_special_arrangement = fields.Integer(related="velome_id.special_arrangement", string="Special Arrangement")
    velome_validity_start = fields.Date(related="velome_id.start_period", string="Validity Start")
    velome_validity_end = fields.Date(related="velome_id.finish_period", string="Validity End")
    velome_cold_leads = fields.Integer('Cold Leads')
    velome_ob = fields.Integer('OB')

    velox_id = fields.Many2one('velo.program','velox ID')
    velox = fields.Char(related="velox_id.name", string="VeloX")
    velox_prog_categ = fields.Many2one('velo.program.category', string="Program Category")
    velox_prog_type = fields.Many2one('velo.program.promo_type', string="Program Type")
    velox_available_prog = fields.Integer('Available Program')
    velox_penetration = fields.Integer(related="velox_id.penetration", string='Penetration')
    velox_annual_tarif_increase = fields.Integer(related="velox_id.annual_tarif_increase", string='Annual Tarif Increase')
    velox_annual_customer_increase = fields.Integer(related="velox_id.annual_customer_increase", string='Annual Customer Increase')
    velox_annual_marketing_budget = fields.Integer(related="velox_id.annual_marketing_budget", string='Annual Marketing Budget')
    velox_contract_period = fields.Integer(related="velox_id.contract_period", string='Contract Period')
    velox_monthly_fee_discount = fields.Integer(related="velox_id.monthly_discount_duration", string='Monthly Fee - Disconut%')
    velox_monthly_fee_discount_period = fields.Float(related="velox_id.discount_monthly_tariff", string='Monthly Fee - Discount Period (Month)')
    velox_onetime_fee = fields.Float(related="velox_id.one_time_charge_discount", string='Onetime Fee')
    velox_gimmick = fields.Html(related="velox_id.desc", string="Gimmick")
    velox_special_arrangement = fields.Integer(related="velox_id.special_arrangement", string="Special Arrangement")
    velox_validity_start = fields.Date(related="velox_id.start_period", string="Validity Start")
    velox_validity_end = fields.Date(related="velox_id.finish_period", string="Validity End")
    velox_cold_leads = fields.Integer('Cold Leads')
    velox_ob = fields.Integer('OB')

    newnormal_id = fields.Many2one('velo.program','newnormal ID')
    newnormal = fields.Char(related="newnormal_id.name", string="NewNormal")
    newnormal_prog_categ = fields.Many2one('velo.program.category', string="Program Category")
    newnormal_prog_type = fields.Many2one(r'velo.program.promo_type', string="Program Type") 
    newnormal_available_prog = fields.Integer('Available Program')
    newnormal_penetration = fields.Integer(related="newnormal_id.penetration", string='Penetration')
    newnormal_annual_tarif_increase = fields.Integer(related="newnormal_id.annual_tarif_increase", string='Annual Tarif Increase')
    newnormal_annual_customer_increase = fields.Integer(related="newnormal_id.annual_customer_increase", string='Annual Customer Increase')
    newnormal_annual_marketing_budget = fields.Integer(related="newnormal_id.annual_marketing_budget", string='Annual Marketing Budget')
    newnormal_contract_period = fields.Integer(related="newnormal_id.contract_period", string='Contract Period')
    newnormal_monthly_fee_discount = fields.Integer(related="newnormal_id.monthly_discount_duration", string='Monthly Fee - Discount%')
    newnormal_monthly_fee_discount_period = fields.Float(related="newnormal_id.discount_monthly_tariff", string='Monthly Fee - Discount Period (Month)')
    newnormal_onetime_fee = fields.Float(related="newnormal_id.one_time_charge_discount", string='Onetime Fee')
    newnormal_gimmick = fields.Html(related="newnormal_id.desc", string="Gimmick")
    newnormal_special_arrangement = fields.Integer(related="newnormal_id.special_arrangement", string="Special Arrangement")
    newnormal_validity_start = fields.Date(related="newnormal_id.start_period", string="Validity Start")
    newnormal_validity_end = fields.Date(related="newnormal_id.finish_period", string="Validity End")
    newnormal_cold_leads = fields.Integer('Cold Leads')
    newnormal_ob = fields.Integer('OB')

    ob = fields.Integer('Tariff Generated (ob)', compute="_ob")
    # sf = fields.Integer('Sales Focus(Hot Leads)', compute="_ob")
    # mcfc = fields.Integer('MCF-C(Warm leads)', compute="_ob")
    mcfb = fields.Integer('Cold Leads Generated', compute="_ob")
    # average_selling = fields.Integer('Average Selling Cycle', compute="_ob")

class Program_retention(models.Model):
    _name = 'velo.retention'
    _description = 'Program and Retention'
    _rec_name =  'name'

    name = fields.Char("Name")
    program_retention_id = fields.Char("Program ID")
    contract_renewal_rate = fields.Integer("Contract Renewal Rate")
    mtl_churn = fields.Integer("Monthly Tarif Loss From Churn")
    mtl_downgrade = fields.Integer("Monthly Tarif Loss From Downgrade")
    decrease = fields.Integer("Decrease % - Monthly Tariff from New Tarif")
    increase = fields.Integer("Incre(Decre) % - B/W Capacity")
    desc = fields.Html('Gimmick')
    gimmick_desc = fields.Html('Gimmick Description')
    start_period = fields.Char(string="Validity Start")
    finish_period = fields.Char(string="Validity End")

    mothly_tariff_adj = fields.Integer("Monthly Tariff Adjutsment (Downgrade)")
    monthly_customer_loss = fields.Integer("Monthly Customer Loss (Churn)")
    montly_customer_renewal_rate = fields.Integer("Monthly Cusotomer Renewal Rate")
    montly_contract_loss = fields.Integer("Monthly Contract Loss")
    state = fields.Selection([('active','Active')], string="State", default='active')

class program_name(models.Model):
    _name = 'velo.program.name'
    _description = "Promo Name"

    name = fields.Char("Name")

class overview_program_retention(models.Model):
    _name = 'overview.program.retention'
    _description = 'Overview Program Retention'
    _rec_name = 'overview_program_retention'

    overview_program_retention = fields.Char('Overview')

    blue_id = fields.Many2one('velo.retention','Blue ID')
    blue = fields.Char(related="blue_id.name", string="Blue (Mind)")
    blue_contract_renewal_rate = fields.Integer(related="blue_id.contract_renewal_rate", string="Contract Renewal Rate")
    blue_mtl_churn = fields.Integer(related="blue_id.mtl_churn", string="Monthly Tarif Loss From Churn")
    blue_mtl_downgrade = fields.Integer(related="blue_id.mtl_downgrade", string="Monthly Tarif Loss From Downgrade")
    blue_prog_name = fields.Many2one('velo.program.name', string="Program Name")
    blue_prog_type = fields.Many2one('velo.program.promo_type', string="Program Type")
    blue_decrease = fields.Integer(related="blue_id.decrease", string="Decrease % - Monthly Tariff from New Tarif")
    blue_increase = fields.Integer(related="blue_id.increase", string="Incre(Decre) % - B/W Capacity")
    blue_gimmick = fields.Html(related="blue_id.desc", string="Gimmick")
    blue_validity_start = fields.Char(related="blue_id.start_period", string="Validity Start")
    blue_validity_end = fields.Char(related="blue_id.finish_period", string="Validity End")
    blue_mothly_tariff_adj = fields.Integer(related="blue_id.mothly_tariff_adj", sting="Monthly Tariff Adjutsment (Downgrade)")
    blue_monthly_customer_loss = fields.Integer(related="blue_id.monthly_customer_loss", sting="Monthly Customer Loss (Churn)")
    blue_montly_customer_renewal_rate = fields.Integer(related="blue_id.montly_customer_renewal_rate", sting="Monthly Customer Renewal Rate")
    blue_montly_contract_loss = fields.Integer(related="blue_id.montly_contract_loss", sting="Monthly Contract Loss")

    green_id = fields.Many2one('velo.retention','Green ID')
    green = fields.Char(related="green_id.name", string="green (Soul)")
    green_contract_renewal_rate = fields.Integer(related="green_id.contract_renewal_rate", string="Contract Renewal Rate")
    green_mtl_churn = fields.Integer(related="green_id.mtl_churn", string="Monthly Tarif Loss From Churn")
    green_mtl_downgrade = fields.Integer(related="green_id.mtl_downgrade", string="Monthly Tarif Loss From Downgrade")
    green_prog_name = fields.Many2one('velo.program.name', string="Program Name")
    green_prog_type = fields.Many2one('velo.program.promo_type', string="Program Type")
    green_decrease = fields.Integer(related="green_id.decrease", string="Decrease % - Monthly Tariff from New Tarif")
    green_increase = fields.Integer(related="green_id.increase", string="Incre(Decre) % - B/W Capacity")
    green_gimmick = fields.Html(related="green_id.desc", string="Gimmick")
    green_validity_start = fields.Char(related="green_id.start_period", string="Validity Start")
    green_validity_end = fields.Char(related="green_id.finish_period", string="Validity End")
    green_mothly_tariff_adj = fields.Integer(related="green_id.mothly_tariff_adj", sting="Monthly Tariff Adjutsment (Downgrade)")
    green_monthly_customer_loss = fields.Integer(related="green_id.monthly_customer_loss", sting="Monthly Customer Loss (Churn)")
    green_montly_customer_renewal_rate = fields.Integer(related="green_id.montly_customer_renewal_rate", sting="Monthly Customer Renewal Rate")
    green_montly_contract_loss = fields.Integer(related="green_id.montly_contract_loss", sting="Monthly Contract Loss")

    yellow_id = fields.Many2one('velo.retention','Yellow ID')
    yellow = fields.Char(related="yellow_id.name", string="yellow (Reality)")
    yellow_contract_renewal_rate = fields.Integer(related="yellow_id.contract_renewal_rate", string="Contract Renewal Rate")
    yellow_mtl_churn = fields.Integer(related="yellow_id.mtl_churn", string="Monthly Tarif Loss From Churn")
    yellow_mtl_downgrade = fields.Integer(related="yellow_id.mtl_downgrade", string="Monthly Tarif Loss From Downgrade")
    yellow_prog_name = fields.Many2one('velo.program.name', string="Program Name")
    yellow_prog_type = fields.Many2one('velo.program.promo_type', string="Program Type")
    yellow_decrease = fields.Integer(related="yellow_id.decrease", string="Decrease % - Monthly Tariff from New Tarif")
    yellow_increase = fields.Integer(related="yellow_id.increase", string="Incre(Decre) % - B/W Capacity")
    yellow_gimmick = fields.Html(related="yellow_id.desc", string="Gimmick")
    yellow_validity_start = fields.Char(related="yellow_id.start_period", string="Validity Start")
    yellow_validity_end = fields.Char(related="yellow_id.finish_period", string="Validity End")
    yellow_mothly_tariff_adj = fields.Integer(related="yellow_id.mothly_tariff_adj", sting="Monthly Tariff Adjutsment (Downgrade)")
    yellow_monthly_customer_loss = fields.Integer(related="yellow_id.monthly_customer_loss", sting="Monthly Customer Loss (Churn)")
    yellow_montly_customer_renewal_rate = fields.Integer(related="yellow_id.montly_customer_renewal_rate", sting="Monthly Customer Renewal Rate")
    yellow_montly_contract_loss = fields.Integer(related="yellow_id.montly_contract_loss", sting="Monthly Contract Loss")

    red_id = fields.Many2one('velo.retention','Red ID')
    red = fields.Char(related="red_id.name", string="red (Power)")
    red_contract_renewal_rate = fields.Integer(related="red_id.contract_renewal_rate", string="Contract Renewal Rate")
    red_mtl_churn = fields.Integer(related="red_id.mtl_churn", string="Monthly Tarif Loss From Churn")
    red_mtl_downgrade = fields.Integer(related="red_id.mtl_downgrade", string="Monthly Tarif Loss From Downgrade")
    red_prog_name = fields.Many2one('velo.program.name', string="Program Name")
    red_prog_type = fields.Many2one('velo.program.promo_type', string="Program Type")
    red_decrease = fields.Integer(related="red_id.decrease", string="Decrease % - Monthly Tariff from New Tarif")
    red_increase = fields.Integer(related="red_id.increase", string="Incre(Decre) % - B/W Capacity")
    red_gimmick = fields.Html(related="red_id.desc", string="Gimmick")
    red_validity_start = fields.Char(related="red_id.start_period", string="Validity Start")
    red_validity_end = fields.Char(related="red_id.finish_period", string="Validity End")
    red_mothly_tariff_adj = fields.Integer(related="red_id.mothly_tariff_adj", sting="Monthly Tariff Adjutsment (Downgrade)")
    red_monthly_customer_loss = fields.Integer(related="red_id.monthly_customer_loss", sting="Monthly Customer Loss (Churn)")
    red_montly_customer_renewal_rate = fields.Integer(related="red_id.montly_customer_renewal_rate", sting="Monthly Customer Renewal Rate")
    red_montly_contract_loss = fields.Integer(related="red_id.montly_contract_loss", sting="Monthly Contract Loss")



 
