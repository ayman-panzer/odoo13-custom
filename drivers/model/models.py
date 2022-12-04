from odoo import models, fields


class Drivers (models.Model):
    _name = "drivers.drivers"

    name =  fields.Char(string="Driver Name",required=True, help="Enter the name", default='Ayman', translate=True)
    age  = fields.Integer(string="Drivers Age", help="Enter the age", default=22)
    birthDate = fields.Date(help="Enter the birthdate",required=True)
    address  = fields.Char(help="Enter the address", default='sudan')
    is_GL = fields.Boolean(string="International license?", help="Enter the info", default=True)
    salary = fields.Float(default=5000, readonly=False)
    state = fields.Selection([('draft','Draft'),('confirm','Confirm'),('done','Done')] , default='draft')

    def set_salary(self):
        # print("set salary\n"*10)

        if self.salary + 5000 < 50000 :
            self.salary = self.salary +5000
        else:self.salary = 50000



        
    def test(self):
       if self.state == 'draft':
           self.state = 'confirm'
       elif self.state == 'confirm':
           self.state = 'done'
       else:
        self.state = 'draft'
