# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import api, fields, models

from odoo.addons.ssi_hr_payroll.models.hr_payslip import BrowsableObject


class AgreementInputLine(BrowsableObject):
    def sum(self, code):
        self.env.cr.execute(
            """
            SELECT sum(b.amount) as sum
            FROM payroll_agreement as a
            JOIN payroll_agreement_input as b ON a.id=b.employee_id
            JOIN payroll_agreement_input_type as c ON b.input_type_id=c.id
            WHERE a.id = %s AND c.code = %s""",
            (self.employee_id, code),
        )
        return self.env.cr.fetchone()[0] or 0.0


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    @api.depends(
        "employee_id",
        "employee_id.method",
    )
    def _compute_payroll_agreement_id(self):
        for record in self:
            if record.employee_id:
                record.payroll_agreement_id = record.employee_id.payroll_agreement_id

    payroll_agreement_id = fields.Many2one(
        comodel_name="payroll_agreement",
        compute="_compute_payroll_agreement_id",
        string="Active Agreement",
        store=True,
    )
    method = fields.Selection(
        related="employee_id.method",
    )

    def _get_salary_rules(self):
        _super = super(HrPayslip, self)
        res = _super._get_salary_rules()
        if self.method == "agreement":
            res = self.payroll_agreement_id.salary_rule_ids
        return res

    def _get_base_localdict(self, payslip):
        _super = super(HrPayslip, self)
        res = _super._get_base_localdict(payslip)
        aggr_inputs_dict = {}

        for aggr_input_line in self.payroll_agreement_id.input_line_ids:
            aggr_inputs_dict[aggr_input_line.input_type_id.code] = aggr_input_line

        aggr_inputs = AgreementInputLine(
            payslip.employee_id.id, aggr_inputs_dict, self.env
        )
        if aggr_inputs:
            res["aggr_inputs"] = aggr_inputs

        return res
