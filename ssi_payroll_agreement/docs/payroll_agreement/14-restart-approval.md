# Restart Approval Process — Payroll Agreement

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement`\
> **Menu:** Human Resource > Payroll > Agreements\
> **Actor:** user in group `Validator` (`payroll_agreement_validator_group`)\
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**, and the record currently has no
  `approval.template` linked (e.g. the template that was assigned when the record was
  confirmed was later deactivated or removed).
- **Config:** An active `policy.template` (**Standard**) for this model grants
  `restart_approval_ok` for state `confirm` to the actor's group, on the condition that
  the record has no `approval.template` linked.
- **Config:** An active `approval.template` (**Standard**) for this model exists, so the
  reload can find a match and build the approver list again.
- **Access:** User is in group `Validator` (`payroll_agreement_validator_group`).

## Flow

1. Open the **Human Resource > Payroll > Agreements** menu.
2. Open the record to restart the approval process for.
3. Click the **Restart Approval Process** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The approver list on the **Approvals** tab is rebuilt: it was empty before (no
  `approval.template` was linked), and now shows the approver level(s) defined by the
  **Standard** approval template.
- Status remains **Waiting for Approval** — this action does not change the record's
  state.

## Related Actions

- **Reload Template Policy** (`action_reload_policy_template`, on the **Policies** tab,
  restricted to `base.group_system`) is a technical/administrative action with no
  meaningful end-user flow — it re-evaluates and rewrites `policy_template_id` from the
  model's `policy.template` configuration. It is intentionally **not** documented as its
  own Instruksi Kerja and has no tour.
