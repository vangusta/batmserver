# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request
from odoo.exceptions import Warning, UserError

class velo_current_issue(models.Model):
    _name = 'current.issue'
    _description = 'Model Menu current issue'

    name = fields.Char(string="Name")

class velo_price_issue(models.Model):
    _name = 'price.issue'
    _description = 'Model Menu price issue'

    name = fields.Char(string="Name")
    value = fields.Float(string="Value")

class velo_retention_category(models.Model):
    _name = 'retention.category'
    _description = 'Model Menu Retention Category'

    name = fields.Char(string="Name")
    tipe = fields.Selection([('survival','Survival'),('termination','Termination')],string="Tipe")

class velo_issue_category(models.Model):
    _name = 'issue.category'
    _description = 'Model Menu issue category'

    name = fields.Char(string="Name")

# class velo_workorder(models.Model):
#     _name = 'work.order'
#     _description = 'Model Workorder'

#     name = fields.Char(string="Name")
#     start_of_issue = fields.Date(string="Start Of Issue")
#     issue_category = fields.Many2one('issue.category', string="Issue Category")
#     industry_id = fields.Char(string="Industry Category")
#     industry_name = fields.Char(string="Industry Name")
#     company_name = fields.Char(string="Company Name")
#     contract_value = fields.Char(string="Contract Value")
#     product_code = fields.Char(string="Product Code")
#     product_name = fields.Char(string="Product Name")
#     service = fields.Char(string="Service")

class velo_retention_pipeline(models.Model):
    _name = 'retention.pipeline'
    _description = 'Model Menu Retention Pipeline'
    _rec_name = 'crf_no'

    def action_approve(self):
        if self.retention_category :
            if self.survival == True :
                self.state = 'survival'
                sale_vals = {
                    'partner_id': self.cust_name.id,
                }
                sales = request.env['sale.order'].sudo().create(sale_vals)

            if self.termination == True :
                self.state = 'termination'
        else :
            raise Warning('Retention Category empty !!')
    
    def action_proses_warm(self):
        self.state = 'b_warm_survival'
    
    def action_proses_hot(self):
        self.state = 'c_hot_survival'
    
    def action_proses_result(self):
        self.state = 'd_result'

    def action_iwo(self):
        self.state = 'wo'

    def action_dwo(self):
        self.state = 'wo'


    def action_termination(self):
        self.state = 'dwo'

    def action_survival(self):
        self.state = 'iwo'

    @api.model
    def create(self, values):
        record = super(velo_retention_pipeline, self).create(values);
        record['crf_no'] = self.env['ir.sequence'].next_by_code('velo.retention.seq') or '/'
        return record

    @api.onchange('cust_name')
    def _onchange_cust_name(self):
        if self.cust_name :
            self.cust_code = self.cust_name.id_object
            self.email = self.cust_name.email
            self.phone = self.cust_name.phone
            self.address = self.cust_name.street
            self.industry = self.cust_name.industry.id

    @api.onchange('current_service')
    def _onchange_current_service(self):
        if self.current_service :
            self.contact_person = self.current_service.user_id.id
            self.cust_period = self.current_service.date_start
            self.current_tarif = self.current_service.recurring_total

    @api.onchange('retention_category')
    def _onchange_survival(self):
        if self.retention_category.tipe == 'survival':
             self.survival = True
             self.termination = False
        else:
             self.survival = False
             self.termination = True


    crf_no = fields.Char(string="CRF. No")
    cust_code = fields.Char(string="Customer Code")
    cust_name = fields.Many2one('res.partner',string="Customer Name")
    iwo_related = fields.Many2one('order.iwo',string="IWO Related")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    address = fields.Char(string="Address")

    current_service = fields.Many2one('sale.subscription',string="Current Service")
    current_tarif = fields.Float(string="Current Tarif")
    contact_person = fields.Many2one('res.users',string="Contact Person")
    contract_period = fields.Date(string="Contract Period")

    effective_date = fields.Date(string="Efective Date")
    issue_category = fields.Many2one('issue.category',string="Facing Issues")
    retention_category = fields.Many2one('retention.category',string="Retention Result")

    # Survival
    survival = fields.Boolean(string='Survival')
    date_of_issue = fields.Date(string="Date Of Issue")
    price_issue = fields.Many2one('price.issue',string="Price Issue")
    reason = fields.Text(string="Reason")
    new_tarif_survival = fields.Float(string="New Tarif")
    new_service_survival = fields.Many2one('sale.subscription',string="New Service")
    gross_margin = fields.Float(string="Gross Margin")

    # renewal
    expire_date = fields.Date(string="Expire Date")
    current_issue = fields.Many2one('current.issue',string="Current Issue")
    new_tarif_renewal = fields.Float(string="New Tarif")
    new_service_renewal = fields.Many2one('sale.subscription',string="New Service")
    other_changes = fields.Float(string="Other Change")
    new_contract_date = fields.Date(string="New Contract Efective Date")

    # termination
    termination = fields.Boolean(string='Termination')
    request_date = fields.Date(string="Request Date")
    termination_date = fields.Date(string="Termination Date")
    reason_given = fields.Text(string="Reason Given")
    formal_respon = fields.Char(string="Formal Respon")

    latest_veloship = fields.Date(string="Latest Veloship")
    competitor_tarif = fields.Float(string="Competitor Tarif")
    new_tarif_proposed = fields.Float(string="New Tarif Proposed")
    new_service_proposed = fields.Many2one('sale.subscription',string="New Service Proposed")
    ytd_sla = fields.Char(string="YTD SLA")
    longest_outage = fields.Char(string="Longest Outage")
    action_taken_to_resolve_sla = fields.Char(string="Action taken to resolve SLA")

    start_of_issues = fields.Date(string="Start Of Issues", default=lambda self:fields.Datetime.now())
    industry = fields.Many2one('pop.industry' ,string="Industry")
    product = fields.Many2one('product.category' ,string="Product")
    state = fields.Selection([('a_cold_survival', 'Cold Survival'),
                              ('b_warm_survival', 'Warm Survival'),
                              ('c_hot_survival', 'Hot Survival'),
                              ('d_result', 'Retention Result')], string="State", default='a_cold_survival')
    negotiation_ids = fields.One2many('retention.negotiation','negotiation_id',string="Negotiation")


class velo_retention_negotiation(models.Model):
    _name = 'retention.negotiation'
    _description = 'Model Menu Retention negotiation'
    _rec_name = 'proposed_date'

    @api.onchange('tarif_proposed','selling_price')
    def _onchange_tarif_proposed(self):
        if self.tarif_proposed :
            self.selling_price = self.tarif_proposed;

    @api.onchange('upstream','local_loop','site_cost','cpe','marketing_associate','tarif_proposed','selling_price')
    def _onchange_total_cost(self):
        self.total_cost = self.upstream + self.local_loop + self.site_cost + self.cpe + self.marketing_associate;
        self.gross_profit = self.selling_price - self.total_cost;

        if self.gross_profit > 0 and  self.total_cost > 0:
            self.new_gp_persentage = int((self.gross_profit / self.total_cost)*100);



    negotiation_id = fields.Many2one('retention.pipeline',string='Negotiation')
    proposed_date = fields.Date(string='Proposed Date')
    service_proposed = fields.Char(string="Service Proposed")
    tarif_proposed = fields.Float(string="Tariff Proposed")
    new_service = fields.Float(string="New Service/Tarif Started")
    latest_veloship = fields.Char(string="Latest Veloship")
    competitor_name = fields.Char(string="Competitor Name")
    competitor_service = fields.Char(string="Competitor Service")
    competitor = fields.Char(string="Competitor")

    negotiation_category = fields.Many2one('negotiation.category',string='Negotiation Category')
    effective_date = fields.Date(string='Efective Date')
    new_gp_persentage = fields.Integer(string='New GP (%)')
    selling_price = fields.Float(string='Selling Price')
    upstream = fields.Float(string='upstream')
    local_loop = fields.Float(string='Local Loop')
    site_cost = fields.Float(string='Site Cost')
    cpe = fields.Float(string='CPE')
    marketing_associate = fields.Float(string='Marketing Associate')
    total_cost = fields.Float(string='Total Cost' )
    gross_profit = fields.Float(string='Gross Profit')

class velo_negotiation_category(models.Model):
    _name = 'negotiation.category'
    _description = 'Model negotiation category'

    name = fields.Char(string="Name")
