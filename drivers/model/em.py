from odoo import models, fields


class em (models.Model):
    _name = "em.em"

    name =  fields.Char(string="Name",required=True, help="Enter the name", default='em', translate=True)
    phone_number  = fields.Char(string="phone number", help="Enter the number", default="+249")
    address  = fields.Char(help="Enter the address", default='sudan')
    salary = fields.Float()
    birthDate = fields.Date(help="Enter the birthdate",required=True)
    Section = fields.Char(help="Enter the Section")
    Years_of_Experience = fields.Integer()
    image = fields.Binary("Image", help="Select image here")
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done')], default='draft')


    def set_done(self):
        self.state = "done"


    def set_confirm(self):
       self.state = "confirm"


    def set_draft(self):
        self.state = "draft"

