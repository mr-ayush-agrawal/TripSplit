from fasthtml.common import *
from client.components.user.welcome import welcome_section
from client.components.user.cards import action_cards
from client.components.user.layout import dashboard_layout

def user_dashboard_page(username="User", total_groups=0, total_expenses=0, balance=0.0):
    """Main user dashboard page"""
    content = Div(
        welcome_section(username=username),
        # stats_cards(total_groups=total_groups, total_expenses=total_expenses, balance=balance),
        action_cards()
    )
    
    return dashboard_layout(
        title="Dashboard",
        content=content,
        username=username
    )
