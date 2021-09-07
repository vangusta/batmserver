# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.http import request

class velo_contract_inherit(models.Model):
    _inherit = 'sale.subscription'
    _order = 'contract_date desc'

    @api.model
    def _product_code(self):
        for n in self:
            prod = ''
            cap = ''
            for m in n.recurring_invoice_line_ids :
                prod += str(m.product_code) + ' '
                if m.capacity :
                    cap += str(m.capacity) + ' '
            n.product_code = str(prod)
            n.capacity = str(cap)
    
    @api.model
    def _service_id(self):
        for n in self:
            serv = ''
            for m in n.recurring_invoice_line_ids:
                serv += str(m.service_id) + ' '
            n.service_id = str(serv)

    partner_id = fields.Many2one('res.partner', string='Customer Name', required=True, auto_join=True, domain="['&', ('customer_rank', '=', True), ('tenant', '=', False)]")
    pop_service_coverage_id = fields.Many2one('pop.service.coverage', string="POP ID", required=True)

    customer_id = fields.Char(related="partner_id.id_object", string="Customer ID")
    brand_id = fields.Many2one('brand.object', string="Brand")
    group_id = fields.Many2one('group.object', string="Group")
    pop_name = fields.Char(related="pop_service_coverage_id.pop_name", string="POP Name")
    industry = fields.Many2one('pop.industry', string="POP Industry")
    pic = fields.Char(related="partner_id.contact_name", string="PIC")
    #contract_capacity = fields.Char("Contract Capacity")

    contract_id = fields.Char(string="Contract ID")
    service_id = fields.Char(string="Service ID", compute="_service_id")
    contract_date = fields.Date(string="Contract Date", default=fields.Date.today)
    registration_date = fields.Date(string="Registration Date")
    act_date = fields.Date(string="Activation Date")
    iwo_date = fields.Date(string="IWO Date")
    termination_date = fields.Date(string="Termination Date")
    exp_date = fields.Date(string="Contract Expiry")
    contract_number = fields.Integer('Contract Number')
    act_fee = fields.Integer('Activation Fee')
    monthly_fee = fields.Integer('Monthly Fee')
    contract_period = fields.Char('Contract Period')
    contract_value = fields.Integer('Contract Value')
    contract_remark = fields.Text('Remark')

    service_product = fields.Many2one(
        'product.template', string="Service Product")
    service_location = fields.Many2one('pop.area', string="Service Location")

    product_code = fields.Char(string="Product ID", compute="_product_code")
    capacity = fields.Char(string="Capacity", compute="_product_code")
    serv_desc = fields.Text('Service Desctiption')

    address = fields.Char('Address')

    # @api.depends('recurring_invoice_line_ids')
    # def _total_contract_value(self):
    #     for a in self:
    #         a.contract_value = sum(line.price_subtotal for line in a.recurring_invoice_line_ids)

class pop_inherit(models.Model):
    _inherit = 'pop.service.coverage'

    pop_sale_subscription_ids = fields.One2many('sale.subscription','pop_service_coverage_id', string="POP Sale Subcsription")


    # @api.depends('pop_sale_subscription_ids')
    # def _total_monthly_tariff(self):
    #     for a in self:
    #         a.pop_total_monthly_tariff = sum(line.recurring_total for line in a.pop_sale_subscription_ids)

    # @api.depends('pop_sale_subscription_ids')
    # def _total_arpu(self):
    #     for b in self:
    #         b.pop_total_monthly_tariff = sum(line.recurring_total for line in b.pop_sale_subscription_ids)
    #         if len(b.pop_sale_subscription_ids) == 0:
    #             b.pop_arpu = 0
    #         else:
    #             b.pop_arpu = b.pop_total_monthly_tariff / (len(b.pop_sale_subscription_ids))


class velo_contract_line_inherit(models.Model):
    _inherit = 'sale.subscription.line'

    @api.onchange('product_id_tmpl')
    def onchange_product_id_tmpl(self):
        product_tmpl_id = self.product_id_tmpl.id
        self.product_id = self.env['product.product'].search([('product_tmpl_id', '=', product_tmpl_id)])
        self.product_code = self.product_id_tmpl.product_code
        self.capacity = self.product_id_tmpl.capacity

    @api.onchange('product_code')
    def onchange_product_code(self):
        product_code = self.product_code
        product_tmpl = self.env['product.template'].search([('product_code', '=', product_code)])
        product_tmpl_id = product_tmpl.id
        self.product_id = self.env['product.product'].search([('product_tmpl_id', '=', product_tmpl_id)])
        self.product_id_tmpl = product_tmpl_id

    @api.model
    def create(self, values):
        product_code = values.get('product_code')
       

        product_tmpl = self.env['product.template'].search([('product_code', '=', product_code)])
        product_tmpl_id = product_tmpl.id
        product_ida = self.env['product.product'].search([('product_tmpl_id', '=', product_tmpl_id)])
        product_id = product_ida.id
        product_name = product_ida.name
        uom_id = product_tmpl.uom_id.id
        values['product_id_tmpl'] = product_tmpl_id
        values['product_id'] = product_id
        values['name'] = product_name
        values['uom_id'] = uom_id
        return super(velo_contract_line_inherit, self).create(values)

    price_unit = fields.Float(string='Unit Price', required=True, digits='Product Price')


    service_id = fields.Char(string="Service ID")
    product_id_tmpl = fields.Many2one(
        'product.template', string='Product', check_company=True,
        domain="[('recurring_invoice','=',True)]")
    capacity = fields.Char(string="Capacity")

    product_id = fields.Many2one(
        'product.product', string='Product', check_company=True,
        domain="[('recurring_invoice','=',True)]")
    name = fields.Text(string='Description')
    product_code = fields.Char(string="Product ID")

    space = fields.Char(' ', readonly=True)

    act_date = fields.Date(related="analytic_account_id.act_date", string="Activation Date")
    exp_date = fields.Date(related="analytic_account_id.exp_date", string="Contract Expiry")
    term_date = fields.Date(related="analytic_account_id.termination_date", string="Termination Date")
    customer_id = fields.Char(related="analytic_account_id.partner_id.name", string="Customer Name")
    cust_id_object = fields.Char(related="analytic_account_id.customer_id", string="Customer ID")

    
