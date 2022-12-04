from odoo import models, fields


class Driversm (models.Model):
    _inherit = "drivers.drivers"


    irregularities = fields.Char()
    work_injury    = fields.Char()


