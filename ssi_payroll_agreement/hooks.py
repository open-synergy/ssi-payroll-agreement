# Copyright 2025 OpenSynergy Indonesia
# Copyright 2025 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


def post_init_hook(cr, registry):
    """Seed ``manual_salary_structure_id`` from the existing structure.

    For every ``hr_employee`` row, copies its pre-existing
    ``salary_structure_id`` into the new
    ``manual_salary_structure_id`` column via a direct SQL
    ``UPDATE``, so installing this module does not silently change
    which salary structure an employee's payslips already used.

    :param cr: database cursor
    :param registry: model registry (unused)
    """
    cr.execute(
        """
    UPDATE
        hr_employee dest
    SET
        manual_salary_structure_id = src.salary_structure_id
    FROM hr_employee src
    WHERE
        dest.id = src.id;
    """
    )
