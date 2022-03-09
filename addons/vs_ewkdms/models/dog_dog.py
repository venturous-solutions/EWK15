from odoo import api, fields, models


class DogDog(models.Model):
    _name = 'dog.dog'
    _description = 'shit dog breed'

    name = fields.Char(required='True')
    display_name = fields.Char(compute='_compute_display_name')
    owner_id = fields.Many2one(
        'res.partner', string='Owner', required='True', ondelete='restrict',)
    breed = fields.Many2one('dog.breed', required='True', ondelete='restrict',)
    gender = fields.Selection([
        ('female', 'Female'),
        ('male', 'Male'),
    ])
    color = fields.Many2one('dog.color', ondelete='restrict',)
    people_beh = fields.Many2one('people.behavior')
    birth_date = fields.Date()
    estimated = fields.Boolean(help='is birth date estimated')
    food_type = fields.Many2one('dog.food')
    image = fields.Image('Image', max_width=128, max_height=128)

    @api.depends('name', 'owner_id')
    def _compute_display_name(self):
        for dog in self:
            dog.display_name = '%s - %s' % (dog.name, dog.owner_id.display_name)
