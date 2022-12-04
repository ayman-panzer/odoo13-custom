from odoo import models, fields


class Cars (models.Model):
    _inherit = "sale.order"

    notes =fields.Char()
    driver = fields.Many2one("em.em")


    def set_draft(self):
        self.state= 'draft'




