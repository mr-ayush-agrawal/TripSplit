from fasthtml.common import *

def debts_summary_section(payments, base_currency, current_user):
    """Summary of user's debts and receivables"""
    user_owes = []
    user_receives = []
    
    # Calculate what current user owes
    for payer, payment_list in payments.items():
        if payer == current_user:
            for receiver, amount in payment_list:
                user_owes.append({"to": receiver, "amount": amount})
    
    # Calculate what current user receives
    for payer, payment_list in payments.items():
        for receiver, amount in payment_list:
            if receiver == current_user:
                user_receives.append({"from": payer, "amount": amount})
    
    total_owes = sum(item["amount"] for item in user_owes)
    total_receives = sum(item["amount"] for item in user_receives)
    
    # Calculate net balance and settlement count
    net_balance = total_receives - total_owes
    settlement_count = len(user_owes) + len(user_receives)
    
    return Div(
        H2("Your Summary"),
        Div(
            Div(
                # Net balance card
                Div(
                    H3(f"{base_currency} {abs(net_balance):.2f}"),
                    P("You are owed" if net_balance > 0 else "You owe" if net_balance < 0 else "You're settled"),
                    cls=f"summary-card {'receive-card' if net_balance > 0 else 'owe-card' if net_balance < 0 else 'settled-card'}"
                ),
                # Settlement count card
                Div(
                    H3(str(settlement_count)),
                    P("Settlements remaining"),
                    cls="summary-card count-card"
                ),
                cls="summary-cards"
            ),
            cls="summary-content"
        ),
        cls="summary-section"
    )

def payments_section(payments, base_currency, current_user, group_id):
    """Section showing all payments to be made"""
    if not payments:
        return Div(
            H2("Payments"),
            Div(
                P("🎉 All debts are settled! No payments needed."),
                cls="no-payments"
            ),
            cls="payments-section"
        )
    
    payment_items = []
    
    for payer, payment_list in payments.items():
        for receiver, amount in payment_list:
            # Check if current user is involved in this payment
            user_involved = payer == current_user or receiver == current_user
            
            payment_item = create_payment_item(
                payer, receiver, amount, base_currency, 
                user_involved, current_user, group_id
            )
            payment_items.append(payment_item)
    
    return Div(
        H2("Payments to be made"),
        Div(
            *payment_items,
            cls="payments-list"
        ),
        cls="payments-section"
    )

def create_payment_item(payer, receiver, amount, currency, user_involved, current_user, group_id):
    """Create individual payment item"""
    # Determine the action for current user
    action_button = None
    if payer == current_user:
        action_button = Form(
            Input(type="hidden", name="paid_by", value=payer),
            Input(type="hidden", name="paid_to", value=receiver),
            Input(type="hidden", name="amount", value=str(amount)),
            Button(
                "Mark as Paid",
                type="submit",
                cls="settle-button pay-button"
            ),
            method="POST",
            action=f"/group/{group_id}/settle"
        )
    elif receiver == current_user:
        action_button = Form(
            Input(type="hidden", name="paid_by", value=payer),
            Input(type="hidden", name="paid_to", value=receiver),
            Input(type="hidden", name="amount", value=str(amount)),
            Button(
                "Mark as Received",
                type="submit", 
                cls="settle-button receive-button"
            ),
            method="POST",
            action=f"/group/{group_id}/settle"
        )
    
    return Div(
        Div(
            Div(
                Div(
                    Strong(payer),
                    Span(" owes "),
                    Strong(receiver),
                    cls="payment-parties"
                ),
                Div(
                    Span(f"{currency} {amount:.2f}", cls="payment-amount"),
                    cls="payment-details"
                ),
                cls="payment-info"
            ),
            action_button if action_button else Div(cls="payment-spacer"),
            cls="payment-content"
        ),
        cls=f"payment-item {'user-involved' if user_involved else ''}",
        id=f"payment-{payer}-{receiver}"
    )

