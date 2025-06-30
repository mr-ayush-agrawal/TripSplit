from fasthtml.common import *
from client.static.user.dropdown import dropdown_styles
from client.components.navbar import dashboard_nav
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
            # Logout Modal
            Div(
                Div(
                    Article(
                        Header(
                            H3("Confirm Logout", style="margin: 0; text-align: center;")
                        ),
                        P("Are you sure you want to logout?", style="text-align: center; margin: 1.5rem 0;"),
                        Footer(
                            Div(
                                Button("Cancel", onclick="hideLogoutModal()", cls="outline", style="margin-right: 1rem;"),
                                A("Logout", href="/user/logout", role="button", style="background: #dc3545; border-color: #dc3545;"),
                                style="text-align: center;"
                            )
                        )
                    ),
                    style="max-width: 400px; margin: 0 auto; position: relative; top: 50%; transform: translateY(-50%);"
                ),
                id="logoutModal",
                style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999;",
                onclick="event.target === this && hideLogoutModal()"
            ),
            Script("""
                function showLogoutModal() {
                    document.getElementById('logoutModal').style.display = 'block';
                }
                
                function hideLogoutModal() {
                    document.getElementById('logoutModal').style.display = 'none';
                }
                
                // Close modal on Escape key
                document.addEventListener('keydown', function(e) {
                    if (e.key === 'Escape') {
                        hideLogoutModal();
                    }
                });
            """),
            style="display: flex; flex-direction: column; min-height: 100vh;"
        )
    )
