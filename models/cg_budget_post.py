from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CGBudgetPost(models.Model):
    _inherit = 'account.budget.post'

    budget_distribution_ids = fields.One2many(
        'cg.budget.distribution', 'budget_post_id', string="Budget Distribution"
    )
    total_planned_amount = fields.Monetary(
        string="Total Planned Amount", readonly=True, currency_field='currency_id', compute="_compute_total_planned_amount")
    total_left_to_spend = fields.Monetary(
        string="Total Left to Spend", readonly=True,currency_field='currency_id' ,compute="_compute_total_left_to_spend")
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)


    @api.depends('budget_distribution_ids')
    def _compute_total_planned_amount(self):
        for record in self:
            record.total_planned_amount = sum(record.budget_distribution_ids.mapped('planned_amount'))

    @api.depends('budget_distribution_ids')
    def _compute_total_left_to_spend(self):
        for record in self:
            record.total_left_to_spend = sum(record.budget_distribution_ids.mapped('left_to_spend'))