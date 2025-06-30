from fasthtml.common import *

def dashboard_card(title, description, href, icon="📊", button_text="Go"):
    """Reusable dashboard card component"""
    return Article(
        Header(
            H3(
                Span(icon, style="font-size: 2rem; margin-right: 0.5rem;"),
                title,
                style="text-align: center; margin-bottom: 1rem;"
            )
        ),
        P(description, style="text-align: center; margin-bottom: 2rem; color: var(--muted-color);"),
        Footer(
            A(button_text, href=href, role="button", style="width: 100%;"),
            style="text-align: center;"
        ),
        style="height: 100%; display: flex; flex-direction: column; justify-content: space-between;",
        onmouseover="this.style.transform='translateY(-7px)'; this.style.boxShadow='0 8px 20px rgba(0,0,0,0.15)';",
        onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='';"
    )

def action_cards():
    """Main action cards for the dashboard"""
    return Section(
        H2("Quick Actions", style="text-align: center; margin-bottom: 2rem;"),
        Div(
            Div(
                dashboard_card(
                    title="My Groups",
                    description="View and manage all your expense groups. See balances, recent activities, and group members.",
                    href="/group",
                    icon="👥",
                    button_text="View Groups"
                ),
                cls="col-md-6"
            ),
            Div(
                dashboard_card(
                    title="Create Group",
                    description="Start a new expense group with friends, roommates, or colleagues. Split bills easily.",
                    href="/group/create-group",
                    icon="➕",
                    button_text="Create Group"
                ),
                cls="col-md-6"
            ),
            cls="row"
        ),
        style="margin: 3rem 0;"
    )

