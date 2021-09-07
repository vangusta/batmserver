# -*- coding: utf-8 -*-
from odoo import http

# class ProductVelo(http.Controller):
#     @http.route('/product_velo/product_velo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_velo/product_velo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_velo.listing', {
#             'root': '/product_velo/product_velo',
#             'objects': http.request.env['product_velo.product_velo'].search([]),
#         })

#     @http.route('/product_velo/product_velo/objects/<model("product_velo.product_velo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_velo.object', {
#             'object': obj
#         })