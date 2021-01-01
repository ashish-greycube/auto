from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
    config = [
        {
            "label": _("Documents"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Vehicle Info",
                    "label": "Vehicle Info",
                    "description": "Vehicle Info"
                },
                {
                    "type": "doctype",
                    "name": "Quotation",
                    "label": "Quotation",
                    "description": "Quotation"
                },
                {
                    "type": "doctype",
                    "name": "Sales Order",
                    "label": "Sales Order",
                    "description": "Sales Order"
                },
                {
                    "type": "doctype",
                    "name": "Sales Invoice",
                    "label": "Sales Invoice",
                    "description": "Sales Invoice"
                },
            ]
        }
    ]
    return config
