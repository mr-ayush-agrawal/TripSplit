from fasthtml.common import *
from client.components import FOOTER_CONTENT

def dashboard_footer():
    return Footer(
        Div(
            Hr(),
            Div(
                Small(FOOTER_CONTENT),
                Small(
                    A("Feedback", href="/feedback", style="margin-right: 1rem;"),
                    # A("Privacy Policy", href="/privacy", style="margin-left: 1rem;"),
                    # A("Terms of Service", href="/terms", style="margin-left: 1rem;"),
                    style="float: right;"
                ),
                style="display: flex; justify-content: space-between; align-items: center;"
            ),
            cls="container"
        ),
        style="margin-top: auto; padding: 2rem 0;"
    )