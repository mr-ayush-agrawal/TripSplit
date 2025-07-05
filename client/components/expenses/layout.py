from fasthtml.common import *

def expense_header(expense: dict, username: str, group_data: dict):
    """
    Header section with expense title and basic info
    """
    return Div(
        # Back button
        A(
            I(cls="fas fa-arrow-left"),
            " Back to Group",
            href=f"/group/{expense.get('group_id', '')}",
            cls="btn btn-secondary back-button"
        ),
        # Header content with title and actions
        Div(
            H1(group_data.get('group_name', 'Group Name'), cls="expense-title"),
            P(group_data.get('description', ''), cls="expense-description") if expense.get('description') else None,
            cls='expense-header-content',
            style='margin-bottom : 2rem;'
        ),
        Div(
            # Left side - Title and description
            Div(
                H1(expense.get('title', 'Expense Details'), cls="expense-title"),
                P(expense.get('description', ''), cls="expense-description") if expense.get('description') else None,
                cls="expense-header-left"
            ),
            Div(
                # Owner info
                Div(
                    Span("Created by: ", cls="label"),
                    Span(expense.get('expense_owner', 'Unknown'), cls="expense-owner"),
                    cls="expense-meta"
                ),
                expense_actions_buttons(expense, username),
                cls="expense-header-right"
            ),
            cls="expense-header-content"
        ),
        cls="expense-header"
    )


def expense_members_breakdown(expense: dict, group_data: dict):
    """
    Detailed breakdown of each member's involvement
    """
    paid_by = expense.get('paid_by', {})
    borrowed_by = expense.get('borrowed_by', {})
    all_members = group_data.get('members', [])
    
    # Get all users involved in the expense
    involved_users = set(paid_by.keys()) | set(borrowed_by.keys())
    
    return Div(
        Div(
            H3("Member Breakdown", cls="card-title"),
            cls="card-header"
        ),
        
        Div(
            # Table for involved members
            Table(
                Thead(
                    Tr(
                        Th("Member", cls="member-col"),
                        Th("Paid", cls="amount-col"),
                        Th("Borrowed", cls="amount-col"),
                        Th("Net Balance", cls="amount-col"),
                        cls="table-header"
                    )
                ),
                Tbody(
                    *[member_row(member, paid_by, borrowed_by) for member in involved_users]
                ),
                cls="table table-striped members-table"
            ),
            
            # Show non-involved members if any
            non_involved_members(all_members, involved_users),
            
            cls="card-body"
        ),
        
        cls="members-breakdown-card card"
    )


def member_row(member: str, paid_by: dict, borrowed_by: dict):
    """
    Individual member row in the breakdown table
    """
    paid_amount = paid_by.get(member, 0.0)
    borrowed_amount = borrowed_by.get(member, 0.0)
    net_balance = paid_amount - borrowed_amount
    
    return Tr(
        Td(
            Div(
                I(cls="fas fa-user-circle member-icon"),
                Span(member, cls="member-name"),
                cls="member-info"
            ),
            cls="member-cell"
        ),
        Td(
            Span(f"₹{paid_amount:.2f}", cls="amount-paid") if paid_amount > 0 else Span("-", cls="amount-zero"),
            cls="amount-cell"
        ),
        Td(
            Span(f"₹{borrowed_amount:.2f}", cls="amount-borrowed") if borrowed_amount > 0 else Span("-", cls="amount-zero"),
            cls="amount-cell"
        ),
        Td(
            Span(
                f"₹{abs(net_balance):.2f}",
                cls=f"amount-net {'text-success' if net_balance > 0 else 'text-danger' if net_balance < 0 else 'text-muted'}"
            ),
            Span(
                "owes" if net_balance > 0 else "owed" if net_balance < 0 else "settled",
                cls="balance-status"
            ),
            cls="balance-cell"
        ),
        cls="member-row"
    )
def non_involved_members(all_members: list, involved_users: set):
    """
    Show members who weren't involved in the expense
    """
    non_involved = [member for member in all_members if member not in involved_users]
    
    if not non_involved:
        return None
    
    return Div(
        H5("Not Involved", cls="non-involved-title"),
        Div(
            *[
                Span(
                    I(cls="fas fa-user-circle"),
                    member,
                    cls="non-involved-member"
                )
                for member in non_involved
            ],
            cls="non-involved-list"
        ),
        cls="non-involved-section"
    )

def expense_actions_buttons(expense: dict, username: str):
    """
    Action buttons for edit/delete (only for expense owner) - now inline in header
    """
    expense_owner = expense.get('expense_owner', '')
    expense_id = expense.get('expense_id', '')
    group_id = expense.get('group_id', '')
    
    if expense_owner != username:
        return None
    
    return Div(
        A(
            I(cls="fas fa-edit"),
            " Edit",
            href=f"/group/{group_id}/expense/{expense_id}/edit",
            cls="btn btn-primary btn-action-inline"
        ),
        
        Button(
            I(cls="fas fa-trash"),
            " Delete",
            onclick=f"confirmDelete('{expense_id}', '{group_id}')",
            cls="btn btn-danger btn-action-inline"
        ),
        
        cls="expense-actions-inline"
    )