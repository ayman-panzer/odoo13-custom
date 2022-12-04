from odoo import models, fields


class Cars (models.Model):
    _name = "cars.cars"

    name =  fields.Char(string="Driver Name",required=True, help="Enter the name", default='truk', translate=True)
    car_plate  = fields.Char(string="car number", help="Enter the number", default=1134550)
    color = fields.Char(help="Enter the car color")
    car_load  = fields.Char(help="Enter the car load", default='10000kg')
    heavy_vehicle = fields.Boolean()
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done')], default='draft')

    def set_done(self):
        self.state = "done"


    def set_confirm(self):
       self.state = "confirm"


    def set_draft(self):
        self.state = "draft"

    def set_heavy(self):

        if self.heavy_vehicle == True :
            self.heavy_vehicle = False
        elif self.heavy_vehicle == False :
            self.heavy_vehicle = True