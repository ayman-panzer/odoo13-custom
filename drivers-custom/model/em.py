from odoo import models, fields


class em (models.Model):
    _inherit = "em.em"

    holiyday        = fields.Date()
    yearly_vacation = fields.Date()

