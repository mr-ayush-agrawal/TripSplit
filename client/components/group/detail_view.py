from fasthtml.common import *

def single_group_header(group_data, is_owner):
    """Header for single group view - different from groups home page header"""
    group_name = group_data.get("group_name", "Group")
    group_description = group_data.get("group_description", "")
    group_id = group_data.get("group_id", "")
    
    action_buttons = []
    # if is_owner:
    #     action_buttons.extend([
    #         A("Add Members", href=f"/group/{group_id}/add-members", cls="btn btn-secondary"),
    #         A("Manage Group", href=f"/group/{group_id}/manage", cls="btn btn-outline")
    #     ])
    action_buttons.append(A("Simplified Debts", href=f"/group/{group_id}/simplified-debts", cls="btn btn-success"))
    action_buttons.append(A("Add Expense", href=f"/group/{group_id}/add-expense", cls="btn btn-primary"))
    
    return Div(
        Div(
            H1(group_name, cls="group-title"),
            P(group_description, cls="group-description") if group_description else None,
            cls="group-info"
        ),
        Div(*action_buttons, cls="group-actions") if action_buttons else None,
        cls="group-header"
    )


def group_stats_section(group_data, expenses_data):
    """Group statistics section"""
    members_count = len(group_data.get("members", []))
    total_expense = group_data.get("total_expense", 0.0)
    expenses_count = len(expenses_data.get("expenses", []))
    base_currency = group_data.get("base_currency", "INR")
    
    stats = [
        ("Members", str(members_count), "👥"),
        ("Total Spent", f"{base_currency} {total_expense:.2f}", "💰"),
        ("Expenses", str(expenses_count), "📝")
    ]
    
    stat_cards = [
        Div(
            Div(icon, cls="stat-icon"),
            Div(
                Div(value, cls="stat-value"),
                Div(label, cls="stat-label"),
                cls="stat-content"
            ),
            cls="stat-card"
        ) for label, value, icon in stats
    ]
    
    return Div(
        H2("Group Statistics", cls="section-title"),
        Div(*stat_cards, cls="stats-grid"),
        cls="group-stats-section"
    )

def members_section(group_data, is_owner):
    """Members section with balances"""
    members = group_data.get("members", [])
    member_balances = group_data.get("member_balances", {})
    base_currency = group_data.get("base_currency", "INR")
    owner_username = group_data.get("owner_username", "")
    group_id = group_data.get("group_id", "")
    
    member_items = []
    for member in members:
        balance = member_balances.get(member, 0.0)
        balance_class = "balance-positive" if balance > 0 else "balance-negative" if balance < 0 else "balance-zero"
        balance_text = f"owes {base_currency} {abs(balance):.2f}" if balance < 0 else f"owed {base_currency} {balance:.2f}" if balance > 0 else "Settled"
        
        member_item = Div(
            Div(
                Div(member, cls="member-name"),
                Div("👑 Admin" if member == owner_username else "", cls="member-role"),
                cls="member-info"
            ),
            Div(
                Div(f"{balance_text}", cls=f"member-balance {balance_class}"),
                cls="member-balance-container"
            ),
            cls="member-item"
        )
        member_items.append(member_item)
    
    # Add member management buttons for owner
    manage_buttons = []
    if is_owner:
        manage_buttons = [
            A("Add Members", href=f"/group/{group_id}/add-members", cls="btn btn-sm btn-primary"),
            A("Remove Members", href=f"/group/{group_id}/remove-members", cls="btn btn-sm btn-secondary")
        ]
    
    return Div(
        Div(
            H2("Members", cls="section-title"),
            Div(f"{len(members)} members", cls="members-count"),
            cls="members-header"
        ),
        Div(*member_items, cls="members-list"),
        Div(*manage_buttons, cls="member-actions") if manage_buttons else None,
        cls="members-section"
    )
