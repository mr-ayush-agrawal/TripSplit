from fasthtml.common import *
from client.components.group.member import add_members_header, add_members_form, existing_members_display, add_members_info
from client.components.group.cards import members_overview_cards
from client.components.group.member import remove_member_form, show_message, no_removable_members
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

def remove_members_page(username="User", group_data=None, error_message=None, success_message=None):
    """Remove members page layout"""
    if not group_data:
        group_data = {}
    
    group_name = group_data.get("group_name", "Group")
    group_id = group_data.get("group_id", "")
    members = group_data.get("members", [])
    member_balances = group_data.get("member_balances", {})
    base_currency = group_data.get("base_currency", "INR")
    owner_username = group_data.get("owner_username", "")
    
    all_members = members.copy()
    other_members = [m for m in members if m != owner_username]

    # First, determine who can be considered for removal based on group hierarchy
    if len(other_members) == 0:
        # Owner is the only member, they can be considered for removal
        candidates_for_removal = [owner_username]
    else:
        # There are other members, owner cannot be removed yet
        candidates_for_removal = other_members

    # Now filter candidates by balance - only members with zero balance can actually be removed
    removable_members = []
    for member in candidates_for_removal:
        balance = member_balances.get(member, 0.0)
        if round(balance, 2) == 0.0:
            removable_members.append(member)
    
    content = Div(
        # Header
        Div(
            Div(
                H1(f"Remove Members from {group_name}", cls="page-title"),
                P(f"Manage group membership", cls="page-subtitle"),
                cls="header-text"
            ),
            Div(
                A("← Back to Group", href=f"/group/{group_id}", cls="btn btn-secondary"),
                cls="header-actions"
            ),
            cls="page-header"
        ),
        
        # Messages
        show_message(error_message, "error") if error_message else None,
        show_message(success_message, "success") if success_message else None,
        
        # Main content
        Div(
            # Current members overview
            Div(
                H2("Current Members", cls="section-title"),
                Div(
                    *members_overview_cards(members, member_balances, base_currency, owner_username),
                    cls="members-overview"
                ),
                cls="members-section"
            ),
            
            # Remove member form
            Div(
                H2("Remove Member", cls="section-title"),
                remove_member_form(removable_members, member_balances, base_currency, group_id, owner_username, members) if removable_members else no_removable_members(),                cls="remove-section"
            ),
            
            cls="remove-members-content"
        ),
        
        cls="remove-members-container"
    )
    
    return dashboard_layout(
        title=f"Remove Members - {group_name}",
        content=content,
        username=username
    )
