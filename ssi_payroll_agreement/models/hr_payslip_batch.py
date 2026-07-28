# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import models


class HrPayslipBatch(models.Model):
    """
    Re-triggers the payroll agreement onchanges on payslips created
    from a batch, so they resolve their agreement/salary structure
    the same way a manually opened payslip form would.
    """

    _name = "hr.payslip_batch"
    _inherit = [
        "hr.payslip_batch",
    ]

    def _trigger_onchange(self, payslip):
        """Also trigger the payroll agreement onchanges on the payslip.

        Overridden because ``super()._trigger_onchange`` predates
        the ``payroll_agreement_id``/``structure_id`` onchanges added
        by this module, so batch-generated payslips would otherwise
        never resolve the employee's payroll agreement or its
        salary structure.
        """
        self.ensure_one()
        _super = super(HrPayslipBatch, self)
        _super._trigger_onchange(payslip)
        payslip.onchange_payroll_agreement_id()
        payslip.onchange_aggrement_structure_id()
