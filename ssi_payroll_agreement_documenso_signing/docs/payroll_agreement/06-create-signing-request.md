# Create Signing Request for Payroll Agreement

> **Module:** ssi_payroll_agreement_documenso_signing\
> **Model:** `payroll_agreement`\
> **Menu:** Human Resource > Payroll > Agreements\
> **Actor:** user in group `User` (`payroll_agreement_user_group`)\
> **Requires:** `ssi_payroll_agreement/payroll_agreement/01-create`\
> **Extends:** ssi_payroll_agreement — model `payroll_agreement`

## Pre-Condition

- **Record:** A `payroll_agreement` record exists. The **Signature Requests** tab is
  present on the form regardless of status, since
  `_documenso_signing_create_page = True` is set unconditionally by this module.
- **Config:** An active `documenso.signing.template` exists with **Source Model** set to
  `payroll_agreement`.
- **Config:** An active `documenso.backend` exists.
- **Access:** User is in group `User` (`payroll_agreement_user_group`) — the button
  carries no additional group restriction beyond normal record access.

## Flow

1. Open the **Human Resource > Payroll > Agreements** menu.
2. Open the record.
3. Open the **Signature Requests** tab.
4. Click the **New Signing Request** button.
5. In the wizard that appears, fill in:
   - **Signing Template** _(required)_: select the Documenso Signing Template configured
     for **Payroll Agreement**.
   - **Backend**: Automatically filled with the active Documenso Backend. Change if
     needed.
6. Click **Create**. The browser navigates to the newly created signature request's own
   form.
7. Return to the **Human Resource > Payroll > Agreements** menu, open the same record
   again, and open the **Signature Requests** tab.

## Post-Condition

- A new row appears in the list on the **Signature Requests** tab, for the signature
  request just created. The row's field values are not asserted.
- This action does not move `payroll_agreement`'s own status.

## Note — Open Signature Requests button

- The **Open Signature Requests** button on the same **Signature Requests** tab
  (`action_open_signature_requests`) is verdict **N** (nol IK): it only returns an
  `ir.actions.act_window` that opens the list of this record's signature requests — it
  writes no field. No IK or tour is written for it.
