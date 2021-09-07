# -*- coding: utf-8 -*-
from odoo import http

# class VeloOrderFulfilment(http.Controller):
#     @http.route('/velo_order_fulfilment/velo_order_fulfilment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/velo_order_fulfilment/velo_order_fulfilment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('velo_order_fulfilment.listing', {
#             'root': '/velo_order_fulfilment/velo_order_fulfilment',
#             'objects': http.request.env['velo_order_fulfilment.velo_order_fulfilment'].search([]),
#         })

#     @http.route('/velo_order_fulfilment/velo_order_fulfilment/objects/<model("velo_order_fulfilment.velo_order_fulfilment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('velo_order_fulfilment.object', {
#             'object': obj
#         })