# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Inherit(models.Model):
    _inherit = 'product.template'
    _order = 'capacity asc'

    def product_quotation(self):
        active_id = self.id
        product_name = self.name
        product_tmpl_id = self.id
        product_id = self.env['product.product'].search([('product_tmpl_id', '=', product_tmpl_id)])


        ctx = {
            'default_model': 'sale.order.line',
            'default_res_id': self.id,
            'default_product_id': product_id.id,
        }

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'views': [(False, 'form')],
            'view_id': True,
            'target': 'new',
            'context': ctx,
        }

    #Graph Pricing Didepan
    def action_view_price_graph(self):
        action = self.env.ref('velo_product_pricing.action_product_validity_views').read()[0]
        action['domain'] = [('validity_id', '=', self.id)]
        action['target'] = 'new'
        action['view_mode'] = 'graph'
        action['views'] = [(False, 'graph')]
        action['view_id'] = True

        return action

    product_group = fields.Char('Product Group')
    product_code = fields.Char('Product ID')
    product_description = fields.Char('Product Description')
    capacity = fields.Integer('Capacity')
    product_availability = fields.Selection([
        ('All Region', 'All Region')], string="Availability")

    ip_address = fields.Char('IP Address')
    bandwith = fields.Char('Bandwith')

    space = fields.Char(' ', readonly=True)

    region = fields.Many2one(related='validity_ids.region', string="Region")
    list_price = fields.Float(
        'Sales Price', default=1.0,
        digits='Product Price',
        help="Price at which the product is sold to customers.",
        compute="_sum_monthly_fee",
        store=False) #
    
    monthly_fee = fields.Float('Mothly Fee', compute="_sum_monthly_fee")
    installation_fee = fields.Float('Installation Fee', compute="_sum_installation_fee")

    @api.depends('validity_ids')
    def _sum_monthly_fee(self):
        for a in self:
            monthly_fee = 0
            for line in a.validity_ids:
                if monthly_fee < 1 :
                    monthly_fee = line.monthly_tariff 

            a.monthly_fee = monthly_fee
            a.list_price = monthly_fee
    
    @api.depends('validity_ids')
    def _sum_installation_fee(self):
        for a in self:
            installation_fee = 0
            for line in a.validity_ids:
                if installation_fee < 1 :
                    installation_fee = line.installation_fee 

            a.installation_fee = installation_fee
    
    #Bali
    region_bali = fields.Many2one(related='validity_bali_ids.region', string="Region")
    validity_date_bali = fields.Date(related='validity_bali_ids.date_start', string="Validity")
    validity_date_bali_metro = fields.Date(related='validity_bali_metro_ids.date_start', string="Validity")
    validity_date_bali_nonmetro = fields.Date(related='validity_bali_nonmetro_ids.date_start', string="Validity")

    monthly_fee_bali = fields.Float('Mothly Fee', compute="_sum_monthly_fee_bali")
    monthly_fee_bali_metro = fields.Float('Mothly Fee', compute="_sum_monthly_fee_bali_metro")
    monthly_fee_bali_nonmetro = fields.Float('Mothly Fee', compute="_sum_monthly_fee_bali_nonmetro")
    
    installation_fee_bali_nonmetro = fields.Float('Installation Fee', compute="_sum_installation_fee_bali_nonmetro")

    mtti_bali = fields.Integer('MTTI', compute="_sum_mtti_bali")
    mtti_bali_nonmetro = fields.Integer('MTTI', compute="_sum_mtti_bali_nonmetro")

    @api.depends('validity_bali_ids')
    def _sum_mtti_bali(self):
        for a in self:
            mtti_bali = 0
            for line in a.validity_bali_ids:
                if mtti_bali < 1 :
                    mtti_bali = line.mtti

            a.mtti_bali = mtti_bali

    @api.depends('validity_bali_nonmetro_ids')
    def _sum_mtti_bali_nonmetro(self):
        for a in self:
            mtti_bali_nonmetro = 0
            for line in a.validity_bali_nonmetro_ids:
                if mtti_bali_nonmetro < 1 :
                    mtti_bali_nonmetro = line.mtti

            a.mtti_bali_nonmetro = mtti_bali_nonmetro

    validity_bali_ids = fields.One2many('product.validity', 'validity_id', string="Pricing Bali", domain=[('status','=', 1),('region','=', 'Bali')])
    validity_bali_metro_ids = fields.One2many('product.validity', 'validity_id', string="Pricing Bali Metro", domain=[('status','=', 1),('region','=', 'Bali'),('metroe','=', 'Metro')])
    validity_bali_nonmetro_ids = fields.One2many('product.validity', 'validity_id', string="Pricing Bali Non Metro", domain=[('status','=', 1),('region','=', 'Bali'),('metroe','=', 'Non Metro')])
    previous_bali_pricing_ids = fields.One2many('product.validity', 'validity_id', string="Product Description", domain=[('status', '=', 0),('region','=', 'Bali')])
    
    #Monthly fee Bali
    @api.depends('validity_bali_ids')
    def _sum_monthly_fee_bali(self):
        for a in self:
            monthly_fee_bali = 0
            for line in a.validity_bali_ids:
                if monthly_fee_bali < 1 :
                    monthly_fee_bali = line.monthly_tariff 

            a.monthly_fee_bali = monthly_fee_bali 
    
    @api.depends('validity_bali_metro_ids')
    def _sum_monthly_fee_bali_metro(self):
        for a in self:
            monthly_fee_bali_metro = 0
            for line in a.validity_bali_metro_ids:
                if monthly_fee_bali_metro < 1 :
                    monthly_fee_bali_metro = line.monthly_tariff 

            a.monthly_fee_bali_metro = monthly_fee_bali_metro

    @api.depends('validity_bali_nonmetro_ids')
    def _sum_monthly_fee_bali_nonmetro(self):
        for a in self:
            monthly_fee_bali_nonmetro = 0
            for line in a.validity_bali_nonmetro_ids:
                if monthly_fee_bali_nonmetro < 1 :
                    monthly_fee_bali_nonmetro = line.monthly_tariff 

            a.monthly_fee_bali_nonmetro = monthly_fee_bali_nonmetro
    
    #Installation Fee
    @api.depends('validity_bali_nonmetro_ids')
    def _sum_installation_fee_bali_nonmetro(self):
        for a in self:
            installation_fee_bali_nonmetro = 0
            for line in a.validity_bali_nonmetro_ids:
                if installation_fee_bali_nonmetro < 1 :
                    installation_fee_bali_nonmetro = line.installation_fee 

            a.installation_fee_bali_nonmetro = installation_fee_bali_nonmetro
    
    #Jakarta
    region_jakarta = fields.Many2one(related='validity_jakarta_ids.region', string="Region")
    validity_date_jakarta = fields.Date(related='validity_jakarta_ids.date_start', string="Validity")
    validity_date_jakarta_metro = fields.Date(related='validity_jakarta_metro_ids.date_start', string="Validity")
    validity_date_jakarta_nonmetro = fields.Date(related='validity_jakarta_nonmetro_ids.date_start', string="Validity")

    monthly_fee_jakarta = fields.Float('Mothly Fee', compute="_sum_monthly_fee_jakarta")
    monthly_fee_jakarta_metro = fields.Float('Mothly Fee', compute="_sum_monthly_fee_jakarta_metro")
    monthly_fee_jakarta_nonmetro = fields.Float('Mothly Fee', compute="_sum_monthly_fee_jakarta_nonmetro")
    
    installation_fee_jakarta_nonmetro = fields.Float('Installation Fee', compute="_sum_installation_fee_jakarta_nonmetro")

    mtti_jakarta = fields.Integer('MTTI', compute="_sum_mtti_jakarta")
    mtti_jakarta_nonmetro = fields.Integer('MTTI', compute="_sum_mtti_jakarta_nonmetro")

    @api.depends('validity_jakarta_ids')
    def _sum_mtti_jakarta(self):
        for a in self:
            mtti_jakarta = 0
            for line in a.validity_jakarta_ids:
                if mtti_jakarta < 1 :
                    mtti_jakarta = line.mtti

            a.mtti_jakarta = mtti_jakarta

    @api.depends('validity_jakarta_nonmetro_ids')
    def _sum_mtti_jakarta_nonmetro(self):
        for a in self:
            mtti_jakarta_nonmetro = 0
            for line in a.validity_jakarta_nonmetro_ids:
                if mtti_jakarta_nonmetro < 1 :
                    mtti_jakarta_nonmetro = line.mtti

            a.mtti_jakarta_nonmetro = mtti_jakarta_nonmetro

    validity_jakarta_ids = fields.One2many('product.validity', 'validity_id', string="Pricing Jakarta", domain=[('status','=', 1),('region','=', 'Jakarta')])
    validity_jakarta_metro_ids = fields.One2many('product.validity', 'validity_id', string="Pricing Jakarta Metro", domain=[('status','=', 1),('region','=', 'Jakarta'),('metroe','=', 'Metro')])
    validity_jakarta_nonmetro_ids = fields.One2many('product.validity', 'validity_id', string="Pricing Jakarta Non Metro", domain=[('status','=', 1),('region','=', 'Jakarta'),('metroe','=', 'Non Metro')])
    previous_jakarta_pricing_ids = fields.One2many('product.validity', 'validity_id', string="Product Description", domain=[('status', '=', 0),('region','=', 'Jakarta')])
    
    #Monthly fee Jakarta
    @api.depends('validity_jakarta_ids')
    def _sum_monthly_fee_jakarta(self):
        for a in self:
            monthly_fee_jakarta = 0
            for line in a.validity_jakarta_ids:
                if monthly_fee_jakarta < 1 :
                    monthly_fee_jakarta = line.monthly_tariff 

            a.monthly_fee_jakarta = monthly_fee_jakarta 
    
    @api.depends('validity_jakarta_metro_ids')
    def _sum_monthly_fee_jakarta_metro(self):
        for a in self:
            monthly_fee_jakarta_metro = 0
            for line in a.validity_jakarta_metro_ids:
                if monthly_fee_jakarta_metro < 1 :
                    monthly_fee_jakarta_metro = line.monthly_tariff 

            a.monthly_fee_jakarta_metro = monthly_fee_jakarta_metro

    @api.depends('validity_jakarta_nonmetro_ids')
    def _sum_monthly_fee_jakarta_nonmetro(self):
        for a in self:
            monthly_fee_jakarta_nonmetro = 0
            for line in a.validity_jakarta_nonmetro_ids:
                if monthly_fee_jakarta_nonmetro < 1 :
                    monthly_fee_jakarta_nonmetro = line.monthly_tariff 

            a.monthly_fee_jakarta_nonmetro = monthly_fee_jakarta_nonmetro
    
    #Installation Fee
    @api.depends('validity_jakarta_nonmetro_ids')
    def _sum_installation_fee_jakarta_nonmetro(self):
        for a in self:
            installation_fee_jakarta_nonmetro = 0
            for line in a.validity_jakarta_nonmetro_ids:
                if installation_fee_jakarta_nonmetro < 1 :
                    installation_fee_jakarta_nonmetro = line.installation_fee 

            a.installation_fee_jakarta_nonmetro = installation_fee_jakarta_nonmetro

    #Bandung
    region_bandung = fields.Many2one(related='validity_bandung_nonmetro_ids.region', string="Region")
    validity_date_bandung_nonmetro = fields.Date(related='validity_bandung_nonmetro_ids.date_start', string="Validity")

    monthly_fee_bandung_nonmetro = fields.Float('Mothly Fee', compute="_sum_monthly_fee_bandung_nonmetro")
    
    installation_fee_bandung_nonmetro = fields.Float('Installation Fee', compute="_sum_installation_fee_bandung_nonmetro")

    mtti_bandung_nonmetro = fields.Integer('MTTI', compute="_sum_mtti_bandung_nonmetro")

    @api.depends('validity_bandung_nonmetro_ids')
    def _sum_mtti_bandung_nonmetro(self):
        for a in self:
            mtti_bandung_nonmetro = 0
            for line in a.validity_bandung_nonmetro_ids:
                if mtti_bandung_nonmetro < 1 :
                    mtti_bandung_nonmetro = line.mtti

            a.mtti_bandung_nonmetro = mtti_bandung_nonmetro

    validity_bandung_nonmetro_ids = fields.One2many('product.validity', 'validity_id', string="Pricing Bandung Non Metro", domain=[('status','=', 1),('region','=', 'Bandung'),('metroe','=', 'Non Metro')])
    previous_bandung_pricing_ids = fields.One2many('product.validity', 'validity_id', string="Product Description", domain=[('status', '=', 0),('region','=', 'Bandung')])
    
    @api.depends('validity_bandung_nonmetro_ids')
    def _sum_monthly_fee_bandung_nonmetro(self):
        for a in self:
            monthly_fee_bandung_nonmetro = 0
            for line in a.validity_bandung_nonmetro_ids:
                if monthly_fee_bandung_nonmetro < 1 :
                    monthly_fee_bandung_nonmetro = line.monthly_tariff 

            a.monthly_fee_bandung_nonmetro = monthly_fee_bandung_nonmetro
    
    #Installation Fee
    @api.depends('validity_bandung_nonmetro_ids')
    def _sum_installation_fee_bandung_nonmetro(self):
        for a in self:
            installation_fee_bandung_nonmetro = 0
            for line in a.validity_bandung_nonmetro_ids:
                if installation_fee_bandung_nonmetro < 1 :
                    installation_fee_bandung_nonmetro = line.installation_fee 

            a.installation_fee_bandung_nonmetro = installation_fee_bandung_nonmetro
    
    #Semarang
    region_semarang = fields.Many2one(related='validity_semarang_nonmetro_ids.region', string="Region")
    validity_date_semarang_nonmetro = fields.Date(related='validity_semarang_nonmetro_ids.date_start', string="Validity")

    monthly_fee_semarang_nonmetro = fields.Float('Mothly Fee', compute="_sum_monthly_fee_semarang_nonmetro")
    
    installation_fee_semarang_nonmetro = fields.Float('Installation Fee', compute="_sum_installation_fee_semarang_nonmetro")

    mtti_semarang_nonmetro = fields.Integer('MTTI', compute="_sum_mtti_semarang_nonmetro")

    @api.depends('validity_semarang_nonmetro_ids')
    def _sum_mtti_semarang_nonmetro(self):
        for a in self:
            mtti_semarang_nonmetro = 0
            for line in a.validity_semarang_nonmetro_ids:
                if mtti_semarang_nonmetro < 1 :
                    mtti_semarang_nonmetro = line.mtti

            a.mtti_semarang_nonmetro = mtti_semarang_nonmetro

    validity_semarang_nonmetro_ids = fields.One2many('product.validity', 'validity_id', string="Pricing Semarang Non Metro", domain=[('status','=', 1),('region','=', 'Semarang'),('metroe','=', 'Non Metro')])
    previous_semarang_pricing_ids = fields.One2many('product.validity', 'validity_id', string="Product Description", domain=[('status', '=', 0),('region','=', 'Semarang')])
    
    @api.depends('validity_semarang_nonmetro_ids')
    def _sum_monthly_fee_semarang_nonmetro(self):
        for a in self:
            monthly_fee_semarang_nonmetro = 0
            for line in a.validity_semarang_nonmetro_ids:
                if monthly_fee_semarang_nonmetro < 1 :
                    monthly_fee_semarang_nonmetro = line.monthly_tariff 

            a.monthly_fee_semarang_nonmetro = monthly_fee_semarang_nonmetro
    
    #Installation Fee
    @api.depends('validity_semarang_nonmetro_ids')
    def _sum_installation_fee_semarang_nonmetro(self):
        for a in self:
            installation_fee_semarang_nonmetro = 0
            for line in a.validity_semarang_nonmetro_ids:
                if installation_fee_semarang_nonmetro < 1 :
                    installation_fee_semarang_nonmetro = line.installation_fee 

            a.installation_fee_semarang_nonmetro = installation_fee_semarang_nonmetro
    
    #Surabaya
    region_surabaya = fields.Many2one(related='validity_surabaya_nonmetro_ids.region', string="Region")
    validity_date_surabaya_nonmetro = fields.Date(related='validity_surabaya_nonmetro_ids.date_start', string="Validity")

    monthly_fee_surabaya_nonmetro = fields.Float('Mothly Fee', compute="_sum_monthly_fee_surabaya_nonmetro")
    
    installation_fee_surabaya_nonmetro = fields.Float('Installation Fee', compute="_sum_installation_fee_surabaya_nonmetro")

    mtti_surabaya_nonmetro = fields.Integer('MTTI', compute="_sum_mtti_surabaya_nonmetro")

    @api.depends('validity_surabaya_nonmetro_ids')
    def _sum_mtti_surabaya_nonmetro(self):
        for a in self:
            mtti_surabaya_nonmetro = 0
            for line in a.validity_surabaya_nonmetro_ids:
                if mtti_surabaya_nonmetro < 1 :
                    mtti_surabaya_nonmetro = line.mtti

            a.mtti_surabaya_nonmetro = mtti_surabaya_nonmetro

    validity_surabaya_nonmetro_ids = fields.One2many('product.validity', 'validity_id', string="Pricing Surabaya Non Metro", domain=[('status','=', 1),('region','=', 'Surabaya'),('metroe','=', 'Non Metro')])
    previous_surabaya_pricing_ids = fields.One2many('product.validity', 'validity_id', string="Product Description", domain=[('status', '=', 0),('region','=', 'Surabaya')])
    
    @api.depends('validity_surabaya_nonmetro_ids')
    def _sum_monthly_fee_surabaya_nonmetro(self):
        for a in self:
            monthly_fee_surabaya_nonmetro = 0
            for line in a.validity_surabaya_nonmetro_ids:
                if monthly_fee_surabaya_nonmetro < 1 :
                    monthly_fee_surabaya_nonmetro = line.monthly_tariff 

            a.monthly_fee_surabaya_nonmetro = monthly_fee_surabaya_nonmetro
    
    #Installation Fee
    @api.depends('validity_surabaya_nonmetro_ids')
    def _sum_installation_fee_surabaya_nonmetro(self):
        for a in self:
            installation_fee_surabaya_nonmetro = 0
            for line in a.validity_surabaya_nonmetro_ids:
                if installation_fee_surabaya_nonmetro < 1 :
                    installation_fee_surabaya_nonmetro = line.installation_fee 

            a.installation_fee_surabaya_nonmetro = installation_fee_surabaya_nonmetro
    
    #Yogyakarta
    region_yogyakarta = fields.Many2one(related='validity_yogyakarta_nonmetro_ids.region', string="Region")
    validity_date_yogyakarta_nonmetro = fields.Date(related='validity_yogyakarta_nonmetro_ids.date_start', string="Validity")

    monthly_fee_yogyakarta_nonmetro = fields.Float('Mothly Fee', compute="_sum_monthly_fee_yogyakarta_nonmetro")
    
    installation_fee_yogyakarta_nonmetro = fields.Float('Installation Fee', compute="_sum_installation_fee_yogyakarta_nonmetro")
    
    mtti_yogyakarta_nonmetro = fields.Integer('MTTI', compute="_sum_mtti_yogyakarta_nonmetro")

    @api.depends('validity_yogyakarta_nonmetro_ids')
    def _sum_mtti_yogyakarta_nonmetro(self):
        for a in self:
            mtti_yogyakarta_nonmetro = 0
            for line in a.validity_yogyakarta_nonmetro_ids:
                if mtti_yogyakarta_nonmetro < 1 :
                    mtti_yogyakarta_nonmetro = line.mtti

            a.mtti_yogyakarta_nonmetro = mtti_yogyakarta_nonmetro

    validity_yogyakarta_nonmetro_ids = fields.One2many('product.validity', 'validity_id', string="Pricing Yogyakarta Non Metro", domain=[('status','=', 1),('region','=', 'Yogyakarta'),('metroe','=', 'Non Metro')])
    previous_yogyakarta_pricing_ids = fields.One2many('product.validity', 'validity_id', string="Product Description", domain=[('status', '=', 0),('region','=', 'Yogyakarta')])
    
    @api.depends('validity_yogyakarta_nonmetro_ids')
    def _sum_monthly_fee_yogyakarta_nonmetro(self):
        for a in self:
            monthly_fee_yogyakarta_nonmetro = 0
            for line in a.validity_yogyakarta_nonmetro_ids:
                if monthly_fee_yogyakarta_nonmetro < 1 :
                    monthly_fee_yogyakarta_nonmetro = line.monthly_tariff 

            a.monthly_fee_yogyakarta_nonmetro = monthly_fee_yogyakarta_nonmetro
    
    #Installation Fee
    @api.depends('validity_yogyakarta_nonmetro_ids')
    def _sum_installation_fee_yogyakarta_nonmetro(self):
        for a in self:
            installation_fee_yogyakarta_nonmetro = 0
            for line in a.validity_yogyakarta_nonmetro_ids:
                if installation_fee_yogyakarta_nonmetro < 1 :
                    installation_fee_yogyakarta_nonmetro = line.installation_fee 

            a.installation_fee_yogyakarta_nonmetro = installation_fee_yogyakarta_nonmetro

    
    otc_hrb_metroe = fields.Float('OTC HRB/Metro-E')
    otc_standalone_non_metro = fields.Float('OTC StandAlone/Non-Metro')
    adhoc_ok = fields.Boolean('Ad Hoc Product', default=True)
    service_ids = fields.One2many('sale.subscription.line', 'product_id_tmpl', string="service", readonly=True)
    #total_tariff = fields.Float('Total Tariff' , compute="_total_ct" )
    total_customers = fields.Integer('Total Customers', compute="_count_customers", default=False, store=True)
    mtti = fields.Integer('MTTI', compute="_sum_mtti")

    @api.depends('validity_ids')
    def _sum_mtti(self):
        for a in self:
            # a.mtti = sum(line.mtti for line in a.validity_ids)
            mtti = 0
            for line in a.validity_ids:
                if mtti < 1 :
                    mtti = line.mtti

            a.mtti = mtti

    validity_date = fields.Date(related='validity_ids.date_start', string="Validity")
    
    total_product_sold = fields.Integer('Total Product Sold', compute="_count_total_product_sold")
    total_active_service = fields.Integer('Total Active Service', compute="_count_total_service", store=True)
    total_revenue = fields.Float('Total Revenue', compute="_total_revenue", store=True)
    arpu = fields.Float('ARPU', compute="_total_arpu")
    availability_count = fields.Integer('Availability', compute="_count_availability")

    validity_ids = fields.One2many('product.validity', 'validity_id', string="Pricing", domain=[('status','=', 1)])
    previous_pricing_ids = fields.One2many('product.validity', 'validity_id', string="Product Description", domain=[('status', '=', 0)])
    
    availability_ids = fields.Many2many('pop.service.coverage', string="Availability")
    categ_short_name = fields.Char(related='categ_id.short_name', string='Category Short Name' ,store=True)

    


    @api.depends('availability_ids')
    def _count_availability(self):
        for n in self:
           n.availability_count = len(n.availability_ids)

    @api.model
    def _count_total_product_sold(self):
        porduct_sold = self.env['sale.subscription.line'].search(
            [('product_id_tmpl', '=', self.name)])
        total_product = 0
        for m in porduct_sold:
            total_product +=  int(m.quantity)
        for i in self:
            i.total_product_sold = int(total_product)
    
    @api.depends('service_ids')
    def _count_total_service(self):
        for n in self:
           n.total_active_service = len(n.service_ids)
    
    @api.depends('service_ids')
    def _total_revenue(self):
        for a in self:
            a.total_revenue = sum(line.price_unit for line in a.service_ids)
    
    @api.depends('total_revenue','total_customers')
    def _total_arpu(self):
        for b in self:
            if b.total_revenue == 0:
                b.arpu = 0
            elif b.total_customers == 0:
                b.arpu = 0
            else:
                b.arpu = (b.total_revenue / b.total_customers)

    @api.depends('service_ids')
    def _count_customers(self):
        try:
            for i in self:
                customers = self.env['sale.subscription'].read_group (
                [('recurring_invoice_line_ids.product_id_tmpl.id', '=', i.id)], 
                fields = ['partner_id'], groupby = ['partner_id'])
                i.total_customers = int(len(customers))
        except:
            pass


class InheritVeloProgram(models.Model):
    _inherit = 'velo.program'
    
    product_ids = fields.Many2one('product.product')
    

class velo_pricing_summary(models.Model):
    _name = 'pricing.summary'
    _description = 'Pricing Summary'
    _rec_name = 'name'

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")

    metro_bali = fields.Integer('Metro Bali', compute="_metro_bali")
    non_metro_bali = fields.Integer('Non Metro Bali', compute="_non_metro_bali")

    metro_bandung = fields.Integer('Metro Bandung', compute="_metro_bandung")
    non_metro_bandung = fields.Integer('Non Metro Bali', compute="_non_metro_bandung")

    metro_jakarta = fields.Integer('Metro Jakarta', compute="_metro_jakarta")
    non_metro_jakarta = fields.Integer('Non Metro Bali', compute="_non_metro_jakarta")

    metro_semarang = fields.Integer('Metro Semarang', compute="_metro_semarang")
    non_metro_semarang = fields.Integer('Metro Bali', compute="_non_metro_semarang")

    metro_surabaya = fields.Integer('Metro Surabaya', compute="_metro_surabaya")
    non_metro_surabaya = fields.Integer('Non Metro Bali', compute="_non_metro_surabaya")

    metro_yogyakarta = fields.Integer('Metro Yogyakarta', compute="_metro_yogyakarta")
    non_metro_yogyakarta = fields.Integer('Non Metro Bali', compute="_non_metro_yogyakarta")

    @api.model
    def _metro_bali(self):
        metro_bali = self.env['product.validity'].search(
            [('region', '=', 'Bali'),('metroe', '=', 'Metro')])
        for i in self:
            i.metro_bali = len(metro_bali)

    @api.model
    def _non_metro_bali(self):
        non_metro_bali = self.env['product.validity'].search(
            [('region', '=', 'Bali'),('metroe', '=', 'Non Metro')])
        for i in self:
            i.non_metro_bali = len(non_metro_bali)
    
    @api.model
    def _metro_bandung(self):
        metro_bandung = self.env['product.validity'].search(
            [('region', '=', 'Bandung'),('metroe', '=', 'Metro')])
        for i in self:
            i.metro_bandung = len(metro_bandung)

    @api.model
    def _non_metro_bandung(self):
        non_metro_bandung = self.env['product.validity'].search(
            [('region', '=', 'Bandung'),('metroe', '=', 'Non Metro')])
        for i in self:
            i.non_metro_bandung = len(non_metro_bandung)

    @api.model
    def _metro_jakarta(self):
        metro_jakarta = self.env['product.validity'].search(
            [('region', '=', 'Jakarta'),('metroe', '=', 'Metro')])
        for i in self:
            i.metro_jakarta = len(metro_jakarta)

    @api.model
    def _non_metro_jakarta(self):
        non_metro_jakarta = self.env['product.validity'].search(
            [('region', '=', 'Jakarta'),('metroe', '=', 'Non Metro')])
        for i in self:
            i.non_metro_jakarta = len(non_metro_jakarta)

    @api.model
    def _metro_semarang(self):
        metro_semarang = self.env['product.validity'].search(
            [('region', '=', 'Semarang'),('metroe', '=', 'Metro')])
        for i in self:
            i.metro_semarang = len(metro_semarang)

    @api.model
    def _non_metro_semarang(self):
        non_metro_semarang = self.env['product.validity'].search(
            [('region', '=', 'Semarang'),('metroe', '=', 'Non Metro')])
        for i in self:
            i.non_metro_semarang = len(non_metro_semarang)
    
    @api.model
    def _metro_surabaya(self):
        metro_surabaya = self.env['product.validity'].search(
            [('region', '=', 'Surabaya'),('metroe', '=', 'Metro')])
        for i in self:
            i.metro_surabaya = len(metro_surabaya)

    @api.model
    def _non_metro_surabaya(self):
        non_metro_surabaya = self.env['product.validity'].search(
            [('region', '=', 'Surabaya'),('metroe', '=', 'Non Metro')])
        for i in self:
            i.non_metro_surabaya = len(non_metro_surabaya)
    
    @api.model
    def _metro_yogyakarta(self):
        metro_yogyakarta = self.env['product.validity'].search(
            [('region', '=', 'Yogyakarta'),('metroe', '=', 'Metro')])
        for i in self:
            i.metro_yogyakarta = len(metro_yogyakarta)

    @api.model
    def _non_metro_yogyakarta(self):
        non_metro_yogyakarta = self.env['product.validity'].search(
            [('region', '=', 'Yogyakarta'),('metroe', '=', 'Non Metro')])
        for i in self:
            i.non_metro_yogyakarta = len(non_metro_yogyakarta)


class velo_product_validity(models.Model):
    _name = 'product.validity'
    _description = 'Product Validity'
    _rec_name = 'validity_id'
    _order = 'sequence, id'
   

    def action_view_validity_graph(self):
        # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',self.region.id,self.metroe,self.hrb)
        action = self.env.ref('velo_product_pricing.action_product_graph_views').read()[0]
        action['domain'] = [('validity_id', '=', self.validity_id.id),('region', '=', self.region.id),('metroe', '=', self.metroe),('hrb', '=', self.hrb)]
        action['target'] = 'new'
        action['view_mode'] = 'graph'
        action['views'] = [(False, 'graph')]
        action['view_id'] = True
        action['graph_mode'] = 'line'

        return action

    space = fields.Char(' ', readonly=True)
    sequence = fields.Integer(string='Sequence', default=10)
    validity_id = fields.Many2one('product.template', string="Product Description")
    product_id = fields.Char(related="validity_id.product_code", string="Product ID")
    date = fields.Date(string="Date")
    metroe = fields.Selection([('Metro', 'Metro Velo'), ('Non Metro', 'Non Metro Velo')], string="(Non)Metro Velo")
    hrb = fields.Selection([('hrb', 'HRB'), ('nonhrb', 'Non HRB'), ('All POP', 'All POP')], string="Type of POP")
    region = fields.Many2one('pop.regional', string="Region")
    monthly_tariff = fields.Float(string="Monthly Tariff", group_operator=False)
    installation_fee = fields.Float(string="Installation Fee", group_operator=False)
    mtti = fields.Integer('MTTI', group_operator=False)
    date_start = fields.Date(string="Start Date", default=lambda self:fields.Datetime.now())
    date_end = fields.Date(string="End Date")
    status = fields.Boolean('Active', default=True)

class velo_product_summary(models.Model):
    _name = 'product.summary'
    _description = 'Product Summary'
    _rec_name = 'name'

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")

    velocity_sold_annual = fields.Integer('Velocity Sold Annual', compute="_velocity_sold_annual")
    velocity_tariff = fields.Float('Velocity Tariff', compute="_velocity_tariff")
    velocity_number_customer = fields.Integer('Velocity Number Customer', compute="_velocity_number_customer")
    velocity_available_product = fields.Integer('Velocity Available products', compute="_velocity_available_product")
    velocity_current_sf_potential = fields.Integer('Velocity Current SF - Potential', compute="_velocity_current_sf_potential")
    velocity_current_sf_tariff = fields.Integer('Velocity Current SF - Tariff', compute="_velocity_current_sf_tariff")
    velocity_arpu = fields.Float('ARPU', compute="_velocity_arpu")

    vraptor_sold_annual = fields.Integer('VRaptor Sold Annual', compute="_vraptor_sold_annual")
    vraptor_tariff = fields.Float('VRaptor Tariff', compute="_vraptor_tariff")
    vraptor_number_customer = fields.Integer('Vraptor Number Customer', compute="_vraptor_number_customer")
    vraptor_available_product = fields.Integer('vraptor Available products', compute="_vraptor_available_product")
    vraptor_current_sf_potential = fields.Integer('vraptor Current SF - Potential', compute="_vraptor_current_sf_potential")
    vraptor_current_sf_tariff = fields.Integer('vraptor Current SF - Tariff', compute="_vraptor_current_sf_tariff")
    vraptor_arpu = fields.Float('VRaptor ARPU', compute="_vraprtor_arpu")
 
    velocloud_sold_annual = fields.Integer('Velocloud Sold Annual', compute="_velocloud_sold_annual")
    velocloud_tariff = fields.Float('Velocloud Tariff', compute="_velocloud_tariff")
    velocloud_number_customer = fields.Integer('Velocloud Number Customer', compute="_velocloud_number_customer")
    velocloud_available_product = fields.Integer('velocloud Available products', compute="_velocloud_available_product")
    velocloud_current_sf_potential = fields.Integer('velocloud Current SF - Potential', compute="_velocloud_current_sf_potential")
    velocloud_current_sf_tariff = fields.Integer('velocloud Current SF - Tariff', compute="_velocloud_current_sf_tariff")
    velocloud_arpu = fields.Float('Velo Cloud ARPU', compute="_velocloud_arpu")

    velolink_sold_annual = fields.Integer('Velolink Sold Annual', compute="_velolink_sold_annual")
    velolink_tariff = fields.Float('Velolink Tariff', compute="_velolink_tariff")
    velolink_number_customer = fields.Integer('Velolink Number Customer', compute="_velolink_number_customer")
    velolink_available_product = fields.Integer('velolink Available products', compute="_velolink_available_product")
    velolink_current_sf_potential = fields.Integer('velolink Current SF - Potential', compute="_velolink_current_sf_potential")
    velolink_current_sf_tariff = fields.Integer('velolink Current SF - Tariff', compute="_velolink_current_sf_tariff")
    velolink_arpu = fields.Float('Velo Link ARPU', compute="_velolink_arpu")

    velonet_sold_annual = fields.Integer('Velonet Sold Annual', compute="_velonet_sold_annual")
    velonet_tariff = fields.Float('Velonet Tariff', compute="_velonet_tariff")
    velonet_number_customer = fields.Integer('Velonet Number_customer', compute="_velonet_number_customer")
    velonet_available_product = fields.Integer('velonet Available products', compute="_velonet_available_product")
    velonet_current_sf_potential = fields.Integer('velonet Current SF - Potential', compute="_velonet_current_sf_potential")
    velonet_current_sf_tariff = fields.Integer('velonet Current SF - Tariff', compute="_velonet_current_sf_tariff")
    velonet_arpu = fields.Float('Velonet ARPU', compute="_velonet_arpu")

    velo1solution_sold_annual = fields.Integer('Velo1Solution Sold Annual', compute="_velo1solution_sold_annual")
    velo1solution_tariff = fields.Float('Velo1Solution Tariff', compute="_velo1solution_tariff")
    velo1solution_number_customer = fields.Integer('Velo1Solution Number_customer', compute="_velo1solution_number_customer")
    velo1solution_available_product = fields.Integer('velo1solution Available products', compute="_velo1solution_available_product")
    velo1solution_current_sf_potential = fields.Integer('velo1solution Current SF - Potential', compute="_velo1solution_current_sf_potential")
    velo1solution_current_sf_tariff = fields.Integer('velo1solution Current SF - Tariff', compute="_velo1solution_current_sf_tariff")
    velo1solution_arpu = fields.Float('Velo 1solution ARPU', compute="_velo1solution_arpu")

    @api.depends('velocity_tariff','velocity_sold_annual')
    def _velocity_arpu(self):
        for i in self:
            if i.velocity_tariff == 0:
                i.velocity_arpu = 0
            else:
                i.velocity_arpu = i.velocity_tariff / i.velocity_sold_annual
    
    @api.depends('vraptor_tariff','vraptor_sold_annual')
    def _vraprtor_arpu(self):
        for i in self:
            if i.vraptor_tariff == 0:
                i.vraptor_arpu = 0
            else:
                i.vraptor_arpu = i.vraptor_tariff / i.vraptor_sold_annual

    @api.depends('velocloud_tariff','velocloud_sold_annual')
    def _velocloud_arpu(self):
        for i in self:
            if i.velocloud_tariff == 0:
                i.velocloud_arpu = 0
            else:
                i.velocloud_arpu = i.velocloud_tariff / i.velocloud_sold_annual

    @api.depends('velolink_tariff','velolink_sold_annual')
    def _velolink_arpu(self):
        for i in self:
            if i.velolink_tariff == 0:
                i.velolink_arpu = 0
            else:
                i.velolink_arpu = i.velolink_tariff / i.velolink_sold_annual
    
    @api.depends('velonet_tariff','velonet_sold_annual')
    def _velonet_arpu(self):
        for i in self:
            if i.velonet_tariff == 0:
                i.velonet_arpu = 0
            else:
                i.velonet_arpu = i.velonet_tariff / i.velonet_sold_annual

    @api.depends('velo1solution_tariff','velo1solution_sold_annual')
    def _velo1solution_arpu(self):
        for i in self:
            if i.velo1solution_tariff == 0:
                i.velo1solution_arpu = 0
            else:
                i.velo1solution_arpu = i.velo1solution_tariff / i.velo1solution_sold_annual
                
    @api.model
    def _velocity_sold_annual(self):
        annual = self.env['sale.subscription.line'].search(
            [('product_id_tmpl.categ_id.name', 'ilike', 'velocity')])
        total_product = 0
        for m in annual:
            total_product +=  int(m.quantity)
        for i in self:
            i.velocity_sold_annual = int(total_product)

    @api.model
    def _velocity_tariff(self):
        product = self.env['sale.subscription.line'].search(
            [('product_id_tmpl.categ_id.name', 'ilike', 'velocity')])
        total_val = 0
        for m in product:
            total_val +=  float(m.price_subtotal)
        for i in self:
            i.velocity_tariff = float(total_val)

    @api.model
    def _velocity_number_customer(self):
        customers = self.env['sale.subscription'].read_group (
            [('recurring_invoice_line_ids.product_id_tmpl.categ_id.name', 'ilike', 'velocity')], 
            fields = ['partner_id'], groupby = ['partner_id'])
        for i in self:
            i.velocity_number_customer = len(customers)


    @api.model
    def _velocity_available_product(self):
        products = self.env['product.template'].search([('categ_id.name','ilike', 'velocity')])
        for i in self:
            i.velocity_available_product = len(products)
    
    @api.model
    def _velocity_current_sf_potential(self):
        customers = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus'),('order_ids.order_line.product_template_id.categ_id.name','ilike', 'velocity')])
        for i in self:
            i.velocity_current_sf_potential = len(customers)


    @api.model
    def _velocity_current_sf_tariff(self):
        sale_line = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus'),('order_ids.order_line.product_template_id.categ_id.name','ilike', 'velocity')])
        tariff = 0
        for m in sale_line:
            tariff +=  float(m.order_ids.order_line.price_unit)
        for i in self:
            i.velocity_current_sf_tariff = float(tariff)
    
    @api.model
    def _vraptor_sold_annual(self):
        annual = self.env['sale.subscription.line'].search(
            [('product_id_tmpl.categ_id.name', 'ilike', 'vraptor')])
        total_product = 0
        for m in annual:
            total_product +=  int(m.quantity)
        for i in self:
            i.vraptor_sold_annual = int(total_product)

    @api.model
    def _vraptor_tariff(self):
        product = self.env['sale.subscription.line'].search(
            [('product_id_tmpl.categ_id.name', 'ilike', 'vraptor')])
        total_val = 0
        for m in product:
            total_val +=  float(m.price_subtotal)
        for i in self:
            i.vraptor_tariff = float(total_val)

    @api.model
    def _vraptor_number_customer(self):
        customers = self.env['sale.subscription'].read_group (
            [('recurring_invoice_line_ids.product_id_tmpl.categ_id.name', 'ilike', 'vraptor')], 
            fields = ['partner_id'], groupby = ['partner_id'])
        for i in self:
            i.vraptor_number_customer = len(customers)

    @api.model
    def _vraptor_available_product(self):
        products = self.env['product.template'].search([('categ_id.name','ilike', 'vraptor')])
        for i in self:
            i.vraptor_available_product = len(products)
    
    @api.model
    def _vraptor_current_sf_potential(self):
        customers = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus'),('order_ids.order_line.product_template_id.categ_id.name','ilike', 'vraptor')])
        for i in self:
            i.vraptor_current_sf_potential = len(customers)


    @api.model
    def _vraptor_current_sf_tariff(self):
        sale_line = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus'),('order_ids.order_line.product_template_id.categ_id.name','ilike', 'vraptor')])
        tariff = 0
        for m in sale_line:
            tariff +=  float(m.order_ids.order_line.price_unit)
        for i in self:
            i.vraptor_current_sf_tariff = float(tariff)    

    



    @api.model
    def _velocloud_sold_annual(self):
        annual = self.env['sale.subscription.line'].search(
            [('product_id_tmpl.categ_id.name', 'ilike', 'velocloud')])
        total_product = 0
        for m in annual:
            total_product +=  int(m.quantity)
        for i in self:
            i.velocloud_sold_annual = int(total_product)

    @api.model
    def _velocloud_tariff(self):
        product = self.env['sale.subscription.line'].search(
            [('product_id_tmpl.categ_id.name', 'ilike', 'velocloud')])
        total_val = 0
        for m in product:
            total_val +=  float(m.price_subtotal)
        for i in self:
            i.velocloud_tariff = float(total_val)

    @api.model
    def _velocloud_number_customer(self):
        customers = self.env['sale.subscription'].read_group (
            [('recurring_invoice_line_ids.product_id_tmpl.categ_id.name', 'ilike', 'velocloud')], 
            fields = ['partner_id'], groupby = ['partner_id'])
        for i in self:
            i.velocloud_number_customer = len(customers)

    @api.model
    def _velocloud_available_product(self):
        products = self.env['product.template'].search([('categ_id.name','ilike', 'velocloud')])
        for i in self:
            i.velocloud_available_product = len(products)
    
    @api.model
    def _velocloud_current_sf_potential(self):
        customers = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus'),('order_ids.order_line.product_template_id.categ_id.name','ilike', 'velocloud')])
        for i in self:
            i.velocloud_current_sf_potential = len(customers)


    @api.model
    def _velocloud_current_sf_tariff(self):
        sale_line = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus'),('order_ids.order_line.product_template_id.categ_id.name','ilike', 'velocloud')])
        tariff = 0
        for m in sale_line:
            tariff +=  float(m.order_ids.order_line.price_unit)
        for i in self:
            i.velocloud_current_sf_tariff = float(tariff)





    @api.model
    def _velolink_sold_annual(self):
        annual = self.env['sale.subscription.line'].search(
            [('product_id_tmpl.categ_id.name', 'ilike', 'velolink')])
        total_product = 0
        for m in annual:
            total_product +=  int(m.quantity)
        for i in self:
            i.velolink_sold_annual = int(total_product)

    @api.model
    def _velolink_tariff(self):
        product = self.env['sale.subscription.line'].search(
            [('product_id_tmpl.categ_id.name', 'ilike', 'velolink')])
        total_val = 0
        for m in product:
            total_val +=  float(m.price_subtotal)
        for i in self:
            i.velolink_tariff = float(total_val)

    @api.model
    def _velolink_number_customer(self):
        customers = self.env['sale.subscription'].read_group (
            [('recurring_invoice_line_ids.product_id_tmpl.categ_id.name', 'ilike', 'velolink')], 
            fields = ['partner_id'], groupby = ['partner_id'])
        for i in self:
            i.velolink_number_customer = len(customers)

    @api.model
    def _velolink_available_product(self):
        products = self.env['product.template'].search([('categ_id.name','ilike', 'velolink')])
        for i in self:
            i.velolink_available_product = len(products)
    
    @api.model
    def _velolink_current_sf_potential(self):
        customers = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus'),('order_ids.order_line.product_template_id.categ_id.name','ilike', 'velolink')])
        for i in self:
            i.velolink_current_sf_potential = len(customers)


    @api.model
    def _velolink_current_sf_tariff(self):
        sale_line = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus'),('order_ids.order_line.product_template_id.categ_id.name','ilike', 'velolink')])
        tariff = 0
        for m in sale_line:
            tariff +=  float(m.order_ids.order_line.price_unit)
        for i in self:
            i.velolink_current_sf_tariff = float(tariff)






    
    @api.model
    def _velonet_sold_annual(self):
        annual = self.env['sale.subscription.line'].search(
            [('product_id_tmpl.categ_id.name', 'ilike', 'velonet')])
        total_product = 0
        for m in annual:
            total_product +=  int(m.quantity)
        for i in self:
            i.velonet_sold_annual = int(total_product)

    @api.model
    def _velonet_tariff(self):
        product = self.env['sale.subscription.line'].search(
            [('product_id_tmpl.categ_id.name', 'ilike', 'velonet')])
        total_val = 0
        for m in product:
            total_val +=  float(m.price_subtotal)
        for i in self:
            i.velonet_tariff = float(total_val)

    @api.model
    def _velonet_number_customer(self):
        customers = self.env['sale.subscription'].read_group (
            [('recurring_invoice_line_ids.product_id_tmpl.categ_id.name', 'ilike', 'velonet')], 
            fields = ['partner_id'], groupby = ['partner_id'])
        for i in self:
            i.velonet_number_customer = len(customers)

    @api.model
    def _velonet_available_product(self):
        products = self.env['product.template'].search([('categ_id.name','ilike', 'velonet')])
        for i in self:
            i.velonet_available_product = len(products)
    
    @api.model
    def _velonet_current_sf_potential(self):
        customers = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus'),('order_ids.order_line.product_template_id.categ_id.name','ilike', 'velonet')])
        for i in self:
            i.velonet_current_sf_potential = len(customers)


    @api.model
    def _velonet_current_sf_tariff(self):
        sale_line = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus'),('order_ids.order_line.product_template_id.categ_id.name','ilike', 'velonet')])
        tariff = 0
        for m in sale_line:
            tariff +=  float(m.order_ids.order_line.price_unit)
        for i in self:
            i.velonet_current_sf_tariff = float(tariff)








    
    @api.model
    def _velo1solution_sold_annual(self):
        annual = self.env['sale.subscription.line'].search(
            [('product_id_tmpl.categ_id.name', 'ilike', 'ms')])
        total_product = 0
        for m in annual:
            total_product +=  int(m.quantity)
        for i in self:
            i.velo1solution_sold_annual = int(total_product)

    @api.model
    def _velo1solution_tariff(self):
        product = self.env['sale.subscription.line'].search(
            [('product_id_tmpl.categ_id.name', 'ilike', 'ms')])
        total_val = 0
        for m in product:
            total_val +=  float(m.price_subtotal)
        for i in self:
            i.velo1solution_tariff = float(total_val)

    @api.model
    def _velo1solution_number_customer(self):
        customers = self.env['sale.subscription'].read_group (
            [('recurring_invoice_line_ids.product_id_tmpl.categ_id.name', 'ilike', 'ms')], 
            fields = ['partner_id'], groupby = ['partner_id'])
        for i in self:
            i.velo1solution_number_customer = len(customers)

    @api.model
    def _velo1solution_available_product(self):
        products = self.env['product.template'].search([('categ_id.name','ilike', 'ms')])
        for i in self:
            i.velo1solution_available_product = len(products)
    
    @api.model
    def _velo1solution_current_sf_potential(self):
        customers = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus'),('order_ids.order_line.product_template_id.categ_id.name','ilike', 'ms')])
        for i in self:
            i.velo1solution_current_sf_potential = len(customers)


    @api.model
    def _velo1solution_current_sf_tariff(self):
        sale_line = self.env['crm.lead'].search([('stage_id.name','ilike', 'Sales Focus'),('order_ids.order_line.product_template_id.categ_id.name','ilike', 'ms')])
        tariff = 0
        for m in sale_line:
            tariff +=  float(m.order_ids.order_line.price_unit)
        for i in self:
            i.velo1solution_current_sf_tariff = float(tariff)


class Inherit(models.Model):
    _inherit = 'product.category'

    short_name = fields.Char('Short Name')