from fasthtml.common import *

def group_expense_card(expense, group_id, base_currency):
    """Create individual expense card"""
    expense_id = expense.get("expense_id", "")
    title = expense.get("title", "Untitled Expense")
    description = expense.get("description", "")
    amount = expense.get("amount", 0.0)
    currency = expense.get("currency")
    if not currency:
        currency = base_currency
    paid_by_user = expense.get("paid_by_user", 0.0)
    borrowed_by_user = expense.get("borrowed_by_user", 0.0)
    date = expense.get("date", "")
    
    # Calculate user's net for this expense
    user_net = paid_by_user - borrowed_by_user
    # Format date
    formatted_date = ""
    if date:
        try:
            from datetime import datetime
            if isinstance(date, str):
                parsed_date = datetime.fromisoformat(date.replace('Z', '+00:00'))
                formatted_date = parsed_date.strftime("%b %d, %Y")
        except:
            formatted_date = str(date)[:10]  # Fallback
    
    # Determine balance display
    balance_class = "expense-positive" if user_net > 0 else "expense-negative" if user_net < 0 else "expense-zero"
    balance_text = f"you lent {currency} {abs(user_net):.2f}" if user_net > 0 else f"you owe {currency} {abs(user_net):.2f}" if user_net < 0 else "settled"
    
    return A(
        Div(
            Div(
                Div(
                    H3(title, cls="expense-title"),
                    P(description, cls="expense-description") if description else None,
                    P(formatted_date, cls="expense-date") if formatted_date else None,
                    cls="expense-info"
                ),
                Div(
                    Div(f"{currency} {amount:.2f}", cls="expense-amount"),
                    Div(balance_text, cls=f"expense-balance {balance_class}"),
                    cls="expense-amounts"
                ),
                cls="expense-content"
            ),
            cls="expense-card-inner"
        ),
        href=f"/group/{group_id}/expense/{expense_id}",
        cls="expense-card"
    )


def expense_summary_card(expense: dict, user_amount: float, group_currency = str):
    """
    Summary card showing total amount and user's balance
    """
    total_amount = expense.get('amount', 0.0)
    original_amount = expense.get('amount_original', 0.0)
    original_currency = expense.get('original_currency')
    if not original_currency:
        original_currency = 'INR'
    exchange_rate = expense.get('exchange_rate', 1.0)
    
    return Div(
        Div(
            H3("Expense Summary", cls="card-title"),
            cls="card-header"
        ),
        
        Div(
            # Total amount
            Div(
                Span("Total Amount", cls="amount-label"),
                Div(
                    Span(f"{group_currency} {total_amount:.2f}", cls="amount-primary"),
                    Span(f"({original_currency} {original_amount:.2f})", cls="amount-secondary") if exchange_rate != 1.0 else None,
                    cls="amount-display"
                ),
                cls="amount-item"
            ),
            
            # Exchange rate (only show if currencies are different)
            Div(
                Span("Exchange Rate", cls="amount-label"),
                Div(
                    Span(f"1 {original_currency} = {exchange_rate:.2f} {group_currency}", cls="exchange-rate-display"),
                    cls="amount-display"
                ),
                cls="amount-item exchange-rate-item"
            ) if original_currency != group_currency else None,
            
            # User's balance
            Div(
                Span("Your Balance", cls="amount-label"),
                Div(
                    Span(
                        f"{original_currency} {abs(user_amount):.2f}",
                        cls=f"amount-primary {'text-success' if user_amount > 0 else 'text-danger' if user_amount < 0 else 'text-muted'}"
                    ),
                    Span(
                        "You are owed" if user_amount > 0 else "You owe" if user_amount < 0 else "Settled",
                        cls="amount-secondary"
                    ),
                    cls="amount-display"
                ),
                cls="amount-item"
            ),
            
            cls="summary-content"
        ),
        
        cls="expense-summary-card card"
    )