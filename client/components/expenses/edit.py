from fasthtml.common import *
from client.components.expenses.add import basic_expense_fields, paid_by_section, split_by_section

def edit_expense_form(members, base_currency, expense_data, group_id: str, expense_id: str):
    print(expense_data)
    return Form(
        Div(
            Div(
                basic_expense_fields(base_currency, expense_data),
                cls="expense-basic"
            ),
            Div(
                Div(paid_by_section(members, expense_data), cls="expense-paid-by"),
                Div(split_by_section(members, expense_data), cls="expense-split-by"),
                cls="form-split-row"
            ),
            Div(
                Button("Update Expense", type="submit", cls="submit-btn"),
                Button("Cancel", type="button", onclick=f"window.location.href='/group/{group_id}/expense/{expense_id}'", cls="cancel-btn"),
                cls="form-actions"
            ),
            cls="form-content"
        ),
        method="post",
        action=f"/group/{group_id}/expense/{expense_id}/edit",
        onsubmit="return validateAndSubmitForm(event)",
        cls="expense-form"
    )


def edit_paid_by_member(member_name, amount, all_members):
    """Create a pre-filled paid by member row"""
    return Div(
        Select(
            *[Option(member, value=member, selected=(member == member_name)) 
              for member in all_members],
            cls="form-select member-select",
            onchange="updatePaidByData()"
        ),
        Input(
            type="number",
            cls="form-input amount-input",
            placeholder="Amount",
            step="0.01",
            min="0",
            value=str(amount),
            onchange="updatePaidByData()"
        ),
        Button(
            I(cls="fas fa-trash"),
            type="button",
            cls="btn btn-danger remove-btn",
            onclick="removePaidByMember(this)"
        ),
        cls="member-input-group"
    )
def edit_borrowed_by_member(member_name, amount, all_members):
    """Create a pre-filled borrowed by member row"""
    return Div(
        Select(
            *[Option(member, value=member, selected=(member == member_name)) 
              for member in all_members],
            cls="form-select member-select",
            onchange="updateBorrowedByData()"
        ),
        Input(
            type="number",
            cls="form-input amount-input",
            placeholder="Amount",
            step="0.01",
            min="0",
            value=str(amount),
            onchange="updateBorrowedByData()"
        ),
        Button(
            I(cls="fas fa-trash"),
            type="button",
            cls="btn btn-danger remove-btn",
            onclick="removeBorrowedByMember(this)"
        ),
        cls="member-input-group"
    )

def success_popup():
    """Success popup component"""
    return Div(
        Div(
            I(cls="fas fa-check-circle"),
            P("Expense updated successfully!"),
            cls="popup-content success"
        ),
        id="success-popup",
        cls="popup-overlay hidden"
    )
def error_popup():
    """Error popup component"""
    return Div(
        Div(
            I(cls="fas fa-exclamation-circle"),
            P("Error updating expense. Please try again."),
            cls="popup-content error"
        ),
        id="error-popup",
        cls="popup-overlay hidden"
    )