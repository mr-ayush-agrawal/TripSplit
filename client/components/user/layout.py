from fasthtml.common import *
from client.static.user.dropdown import dropdown_styles
from client.components.navbar import dashboard_nav
from client.components.auth.logout_model import logout_modal
from client.components import FOOTER_CONTENT

def dashboard_layout( content, title = 'Welcome', username="User"):
    """Base layout for dashboard pages"""
    return Html(
        Head(
            Title(f"{title} - SplitWise"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"),
            Link(rel="stylesheet", href="/client/static/style.css"),
            Script(src="https://unpkg.com/htmx.org@1.9.10"),
            dropdown_styles()
        ),
        Body(
            Header(dashboard_nav(user_name=username)),
            Main(content, cls="container", style="min-height: calc(100vh - 140px);"),
            Footer(
                Small(FOOTER_CONTENT),
                cls="container",
                style="text-align: center; padding: 2rem 0; margin-top: auto;"
            ),
            logout_modal(),
            Script("""
                function showLogoutModal() {
                    document.getElementById('logoutModal').style.display = 'block';
                }

                function hideLogoutModal() {
                    document.getElementById('logoutModal').style.display = 'none';
                }

                document.addEventListener('keydown', function(e) {
                    if (e.key === 'Escape') hideLogoutModal();
                });
            """),
            style="display: flex; flex-direction: column; min-height: 100vh;"
        )
    )
