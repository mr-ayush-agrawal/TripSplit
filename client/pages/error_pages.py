from fasthtml.common import *
from client.components.user.layout import dashboard_layout

def group_not_found(username):
    """Page shown when group is not found"""
    content = Div(
        Div(
            H1("Group Not Found", cls="error-title"),
            P("The group you're looking for doesn't exist or has been deleted.", cls="error-message"),
            A("Back to Groups", href="/group/", cls="btn btn-primary"),
            cls="error-content"
        ),
        cls="error-page"
    )
    
    return dashboard_layout(
        title="Group Not Found",
        content=content,
        username=username
    )

def group_access_denied(username):
    """Page shown when user doesn't have access to group"""
    content = Div(
        Div(
            H1("Access Denied", cls="error-title"),
            P("You don't have permission to view this group.", cls="error-message"),
            A("Back to Groups", href="/group/", cls="btn btn-primary"),
            cls="error-content"
        ),
        cls="error-page"
    )
    
    return dashboard_layout(
        title="Access Denied",
        content=content,
        username=username
    )