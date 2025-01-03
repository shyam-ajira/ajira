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
        frappe.msgprint("Custom fields removed successfully during uninstallation.")
        
    except Exception as e:
        frappe.log_error(str(e), "Custom Fields Uninstallation Error")
        frappe.msgprint(f"An error occurred while removing custom fields: {str(e)}")

def remove_custom_field_entries(custom_fields):
    """Remove entries from Custom Field doctype"""
    for field in custom_fields:
        try:
            if frappe.db.exists("Custom Field", field.name):
                frappe.log(f"Removing custom field: {field.name}")
                frappe.delete_doc("Custom Field", field.name, force=True)
        except Exception as e:
            frappe.log_error(
                f"Error removing field {field.fieldname}: {str(e)}", 
                "Custom Field Removal Error"
            )

def remove_lead_table_columns():
    """Remove columns from Lead table"""
    if not frappe.db:
        frappe.connect()  # Ensure database connection if not already established
        
    try:
        # Disable foreign key checks
        frappe.db.sql("SET FOREIGN_KEY_CHECKS=0")
        
        # Query to drop columns
        query = """
            ALTER TABLE `tabLead` 
            DROP COLUMN IF EXISTS `district`,
            DROP COLUMN IF EXISTS `municipality`,
            DROP COLUMN IF EXISTS `ward`,
            DROP COLUMN IF EXISTS `unit_type`,
            DROP COLUMN IF EXISTS `ropani`,
            DROP COLUMN IF EXISTS `aana`,
            DROP COLUMN IF EXISTS `paisa`,
            DROP COLUMN IF EXISTS `daam`,
            DROP COLUMN IF EXISTS `bigha`,
            DROP COLUMN IF EXISTS `kattha`,
            DROP COLUMN IF EXISTS `dhur`,
            DROP COLUMN IF EXISTS `sq_feet`,
            DROP COLUMN IF EXISTS `sq_mtr`
        """
        # Execute query
        frappe.db.sql(query)
        frappe.db.commit()
        frappe.log("Successfully removed columns from `tabLead`")

    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(message=str(e), title="Column Removal Error")

    finally:
        # Re-enable foreign key checks
        frappe.db.sql("SET FOREIGN_KEY_CHECKS=1")
        frappe.db.commit()