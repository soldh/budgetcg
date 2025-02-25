from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools.populate import compute


class BudgetDistribution(models.Model):
    _name = 'cg.budget.distribution'
    _description = 'Budget Distribution'

    name =  fields.Char(string='Distribute code', required=True)
    budget_post_id = fields.Many2one('account.budget.post', string="Budget Post", ondelete='cascade')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    planned_amount = fields.Monetary(string='Planned Amount', currency_field='currency_id')
    practical_amount = fields.Monetary(string='Practical Amount', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    left_to_spend = fields.Monetary(string='Left to Spend', currency_field='currency_id', readonly=True, compute='_compute_left_to_spend')

    def _compute_left_to_spend(self):
        for record in self:
            record.left_to_spend = record.planned_amount - record.practical_amount

