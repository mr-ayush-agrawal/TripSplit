from fasthtml.common import *

def auth_layout(title, content, script = None):
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
                        content
                    ),
                    style="max-width: 600px; margin: 2rem auto;"
                )
            ),
            script
        )
    )
