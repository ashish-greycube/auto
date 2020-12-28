// Copyright (c) 2020, Greycube.in and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle Info", {
  refresh: function (frm) {
    frm.add_custom_button(__("Refresh VIN Info"), function () {
      return frappe.call({
        doc: frm.doc,
        method: "refresh_vin_info",
        callback: function () {
          frm.refresh();
        },
      });
    });
  },
});
