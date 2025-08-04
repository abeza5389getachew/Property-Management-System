from odoo import api, fields, models
from datetime import date

class RentPayment(models.Model):
    _name = "rent.payment"
    _description = "Rent Payment"

    lease_id = fields.Many2one('property.lease', string='Lease', required = True)
    payment_date = fields.Date(string = 'Payment Date', required=True)
    currency_id=fields.Many2one('res.currency',string="Currency")
    amount_paid = fields.Monetary(string = 'Amount paid', required=True)
    status = fields.Selection([('paid', 'Paid'), ('unpaid', 'Unpaid')], string = 'State', required = True)
    note = fields.Text(string = 'Note')