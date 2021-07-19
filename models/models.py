# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools import pycompat
from odoo.exceptions import ValidationError, UserError, AccessError

class custom_exceptions(models.Model):
    _name = 'custom_exceptions'

    name = fields.Char(default='a')

    # @api.constrains('name')
    # def raise_exceptions(self):
    #     for r in self:
    #         if r.name:
    #             raise ValidationError('Test 123456789')


class custom_exceptions2(models.Model):
    _name = 'custom_exceptions_2'

    name = fields.Char(default='2')

    @api.model
    def create(self, vals):
        a = self.env['custom_exceptions'].create({'a': 1})
        return super(custom_exceptions2, self).create(vals)

