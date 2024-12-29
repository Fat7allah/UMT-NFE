app_name = "umt_nfe"
app_title = "UMT NFE"
app_publisher = "Codeium"
app_description = "National Federation of Education Management System"
app_email = "contact@codeium.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_js = "/assets/js/umt_nfe.min.js"
app_include_css = "/assets/css/umt_nfe.min.css"

# include js, css files in header of web template
# web_include_css = "/assets/umt_nfe/css/umt_nfe_web.css"
# web_include_js = "/assets/umt_nfe/js/umt_nfe_web.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "umt_nfe/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Member": "public/js/member.js",
    "Membership Card": "public/js/membership_card.js",
    "Federation Structure": "public/js/federation_structure.js",
    "Mutual Structure": "public/js/mutual_structure.js",
    "Income": "public/js/income.js",
    "Expense": "public/js/expense.js"
}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------
# application home page (will override Website Settings)
home_page = "login"

# website user home page (by Role)
role_home_page = {
    "System Manager": "UMT NFE"
}

# Generators
# ----------

# Document Events
# ---------------
doc_events = {
    "Member": {
        "validate": "umt_nfe.umt_nfe.doctype.member.member.validate",
        "before_save": "umt_nfe.umt_nfe.doctype.member.member.before_save"
    },
    "Membership Card": {
        "validate": "umt_nfe.umt_nfe.doctype.membership_card.membership_card.validate",
        "before_save": "umt_nfe.umt_nfe.doctype.membership_card.membership_card.before_save"
    },
    "Federation Structure": {
        "validate": "umt_nfe.umt_nfe.doctype.federation_structure.federation_structure.validate"
    },
    "Mutual Structure": {
        "validate": "umt_nfe.umt_nfe.doctype.mutual_structure.mutual_structure.validate"
    },
    "Income": {
        "validate": "umt_nfe.umt_nfe.doctype.income.income.validate",
        "before_save": "umt_nfe.umt_nfe.doctype.income.income.before_save",
        "on_trash": "umt_nfe.umt_nfe.doctype.income.income.on_trash"
    },
    "Expense": {
        "validate": "umt_nfe.umt_nfe.doctype.expense.expense.validate"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "umt_nfe.tasks.daily"
    ],
    "monthly": [
        "umt_nfe.tasks.monthly"
    ]
}

# Desktop Icons
# ---------------

# Desk properties
# --------------
desk_properties = {
    "UMT NFE": {
        "module_name": "UMT NFE",
        "type": "module",
        "label": "UMT NFE",
        "link": "List/Member",
        "color": "#1abc9c",
        "icon": "octicon octicon-organization",
        "category": "Modules"
    }
}

# Testing
# -------
# before_tests = "umt_nfe.install.before_tests"

# Overriding Methods
# ---------------
#
# override_whitelisted_methods = {
#     "frappe.desk.doctype.event.event.get_events": "umt_nfe.event.get_events"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["umt_nfe.utils.before_request"]
# after_request = ["umt_nfe.utils.after_request"]

# Job Events
# ----------
# before_job = ["umt_nfe.utils.before_job"]
# after_job = ["umt_nfe.utils.after_job"]
