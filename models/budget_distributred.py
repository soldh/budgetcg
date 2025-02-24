from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BudgetDistribution(models.Model):
    _name = 'budget.distribution'
    _description = 'Budget Distribution'

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    planned_amount = fields.Monetary(string='Planned Amount', currency_field='currency_id')
    practical_amount = fields.Monetary(string='Practical Amount', currency_field='currency_id')
    left_to_spend = fields.Monetary(string='Left to Spend', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)