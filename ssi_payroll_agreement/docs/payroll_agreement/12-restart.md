# Restart Payroll Agreement

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement`\
> **Menu:** Human Resource > Payroll > Agreements\
> **Actor:** user in group `Validator` (`payroll_agreement_validator_group`)\
> **State:** `cancel` | `reject` → `draft`\
> **Requires:** `10-cancel`, `06-reject`

## Pre-Condition

- **Record:** Status is **Cancelled** or **Rejected**.
- **Config:** An active `policy.template` (**Standard**) grants `restart_ok` for that
  state to the actor's group.
- **Access:** User is in group `Validator` (`payroll_agreement_validator_group`).

## Flow

1. Open the **Human Resource > Payroll > Agreements** menu.
2. Open the record to restart.
3. Click the **Restart** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status returns to **Draft**.
- All approval records are removed and the approval template is cleared. A later Confirm
  starts the approval process from the beginning.
