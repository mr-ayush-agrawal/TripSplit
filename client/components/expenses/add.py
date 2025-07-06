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

def basic_expense_fields(base_currency):
    """Basic expense information fields with two properly structured rows"""
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
                    placeholder="Enter expense title"
                ),
                cls="form-group"
            ),
            Div(
                Label("Description", for_="description"),
                Input(
                    id="description",
                    name="description",
                    placeholder="Enter expense description (optional)",
                    rows="3"
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
                    oninput="updateAmountDisplay()"
                ),
                cls="form-group"
            ),
            Div(
                Label("Currency", for_="currency"),
                Div(
                    Select(
                        Option(base_currency, value=base_currency, selected=True),
                        Option("USD", value="USD"),
                        Option("EUR", value="EUR"),
                        Option("GBP", value="GBP"),
                        Option("INR", value="INR"),
                        Option("JPY", value="JPY"),
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
                    value="1",
                    placeholder="1.00"
                ),
                Small(f"Rate to convert to {base_currency}", cls="help-text"),
                cls="form-group exchange-rate-group hidden"
            ),
            cls="form-row"
        ),
        cls="form-col"
    )

def paid_by_section(members):
    """Paid by section with single/multiple toggle"""
    return Div(
        H3("Paid By"),
        Div(
            Button("Single Payer", type="button", id="single-payer-btn", onclick="togglePaidByMode('single')", cls="mode-btn active"),
            Button("Multiple Payers", type="button", id="multiple-payers-btn", onclick="togglePaidByMode('multiple')", cls="mode-btn"),
            cls="mode-toggle"
        ),
        Div(
            Div(
                Label("Select who paid:", for_="single-payer"),
                Select(*[Option(member, value=member) for member in members], id="single-payer", name="single-payer", onchange="updatePaidBy()"),
                id="single-payer-section",
                cls="payer-section"
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
                                value="0",
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
                cls="payer-section hidden"
            ),
            cls="paid-by-content"
        ),
        cls="paid-by-section"
    )
def split_by_section(members):
    """Split by section with different splitting options"""
    return Div(
        H3("Split By"),
        Div(
            Button("Equally", type="button", onclick="setSplitMode('equally')", cls="split-btn active"),
            Button("Unequally", type="button", onclick="setSplitMode('unequally')", cls="split-btn"),
            Button("By Shares", type="button", onclick="setSplitMode('shares')", cls="split-btn"),
            Button("By Percentage", type="button", onclick="setSplitMode('percentage')", cls="split-btn"),
            cls="split-mode-toggle"
        ),
        # Equally split section
        Div(
            Label("Select who should split the expense:"),
            Div(
                *[
                    Div(
                        Input(type="checkbox", id=f"equal-{member}", value=member, checked=True, onchange="updateEqualSplit()"),
                        Label(member, for_=f"equal-{member}"),
                        cls="checkbox-item"
                    ) for member in members
                ],
                cls="checkbox-group"
            ),
            id="equally-section",
            cls="split-section"
        ),
        # Unequally
        Div(
            Label("Enter exact amount for each member:"),
            Div(
                *[
                    Div(
                        Label(member, for_=f"unequal-{member}"),
                        Input(type="number", id=f"unequal-{member}", step="0.01", min="0", value="0", placeholder="0.00", oninput="updateUnequalSplit()"),
                        cls="member-input"
                    ) for member in members
                ],
                cls="member-inputs"
            ),
            Div(
                Small("Total: ", cls="total-label"),
                Span("0.00", id="unequal-total", cls="total-value"),
                cls="total-display"
            ),
            id="unequally-section",
            cls="split-section hidden"
        ),
        # Shares
        Div(
            Label("Enter shares for each member:"),
            Div(
                *[
                    Div(
                        Label(member, for_=f"share-{member}"),
                        Input(type="number", id=f"share-{member}", min="0", value="1", placeholder="1", oninput="updateShareSplit()"),
                        cls="member-input"
                    ) for member in members
                ],
                cls="member-inputs"
            ),
            Div(
                Small("Total Shares: ", cls="total-label"),
                Span("0", id="share-total", cls="total-value"),
                cls="total-display"
            ),
            id="shares-section",
            cls="split-section hidden"
        ),
        # Percentage
        Div(
            Label("Enter percentage for each member:"),
            Div(
                *[
                    Div(
                        Label(member, for_=f"percent-{member}"),
                        Input(type="number", id=f"percent-{member}", step="0.01", min="0", max="100", value="0", placeholder="0.00", oninput="updatePercentageSplit()"),
                        Span("%", cls="percent-symbol"),
                        cls="member-input percent-input"
                    ) for member in members
                ],
                cls="member-inputs"
            ),
            Div(
                Small("Total: ", cls="total-label"),
                Span("0.00%", id="percentage-total", cls="total-value"),
                cls="total-display"
            ),
            id="percentage-section",
            cls="split-section hidden"
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
