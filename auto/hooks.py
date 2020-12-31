# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "auto"
app_title = "Auto"
app_publisher = "GreyCube Technologies"
app_description = "Customization for auto repair"
app_icon = "fa fa-car"
app_color = "blue"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/auto/css/auto.css"
# app_include_js = "/assets/auto/js/auto.js"

# include js, css files in header of web template
# web_include_css = "/assets/auto/css/auto.css"
# web_include_js = "/assets/auto/js/auto.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Customer": "public/js/customer.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "auto.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "auto.install.before_install"
# after_install = "auto.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "auto.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
    "Quotation": {
        "validate": "auto.auto.doctype.vehicle_info.vehicle_info.update_vehicle_info"
    },
    "Sales Order": {"validate": "auto.auto.doctype.vehicle_info.vehicle_info.update_vehicle_info"},
    "Sales Invoice": {"validate": "auto.auto.doctype.vehicle_info.vehicle_info.update_vehicle_info"},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"auto.tasks.all"
# 	],
# 	"daily": [
# 		"auto.tasks.daily"
# 	],
# 	"hourly": [
# 		"auto.tasks.hourly"
# 	],
# 	"weekly": [
# 		"auto.tasks.weekly"
# 	]
# 	"monthly": [
# 		"auto.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "auto.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "auto.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "auto.task.get_dashboard_data"
# }
