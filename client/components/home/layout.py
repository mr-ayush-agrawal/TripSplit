from fasthtml.common import *
from client.components.navbar import navbar
from client.components import FOOTER_CONTENT
from client.components.footer import dashboard_footer

def home_base_layout(title, content, nav_auth_button = True):
    return Html(
        Head(
            Title(f"{title} - Nishka"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"),
            Link(rel="stylesheet", href="client/static/style.css")
        ),
        Body(
            Header(navbar(show_auth_buttons=nav_auth_button)),
            Main(content, cls="container"),
            dashboard_footer()
        )
    )


def hero_section():
    return Section(
        Div(
            H1("Split Expenses with Friends", style="text-align: center; font-size: 2.5rem; margin-bottom: 1rem;"),
            P("Track shared expenses and settle up with friends easily. No more awkward money conversations.", 
              style="text-align: center; font-size: 1.2rem; margin-bottom: 2rem;"),
            Div(
                A("Get Started", href="/user/signup", role="button"),
                A("Learn More", href="#features", role="button", cls="outline", style="margin-left: 1rem;"),
                style="text-align: center;"
            ),
            style="max-width: 800px; margin: 0 auto; padding: 4rem 0;"
        ),
        style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;"
    )

def feedback_layout(title):
    return Html(
        Head(
            Title(f"{title} - Nishka"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"),
            Link(rel="stylesheet", href="/client/static/style.css")
        ),
        Body(
            Main(
                Div(
                    Article(
                        Header(H2("Nishka", style="text-align: center; margin-bottom: .6rem;")),
                        feedback_form()
                    ),
                    style="max-width: 600px; margin: 2rem auto;"
                )
            ),
        )
    )

def feedback_form():
    return Form(
        H2("Feedback"),
        Label("Title"),
        Input(type="text", name="title", placeholder="Enter the Title / Topic", required=True),
        Label("Description"),
        Input(type="text", name="description", placeholder="Describe your feedback", required=True),
        Button("Send Feedback", type="submit", cls="contrast"),
        method="post",
        action="/feedback"
    )