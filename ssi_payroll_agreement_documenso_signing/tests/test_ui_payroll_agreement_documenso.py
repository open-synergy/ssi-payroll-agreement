# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPayrollAgreementDocumenso(HttpSavepointCase):
    """Tour test for the ``payroll_agreement`` Documenso signing delta."""

    @classmethod
    def setUpClass(cls):
        """Create fixtures for both tours in this test class.

        ``base.user_admin`` is already a member of
        ``payroll_agreement_validator_group`` (which implies the
        ``User`` group) via ``ssi_payroll_agreement``'s
        ``security/res_group_data.xml``, so it can confirm the record
        directly, without extra group setup. One payroll agreement is
        moved to ``confirm`` here in Python (``action_confirm()``),
        not via UI clicks, per Keputusan Desain (issue
        open-synergy/ssi-payroll-agreement#25). A second, separate
        payroll agreement plus an active Documenso backend and signing
        template are created for the New Signing Request tour (issue
        open-synergy/ssi-payroll-agreement#36).
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

        # Pre-Condition IK 06-create-signing-request.md: an active
        # documenso.backend and an active documenso.signing.template
        # (Source Model = payroll_agreement) must exist, plus a
        # payroll_agreement record whose form shows the Signature
        # Requests tab (any status -- the tab is unconditional).
        cls.documenso_backend = (
            cls.env["documenso.backend"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "Tour PA Documenso Backend",
                    "base_url": "https://documenso.example.com",
                    "api_key": "tour-test-api-key",
                }
            )
        )
        # ``documenso.signature.request.py3o_report_id`` is required, and the
        # wizard copies it from the signing template's ``py3o_report_id`` on
        # confirm -- without a matching report the create() call in
        # ``action_confirm`` raises a validation error and the wizard never
        # closes. ``ssi_payroll_agreement`` ships no py3o report of its own,
        # so a minimal one is created here for the tour's fixture only.
        cls.documenso_py3o_report = (
            cls.env["ir.actions.report"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "Tour PA Documenso Py3o Report",
                    "model": "payroll_agreement",
                    "report_name": "ssi_payroll_agreement_documenso_signing.tour_report",
                    "report_type": "py3o",
                    "py3o_filetype": "pdf",
                }
            )
        )
        cls.documenso_signing_template = (
            cls.env["documenso.signing.template"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "Tour PA Documenso Signing Template",
                    "code": "TOURPADST",
                    "res_model": "payroll_agreement",
                    "py3o_report_id": cls.documenso_py3o_report.id,
                }
            )
        )
        employee_signing_request = (
            cls.env["hr.employee"]
            .with_user(cls.admin)
            .create({"name": "Tour PA Documenso Employee Signing Request"})
        )
        cls.agreement_signing_request = (
            cls.env["payroll_agreement"]
            .with_user(cls.admin)
            .create(
                {
                    "employee_id": employee_signing_request.id,
                    "type_id": agreement_type.id,
                    "salary_structure_id": salary_structure.id,
                    "date": "2026-01-01",
                }
            )
        )

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

    def test_create_signing_request(self):
        """Run the New Signing Request tour on payroll_agreement.

        IK: docs/payroll_agreement/06-create-signing-request.md (E3 --
        new action). The tour stops once the new row appears on the
        Signature Requests page; it does not click into the created
        request's own form to send it to Documenso over the network.
        """
        self.start_tour(
            "/web",
            "ssi_payroll_agreement_documenso_signing_payroll_agreement"
            "_create_signing_request",
            login="admin",
        )
