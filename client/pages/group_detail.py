from fasthtml.common import *
from client.components.user.layout import dashboard_layout
from client.components.group.detail_view import (
    single_group_header, group_stats_section, members_section
)
from client.components.expenses.expense_list import expense_list


def single_group_page(username="User", group_data=None, expenses_data=None):
    """Single group page layout"""
    if not group_data:
        group_data = {}
    if not expenses_data:
        expenses_data = {}
    
    is_owner = group_data.get("owner_username") == username
    
    content = Div(
        single_group_header(group_data, is_owner),
        Div(
            # Main content area
            Div(
                group_stats_section(group_data, expenses_data),
                expense_list(group_data, expenses_data),
                cls="main-content"
            ),
            # Sidebar
            Div(
                members_section(group_data, is_owner),
                cls="sidebar"
            ),
            cls="group-layout"
        ),
        cls="single-group-container"
    )
    
    return dashboard_layout(
        title=f"{group_data.get('group_name', 'Group')} - Details",
        content=content,
        username=username
    )