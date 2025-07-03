from fasthtml.common import *

def create_group_form(error_message=None):
    """Form for creating a new group"""
    error_div = ""
    if error_message:
        error_div = Div(
            P(error_message, style="color: var(--del-color); text-align: center; margin-bottom: 1rem;"),
            role="alert"
        )

    return Form(
        error_div,
        
        # Group Name
        Div(
            Label("Group Name", For="group_name"),
            Input(
                type="text",
                name="group_name",
                id="group_name",
                placeholder="Enter group name (e.g., 'Roommates', 'Trip to Goa')",
                required=True,
                maxlength="100"
            ),
            style="margin-bottom: 1rem;"
        ),
        
        # Group Description  
        Div(
            Label("Description (Optional)", For="group_description"),
            Textarea(
                name="group_description",
                id="group_description",
                placeholder="Brief description of this group",
                rows="3",
                maxlength="500"
            ),
            style="margin-bottom: 1rem;"
        ),
        
        # Base Currency
        Div(
            Label("Base Currency", For="base_currency"),
            Select(
                Option("INR - Indian Rupee", value="INR", selected=True),
                Option("USD - US Dollar", value="USD"),
                Option("EUR - Euro", value="EUR"),
                Option("GBP - British Pound", value="GBP"),
                Option("CAD - Canadian Dollar", value="CAD"),
                Option("AUD - Australian Dollar", value="AUD"),
                name="base_currency",
                id="base_currency"
            ),
            style="margin-bottom: 2rem;"
        ),
        
        # Submit Button
        Div(
            Button("Create Group", type="submit", style="width: 100%; background: var(--primary);"),
            style="text-align: center;"
        ),
        
        method="POST",
        action="/group/create",
        style="max-width: 825px; margin: 0 auto; padding: 2rem; background: var(--card-background-color); border-radius: 0.5rem; box-shadow: 0 2px 10px rgba(0,0,0,0.1); border: 1px solid var(--card-border-color);"
    )



def group_creation_steps():
    """Steps indicator for group creation process"""
    return Section(
        Div(
            H3("Create New Group", style="text-align: center; margin-bottom: 2rem;"),
            Div(
                Div(
                    Div("1", style="background: var(--primary); color: white; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; margin: 0 auto 0.5rem;"),
                    Small("Group Details", style="text-align: center; display: block; color: var(--primary);"),
                    cls="col-md-4"
                ),
                Div(
                    Div("2", style="background: var(--muted-color); color: white; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; margin: 0 auto 0.5rem;"),
                    Small("Add Members", style="text-align: center; display: block; color: var(--muted-color);"),
                    cls="col-md-4"
                ),
                Div(
                    Div("3", style="background: var(--muted-color); color: white; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; margin: 0 auto 0.5rem;"),
                    Small("Start Splitting", style="text-align: center; display: block; color: var(--muted-color);"),
                    cls="col-md-4"
                ),
                cls="row"
            ),
            style="margin-bottom: 3rem;"
        )
    )

def create_group_info():
    """Information section for create group page"""
    return Section(
        Div(
            H2("Getting Started", style="text-align: center; margin-bottom: 2rem;"),
            Div(
                Div(
                    H4("📝 Step 1: Group Details"),
                    P("Give your group a name and description. Choose the currency you'll be using for expenses."),
                    cls="col-md-4"
                ),
                Div(
                    H4("👥 Step 2: Add Members"),
                    P("Invite friends by their username or email. You can add members later too."),
                    cls="col-md-4"
                ),
                Div(
                    H4("💰 Step 3: Start Splitting"),
                    P("Add expenses and split them among group members. Keep track of who owes what."),
                    cls="col-md-4"
                ),
                cls="row"
            ),
            style="background: var(--card-background-color); padding: 2rem; border-radius: 0.5rem; margin-bottom: 1rem; border: 1px solid var(--card-border-color);"
        )
    )
