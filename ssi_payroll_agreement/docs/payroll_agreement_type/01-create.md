# Create Payroll Agreement Type

> **Module:** ssi_payroll_agreement\
> **Model:** `payroll_agreement_type`\
> **Menu:** Human Resource > Configuration > Payroll Agreement > Types\
> **Actor:** user in group `Payroll Agreement Type` (`payroll_agreement_type_group`)

## Pre-Condition

- **Access:** User is in group `Payroll Agreement Type`
  (`payroll_agreement_type_group`).

## Flow

1. Open the **Human Resource > Configuration > Payroll Agreement > Types** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Payroll Agreement Type** _(required)_: enter the label for this agreement type.
   - **Code** _(required)_: fill with **/** to let the system auto-assign a code, or
     enter a unique code manually.
   - **Active**: enabled by default. Leave enabled so this type can be selected on new
     **Payroll Agreement** records.
4. Click **Save**.

## Post-Condition

- A new record is created and is active by default.
- The record can now be selected as **Payroll Agreement Type** on **Payroll Agreement**
  records.
