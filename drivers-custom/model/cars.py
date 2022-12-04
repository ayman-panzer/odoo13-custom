from odoo import models, fields


class Cars (models.Model):
    _inherit = "cars.cars"

    descriptions=fields.Text()
    km          =fields.Float()



