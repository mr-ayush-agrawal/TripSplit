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
