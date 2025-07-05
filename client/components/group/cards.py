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
                A("Add", href=f"/group/{group_id}/add-expense", role="button", cls="btn-outline"),
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

def members_overview_cards(members, member_balances, base_currency, owner_username):
    """Display overview cards for all members"""
    cards = []
    
    for member in members:
        balance = member_balances.get(member, 0.0)
        balance_class = "balance-positive" if balance > 0 else "balance-negative" if balance < 0 else "balance-zero"
        balance_text = f"owes {base_currency} {abs(balance):.2f}" if balance < 0 else f"owed {base_currency} {balance:.2f}" if balance > 0 else "Settled"
        
        # Status indicator
        if member == owner_username:
            status_badge = Span("👑 Admin", cls="badge badge-owner")
            if len([m for m in members if m != owner_username]) > 0:
                # There are other members, owner cannot be removed
                removable_status = Span("Remove other members first", cls="status-warning")
            else:
                # Owner is the only member, can be removed
                removable_status = Span("Can be removed (last member)", cls="status-success") if balance == 0 else Span("Must settle balance first", cls="status-warning")
        elif balance != 0:
            status_badge = Span("💰 Has balance", cls="badge badge-balance")
            removable_status = Span("Must settle balance first", cls="status-warning")
        else:
            status_badge = Span("✅ Settled", cls="badge badge-settled")
            removable_status = Span("Can be removed", cls="status-success")
        
        card = Div(
            Div(
                Div(
                    Div(member, cls="member-name"),
                    status_badge,
                    cls="member-header"
                ),
                Div(
                    Div(f"{balance_text}", cls=f"balance {balance_class}"),
                    removable_status,
                    cls="member-details"
                ),
                cls="member-info"
            ),
            cls="member-card"
        )
        cards.append(card)
    
    return cards
