from fasthtml.common import *

def create_expense_card(expense, group_id, base_currency):
    """Create individual expense card"""
    print(type(expense), expense)
    expense_id = expense.get("expense_id", "")
    title = expense.get("title", "Untitled Expense")
    description = expense.get("description", "")
    amount = expense.get("amount", 0.0)
    currency = expense.get("currency", base_currency)
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
    balance_text = f"you lent {abs(user_net):.2f}" if user_net > 0 else f"you owe {abs(user_net):.2f}" if user_net < 0 else "settled"
    
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
        href=f"/group/{group_id}/{expense_id}",
        cls="expense-card"
    )