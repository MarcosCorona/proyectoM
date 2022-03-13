# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyecto_odoo(models.Model):
#     _name = 'proyecto_odoo.proyecto_odoo'
#     _description = 'proyecto_odoo.proyecto_odoo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
