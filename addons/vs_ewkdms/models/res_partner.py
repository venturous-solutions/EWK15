from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    dog_ids = fields.One2many('dog.dog', 'owner_id', string='My Dogs')
