from fasthtml.common import *

def auth_layout(title, content):
    return Html(
        Head(
            Title(f"{title} - SplitWise"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"),
            Link(rel="stylesheet", href="/static/style.css")
        ),
        Body(
            Main(
                Div(
                    Article(
                        Header(H2("SplitWise", style="text-align: center; margin-bottom: .6rem;")),
                        content
                    ),
                    style="max-width: 400px; margin: 2rem auto;"
                )
            )
        )
    )