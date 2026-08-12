# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPayrollAgreementInputType(HttpSavepointCase):
    """Tour tests for the ``payroll_agreement_input_type`` work instructions."""

    def test_create(self):
        """Run the create tour for ``payroll_agreement_input_type``.

        Pre-Condition IK (Access) is already satisfied: the
        ``payroll_agreement_input_type_configurator_group`` is granted to
        ``base.user_admin`` by ``security/res_group_data.xml``, so no extra
        setup is needed.

        IK: docs/payroll_agreement_input_type/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_payroll_agreement_payroll_agreement_input_type_create",
            login="admin",
        )
