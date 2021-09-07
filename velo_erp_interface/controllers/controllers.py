# -*- coding: utf-8 -*-
from odoo import http

# class VeloErpInterface(http.Controller):
#     @http.route('/velo_erp_interface/velo_erp_interface/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/velo_erp_interface/velo_erp_interface/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('velo_erp_interface.listing', {
#             'root': '/velo_erp_interface/velo_erp_interface',
#             'objects': http.request.env['velo_erp_interface.velo_erp_interface'].search([]),
#         })

#     @http.route('/velo_erp_interface/velo_erp_interface/objects/<model("velo_erp_interface.velo_erp_interface"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('velo_erp_interface.object', {
#             'object': obj
#         })