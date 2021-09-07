# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class velo_sales_order(models.Model):
	_inherit = 'sale.order'

	@api.model
	def create(self, vals):
		if vals.get('name', _('New')) == _('New'):
		    seq_date = None
		    if 'date_order' in vals:
		        seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
		    if 'company_id' in vals:
		        vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code(
		            'velo_sale.order', sequence_date=seq_date) or _('New')
		    else:
		        vals['name'] = self.env['ir.sequence'].next_by_code('velo_sale.order', sequence_date=seq_date) or _('New')

		# Makes sure partner_invoice_id', 'partner_shipping_id' and 'pricelist_id' are defined
		if any(f not in vals for f in ['partner_invoice_id', 'partner_shipping_id', 'pricelist_id']):
		    partner = self.env['res.partner'].browse(vals.get('partner_id'))
		    addr = partner.address_get(['delivery', 'invoice'])
		    vals['partner_invoice_id'] = vals.setdefault('partner_invoice_id', addr['invoice'])
		    vals['partner_shipping_id'] = vals.setdefault('partner_shipping_id', addr['delivery'])
		    vals['pricelist_id'] = vals.setdefault('pricelist_id', partner.property_product_pricelist and partner.property_product_pricelist.id)
		result = super(velo_sales_order, self).create(vals)
		return result
	
	pop_name = fields.Many2one('pop.service.coverage',string="POP Name")
	pop_id = fields.Char(related="pop_name.pop_id",string="POP ID")
	pop_regional = fields.Many2one(related="pop_name.pop_regional", string="Province")
	pop_type = fields.Many2one(related="pop_name.pop_type", string="POP Type")
	pop_metroe = fields.Boolean(related="pop_name.pop_metroe",string="MetroE")

	email = fields.Char(related="partner_id.email",string="Email")
	phone = fields.Char(related="partner_id.phone",string="Phone")
	potential = fields.Boolean(string='Potential', default='1')
	partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|','&', ('company_id', '=', False), ('company_id', '=', company_id), ('tenant', '=', potential)]",)
	program = fields.Many2one('velo.program',string="Program")
	discount_monthly_tariff = fields.Float(related="program.discount_monthly_tariff", string=""'Discount Monthly Tariff')

	@api.onchange('program')
	def _onchange_program(self):
		for rec in self:
			if rec.program:
				lines = [(5, 0, 0)]
				print("self.program", self.program)
				for line in self.program:
					val = {
						'product_id': line.product_ids.id,
						'name': line.product_ids.name,
						'product_uom_qty': 1.0,
						'product_uom': 1,
						'price_unit': line.product_ids.list_price
						}
					lines.append((0, 0, val))
				rec.order_line = lines

class velo_sales_order_line(models.Model):
	_inherit = 'sale.order.line'

	@api.depends('product_id','order_id.pop_name')
	def _product_group_function(self):
		for i in self:
			i.product_group = i.product_template_id.product_group
			i.product_category = i.product_template_id.categ_id.name

			pop_regional =  i.order_id.pop_regional.pop_regional_name
			pop_type =  i.order_id.pop_type.poptype_name
			pop_metroe =  i.order_id.pop_metroe
			product_template_id = i.product_template_id.id

			regional = ''
			for rec in i.product_template_id.validity_ids :
				regional = rec.region.pop_regional_name


			if pop_type == 'HRB' :
				 pop_type = 'hrb'
			else :
				 pop_type = 'nonhrb'

			if pop_metroe == True :
				 pop_metroe = 'Metro'
			else :
				 pop_metroe = 'Non Metro'

			if regional == 'All Region' :
				value = self.env['product.validity'].search([('region','=', regional),('validity_id','=', product_template_id),('status','=', True)])
			else :
				value = self.env['product.validity'].search([('region','=', pop_regional),('hrb','ilike', pop_type),('metroe','=', pop_metroe),('validity_id','=', product_template_id),('status','=', True)])

			i.price_unit = value.monthly_tariff
			i.one_time_charge = value.installation_fee


	def _compute_amount(self):
		for line in self:
			price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
			taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
			one_time_charge = line.one_time_charge
			line.update({
					'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
					'price_total': taxes['total_included'],
					'price_subtotal': float(taxes['total_excluded']) + float(one_time_charge),
				})

	
	product_group = fields.Char(string="Product Group", compute="_product_group_function")
	product_category = fields.Char(string="Product category", compute="_product_group_function")
	price_unit = fields.Float('Unit Price', required=True, digits='Product Price', default=0.0)
	one_time_charge = fields.Float(string="One Time Charge", compute="_product_group_function") 
	discount_monthly_tariff = fields.Float(related="order_id.discount_monthly_tariff", string=""'Discount Monthly Tariff')