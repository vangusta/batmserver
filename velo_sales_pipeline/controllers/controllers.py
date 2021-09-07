# -*- coding: utf-8 -*-
from odoo import http

# class VeloSalesPipeline(http.Controller):
#     @http.route('/velo_sales_pipeline/velo_sales_pipeline/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/velo_sales_pipeline/velo_sales_pipeline/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('velo_sales_pipeline.listing', {
#             'root': '/velo_sales_pipeline/velo_sales_pipeline',
#             'objects': http.request.env['velo_sales_pipeline.velo_sales_pipeline'].search([]),
#         })

#     @http.route('/velo_sales_pipeline/velo_sales_pipeline/objects/<model("velo_sales_pipeline.velo_sales_pipeline"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('velo_sales_pipeline.object', {
#             'object': obj
#         })