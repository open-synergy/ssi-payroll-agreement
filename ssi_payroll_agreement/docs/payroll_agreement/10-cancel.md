# Cancel Payroll Agreement

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement`\
> **Menu:** Human Resource > Payroll > Agreements\
> **Actor:** user in group `Validator` (`payroll_agreement_validator_group`)\
> **State:** `draft` | `confirm` | `ready` | `open` | `done` → `cancel`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**, **Waiting for Approval**, **Ready to Process**, **In
  Progress**, or **Done**.
- **Data:** An active `base.cancel_reason` record exists that applies to this model
  (either global or linked to it).
- **Config:** An active `policy.template` (**Standard**) grants `cancel_ok` for that
  state to the actor's group.
- **Access:** User is in group `Validator` (`payroll_agreement_validator_group`).

## Flow

1. Open the **Human Resource > Payroll > Agreements** menu.
2. Open the record to cancel.
3. Click the **Cancel** button.
4. In the wizard that appears, select the **Cancellation Reason**.
5. Click **Confirm**.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Cancelled**.
