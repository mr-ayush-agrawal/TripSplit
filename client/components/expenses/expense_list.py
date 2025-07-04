from fasthtml.common import *
from client.components.expenses.card import create_expense_card

def expense_list(group_data, expenses_data):
    """Expenses section with expense cards"""
    expenses = expenses_data.get("expenses", [])
    user_net_amount = expenses_data.get("amount", 0.0)
    base_currency = expenses_data.get("currency", group_data.get("base_currency", "INR"))
    group_id = group_data.get("group_id", "")
    
    # User's net balance summary
    net_balance_class = "net-positive" if user_net_amount > 0 else "net-negative" if user_net_amount < 0 else "net-zero"
    net_balance_text = f"You are owed {base_currency} {abs(user_net_amount):.2f}" if user_net_amount > 0 else f"You owe {base_currency} {abs(user_net_amount):.2f}" if user_net_amount < 0 else "You are settled up"
    
    # Create expense cards
    expense_cards = []
    for expense in expenses:
        expense_card = create_expense_card(expense, group_id, base_currency)
        expense_cards.append(expense_card)
    
    # Empty state
    if not expense_cards:
        expense_cards.append(
            Div(
                Div("💸", cls="empty-icon"),
                H3("No expenses yet", cls="empty-title"),
                P("Add your first expense to start tracking group spending", cls="empty-description"),
                A("Add Expense", href=f"/group/{group_id}/add-expense", cls="btn btn-primary"),
                cls="empty-state"
            )
        )
    
    return Div(
        Div(
            H2("Expenses", cls="section-title"),
            Div(
                Span(f"{net_balance_text}", cls=f"net-balance {net_balance_class}"),
                cls="user-balance-summary"
            ),
            cls="expenses-header"
        ),
        Div(*expense_cards, cls="expenses-list"),
        cls="expenses-section"
    )
