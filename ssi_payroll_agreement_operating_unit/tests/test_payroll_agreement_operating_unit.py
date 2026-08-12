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

    def test_ir_rule_scopes_by_operating_unit(self):
        """Restrict search results to the caller's own operating unit.

        Pure Python -- trigger P10 (L-09..L-12: assembling two users
        pinned to different operating units via
        ``assigned_operating_unit_ids``, then diffing the id sets a
        per-user ``search()`` returns, needs imperative fixture code
        and set comparisons that the YAML DSL's restricted ``EVAL:``
        sandbox and lack of loops/comprehensions cannot express).

        Covers the positive and negative branches of the issue's
        Skenario Uji: a user only sees documents scoped to their own
        operating unit, and a document with an empty
        ``operating_unit_id`` is invisible to every operating-unit-
        scoped user, including its own creator.
        """
        ou_a = self._create_operating_unit("OUACC1")
        ou_b = self._create_operating_unit("OUACC2")
        user_a = self._create_ou_scoped_user("ou_access_a", ou_a)
        user_b = self._create_ou_scoped_user("ou_access_b", ou_b)

        agreement_a = self._create_agreement(ou_a, "OUACCS1", "OUACCT1")
        agreement_b = self._create_agreement(ou_b, "OUACCS2", "OUACCT2")
        agreement_no_ou = self._create_agreement(False, "OUACCS3", "OUACCT3")
        domain = [
            (
                "id",
                "in",
                (agreement_a + agreement_b + agreement_no_ou).ids,
            )
        ]

        visible_to_a = self.env["payroll_agreement"].with_user(user_a).search(domain)
        visible_to_b = self.env["payroll_agreement"].with_user(user_b).search(domain)

        self.assertEqual(visible_to_a.ids, agreement_a.ids)
        self.assertEqual(visible_to_b.ids, agreement_b.ids)

    def test_ir_rule_ignores_users_outside_ou_group(self):
        """Leave the operating unit rule inactive outside its group.

        Pure Python -- same P10 fixture-construction trigger as
        ``test_ir_rule_scopes_by_operating_unit`` (L-09..L-12).

        Verified against ``security/ir_rule/ir_rule_data.xml``: the
        operating unit rule's ``groups`` field lists only
        ``payroll_agreement_ou_group``. In Odoo's ``ir.rule``
        algorithm, a rule scoped to a group only participates for
        users who are members of that group -- a user outside it is
        scoped solely by ``payroll_agreement_internal_user_rule``
        (``base.group_user``, self-scoped by ``employee_id``), so
        their assigned operating unit never narrows or widens what
        they can see.
        """
        ou_a = self._create_operating_unit("OUACC3")
        ou_b = self._create_operating_unit("OUACC4")
        outsider = self.env["res.users"].create(
            {
                "name": "OU Access Outsider",
                "login": "ou_access_outsider@example.com",
                "email": "ou_access_outsider@example.com",
                "groups_id": [(6, 0, [self.env.ref("base.group_user").id])],
                "assigned_operating_unit_ids": [(6, 0, [ou_a.id])],
            }
        )
        own_employee = self.env["hr.employee"].create(
            {
                "name": "OU Access Outsider Employee",
                "company_id": self.env.company.id,
                "user_id": outsider.id,
            }
        )
        other_employee = self.env["hr.employee"].create(
            {"name": "OU Access Other Employee"}
        )
        # Own document, on a *different* operating unit than the one
        # assigned to the outsider -- visible only through
        # ``payroll_agreement_internal_user_rule`` (ownership by
        # ``employee_id``), unrelated to operating unit.
        own_agreement = self._create_agreement(
            ou_b, "OUACCS4", "OUACCT4", employee=own_employee
        )
        # Someone else's document, on the *same* operating unit
        # assigned to the outsider -- must stay invisible, proving
        # the group-gated operating unit rule never activates for a
        # user outside ``payroll_agreement_ou_group``.
        other_agreement = self._create_agreement(
            ou_a, "OUACCS5", "OUACCT5", employee=other_employee
        )

        domain = [("id", "in", (own_agreement + other_agreement).ids)]
        visible = self.env["payroll_agreement"].with_user(outsider).search(domain)

        self.assertEqual(visible.ids, own_agreement.ids)

    def _create_operating_unit(self, code):
        """Create an ``operating.unit`` fixture for access tests.

        :param code: unique code for the operating unit and its
            owning partner.
        :return: the created ``operating.unit`` record.
        """
        partner = self.env["res.partner"].create(
            {"name": "OU Access Partner %s" % code}
        )
        return self.env["operating.unit"].create(
            {
                "name": "OU Access Unit %s" % code,
                "code": code,
                "partner_id": partner.id,
            }
        )

    def _create_ou_scoped_user(self, login_prefix, operating_unit):
        """Create a user scoped to a single operating unit.

        :param login_prefix: unique prefix for the user's login and
            email.
        :param operating_unit: ``operating.unit`` record assigned to
            the new user.
        :return: the created ``res.users`` record, a member of
            ``payroll_agreement_ou_group`` with
            ``assigned_operating_unit_ids`` set to
            ``operating_unit``.
        """
        ou_group = self.env.ref(
            "ssi_payroll_agreement_operating_unit.payroll_agreement_ou_group"
        )
        return self.env["res.users"].create(
            {
                "name": "OU Access User %s" % login_prefix,
                "login": "%s@example.com" % login_prefix,
                "email": "%s@example.com" % login_prefix,
                "groups_id": [
                    (
                        6,
                        0,
                        [self.env.ref("base.group_user").id, ou_group.id],
                    )
                ],
                "assigned_operating_unit_ids": [(6, 0, [operating_unit.id])],
            }
        )

    def _create_agreement(
        self, operating_unit, structure_code, type_code, employee=None
    ):
        """Create a minimal ``payroll_agreement`` fixture.

        :param operating_unit: ``operating.unit`` record to assign,
            or a falsy value to leave the field empty.
        :param structure_code: unique code for the fixture's
            ``hr.salary_structure``.
        :param type_code: unique code for the fixture's
            ``payroll_agreement_type``.
        :param employee: ``hr.employee`` record to own the
            agreement; a fresh employee is created when omitted.
        :return: the created ``payroll_agreement`` record.
        """
        if employee is None:
            employee = self.env["hr.employee"].create(
                {"name": "OU Access Employee %s" % structure_code}
            )
        salary_structure = self.env["hr.salary_structure"].create(
            {"name": "OU Access Structure %s" % structure_code, "code": structure_code}
        )
        agreement_type = self.env["payroll_agreement_type"].create(
            {"name": "OU Access Type %s" % type_code, "code": type_code}
        )
        return self.env["payroll_agreement"].create(
            {
                "employee_id": employee.id,
                "type_id": agreement_type.id,
                "salary_structure_id": salary_structure.id,
                "date": "2025-01-01",
                "operating_unit_id": operating_unit and operating_unit.id,
            }
        )
