import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from ajira.scripts.custom_scripts import add_custom_fields

def before_install():
    pass

def after_install():
    try:
        # Call your existing add_custom_fields function
        custom_fields=add_custom_fields()
        frappe.log(f"Debug: add_custom_fields() returned: {custom_fields}")
        if custom_fields:
            frappe.msgprint(f"Custom fields created during app installation: {custom_fields}")
            frappe.log(f"Custom fields created during app installation: {custom_fields}")
        else:
            frappe.msgprint("No custom fields were created during app installation.")
            frappe.log("No custom fields were created during app installation.")

    except Exception as e:
        frappe.log_error(f"Error during installation while creating custom fields: {e}", "Installation Error")
