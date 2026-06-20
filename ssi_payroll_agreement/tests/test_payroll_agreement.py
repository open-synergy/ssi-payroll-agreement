# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import Form, tagged


@tagged("post_install", "-at_install")
class TestPayrollAgreement(YamlTransactionCase):
    def test_payroll_agreement(self):
        self.run_yaml_scenario("test_data_payroll_agreement.yaml")

    def test_onchange_input_type_id(self):
        """When input_type_id is set, amount should be updated with default_amount."""
        input_type = self.env["payroll_agreement_input_type"].create(
            {
                "name": "Test Onchange Input Type",
                "code": "ONCHT001",
                "default_amount": 2500.0,
            }
        )
        agreement_type = self.env["payroll_agreement_type"].create(
            {
                "name": "Test Onchange Agreement Type",
                "code": "ONCHAT001",
            }
        )
        employee = self.env["hr.employee"].create({"name": "Test Onchange Employee PA"})
        salary_structure = self.env["hr.salary_structure"].create(
            {
                "name": "Test Onchange Salary Structure",
                "code": "ONCHSTR001",
            }
        )
        import datetime

        agreement = self.env["payroll_agreement"].create(
            {
                "employee_id": employee.id,
                "type_id": agreement_type.id,
                "salary_structure_id": salary_structure.id,
                "date": datetime.date.today(),
            }
        )
        form = Form(agreement)
        with form.input_line_ids.new() as line:
            line.input_type_id = input_type
            self.assertAlmostEqual(line.amount, 2500.0)
