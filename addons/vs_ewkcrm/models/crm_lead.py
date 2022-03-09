from datetime import timedelta

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class CrmStage(models.Model):
    _inherit = 'crm.stage'

    probability = fields.Float(string='Probability', digits=(3, 2))
    default_activity_id = fields.Many2one(
        'mail.activity.type', 'Default Activity',
        default=lambda self: self.env.ref('mail.mail_activity_data_todo'),
        domain=lambda self: ['|', ('res_model_id', '=', False), (
            'res_model_id', '=', self.env['ir.model']._get('crm.lead').id)],
        ondelete='restrict'
    )
    due_within = fields.Integer(string='Due Within (Days)')


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    verified = fields.Boolean(tracking=10)
    tag_ids = fields.Many2many(
        'crm.tag', 'crm_tag_rel', 'lead_id', 'tag_id', string='Interests',
        tracking=20,
        help="Classify and analyze your lead/opportunity categories like: Training, Service")

    def action_set_won(self):
        """ prevent conversion without verification """
        for lead in self:
            if not lead.verified and len(lead.tag_ids) == 0:
                raise UserError(
                    _('Please verify primary phone number & make sure to add an interest'))
        return super(CrmLead, self).action_set_won()

    def _create_activities(self):
        for lead in self:
            if lead.stage_id and lead.stage_id.default_activity_id:
                date_deadline = (fields.Date.today() + timedelta(
                    days=lead.stage_id.due_within))
                act_id = lead.stage_id.default_activity_id.id
                v = self.env['mail.activity'].create({
                    'date_deadline': date_deadline,
                    'user_id': self.env.user.id,
                    'activity_type_id': act_id,
                    'res_model_id': self.env['ir.model']._get('crm.lead').id,
                    'res_id': lead.id,
                })
