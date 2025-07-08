from fasthtml.common import *

from client.components.expenses.layout import edit_expense_header
from client.components.expenses.edit import edit_expense_form, success_popup, error_popup
from client.components.expenses.add import expense_form, success_popup, error_popup
from client.components.user.layout import dashboard_layout
from client.static.expense.add_script import add_expense_javascript
from client.static.expense.edit_script import expense_edit_initialization_script

def edit_expense_page(username, group_data, expense_data, group_id: str, expense_id: str):
    if not group_data:
        group_data = {}
    
    members = group_data.get("members", [])
    base_currency = group_data.get("base_currency", "INR")
    
    content = Div(
        edit_expense_header(group_id, expense_id),
        Div(
            edit_expense_form(members, base_currency, expense_data, group_id, expense_id),
            cls="form-container"
        ),
        expense_edit_initialization_script(expense_data),
        success_popup(),
        error_popup(),
        add_expense_javascript(),
        cls="add-expense-container"
    )
    
    return dashboard_layout(
        title=f"Edit Expense - {expense_data.get('title', 'Expense')}",
        content=content,
        username=username
    )
