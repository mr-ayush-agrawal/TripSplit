from fasthtml.common import *


def group_card(name, group_id, balance=0.0, member_count=0, recent_activity="No recent activity"):
    """Redesigned group card with better layout and responsiveness"""
    
    # Determine balance color and text
    if balance > 0:
        balance_color = "#0A9548"
        balance_text = f"+₹{balance:.2f}"
        balance_label = "You are owed"
    elif balance < 0:
        balance_color = "#e74c3c"
        balance_text = f"-₹{abs(balance):.2f}"
        balance_label = "You owe"
    else:
        balance_color = "var(--muted-color)"
        balance_text = "₹0.00"
        balance_label = "Settled up"
    
    return Article(
        Div(  # Flex layout container
            # Left: Group info
            Div(
                H3(name, style="margin: 0; color: var(--color); font-size: 1.2rem;"),
                Small(f"{member_count} members", style="color: var(--muted-color); font-size: 0.85rem;"),
                cls="group-left"
            ),

            # Center: Balance info
            Div(
                Small(balance_label, style="color: var(--muted-color); font-size: 0.8rem;"),
                Strong(balance_text, style=f"color: {balance_color}; font-size: 1.1rem;"),
                cls="group-center"
            ),

            # Right: Buttons
            Div(
                A("View", href=f"/group/{group_id}", role="button", cls="btn-primary"),
                A("Add", href=f"/group/{group_id}/expense", role="button", cls="btn-outline"),
                cls="group-right"
            ),
            cls="group-header"
        ),

        # Recent activity (optional)
        # Div(
        #     P(recent_activity, style="margin-top: 0.5rem; color: var(--muted-color); font-style: italic; font-size: 0.9rem;"),
        #     cls="group-footer"
        # ),

        cls="group-card",
        style="padding: 1rem 1.5rem; border: 1px solid var(--border-color); border-radius: 10px; margin-bottom: 1rem;"
    )