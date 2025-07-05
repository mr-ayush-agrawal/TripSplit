from fasthtml.common import *

def add_members_header(group_name):
    """Header section for add members page"""
    return Div(
        H2(f"Add Members to {group_name}", cls="page-title"),
        P("Add friends to your group by entering their usernames", cls="page-subtitle"),
        cls="add-members-header"
    )

def add_members_form(group_id, error_message=None, success_message=None):
    """Form for adding members"""
    form_content = [
        # Success/Error messages
        *([Div(success_message, cls="alert alert-success")] if success_message else []),
        *([Div(error_message, cls="alert alert-error")] if error_message else []),
        
        # Form fields
        Div(
            Label("Enter Usernames", For="usernames", cls="form-label"),
            P("Enter usernames separated by commas or new lines", cls="form-help"),
            Textarea(
                name="usernames",
                id="usernames",
                placeholder="john_doe, jane_smith, alice123\nor one per line",
                cls="form-textarea",
                rows="4",
                required=True
            ),
            cls="form-group"
        ),
        Div(
            Button("Add Members", type="submit", cls="btn btn-primary"),
            A("Cancel", href=f"/group/{group_id}", cls="btn btn-secondary"),
            cls="form-actions"
        )
    ]
    
    return Form(
        *form_content,
        method="POST",
        cls="add-members-form"
    )

def existing_members_display(members, group_id):
    """Display existing members"""
    if not members:
        return Div()
    
    member_items = [
        Div(
            Span(member, cls="member-name"),
            cls="member-item"
        ) for member in members
    ]
    
    return Div(
        H3("Current Members", cls="section-title"),
        Div(*member_items, cls="members-list"),
        Div(
            A("Finish & Go to Group", href=f"/group/{group_id}", cls="btn btn-success"),
            cls="finish-group-action"
        ),
        cls="existing-members-section"
    )

def add_members_info():
    """Information section about adding members"""
    return Div(
        H3("Tips for Adding Members", cls="section-title"),
        Ul(
            Li("Members must have registered accounts with these exact usernames"),
            Li("You can add multiple members at once by separating usernames with commas"),
            Li("Only the group owner can add new members"),
            Li("Added members will be able to view and add expenses to this group"),
            cls="info-list"
        ),
        cls="add-members-info"
    )



def remove_member_form(removable_members, member_balances, base_currency, group_id, owner_username, members):
    """Form to remove a member"""
    if not removable_members:
        return no_removable_members()
    
    # Create options for members who can be removed (balance = 0)
    member_options = []
    removable_count = 0
    
    for member in removable_members:
        balance = member_balances.get(member, 0.0)
        is_owner = member == owner_username
        other_members_exist = len([m for m in members if m != owner_username]) > 0
        
        if round(balance, 2) == 0.0:
            if is_owner and other_members_exist:
                # Owner with other members still in group - cannot remove
                member_options.append(
                    Option(
                        f"{member} (👑 Admin - Remove other members first)",
                        value=member,
                        disabled=True
                    )
                )
            else:
                # Regular member with zero balance OR owner who is last member - can remove
                label = f"{member} (👑 Last member - Settled)" if is_owner else f"{member} (Settled)"
                member_options.append(
                    Option(
                        label,
                        value=member,
                        selected=False
                    )
                )
                removable_count += 1
        else:
            balance_text = f"owes {abs(balance):.2f}" if balance < 0 else f"owed {balance:.2f}"
            owner_prefix = "👑 " if is_owner else ""
            member_options.append(
                Option(
                    f"{owner_prefix}{member} ({base_currency} {balance_text}) - Cannot remove",
                    value=member,
                    disabled=True
                )
            )
    
    if removable_count == 0:
        return Div(
            Div(
                "⚠️ No members can be removed at this time.",
                cls="alert alert-warning"
            ),
            P("Members must settle their balances before removal. If you're the owner, remove other members first before removing yourself."),
            cls="no-removable-info"
        )
    
    return Form(
        Div(
            Label("Select member to remove:", For="member_username", cls="form-label"),
            Select(
                Option("Choose a member...", value="", selected=True),
                *member_options,
                name="member_username",
                id="member_username",
                cls="form-select",
                required=True
            ),
            cls="form-group"
        ),
        
        Div(
            "⚠️ Warning: This action cannot be undone. The member will lose access to this group and all its data.",
            cls="alert alert-warning"
        ),
        
        Div(
            Button("Remove Member", type="submit", cls="btn btn-danger"),
            A("Cancel", href=f"/group/{group_id}", cls="btn btn-secondary"),
            cls="form-actions"
        ),
        
        method="POST",
        cls="remove-member-form"
    )

def no_removable_members():
    """Display when no members can be removed"""
    return Div(
        Div(
            "ℹ️ No members available for removal.",
            cls="alert alert-info"
        ),
        P("Either all members have outstanding balances, or you are the only member in this group."),
        cls="no-removable-info"
    )

def show_message(message, type="info"):
    """Display success/error messages"""
    icon = "✅" if type == "success" else "❌" if type == "error" else "ℹ️"
    return Div(
        f"{icon} {message}",
        cls=f"alert alert-{type}"
    )
