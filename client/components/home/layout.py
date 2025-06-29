from fasthtml.common import *
from client.components.navbar import navbar

def home_base_layout(title, content, nav_auth_button = True):
    return Html(
        Head(
            Title(f"{title} - SplitWise"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"),
            Link(rel="stylesheet", href="/static/style.css")
        ),
        Body(
            Header(navbar(show_auth_buttons=nav_auth_button )),
            Main(content, cls="container"),
            Footer(
                Small("© 2025 SplitWise. Built with FastHTML."),
                cls="container"
            )
        )
    )




def hero_section():
    return Section(
        Div(
            H1("Split Expenses with Friends", style="text-align: center; font-size: 2.5rem; margin-bottom: 1rem;"),
            P("Track shared expenses and settle up with friends easily. No more awkward money conversations.", 
              style="text-align: center; font-size: 1.2rem; margin-bottom: 2rem;"),
            Div(
                A("Get Started", href="/signup", role="button"),
                A("Learn More", href="#features", role="button", cls="outline", style="margin-left: 1rem;"),
                style="text-align: center;"
            ),
            style="max-width: 800px; margin: 0 auto; padding: 4rem 0;"
        ),
        style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;"
    )