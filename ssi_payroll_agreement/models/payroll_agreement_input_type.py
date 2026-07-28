# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import fields, models


class PayrollAgreementInputType(models.Model):
    """
    Master data listing the input types a payroll agreement's
    ``input_line_ids`` can reference (e.g. housing or transport
    allowances), identified by ``code`` and read from salary rule
    Python code via ``aggr_inputs``.
    """

    _name = "payroll_agreement_input_type"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Payroll Agreement Input Type"

    default_amount = fields.Float(
        string="Default Amount",
        default=0.0,
    )
