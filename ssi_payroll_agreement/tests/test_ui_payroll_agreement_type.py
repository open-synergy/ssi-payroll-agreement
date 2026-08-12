# Copyright 2026 OpenSynergy Indonesia
# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import HttpSavepointCase, tagged


@tagged("post_install", "-at_install")
class TestUiPayrollAgreementType(HttpSavepointCase):
    """Tour tests for the ``payroll_agreement_type`` work instructions."""

    @classmethod
    def setUpClass(cls):
        """Create the sequence template used by the Generate Code step.

        Realizes the ``01-create.md`` Pre-Condition ``Config`` item: an
        active ``sequence.template`` for ``payroll_agreement_type``, with
        ``initial_string`` ``/`` so the tour's own ``/`` entry in **Code**
        is eligible for generation. No ``sequence.template`` data record
        is added to the module itself -- this fixture is test-only.
        """
        super().setUpClass()
        cls.admin = cls.env.ref("base.user_admin")

        sequence = (
            cls.env["ir.sequence"]
            .with_user(cls.admin)
            .create(
                {
                    "name": "Tour Payroll Agreement Type Sequence",
                    "prefix": "TOURPAT-",
                    "padding": 4,
                }
            )
        )
        model = cls.env["ir.model"].search(
            [("model", "=", "payroll_agreement_type")], limit=1
        )
        code_field = cls.env["ir.model.fields"].search(
            [("model_id", "=", model.id), ("name", "=", "code")], limit=1
        )
        date_field = cls.env["ir.model.fields"].search(
            [("model_id", "=", model.id), ("name", "=", "create_date")], limit=1
        )
        cls.env["sequence.template"].with_user(cls.admin).create(
            {
                "name": "Tour Standard",
                "model_id": model.id,
                "initial_string": "/",
                "sequence_field_id": code_field.id,
                "date_field_id": date_field.id,
                "computation_method": "use_python",
                "python_code": "result = True",
                "sequence_selection_method": "use_sequence",
                "sequence_id": sequence.id,
            }
        )

    def test_create(self):
        """Run the create tour for ``payroll_agreement_type``.

        Pre-Condition IK (Access) is already satisfied: the
        ``payroll_agreement_type_group`` is granted to ``base.user_admin``
        by ``security/res_group_data.xml``, so no extra setup is needed.
        Pre-Condition IK (Config) is set up in :meth:`setUpClass`.

        IK: docs/payroll_agreement_type/01-create.md
        """
        self.start_tour(
            "/web", "ssi_payroll_agreement_payroll_agreement_type_create", login="admin"
        )
