# Create Payroll Agreement

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement`\
> **Menu:** Human Resource > Payroll > Agreements\
> **Actor:** user in group `User` (`payroll_agreement_user_group`)\
> **State:** `—` → `draft`\
> **Requires:** `payroll_agreement_type/01-create`, `payroll_agreement_input_type/01-create`\
> **Inline Actions:** `action_populate_salary_rule_ids` (Populate)

## Pre-Condition

- **Data:** An active `payroll_agreement_type` record exists to select as **Type** (see
  `payroll_agreement_type/01-create`).
- **Data:** An active `hr.salary_structure` record exists to select as **Salary
  Structure**.
- **Data:** An active `payroll_agreement_input_type` record exists for each line to add
  on the **Inputs** tab (see `payroll_agreement_input_type/01-create`).
- **Data:** No other **payroll_agreement** for the same **Employee** may already be **In
  Progress** — this is only enforced when the agreement is started, not at creation time
  (see `07-start`).
- **Access:** User is in group `User` (`payroll_agreement_user_group`).

## Flow

1. Open the **Human Resource > Payroll > Agreements** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Employee** _(required)_: select the employee this agreement applies to.
   - **Type** _(required)_: select the payroll agreement type.
   - **Salary Structure** _(required)_: select the salary structure this agreement
     follows.
   - **Date** _(required)_: enter the agreement date.
   - **Reference**: free-text reference. Optional.
4. On the **Rules** tab, click **Populate** to fill **Salary Rules** with the rules of
   the selected **Salary Structure**. There is no manual way to add or remove rules —
   the **Salary Rules** list is read-only. If this step is skipped, payslips generated
   for this agreement's employee fall back to using the salary structure's default rules
   instead of this agreement's rules.
5. On the **Inputs** tab, add lines as needed. Repeat the following steps as many times
   as needed:
   - Click **Add a line**.
   - Fill in each line with:
     - **Input Type** _(required)_: select the payroll agreement input type.
     - **Amount**: Automatically filled from **Input Type**'s default amount. Change if
       needed.
6. On the **Note** tab, fill in **Note**. Optional.
7. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
- Document number shows **/** until the record reaches **Ready to Process**, when it
  receives an automatic number according to the sequence template configuration.
