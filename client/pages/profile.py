from fasthtml.common import *
from client.components.user.layout import dashboard_layout
from client.components.user.profile_info import profile_header, profile_grid
from client.components.user.profile_update_modal import profile_modals

def profile_page(profile_data, total_groups=0):
    """Main profile page"""
    # Extract profile data
    name = profile_data.get("name", "Unknown User")
    username = profile_data.get("user_name", "unknown")
    email = profile_data.get("email", "")
    currency = profile_data.get("currency", "INR")
    
    # Organize data for display
    personal_info = {
        "Full Name": name
    }
    
    account_info = {
        "Username": username,
        "Email": email,
        "Currency": currency
    }
    
    # Build page content
    content = Div(
        profile_header(name=name, username=username),
        profile_grid(
            personal_info=personal_info,
            account_info=account_info, 
            total_groups=total_groups
        ),
        # Add all modals
        *profile_modals(profile_data)
    )
    
    return dashboard_layout(
        title="Profile",
        content=content,
        username=name
    )

