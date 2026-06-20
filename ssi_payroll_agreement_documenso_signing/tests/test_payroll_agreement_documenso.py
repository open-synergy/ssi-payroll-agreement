# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestPayrollAgreementDocumenso(YamlTransactionCase):
    def test_payroll_agreement_documenso(self):
        self.run_yaml_scenario("test_data_payroll_agreement_documenso.yaml")
