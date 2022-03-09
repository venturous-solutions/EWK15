from odoo import _, api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    dog_id = fields.Many2one('dog.dog', 'Dog', ondelete='set null',)
    breed = fields.Many2one(related='dog_id.breed', readonly=True)
    gender = fields.Selection(related='dog_id.gender', readonly=True)
    dog_birth_date = fields.Date(related='dog_id.birth_date', readonly=True)
    info_complete = fields.Boolean(
        compute='_compute_info_completion', store=True)

    @api.depends('phone', 'verified', 'dog_id')
    def _compute_info_completion(self):
        for lead in self:
            if lead.phone and lead.verified and lead.dog_id:
                lead.info_complete = True
