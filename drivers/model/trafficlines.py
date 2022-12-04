from odoo import models, fields


class Trafficlines (models.Model):
    _name = "trafficlines.trafficlines"
    _rec_name="traffic_lines"

    traffic_lines = fields.Char(string="Traffic Name",required=True)
    start_time = fields.Float(required=True,help=".زمن الانطلاق")
    end_time = fields.Float(required=True)
    Available = fields.Boolean(default=True ,required=True)
    driver = fields.Many2one("em.em")
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done')], default='draft')



    def set_done(self):
        self.state = "done"


    def set_confirm(self):
       self.state = "confirm"


    def set_draft(self):
        self.state = "draft"

