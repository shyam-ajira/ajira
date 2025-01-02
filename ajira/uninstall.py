import frappe

def before_uninstall():
    remove_custom_fields()

def after_uninstall():
    pass

def remove_custom_fields():
    try:
        # Get all custom fields for the Lead doctype
        custom_fields = frappe.get_all(
            "Custom Field",
            filters={"dt": "Lead"},
            fields=["name", "fieldname"]
        )

        # Remove each custom field
        for field in custom_fields:
            try:
                # Check if the custom field still exists before attempting deletion
                if frappe.db.exists("Custom Field", field.name):
                    frappe.log(f"ALTER TABLE `tabLead` DROP COLUMN `{field.fieldname}`")#show message in console
                    # Delete the custom field
                    frappe.delete_doc("Custom Field", field.name, force=True)
                
                # Check if the column exists in the database table before dropping it
                try:
                    if frappe.db.has_column("tabLead", field.fieldname):
                        query = f"ALTER TABLE `tabLead` DROP COLUMN `{field.fieldname}`"
                        frappe.log(f"Shyam--LTER TABLE `tabLead` DROP COLUMN `{query}`")
                        frappe.db.sql(query)
                    
                    # Commit the transaction for each field
                    frappe.db.commit()
                except Exception as e:
                    # Log errors for each individual field without interrupting the loop
                    frappe.log_error(f"Error removing column {field.fieldname}: {str(e)}", "Column Removal Error")
                    frappe.log(f"Error removing column {field.fieldname}: {str(e)}", "Column Removal Error")
            except Exception as e:
                # Log errors for each individual field without interrupting the loop
                frappe.log_error(f"Error removing field {field.fieldname}: {str(e)}", "Custom Field Removal Error")

        # Clear cache after all changes
        frappe.clear_cache(doctype="Lead")
        frappe.msgprint("Custom fields removed successfully during uninstallation.")
        
    except Exception as e:
        # Log general errors and notify the user
        frappe.log_error(str(e), "Custom Fields Uninstallation Error")
        frappe.msgprint(f"An error occurred while removing custom fields: {str(e)}")
