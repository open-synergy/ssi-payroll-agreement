.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0.html
   :alt: License: AGPL-3

==================
📝 **Description**
==================

Payroll Agreement - Operating Unit Integration is an Odoo module that extends the
Payroll Agreement module with Operating Unit support. It allows payroll agreement
documents to be scoped and filtered by a specific operating unit, enabling
multi-company or multi-division environments to manage their payroll agreements
independently.

==========================
💡 **Use Cases / Context**
==========================

- Organizations with multiple operating units requiring separate payroll agreement management
- Multi-division companies needing to restrict payroll agreement visibility per unit
- Businesses using operating unit-based access control for HR documents

===================
🚀 **Installation**
===================

To install this module:

1.  Clone the branch **14.0** of the repository: https://github.com/open-synergy/ssi-payroll-agreement
2.  Add the path to this repository in your Odoo configuration (`addons-path`)
3.  Update the module list (ensure you are in developer mode)
4.  Go to menu *Apps → Apps → Main Apps*
5.  Search for *Payroll Agreement + Operating Unit*
6.  Install the module

=================
🛠️ **How To Use**
=================

1. Install this module along with ``ssi_payroll_agreement`` and ``ssi_operating_unit_mixin``.
2. Activate developer mode in Odoo.
3. Go to the Payroll Agreement menu in Odoo.
4. Create or open a payroll agreement.
5. Select the desired **Operating Unit** on the agreement form.
6. Access rules will automatically filter records based on the user's operating unit.

==================
🐞 **Bug Tracker**
==================

Bugs are tracked on `GitHub Issues <https://github.com/open-synergy/ssi-payroll-agreement/issues>`_.
If you encounter any issues, please check if it has already been reported. If not, help us improve by providing detailed feedback.

==============
🙌 **Credits**
==============

**Contributors:**

- Andhitia Rama <andhitia.r@gmail.com>

===============
**Maintainer:**
===============

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by PT. Simetri Sinergi Indonesia.
