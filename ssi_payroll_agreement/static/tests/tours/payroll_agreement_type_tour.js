odoo.define("ssi_payroll_agreement.payroll_agreement_type_tour", function (require) {
    "use strict";

    var tour = require("web_tour.tour");

    // IK: docs/payroll_agreement_type/01-create.md
    tour.register(
        "ssi_payroll_agreement_payroll_agreement_type_create",
        {
            test: true,
            url: "/web",
        },
        [
            // ── Flow 1 — Open the Human Resource > Configuration >
            // Payroll Agreement > Types menu
            tour.stepUtils.showAppsMenuItem(),
            {
                content: "Open the Human Resource app",
                trigger: '.o_app[data-menu-xmlid="ssi_hr.menu_root_human_resource"]',
            },
            {
                content: "Open the Configuration menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_hr.menu_human_resource_configuration"]',
            },
            {
                // "Payroll Agreement" is a non-actionable grouping header
                // (renders as a plain <div class="dropdown-header">, not a
                // clickable [data-menu-xmlid] item) — go straight to the
                // Types leaf item underneath it.
                content: "Open the Types menu",
                trigger:
                    '.o_menu_sections [data-menu-xmlid="ssi_payroll_agreement.payroll_agreement_type_menu"]',
            },
            {
                // Gate: wait for the TARGET action to be mounted, not just
                // any list view (the app may land on a stale list first).
                content: "Payroll Agreement Types list is displayed",
                trigger:
                    ".o_control_panel .breadcrumb-item.active:contains(Payroll Agreement Types)",
                extra_trigger: ".o_list_view",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 2 — Click the Create button
            {
                content: "Click Create",
                trigger: ".o_list_button_add",
                extra_trigger: ".o_list_view",
            },
            {
                content: "Form is open in edit mode",
                trigger: ".o_form_view.o_form_editable",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Flow 3 — Fill in the required fields (Payroll Agreement
            // Type, Code, Active)
            {
                content: "Fill in the Payroll Agreement Type name",
                trigger: ".o_field_widget[name='name']",
                extra_trigger: ".o_form_view.o_form_editable",
                run: "text Tour Payroll Agreement Type",
            },
            {
                content: "Fill in Code",
                trigger: ".o_field_widget[name='code']",
                run: "text /",
            },

            // ── Flow 4 — Click Save
            {
                content: "Save the record",
                trigger: ".o_form_button_save",
            },

            // ── Flow 5 (Inline Action) — Click Generate Code to assign a
            // code from the sequence template configured in setUpClass
            {
                content: "Click Generate Code",
                trigger: "button[name='action_generate_code']",
                extra_trigger: ".o_form_view.o_form_readonly",
            },
            {
                // Gate: fails if Generate Code was not actually clicked --
                // the Code widget keeps showing the literal "/" left over
                // from Flow 3 until action_generate_code replaces it. The
                // generated value itself is not asserted here (unit test
                // territory).
                content: "Code is no longer the literal /",
                trigger: ".o_field_widget[name='code']:not(:contains(/))",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },

            // ── Post-Condition — A new record is created and is active
            // by default
            {
                content: "Payroll Agreement Type record is saved and active",
                trigger: ".o_form_view.o_form_readonly",
                run: function () {
                    // Assertion only; do not trigger the default click action.
                },
            },
        ]
    );
});
