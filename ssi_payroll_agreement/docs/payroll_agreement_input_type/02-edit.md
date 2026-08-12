# Edit Payroll Agreement Input Type

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement_input_type`\
> **Menu:** Human Resource > Configuration > Payroll Agreement > Input Types\
> **Actor:** user in group `Payroll Agreement Input Type` (`payroll_agreement_input_type_configurator_group`)\
> **Requires:** `01-create`\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Access:** User is in group `Payroll Agreement Input Type`
  (`payroll_agreement_input_type_configurator_group`).

## Flow

1. Open the **Human Resource > Configuration > Payroll Agreement > Input Types** menu.
2. Find and open the record to edit.
3. Change the required fields.
4. Click **Save**.
5. If **Code** still shows **/**, click **Generate Code** in the header to assign a code
   from the configured sequence template. There is no other way to turn **/** into a
   real code — skipping this step leaves **Code** showing **/** on the list and form
   instead of a generated identifier.

## Post-Condition

- The record is updated with the new values.
