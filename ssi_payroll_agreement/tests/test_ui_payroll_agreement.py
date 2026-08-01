# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPayrollAgreement(HttpSavepointCase):
    """Tour tests for the ``payroll_agreement`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create master data and one agreement per tour's pre-state.

        ``base.user_admin`` is already a member of
        ``payroll_agreement_validator_group`` (which implies the
        ``User`` group) via ``security/res_group_data.xml``, so it can
        run every tour below without extra group setup. Every
        scenario that reaches ``open`` uses its own employee --
        ``_constrains_open`` forbids two ``open`` agreements for the
        same employee -- and every other scenario also gets a
        dedicated employee so its list row can be found by "Employee"
        column text alone.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")

        cls.agreement_type = (
            cls.env["payroll_agreement_type"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "Tour PA Agreement Type",
                    "code": "TOURPAAT",
                }
            )
        )
        cls.salary_structure = (
            cls.env["hr.salary_structure"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "Tour PA Salary Structure",
                    "code": "TOURPASS",
                }
            )
        )
        cls.input_type = (
            cls.env["payroll_agreement_input_type"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "Tour PA Input Type",
                    "code": "TOURPAIT",
                    "default_amount": 1000.0,
                }
            )
        )
        # Global cancel reason so it is selectable regardless of whether
        # ssi_transaction_cancel_mixin demo data is loaded.
        cls.cancel_reason = (
            cls.env["base.cancel_reason"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "Tour PA Cancel Reason",
                    "code": "TOURPACR",
                    "global_use": True,
                }
            )
        )

        def _create_employee(label):
            """Create a dedicated employee for one tour scenario.

            :param label: short scenario name, e.g. ``"Confirm"``
            :return: the new ``hr.employee`` record
            """
            return (
                cls.env["hr.employee"]
                .with_user(cls.admin)
                .create({"name": "Tour PA Employee %s" % label})
            )

        def _create_agreement(label):
            """Create a Draft agreement for one tour scenario.

            :param label: short scenario name, e.g. ``"Confirm"``
            :return: the new ``payroll_agreement`` record, in Draft,
                linked to a dedicated employee named after ``label``
            """
            employee = _create_employee(label)
            return (
                cls.env["payroll_agreement"]
                .with_user(cls.admin)
                .create(
                    {
                        "employee_id": employee.id,
                        "type_id": cls.agreement_type.id,
                        "salary_structure_id": cls.salary_structure.id,
                        "date": "2026-01-01",
                    }
                )
            )

        # Pre-Condition 01-create.md: only the employee to pick in the
        # New form is needed here -- the agreement itself is created
        # by the tour.
        cls.employee_create = _create_employee("Create")

        # Pre-Condition 04-confirm.md: Draft.
        cls.agreement_confirm = _create_agreement("Confirm")

        # Pre-Condition 05-approve.md / 06-reject.md: Waiting for
        # Approval.
        cls.agreement_approve = _create_agreement("Approve")
        cls.agreement_approve.action_confirm()

        cls.agreement_reject = _create_agreement("Reject")
        cls.agreement_reject.action_confirm()

        # Pre-Condition 07-start.md: Ready to Process. There is a
        # single approval level, so action_approve_approval() also
        # auto-transitions confirm -> ready via
        # _after_approved_method. invalidate_cache() is required
        # because approve_ok's additional_python_code reads
        # active_approver_user_ids, which is computed from the
        # approval.approval records action_confirm() just created.
        cls.agreement_start = _create_agreement("Start")
        cls.agreement_start.action_confirm()
        cls.agreement_start.invalidate_cache()
        cls.agreement_start.action_approve_approval()

        # Pre-Condition 09-finish.md: In Progress. A second
        # invalidate_cache() is needed before action_open(): open_ok
        # is computed from policy.template, and the "ready" state
        # just written by the previous action_ready() call (triggered
        # internally by action_approve_approval()) must be visible
        # before open_ok is (re)computed for the current environment.
        cls.agreement_finish = _create_agreement("Finish")
        cls.agreement_finish.action_confirm()
        cls.agreement_finish.invalidate_cache()
        cls.agreement_finish.action_approve_approval()
        cls.agreement_finish.invalidate_cache()
        cls.agreement_finish.action_open()

        # Pre-Condition 10-cancel.md: Draft (one of the allowed
        # states).
        cls.agreement_cancel = _create_agreement("Cancel")

        # Pre-Condition 12-restart.md: Rejected.
        cls.agreement_restart = _create_agreement("Restart")
        cls.agreement_restart.action_confirm()
        cls.agreement_restart.invalidate_cache()
        cls.agreement_restart.action_reject_approval()

    def test_create(self):
        """Run the create tour for ``payroll_agreement``.

        IK: docs/payroll_agreement/01-create.md
        """
        self.start_tour(
            "/web",
            "ssi_payroll_agreement_payroll_agreement_create",
            login="admin",
        )

    def test_confirm(self):
        """Run the confirm tour for ``payroll_agreement``.

        IK: docs/payroll_agreement/04-confirm.md
        """
        self.start_tour(
            "/web",
            "ssi_payroll_agreement_payroll_agreement_confirm",
            login="admin",
        )

    def test_approve(self):
        """Run the approve tour for ``payroll_agreement``.

        IK: docs/payroll_agreement/05-approve.md
        """
        self.start_tour(
            "/web",
            "ssi_payroll_agreement_payroll_agreement_approve",
            login="admin",
        )

    def test_reject(self):
        """Run the reject tour for ``payroll_agreement``.

        IK: docs/payroll_agreement/06-reject.md
        """
        self.start_tour(
            "/web",
            "ssi_payroll_agreement_payroll_agreement_reject",
            login="admin",
        )

    def test_start(self):
        """Run the start tour for ``payroll_agreement``.

        IK: docs/payroll_agreement/07-start.md
        """
        self.start_tour(
            "/web",
            "ssi_payroll_agreement_payroll_agreement_start",
            login="admin",
        )

    def test_finish(self):
        """Run the finish tour for ``payroll_agreement``.

        IK: docs/payroll_agreement/09-finish.md
        """
        self.start_tour(
            "/web",
            "ssi_payroll_agreement_payroll_agreement_finish",
            login="admin",
        )

    def test_cancel(self):
        """Run the cancel tour for ``payroll_agreement``.

        IK: docs/payroll_agreement/10-cancel.md
        """
        self.start_tour(
            "/web",
            "ssi_payroll_agreement_payroll_agreement_cancel",
            login="admin",
        )

    def test_restart(self):
        """Run the restart tour for ``payroll_agreement``.

        IK: docs/payroll_agreement/12-restart.md
        """
        self.start_tour(
            "/web",
            "ssi_payroll_agreement_payroll_agreement_restart",
            login="admin",
        )
