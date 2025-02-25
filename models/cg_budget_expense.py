from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BudgetExpense(models.Model):
    _name = 'cg.budget.expense'
    _description = 'Budget Expense'
    _inherit = ['mail.thread']

    name = fields.Char(string='Name', required=True)
    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account')
    budget_id = fields.Many2one(comodel_name="crossovered.budget", required=True)
    description = fields.Char(string="Deskripsi Pengajuan")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('cancel', 'Cancelled'),
        ('waiting_for_validate', 'Waiting for validate'),
        ('validate', 'Validated'),
        ('waiting_for_review', 'Waiting for Review'),
        ('reviewed', 'Reviewed'),
        ('done', 'Done'),
        ('reject', 'Reject')
    ], 'Status', default='draft', index=True, required=True, readonly=True, copy=False, tracking=True)


    def action_confirm(self):
        self.write({'state': 'waiting_for_validate'})

    def action_reject(self):
        self.write({'state': 'reject'})

    def action_cancel(self):
        self.write({'state': 'cancel'})

# class BudgetExpenseLine(models.Model):
#     _name = 'budget.expense.line'
#     _description = 'Budget Expense Line'




