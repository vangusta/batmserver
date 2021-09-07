# -*- coding: utf-8 -*-
from odoo import http

# class ServiceCoverage(http.Controller):
#     @http.route('/service_coverage/service_coverage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/service_coverage/service_coverage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('service_coverage.listing', {
#             'root': '/service_coverage/service_coverage',
#             'objects': http.request.env['service_coverage.service_coverage'].search([]),
#         })

#     @http.route('/service_coverage/service_coverage/objects/<model("service_coverage.service_coverage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('service_coverage.object', {
#             'object': obj
#         })