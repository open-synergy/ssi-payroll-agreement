# Create Payroll Agreement Type

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement_type`\
> **Menu:** Human Resource > Configuration > Payroll Agreement > Types\
> **Actor:** user in group `Payroll Agreement Type` (`payroll_agreement_type_group`)\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Config:** An active `sequence.template` exists for this model, so **Generate Code**
  (step 5) can assign a code. Without it, clicking **Generate Code** raises an error.
- **Access:** User is in group `Payroll Agreement Type`
  (`payroll_agreement_type_group`).

## Flow

1. Open the **Human Resource > Configuration > Payroll Agreement > Types** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Payroll Agreement Type** _(required)_: enter the label for this agreement type.
   - **Code** _(required)_: enter a unique code manually, or fill with **/** and use
     **Generate Code** (step 5) after saving to assign one automatically.
   - **Active**: enabled by default. Leave enabled so this type can be selected on new
     **Payroll Agreement** records.
4. Click **Save**.
5. If **Code** was left as **/**, click **Generate Code** in the header to assign a code
   from the configured sequence template. There is no other way to turn **/** into a
   real code — skipping this step leaves **Code** showing **/** on the list and form
   instead of a generated identifier.

## Post-Condition

- A new record is created and is active by default.
- The record can now be selected as **Payroll Agreement Type** on **Payroll Agreement**
  records.
