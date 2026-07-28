# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import models


class PayrollAgreement(models.Model):
    """Adds Documenso electronic signature support to payroll agreements.

    Extends ``payroll_agreement`` with ``mixin.documenso_signing_approval``
    so the agreement approval flow can be driven by a Documenso signature
    request instead of manual approvers. Setting
    ``_documenso_signing_create_page`` to ``True`` injects the Documenso
    signing tab into the payroll agreement form view.
    """

    _name = "payroll_agreement"
    _inherit = [
        "payroll_agreement",
        "mixin.documenso_signing_approval",
    ]

    _documenso_signing_create_page = True
