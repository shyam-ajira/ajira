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

        # First remove custom field entries
        remove_custom_field_entries(custom_fields)
        
        # Then remove the columns from Lead table
        remove_lead_table_columns(custom_fields)

        # Clear cache after all changes
        frappe.clear_cache(doctype="Lead")
        frappe.db.commit()  # Commit changes
        frappe.msgprint("Custom fields removed successfully during uninstallation.")
        
    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(str(e), "Custom Fields Uninstallation Error")
        frappe.msgprint(f"An error occurred while removing custom fields: {str(e)}")

def remove_custom_field_entries(custom_fields):
    """Remove entries from Custom Field doctype"""
    for field in custom_fields:
        try:
            if frappe.db.exists("Custom Field", field.name):
                # Delete the custom field
                frappe.delete_doc("Custom Field", field.name, force=1, ignore_permissions=True)
                frappe.db.commit()  # Commit after each deletion
        except Exception as e:
            frappe.db.rollback()
            frappe.log_error(
                f"Error removing field {field.fieldname}: {str(e)}", 
                "Custom Field Removal Error"
            )

def remove_lead_table_columns(custom_fields):
    """Remove columns from Lead table"""
    if not custom_fields:
        return

    if not frappe.db:
        frappe.connect()
        
    try:
        # Disable foreign key checks
        frappe.db.sql("SET FOREIGN_KEY_CHECKS=0")
        
        # Build a single ALTER TABLE statement for all columns
        alter_statements = []
        for field in custom_fields:
            alter_statements.append(f"DROP COLUMN IF EXISTS `{field.fieldname}`")
        
        if alter_statements:
            query = f"ALTER TABLE `tabLead` {', '.join(alter_statements)}"
            frappe.db.sql(query)
            frappe.db.commit()
            
            # Rebuild the Lead DocType
            frappe.reload_doctype("Lead")
            
    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(message=str(e), title="Column Removal Error")

    finally:
        # Re-enable foreign key checks
        frappe.db.sql("SET FOREIGN_KEY_CHECKS=1")
        frappe.db.commit()
