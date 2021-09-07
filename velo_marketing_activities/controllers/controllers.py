# -*- coding: utf-8 -*-
from odoo import http

# class VeloMarketingActivites(http.Controller):
#     @http.route('/velo_marketing_activities/velo_marketing_activities/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/velo_marketing_activities/velo_marketing_activities/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('velo_marketing_activities.listing', {
#             'root': '/velo_marketing_activities/velo_marketing_activities',
#             'objects': http.request.env['velo_marketing_activities.velo_marketing_activities'].search([]),
#         })

#     @http.route('/velo_marketing_activities/velo_marketing_activities/objects/<model("velo_marketing_activities.velo_marketing_activities"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('velo_marketing_activities.object', {
#             'object': obj
#         })