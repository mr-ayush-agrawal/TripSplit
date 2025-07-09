from fasthtml.common import Div

from client.components.expenses.card import expense_summary_card
from client.components.expenses.layout import (
    expense_members_breakdown, expense_header, 
)

def expense_detail_page(group_id, expense_id, username: str, expense_data: dict, group_data: dict, user_amount: float):
    """
    Main expense detail page component
    """
    expense = expense_data  # expense_data is already the expense object
    group_currency = group_data.get('base_currency', 'INR')
    
    return Div(
        expense_header(group_id, expense_id, expense, username, group_data),
        expense_summary_card(expense, user_amount, group_currency),
        expense_members_breakdown(expense, group_data),
        cls="expense-detail-container"
    )