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

def profile_info_card(title, fields, edit_button_id, edit_modal_id):
    """Reusable profile information card"""
    field_elements = []
    for label, value in fields.items():
        field_elements.append(
            Div(
                Strong(f"{label}:"),
                Span(value, style="margin-left: 0.5rem; color: var(--muted-color);"),
                style="margin-bottom: 1rem; display: flex; justify-content: space-between; align-items: center;"
            )
        )
    
    return Article(
        Header(
            H3(title, style="margin-bottom: 0;"),
            Button("Edit", 
                   cls="outline", 
                   onclick=f"document.getElementById('{edit_modal_id}').style.display='block'",
                   style="padding: 0.25rem 0.75rem; font-size: 0.875rem;"),
            style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;"
        ),
        Div(*field_elements),
        style="margin-bottom: 2rem;"
    )

def profile_stats_card(total_groups=0):
    """Profile statistics card"""
    return Article(
        Header(
            H3("Statistics", style="text-align: center; margin-bottom: 1.5rem;")
        ),
        Div(
            Div(
                H4(str(total_groups), style="font-size: 2.5rem; text-align: center; margin: 0; color: var(--primary);"),
                P("Groups Joined", style="text-align: center; margin: 0.5rem 0 0 0; color: var(--muted-color);"),
                style="text-align: center;"
            ),
            # Placeholder for future stats
            style="padding: 1rem;"
        ),
        style="margin-bottom: 2rem;"
    )


def password_change_card():
    """Password change card"""
    return Article(
        Header(
            H3("Security", style="margin-bottom: 0;"),
            Button("Change Password", 
                   cls="outline", 
                   onclick="document.getElementById('password-modal').style.display='block'",
                   style="padding: 0.25rem 0.75rem; font-size: 0.875rem; background: var(--del-color, #d32f2f); color: white; border-color: var(--del-color, #d32f2f);"),
            style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1.5rem;"
        ),
        P("Keep your account secure by regularly updating your password.", 
          style="color: var(--muted-color); margin: 0;"),
        style="margin-bottom: 2rem;"
    )

