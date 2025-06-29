from fasthtml.common import *

def feature_card(icon, title, description):
    return Article(
        Header(
            H3(f"{icon} {title}", style="text-align: center;")
        ),
        P(description, style="text-align: center;")
    )

