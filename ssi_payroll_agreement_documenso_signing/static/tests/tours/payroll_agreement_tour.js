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
                content:
                    "Signature Requests tab shows the Approval Signature Request field",
                trigger: ".o_field_widget[name='approval_signature_request_id']",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                    // The tour stops here -- it does not click Approve, does
                    // not assert a final state, and never calls the external
                    // Documenso service.
                },
            },
        ]
    );
});
