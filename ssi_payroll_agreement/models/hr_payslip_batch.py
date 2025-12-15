# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class HrPayslipBatch(models.Model):
    _name = "hr.payslip_batch"
    _inherit = [
        "hr.payslip_batch",
    ]

    def _trigger_onchange(self, payslip):
        self.ensure_one()
        _super = super(HrPayslipBatch, self)
        res = _super._trigger_onchange(payslip)
        payslip.onchange_payroll_agreement_id()
        payslip.onchange_aggrement_structure_id()
        payslip.onchange_structure_id()