frappe.ui.form.on("Customer", {
  onload: function (frm) {
    frm.set_query("link_doctype", "vehicle_links", function (doc, cdt, cdn) {
      return {
        filters: {
          name: "Vehicle Info",
        },
      };
    });
  },
});

frappe.ui.form.on("Dynamic Link", {
  link_name: function (frm, cdt, cdn) {
    var child = locals[cdt][cdn];
    if (child.link_name) {
      frappe.model.with_doctype(child.link_doctype, function () {
        var title_field =
          frappe.get_meta(child.link_doctype).title_field || "name";
        frappe.model.get_value(
          child.link_doctype,
          child.link_name,
          title_field,
          function (r) {
            frappe.model.set_value(cdt, cdn, "link_title", r[title_field]);
          }
        );
      });
    }
  },
});
