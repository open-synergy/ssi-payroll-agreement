# Reset Document Number — Payroll Agreement

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement`\
> **Menu:** Human Resource > Payroll > Agreements\
> **Actor:** user in group `Validator` (`payroll_agreement_validator_group`)\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `sequence.template` (**Standard**) exists for this model.
- **Access:** User is in group `Validator` (`payroll_agreement_validator_group`).

## Flow

1. Open the **Human Resource > Payroll > Agreements** menu.
2. Open the record whose document number will be reset.
3. Click the **Reset Document Number** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Document number returns to **/**.
- The record will receive an automatic number when it transitions to **Ready to
  Process**, according to the **Standard** sequence template configuration.
