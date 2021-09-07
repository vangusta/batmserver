# -*- coding: utf-8 -*-
from odoo import http

# class VeloContract(http.Controller):
#     @http.route('/velo_contract/velo_contract/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/velo_contract/velo_contract/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('velo_contract.listing', {
#             'root': '/velo_contract/velo_contract',
#             'objects': http.request.env['velo_contract.velo_contract'].search([]),
#         })

#     @http.route('/velo_contract/velo_contract/objects/<model("velo_contract.velo_contract"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('velo_contract.object', {
#             'object': obj
#         })