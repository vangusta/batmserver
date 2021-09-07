# -*- coding: utf-8 -*-
from odoo import http

# class VeloCustomers(http.Controller):
#     @http.route('/velo_customers/velo_customers/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/velo_customers/velo_customers/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('velo_customers.listing', {
#             'root': '/velo_customers/velo_customers',
#             'objects': http.request.env['velo_customers.velo_customers'].search([]),
#         })

#     @http.route('/velo_customers/velo_customers/objects/<model("velo_customers.velo_customers"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('velo_customers.object', {
#             'object': obj
#         })