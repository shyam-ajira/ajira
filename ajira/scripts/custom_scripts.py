import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def add_custom_fields():
    custom_fields = {
        "Lead": [
            {
                "fieldname": "land_details_section",
                "label": "Land Details",
                "fieldtype": "Tab Break",
                "insert_after": "blog_subscriber",
                "permlevel": 0
            },
            # Land Information Section
            {
                "fieldname": "land_section",
                "label": "Land Information",
                "fieldtype": "Section Break",
                "insert_after": "land_details_section",
                "permlevel": 0
            },
            {
                "fieldname": "district",
                "label": "District",
                "fieldtype": "Data",
                "mandatory": 1,
                "insert_after": "land_section",
                "in_list_view": 1,
                "permlevel": 0
            },
            {
                "fieldname": "col_break_1",
                "fieldtype": "Column Break",
                "insert_after": "district",
                "permlevel": 0
            },
            {
                "fieldname": "municipality",
                "label": "Municipality",
                "fieldtype": "Data",
                "mandatory": 1,
                "insert_after": "col_break_1",
                "in_list_view": 1,
                "permlevel": 0
            },
            {
                "fieldname": "col_break_2",
                "fieldtype": "Column Break",
                "insert_after": "municipality",
                "permlevel": 0
            },
            {
                "fieldname": "ward",
                "label": "Ward",
                "fieldtype": "Int",
                "mandatory": 1,
                "insert_after": "col_break_2",
                "in_list_view": 1,
                "permlevel": 0
            },
            {
                "fieldname": "col_break_3",
                "fieldtype": "Column Break",
                "insert_after": "ward",
                "permlevel": 0
            },
            {
                "fieldname": "col_break_4",
                "fieldtype": "Column Break",
                "insert_after": "col_break_3",
                "permlevel": 0
            },
            # Area Type Selection Section
            {
                "fieldname": "area_type_section",
                "label": "Area Type Selection",
                "fieldtype": "Section Break",
                "insert_after": "col_break_4",
                "permlevel": 0
            },
            {
                "fieldname": "unit_type",
                "label": "Select Area Type",
                "fieldtype": "Select",
                "options": "Hilly Area\nTerai Area",
                "mandatory": 1,
                "insert_after": "area_type_section",
                "in_list_view": 1
            },
            {
                "fieldname": "col_break_5",
                "fieldtype": "Column Break",
                "insert_after": "unit_type",
                "permlevel": 0
            },
            {
                "fieldname": "col_break_6",
                "fieldtype": "Column Break",
                "insert_after": "col_break_5",
                "permlevel": 0
            },
            # Hilly Area Section
            {
                "fieldname": "rapd_section",
                "label": "R-A-P-D",
                "fieldtype": "Section Break",
                "insert_after": "col_break_6",
                "depends_on": "eval:doc.unit_type == 'Hilly Area'"
            },
            {
                "fieldname": "ropani",
                "label": "Ropani",
                "fieldtype": "Float",
                "depends_on": "eval:doc.unit_type == 'Hilly Area'",
                "insert_after": "rapd_section"
            },
            {
                "fieldname": "col_break_rapd_1",
                "fieldtype": "Column Break",
                "insert_after": "ropani"
            },
            {
                "fieldname": "aana",
                "label": "Aana",
                "fieldtype": "Float",
                "depends_on": "eval:doc.unit_type == 'Hilly Area'",
                "insert_after": "col_break_rapd_1"
            },
            {
                "fieldname": "col_break_rapd_2",
                "fieldtype": "Column Break",
                "insert_after": "aana"
            },
            {
                "fieldname": "paisa",
                "label": "Paisa",
                "fieldtype": "Float",
                "depends_on": "eval:doc.unit_type == 'Hilly Area'",
                "insert_after": "col_break_rapd_2"
            },
            {
                "fieldname": "col_break_rapd_3",
                "fieldtype": "Column Break",
                "insert_after": "paisa"
            },
            {
                "fieldname": "daam",
                "label": "Daam",
                "fieldtype": "Float",
                "depends_on": "eval:doc.unit_type == 'Hilly Area'",
                "insert_after": "col_break_rapd_3"
            },
            {
                "fieldname": "col_break_rapd_4",
                "fieldtype": "Column Break",
                "insert_after": "daam"
            },
            {
                "fieldname": "col_break_rapd_5",
                "fieldtype": "Column Break",
                "insert_after": "col_break_rapd_4"
            },
            # Terai Area Section
            {
                "fieldname": "bkd_section",
                "label": "B-K-D",
                "fieldtype": "Section Break",
                "insert_after": "col_break_rapd_5",
                "depends_on": "eval:doc.unit_type == 'Terai Area'"
            },
            {
                "fieldname": "bigha",
                "label": "Bigha",
                "fieldtype": "Float",
                "depends_on": "eval:doc.unit_type == 'Terai Area'",
                "insert_after": "bkd_section"
            },
            {
                "fieldname": "col_break_bkd_1",
                "fieldtype": "Column Break",
                "insert_after": "bigha"
            },
            {
                "fieldname": "kattha",
                "label": "Kattha",
                "fieldtype": "Float",
                "depends_on": "eval:doc.unit_type == 'Terai Area'",
                "insert_after": "col_break_bkd_1"
            },
            {
                "fieldname": "col_break_bkd_2",
                "fieldtype": "Column Break",
                "insert_after": "kattha"
            },
            {
                "fieldname": "dhur",
                "label": "Dhur",
                "fieldtype": "Float",
                "depends_on": "eval:doc.unit_type == 'Terai Area'",
                "insert_after": "col_break_bkd_2"
            },
            {
                "fieldname": "col_break_bkd_3",
                "fieldtype": "Column Break",
                "insert_after": "dhur"
            },
            {
                "fieldname": "col_break_bkd_4",
                "fieldtype": "Column Break",
                "insert_after": "col_break_bkd_3"
            },
            # Square Feet and Meter Section
            {
                "fieldname": "square_feet_meter_section",
                "label": "Square Feet and Meter",
                "fieldtype": "Section Break",
                "insert_after": "col_break_bkd_4"
            },
            {
                "fieldname": "sq_feet",
                "label": "Square Feet",
                "fieldtype": "Float",
                "insert_after": "square_feet_meter_section"
            },
            {
                "fieldname": "col_break_sq_1",
                "fieldtype": "Column Break",
                "insert_after": "sq_feet"
            },
            {
                "fieldname": "sq_mtr",
                "label": "Square Meter",
                "fieldtype": "Float",
                "insert_after": "col_break_sq_1"
            },
            {
                "fieldname": "col_break_sq_2",
                "fieldtype": "Column Break",
                "insert_after": "sq_mtr"
            },
            {
                "fieldname": "col_break_sq_3",
                "fieldtype": "Column Break",
                "insert_after": "col_break_sq_2"
            }
        ]
    }

    try:
        create_custom_fields(custom_fields)
        frappe.db.commit()
        frappe.clear_cache()
        frappe.msgprint("Custom fields added successfully.")
    except Exception as e:
        frappe.log_error(f"Error creating custom fields: {e}", "Custom Field Error")
