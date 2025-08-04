from odoo import api, fields, models
#from odoo import ValidationError
from odoo.exceptions import ValidationError

from datetime import date

class Lease(models.Model):
    _name = 'property.lease'
    _description = 'Lease'

    lease_name = fields.Char(string="Lease Name", compute='_compute_lease_name', store='True')
    tenant_id = fields.Many2one('property.tenant', string='Tenant', required = True)
    property_id = fields.Many2one('property.management', string ='Property', required = True)
    start_date = fields.Date(string = 'Start Date', required = True)
    end_date = fields.Date(string = 'End Date', required = True)
    monthly_rent = fields.Float(string="Monthly Rent", required=True )
    #,readonly="state == 'rented'"
    state = fields.Selection([('draft', 'Draft'), ('active', 'Active'), ('expired', 'Expired')], string='Status', default='draft')

    lease_pdf= fields.Binary('PDF')
    rent_payment_ids = fields.One2many('rent.payment', 'lease_id', string='rent Payments')

    #compute lease name
    @api.depends('tenant_id', 'property_id')
    def _compute_lease_name(self):
        for rec in self:
            if rec.tenant_id and rec.property_id:
                rec.lease_name = f"{rec.tenant_id.name} - {rec.property_id.name}"
            else:
                rec.lease_name = "lease"

    #onchange state
    @api.onchange('property_id')
    def _onchange_property_id(self):
        if self.property_id:
            self.monthly_rent = self.property_id.price_per_month

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for rec in self:
            if rec.start_date and rec.end_date and rec.end_date <= rec.start_date:
                raise ValidationError("End date must be after start date")
            
    @api.model
    def create(self, vals):
        record = super().create(vals)
        record.property_id.status = 'rented'
        return record

    def expire_lease(self):
        for rec in self:
            if rec.end_date < fields.Date.today():
                rec.state = 'expired'

    # def print_xlsx_report(self):
    #     return self.env.ref('property_management.lease_xlsx_report').report_action(self)