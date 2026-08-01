# Approve Payroll Agreement

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement`\
> **Menu:** Human Resource > Payroll > Agreements\
> **Actor:** user registered as approver on the pending approval level, via the **Standard**
> approval template, group `Validator` (`payroll_agreement_validator_group`)\
> **State:** `confirm` → `ready`\
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `policy.template` (**Standard**) grants `approve_ok` to the
  actor.
- **Access:** User is registered as an approver on the approval level that is currently
  **pending**. The **Standard** approval template uses sequential approval
  (`validate_sequence`), so only the first unapproved level is pending.

## Flow

1. Open the **Human Resource > Payroll > Agreements** menu.
2. Open the record to approve.
3. Click the **Approve** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- If all approval levels are fulfilled, status automatically changes to **Ready to
  Process** — the record does not stop at an intermediate state; the transition is
  triggered internally by `action_ready` right after the last approval, with no separate
  button click required.
- If there are still pending approval levels, status remains **Waiting for Approval**
  and the next level becomes pending.
