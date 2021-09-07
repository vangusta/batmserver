# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request

class Inherit_res_partner_velo(models.Model):
    _inherit = 'res.partner'
    _order = 'pop_name asc, name asc'

    id_object = fields.Char(string="Cust ID")
    contact_name = fields.Char(string="IT Contact")
    contact_title = fields.Char(string="Title")
    contact_cluster = fields.Char(string="Cluster")
    brand_object = fields.Many2one('brand.object', string="Brand")
    technical_contact = fields.Char('Technical Contact')
    customer_type = fields.Selection([('Reguler', 'Reguler'), ('Major', 'Major')], string="Customer Type")
    industry = fields.Many2one('pop.industry', string="Industry")
    industry_cluster = fields.Many2one('pop.industry.cluster', string="Industry Cluster")
    total_service = fields.Integer(compute="_count_total_contract", string="Total Service", store=True)
    total_revenue = fields.Char(string="Total Revenue")
    revenue_month = fields.Float(compute="_total_revenue_month", string="Monthly Tariff", store=True)
    arpu_month = fields.Float(compute="_total_arpu_month", string="ARPU/Month", store=True)
    group_object = fields.Many2one('group.object', string="Group")
    job_position = fields.Char(string="Job Position")
    pop_id = fields.Many2many('pop.service.coverage', string="POP")
    pop_ids = fields.Char(related="pop_id.pop_id", string="POP ID", store=True)
    pop_name = fields.Char(related="pop_id.pop_name", string="POP Name", store=True)
    service_id = fields.Char(string="Service ID", compute="_count_total_contract")
    activation_date = fields.Char(string="Activation Date", compute="_count_total_contract")
    termination_date = fields.Char(string="Termination Date", compute="_count_total_contract")
    exp_date = fields.Char(string="Contract Expiry", compute="_count_total_contract")
    space = fields.Char(' ', readonly=True) 
    capacity = fields.Char('Capacity')
    product = fields.Many2one('product.template', string="Product")

    sale_subcription_ids = fields.One2many('sale.subscription','partner_id',string="Sale Subcription")

    tenant_cold_leads = fields.Char('Cold Leads')
    tenant_mcf_c = fields.Boolean(string="MCF-C")
    tenant_sales_focus = fields.Char('Sales Focus')

    tenant_am = fields.Many2one('pop.pic', string="AM")
    tenant_remarks = fields.Char(string="Remarks")
    tenant_floor = fields.Char(string="Floor")
    tenant_budget = fields.Char(string="Budget")
    tenant_existing_provider = fields.Char(string="Existing Provider")
    tenant_service = fields.Char(string="Service")
    tenant_program = fields.Selection([('LoveVelo', 'LoveVelo'), ('BeVelo', 'BeVelo')], default='')
    tenant_sales_pipeline2 = fields.Many2one('crm.stage', string="Pipeline Progress")
    tenant_total_user = fields.Integer(string="Total User")
    tenant_expired = fields.Date(string="Contract Expiry")
    tenant_capacity = fields.Char('Capacity')
    tenant_product = fields.Many2one('product.template', string="Product")

    marketing_activities = fields.Char('Marketing Activities')
    marketing_date = fields.Date('Date')
    response_date = fields.Date('Response Date')
    req_follow_up = fields.Boolean('Request Follow-Up')
    cold_leads_date = fields.Date('Cold Lead Date')

    sales_activities = fields.Char('Sales Activities')
    activities_date = fields.Date('Activities Date')
    opportunity_stage = fields.Char('Opportunity Stage')
    opportunity_stage_budget = fields.Boolean('Budget')
    opportunity_stage_service_delivery = fields.Boolean('Service Delivery')
    opportunity_stage_solution_fit = fields.Boolean('Solution Fit')
    opportunity_stage_pricing = fields.Boolean('Pricing')
    opportunity_stage_relationship = fields.Boolean('Relationship')

    tenant = fields.Boolean(string="Potential", default=True)
    tenant_mcf_c = fields.Boolean(string="MCF-C")
    partner = fields.Boolean(string="Partner")
    competitor = fields.Boolean(string="Competitor")
    contact = fields.Boolean(string="Contact")

    acc_mgm = fields.Many2one('pic.manager', string="AM Manager")
    pic_partner_id = fields.Many2one('pop.pic', string="Account Manager")

    opportunity_stage = fields.Char('Opportunity Stage')
    opportunity_stage1 = fields.Integer(string="Opportunity Progress", compute="_compute_opportunity_stage")

    opportunity_stage_budget = fields.Boolean(string="Budget", readonly=True)
    opportunity_stage_service_delivery = fields.Boolean(string="Service Delivery",readonly=True)
    opportunity_stage_solution_fit = fields.Boolean(string='Solution Fit',readonly=True)
    opportunity_stage_pricing = fields.Boolean(string='Pricing',readonly=True)
    opportunity_stage_relationship = fields.Boolean(string='Relationship',readonly=True)

    def function_name(self):
        self.tenant = True

    @api.depends('opportunity_stage_budget', 'opportunity_stage_service_delivery', 'opportunity_stage_solution_fit','opportunity_stage_pricing','opportunity_stage_relationship')
    def _compute_opportunity_stage(self):
        budget = 20
        service_delivery = 20
        solution_fit = 20
        pricing = 20
        relationship = 20
        for rec in self:
            if rec.opportunity_stage_budget == True:
                rec.opportunity_stage1 = budget
            if rec.opportunity_stage_service_delivery == True:
                rec.opportunity_stage1 = service_delivery
            if rec.opportunity_stage_solution_fit == True:
                rec.opportunity_stage1 = solution_fit
            if rec.opportunity_stage_pricing == True:
                rec.opportunity_stage1 = pricing
            if rec.opportunity_stage_relationship == True:
                 rec.opportunity_stage1 = relationship

            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True:
                  rec.opportunity_stage1 = budget + service_delivery
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_solution_fit == True:
                  rec.opportunity_stage1 = budget + solution_fit
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_pricing == True:
                  rec.opportunity_stage1 = budget + pricing
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_relationship == True:
                  rec.opportunity_stage1 = budget + relationship
            
            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True:
                  rec.opportunity_stage1 = service_delivery + solution_fit
            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_pricing == True:
                  rec.opportunity_stage1 = service_delivery + pricing
            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_relationship == True:
                  rec.opportunity_stage1 = service_delivery + relationship

            if rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True:
                  rec.opportunity_stage1 = solution_fit + pricing
            if rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_relationship == True:
                  rec.opportunity_stage1 = solution_fit + relationship
            if rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                  rec.opportunity_stage1 = pricing + relationship
            
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True:
                rec.opportunity_stage1 = budget + service_delivery + solution_fit
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_pricing == True:
                rec.opportunity_stage1 = budget + service_delivery + pricing
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1 = budget + service_delivery + relationship
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True:
                rec.opportunity_stage1 = budget + solution_fit + pricing
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1 = budget + solution_fit + relationship
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1 = budget + pricing + relationship

            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True:
                rec.opportunity_stage1 = service_delivery + solution_fit + pricing
            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1 = service_delivery + solution_fit + relationship
            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1 = service_delivery + pricing + relationship
            if rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1 = solution_fit + pricing + relationship
            
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True:
                rec.opportunity_stage1 = budget + service_delivery + solution_fit + pricing
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1 = budget + service_delivery + solution_fit + relationship
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1 = budget + service_delivery + pricing + relationship
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1 = budget + solution_fit + pricing + relationship
            if rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1 = service_delivery + solution_fit + pricing + relationship
            if rec.opportunity_stage_budget == True and rec.opportunity_stage_service_delivery == True and rec.opportunity_stage_solution_fit == True and rec.opportunity_stage_pricing == True and rec.opportunity_stage_relationship == True:
                rec.opportunity_stage1 = budget + service_delivery + solution_fit + pricing + relationship
            if rec.opportunity_stage_budget == False and rec.opportunity_stage_service_delivery == False and rec.opportunity_stage_solution_fit == False and rec.opportunity_stage_pricing == False and rec.opportunity_stage_relationship == False:
                rec.opportunity_stage1 = 0

    @api.depends('sale_subcription_ids')
    def _count_total_contract(self):
        for i in self:
            val_service = ''
            val_act_date = ''
            val_term_date = ''
            val_exp_date = ''
            for n in i.sale_subcription_ids :
                if n.service_id :
                    val_service = str(val_service) + str(n.service_id) + ', '
                if n.act_date :
                    val_act_date = str(val_act_date) + str(n.act_date) + ', '
                if n.termination_date :
                    val_term_date = str(val_term_date) + str(n.termination_date) +', '
                if n.exp_date :
                    val_exp_date = str(val_exp_date) + str(n.exp_date) +', '

            i.service_id = val_service
            i.activation_date = val_act_date
            i.termination_date = val_term_date
            i.exp_date = val_exp_date
            i.total_service = len(i.sale_subcription_ids)
    
    @api.depends('sale_subcription_ids')
    def _total_revenue_month(self):
        for a in self:
            a.revenue_month = sum(line.recurring_total for line in a.sale_subcription_ids)
    
    @api.depends('sale_subcription_ids')
    def _total_arpu_month(self):
        for b in self:
            b.revenue_month = sum(line.recurring_total for line in b.sale_subcription_ids)
            if len(b.sale_subcription_ids) != 0:
                b.arpu_month = b.revenue_month / (len(b.sale_subcription_ids))
            else:
                b.arpu_month = 0


class velo_customer_brand(models.Model):
    _name = 'brand.object'
    _description = 'Model customer brand'

    name = fields.Char(string="Name")

class velo_customer_group(models.Model):
    _name = 'group.object'
    _description = 'Model customer group'

    name = fields.Char(string="Name")

class pic_manager(models.Model):
    _name = 'pic.manager'
    _description = 'PIC Manager'
    _rec_name = 'pic_manager_name'

    pic_manager_name = fields.Many2one('hr.employee', string="Manager Name")
    pic_number_of_customer = fields.Float(string="Total Customer", compute="_total_number_of_customers_manager", store=True)#
    pic_number_of_customer_pop = fields.Float(string="Customer POP", compute="_total_number_of_customers_pop", store=True)
    pic_number_of_customer_am = fields.Float(string="Customer AM", compute="_total_number_of_customers_am", store=True)
    
    pic_number_of_customer_industry_cluster = fields.Float(string="Number of Customers", compute="_total_number_of_customers_cluster_manager", store=True)
    pic_number_of_customer_industry_cluster_cluster = fields.Float(string="Number of Customers", compute="_total_number_of_customers_cluster_cluster", store=True)
    pic_number_of_customer_industry_cluster_am = fields.Float(string="Number of Customers", compute="_total_number_of_customers_cluster_am", store=True)
    
    pic_number_of_potential = fields.Float(string="Total Potential", compute="_total_number_of_potential_manager", store=True)
    pic_number_of_potential_pop = fields.Float(string="Potential POP", compute="_total_number_of_potential_pop", store=True)
    pic_number_of_potential_am = fields.Float(string="Potential AM", compute="_total_number_of_potential_am", store=True)
    
    pic_number_of_potential_industry_cluster = fields.Float(string="Number of Potential", compute="_total_number_of_potential_cluster_manager", store=True)
    pic_number_of_potential_industry_cluster_cluster = fields.Float(string="Number of Potential", compute="_total_number_of_potential_cluster_cluster", store=True)
    pic_number_of_potential_industry_cluster_am = fields.Float(string="Number of Potential", compute="_total_number_of_potential_cluster_am", store=True)
    
    pic_current_penetration = fields.Float(string="Total Penetration", compute="_total_current_penetration", store=True)
    pic_current_penetration_industry_cluster = fields.Float(string="Current Penetration", compute="_total_current_penetration_industry_cluster", store=True)
    
    pic_monthly_tariff = fields.Float(string="Total Monthly Tariff", compute="_total_monthly_tariff_manager", store=True)
    pic_monthly_tarif_pop = fields.Float(string="Monthly Tariff POP", compute="_total_monthly_tariff_pop", store=True)
    pic_monthly_tarif_am = fields.Float(string="Monthly Tariff AM", compute="_total_monthly_tariff_am", store=True)

    pic_monthly_tarif_cluster = fields.Float(string="Monthly Tariff", compute="_total_monthly_tarif_cluster_manager", store=True)
    pic_monthly_tarif_cluster_cluster = fields.Float(string="Monthly Tariff POP", compute="_total_monthly_tarif_cluster_cluster", store=True)
    pic_monthly_tarif_cluster_am = fields.Float(string="Monthly Tariff AM", compute="_total_monthly_tarif_cluster_am", store=True)

    pic_summary_of_specific_industry = fields.Many2one('pop.type', string="Specific Industry")
    pic_period = fields.Date(string="Period")
    pic_annual_quota = fields.Integer(string="Annual Quota")
    pic_quota_this_month = fields.Integer(string="OB This Month")
    pic_quota_last_month = fields.Integer('OB Last Month')
    pic_mcfc_this_month = fields.Integer('MCF-C This Month')
    pic_ytd_achievement = fields.Float(string="YTD Achievement")
    pic_sf_this_month = fields.Integer(related="service_coverage_ids.pop_total_sales_focus", string="SF This Month")
    
    pic_cold_leads = fields.Integer(string="Cold Leads", compute="_total_cold_leads", store=True)
    pic_cold_leads_pop = fields.Integer(string="Cold Leads", compute="_total_cold_leads_pop", store=True)
    pic_cold_leads_am = fields.Integer(string="Cold Leads", compute="_total_cold_leads_am", store=True)
    
    pic_cold_leads_cluster = fields.Integer(string="Cold Leads", compute="_total_cold_leads_cluster_manager", store=True )
    pic_cold_leads_cluster_cluster = fields.Integer(string="Cold Leads", compute="_total_cold_leads_cluster_cluster", store=True)
    pic_cold_leads_cluster_am = fields.Integer(string="Cold Leads", compute="_total_cold_leads_cluster_am", store=True)

    pic_number_of_arpu = fields.Float(string="ARPU", compute="_total_number_of_arpu_manager", store=True)
    pic_number_of_arpu_pop = fields.Float(string="ARPU POP", compute="_total_number_of_arpu_pop", store=True)

    total_rowcount_name_pop = fields.Integer(string="Total Pop/Cluster", compute="_total_rowcount_name_pop", store=True)
    
    industry_cluster_ids = fields.One2many('pop.industry.cluster', 'pop_industry_cluster_manager', string="Industry Cluster ID")
    service_coverage_ids = fields.One2many('pop.service.coverage', 'pic_manager', string="Service Coverage ID")
    pop_pic_am_ids = fields.One2many('pop.pic', 'pic_am_manager', string="PIC ID")
    partner_ids = fields.One2many('res.partner', 'acc_mgm', string="Service Coverage Customer")
    user_id = fields.Many2one('res.users', string='Related User', required=True)



    #total pop/cluster
    @api.depends('service_coverage_ids')
    def _total_rowcount_name_pop(self):  
        for service in self:      
            total_rowcount = 0.0       
            for line in service.service_coverage_ids:
                total_rowcount += 1
            service.update({
                'total_rowcount_name_pop': total_rowcount,
            })

    #total cold leads Industry Cluster
    @api.depends('industry_cluster_ids')
    def _total_cold_leads_cluster_cluster(self):
        for a in self:
            a.pic_cold_leads_cluster_cluster = sum(line.pop_industry_cluster_cold_leads for line in a.industry_cluster_ids)
    
    @api.depends('pop_pic_am_ids')
    def _total_cold_leads_cluster_am(self):
        for a in self:
            a.pic_cold_leads_cluster_am = sum(line.pic_cold_leads for line in a.pop_pic_am_ids)

    @api.depends('pic_cold_leads_cluster_cluster', 'pic_cold_leads_cluster_am')
    def _total_cold_leads_cluster_manager(self):
        for rec in self:
            rec.pic_cold_leads_cluster = rec.pic_cold_leads_cluster_cluster + rec.pic_cold_leads_cluster_am
    
    #total Customer Industry Cluster
    @api.depends('industry_cluster_ids')
    def _total_number_of_customers_cluster_cluster(self):
        for a in self:
            a.pic_number_of_customer_industry_cluster_cluster = sum(line.pop_industry_cluster_total_customer for line in a.industry_cluster_ids)
    
    @api.depends('pop_pic_am_ids')
    def _total_number_of_customers_cluster_am(self):
        for a in self:
            a.pic_number_of_customer_industry_cluster_am = sum(line.pic_number_of_customer_industry_cluster for line in a.pop_pic_am_ids)

    @api.depends('pic_number_of_customer_industry_cluster_cluster', 'pic_number_of_customer_industry_cluster_am')
    def _total_number_of_customers_cluster_manager(self):
        for rec in self:
            rec.pic_number_of_customer_industry_cluster = rec.pic_number_of_customer_industry_cluster_cluster + rec.pic_number_of_customer_industry_cluster_am
    
    #total potential industry cluster
    @api.depends('industry_cluster_ids')
    def _total_number_of_potential_cluster_cluster(self):
        for a in self:
            a.pic_number_of_potential_industry_cluster_cluster = sum(line.pop_industry_cluster_total_potential for line in a.industry_cluster_ids)
    
    @api.depends('pop_pic_am_ids')
    def _total_number_of_potential_cluster_am(self):
        for a in self:
            a.pic_number_of_potential_industry_cluster_am = sum(line.pic_number_of_potential_industry_cluster for line in a.pop_pic_am_ids)

    @api.depends('pic_number_of_potential_industry_cluster_cluster', 'pic_number_of_potential_industry_cluster_am')
    def _total_number_of_potential_cluster_manager(self):
        for rec in self:
            rec.pic_number_of_potential_industry_cluster = rec.pic_number_of_potential_industry_cluster_cluster + rec.pic_number_of_potential_industry_cluster_am
          
    #total monthly tariff industry cluster
    @api.depends('industry_cluster_ids')
    def _total_monthly_tarif_cluster_cluster(self):
        for a in self:
            a.pic_monthly_tarif_cluster_cluster = sum(line.pop_industry_cluster_revenue_month for line in a.industry_cluster_ids)
    
    @api.depends('pop_pic_am_ids')
    def _total_monthly_tarif_cluster_am(self):
        for a in self:
            a.pic_monthly_tarif_cluster_am = sum(line.pic_monthly_tarif_industry_cluster for line in a.pop_pic_am_ids)

    @api.depends('pic_monthly_tarif_cluster_cluster', 'pic_monthly_tarif_cluster_am')
    def _total_monthly_tarif_cluster_manager(self):
        for rec in self:
            rec.pic_monthly_tarif_cluster = rec.pic_monthly_tarif_cluster_cluster + rec.pic_monthly_tarif_cluster_am
    
          
    #total customer pop list
    @api.depends('service_coverage_ids')
    def _total_number_of_customers_pop(self):
        for a in self:
            a.pic_number_of_customer_pop = sum(line.pop_total_customer for line in a.service_coverage_ids)
    
    @api.depends('pop_pic_am_ids')
    def _total_number_of_customers_am(self):
        for a in self:
            a.pic_number_of_customer_am = sum(line.pic_number_of_customer for line in a.pop_pic_am_ids)

    @api.depends('pic_number_of_customer_pop', 'pic_number_of_customer_am')
    def _total_number_of_customers_manager(self):
        for rec in self:
            rec.pic_number_of_customer = rec.pic_number_of_customer_pop + rec.pic_number_of_customer_am
          

    #total potential pop list
    @api.depends('service_coverage_ids')
    def _total_number_of_potential_pop(self):
        for a in self:
            a.pic_number_of_potential_pop = sum(line.pop_total_potential for line in a.service_coverage_ids)
    
    @api.depends('pop_pic_am_ids')
    def _total_number_of_potential_am(self):
        for a in self:
            a.pic_number_of_potential_am = sum(line.pic_number_of_potential for line in a.pop_pic_am_ids)
    
    @api.depends('pic_number_of_potential_pop', 'pic_number_of_potential_am')
    def _total_number_of_potential_manager(self):
        for rec in self:
            rec.pic_number_of_potential = rec.pic_number_of_potential_pop + rec.pic_number_of_potential_am

    #total monthly tariff pop list
    @api.depends('service_coverage_ids')
    def _total_monthly_tariff_pop(self):
        for a in self:
            a.pic_monthly_tarif_pop = sum(line.pop_total_monthly_tariff for line in a.service_coverage_ids)
    
    @api.depends('pop_pic_am_ids')
    def _total_monthly_tariff_am(self):
        for a in self:
            a.pic_monthly_tarif_am = sum(line.pic_monthly_tarif for line in a.pop_pic_am_ids)

    @api.depends('pic_monthly_tarif_pop', 'pic_monthly_tarif_am')
    def _total_monthly_tariff_manager(self):
        for rec in self:
            rec.pic_monthly_tariff = rec.pic_monthly_tarif_pop + rec.pic_monthly_tarif_am

    #total ARPU pop list
    @api.depends('service_coverage_ids')
    def _total_number_of_arpu_pop(self):
        for a in self:
            a.pic_number_of_arpu_pop = sum(line.pop_arpu for line in a.service_coverage_ids)

    @api.depends('pic_number_of_arpu_pop')
    def _total_number_of_arpu_manager(self):
        for rec in self:
            rec.pic_number_of_arpu = rec.pic_number_of_arpu_pop 
    
    #total cold leads pop list
    @api.depends('service_coverage_ids')
    def _total_cold_leads_pop(self):
        for a in self:
            a.pic_cold_leads_pop = sum(line.pop_cold_leads for line in a.service_coverage_ids)
    
    @api.depends('pop_pic_am_ids')
    def _total_cold_leads_am(self):
        for a in self:
            a.pic_cold_leads_am = sum(line.pic_cold_leads for line in a.pop_pic_am_ids)

    @api.depends('pic_cold_leads_pop', 'pic_cold_leads_am')
    def _total_cold_leads(self):
        for rec in self:
            rec.pic_cold_leads = rec.pic_cold_leads_pop + rec.pic_cold_leads_am

    #menghitung total penetration di form pic.manager (HRB)
    @api.depends('pic_number_of_customer','pic_number_of_potential')
    def _total_current_penetration(self):
        for i in self:
            if i.pic_number_of_customer == 0:
                i.pic_current_penetration = 0
            elif i.pic_number_of_potential == 0:
                i.pic_current_penetration = 0
            else:
                i.pic_current_penetration = (i.pic_number_of_customer / i.pic_number_of_potential)
    
    #menghitung total penetration industry cluster di form pic.manager 
    @api.depends('pic_number_of_customer_industry_cluster','pic_number_of_potential_industry_cluster')
    def _total_current_penetration_industry_cluster(self):
        for i in self:
            if i.pic_number_of_customer_industry_cluster == 0:
                i.pic_current_penetration_industry_cluster = 0
            elif i.pic_number_of_potential_industry_cluster == 0:
                i.pic_current_penetration_industry_cluster = 0
            else:
                i.pic_current_penetration_industry_cluster = (i.pic_number_of_customer_industry_cluster / i.pic_number_of_potential_industry_cluster)
        
    
class pic(models.Model):
    _name = 'pop.pic'
    _description = 'POP PIC'
    _rec_name = 'pop_pic_name_am'

    pop_pic_name_am = fields.Many2one('hr.employee', string="AM Name")
    pic_am_manager = fields.Many2one('pic.manager', string="Manager In Charge")
    pic_number_of_customer = fields.Integer(string="Total Customer", compute="_total_number_of_customers")
    pic_number_of_customer_industry_cluster = fields.Integer(string="Total Customer", compute="_total_number_of_customers_inudstry_cluster")
    pic_number_of_potential = fields.Integer(string="Total Potential", compute="_total_number_of_potential")
    pic_number_of_potential_industry_cluster = fields.Integer(string="Total Potential", compute="_total_number_of_potential_inudstry_cluster")
    pic_current_penetration = fields.Float(string="Total Penetration", compute="_total_current_penetration")
    pic_current_penetration_industry_cluster = fields.Float(string="Total Penetration", compute="_total_current_penetration_inudstry_cluster")
    pic_monthly_tarif = fields.Integer(string="Total Monthly Tariff", compute="_total_monthly_tariff", store=True)
    pic_monthly_tarif_industry_cluster = fields.Integer(string="Monthly Tariff", compute="_total_monthly_tariff_industry_cluster")
    pic_summary_of_specific_industry = fields.Many2one('pop.type', string="Specific Industry")
    pic_period = fields.Date(string="Period")
    pic_annual_quota = fields.Integer(string="Annual Quota")
    pic_quota_this_month = fields.Integer(string="OB This Month")
    pic_quota_last_month = fields.Integer('OB Last Month')
    pic_mcfc_this_month = fields.Integer('MCF-C This Month')
    pic_ytd_achievement = fields.Float(string="YTD Achievement")
    pic_sf_this_month = fields.Integer(related="service_coverage_ids.pop_total_sales_focus", string="SF This Month")
    pic_cold_leads = fields.Integer(string="Cold Leads")

    industry_cluster_ids = fields.One2many('pop.industry.cluster', 'pop_industry_cluster_pic_am', string="Industry Cluster ID")
    service_coverage_ids = fields.One2many('pop.service.coverage', 'pic_id', string="Service Coverage ID")

    ytd_achievement_ids = fields.One2many('ytd.achievement', 'pic_id')
    ytd_sales_focus = fields.One2many('ytd.sales.focus', 'pic_id')
    ytd_mcfc_ids = fields.One2many('ytd.mcfc', 'pic_id')
    ytd_cold_leads_ids = fields.One2many('ytd.cold.leads', 'pic_id')
    total_rowcount_name_pic = fields.Integer(string="Total Pop/Cluster", compute="_total_rowcount_name_pic")
    pic_number_of_arpu = fields.Integer(string="ARPU", compute="_total_number_of_arpu_manager")
    pic_number_of_arpu_pic = fields.Integer(string="ARPU POP", compute="_total_number_of_arpu_pop")
    pic_partner_ids = fields.One2many('res.partner', 'pic_partner_id', string="PIC Customer")
    user_id = fields.Many2one('res.users', string='Related User', required=True)


    #total pop/cluster
    @api.depends('service_coverage_ids')
    def _total_rowcount_name_pic(self):  
        for service in self:      
            total_rowcount = 0.0       
            for line in service.service_coverage_ids:
                total_rowcount += 1
            service.update({
                'total_rowcount_name_pic': total_rowcount,
            })

    #total ARPU pop list
    @api.depends('service_coverage_ids')
    def _total_number_of_arpu_pop(self):
        for a in self:
            a.pic_number_of_arpu_pic = sum(line.pop_arpu for line in a.service_coverage_ids)

    #total ARPU pop list
    @api.depends('pic_number_of_arpu_pic')
    def _total_number_of_arpu_manager(self):
        for rec in self:
            rec.pic_number_of_arpu = rec.pic_number_of_arpu_pic 

    #total customer di form pop.pic
    @api.depends('service_coverage_ids')
    def _total_number_of_customers(self):
        for a in self:
            a.pic_number_of_customer = sum(line.pop_total_customer for line in a.service_coverage_ids)
    
    #total potential di form pop.pic
    @api.depends('service_coverage_ids')
    def _total_number_of_potential(self):
        for a in self:
            a.pic_number_of_potential = sum(line.pop_total_potential for line in a.service_coverage_ids)
    
    ##total penetration di form pop.pic
    @api.depends('pic_number_of_customer','pic_number_of_potential')
    def _total_current_penetration(self):
        for i in self:
            if i.pic_number_of_customer == 0:
                i.pic_current_penetration = 0
            elif i.pic_number_of_potential == 0:
                i.pic_current_penetration = 0
            else:
                i.pic_current_penetration = (i.pic_number_of_customer / i.pic_number_of_potential)
    
    #total monthly tarif di form pop.pic
    @api.depends('service_coverage_ids')
    def _total_monthly_tariff(self):
        for a in self:
            a.pic_monthly_tarif = sum(line.pop_total_monthly_tariff for line in a.service_coverage_ids)
    
    #total customer industry cluster di form pop.pic
    @api.depends('industry_cluster_ids')
    def _total_number_of_customers_inudstry_cluster(self):
        for a in self:
            a.pic_number_of_customer_industry_cluster = sum(line.pop_industry_cluster_total_customer for line in a.industry_cluster_ids)
    
    #total potential industry cluster di form pop.pic
    @api.depends('industry_cluster_ids')
    def _total_number_of_potential_inudstry_cluster(self):
        for a in self:
            a.pic_number_of_potential_industry_cluster = sum(line.pop_industry_cluster_total_potential for line in a.industry_cluster_ids)
    
    #total penetration industry cluster di form pop.pic
    @api.depends('pic_number_of_customer_industry_cluster','pic_number_of_potential_industry_cluster')
    def _total_current_penetration_inudstry_cluster(self):
        for i in self:
            if i.pic_number_of_customer_industry_cluster == 0:
                i.pic_current_penetration_industry_cluster = 0
            elif i.pic_number_of_potential_industry_cluster == 0:
                i.pic_current_penetration_industry_cluster = 0
            else:
                i.pic_current_penetration_industry_cluster = (i.pic_number_of_customer_industry_cluster / i.pic_number_of_potential_industry_cluster)
    
    #total monthly tariff industry cluster di form pop.pic
    @api.depends('industry_cluster_ids')
    def _total_monthly_tariff_industry_cluster(self):
        for a in self:
            a.pic_monthly_tarif_industry_cluster = sum(line.pop_industry_cluster_revenue_month for line in a.industry_cluster_ids)

class YtdAchievement(models.Model):
    _name = 'ytd.achievement'
    _description = 'YTD Achievement'

    pic_id = fields.Many2one('pop.pic', string="PIC")
    customer_name = fields.Many2one('res.partner', string="Customer Name", domain=[('customer_rank', '=', True)])
    period = fields.Date('Period')
    ob_date = fields.Date('OB Date')
    monthly_tariff = fields.Integer('Monthly Tariff')
    service = fields.Char('Service')
    ba_date = fields.Date('BA Date')

class YtdSalesFocus(models.Model):
    _name = 'ytd.sales.focus'
    _description = 'YTD Sales Focus'

    pic_id = fields.Many2one('pop.pic', string="PIC")
    potential_name = fields.Many2one('res.partner', string="Potential Name", domain=[('tenant', '=', True)])
    period = fields.Date('Period')
    propose_tariff = fields.Date('Propose Tariff')
    service = fields.Char('Service')
    opportunity = fields.Float('Opportunity %')
    opportunity_mix = fields.Char('Opportunity Mix')
    sf_result = fields.Selection([('Win', 'Win'), ('Lose', 'Lose'), ('Carry Over', 'Carry Over')], string="SF Result")
    next_action = fields.Char('Next Action')

class YtdMcfC(models.Model):
    _name = 'ytd.mcfc'
    _description = 'YTD MCF-C'

    pic_id = fields.Many2one('pop.pic', string="PIC")
    potential_name = fields.Many2one('res.partner', string="Potential Name", domain=[('tenant', '=', True)])
    period = fields.Date('Period')
    propose_tariff = fields.Date('Propose Tariff')
    service = fields.Char('Service')
    opportunity = fields.Float('Opportunity %')
    opportunity_mix = fields.Char('Opportunity Mix')
    sf_result = fields.Selection([('Win', 'Win'), ('Lose', 'Lose'), ('Carry Over', 'Carry Over')], string="SF Result")
    next_action = fields.Char('Next Action')

class YtdColdLeads(models.Model):
    _name = 'ytd.cold.leads'
    _description = 'YTD Cold Leads'

    pic_id = fields.Many2one('pop.pic', string="PIC")
    cold_leads_name = fields.Many2one('res.partner', string="Potential Name", domain=[('tenant', '=', True)])
    period = fields.Date('Period')
    cold_leads_date = fields.Date('Cold Leads Date')
    marketing_program = fields.Many2one('velo.program', string="Marketing Program")

class Inherit_pop_industry_cluster(models.Model):
    _inherit = 'pop.industry.cluster'
    
    pop_potential_ids = fields.One2many('res.partner', 'industry_cluster', string="Pontential", domain=[('tenant', '=', True)])
    industry_cluster_customer_ids = fields.One2many('res.partner', 'industry_cluster', string="Customer", domain=[('customer_rank', '=', 1), ('tenant', '=', False)])
    
     #count total industri potential di menu market potential (setting=>pop industry cluster)
    @api.depends('pop_potential_ids')
    def _count_total_potential(self):
        for i in self:
            i.pop_industry_cluster_total_potential = len(i.pop_potential_ids)

    #count total industri potential di menu market potential (setting=>pop industry cluster)
    @api.depends('industry_cluster_customer_ids')
    def _count_total_customer(self):
        for i in self:
            i.pop_industry_cluster_total_customer = len(i.industry_cluster_customer_ids)
    
    #count total industri ponetration di menu market potential (setting=>pop industry cluster)
    @api.depends('pop_industry_cluster_total_customer','pop_industry_cluster_total_potential')
    def _total_current_penetration(self):
        for i in self:
            if i.pop_industry_cluster_total_customer == 0:
                i.pop_industry_cluster_total_penetration = 0
            elif i.pop_industry_cluster_total_potential == 0:
                i.pop_industry_cluster_total_penetration = 0
            else:
                i.pop_industry_cluster_total_penetration = (i.pop_industry_cluster_total_customer / i.pop_industry_cluster_total_potential)

    #count total customer di menu market potential (setting=>pop industry cluster)
    @api.depends('industry_cluster_customer_ids')
    def _total_monthly_tariff(self):
        for a in self:
            a.pop_industry_cluster_revenue_month = sum(line.revenue_month for line in a.industry_cluster_customer_ids)
    
    #count total service di menu market potential (setting=>pop industry cluster)
    @api.depends('industry_cluster_customer_ids')
    def _total_service(self):
        for a in self:
            a.pop_indistry_cluster_total_service = sum(line.total_service for line in a.industry_cluster_customer_ids)
    
    #count total ARPU di menu market potential (setting=>pop industry cluster)
    @api.depends('pop_industry_cluster_revenue_month','pop_industry_cluster_total_customer')
    def _industry_cluster_arpu(self):
        for i in self:
            if i.pop_industry_cluster_revenue_month == 0:
                i.pop_industry_cluster_arpu = 0
            elif i.pop_industry_cluster_total_customer == 0:
                i.pop_industry_cluster_arpu
            else:
                i.pop_industry_cluster_arpu = i.pop_industry_cluster_revenue_month / i.pop_industry_cluster_total_customer


class Pop(models.Model):
    _inherit = 'pop.service.coverage'

    pic_manager = fields.Many2one('pic.manager', string="Account Management")
    pic_id = fields.Many2one('pop.pic', string="PIC ID")
    
    res_partner = fields.Many2many('res.partner', string="Customer", domain=[('customer_rank', '=', 1), ('tenant', '=', False)])
    product_template_ids = fields.Many2many('product.template', string="Product")
    pop_tenant_id = fields.One2many('res.partner', 'pop_id', string="Potential", domain=[('tenant', '=', True)])
    
   #count total Monthly tariff di menu market potential (summary of type)
    @api.depends('res_partner')
    def _total_monthly_tariff(self):
        for a in self:
            a.pop_total_monthly_tariff = sum(line.revenue_month for line in a.res_partner)

    #count ARPU di menu market potential (summary of type)
    @api.depends('res_partner')
    def _total_arpu(self):
        for b in self:
            b.pop_total_monthly_tariff = sum(line.revenue_month for line in b.res_partner)
            if len(b.res_partner) == 0:
                b.pop_arpu = 0
            else:
                b.pop_arpu = b.pop_total_monthly_tariff / (len(b.res_partner))

    #count pop total customer di menu market potential (summary of type)
    @api.depends('res_partner')
    def _count_tot_customer(self):
        for i in self:
            i.pop_total_customer = len(i.res_partner)

    #count total industry (HRB) di menu market potential (summary of type)
    @api.depends('res_partner')
    def _count_tot_customer_hrb(self):
        for rec in self:
            count = 0
            tarif = 0
            service = 0
            for line in rec.res_partner:
                if line.industry.pop_industry_name.poptype_name == 'HRB':
                    count += 1
                    tarif += line.revenue_month
                    service += line.total_service

            rec.pop_total_customer_hrb = count
            rec.pop_total_monthly_tarif_hrb = tarif
            rec.pop_total_service_hrb = service

    #count total service di menu market potential (summary of type)
    @api.depends('res_partner')
    def _pop_total_service(self):
        for a in self:
            a.pop_total_service = sum(line.total_service for line in a.res_partner)
    
    #count Total Potential di menu market potential (summary of type)
    @api.depends('pop_tenant_id')
    def _count_tot_potential(self):
        for i in self:
            i.pop_total_potential = len(i.pop_tenant_id)


class velo_customer_summary(models.Model):
    _name = 'customer.summary'
    _description = 'Model Customer Summary'

    #count number of customer di Menu customer (setting=>Customer Summary)
    @api.model
    def _number_of_customer(self):
        hos_customer = self.env['res.partner'].search([('industry.id','=', self.hos_name.id),('tenant','=', False),('customer_rank','>', 0)])
        hrb_customer = self.env['res.partner'].search([('industry.id','=', self.hrb_name.id),('tenant','=', False),('customer_rank','>', 0)])
        itemb_customer = self.env['res.partner'].search([('industry.id','=', self.itemb_name.id),('tenant','=', False),('customer_rank','>', 0)])
        nrx_customer = self.env['res.partner'].search([('industry.id','=', self.nrx_name.id),('tenant','=', False),('customer_rank','>', 0)])
        for i in self:
            i.hos_number_of_customer = len(hos_customer)
            i.hrb_number_of_customer = len(hrb_customer)
            i.itemb_number_of_customer = len(itemb_customer)
            i.nrx_number_of_customer = len(nrx_customer)

            i.hos_revenue_month = sum(line.revenue_month for line in hos_customer)
            i.hrb_revenue_month = sum(line.revenue_month for line in hrb_customer)
            i.itemb_revenue_month = sum(line.revenue_month for line in itemb_customer)
            i.nrx_revenue_month = sum(line.revenue_month for line in nrx_customer)

            i.hos_arpu = i.hos_revenue_month / i.hos_number_of_customer
            i.hrb_arpu = i.hrb_revenue_month / i.hrb_number_of_customer
            i.itemb_arpu = i.itemb_revenue_month / i.itemb_number_of_customer
            i.nrx_arpu = i.nrx_revenue_month / i.nrx_number_of_customer

            hos_number_of_service = 0
            hrb_number_of_service = 0
            itemb_number_of_service = 0
            nrx_number_of_service = 0
            for line in hos_customer.sale_subcription_ids :
                hos_number_of_service = hos_number_of_service + 1 

            for line in hrb_customer.sale_subcription_ids :
                hrb_number_of_service = hrb_number_of_service + 1 

            for line in itemb_customer.sale_subcription_ids :
                itemb_number_of_service = itemb_number_of_service + 1 

            for line in nrx_customer.sale_subcription_ids :
                nrx_number_of_service = nrx_number_of_service + 1 

            i.hos_number_of_service = hos_number_of_service
            i.hrb_number_of_service = hrb_number_of_service
            i.itemb_number_of_service = itemb_number_of_service
            i.nrx_number_of_service = nrx_number_of_service


    hos_name = fields.Many2one("pop.industry",string="HOS Name")
    hos_number_of_customer = fields.Integer(string="HOS Number of Customer", compute="_number_of_customer")
    hos_revenue_month = fields.Float(string="HOS Revenue/Month", compute="_number_of_customer")
    hos_arpu = fields.Float(string="HOS ARPU", compute="_number_of_customer")
    hos_number_of_service = fields.Integer(string="HOS Number of Service", compute="_number_of_customer")
    hos_ob_quota = fields.Integer(string="HOS OB Quota")
    hos_ytd_achivement = fields.Float(string="HOS YTD Achivement")
    hos_achieve = fields.Float(stirng="HOS Achieve %")
    hos_ytd_churn = fields.Float(string="HOS YTD Churn")
    hos_ytd_downgrade = fields.Float(string="HOS YTD Downgrade")
    hos_ytd_net_increase = fields.Float(string="HOS YTD Net Increase")
    hos_ytd_rev_growth = fields.Float(string="HOS YTD Rev Growth")

    hrb_name = fields.Many2one("pop.industry",string="hrb Name")
    hrb_number_of_customer = fields.Integer(string="hrb Number of Customer", compute="_number_of_customer")
    hrb_revenue_month = fields.Float(string="hrb Revenue/Month", compute="_number_of_customer")
    hrb_arpu = fields.Float(string="hrb ARPU", compute="_number_of_customer")
    hrb_number_of_service = fields.Integer(string="hrb Number of Service", compute="_number_of_customer")
    hrb_ob_quota = fields.Integer(string="hrb OB Quota")
    hrb_ytd_achivement = fields.Float(string="hrb YTD Achivement")
    hrb_achieve = fields.Float(stirng="hrb Achieve %")
    hrb_ytd_churn = fields.Float(string="hrb YTD Churn")
    hrb_ytd_downgrade = fields.Float(string="hrb YTD Downgrade")
    hrb_ytd_net_increase = fields.Float(string="hrb YTD Net Increase")
    hrb_ytd_rev_growth = fields.Float(string="hrb YTD Rev Growth")

    itemb_name = fields.Many2one("pop.industry",string="itemb Name")
    itemb_number_of_customer = fields.Integer(string="itemb Number of Customer", compute="_number_of_customer")
    itemb_revenue_month = fields.Float(string="itemb Revenue/Month", compute="_number_of_customer")
    itemb_arpu = fields.Float(string="itemb ARPU", compute="_number_of_customer")
    itemb_number_of_service = fields.Integer(string="itemb Number of Service", compute="_number_of_customer")
    itemb_ob_quota = fields.Integer(string="itemb OB Quota")
    itemb_ytd_achivement = fields.Float(string="itemb YTD Achivement")
    itemb_achieve = fields.Float(stirng="itemb Achieve %")
    itemb_ytd_churn = fields.Float(string="itemb YTD Churn")
    itemb_ytd_downgrade = fields.Float(string="itemb YTD Downgrade")
    itemb_ytd_net_increase = fields.Float(string="itemb YTD Net Increase")
    itemb_ytd_rev_growth = fields.Float(string="itemb YTD Rev Growth")

    nrx_name = fields.Many2one("pop.industry",string="nrx Name")
    nrx_number_of_customer = fields.Integer(string="nrx Number of Customer", compute="_number_of_customer")
    nrx_revenue_month = fields.Float(string="nrx Revenue/Month", compute="_number_of_customer")
    nrx_arpu = fields.Float(string="nrx ARPU", compute="_number_of_customer")
    nrx_number_of_service = fields.Integer(string="nrx Number of Service", compute="_number_of_customer")
    nrx_ob_quota = fields.Integer(string="nrx OB Quota")
    nrx_ytd_achivement = fields.Float(string="nrx YTD Achivement")
    nrx_achieve = fields.Float(stirng="nrx Achieve %")
    nrx_ytd_churn = fields.Float(string="nrx YTD Churn")
    nrx_ytd_downgrade = fields.Float(string="nrx YTD Downgrade")
    nrx_ytd_net_increase = fields.Float(string="nrx YTD Net Increase")
    nrx_ytd_rev_growth = fields.Float(string="nrx YTD Rev Growth")

    total_number_of_customer = fields.Integer('Total Number Customer', compute="_total_number_customers")
    total_revenue_month = fields.Float('Total Revenue/Month', compute="_total_revenue_month")
    total_arpu = fields.Float('Total ARPU', compute="_total_arpu")
    total_number_of_service = fields.Integer('Total Number of Customer', compute="_total_number_of_service")
    total_ob_quota = fields.Integer('Total OB Quota', compute="_total_ob_quota")
    total_ytd_achivement = fields.Float('Total YTD Achievement', compute="_total_ytd_achivement")
    total_achieve = fields.Float('Total Achieve%', compute="_total_achieve")
    total_ytd_churn = fields.Float('Total YTD Churn', compute="_total_ytd_churn")
    total_ytd_downgrade = fields.Float('Total YTD Downgrade', compute="_total_ytd_downgrade")
    total_ytd_net_increase = fields.Float('Total YTD Net Increase', compute="_total_ytd_net_increase")
    total_ytd_rev_growth = fields.Float('Total YTD Rev Growth', compute="_total_ytd_rev_growth")

    #count number of customer di Menu customer (setting=>Customer Summary)
    @api.depends('total_number_of_customer')
    def _total_number_customers(self):
        self.total_number_of_customer = self.hos_number_of_customer + self.hrb_number_of_customer + self.itemb_number_of_customer + self.nrx_number_of_customer

    #count revenue/month di Menu customer (setting=>Customer Summary)
    @api.depends('total_revenue_month')
    def _total_revenue_month(self):
        self.total_revenue_month = self.hos_revenue_month + self.hrb_revenue_month + self.itemb_revenue_month + self.nrx_revenue_month

    #count ARPU di Menu customer (setting=>Customer Summary)
    @api.depends('total_arpu')
    def _total_arpu(self):
        self.total_arpu = self.total_revenue_month / self.total_number_of_customer
    
    #count number of service di Menu customer (setting=>Customer Summary) 
    @api.depends('total_number_of_service')
    def _total_number_of_service(self):
        self.total_number_of_service = self.hos_number_of_service + self.hrb_number_of_service + self.itemb_number_of_service + self.nrx_number_of_service

    #count OB Quota di Menu customer (setting=>Customer Summary)
    @api.depends('total_ob_quota')
    def _total_ob_quota(self):
        self.total_ob_quota = self.hos_ob_quota + self.hrb_ob_quota + self.itemb_ob_quota + self.nrx_ob_quota

    #count YTD Achievement di Menu customer (setting=>Customer Summary)
    @api.depends('total_ytd_achivement')
    def _total_ytd_achivement(self):
        self.total_ytd_achivement = self.hos_ytd_achivement + self.hrb_ytd_achivement + self.itemb_ytd_achivement + self.nrx_ytd_achivement

    #count achieve% di Menu customer (setting=>Customer Summary)
    @api.depends('total_achieve')
    def _total_achieve(self):
        self.total_achieve = self.hos_achieve + self.hrb_achieve + self.itemb_achieve + self.nrx_achieve

    #count YTD Churn di Menu customer (setting=>Customer Summary)
    @api.depends('total_ytd_churn')
    def _total_ytd_churn(self):
        self.total_ytd_churn = self.hos_ytd_churn + self.hrb_ytd_churn + self.itemb_ytd_churn + self.nrx_ytd_churn

    #count YTD Downgrade di Menu customer (setting=>Customer Summary)
    @api.depends('total_ytd_downgrade')
    def _total_ytd_downgrade(self):
        self.total_ytd_downgrade = self.hos_ytd_downgrade + self.hrb_ytd_downgrade + self.itemb_ytd_downgrade + self.nrx_ytd_downgrade
    
    #count YTD Net Increase di Menu customer (setting=>Customer Summary)
    @api.depends('total_ytd_net_increase')
    def _total_ytd_net_increase(self):
        self.total_ytd_net_increase = self.hos_ytd_net_increase + self.hrb_ytd_net_increase + self.itemb_ytd_net_increase + self.nrx_ytd_net_increase

    #count rev growth di Menu customer (setting=>Customer Summary)
    @api.depends('total_ytd_rev_growth')
    def _total_ytd_rev_growth(self):
        self.total_ytd_rev_growth = self.hos_ytd_rev_growth + self.hrb_ytd_rev_growth + self.itemb_ytd_rev_growth + self.nrx_ytd_rev_growth


class velo_potential_summary(models.Model):
    _name = 'potential.summary'
    _description = 'Model potential Summary'
    _rec_name = 'id'

    #count number of customer di Menu customer (setting=>Potential Summary)
    @api.model
    def _number_of_customer(self):
        hos_customer = self.env['res.partner'].search([('industry.id','=', self.hos_name.id),('tenant','=', False),('customer_rank','>', 0)])
        hrb_customer = self.env['res.partner'].search([('industry.id','=', self.hrb_name.id),('tenant','=', False),('customer_rank','>', 0)])
        itemb_customer = self.env['res.partner'].search([('industry.id','=', self.itemb_name.id),('tenant','=', False),('customer_rank','>', 0)])
        nrx_customer = self.env['res.partner'].search([('industry.id','=', self.nrx_name.id),('tenant','=', False),('customer_rank','>', 0)])
        for i in self:
            i.hos_number_of_customer = len(hos_customer)
            i.hrb_number_of_customer = len(hrb_customer)
            i.itemb_number_of_customer = len(itemb_customer)
            i.nrx_number_of_customer = len(nrx_customer)

    #count number of potential di Menu customer (setting=>Potential Summary)
    @api.model
    def _number_of_potential(self):
        hos_potential = self.env['res.partner'].search([('industry.id','=', self.hos_name.id),('tenant','=', True),('customer_rank','>', 0)])
        hrb_potential = self.env['res.partner'].search([('industry.id','=', self.hrb_name.id),('tenant','=', True),('customer_rank','>', 0)])
        itemb_potential = self.env['res.partner'].search([('industry.id','=', self.itemb_name.id),('tenant','=', True),('customer_rank','>', 0)])
        nrx_potential = self.env['res.partner'].search([('industry.id','=', self.nrx_name.id),('tenant','=', True),('customer_rank','>', 0)])
        for i in self:
            i.hos_number_of_potential = len(hos_potential)
            i.hrb_number_of_potential = len(hrb_potential)
            i.itemb_number_of_potential = len(itemb_potential)
            i.nrx_number_of_potential = len(nrx_potential)

    #count penetration (HOS) di Menu customer (setting=>Potential Summary)
    @api.depends('hos_number_of_customer','hos_number_of_potential')
    def _sum_penetration_potential_hos(self):
        for i in self:
            if i.hos_number_of_customer == 0:
                i.hos_penetration = 0
            elif i.hos_number_of_potential == 0:
                i.hos_penetration = 0
            else:
                i.hos_penetration = (i.hos_number_of_customer / i.hos_number_of_potential) * 100
    
    #count penetration (HRB) di Menu customer (setting=>Potential Summary)
    @api.depends('hrb_number_of_customer','hrb_number_of_potential')
    def _sum_penetration_potential_hrb(self):
        for i in self:
            if i.hrb_number_of_customer == 0:
                i.hrb_penetration = 0
            elif i.hrb_number_of_potential == 0:
                i.hrb_penetration = 0
            else:
                i.hrb_penetration = (i.hrb_number_of_customer / i.hrb_number_of_potential) * 100
    
    #count penetration (ITEMB) di Menu customer (setting=>Potential Summary)
    @api.depends('itemb_number_of_customer','itemb_number_of_potential')
    def _sum_penetration_potential_itemb(self):
        for i in self:
            if i.itemb_number_of_customer == 0:
                i.itemb_penetration = 0
            elif i.itemb_number_of_potential == 0:
                i.itemb_penetration = 0
            else:
                i.itemb_penetration = (i.itemb_number_of_customer / i.itemb_number_of_potential) * 100
    
    #count penetration (NRX) di Menu customer (setting=>Potential Summary)
    @api.depends('nrx_number_of_customer','nrx_number_of_potential')
    def _sum_penetration_potential_nrx(self):
        for i in self:
            if i.nrx_number_of_customer == 0:
                i.nrx_penetration = 0
            elif i.nrx_number_of_potential == 0:
                i.nrx_penetration = 0
            else:
                i.nrx_penetration = (i.nrx_number_of_customer / i.nrx_number_of_potential) * 100
    
    hos_name = fields.Many2one("pop.industry",string="HOS Name")
    hos_number_of_customer = fields.Integer('HOS Number of Customer', compute="_number_of_customer")
    hos_number_of_potential = fields.Integer(string="HOS Number of potential", compute="_number_of_potential")
    hos_penetration = fields.Float(string="HOS Penetration", compute="_sum_penetration_potential_hos")
    hos_tariff = fields.Float(string="HOS Tariff")
    hos_quota = fields.Integer(string="HOS Quota")
    hos_ytd_ob = fields.Float('HOS YTD OB')
    hos_ytd_achivement = fields.Float(string="HOS YTD Achivement")
    hos_sf_this_month = fields.Integer(stirng="HOS SF This Month")
    hos_mcfc_this_month = fields.Integer(string="HOS MCF-C This Month")
    hos_cold_leads = fields.Integer(string="HOS Cold Leads")
    
    hrb_name = fields.Many2one("pop.industry",string="HRB Name")
    hrb_number_of_customer = fields.Integer('HRB Number of Customer', compute="_number_of_customer")
    hrb_number_of_potential = fields.Integer(string="HRB Number of potential", compute="_number_of_potential")
    hrb_penetration = fields.Float(string="HRB Penetration", compute="_sum_penetration_potential_hrb")
    hrb_tariff = fields.Float(string="HRB Tariff")
    hrb_quota = fields.Integer(string="HRB Quota")
    hrb_ytd_ob = fields.Float('HRB YTD OB')
    hrb_ytd_achivement = fields.Float(string="HRB YTD Achivement")
    hrb_sf_this_month = fields.Integer(stirng="HRB SF This Month")
    hrb_mcfc_this_month = fields.Integer(string="HRB MCF-C This Month")
    hrb_cold_leads = fields.Integer(string="HRB Cold Leads")

    itemb_name = fields.Many2one("pop.industry",string="ITEMB Name")
    itemb_number_of_customer = fields.Integer('ITEMB Number of Customer', compute="_number_of_customer")
    itemb_number_of_potential = fields.Integer(string="ITEMB Number of potential", compute="_number_of_potential")
    itemb_penetration = fields.Float(string="ITEMB Penetration", compute="_sum_penetration_potential_itemb")
    itemb_tariff = fields.Float(string="ITEMB Tariff")
    itemb_quota = fields.Integer(string="ITEMB Quota")
    itemb_ytd_ob = fields.Float('ITEMB YTD OB')
    itemb_ytd_achivement = fields.Float(string="ITEMB YTD Achivement")
    itemb_sf_this_month = fields.Integer(stirng="ITEMB SF This Month")
    itemb_mcfc_this_month = fields.Integer(string="ITEMB MCF-C This Month")
    itemb_cold_leads = fields.Integer(string="ITEMB Cold Leads")

    nrx_name = fields.Many2one("pop.industry",string="NRX Name")
    nrx_number_of_customer = fields.Integer('NRX Number of Customer', compute="_number_of_customer")
    nrx_number_of_potential = fields.Integer(string="NRX Number of potential", compute="_number_of_potential")
    nrx_penetration = fields.Float(string="NRX Penetration", compute="_sum_penetration_potential_nrx")
    nrx_tariff = fields.Float(string="NRX Tariff")
    nrx_quota = fields.Integer(string="NRX Quota")
    nrx_ytd_ob = fields.Float('NRX YTD OB')
    nrx_ytd_achivement = fields.Float(string="NRX YTD Achivement")
    nrx_sf_this_month = fields.Integer(stirng="NRX SF This Month")
    nrx_mcfc_this_month = fields.Integer(string="NRX MCF-C This Month")
    nrx_cold_leads = fields.Integer(string="NRX Cold Leads")

    total_pot_number_of_customer = fields.Integer('Total Number of Customer', compute="_total_pot_number_of_customer")
    total_pot_number_of_potential = fields.Integer('Total Number of potential', compute="_total_pot_number_of_potential")
    total_pot_penetration = fields.Float('Total Penetration', compute="_total_pot_penetration")
    total_pot_tariff = fields.Float('Total Tariff', compute="_total_pot_tariff")
    total_pot_quota = fields.Integer('Total Quota', compute="_total_pot_quota")
    total_pot_ytd_ob = fields.Float('NRX YTD OB', compute="_total_pot_ytd_ob")
    total_pot_ytd_achivement = fields.Float('NRX YTD Achivement', compute="_total_pot_ytd_achivement")
    total_pot_sf_this_month = fields.Integer('NRX SF This Month', compute="_total_pot_sf_this_month")
    total_pot_mcfc_this_month = fields.Integer('NRX MCF-C This Month', compute="_total_pot_mcfc_this_month")
    total_pot_cold_leads = fields.Integer('NRX Cold Leads', compute="_total_pot_cold_leads")

    #count total number of customer di Menu customer (setting=>Potential Summary)
    @api.depends('total_pot_number_of_customer')
    def _total_pot_number_of_customer(self):
        self.total_pot_number_of_customer = self.hos_number_of_customer + self.hrb_number_of_customer + self.itemb_number_of_customer + self.nrx_number_of_customer

    #count total number of potential di Menu customer (setting=>Potential Summary)
    @api.depends('total_pot_number_of_potential')
    def _total_pot_number_of_potential(self):
        self.total_pot_number_of_potential = self.hos_number_of_potential + self.hrb_number_of_potential + self.itemb_number_of_potential + self.nrx_number_of_potential

    #count total penetration di Menu customer (setting=>Potential Summary)
    @api.depends('total_pot_number_of_customer','total_pot_number_of_potential')
    def _total_pot_penetration(self):
        for i in self:
            if i.total_pot_number_of_customer == 0:
                i.total_pot_penetration = 0
            elif i.total_pot_number_of_potential == 0:
                i.total_pot_penetration = 0
            else:
                i.total_pot_penetration = (i.total_pot_number_of_customer / i.total_pot_number_of_potential) *100

    #count total tariff di Menu customer (setting=>Potential Summary)
    @api.depends('total_pot_tariff')
    def _total_pot_tariff(self):
        self.total_pot_tariff = self.hos_tariff + self.hrb_tariff + self.itemb_tariff + self.nrx_tariff

    #count total quota di Menu customer (setting=>Potential Summary)
    @api.depends('total_pot_quota')
    def _total_pot_quota(self):
        self.total_pot_quota = self.hos_quota + self.hrb_quota + self.itemb_quota + self.nrx_quota
    
    #count total ytd ob di Menu customer (setting=>Potential Summary)
    @api.depends('total_pot_ytd_ob')
    def _total_pot_ytd_ob(self):
        self.total_pot_ytd_ob = self.hos_ytd_ob + self.hrb_ytd_ob + self.itemb_ytd_ob + self.nrx_ytd_ob
    
    #count total ytd achievement di Menu customer (setting=>Potential Summary)
    @api.depends('total_pot_ytd_achivement')
    def _total_pot_ytd_achivement(self):
        self.total_pot_ytd_achivement = self.hos_ytd_achivement + self.hrb_ytd_achivement + self.itemb_ytd_achivement + self.nrx_ytd_achivement
    
    #count total sf this month di Menu customer (setting=>Potential Summary)
    @api.depends('total_pot_sf_this_month')
    def _total_pot_sf_this_month(self):
        self.total_pot_sf_this_month = self.hos_sf_this_month + self.hrb_sf_this_month + self.itemb_sf_this_month + self.nrx_sf_this_month

    #count total mcfc this month di Menu customer (setting=>Potential Summary)
    @api.depends('total_pot_mcfc_this_month')
    def _total_pot_mcfc_this_month(self):
        self.total_pot_mcfc_this_month = self.hos_mcfc_this_month + self.hrb_mcfc_this_month + self.itemb_mcfc_this_month + self.nrx_mcfc_this_month

    #count total cold leads di Menu customer (setting=>Potential Summary)
    @api.depends('total_pot_cold_leads')
    def _total_pot_cold_leads(self):
        self.total_pot_cold_leads = self.hos_cold_leads + self.hrb_cold_leads + self.itemb_cold_leads + self.nrx_cold_leads


class pic_am(models.Model):
    _name = 'pic.am'
    _description = "PIC Account Manager"
    _inherit = ['pop.pic', 'pic.manager', 'pop.service.coverage']

    pic_am_id = fields.Many2one('pop.pic', string="AM Name")
    pic_am_pic_summary_of_specific_industry = fields.Many2one(related='pic_am_id.pic_summary_of_specific_industry', string="Specific Industry")
    pic_am_pic_period = fields.Date(related='pic_am_id.pic_period', string="Period")
    pic_am_pic_am_manager = fields.Many2one(related='pic_am_id.pic_am_manager', string="Manager In Charge")
    pic_am_total_rowcount_name_pic = fields.Integer(related="pic_am_id.total_rowcount_name_pic", string="Total Pop/Cluster")
    pic_am_pic_number_of_customer = fields.Integer(related="pic_am_id.pic_number_of_customer", string="Total Customer")
    pic_am_pic_number_of_potential = fields.Integer(related="pic_am_id.pic_number_of_potential",string="Total Potential")
    pic_am_pic_current_penetration = fields.Float(related="pic_am_id.pic_current_penetration", string="Total Penetration")
    pic_am_pic_monthly_tarif = fields.Integer(related="pic_am_id.pic_monthly_tarif", string="Total Monthly Tariff", store=False)
    pic_am_pic_number_of_arpu = fields.Integer(related="pic_am_id.pic_number_of_arpu", string="ARPU")
    pic_am_pic_annual_quota = fields.Integer(related="pic_am_id.pic_annual_quota", string="Annual Quota")
    pic_am_pic_quota_this_month = fields.Integer(related="pic_am_id.pic_quota_this_month", string="OB This Month")
    pic_am_pic_ytd_achievement = fields.Float(related="pic_am_id.pic_ytd_achievement", string="YTD Achievement")
    pic_am_pic_mcfc_this_month = fields.Integer(related="pic_am_id.pic_mcfc_this_month", string="MCF-C This Month")
    pic_am_pic_sf_this_month = fields.Integer(related="pic_am_id.pic_sf_this_month", string="SF This Month")
    pic_am_pic_cold_leads = fields.Integer(related="pic_am_id.pic_cold_leads", strin="Cold Leads")

    pic_am_service_coverage_ids = fields.One2many(related="pic_am_id.service_coverage_ids", string="Service Coverage ID")
    pic_am_partner_ids = fields.One2many(related="pic_am_id.pic_partner_ids", strring="PIC Customer")
    pic_am_ytd_achievement_ids = fields.One2many(related="pic_am_id.ytd_achievement_ids", string="YTD Achievement")
    pic_am_ytd_sales_focus = fields.One2many(related="pic_am_id.ytd_sales_focus", string="YTD Sales Focus")
    pic_am_ytd_mcfc_ids = fields.One2many(related="pic_am_id.ytd_mcfc_ids", string="YTD MCF-C")
    pic_am_ytd_cold_leads_ids = fields.One2many(related="pic_am_id.ytd_cold_leads_ids", string="YTD Cold Leads")
    
    # def pic_am_print(self):
    #     print(self.pic_am_id)