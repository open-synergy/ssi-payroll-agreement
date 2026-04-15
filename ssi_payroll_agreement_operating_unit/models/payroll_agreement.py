# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PayrollAgreement(models.Model):  # pylint: disable=too-few-public-methods
    """
    Extends payroll_agreement with operating unit support.
    Adds mixin.single_operating_unit so payroll agreement documents
    can be scoped to a specific operating unit.
    """

    _name = "payroll_agreement"
    _inherit = [
        "payroll_agreement",
        "mixin.single_operating_unit",
    ]
