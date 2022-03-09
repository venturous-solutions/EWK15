from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    dog_id = fields.Many2one('dog.dog', required=True, ondelete='cascade')
