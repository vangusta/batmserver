# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PopMaster(models.Model):
    _name = 'pop.master'
    _description = 'Data POP Master'
    _rec_name = 'popname'

    popid = fields.Integer(string="POP ID")
    poptype = fields.Many2one('pop.type', string="POP TYPE")
    popname = fields.Char(string="POP Name")
    service_delivery = fields.Selection([('DIRECT', 'DIRECT'), ('INDIRECT', 'INDIRECT')], string="Service Delivery")
    provinsi = fields.Many2one('pop.regional', string="Provinsi")
    kabupaten = fields.Many2one('pop.area', string="Kabupaten", domain="[('area_id', '=', provinsi)]")
    longitude = fields.Float(string="Long")
    latitude = fields.Float(string="Lat")
    regionalhub = fields.Many2one('pop.hub.region', string="Regional HUB", domain="[('regionalhub_id', '=', provinsi)]")
    state = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string="Status")

class RegionalHub(models.Model):
    _name = 'pop.hub.region'
    _description = 'POP Regional Hub'
    _rec_name = 'regionalhub_name'

    regionalhub_name = fields.Char(string="Regional HUB Name")
    regionalhub_id = fields.Many2one('pop.regional', string="Regional Hub")

class PopType(models.Model):
    _name = 'pop.type'
    _description = 'POP Type'
    _rec_name = 'poptype_name'

    poptype_name = fields.Char(string="POP Type")
    poptype_description = fields.Text(string="Description")

class PopRegional(models.Model):
    _name = 'pop.regional'
    _description = 'POP Regional'
    _rec_name = 'pop_regional_name'

    pop_regional_name = fields.Char(string="POP Regional")
    pop_regional_id = fields.Char(string="POP Regional ID")
    pop_regional_description = fields.Text(string="Description")
    area_ids = fields.One2many('pop.area', 'area_id', string="Kabupaten")
    regionalhub_ids = fields.One2many('pop.hub.region', 'regionalhub_id', string="Region Hub")

class PopArea(models.Model):
    _name = 'pop.area'
    _description = 'POP Area'
    _rec_name = 'pop_area_name'

    pop_area_name = fields.Char(string="POP Area")
    pop_area_description = fields.Text(string="Description")
    area_id = fields.Many2one('pop.regional', string="Area ID")


class OverviewSummary(models.Model):
    _name = 'pop.overview.summary'
    _description = 'Overview Summary'
    _rec_name = 'overview_type'

    overview_type = fields.Many2one('pop.type', string="POP Type")
    overview_number_pop = fields.Integer(compute="_sum_number_pop", string="Number POP")
    sum_apt_pop = fields.Integer('APT Number POP', compute="_sum_apt_pop")
    sum_bws_pop = fields.Integer('BWS Number POP', compute="_sum_bws_pop")
    sum_dc_pop = fields.Integer('DC Number POP', compute="_sum_dc_pop")
    sum_fdc_pop = fields.Integer('FDC Number POP', compute="_sum_fdc_pop")
    sum_hrb_pop = fields.Integer('HRB Number POP', compute="_sum_hrb_pop")
    sum_noc_pop = fields.Integer('NOC Number POP', compute="_sum_noc_pop")

    overview_number_customer = fields.Integer(compute="_sum_total_customer", string="Total Customer")
    sum_apt_cust = fields.Integer('APT Cust', compute="_sum_apt_cust")
    sum_bws_cust = fields.Integer('BWS Cust', compute="_sum_bws_cust")
    sum_dc_cust = fields.Integer('DC Cust', compute="_sum_dc_cust")
    sum_fdc_cust = fields.Integer('FDC Cust', compute="_sum_fdc_cust")
    sum_hrb_cust = fields.Integer('HRB Cust', compute="_sum_hrb_cust")
    sum_noc_cust = fields.Integer('NOC Cust', compute="_sum_noc_cust")

    overview_monthly_tarif = fields.Float(string="Monthly Tarif", compute="_sum_total_monthly_tarif")
    sum_apt_month_tarif = fields.Float('APT Monthly Tarif', compute="_sum_apt_mothly_tariff")
    sum_bws_month_tarif = fields.Float('BWS Monthly Tarif', compute="_sum_bws_mothly_tariff")
    sum_dc_month_tarif = fields.Float('DC Monthly Tarif', compute="_sum_dc_mothly_tariff")
    sum_fdc_month_tarif = fields.Float('FDC Monthly Tarif', compute="_sum_fdc_mothly_tariff")
    sum_hrb_month_tarif = fields.Float('HRB Monthly Tarif', compute="_sum_hrb_mothly_tariff")
    sum_noc_month_tarif = fields.Float('NOC Monthly Tarif', compute="_sum_noc_mothly_tariff")

    overview_total_potential = fields.Integer(compute="_sum_total_potential", string="Total Potential")
    sum_apt_tot_potential = fields.Integer('APT Total Potential', compute="_sum_apt_potential")
    sum_bws_tot_potential = fields.Integer('BWS Total Potential', compute="_sum_bws_potential")
    sum_dc_tot_potential = fields.Integer('DC Total Potential', compute="_sum_dc_potential")
    sum_fdc_tot_potential = fields.Integer('FDC Total Potential', compute="_sum_fdc_potential")
    sum_hrb_tot_potential = fields.Integer('HRB Total Potential', compute="_sum_hrb_potential")
    sum_noc_tot_potential = fields.Integer('NOC Total Potential', compute="_sum_noc_potential")

    overview_current_penetration = fields.Float(string="Current Penetration", compute="_sum_current_penetration")
    sum_apt_current_penetration = fields.Float('APT Current Penetration', compute="_sum_current_penetration_apt_htl")
    sum_bws_current_penetration = fields.Float('BWS Current Penetration', compute="_sum_current_penetration_bws")
    sum_dc_current_penetration = fields.Float('DC Current Penetration', compute="_sum_current_penetration_dc")
    sum_fdc_current_penetration = fields.Float('FDC Current Penetration', compute="_sum_current_penetration_fdc")
    sum_hrb_current_penetration = fields.Float('HRB Current Penetration', compute="_sum_current_penetration_hrb")
    sum_noc_current_penetration = fields.Float('NOC Current Penetration', compute="_sum_current_penetration_noc")

    @api.depends('overview_number_pop')
    def _sum_number_pop(self):
        self.overview_number_pop = self.sum_apt_pop + self.sum_bws_pop + self.sum_dc_pop + self.sum_fdc_pop + self.sum_hrb_pop + self.sum_noc_pop

    # @api.depends('overview_number_customer')
    # def _sum_number_customers(self):
    #     self.overview_number_customer = self.sum_apt_cust + self.sum_bws_cust + self.sum_dc_cust + self.sum_fdc_cust + self.sum_hrb_cust + self.sum_noc_cust
    
    @api.model
    def _sum_total_customer(self):
        total_customer = self.env['res.partner'].search(
            [('customer_rank', '=', 1), ('tenant', '=', False)])
        for i in self:
            i.overview_number_customer = len(total_customer)

    # @api.depends('overview_monthly_tarif')
    # def _sum_total_monthly_tarif(self):
    #     self.overview_monthly_tarif = self.sum_apt_month_tarif + self.sum_bws_month_tarif + self.sum_dc_month_tarif + self.sum_fdc_month_tarif + self.sum_hrb_month_tarif + self.sum_noc_month_tarif
    
    @api.model
    def _sum_total_monthly_tarif(self):
        month_tariff = self.env['res.partner'].search(
            [('customer_rank', '=', 1), ('tenant', '=', False)])
        total_month_tariff = 0
        for m in month_tariff:
            total_month_tariff += float(m.revenue_month)
        for i in self:
            i.overview_monthly_tarif = float(total_month_tariff)

    @api.depends('overview_total_potential')
    def _sum_total_potential(self):
        self.overview_total_potential = self.sum_apt_tot_potential + self.sum_bws_tot_potential + self.sum_dc_tot_potential + self.sum_fdc_tot_potential + self.sum_hrb_tot_potential + self.sum_noc_tot_potential
    
    @api.depends('overview_number_customer','overview_total_potential')
    def _sum_current_penetration(self):
        for i in self:
            if i.overview_number_customer == 0:
                i.overview_current_penetration = 0
            elif i.overview_total_potential == 0:
                i.overview_current_penetration = 0
            else:
                i.overview_current_penetration = (i.overview_number_customer / i.overview_total_potential) *100

    @api.model
    def _sum_apt_pop(self):
        apt_pop = self.env['pop.service.coverage'].search(
            [('pop_type', '=', 'APT-HTL')])
        for i in self:
            i.sum_apt_pop = len(apt_pop)

    @api.model
    def _sum_bws_pop(self):
        bws_pop = self.env['pop.service.coverage'].search(
            [('pop_type', '=', 'BWS')])
        for i in self:
            i.sum_bws_pop = len(bws_pop)

    @api.model
    def _sum_dc_pop(self):
        dc_pop = self.env['pop.service.coverage'].search(
            [('pop_type', '=', 'DC')])
        for i in self:
            i.sum_dc_pop = len(dc_pop)

    @api.model
    def _sum_fdc_pop(self):
        fdc_pop = self.env['pop.service.coverage'].search(
            [('pop_type', '=', 'FDC')])
        for i in self:
            i.sum_fdc_pop = len(fdc_pop)
    
    @api.model
    def _sum_hrb_pop(self):
        hrb_pop = self.env['pop.service.coverage'].search(
            [('pop_type', '=', 'HRB')])
        for i in self:
            i.sum_hrb_pop = len(hrb_pop)
    
    @api.model
    def _sum_noc_pop(self):
        noc_pop = self.env['pop.service.coverage'].search(
            [('pop_type', '=', 'NOC')])
        for i in self:
            i.sum_noc_pop = len(noc_pop)


    @api.model
    def _sum_apt_cust(self):
        apt_cust = self.env['res.partner'].search(
            [('customer_rank','=', 1),('tenant','=', False),('pop_id.pop_type', '=', 'APT-HTL')])
        for i in self:
            i.sum_apt_cust = len(apt_cust)
    
    @api.model
    def _sum_bws_cust(self):
        bws_cust = self.env['res.partner'].search(
            [('customer_rank','=', 1),('tenant','=', False),('pop_id.pop_type', '=', 'BWS')])
        for i in self:
            i.sum_bws_cust = len(bws_cust)

    @api.model
    def _sum_dc_cust(self):
        dc_cust = self.env['res.partner'].search(
            [('customer_rank','=', 1),('tenant','=', False),('pop_id.pop_type', '=', 'DC')])
        for i in self:
            i.sum_dc_cust = len(dc_cust)
    
    @api.model
    def _sum_fdc_cust(self):
        fdc_cust = self.env['res.partner'].search(
            [('customer_rank','=', 1),('tenant','=', False),('pop_id.pop_type', '=', 'FDC')])
        for i in self:
            i.sum_fdc_cust = len(fdc_cust)
    
    @api.model
    def _sum_hrb_cust(self):
        hrb_cust = self.env['res.partner'].search(
            [('customer_rank','=', 1),('tenant','=', False),('pop_id.pop_type', '=', 'HRB')]) #customers
        for i in self:
            i.sum_hrb_cust = len(hrb_cust)
    
    @api.model
    def _sum_noc_cust(self):
        noc_cust = self.env['res.partner'].search(
            [('customer_rank','=', 1),('tenant','=', False),('pop_id.pop_type', '=', 'NOC')])
        for i in self:
            i.sum_noc_cust = len(noc_cust)
    
    @api.model
    def _sum_apt_mothly_tariff(self):
        apt_tariff = self.env['res.partner'].search(
            [('customer_rank', '=', 1), ('tenant', '=', False), ('pop_id.pop_type', '=', 'APT-HTL')])
        total_month_tariff = 0
        for m in apt_tariff:
            total_month_tariff += float(m.revenue_month)
        for i in self:
            i.sum_apt_month_tarif = float(total_month_tariff)
    
    @api.model
    def _sum_bws_mothly_tariff(self):
        bws_tariff = self.env['res.partner'].search(
            [('customer_rank', '=', 1), ('tenant', '=', False), ('pop_id.pop_type', '=', 'BWS')])
        total_month_tariff = 0
        for m in bws_tariff:
            total_month_tariff += float(m.revenue_month)
        for i in self:
            i.sum_bws_month_tarif = float(total_month_tariff)
    
    @api.model
    def _sum_dc_mothly_tariff(self):
        dc_tariff = self.env['res.partner'].search(
            [('customer_rank', '=', 1), ('tenant', '=', False), ('pop_id.pop_type', '=', 'DC')])
        total_month_tariff = 0
        for m in dc_tariff:
            total_month_tariff += float(m.revenue_month)
        for i in self:
            i.sum_dc_month_tarif = float(total_month_tariff)

    @api.model
    def _sum_fdc_mothly_tariff(self):
        fdc_tariff = self.env['res.partner'].search(
            [('customer_rank', '=', 1), ('tenant', '=', False), ('pop_id.pop_type', '=', 'FDC')])
        total_month_tariff = 0
        for m in fdc_tariff:
            total_month_tariff += float(m.revenue_month)
        for i in self:
            i.sum_fdc_month_tarif = float(total_month_tariff)

    @api.model
    def _sum_hrb_mothly_tariff(self):
        hrb_tariff = self.env['res.partner'].search(
            [('customer_rank', '=', 1), ('tenant', '=', False), ('pop_id.pop_type', '=', 'HRB')])
        total_month_tariff = 0
        for m in hrb_tariff:
            total_month_tariff += float(m.revenue_month)
        for i in self:
            i.sum_hrb_month_tarif = float(total_month_tariff)
    
    @api.model
    def _sum_noc_mothly_tariff(self):
        noc_tariff = self.env['res.partner'].search(
            [('customer_rank', '=', 1), ('tenant', '=', False), ('pop_id.pop_type', '=', 'NOC')])
        total_month_tariff = 0
        for m in noc_tariff:
            total_month_tariff += float(m.revenue_month)
        for i in self:
            i.sum_noc_month_tarif = float(total_month_tariff)

    @api.model
    def _sum_apt_potential(self):
        apt_potential = self.env['res.partner'].search(
            [('tenant','=', 1), ('pop_id.pop_type', '=', 'APT-HTL')]) #potential
        for i in self:
            i.sum_apt_tot_potential = len(apt_potential)

    @api.model
    def _sum_bws_potential(self):
        bws_potential = self.env['res.partner'].search(
            [('tenant','=', 1),('pop_id.pop_type', '=', 'BWS')]) #potential
        for i in self:
            i.sum_bws_tot_potential = len(bws_potential)

    @api.model
    def _sum_dc_potential(self):
        dc_potential = self.env['res.partner'].search(
            [('tenant','=', 1),('pop_id.pop_type', '=', 'DC')]) #potential
        for i in self:
            i.sum_dc_tot_potential = len(dc_potential)

    @api.model
    def _sum_fdc_potential(self):
        fdc_potential = self.env['res.partner'].search(
            [('tenant','=', 1),('pop_id.pop_type', '=', 'FDC')]) #potential
        for i in self:
            i.sum_fdc_tot_potential = len(fdc_potential)

    @api.model
    def _sum_hrb_potential(self):
        hrb_potential = self.env['res.partner'].search(
            [('tenant','=', 1),('pop_id.pop_type', '=', 'HRB')]) #potential
        for i in self:
            i.sum_hrb_tot_potential = len(hrb_potential)

    @api.model
    def _sum_noc_potential(self):
        noc_potential = self.env['res.partner'].search(
            [('tenant','=', 1),('pop_id.pop_type', '=', 'NOC')]) #potential
        for i in self:
            i.sum_noc_tot_potential = len(noc_potential)
    
    @api.depends('sum_apt_cust','sum_apt_tot_potential')
    def _sum_current_penetration_apt_htl(self):
        for i in self:
            if i.sum_apt_cust == 0:
                i.sum_apt_current_penetration = 0
            elif i.sum_apt_tot_potential == 0:
                i.sum_apt_current_penetration = 0
            else:
                i.sum_apt_current_penetration = (i.sum_apt_cust / i.sum_apt_tot_potential) * 100
    
    @api.depends('sum_bws_cust','sum_bws_tot_potential')
    def _sum_current_penetration_bws(self):
        for i in self:
            if i.sum_bws_cust == 0:
                i.sum_bws_current_penetration = 0
            elif i.sum_bws_tot_potential == 0:
                i.sum_bws_current_penetration = 0
            else:
                i.sum_bws_current_penetration = (i.sum_bws_cust / i.sum_bws_tot_potential) * 100
    
    @api.depends('sum_dc_cust','sum_dc_tot_potential')
    def _sum_current_penetration_dc(self):
        for i in self:
            if i.sum_dc_cust == 0:
                i.sum_dc_current_penetration = 0
            elif i.sum_dc_tot_potential == 0:
                i.sum_dc_current_penetration = 0
            else:
                i.sum_dc_current_penetration = (i.sum_dc_cust / i.sum_dc_tot_potential) * 100
    
    @api.depends('sum_fdc_cust','sum_fdc_tot_potential')
    def _sum_current_penetration_fdc(self):
        for i in self:
            if i.sum_fdc_cust == 0:
                i.sum_fdc_current_penetration = 0
            elif i.sum_fdc_tot_potential == 0:
                i.sum_fdc_current_penetration = 0
            else:
                i.sum_fdc_current_penetration = (i.sum_fdc_cust / i.sum_fdc_tot_potential) * 100

    @api.depends('sum_hrb_cust','sum_hrb_tot_potential')
    def _sum_current_penetration_hrb(self):
        for i in self:
            if i.sum_hrb_cust == 0:
                i.sum_hrb_current_penetration = 0
            elif i.sum_hrb_tot_potential == 0:
                i.sum_hrb_current_penetration = 0
            else:
                i.sum_hrb_current_penetration = (i.sum_hrb_cust / i.sum_hrb_tot_potential) *100
    
    @api.depends('sum_noc_cust','sum_noc_tot_potential')
    def _sum_current_penetration_noc(self):
        for i in self:
            if i.sum_noc_cust == 0:
                i.sum_noc_current_penetration = 0
            if i.sum_noc_tot_potential == 0:
                i.sum_noc_current_penetration = 0
            else:
                i.sum_noc_current_penetration = (i.sum_noc_cust / i.sum_noc_tot_potential) *100

class PopIndustry(models.Model):
    _name = 'pop.industry'
    _description = 'POP Industry'
    _rec_name = 'pop_industry_name'

    pop_industry_name = fields.Many2one('pop.type', string="Name")
    pop_industry_number_of_customer = fields.Integer(string="Total Customer", compute="_total_customer_industry")
    pop_industry_number_of_customer_cluster = fields.Integer(string="Number of Customer Cluster", compute="_count_total_customer_cluster")
    pop_industry_number_of_customer_pop = fields.Integer(string="Number of Customer POP", compute="_count_total_customer_pop")
    
    pop_industry_revenue_month = fields.Float(string="Monthly Tariff", compute="_count_total_revenue_month_industry")
    pop_industry_revenue_month_cluster = fields.Float(string="Monthly Tariff Cluster", compute="_count_total_revenue_month_cluster")
    pop_industry_revenue_month_pop = fields.Float(string="Monthly Tariff POP", compute="_count_total_revenue_month_pop")
    
    pop_industry_arpu = fields.Integer(string="ARPU", compute="_industry_arpu")
    
    pop_industry_number_of_service = fields.Integer(string="Total Service", compute="_total_service")
    pop_industry_potential = fields.Integer('Industry Potential')
    pop_industry_penetration = fields.Integer('Industry Penetration')
    pop_industry_number_of_service_cluster = fields.Integer(string="Number of Service", compute="_total_service_cluster")
    pop_industry_number_of_service_pop = fields.Integer(string="Number of Service", compute="_total_service_pop")
    
    pop_industry_ob_quota = fields.Integer(string="Annual Quota")
    manager_incharge = fields.Char('Manager In Charge')
    pop_industry_cold_leads = fields.Integer('Cold Leads')
    pop_industry_mcfc = fields.Integer('MCF-C')
    pop_industry_sales_focus = fields.Integer('Sales Focus')
    
    pop_industry_ytd_achivement = fields.Integer(string="YTD Achivement")
    pop_industry_achieve = fields.Float(string="Achievement %")
    pop_industry_ytd_churn = fields.Integer(string="YTD Churn")
    pop_industry_ytd_downgrade = fields.Integer(string="YTD Downgrade")
    pop_industry_ytd_net_increase = fields.Integer(string="YTD Net Increase")
    pop_industry_ytd_rev_growth = fields.Integer(string="YTD Rev Growth")
    
    pop_industry_cluster_ids = fields.One2many('pop.industry.cluster', 'cluster_id', string="Industry Cluster ID")
    pop_service_coverage_ids = fields.One2many('pop.service.coverage', 'pop_industry', string="Service Coverage ID")
    
    #Customer
    @api.depends('pop_industry_cluster_ids')
    def _count_total_customer_cluster(self):
        for b in self:
            b.pop_industry_number_of_customer_cluster = sum(line.pop_industry_cluster_total_customer for line in b.pop_industry_cluster_ids)
    
    @api.depends('pop_service_coverage_ids')
    def _count_total_customer_pop(self):
        for b in self:
            b.pop_industry_number_of_customer_pop = sum(line.pop_total_customer_hrb for line in b.pop_service_coverage_ids)
    
    @api.depends('pop_industry_number_of_customer_cluster', 'pop_industry_number_of_customer_pop')
    def _total_customer_industry(self):
        for rec in self:
            rec.pop_industry_number_of_customer = rec.pop_industry_number_of_customer_cluster + rec.pop_industry_number_of_customer_pop
    

    #monthly tariff
    @api.depends('pop_industry_cluster_ids')
    def _count_total_revenue_month_cluster(self):
        for b in self:
            b.pop_industry_revenue_month_cluster = sum(line.pop_industry_cluster_revenue_month for line in b.pop_industry_cluster_ids)
    
    @api.depends('pop_service_coverage_ids')
    def _count_total_revenue_month_pop(self):
        for b in self:
            b.pop_industry_revenue_month_pop = sum(line.pop_total_monthly_tarif_hrb for line in b.pop_service_coverage_ids)
    
    @api.depends('pop_industry_revenue_month_cluster', 'pop_industry_revenue_month_pop')
    def _count_total_revenue_month_industry(self):
        for rec in self:
            rec.pop_industry_revenue_month = rec.pop_industry_revenue_month_cluster + rec.pop_industry_revenue_month_pop
    
    #ARPU
    @api.depends('pop_industry_revenue_month','pop_industry_number_of_customer')
    def _industry_arpu(self):
        for i in self:
            if i.pop_industry_revenue_month == 0:
                i.pop_industry_arpu = 0
            elif i.pop_industry_number_of_customer == 0:
                i.pop_industry_arpu
            else:
                i.pop_industry_arpu = i.pop_industry_revenue_month / i.pop_industry_number_of_customer
    
    #Service
    @api.depends('pop_industry_cluster_ids')
    def _total_service_cluster(self):
        for a in self:
            a.pop_industry_number_of_service_cluster = sum(line.pop_indistry_cluster_total_service for line in a.pop_industry_cluster_ids)
    
    @api.depends('pop_service_coverage_ids')
    def _total_service_pop(self):
        for a in self:
            a.pop_industry_number_of_service_pop = sum(line.pop_total_service_hrb for line in a.pop_service_coverage_ids)
    
    @api.depends('pop_industry_number_of_service_cluster', 'pop_industry_number_of_service_pop')
    def _total_service(self):
        for rec in self:
            rec.pop_industry_number_of_service = rec.pop_industry_number_of_service_cluster + rec.pop_industry_number_of_service_pop
    
class PopIndustryCluster(models.Model):
    _name = 'pop.industry.cluster'
    _description = 'POP Industry Cluster'
    _rec_name = 'pop_industry_cluster_name'

    cluster_id = fields.Many2one('pop.industry', string="Industry Type")
    # cluster_id2 = fields.Many2one('pop.pic', string="Cluster ID POP PIC")
    pop_industry_name = fields.Many2one(related='cluster_id.pop_industry_name', string="Name", relation="pop.type", store="true")
    pop_industry_number_of_customer = fields.Integer(related='cluster_id.pop_industry_number_of_customer', string="Number of Customer", store="true")
    pop_industry_revenue_month = fields.Float(related='cluster_id.pop_industry_revenue_month',string="Monthly Tariff" , store="true")
    pop_industry_arpu = fields.Integer(related='cluster_id.pop_industry_arpu',string="ARPU" , store="true")
    pop_industry_number_of_service = fields.Integer(related='cluster_id.pop_industry_number_of_service',string="Number of Service" , store="true")
    pop_industry_ob_quota = fields.Integer(related='cluster_id.pop_industry_ob_quota',string="OB Quota", store="true")
    pop_industry_ytd_achivement = fields.Integer(related='cluster_id.pop_industry_ytd_achivement',string="YTD Achivement", store="true")
    pop_industry_achieve = fields.Float(related='cluster_id.pop_industry_achieve',stirng="Achieve %", store="true")
    pop_industry_ytd_churn = fields.Integer(related='cluster_id.pop_industry_ytd_churn',string="YTD Churn", store="true")
    pop_industry_ytd_downgrade = fields.Integer(related='cluster_id.pop_industry_ytd_downgrade',string="YTD Downgrade", store="true")
    pop_industry_ytd_net_increase = fields.Integer(related='cluster_id.pop_industry_ytd_net_increase',string="YTD Net Increase", store="true")
    pop_industry_ytd_rev_growth = fields.Integer(related='cluster_id.pop_industry_ytd_rev_growth',string="YTD Rev Growth", store="true")
    space = fields.Char(' ', readonly=True)
    
    pop_industry_cluster_name = fields.Char(string="Cluster Name")
    #pop_industry_cluster_type = fields.Many2one('pop.type', string="Industry Type")
    pop_industry_cluster_id = fields.Char(string="Industry Cluster ID")
    pop_industry_cluster_manager = fields.Many2one('pic.manager', string="Cluster PIC Manager")
    pop_industry_cluster_pic_am = fields.Many2one('pop.pic', string="ACC Mgm")
    pop_industry_cluster_description = fields.Text('Cluster Scope')

    pop_industry_cluster_total_penetration = fields.Float(string="Industry Penetration", compute="_total_current_penetration" )
    pop_industry_cluster_total_customer = fields.Integer(string="Total Customer", compute="_count_total_customer")
    pop_industry_cluster_total_potential = fields.Integer(string="Industry Potential", compute="_count_total_potential")
    pop_industry_cluster_cold_leads = fields.Integer(string="Cold Leads")
    pop_industry_cluster_total_revenue = fields.Integer(string="Total Revenue")
    pop_industry_cluster_revenue_month = fields.Float(string="Monthly Tariff", compute="_total_monthly_tariff")
    pop_industry_cluster_arpu = fields.Float(string="ARPU", compute="_industry_cluster_arpu")
    pop_industry_cluster_ob = fields.Integer(string="Order Booking")
    pop_industry_cluster_mcfc = fields.Integer('MCF-C')
    pop_industry_cluster_sf_this_month = fields.Integer(string="Sales Focus")
    pop_indistry_cluster_total_service = fields.Integer('Total Service', compute="_total_service")

class Pop(models.Model):
    _name = 'pop.service.coverage'
    _description = 'POP'
    _rec_name = 'pop_id'


    @api.depends('pop_id', 'pop_name')
    def name_get(self):
        result = []
        for row in self:
            if row.pop_name :
                name = str(row.pop_id)+'  '+ str(row.pop_name)
                result.append((row.id, name))
        return result

    
    pop_name = fields.Char(string="POP Name")
    pop_id = fields.Char(string="POP ID")
    pop_regional = fields.Many2one('pop.regional', string="Province")
    pop_area = fields.Many2one('pop.area', string="District")
    pop_type = fields.Many2one('pop.type', string="POP Type")
    pop_industry = fields.Many2one('pop.industry', string="Industry Mix")
    pop_capacity = fields.Integer(string="Primary Link Partner")
    primary_link_capacity = fields.Integer(string="Primary Link Capacity")
    backup_link_partner = fields.Integer(string="Backup Link Partner")
    backup_link_capacity = fields.Integer(string="Backup Link Capacity")
    pop_pic_bm = fields.Char(string="BM")
    pop_metroe = fields.Boolean(string="Metro-E Velo")
    #pop_pic_manager = fields.Many2one(related='pic_manager', string="ACC Mgm")

    service_delivery = fields.Selection([('DIRECT', 'DIRECT'), ('INDIRECT', 'INDIRECT')], string="Service Delivery")
    longitude = fields.Float(string="Long")
    latitude = fields.Float(string="Lat")
    regionalhub = fields.Many2one('pop.hub.region', string="Regional HUB")
    state = fields.Selection([('draft','Draft'), ('active','Active'), ('inactive','Inactive')], string="Status", default='draft')

    def action_active(self):
        self.state = 'active'
    
    def action_inactive(self):
        self.state = 'inactive'
    
    def action_draft(self):
        self.state= 'draft'
    
    pop_total_penetration = fields.Float(string="POP Penetration", compute="_total_current_penetration")
    pop_total_penetration_hrb = fields.Float(string="Potential Penetration HRB", compute="_total_current_penetration_hrb")
    pop_total_customer = fields.Integer(string="Total Customer", compute="_count_tot_customer")
    #HRB
    pop_total_customer_hrb = fields.Integer(string="Total Customer", compute="_count_tot_customer_hrb")
    pop_total_monthly_tarif_hrb = fields.Integer(string="Total Monthly Tarif HRB", compute="_count_tot_customer_hrb")
    pop_total_service_hrb = fields.Integer(string="Total Service HRB", compute="_count_tot_customer_hrb")
    space = fields.Char(' ', readonly=True)
    pop_total_service = fields.Integer('POP Total Service', compute="_pop_total_service")
    pop_total_potential = fields.Integer(string="Total Potential", compute="_count_tot_potential")
    pop_total_monthly_tariff = fields.Integer(string="Monthly Tariff", compute="_total_monthly_tariff")
    pop_total_sales_focus = fields.Integer(string="Sales Focus", compute="_sales_focus_blast")
    pop_total_order_booking = fields.Integer(string="Total Order Booking", compute="_order_booking_blast")
    pop_order_booking_this_month = fields.Integer(string="OB This Month", compute="_ob_this_month_blast")
    pop_program = fields.Many2one('velo.program', "Marketing Program")
    pop_arpu = fields.Float(string="ARPU", compute="_total_arpu")
    number_pop = fields.Integer(string="Number POP")
    pop_monthly_tarif = fields.Integer(string="Monthly Tarif") #not used
    pop_cold_leads = fields.Integer(string="Cold Leads")
    pop_mcfc = fields.Integer('MCF-C')
    pop_pic_am = fields.Many2one('pop.pic', string="ACC Mgm")



    @api.depends('pop_total_customer','pop_total_potential')
    def _total_current_penetration(self):
        for i in self:
            if i.pop_total_customer == 0:
                i.pop_total_penetration = 0
            elif i.pop_total_potential == 0:
                i.pop_total_penetration = 0
            else:
                i.pop_total_penetration = (i.pop_total_customer / i.pop_total_potential)
    
    @api.depends('pop_total_customer_hrb','pop_total_potential')
    def _total_current_penetration_hrb(self):
        for i in self:
            if i.pop_total_customer_hrb == 0:
                i.pop_total_penetration_hrb = 0
            elif i.pop_total_potential == 0:
                i.pop_total_penetration_hrb = 0
            else:
                i.pop_total_penetration_hrb = (i.pop_total_customer_hrb / i.pop_total_potential)

    @api.model
    def _sales_focus_blast(self):
        crm_stage = self.env['crm.stage'].search([('name','ilike','Sales Focus')])
        crm = self.env['crm.lead'].search([('stage_id','=',crm_stage.id)])
        for i in self:
            i.pop_total_sales_focus = len(crm)
    
    @api.model
    def _order_booking_blast(self):
        crm_stage = self.env['crm.stage'].search([('name','ilike','Order Booking')])
        crm = self.env['crm.lead'].search([('stage_id','=',crm_stage.id)])
        for i in self:
            i.pop_total_order_booking = len(crm)

    @api.model
    def _ob_this_month_blast(self):
        cl_count = 0
        crm_stage = self.env['crm.stage'].search([('name','ilike','Order Booking')])
        stage_id = crm_stage.id
        self.env.cr.execute("SELECT COUNT(DISTINCT(id))as jml FROM crm_lead WHERE extract (month FROM create_date) = extract (month FROM CURRENT_DATE) and stage_id = stage_id")
        for pro in self.env.cr.dictfetchall():
            cl_count = pro["jml"]

        for i in self:
            i.pop_order_booking_this_month = cl_count

              

class PopService(models.Model):
    _name = 'pop.service'
    _description = 'Service List'
    _rec_name = 'pop_service'

    pop_service_id = fields.Many2one('pop.service.coverage', string="POP Service Coverage ID", default="266")
    pop_service = fields.Many2one('product.product', string="Service")
    pop_service_company = fields.Many2one('res.partner', string="Company")
    pop_service_contract_period = fields.Date(string="Contract Period")
    pop_service_monthly_tarif = fields.Integer(string="Monthly Tariff")
    pop_service_total_revenue = fields.Integer(string="Total Revenue")
    pop_service_total_revenue_sum = fields.Integer(string="SUM Total Revenue", compute="_total_service_revenue")
    pop_service_industry_cluster = fields.Many2one('pop.industry.cluster', string="Industry Cluster")
