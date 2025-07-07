from fasthtml.common import *
from client.components.group.cards import group_card

def groups_grid(user_groups):
    """Grid layout for groups - full width layout"""
    if not user_groups:
        return empty_groups_state()
    
    # Create list of group cards
    cards = []
    for group in user_groups:
        cards.append(
            group_card(
                group_id=group["group_id"],
                name=group["name"],
                balance=group["balance"],
                member_count = group["members_count"]
            )
        )
    
    return Div(*cards, style="width: 100%; display: flex; flex-direction: column; gap: 1rem;")

def empty_groups_state():
    """Empty state when user has no groups"""
    return Section(
        Div(
            H2("No Groups Yet", style="text-align: center; color: var(--muted-color);"),
            P("Create your first group to start splitting expenses with friends", 
              style="text-align: center; color: var(--muted-color); margin-bottom: 2rem;"),
            A("Create Your First Group", href="/groups/create", role="button", style="display: block; max-width: 300px; margin: 0 auto;"),
            style="text-align: center; padding: 4rem 2rem;"
        )
    )

def groups_header(total_groups, total_balance):
    """Header section with stats and create button side by side"""
    # balance_color = "var(--color)" if total_balance >= 0 else "var(--del-color)"
    balance_color = "#0A9548" if total_balance >= 0 else "#e74c3c"
    balance_text = f"₹{total_balance:.2f}" if total_balance >= 0 else f"-₹{abs(total_balance):.2f}"
    
    return Section(
        Div(
            H1("My Groups", style="text-align: center; margin-bottom: 2rem;"),
            
            # Main row for stats + create group
            Div(
                Div(
                    Article(
                        Div( 
                            Div(
                                H3(str(total_groups), style="text-align: center; color: var(--primary); margin: 0; font-size: 2rem;"),
                                P("Total Groups", style="text-align: center; color: var(--muted-color); margin: 0.5rem 0 0 0;"),
                                cls="col-md-6"
                            ),
                            Div(
                                H3(balance_text, style=f"text-align: center; color: {balance_color}; margin: 0; font-size: 2rem;"),
                                P("Overall Balance", style="text-align: center; color: var(--muted-color); margin: 0.5rem 0 0 0;"),
                                cls="col-md-6"
                            ),
                            cls="row"
                        ),
                        style="padding: 1.5rem; height: 100%; margin : auto;"
                    ),
                    style='width : 66%; align: left; padding-right: 0.5rem; '
                ),
                Div(  
                    Article(
                        Div(
                            H3("➕ Create New Group", style="text-align: center; margin-bottom: 1rem; color: var(--primary);"),
                            P("Start splitting expenses with friends", style="text-align: center; color: var(--muted-color); margin-bottom: 1rem;"),
                            A("Create Group", href="/group/create", role="button", style="width: 100%; background: var(--primary);"),
                            style="text-align: center;"
                        ),
                        style="padding: 1.5rem; border: 2px dashed var(--primary); transition: all 0.2s ease; height:100%;"
                    ),
                    style='width : 33%; align: right; padding-left : 0.5rem;'
                ),
                cls="row", 
                style="width: 100%;"
            ),
            style="margin-bottom: 2rem;"
        ),
        style="width: 100%;" 
    )

def simplified_debts_header(group_data, group_id):
    """Header section for simplified debts page"""
    return Div(
        A(Button("← Back to Group", onclick=f"window.location.href='/group/{group_id}'", cls="back-btn")),  
        Div(
            H1(f"{group_data.get('group_name', 'Group')} - Simplified Debts"),
            cls="header-title"
        ),
        cls="simplified-debts-header"
    )
