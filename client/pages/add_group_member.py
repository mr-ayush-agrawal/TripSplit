from fasthtml.common import *
from client.components.group.add_member import add_members_header, add_members_form, existing_members_display, add_members_info
from client.components.user.layout import dashboard_layout

def add_members_page(username="User", group_data=None, error_message=None, success_message=None):
    """Add members page component"""
    if not group_data:
        group_data = {}
    
    group_name = group_data.get("group_name", "Group")
    existing_members = group_data.get("members", [])
    group_id = group_data.get("group_id", "")
    
    content = Div(
        add_members_header(group_name),
        add_members_form(group_id, error_message, success_message),
        existing_members_display(existing_members, group_id),
        add_members_info(),
        cls="add-members-container"
    )
    
    return dashboard_layout(
        title=f"Add Members - {group_name}",
        content=content,
        username=username
    )