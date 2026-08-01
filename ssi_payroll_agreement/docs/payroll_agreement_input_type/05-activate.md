# Activate Payroll Agreement Input Type

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement_input_type`\
> **Menu:** Human Resource > Configuration > Payroll Agreement > Input Types\
> **Actor:** user in group `Payroll Agreement Input Type` (`payroll_agreement_input_type_configurator_group`)\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived.
- **Access:** User is in group `Payroll Agreement Input Type`
  (`payroll_agreement_input_type_configurator_group`).

## Flow

1. Open the **Human Resource > Configuration > Payroll Agreement > Input Types** menu.
2. Enable the **Archived** filter in the search bar.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.
5. Click **OK** to confirm.

## Post-Condition

- The records are restored and appear again in the default list view.
- The records can be selected again on new **Payroll Agreement** input lines.
