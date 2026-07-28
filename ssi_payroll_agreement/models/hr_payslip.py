# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

from odoo.addons.ssi_hr_payroll.models.hr_payslip import BrowsableObject


class AgreementInputLine(BrowsableObject):
    """Expose a payroll agreement's input amounts by input type code.

    Backs the ``aggr_inputs`` local variable made available to salary
    rule Python code (``condition_python`` / ``amount_python``).
    """

    def sum(self, code):
        """Sum a payroll agreement input's ``amount`` for a code.

        Reads directly from ``self.dict`` (built by
        :meth:`HrPayslip._get_base_localdict`), never from
        ``self.env.cr``. Each key maps to a ``payroll_agreement_input``
        recordset that may hold more than one row for the same code, so
        the total is computed with a recordset ``sum()``.

        :param code: ``payroll_agreement_input_type`` code to sum
        :return: summed ``amount`` as a ``float``, or ``0.0`` if the
            code is not present in the dict
        """
        if code not in self.dict:
            return 0.0
        return sum(self.dict[code].mapped("amount"))


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    payroll_agreement_id = fields.Many2one(
        string="Payroll Agreement",
        comodel_name="payroll_agreement",
        required=False,
    )
    method = fields.Selection(
        related="employee_id.method",
        compute_sudo=True,
    )

    def _get_salary_rules(self):
        _super = super(HrPayslip, self)
        res = _super._get_salary_rules()
        if self.payroll_agreement_id:
            rule_ids = self.payroll_agreement_id.salary_rule_ids
            sorted_rule_ids = rule_ids.sorted(lambda x: x.sequence)
            res = sorted_rule_ids
        return res

    def _get_base_localdict(self, payslip):
        """Add ``aggr_inputs`` to the salary rule evaluation localdict.

        ``aggr_inputs`` is an :class:`AgreementInputLine` wrapping a
        dict keyed by ``payroll_agreement_input_type.code``, where each
        value is the **recordset** of ``payroll_agreement_input`` rows
        sharing that code on the payslip's payroll agreement — rows are
        accumulated per code, never overwritten, since there is no
        unique constraint on (``payroll_agreement_id``,
        ``input_type_id``). It is the extension point salary rules use
        to read agreement input amounts via ``aggr_inputs.sum(code)``.

        :param payslip: the ``hr.payslip`` browse record being computed
        :return: the localdict returned by ``super()``, extended with
            ``aggr_inputs``
        """
        _super = super(HrPayslip, self)
        res = _super._get_base_localdict(payslip)
        aggr_inputs_dict = {}
        empty_input = self.env["payroll_agreement_input"]

        for aggr_input_line in self.payroll_agreement_id.input_line_ids:
            code = aggr_input_line.input_type_id.code
            aggr_inputs_dict[code] = (
                aggr_inputs_dict.get(code, empty_input) | aggr_input_line
            )

        aggr_inputs = AgreementInputLine(
            payslip.employee_id.id, aggr_inputs_dict, self.env
        )
        if aggr_inputs:
            res["aggr_inputs"] = aggr_inputs
        return res

    def _get_payroll_agreement(self):
        self.ensure_one()
        result = False

        if not self.employee_id.payroll_agreement_id:
            error_message = """
            Context: Payslip
            Problem: No active payroll agreement was found for employee %s.
            Solution: Please create and start a payroll agreement for this employee.
            """ % (
                self.employee_id.name
            )
            raise ValidationError(_(error_message))

        aggrements = self.employee_id.payroll_agreement_ids.filtered(
            lambda x: x.date <= self.date_start and x.state in ["open", "done"]
        )
        if aggrements:
            result = aggrements[0]
        else:
            error_message = """
            Context: Payslip
            Problem: No payroll agreement was found for %s on %s.
            Solution: Please create and start a payroll agreement for this employee.
            """ % (
                self.employee_id.name,
                self.date_start,
            )
            raise ValidationError(_(error_message))

        return result

    @api.onchange(
        "method",
        "date_start",
    )
    def onchange_payroll_agreement_id(self):
        self.payroll_agreement_id = False
        if self.method == "agreement" and self.date_start:
            self.payroll_agreement_id = self._get_payroll_agreement()

    @api.onchange(
        "payroll_agreement_id",
    )
    def onchange_aggrement_structure_id(self):
        if self.payroll_agreement_id:
            self.structure_id = self.payroll_agreement_id.salary_structure_id
        else:
            self.onchange_structure_id()

    @api.onchange(
        "employee_id",
    )
    def onchange_structure_id(self):
        self.structure_id = False
        if self.employee_id and self.method == "manual":
            self.structure_id = self.employee_id.salary_structure_id
