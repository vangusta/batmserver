# -*- coding: utf-8 -*-
from odoo import http

# class VeloRetentionPipeline(http.Controller):
#     @http.route('/velo_retention_pipeline/velo_retention_pipeline/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/velo_retention_pipeline/velo_retention_pipeline/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('velo_retention_pipeline.listing', {
#             'root': '/velo_retention_pipeline/velo_retention_pipeline',
#             'objects': http.request.env['velo_retention_pipeline.velo_retention_pipeline'].search([]),
#         })

#     @http.route('/velo_retention_pipeline/velo_retention_pipeline/objects/<model("velo_retention_pipeline.velo_retention_pipeline"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('velo_retention_pipeline.object', {
#             'object': obj
#         })