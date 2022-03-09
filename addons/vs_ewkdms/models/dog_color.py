from odoo import api, fields, models


class DogColor(models.Model):
    _name = 'dog.color'
    _description = 'shit dog color'

    name = fields.Char()
    hex_value = fields.Char()
    color = fields.Integer('Colour')
