# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPayrollAgreement(HttpSavepointCase):
    """Tour test for the create-time Operating Unit field."""

    @classmethod
    def setUpClass(cls):
        """Grant ``admin`` the multi operating unit group.

        Pre-Condition IK: the Operating Unit field is gated by
        ``groups="operating_unit.group_multi_operating_unit"`` in the
        form view -- without membership, the field is never rendered
        and the delta assertion would never find it. ``admin`` also
        needs at least one operating unit assigned so the field has a
        meaningful (non-empty) allowed set.

        Pre-Condition is set up in ``setUpClass``, matching the
        sibling tour test in this repository
        (``ssi_payroll_agreement/tests/test_ui_payroll_agreement.py``).
        """
        super().setUpClass()
        cls.user_admin = cls.env.ref("base.user_admin")
        operating_unit_partner = cls.env["res.partner"].create(
            {"name": "Tour PA OU Partner"}
        )
        cls.operating_unit = cls.env["operating.unit"].create(
            {
                "name": "Tour PA Operating Unit",
                "code": "TPAOU",
                "partner_id": operating_unit_partner.id,
            }
        )
        cls.env.ref("operating_unit.group_multi_operating_unit").sudo().write(
            {"users": [(4, cls.user_admin.id)]}
        )
        cls.user_admin.sudo().write(
            {
                "assigned_operating_unit_ids": [(4, cls.operating_unit.id)],
                "default_operating_unit_id": cls.operating_unit.id,
            }
        )

    def test_create(self):
        """Run the create tour for ``payroll_agreement``.

        IK: docs/payroll_agreement/01-create.md (E1 delta -- Additional
        Fields)
        """
        self.start_tour(
            "/web",
            "ssi_payroll_agreement_operating_unit_payroll_agreement_create",
            login="admin",
        )
