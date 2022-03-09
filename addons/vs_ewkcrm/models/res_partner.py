from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'res.partner'

    phone = fields.Char('Primary Phone', tracking=2)
    mobile = fields.Char('Secondary Phone')
    whatsapp = fields.Char('Whatsapp Number')
