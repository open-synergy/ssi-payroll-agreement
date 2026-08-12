// Copyright 2026 OpenSynergy Indonesia
// Copyright 2026 PT. Simetri Sinergi Indonesia
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define("ssi_payroll_agreement_documenso_signing.payroll_agreement_tour", function (
    require
) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/payroll_agreement/05-approve.md (E2a delta -- Modified Flow)
    // Navigation (open menu -> open record) is retraced from the base IK
    // ssi_payroll_agreement/docs/payroll_agreement/05-approve.md Flow
    // steps 1-2 -- see skill odoo-development-ui-test,
    // scope-and-boundaries.md §3 ("E2a -- telusur-ulang aksi itu dari
    // base sampai titik ubah"). The delta assertion, anchored at base
    // Flow step 2 (open the record to approve), verifies the Signature
    // Requests tab injected because `_documenso_signing_create_page =
    // True`, then stops -- base Flow steps 3-4 (Approve / OK) and the
    // resulting Ready to Process status are NOT exercised here, since
    // whether the Approve button is even visible depends on whether the
    // active Approval Template has a Documenso Signing Template
    // configured, and this tour's fixture leaves that unconfigured. The
    // final signed/rejected outcome is driven by the external Documenso
    // connector and out of scope for a tour (Keputusan Desain, issue
    // open-synergy/ssi-payroll-agreement#25).
    tour.register(
        "ssi_payroll_agreement_documenso_signing_payroll_agreement_approve",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Base Flow 1 — Open the Human Resource > Payroll >
            // Agreements menu.
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
                // Gate: wait for the TARGET action to be mounted, not
                // just any list view (the app may land on a stale list
                // first).
                content: "Payroll Agreements list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Payroll Agreements)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Base Flow 2 — Open the record to approve.
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(Tour PA Documenso Employee Approve) .o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Record form is displayed",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Delta assertion (anchor: base Flow step 2) — the
            // Signature Requests tab is always present once this module
            // is installed, regardless of whether Documenso signing is
            // actually used for the current approval.
            {
                content: "Open the Signature Requests tab",
                trigger: ".o_notebook .nav-link:contains(Signature Requests)",
            },
            {
                // Anchored on the group label rather than the (currently
                // empty) `approval_signature_request_id` many2one widget
                // itself -- a many2one rendered with no value has no text
                // node inside its link, so it collapses to a zero-size
                // box and jQuery's `:visible` (offsetWidth/offsetHeight)
                // never matches it, hanging the tour until timeout. The
                // group label always has text, so it is a stable proxy
                // for "the Approval Signing Request group is rendered".
                content:
                    "Signature Requests tab shows the Approval Signing " +
                    "Request group",
                trigger: ".o_horizontal_separator:contains(Approval Signing Request)",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                    // The tour stops here -- it does not click Approve, does
                    // not assert a final state, and never calls the external
                    // Documenso service.
                },
            },
        ]
    );

    // IK: docs/payroll_agreement/06-create-signing-request.md (E3 -- new
    // action). The tour runs the wizard to completion (Create), which
    // navigates to the newly created documenso.signature.request's own
    // form -- it does NOT go further and click that request's own "Send
    // to Documenso" button, since that would call the external Documenso
    // service over the network. After the wizard, the tour returns to
    // the Payroll Agreement record and re-opens the Signature Requests
    // tab to observe the new row -- the row's field values are not
    // asserted (Keputusan Desain, issue open-synergy/ssi-payroll-agreement#36).
    tour.register(
        "ssi_payroll_agreement_documenso_signing_payroll_agreement_create_signing_request",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Human Resource > Payroll > Agreements
            // menu.
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
                // Gate: wait for the TARGET action to be mounted, not
                // just any list view (the app may land on a stale list
                // first).
                content: "Payroll Agreements list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Payroll Agreements)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 2 — Open the record.
            {
                content: "Open the record",
                trigger:
                    ".o_data_row:contains(Tour PA Documenso Employee Signing Request) " +
                    ".o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Record form is displayed",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 3 — Open the Signature Requests tab.
            {
                content: "Open the Signature Requests tab",
                trigger: ".o_notebook .nav-link:contains(Signature Requests)",
            },

            // ── Flow 4 — Click the New Signing Request button.
            {
                content: "Click the New Signing Request button",
                trigger: ".o_form_view button[name='action_create_signing_request']",
            },

            // ── Flow 5 — In the wizard that appears, fill in Signing
            // Template (Backend is filled automatically).
            {
                // 14.0: do not prefix the trigger with `.modal` -- the
                // tour manager already searches inside the modal, and
                // `.modal .o_form_view` would look for a nested modal
                // that does not exist (patterns.md §H).
                content: "The Create Signing Request wizard is open",
                trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Select the Signing Template",
                trigger: ".o_field_many2one[name='signing_template_id'] input",
                run: "text Tour PA Documenso Signing Template",
            },
            {
                content: "Pick the Signing Template from the dropdown",
                trigger:
                    ".ui-autocomplete .ui-menu-item a:contains(Tour PA Documenso " +
                    "Signing Template)",
                in_modal: false,
            },

            // ── Flow 6 — Click Create. The browser navigates to the
            // newly created signature request's own form.
            {
                content: "Click Create",
                trigger: ".modal-footer button[name='action_confirm']",
            },
            {
                content: "The new Signature Request's own form is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Signature Request)",
                extra_trigger: ".o_form_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                    // The tour does NOT click "Send to Documenso" here --
                    // that would call the external Documenso service.
                },
            },

            // ── Flow 7 — Return to the Agreements menu, reopen the same
            // record, and open the Signature Requests tab again.
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Human Resource app again",
                trigger: '.o_app[data-menu-xmlid="ssi_hr.menu_root_human_resource"]',
            },
            {
                content: "Open the Payroll menu again",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_hr_payroll.hr_payroll_root_menu"]',
            },
            {
                content: "Open the Agreements menu again",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_payroll_agreement.menu_payroll_agreement"]',
            },
            {
                content: "Payroll Agreements list is displayed again",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Payroll Agreements)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
            {
                content: "Reopen the record",
                trigger:
                    ".o_data_row:contains(Tour PA Documenso Employee Signing Request) " +
                    ".o_data_cell:first",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Reopen the Signature Requests tab",
                trigger: ".o_notebook .nav-link:contains(Signature Requests)",
            },

            // ── Post-Condition — a new row appears on the Signature
            // Requests page for the request just created. Its field
            // values are not asserted (Keputusan Desain).
            {
                content: "A new row appears on the Signature Requests page",
                trigger: ".o_field_widget[name='signature_request_ids'] .o_data_row",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});
