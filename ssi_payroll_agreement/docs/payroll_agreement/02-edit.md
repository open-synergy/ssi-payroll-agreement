# Edit Payroll Agreement

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement`\
> **Menu:** Human Resource > Payroll > Agreements\
> **Actor:** user in group `User` (`payroll_agreement_user_group`)\
> **Requires:** `01-create`\
> **Inline Actions:** `action_populate_salary_rule_ids` (Populate)

## Pre-Condition

- **Record:** Status is **Draft**.
- **Access:** User is in group `User` (`payroll_agreement_user_group`).

## Flow

1. Open the **Human Resource > Payroll > Agreements** menu.
2. Find and open the record to edit.
3. Change the required fields (**Employee**, **Type**, **Salary Structure**, **Date**)
   or optional fields (**Reference**, **Note**) as needed.
4. On the **Rules** tab, click **Populate** to refresh **Salary Rules** from the
   **Salary Structure** — for example after changing the **Salary Structure**. There is
   no manual way to add or remove rules — the **Salary Rules** list is read-only. If
   this step is skipped after changing the **Salary Structure**, **Salary Rules** keeps
   showing the rules of the previous structure.
5. On the **Inputs** tab, add, edit, or remove lines as needed.
6. Click **Save**.

## Post-Condition

- The record is updated with the new values.
