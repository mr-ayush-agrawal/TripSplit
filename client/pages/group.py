from fasthtml.common import *
from client.components.group.cards import *
from client.components.group.creation import create_group_info, group_creation_steps, create_group_form
from client.components.user.layout import dashboard_layout
from client.components.group.layout import groups_header, empty_groups_state, groups_grid


def create_group_page(username="User", error_message=None):
    """Create group page"""
    content = Div(
        group_creation_steps(),
        create_group_form(error_message),
        create_group_info(),
        cls="create-group-container"
    )
    
    return dashboard_layout(
        title="Create Group",
        content=content,
        username=username
    )


def groups_list_page(username="User", user_groups=None):
    if user_groups is None:
        user_groups = []

    total_groups = len(user_groups)
    total_balance = sum(group["balance"] for group in user_groups)

    content = Div(
        Div(  
            groups_header(total_groups, total_balance),
            groups_grid(user_groups) if user_groups else empty_groups_state(),
            cls="full-width-wrapper"
        )
    )

    return dashboard_layout(
        title="Groups",
        content=content,
        username=username
    )