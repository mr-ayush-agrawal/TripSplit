from fasthtml.common import *
from client.components.user.layout import dashboard_layout
from client.components.group.layout import simplified_debts_header
from client.components.group.simplify_debts import debts_summary_section, payments_section

def simplified_debts_page(username="User", group_data=None, debts_data=None, group_id=""):
    """Simplified debts page layout"""
    if not group_data:
        group_data = {}
    if not debts_data:
        debts_data = {}
    
    payments = debts_data.get("data", {})
    base_currency = debts_data.get("base_currency", "INR")
    
    content = Div(
        # Header
        simplified_debts_header(group_data, group_id),
        
        # Main content
        Div(
            # Summary section
            debts_summary_section(payments, base_currency, username),
            
            # Payments section
            payments_section(payments, base_currency, username, group_id),
            
            cls="simplified-debts-content"
        ),
        
        cls="simplified-debts-container"
    )
    
    return dashboard_layout(
        title=f"{group_data.get('group_name', 'Group')} - Simplified Debts",
        content=content,
        username=username
    )
