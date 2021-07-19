# -*- coding: utf-8 -*-
from odoo import http

# class CustomExceptions(http.Controller):
#     @http.route('/custom_exceptions/custom_exceptions/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_exceptions/custom_exceptions/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_exceptions.listing', {
#             'root': '/custom_exceptions/custom_exceptions',
#             'objects': http.request.env['custom_exceptions.custom_exceptions'].search([]),
#         })

#     @http.route('/custom_exceptions/custom_exceptions/objects/<model("custom_exceptions.custom_exceptions"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_exceptions.object', {
#             'object': obj
#         })