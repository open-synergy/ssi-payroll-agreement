# Finish Payroll Agreement

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement`\
> **Menu:** Human Resource > Payroll > Agreements\
> **Actor:** user in group `User` (`payroll_agreement_user_group`)\
> **State:** `open` → `done`\
> **Requires:** `07-start`

## Pre-Condition

- **Record:** Status is **In Progress**.
- **Config:** An active `policy.template` (**Standard**) grants `done_ok` for state
  `open` to the actor's group.
- **Access:** User is in group `User` (`payroll_agreement_user_group`).

## Flow

1. Open the **Human Resource > Payroll > Agreements** menu.
2. Open the record to finish.
3. Click the **Done** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Done**.
