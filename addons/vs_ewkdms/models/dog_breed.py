from odoo import api, fields, models


class DogBreed(models.Model):
    _name = 'dog.breed'
    _description = 'shit dog breed'

    name = fields.Char()
