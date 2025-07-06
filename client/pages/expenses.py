from fasthtml.common import *
from client.components.expenses.layout import add_expense_header
from client.components.expenses.add import expense_form, success_popup, error_popup
from client.components.user.layout import dashboard_layout
from client.static.expense.add_script import add_expense_javascript

def add_expense_page(username, group_data, group_id: str):
    """Add expense page layout"""
    if not group_data:
        group_data = {}
    
    members = group_data.get("members", [])
    base_currency = group_data.get("base_currency", "USD")
    
    content = Div(
        add_expense_header(group_data, group_id),
        Div(
            expense_form(members, base_currency),
            cls="form-container"
        ),
        success_popup(),
        error_popup(),
        add_expense_javascript(),
        cls="add-expense-container"
    )
    
    return dashboard_layout(
        title=f"Add Expense - {group_data.get('group_name', 'Group')}",
        content=content,
        username=username
    )
