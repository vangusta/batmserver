# -*- coding: utf-8 -*-
from odoo import http

# class VeloHelpdesk(http.Controller):
#     @http.route('/velo_helpdesk/velo_helpdesk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/velo_helpdesk/velo_helpdesk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('velo_helpdesk.listing', {
#             'root': '/velo_helpdesk/velo_helpdesk',
#             'objects': http.request.env['velo_helpdesk.velo_helpdesk'].search([]),
#         })

#     @http.route('/velo_helpdesk/velo_helpdesk/objects/<model("velo_helpdesk.velo_helpdesk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('velo_helpdesk.object', {
#             'object': obj
#         })