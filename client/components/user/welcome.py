from fasthtml.common import *

def welcome_section(username="User"):
    """Welcome section with greeting"""
    return Section(
        Div(
            H1(f"Welcome back, {username}!", style="text-align: center; margin-bottom: 1rem;"),
            P("Manage your expenses and groups from your dashboard", 
              style="text-align: center; color: var(--muted-color); font-size: 1.1rem;"),
            style="text-align: center; padding: 2rem 0;"
        )
    )