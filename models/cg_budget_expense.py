from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BudgetExpense(models.Model):
    _name = 'cg.budget.expense'
    _description = 'Budget Expense'
    _inherit = ['mail.thread']

    name = fields.Char(string='Name', required=True)
    expense_date = fields.Date(string='Tanggal Pengajuan', default=fields.Date.context_today, readonly=True)
    user_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user, readonly=True)
    amount = fields.Monetary(string='Jumlah Pengajuan', currency_field='currency_id', required=True, tracking=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    analytic_account_id = fields.Many2one('account.analytic.account', 'Departement')
    budget_id = fields.Many2one(comodel_name="crossovered.budget", required=True)
    budget_position_reference_id = fields.Many2one(comodel_name="account.budget.post", required=True)
    budget_distribution_id = fields.Many2one(comodel_name="cg.budget.distribution", required=True, tracking=True)
    company_id = fields.Many2one(comodel_name="res.company", string="Company", related="budget_distribution_id.company_id", store=True)
    planned_amount = fields.Monetary(string='Planned Amount', currency_field='currency_id', related="budget_distribution_id.planned_amount", store=True)
    remaining_amount = fields.Monetary(string='Remaining Amount', currency_field='currency_id', related="budget_distribution_id.left_to_spend", store=True)
    description = fields.Char(string="Deskripsi Pengajuan")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting_for_validate', 'Waiting for validate'),
        ('validate', 'Validated'),
        ('waiting_for_review', 'Waiting for Review'),
        ('reviewed', 'Reviewed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
        ('reject', 'Reject')
    ], 'Status', default='draft', index=True, required=True, readonly=True, copy=False, tracking=True)


    def action_confirm(self):
        self.write({'state': 'waiting_for_validate'})

    def action_reject(self):
        self.write({'state': 'reject'})

    def action_cancel(self):
        self.write({'state': 'cancel'})




