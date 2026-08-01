# Create Payroll Agreement Input Type

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement_input_type`\
> **Menu:** Human Resource > Configuration > Payroll Agreement > Input Types\
> **Actor:** user in group `Payroll Agreement Input Type` (`payroll_agreement_input_type_configurator_group`)

## Pre-Condition

- **Access:** User is in group `Payroll Agreement Input Type`
  (`payroll_agreement_input_type_configurator_group`).

## Flow

1. Open the **Human Resource > Configuration > Payroll Agreement > Input Types** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name** _(required)_: enter the label for this input type.
   - **Code** _(required)_: fill with **/** to let the system auto-assign a code, or
     enter a unique code manually.
   - **Default Amount**: the amount used to automatically fill the **Amount** field on a
     payroll agreement input line that references this input type. Optional; defaults to
     **0.0**.
   - **Active**: enabled by default. Leave enabled so this input type can be selected on
     new **Payroll Agreement** input lines.
4. Click **Save**.

## Post-Condition

- A new record is created and is active by default.
- The record can now be selected as **Input Type** on **Payroll Agreement** input lines.
  Selecting it automatically fills the line's **Amount** field from **Default Amount** —
  the user may still change the amount afterward.
