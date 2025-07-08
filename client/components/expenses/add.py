from fasthtml.common import *

def expense_form(members, base_currency):
    """Main expense form with proper layout"""
    return Form(
        Div(
            # Basic expense info (full width)
            Div(
                basic_expense_fields(base_currency),
                cls="expense-basic"
            ),
            # Paid by (left) and Split by (right) side-by-side
            Div(
                Div(paid_by_section(members), cls="expense-paid-by"),
                Div(split_by_section(members), cls="expense-split-by"),
                cls="form-split-row"
            ),
            # Submit and Cancel buttons
            Div(
                Button("Add Expense", type="submit", cls="submit-btn"),
                Button("Cancel", type="button", onclick="window.location.href = document.referrer || '/group/'", cls="cancel-btn"),
                cls="form-actions"
            ),
            cls="form-content"
        ),
        method="post",
        onsubmit="return validateAndSubmitForm(event)",
        cls="expense-form"
    )

def basic_expense_fields(base_currency, expense_data : dict = {}):
    """Basic expense information fields with two properly structured rows"""
    exp_curr = expense_data.get('original_currency')
    if not exp_curr:
        exp_curr = base_currency
    print(exp_curr)
    curr_set = {base_currency, exp_curr, 'INR', 'JPY', 'EUR', 'GBP', 'USD', 'AED'}
    return Div(
        H3("Expense Details"),
        # Row 1: Title and Description
        Div(
            Div(
                Label("Title *", for_="title"),
                Input(
                    type="text",
                    id="title",
                    name="title",
                    required=True,
                    placeholder="Enter expense title",
                    value=expense_data.get("title", "")
                ),
                cls="form-group"
            ),
            Div(
                Label("Description", for_="description"),
                Input(
                    id="description",
                    name="description",
                    placeholder="Enter expense description (optional)",
                    value=expense_data.get("description", "")
                ),
                cls="form-group"
            ),
            cls="form-row"
        ),

        # Row 2: Amount, Currency, Exchange Rate
        Div(
            Div(
                Label("Amount *", for_="amount"),
                Input(
                    type="number",
                    id="amount",
                    name="amount",
                    step="0.01",
                    min="0",
                    required=True,
                    placeholder="0.00",
                    oninput="updateAmountDisplay()",
                    value=expense_data.get("amount_original", "")
                ),
                cls="form-group"
            ),
            Div(
                Label("Currency", for_="currency"),
                Div(
                    Select(
                        *[Option(curr, value = curr, selected=(curr == exp_curr)) for curr in curr_set],
                        id="currency",
                        name="currency",
                        onchange="toggleExchangeRate()"
                    ),
                    cls="select-group"
                ),
                cls="form-group"
            ),
            Div(
                Label("Exchange Rate", for_="exchange_rate"),
                Input(
                    type="number",
                    id="exchange_rate",
                    name="exchange_rate",
                    step="0.01",
                    min="0",
                    # value="1",
                    placeholder="1.00",
                    value=expense_data.get("exchange_rate", "1")
                ),
                Small(f"Rate to convert to {base_currency}", cls="help-text"),
                cls="form-group exchange-rate-group" + ("" if exp_curr != base_currency else " hidden")
            ),
            cls="form-row"
        ),
        cls="form-col"
    )


def paid_by_section(members, expense_data: dict = {}):
    """Paid by section with single/multiple toggle"""
    paid_by_data = expense_data.get("paid_by_original", {})
    non_zero_payers = {k: v for k, v in paid_by_data.items() if v > 0}
    is_single_payer = len(non_zero_payers) == 1
    single_payer_name = list(non_zero_payers.keys())[0] if is_single_payer else members[0]

    return Div(
        H3("Paid By"),
        Div(
            Button(
                "Single Payer", 
                type="button", 
                id="single-payer-btn", 
                onclick="togglePaidByMode('single')", 
                cls="mode-btn" + (" active" if is_single_payer else "")
            ),
            Button(
                "Multiple Payers", 
                type="button", 
                id="multiple-payers-btn", 
                onclick="togglePaidByMode('multiple')", 
                cls="mode-btn" + (" active" if not is_single_payer else "")
            ),
            cls="mode-toggle"
        ),
        Div(
            Div(
                Label("Select who paid:", for_="single-payer"),
                Select(
                    *[Option(member, value=member, selected=(member == single_payer_name)) for member in members], 
                    id="single-payer", 
                    name="single-payer", 
                    onchange="updatePaidBy()"
                ),
                id="single-payer-section",
                cls="payer-section" + ("" if is_single_payer else " hidden")
            ),
            Div(
                Label("Enter amount paid by each member:"),
                Div(
                    *[
                        Div(
                            Label(member, for_=f"paid-{member}"),
                            Input(
                                type="number",
                                id=f"paid-{member}",
                                step="0.01",
                                min="0",
                                value=str(paid_by_data.get(member, 0)),
                                placeholder="0.00",
                                oninput="updatePaidBy()",
                                cls="form-group-input"
                            ),
                            cls="member-input"
                        ) for member in members
                    ],
                    cls="member-inputs"
                ),
                id="multiple-payers-section",
                cls="payer-section" + (" hidden" if is_single_payer else "")
            ),
            cls="paid-by-content"
        ),
        cls="paid-by-section"
    )

def split_by_section(members, expense_data: dict = {}):
    """Split by section with different splitting options and pre-populated data"""
    borrowed_by_data = expense_data.get("borrowed_by_original", {})
    
    # Determine the split mode based on existing data
    non_zero_borrowers = {k: v for k, v in borrowed_by_data.items() if v > 0}
    total_borrowed = sum(borrowed_by_data.values())
    
    # Determine split mode
    split_mode = "equally"  # default
    
    if len(non_zero_borrowers) > 0:
        # Check if it's equal split
        if len(non_zero_borrowers) > 1:
            equal_amount = total_borrowed / len(non_zero_borrowers)
            is_equal = all(abs(v - equal_amount) < 0.01 for v in non_zero_borrowers.values())
            if is_equal:
                split_mode = "equally"
            else:
                # Check if it's percentage based (all values sum to 100 or close)
                if abs(total_borrowed - 100) < 0.01:
                    split_mode = "percentage"
                else:
                    split_mode = "unequally"
        else:
            split_mode = "unequally"
    
    return Div(
        H3("Split By"),
        Div(
            Button(
                "Equally", 
                type="button", 
                onclick="setSplitMode('equally')", 
                cls="split-btn" + (" active" if split_mode == "equally" else "")
            ),
            Button(
                "Unequally", 
                type="button", 
                onclick="setSplitMode('unequally')", 
                cls="split-btn" + (" active" if split_mode == "unequally" else "")
            ),
            Button(
                "By Shares", 
                type="button", 
                onclick="setSplitMode('shares')", 
                cls="split-btn" + (" active" if split_mode == "shares" else "")
            ),
            Button(
                "By Percentage", 
                type="button", 
                onclick="setSplitMode('percentage')", 
                cls="split-btn" + (" active" if split_mode == "percentage" else "")
            ),
            cls="split-mode-toggle"
        ),
        # Equally split section
        Div(
            Label("Select who should split the expense:"),
            Div(
                *[
                    Div(
                        Input(
                            type="checkbox", 
                            id=f"equal-{member}", 
                            value=member, 
                            checked=(borrowed_by_data.get(member, 0) > 0 if split_mode == "equally" else True), 
                            onchange="updateEqualSplit()"
                        ),
                        Label(member, for_=f"equal-{member}"),
                        cls="checkbox-item"
                    ) for member in members
                ],
                cls="checkbox-group"
            ),
            id="equally-section",
            cls="split-section" + ("" if split_mode == "equally" else " hidden")
        ),
        # Unequally
        Div(
            Label("Enter exact amount for each member:"),
            Div(
                *[
                    Div(
                        Label(member, for_=f"unequal-{member}"),
                        Input(
                            type="number", 
                            id=f"unequal-{member}", 
                            step="0.01", 
                            min="0", 
                            value=str(borrowed_by_data.get(member, 0) if split_mode == "unequally" else 0), 
                            placeholder="0.00", 
                            oninput="updateUnequalSplit()"
                        ),
                        cls="member-input"
                    ) for member in members
                ],
                cls="member-inputs"
            ),
            Div(
                Small("Total: ", cls="total-label"),
                Span(str(total_borrowed if split_mode == "unequally" else "0.00"), id="unequal-total", cls="total-value"),
                cls="total-display"
            ),
            id="unequally-section",
            cls="split-section" + ("" if split_mode == "unequally" else " hidden")
        ),
        # Shares
        Div(
            Label("Enter shares for each member:"),
            Div(
                *[
                    Div(
                        Label(member, for_=f"share-{member}"),
                        Input(
                            type="number", 
                            id=f"share-{member}", 
                            min="0", 
                            value=str(int(borrowed_by_data.get(member, 1)) if split_mode == "shares" else 1), 
                            placeholder="1", 
                            oninput="updateShareSplit()"
                        ),
                        cls="member-input"
                    ) for member in members
                ],
                cls="member-inputs"
            ),
            Div(
                Small("Total Shares: ", cls="total-label"),
                Span(str(sum(int(borrowed_by_data.get(member, 1)) for member in members) if split_mode == "shares" else len(members)), id="share-total", cls="total-value"),
                cls="total-display"
            ),
            id="shares-section",
            cls="split-section" + ("" if split_mode == "shares" else " hidden")
        ),
        # Percentage
        Div(
            Label("Enter percentage for each member:"),
            Div(
                *[
                    Div(
                        Label(member, for_=f"percent-{member}"),
                        Input(
                            type="number", 
                            id=f"percent-{member}", 
                            step="0.01", 
                            min="0", 
                            max="100", 
                            value=str(borrowed_by_data.get(member, 0) if split_mode == "percentage" else 0), 
                            placeholder="0.00", 
                            oninput="updatePercentageSplit()"
                        ),
                        Span("%", cls="percent-symbol"),
                        cls="member-input percent-input"
                    ) for member in members
                ],
                cls="member-inputs"
            ),
            Div(
                Small("Total: ", cls="total-label"),
                Span(f"{total_borrowed}%" if split_mode == "percentage" else "0.00%", id="percentage-total", cls="total-value"),
                cls="total-display"
            ),
            id="percentage-section",
            cls="split-section" + ("" if split_mode == "percentage" else " hidden")
        ),
        Input(type="hidden", id="paid_by", name="paid_by", value="{}"),
        Input(type="hidden", id="borrowed_by", name="borrowed_by", value="{}"),
        cls="split-by-section"
    )


def success_popup():
    """Success popup modal"""
    return Div(
        Div(
            Div(
                H3("Success!"),
                P("Expense has been added successfully."),
                Button(
                    "OK",
                    onclick="closeSuccessPopup()",
                    cls="popup-btn"
                ),
                cls="popup-content"
            ),
            cls="popup-modal"
        ),
        id="success-popup",
        cls="popup-overlay hidden"
    )
def error_popup():
    """Error popup modal"""
    return Div(
        Div(
            Div(
                H3("Error"),
                P("", id="error-message"),
                Button(
                    "OK",
                    onclick="closeErrorPopup()",
                    cls="popup-btn"
                ),
                cls="popup-content"
            ),
            cls="popup-modal"
        ),
        id="error-popup",
        cls="popup-overlay hidden"
    )
