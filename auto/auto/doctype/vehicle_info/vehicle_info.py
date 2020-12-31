# -*- coding: utf-8 -*-
# Copyright (c) 2020, Greycube.in and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr
import json
import requests
import json
from frappe.model.document import Document
from frappe.utils import cstr, cint

class VehicleInfo(Document):
    def validate(self):
        if self.is_new():
            self.set_values(self.vin, False)
        self.title = " ".join([cstr(x) for x in [self.make, self.model, self.model_year] if x])

    def set_values(self, vin, overwrite=False):
        vin_info = get_vin_info(vin)
        for df in self.meta.get("fields"):
            if df.options:
                if vin_info.get(df.options):
                    if not self.get(df.fieldname) or cint(overwrite):
                        self.set(df.fieldname, vin_info.get(df.options))

    def refresh_vin_info(self):
        self.set_values(self.vin, True)


def get_vin_info(vin):
    # url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/';
    api_response = {}
    try:
        url = "{}/{}?format=json".format("https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin", vin)
        resp = cstr(requests.get(url).content)
    except Exception as ex:
        frappe.log_error(ex)
        frappe.throw("Error fetching VIN details from api.")

    if not '"Message":"Results returned successfully.' in resp:
        frappe.throw("Error fetching VIN details from api.")

    resp = json.loads(resp)

    if not resp.get("Results"):
        frappe.log_error(api_response)
        frappe.throw("No results fetched from VIN api.")

    out = {attr['Variable']: attr['Value'] for attr in resp.get("Results", [])}
    if out.get("Error Text"):
        frappe.msgprint("VIN details response has some errors. %s" % frappe.bold(out.get("Error Text")))

    return out


def update_vehicle_info(doc, method):
    fields_to_update = ["customer"] + [
            "color_cf",
            "drive_type_cf",
            "engine_displacement_cf",
            "engine_model_cf",
            "licence_plate_cf",
            "make_cf",
            "mileage_cf",
            "model_cf",
            "model_year_cf",
            "transmission_style_cf",
            "trim_cf",
            "tyre_size_cf", ]

    if doc.get("customer_vehicle_cf"):
        args = dict()
        for d in fields_to_update:
            if doc.get(d):
                args.setdefault(d.replace("_cf", ""), doc.get(d))
        if args:
            v_info = frappe.get_doc("Vehicle Info", doc.get("customer_vehicle_cf"))
            v_info.update(args)
            v_info.save()


vpic_sample_response = """
{
  "Suggested VIN": "",
  "Error Code": "6",
  "Possible Values": "",
  "Additional Error Text": None,
  "Error Text": "6 - Incomplete VIN",
  "Destination Market": None,
  "Make": "BMW",
  "Manufacturer Name": "BMW MANUFACTURER CORPORATION / BMW NORTH AMERICA",
  "Model": "X3",
  "Model Year": "2011",
  "Plant City": "MUNICH",
  "Series": "X3",
  "Trim": "xDrive35i",
  "Vehicle Type": "MULTIPURPOSE PASSENGER VEHICLE (MPV)",
  "Plant Country": "GERMANY",
  "Plant Company Name": None,
  "Plant State": None,
  "Trim2": "SAV",
  "Series2": None,
  "Note": None,
  "Base Price ($)": None,
  "Manufacturer Id": "968",
  "Cash For Clunkers": None,
  "Body Class": "Sport Utility Vehicle (SUV)/Multi-Purpose Vehicle (MPV)",
  "Doors": "4",
  "Windows": None,
  "Wheel Base Type": None,
  "Track Width": None,
  "Gross Vehicle Weight Rating": "Class 1D: 5,001 - 6,000 lb (2,268 - 2,722 kg)",
  "Bed Length (inches)": None,
  "Curb Weight (pounds)": None,
  "Wheel Base (inches)": None,
  "Wheel Base (inches) up to": None,
  "Gross Combination Weight Rating": None,
  "Gross Combination Weight Rating up to": None,
  "Gross Vehicle Weight Rating up to": None,
  "Bed Type": None,
  "Cab Type": None,
  "Trailer Type Connection": "Not Applicable",
  "Trailer Body Type": "Not Applicable",
  "Trailer Length (feet)": None,
  "Other Trailer Info": None,
  "Number of Wheels": None,
  "Wheel Size Front (inches)": None,
  "Wheel Size Rear (inches)": None,
  "Entertainment System": None,
  "Steering Location": None,
  "Number of Seats": None,
  "Number of Seat Rows": None,
  "Transmission Style": None,
  "Transmission Speeds": None,
  "Drive Type": None,
  "Axles": None,
  "Axle Configuration": None,
  "Brake System Type": None,
  "Brake System Description": None,
  "Battery Info": None,
  "Battery Type": None,
  "Number of Battery Cells per Module": None,
  "Battery Current (Amps)": None,
  "Battery Voltage (Volts)": None,
  "Battery Energy (KWh)": None,
  "EV Drive Unit": None,
  "Battery Current (Amps) up to": None,
  "Battery Voltage (Volts) up to": None,
  "Battery Energy (KWh) up to": None,
  "Number of Battery Modules per Pack": None,
  "Number of Battery Packs per Vehicle": None,
  "Charger Level": None,
  "Charger Power (KW)": None,
  "Engine Number of Cylinders": "6",
  "Displacement (CC)": "2979.1682352",
  "Displacement (CI)": "181.8",
  "Displacement (L)": "3.0",
  "Engine Stroke Cycles": None,
  "Engine Model": None,
  "Engine Power (KW)": "223.7100",
  "Fuel Type - Primary": "Gasoline",
  "Valve Train Design": None,
  "Engine Configuration": None,
  "Fuel Type - Secondary": None,
  "Fuel Delivery / Fuel Injection Type": None,
  "Engine Brake (hp)": "300",
  "Cooling Type": None,
  "Engine Brake (hp) up to": None,
  "Electrification Level": None,
  "Other Engine Info": None,
  "Turbo": None,
  "Top Speed (MPH)": None,
  "Engine Manufacturer": None,
  "Pretensioner": "Yes",
  "Seat Belts Type": "Manual",
  "Other Restraint System Info": "Head Inflatable Restraint for Driver, Front Passenger, Rear Outboard Driver-side and Rear Outboard Passenger-side.  Knee Inflatable Restraint for Driver.  Pretensioners for Driver and Front Passenger.",
  "Curtain Air Bag Locations": None,
  "Seat Cushion Air Bag Locations": None,
  "Front Air Bag Locations": "1st Row (Driver & Passenger)",
  "Knee Air Bag Locations": None,
  "Side Air Bag Locations": "1st Row (Driver & Passenger)",
  "Driver Assist": None,
  "Adaptive Cruise Control (ACC)": None,
  "Adaptive Headlights": None,
  "Anti-lock Braking System (ABS)": None,
  "Crash Imminent Braking (CIB)": None,
  "Blind Spot Detection (BSD)": None,
  "Electronic Stability Control (ESC)": None,
  "Traction Control": None,
  "Forward Collision Warning (FCW)": None,
  "Lane Departure Warning (LDW)": None,
  "Lane Keeping Support (LKS)": None,
  "Rear Visibility System (RVS)": None,
  "Parking Assist": None,
  "TPMS": "Direct",
  "Active Safety System Note": None,
  "Dynamic Brake Support (DBS)": None,
  "Pedestrian Automatic Emergency Braking (PAEB)": None,
  "Auto-Reverse System for Windows and Sunroofs": None,
  "Automatic Pedestrian Alerting Sound (for Hybrid and EV only)": None,
  "Automatic Crash Notification (CAN) / Advanced Automatic Crash Notification (AACN)": None,
  "Event Data Recorder (EDR)": None,
  "Keyless Ignition": None,
  "Daytime Running Light (DRL)": None,
  "Lower Beam Headlamp Light Source": None,
  "Semiautomatic Headlamp Beam Switching": None,
  "Adaptive Driving Beam (ADB)": None,
  "SAE Automation Level": None,
  "SAE Automation Level up to": None,
  "Rear Cross Traffic Alert": None,
  "NCSA Note": None,
  "Bus Length (feet)": None,
  "Bus Floor Configuration Type": "Not Applicable",
  "Bus Type": "Not Applicable",
  "Other Bus Info": None,
  "Custom Motorcycle Type": "Not Applicable",
  "Motorcycle Suspension Type": "Not Applicable",
  "Motorcycle Chassis Type": "Not Applicable",
  "Other Motorcycle Info": None
}
"""
