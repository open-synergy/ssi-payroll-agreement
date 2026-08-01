# Start Payroll Agreement

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement`\
> **Menu:** Human Resource > Payroll > Agreements\
> **Actor:** user in group `User` (`payroll_agreement_user_group`)\
> **State:** `ready` → `open`\
> **Requires:** `05-approve`

## Pre-Condition

- **Record:** Status is **Ready to Process**.
- **Record:** No other **payroll_agreement** for the same **Employee** is already **In
  Progress** — enforced by `_constrains_open`.
- **Config:** An active `policy.template` (**Standard**) grants `open_ok` for state
  `ready` to the actor's group.
- **Access:** User is in group `User` (`payroll_agreement_user_group`).

## Flow

1. Open the **Human Resource > Payroll > Agreements** menu.
2. Open the record to start.
3. Click the **Start** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **In Progress**.
- If another **payroll_agreement** for the same **Employee** is already **In Progress**,
  the transition is blocked with a validation error.
