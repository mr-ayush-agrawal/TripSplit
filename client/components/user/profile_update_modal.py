# client/components/profile/modals.py
from fasthtml.common import *

def edit_modal(modal_id, title, fields, action_url, method="POST"):
    """Generic edit modal for profile information"""
    form_fields = []
    for field_name, field_info in fields.items():
        field_type = field_info.get('type', 'text')
        field_value = field_info.get('value', '')
        field_label = field_info.get('label', field_name.title())
        field_required = field_info.get('required', False)
        
        if field_type == 'select':
            options = [Option(opt, value=opt, selected=(opt == field_value)) for opt in field_info.get('options', [])]
            form_fields.extend([
                Label(field_label, **{"for": field_name}),
                Select(*options, name=field_name, required=field_required)
            ])
        else:
            form_fields.extend([
                Label(field_label, **{"for": field_name}),
                Input(type=field_type, name=field_name, value=field_value, required=field_required)
            ])
    
    return Div(
        Div(
            Article(
                Header(
                    H3(title, style="margin: 0; text-align: center;"),
                    style="border-bottom: 1px solid var(--border-color); margin-bottom: 1.5rem;"
                ),
                Form(
                    *form_fields,
                    Footer(
                        Div(
                            Button("Cancel", 
                                  type="button",
                                  cls="outline", 
                                  onclick=f"document.getElementById('{modal_id}').style.display='none'",
                                  style="margin-right: 1rem;"),
                            Button("Save Changes", 
                                  type="submit",
                                  style="background: var(--primary); border-color: var(--primary);"),
                            style="display: flex; justify-content: center; gap: 1rem;"
                        ),
                        style="text-align: center; margin-top: 2rem;"
                    ),
                    hx_post=action_url if method == "POST" else None,
                    hx_put=action_url if method == "PUT" else None,
                    hx_trigger="submit",
                    hx_target="body",
                    hx_swap="outerHTML",
                    onsubmit=f"document.getElementById('{modal_id}').style.display='none'"
                ),
                style="max-width: 500px; margin: 0 auto; position: relative;"
            ),
            style="display: flex; align-items: center; justify-content: center; height: 100vh; padding: 2rem;"
        ),
        id=modal_id,
        style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999;",
        onclick=f"if(event.target.id === '{modal_id}') document.getElementById('{modal_id}').style.display='none'"
    )

def password_change_modal():
    """Specific modal for password change"""
    return Div(
        Div(
            Article(
                Header(
                    H3("Change Password", style="margin: 0; text-align: center;"),
                    style="border-bottom: 1px solid var(--border-color); margin-bottom: 1.5rem;"
                ),
                Form(
                    Label("Current Password", **{"for": "current_password"}),
                    Input(type="password", name="current_password", required=True),
                    
                    Label("New Password", **{"for": "new_password"}),
                    Input(type="password", name="new_password", required=True),
                    
                    Label("Confirm New Password", **{"for": "confirm_password"}),
                    Input(type="password", name="new_password", required=True),
                    
                    Footer(
                        Div(
                            Button("Cancel", 
                                  type="button",
                                  cls="outline", 
                                  onclick="document.getElementById('password-modal').style.display='none'",
                                  style="margin-right: 1rem;"),
                            Button("Update Password", 
                                  type="submit",
                                  style="background: var(--del-color, #d32f2f); border-color: var(--del-color, #d32f2f);"),
                            style="display: flex; justify-content: center; gap: 1rem;"
                        ),
                        style="text-align: center; margin-top: 2rem;"
                    ),
                    hx_post="/user/change-password",
                    hx_trigger="submit",
                    hx_target="body",
                    hx_swap="outerHTML",
                    onsubmit="document.getElementById('password-modal').style.display='none'"
                ),
                style="max-width: 500px; margin: 0 auto; position: relative;"
            ),
            style="display: flex; align-items: center; justify-content: center; height: 100vh; padding: 2rem;"
        ),
        id="password-modal",
        style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999;",
        onclick="if(event.target.id === 'password-modal') document.getElementById('password-modal').style.display='none'"
    )

def profile_modals(profile_data):
    """All profile-related modals"""
    personal_fields = {
        "name": {
            "type": "text",
            "value": profile_data.get("name", ""),
            "label": "Full Name",
            "required": True
        }
    }
    
    account_fields = {
        "email": {
            "type": "email",
            "value": profile_data.get("email", ""),
            "label": "Email Address", 
            "required": True
        },
        "currency": {
            "type": "select",
            "value": profile_data.get("currency", "INR"),
            "label": "Preferred Currency",
            "options": ["INR", "USD", "EUR", "GBP", "JPY", "AUD", "CAD"],
            "required": True
        }
    }
    
    return [
        edit_modal(
            modal_id="personal-info-modal",
            title="Edit Personal Information",
            fields=personal_fields,
            action_url="/user/profile/personal"
        ),
        edit_modal(
            modal_id="account-info-modal", 
            title="Edit Account Information",
            fields=account_fields,
            action_url="/user/profile/account"
        ),
        password_change_modal()
    ]