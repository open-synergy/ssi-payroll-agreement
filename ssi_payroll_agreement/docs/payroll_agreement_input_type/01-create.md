# Create Payroll Agreement Input Type

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement_input_type`\
> **Menu:** Human Resource > Configuration > Payroll Agreement > Input Types\
> **Actor:** user in group `Payroll Agreement Input Type` (`payroll_agreement_input_type_configurator_group`)\
> **Inline Actions:** `action_generate_code` (Generate Code)

## Pre-Condition

- **Config:** An active `sequence.template` exists for this model, so **Generate Code**
  (step 5) can assign a code. Without it, clicking **Generate Code** raises an error.
- **Access:** User is in group `Payroll Agreement Input Type`
  (`payroll_agreement_input_type_configurator_group`).

## Flow

1. Open the **Human Resource > Configuration > Payroll Agreement > Input Types** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name** _(required)_: enter the label for this input type.
   - **Code** _(required)_: enter a unique code manually, or fill with **/** and use
     **Generate Code** (step 5) after saving to assign one automatically.
   - **Default Amount**: the amount used to automatically fill the **Amount** field on a
     payroll agreement input line that references this input type. Optional; defaults to
     **0.0**.
   - **Active**: enabled by default. Leave enabled so this input type can be selected on
     new **Payroll Agreement** input lines.
4. Click **Save**.
5. If **Code** was left as **/**, click **Generate Code** in the header to assign a code
   from the configured sequence template. There is no other way to turn **/** into a
   real code — skipping this step leaves **Code** showing **/** on the list and form
   instead of a generated identifier.

## Post-Condition

- A new record is created and is active by default.
- The record can now be selected as **Input Type** on **Payroll Agreement** input lines.
  Selecting it automatically fills the line's **Amount** field from **Default Amount** —
  the user may still change the amount afterward.
