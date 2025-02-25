# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo 16 Budget Management',
    'author': 'Odoo Mates, Odoo SA',
    'category': 'Accounting',
    'version': '16.0.1.0.0',
    'description': """Use budgets to compare actual with expected revenues and costs""",
    'summary': 'Odoo 16 Budget Management',
    'sequence': 10,
    'website': 'https://www.odoomates.tech',
    'depends': ['account'],
    'license': 'LGPL-3',
    'data': [
        'security/account_budget_security.xml',
        'security/cg_budget_security.xml',
        'security/ir.model.access.csv',
        'views/account_analytic_account_views.xml',
        'views/account_budget_views.xml',
        'views/cg_budget_post_views.xml',
        'views/cg_budget_expense_views.xml',
        'views/res_config_settings_views.xml',
    ],
    "images": ['static/description/banner.gif'],
    'demo': ['data/account_budget_demo.xml'],
}
