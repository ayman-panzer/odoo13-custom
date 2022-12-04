from odoo import models, fields


class Trafficlines (models.Model):
    _inherit = "trafficlines.trafficlines"

    special_delivery = fields.Char()
    extra_pay        = fields.Char()


