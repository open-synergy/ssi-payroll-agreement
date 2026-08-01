# Deactivate Payroll Agreement Input Type

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement_input_type`\
> **Menu:** Human Resource > Configuration > Payroll Agreement > Input Types\
> **Actor:** user in group `Payroll Agreement Input Type` (`payroll_agreement_input_type_configurator_group`)\
> **Active:** `true` → `false`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** The record is currently active.
- **Access:** User is in group `Payroll Agreement Input Type`
  (`payroll_agreement_input_type_configurator_group`).

## Flow

1. Open the **Human Resource > Configuration > Payroll Agreement > Input Types** menu.
2. Select one or more records to deactivate (check the checkbox).
3. Click **Action** > **Archive**.
4. Click **OK** to confirm.

## Post-Condition

- The records are archived and no longer appear in the default list view.
- Deactivated records cannot be selected on new **Payroll Agreement** input lines.
- **Payroll Agreement** input lines that already use this input type can still be
  viewed.
