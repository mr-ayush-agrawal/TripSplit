from fasthtml.common import *
from client.components import APP_NAME

def navbar(show_auth_buttons=True):
    """Main navigation bar"""
    buttons = ""
    if show_auth_buttons:
        buttons = Ul(
            Li(A("Login", href="/user/login", role="button", cls="outline")),
            Li(A("Sign Up", href="/user/signup", role="button"))
        )

    nav_bar = Div(
        Nav(
            Ul(
                Li(Strong(A(APP_NAME, href="/", style="text-decoration: none;")))
            ),
            buttons,
            style='height : 25px'
        ),
        cls="container"
    )
    
    return nav_bar


def dashboard_nav(user_name: str = "User"):
    """Navigation for authenticated users"""
    return Div(
        Nav(
            Ul(
                Li(Strong(A(APP_NAME, href="/user/", style="text-decoration: none;")))
            ),
            Ul(
                Li(
                    Details(
                        Summary(
                            user_name,
                            style="cursor: pointer; padding: 0.5rem 1rem; border-radius: 0.5rem; background: var(--primary); color: white;"
                        ),
                        Ul(
                            Li(A("Profile", href="/user/profile", style="cursor: pointer;")),
                            Li(A("Logout", onclick="showLogoutModal()", style="cursor: pointer;"))  # ✅ changed
                        ),
                        cls="dropdown",
                        style="position: relative;"
                    )
                )
            ),
            style='height: 60px; align-items: center;'
        ),
        cls="container"
    )