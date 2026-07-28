# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo_yaml_test import YamlTransactionCase

from odoo.tests import tagged


@tagged("post_install", "-at_install")
class TestPayrollAgreementOperatingUnit(YamlTransactionCase):
    """Cover the operating unit scoping added to ``payroll_agreement``."""

    def test_payroll_agreement_operating_unit(self):
        """Run the ``odoo-yaml-test`` scenario for this module."""
        self.run_yaml_scenario("test_data_payroll_agreement_operating_unit.yaml")
