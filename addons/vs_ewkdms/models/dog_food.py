from odoo import api, fields, models


class DogFood(models.Model):
    _name = 'dog.food'
    _description = 'shit dog food'

    name = fields.Char()
