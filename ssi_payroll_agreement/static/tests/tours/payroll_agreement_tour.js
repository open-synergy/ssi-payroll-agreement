// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("ssi_payroll_agreement.payroll_agreement_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // Shared navigation block reused by every tour below -- corresponds to
    // Flow 1 of every payroll_agreement IK: "Open the Human Resource >
    // Payroll > Agreements menu." "Payroll" (ssi_hr_payroll.hr_payroll_root_menu)
    // is a second-level app menu (parent is the Human Resource app itself),
    // so it is always clickable in the top navbar, same as any other
    // second-level menu.
    function openAgreementList() {
        return [
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Human Resource app",
                trigger: '.o_app[data-menu-xmlid="ssi_hr.menu_root_human_resource"]',
            },
            {
                content: "Open the Payroll menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_hr_payroll.hr_payroll_root_menu"]',
            },
            {
                content: "Open the Agreements menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_payroll_agreement.menu_payroll_agreement"]',
            },
            {
                // Gate: wait for the TARGET action to be mounted, not just
                // any list view (the app may land on a stale list first).
                content: "Payroll Agreements list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Payroll Agreements)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ];
    }

    // Opens the row identified by its Employee column text -- the tree view
    // does not show "# Document" usefully (every Draft record shows "/"),
    // so each scenario below is keyed by its own dedicated employee.
    function openAgreementByEmployee(employeeName) {
        return [
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(" + employeeName + ") .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only.
                },
            },
        ];
    }

    // IK: docs/payroll_agreement/01-create.md
    tour.register(
        "ssi_payroll_agreement_payroll_agreement_create",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Agreements menu.
            openAgreementList(),
            [
                // Flow 2 -- Click the New button.
                {
                    content: "Click New",
                    trigger: ".o_list_button_add",
                    extra_trigger: ".o_list_view",
                },
                {
                    content: "Form is open in edit mode",
                    trigger: ".o_form_view.o_form_editable",
                    run: function () {
                        // Assertion only.
                    },
                },

                // Flow 3 -- Fill in the required fields: Employee, Type,
                // Salary Structure, Date.
                {
                    content: "Select the Employee",
                    trigger: ".o_field_many2one[name='employee_id'] input",
                    extra_trigger: ".o_form_view.o_form_editable",
                    run: "text Tour PA Employee Create",
                },
                {
                    content: "Pick the Employee from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(Tour PA Employee Create)",
                    in_modal: false,
                },
                {
                    content: "Select the Type",
                    trigger: ".o_field_many2one[name='type_id'] input",
                    run: "text Tour PA Agreement Type",
                },
                {
                    content: "Pick the Type from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(Tour PA Agreement Type)",
                    in_modal: false,
                },
                {
                    content: "Select the Salary Structure",
                    trigger: ".o_field_many2one[name='salary_structure_id'] input",
                    run: "text Tour PA Salary Structure",
                },
                {
                    content: "Pick the Salary Structure from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(Tour PA Salary Structure)",
                    in_modal: false,
                },
                {
                    content: "Fill in the Date",
                    trigger: ".o_field_widget[name='date'] input",
                    run: "text 01/15/2026",
                },

                // Flow 4 -- On the Rules tab (open by default, first page
                // of the notebook), click Populate to fill Salary Rules
                // from the Salary Structure.
                {
                    content: "Click Populate",
                    trigger: "button[name='action_populate_salary_rule_ids']",
                },

                // Flow 5 -- On the Inputs tab, add one line: Input Type,
                // Amount is auto-filled by onchange.
                {
                    content: "Open the Inputs tab",
                    trigger: ".o_notebook .nav-link:contains(Inputs)",
                },
                {
                    content: "Add an input line",
                    trigger:
                        ".o_field_x2many[name='input_line_ids'] .o_field_x2many_list_row_add a",
                },
                {
                    content: "Select the Input Type",
                    trigger:
                        ".o_selected_row .o_field_widget[name='input_type_id'] input",
                    run: "text Tour PA Input Type",
                },
                {
                    content: "Pick the Input Type from the dropdown",
                    trigger:
                        ".ui-autocomplete .ui-menu-item a:contains(Tour PA Input Type)",
                    in_modal: false,
                },
                {
                    // Commit the still-editing input line by switching to
                    // another tab -- pressing Tab from the last cell would
                    // open a new empty row and leave the form dirty (see
                    // patterns.md skill odoo-development-ui-test §C
                    // Jebakan 2).
                    content: "Switch back to the Rules tab to commit the line",
                    trigger: ".o_notebook .nav-link:contains(Rules)",
                },

                // Flow 6 (Note tab) is optional and skipped.

                // Flow 7 -- Click Save.
                {
                    content: "Save the record",
                    trigger: ".o_form_button_save",
                },
                {
                    content: "Record is saved",
                    trigger: ".o_form_view.o_form_readonly",
                    run: function () {
                        // Assertion only.
                    },
                },

                // Post-Condition -- back on the Agreements list, the new
                // record is visible.
                {
                    content: "Click the Payroll Agreements breadcrumb",
                    trigger:
                        ".breadcrumb-item.o_back_button a:contains(Payroll Agreements)",
                },
                {
                    content: "New record is visible in the list",
                    trigger:
                        ".o_list_view .o_data_row:contains(Tour PA Employee Create)",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/payroll_agreement/04-confirm.md
    tour.register(
        "ssi_payroll_agreement_payroll_agreement_confirm",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Agreements menu.
            openAgreementList(),
            // Flow 2 -- Open the record to confirm.
            openAgreementByEmployee("Tour PA Employee Confirm"),
            [
                // Flow 3 -- Click the Confirm button.
                {
                    content: "Click the Confirm button",
                    trigger: ".o_statusbar_buttons button[name='action_confirm']",
                    extra_trigger: ".o_form_view",
                },

                // Flow 4 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- status changes to Waiting for Approval.
                {
                    content: "Status is Waiting for Approval",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='confirm'].btn-primary",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/payroll_agreement/05-approve.md
    tour.register(
        "ssi_payroll_agreement_payroll_agreement_approve",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Agreements menu.
            openAgreementList(),
            // Flow 2 -- Open the record to approve.
            openAgreementByEmployee("Tour PA Employee Approve"),
            [
                // Flow 3 -- Click the Approve button.
                {
                    content: "Click the Approve button",
                    trigger:
                        ".o_statusbar_buttons button[name='action_approve_approval']",
                    extra_trigger: ".o_form_view",
                },

                // Flow 4 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- single approval level, so the
                // confirm -> ready transition runs automatically right
                // after approval (_after_approved_method = action_ready).
                {
                    content: "Status is Ready to Process",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='ready'].btn-primary",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/payroll_agreement/06-reject.md
    tour.register(
        "ssi_payroll_agreement_payroll_agreement_reject",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Agreements menu.
            openAgreementList(),
            // Flow 2 -- Open the record to reject.
            openAgreementByEmployee("Tour PA Employee Reject"),
            [
                // Flow 3 -- Click the Reject button.
                {
                    content: "Click the Reject button",
                    trigger:
                        ".o_statusbar_buttons button[name='action_reject_approval']",
                    extra_trigger: ".o_form_view",
                },

                // Flow 4 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- status changes to Rejected.
                {
                    content: "Status is Rejected",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='reject'].btn-primary",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/payroll_agreement/07-start.md
    tour.register(
        "ssi_payroll_agreement_payroll_agreement_start",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Agreements menu.
            openAgreementList(),
            // Flow 2 -- Open the record to start.
            openAgreementByEmployee("Tour PA Employee Start"),
            [
                // Flow 3 -- Click the Start button.
                {
                    content: "Click the Start button",
                    trigger: ".o_statusbar_buttons button[name='action_open']",
                    extra_trigger: ".o_form_view",
                },

                // Flow 4 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- status changes to In Progress.
                {
                    content: "Status is In Progress",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='open'].btn-primary",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/payroll_agreement/09-finish.md
    tour.register(
        "ssi_payroll_agreement_payroll_agreement_finish",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Agreements menu.
            openAgreementList(),
            // Flow 2 -- Open the record to finish.
            openAgreementByEmployee("Tour PA Employee Finish"),
            [
                // Flow 3 -- Click the Done button.
                {
                    content: "Click the Done button",
                    trigger: ".o_statusbar_buttons button[name='action_done']",
                    extra_trigger: ".o_form_view",
                },

                // Flow 4 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- status changes to Done.
                {
                    content: "Status is Done",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='done'].btn-primary",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/payroll_agreement/10-cancel.md
    tour.register(
        "ssi_payroll_agreement_payroll_agreement_cancel",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Agreements menu.
            openAgreementList(),
            // Flow 2 -- Open the record to cancel.
            openAgreementByEmployee("Tour PA Employee Cancel"),
            [
                // Flow 3 -- Click the Cancel button.
                {
                    content: "Click the Cancel button",
                    trigger: ".o_statusbar_buttons button:contains(Cancel)",
                    extra_trigger: ".o_form_view",
                },
                {
                    // Wizard: do NOT prefix the trigger with ".modal" in
                    // 14.0 -- see patterns.md skill
                    // odoo-development-ui-test §H.
                    content: "Wizard is open",
                    trigger: ".o_form_view",
                    run: function () {
                        // Assertion only.
                    },
                },

                // Flow 4 -- Select the Cancellation Reason (rendered as a
                // radio list, inside the wizard modal).
                {
                    content: "Select the cancellation reason",
                    trigger:
                        ".o_field_widget[name='cancel_reason_id'] label:contains(Tour PA Cancel Reason)",
                },

                // Flow 5 -- Click Confirm.
                {
                    content: "Confirm the wizard",
                    trigger: ".modal-footer button[name='action_confirm']",
                },
                {
                    // The wizard's Confirm button carries a stacked "Are
                    // you sure?" dialog (confirm= attribute).
                    content: "Confirm the stacked dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- status changes to Cancelled.
                {
                    content: "Status is Cancelled",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='cancel'].btn-primary",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );

    // IK: docs/payroll_agreement/12-restart.md
    tour.register(
        "ssi_payroll_agreement_payroll_agreement_restart",
        {
            test: true,
            url: "/web",
        },
        [].concat(
            // Flow 1 -- Open the Agreements menu.
            openAgreementList(),
            // Flow 2 -- Open the record to restart.
            openAgreementByEmployee("Tour PA Employee Restart"),
            [
                // Flow 3 -- Click the Restart button.
                {
                    content: "Click the Restart button",
                    trigger: ".o_statusbar_buttons button[name='action_restart']",
                    extra_trigger: ".o_form_view",
                },

                // Flow 4 -- Click OK on the confirmation dialog.
                {
                    content: "Confirm the dialog",
                    trigger: ".modal-footer button.btn-primary",
                    in_modal: true,
                },

                // Post-Condition -- status returns to Draft.
                {
                    content: "Status is Draft",
                    trigger:
                        ".o_statusbar_status .o_arrow_button[data-value='draft'].btn-primary",
                    run: function () {
                        // Assertion only.
                    },
                },
            ]
        )
    );
});
