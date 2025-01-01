import frappe

def get_context(context):
    context.title = "Add New Member"
    
    # Get list of professions from Member doctype
    context.professions = frappe.get_meta("Member").get_field("profession").options.split("\n")
    
    # Get list of roles from Member doctype
    context.roles = frappe.get_meta("Member").get_field("role").options.split("\n")
    
    # Get list of subjects (you may want to customize this list)
    context.subjects = [
        "Arabic",
        "French",
        "English",
        "Mathematics",
        "Physics",
        "Chemistry",
        "Biology",
        "History",
        "Geography",
        "Philosophy",
        "Islamic Studies",
        "Physical Education",
        "Computer Science",
        "Economics",
        "Sociology"
    ]
    
    # Get list of role types
    context.role_types = [
        "Principal",
        "Vice Principal",
        "Department Head",
        "Administrative Staff",
        "Support Staff"
    ]

@frappe.whitelist()
def save_member(data):
    """Save new member to the database"""
    try:
        doc = frappe.get_doc({
            "doctype": "Member",
            "full_name": data.get("full_name"),
            "birth_date": data.get("birth_date"),
            "gender": data.get("gender"),
            "profession": data.get("profession"),
            "subject": data.get("subject"),
            "institution_branch": data.get("institution_branch"),
            "education_level": data.get("education_level"),
            "role": data.get("role"),
            "role_type": data.get("role_type"),
            "phone": data.get("phone"),
            "email": data.get("email")
        })
        doc.insert()
        return {"success": True, "message": "Member added successfully"}
    except Exception as e:
        frappe.throw(str(e))
