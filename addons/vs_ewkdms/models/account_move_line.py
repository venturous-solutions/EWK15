from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'account.move.line'

    dog_id = fields.Many2one('dog.dog', ondelete='cascade')
