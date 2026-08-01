# Reject Payroll Agreement

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement`\
> **Menu:** Human Resource > Payroll > Agreements\
> **Actor:** user registered as approver on the pending approval level, via the **Standard**
> approval template, group `Validator` (`payroll_agreement_validator_group`)\
> **State:** `confirm` → `reject`\
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `policy.template` (**Standard**) grants `reject_ok` to the
  actor.
- **Access:** User is registered as an approver on the approval level that is currently
  pending.

## Flow

1. Open the **Human Resource > Payroll > Agreements** menu.
2. Open the record to reject.
3. Click the **Reject** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Rejected**.
