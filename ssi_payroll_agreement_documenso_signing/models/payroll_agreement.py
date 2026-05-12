# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import models


class PayrollAgreement(models.Model):
    _name = "payroll_agreement"
    _inherit = [
        "payroll_agreement",
        "mixin.documenso_signing_approval",
    ]

    _documenso_signing_create_page = True
