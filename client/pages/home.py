from fasthtml.common import *
from client.components.home.layout import home_base_layout, hero_section
from client.components.home.cards import feature_card

def home_page():
    content = Div(
        hero_section(),
        Section(
            H2("Features", style="text-align: center; margin: 3rem 0 2rem 0;", id="features"),
            Div(
                feature_card("👥", "Create Groups", "Organize expenses by creating groups for trips, roommates, or any shared activity."),
                feature_card("💰", "Track Expenses", "Add expenses and split them equally or customize who owes what."),
                feature_card("⚖️", "Settle Up", "See who owes what and settle debts with minimal transactions."),
                cls="grid",
                style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 2rem 0;"
            )
        )
    )
    return home_base_layout("Home", content)