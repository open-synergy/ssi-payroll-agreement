# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPayrollAgreementDocumenso(HttpSavepointCase):
    """Tour test for the ``payroll_agreement`` Documenso signing delta."""

    @classmethod
    def setUpClass(cls):
        """Create one payroll agreement already Waiting for Approval.

        ``base.user_admin`` is already a member of
        ``payroll_agreement_validator_group`` (which implies the
        ``User`` group) via ``ssi_payroll_agreement``'s
        ``security/res_group_data.xml``, so it can confirm the record
        directly, without extra group setup. The record is moved to
        ``confirm`` here in Python (``action_confirm()``), not via UI
        clicks, per Keputusan Desain (issue
        open-synergy/ssi-payroll-agreement#25).
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")

        agreement_type = (
            cls.env["payroll_agreement_type"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "Tour PA Documenso Agreement Type",
                    "code": "TOURPADAT",
                }
            )
        )
        salary_structure = (
            cls.env["hr.salary_structure"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "Tour PA Documenso Salary Structure",
                    "code": "TOURPADSS",
                }
            )
        )
        employee = (
            cls.env["hr.employee"]
            .with_user(cls.admin)
            .create({"name": "Tour PA Documenso Employee Approve"})
        )

        # Pre-Condition IK 05-approve.md (delta): record already
        # Waiting for Approval. The "Standard" approval template used
        # by ssi_payroll_agreement demo data has no Documenso Signing
        # Template configured, so the Signature Requests tab is
        # present (``_documenso_signing_create_page = True``) but the
        # base Approve/OK Flow is unaffected -- this tour does not
        # exercise it.
        cls.agreement_approve = (
            cls.env["payroll_agreement"]
            .with_user(cls.admin)
            .create(
                {
                    "employee_id": employee.id,
                    "type_id": agreement_type.id,
                    "salary_structure_id": salary_structure.id,
                    "date": "2026-01-01",
                }
            )
        )
        cls.agreement_approve.action_confirm()

    def test_approve(self):
        """Run the approve tour for the Documenso signing delta.

        IK: docs/payroll_agreement/05-approve.md (E2a delta --
        Modified Flow)
        """
        self.start_tour(
            "/web",
            "ssi_payroll_agreement_documenso_signing_payroll_agreement_approve",
            login="admin",
        )
