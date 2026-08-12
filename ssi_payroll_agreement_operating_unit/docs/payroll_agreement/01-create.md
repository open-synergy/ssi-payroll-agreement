# Create Payroll Agreement

> **Module:** ssi_payroll_agreement_operating_unit
>
> **Extends:** ssi_payroll_agreement — model `payroll_agreement`, aksi `01-create`

## Additional Pre-Condition

- **Module:** `ssi_payroll_agreement_operating_unit` is installed.
- **Access:** User is in group **Multiple Operating Unit**
  (`operating_unit.group_multi_operating_unit`) — without this, the Operating Unit field
  described below is never rendered on the create form.
- **Data:** At least one `operating.unit` is assigned to the user (their
  `assigned_operating_unit_ids`), so the field has a non-empty allowed set.

## Additional Fields

When this module is installed, the create form gains one additional field, visible only
to users in the **Multiple Operating Unit** group
(`operating_unit.group_multi_operating_unit`):

- **Operating Unit**: the operating unit that owns this payroll agreement document. Not
  required. Automatically filled from the current user's default operating unit (falls
  back to an operating unit assigned to the user in the active company, if any). Change
  if needed.

## Modified — Record Visibility

- The **Payroll Agreements** list is filtered by operating unit (record rule). A user
  only sees payroll agreement documents whose Operating Unit is one of the operating
  units assigned to them. This is not a Flow step.
- Silent failure: a payroll agreement document whose Operating Unit is left empty is not
  visible to any member of the Operating Unit group, including the user who created it.
