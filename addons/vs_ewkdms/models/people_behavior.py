from odoo import api, fields, models


class PeopleBehavior(models.Model):
    _name = 'people.behavior'
    _description = 'unknow people behavior'

    name = fields.Char()
