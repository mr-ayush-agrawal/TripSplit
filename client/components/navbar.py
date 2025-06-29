from fasthtml.common import *

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
                Li(Strong(A("SplitWise", href="/", style="text-decoration: none;")))
            ),
            buttons,
            style='height : 25px'
        ),
        cls="container"
    )
    
    return nav_bar


# def dashboard_nav(user_name: str = "User"):
#     """Navigation for authenticated users"""
#     return Div(
#         Div(
#             H1("SplitWise", cls="text-3xl font-bold text-blue-600"),
#             Div(
#                 Span(f"Welcome, {user_name}", cls="text-gray-700 mr-4"),
#                 A("Dashboard", href="/dashboard", cls=f"text-blue-600 {BUTTON_SMALL} mr-2 hover:underline"),
#                 A("Groups", href="/groups", cls=f"text-blue-600 {BUTTON_SMALL} mr-2 hover:underline"),
#                 A("Logout", href="/logout", cls=f"bg-red-500 text-white {BUTTON_SMALL} hover:bg-red-600"),
#                 cls="flex items-center"
#             ),
#             cls=NAV_FLEX
#         ),
#         cls=NAV_CONTAINER
#     )