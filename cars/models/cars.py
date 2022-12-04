from odoo import models, fields, api


class cars(models.Model):
    _name = 'cars.cars'
    _description = 'cars.cars'

    name = fields.Char()
    km = fields.Integer()
    description = fields.Text()

