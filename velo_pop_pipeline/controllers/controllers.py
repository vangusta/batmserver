# -*- coding: utf-8 -*-
from odoo import http

# class VeloPopPipeline(http.Controller):
#     @http.route('/velo_pop_pipeline/velo_pop_pipeline/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/velo_pop_pipeline/velo_pop_pipeline/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('velo_pop_pipeline.listing', {
#             'root': '/velo_pop_pipeline/velo_pop_pipeline',
#             'objects': http.request.env['velo_pop_pipeline.velo_pop_pipeline'].search([]),
#         })

#     @http.route('/velo_pop_pipeline/velo_pop_pipeline/objects/<model("velo_pop_pipeline.velo_pop_pipeline"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('velo_pop_pipeline.object', {
#             'object': obj
#         })